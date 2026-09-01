from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db, require_role, get_current_user
from app.schemas.crop_listing import CropListingCreate, CropListingUpdate, CropListingOut
from app.schemas.match import MatchOut, MatchStatusUpdate
from app.crud.crop_listing import (
    create_listing, get_listings_by_farmer, get_listing_by_id,
    update_listing, delete_listing,
)
from app.crud.match import create_match, get_matches_for_listing, get_match_by_id, update_match_status

router = APIRouter(prefix="/api", tags=["Crop Listings"])


def _get_owned_listing_or_403(db: Session, listing_id, current_user):
    """404 if it doesn't exist, 403 if it exists but belongs to someone
    else. Ownership always comes from the JWT, never a client-supplied id."""
    listing = get_listing_by_id(db, listing_id)
    if not listing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop listing not found")
    if listing.farmer_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not own this crop listing")
    return listing


@router.post(
    "/farmer/produce",
    response_model=CropListingOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a crop listing (farmer only)",
)
def add_listing(
    payload: CropListingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("farmer")),
):
    return create_listing(db, current_user.id, payload)


@router.get(
    "/farmer/produce",
    response_model=list[CropListingOut],
    summary="List your own crop listings (farmer only)",
)
def list_my_listings(
    db: Session = Depends(get_db),
    current_user=Depends(require_role("farmer")),
):
    return get_listings_by_farmer(db, current_user.id)


@router.get(
    "/farmer/produce/{listing_id}",
    response_model=CropListingOut,
    summary="Read one of your own crop listings",
)
def get_my_listing(
    listing_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return _get_owned_listing_or_403(db, listing_id, current_user)


@router.patch(
    "/farmer/produce/{listing_id}",
    response_model=CropListingOut,
    summary="Partially update one of your own crop listings",
)
def update_my_listing(
    listing_id: str,
    payload: CropListingUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("farmer")),
):
    listing = _get_owned_listing_or_403(db, listing_id, current_user)
    return update_listing(db, listing, payload)


@router.delete(
    "/farmer/produce/{listing_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete one of your own crop listings",
)
def delete_my_listing(
    listing_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("farmer")),
):
    listing = _get_owned_listing_or_403(db, listing_id, current_user)
    delete_listing(db, listing)
    return None


# --- Buyer interest / matches (backs M3's `matches` table) ---
# Documented flow (Master Plan): Listed -> Buyer Interested -> Deal Confirmed

@router.post(
    "/farmer/produce/{listing_id}/interest",
    response_model=MatchOut,
    status_code=status.HTTP_201_CREATED,
    summary="Buyer expresses interest in a listing (buyer only)",
    description="Creates a match (status=pending). If the listing is currently "
                "'listed', its status is bumped to 'interested'.",
)
def express_interest(
    listing_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("buyer")),
):
    listing = get_listing_by_id(db, listing_id)
    if not listing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop listing not found")

    match = create_match(db, listing_id=listing.id, buyer_id=current_user.id)
    if listing.status == "listed":
        listing.status = "interested"
        db.commit()
    return match


@router.get(
    "/farmer/produce/{listing_id}/matches",
    response_model=list[MatchOut],
    summary="View interested buyers for one of your own listings (farmer only)",
)
def list_listing_matches(
    listing_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("farmer")),
):
    listing = _get_owned_listing_or_403(db, listing_id, current_user)
    return get_matches_for_listing(db, listing.id)


@router.patch(
    "/farmer/produce/{listing_id}/matches/{match_id}",
    response_model=MatchOut,
    summary="Accept or reject a buyer's interest (farmer, owner only)",
    description="Accepting also sets the listing's status to 'confirmed'.",
)
def update_match(
    listing_id: str,
    match_id: str,
    payload: MatchStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("farmer")),
):
    listing = _get_owned_listing_or_403(db, listing_id, current_user)
    match = get_match_by_id(db, match_id)
    if not match or str(match.listing_id) != str(listing.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found for this listing")

    updated = update_match_status(db, match, payload.status)
    if payload.status == "accepted":
        listing.status = "confirmed"
        db.commit()
    return updated
