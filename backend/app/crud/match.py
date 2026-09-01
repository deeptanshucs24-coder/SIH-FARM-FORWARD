import uuid
from sqlalchemy.orm import Session
from app.models.match import Match


def create_match(db: Session, listing_id, buyer_id) -> Match:
    match = Match(listing_id=listing_id, buyer_id=buyer_id, status="pending")
    db.add(match)
    db.commit()
    db.refresh(match)
    return match


def get_matches_for_listing(db: Session, listing_id) -> list[Match]:
    return db.query(Match).filter(Match.listing_id == listing_id).order_by(Match.created_at.desc()).all()


def get_match_by_id(db: Session, match_id) -> Match | None:
    try:
        mid = uuid.UUID(str(match_id))
    except (ValueError, TypeError):
        return None
    return db.query(Match).filter(Match.id == mid).first()


def update_match_status(db: Session, match: Match, status: str) -> Match:
    match.status = status
    db.commit()
    db.refresh(match)
    return match
