from sqlalchemy.orm import Session
from app.models.crop import Crop


def list_crops(db: Session) -> list[Crop]:
    return db.query(Crop).order_by(Crop.crop_name).all()


def get_crop_by_id(db: Session, crop_id: int) -> Crop | None:
    return db.query(Crop).filter(Crop.crop_id == crop_id).first()
