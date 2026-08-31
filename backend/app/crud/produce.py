from sqlalchemy.orm import Session
from app.models.farmer_produce import FarmerProduce
from app.schemas.produce import FarmerProduceCreate, FarmerProduceUpdate


def create_produce(db: Session, farmer_id: int, payload: FarmerProduceCreate) -> FarmerProduce:
    produce = FarmerProduce(
        farmer_id=farmer_id,
        crop_id=payload.crop_id,
        quantity=payload.quantity,
        available_date=payload.available_date,
        expected_price=payload.expected_price,
    )
    db.add(produce)
    db.commit()
    db.refresh(produce)
    return produce


def get_produce_by_farmer(db: Session, farmer_id: int) -> list[FarmerProduce]:
    return (
        db.query(FarmerProduce)
        .filter(FarmerProduce.farmer_id == farmer_id)
        .order_by(FarmerProduce.created_at.desc())
        .all()
    )


def get_produce_by_id(db: Session, produce_id: int) -> FarmerProduce | None:
    return db.query(FarmerProduce).filter(FarmerProduce.produce_id == produce_id).first()


def update_produce(db: Session, produce: FarmerProduce, payload: FarmerProduceUpdate) -> FarmerProduce:
    updates = payload.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(produce, field, value)
    db.commit()
    db.refresh(produce)
    return produce


def delete_produce(db: Session, produce: FarmerProduce) -> None:
    db.delete(produce)
    db.commit()
