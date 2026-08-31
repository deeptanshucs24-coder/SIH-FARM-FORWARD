from sqlalchemy.orm import Session
from app.models.recommendation import Recommendation


def save_recommendation(db: Session, **fields) -> Recommendation:
    rec = Recommendation(**fields)
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec
