from sqlalchemy.orm import Session
from app.models.price_prediction import PricePrediction


def save_prediction(db: Session, **fields) -> PricePrediction:
    prediction = PricePrediction(**fields)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction
