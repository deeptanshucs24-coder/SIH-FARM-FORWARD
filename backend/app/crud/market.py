import uuid
import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc, func

from app.models.market import Market
from app.models.market_price import MarketPrice


def list_markets(db: Session) -> list[Market]:
    return db.query(Market).order_by(Market.name).all()


def get_market_by_id(db: Session, market_id) -> Market | None:
    try:
        mid = uuid.UUID(str(market_id))
    except (ValueError, TypeError):
        return None
    return db.query(Market).filter(Market.id == mid).first()


def get_current_price(db: Session, crop_name: str, market_id=None) -> list[MarketPrice]:
    """Returns exactly ONE row per market: the most recent date on record
    for that crop_name at that market (case-insensitive match on crop_name,
    since Postgres/SQLite both support LOWER())."""
    latest_per_market = (
        db.query(
            MarketPrice.market_id,
            func.max(MarketPrice.date).label("max_date"),
        )
        .filter(func.lower(MarketPrice.crop_name) == crop_name.lower())
    )
    if market_id:
        latest_per_market = latest_per_market.filter(MarketPrice.market_id == market_id)
    latest_per_market = latest_per_market.group_by(MarketPrice.market_id).subquery()

    return (
        db.query(MarketPrice)
        .join(
            latest_per_market,
            (MarketPrice.market_id == latest_per_market.c.market_id)
            & (MarketPrice.date == latest_per_market.c.max_date),
        )
        .filter(func.lower(MarketPrice.crop_name) == crop_name.lower())
        .order_by(MarketPrice.market_id)
        .all()
    )


def get_price_history(db: Session, crop_name: str, market_id, days: int) -> list[MarketPrice]:
    since = datetime.date.today() - datetime.timedelta(days=days)
    query = db.query(MarketPrice).filter(
        func.lower(MarketPrice.crop_name) == crop_name.lower(),
        MarketPrice.date >= since,
    )
    if market_id:
        query = query.filter(MarketPrice.market_id == market_id)
    return query.order_by(MarketPrice.date).all()


def get_latest_price_for_market(db: Session, crop_name: str, market_id) -> MarketPrice | None:
    return (
        db.query(MarketPrice)
        .filter(func.lower(MarketPrice.crop_name) == crop_name.lower(), MarketPrice.market_id == market_id)
        .order_by(desc(MarketPrice.date))
        .first()
    )


def list_distinct_crop_names(db: Session) -> list[str]:
    """M3's schema has no 'crops' reference table - this derives the
    'supported crops' list dynamically from what's actually in market_prices
    (falling back to crop_listings for anything not yet priced anywhere)."""
    from app.models.crop_listing import CropListing
    price_crops = {row[0] for row in db.query(MarketPrice.crop_name).distinct().all()}
    listing_crops = {row[0] for row in db.query(CropListing.crop_name).distinct().all()}
    return sorted(price_crops | listing_crops, key=str.lower)
