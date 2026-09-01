from sqlalchemy.orm import Session
from app.models.user import User
from app.models.buyer_requirement import BuyerRequirement
from app.schemas.buyer import BuyerRequirementCreate


def list_buyers(db: Session) -> list[User]:
    """A buyer is just a users row with role='buyer' - M3's schema has no
    separate buyers table, so there is no verification_status to filter on.
    See README 'Flag for team'."""
    return db.query(User).filter(User.role == "buyer").order_by(User.name).all()


def create_requirement(db: Session, buyer_id, payload: BuyerRequirementCreate) -> BuyerRequirement:
    req = BuyerRequirement(
        buyer_id=buyer_id,
        crop_name=payload.crop_name,
        quantity_needed_kg=payload.quantity_needed_kg,
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return req
