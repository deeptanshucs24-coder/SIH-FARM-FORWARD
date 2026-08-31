from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.dependencies import get_db, require_role, get_current_user_optional
from app.schemas.buyer import BuyerOut, BuyerRequirementCreate, BuyerRequirementOut
from app.crud.buyer import list_buyers, get_buyer_by_user_id, create_requirement
from app.crud.crop import get_crop_by_id

router = APIRouter(prefix="/api", tags=["Buyers"])


@router.get(
    "/buyers",
    response_model=list[BuyerOut],
    summary="List buyers. Non-admin callers only ever see VERIFIED buyers, "
            "regardless of what verification_status filter they pass - matches "
            "the documented Buyer Verification flow (pending/rejected buyers "
            "must never be exposed to farmers as if they were verified).",
)
def get_buyers(
    verification_status: str | None = Query(None, pattern="^(PENDING|VERIFIED|REJECTED)$"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user_optional),
):
    if current_user and current_user.role == "ADMIN":
        return list_buyers(db, verification_status)
    # Farmers, buyers, and anonymous callers: always locked to VERIFIED only.
    return list_buyers(db, "VERIFIED")


@router.post("/buyer/requirements", response_model=BuyerRequirementOut, status_code=201)
def post_requirement(
    payload: BuyerRequirementCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("BUYER")),
):
    if not get_crop_by_id(db, payload.crop_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop not found")

    buyer_profile = get_buyer_by_user_id(db, current_user.user_id)
    if not buyer_profile:
        # Shouldn't normally happen - a buyer profile is auto-created at registration.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No buyer profile found for this account")
    return create_requirement(db, buyer_profile.buyer_id, payload)
