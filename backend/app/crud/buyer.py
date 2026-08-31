from sqlalchemy.orm import Session
from app.models.buyer import Buyer
from app.models.buyer_requirement import BuyerRequirement
from app.schemas.buyer import BuyerRequirementCreate


def list_buyers(db: Session, verification_status: str | None = None) -> list[Buyer]:
    query = db.query(Buyer)
    if verification_status:
        query = query.filter(Buyer.verification_status == verification_status)
    return query.order_by(Buyer.buyer_name).all()


def get_buyer_by_user_id(db: Session, user_id: int) -> Buyer | None:
    return db.query(Buyer).filter(Buyer.user_id == user_id).first()


def create_requirement(db: Session, buyer_id: int, payload: BuyerRequirementCreate) -> BuyerRequirement:
    req = BuyerRequirement(
        buyer_id=buyer_id,
        crop_id=payload.crop_id,
        required_quantity=payload.required_quantity,
        offered_price=payload.offered_price,
        status="OPEN",
        expires_at=payload.expires_at,
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return req
