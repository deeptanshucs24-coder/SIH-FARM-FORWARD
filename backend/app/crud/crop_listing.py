import uuid
from sqlalchemy.orm import Session

from app.models.crop_listing import CropListing
from app.schemas.crop_listing import CropListingCreate, CropListingUpdate


def create_listing(db: Session, farmer_id, payload: CropListingCreate) -> CropListing:
    listing = CropListing(
        farmer_id=farmer_id,
        crop_name=payload.crop_name,
        quantity_kg=payload.quantity_kg,
        grade=payload.grade,
        harvest_date=payload.harvest_date,
        status="listed",
    )
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing


def get_listings_by_farmer(db: Session, farmer_id) -> list[CropListing]:
    return (
        db.query(CropListing)
        .filter(CropListing.farmer_id == farmer_id)
        .order_by(CropListing.created_at.desc())
        .all()
    )


def get_listing_by_id(db: Session, listing_id) -> CropListing | None:
    try:
        lid = uuid.UUID(str(listing_id))
    except (ValueError, TypeError):
        return None
    return db.query(CropListing).filter(CropListing.id == lid).first()


def update_listing(db: Session, listing: CropListing, payload: CropListingUpdate) -> CropListing:
    updates = payload.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(listing, field, value)
    db.commit()
    db.refresh(listing)
    return listing


def delete_listing(db: Session, listing: CropListing) -> None:
    db.delete(listing)
    db.commit()


def list_open_listings(db: Session, crop_name: str | None = None) -> list[CropListing]:
    """Buyer-side browse: listings still open (status='listed')."""
    query = db.query(CropListing).filter(CropListing.status == "listed")
    if crop_name:
        query = query.filter(CropListing.crop_name.ilike(f"%{crop_name}%"))
    return query.order_by(CropListing.created_at.desc()).all()
