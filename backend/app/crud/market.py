import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc, func

from app.models.market import Market
from app.models.market_price import MarketPrice


def list_markets(db: Session) -> list[Market]:
    return db.query(Market).order_by(Market.market_name).all()


def get_market_by_id(db: Session, market_id: int) -> Market | None:
    return db.query(Market).filter(Market.market_id == market_id).first()


def get_current_price(db: Session, crop_id: int, market_id: int | None = None) -> list[MarketPrice]:
    """Returns exactly ONE row per market: the most recent price_date on
    record for that crop at that market. This is deliberately NOT the same
    as get_price_history - a bug in an earlier version returned every
    historical row here, which this subquery-based approach fixes."""
    latest_per_market = (
        db.query(
            MarketPrice.market_id,
            func.max(MarketPrice.price_date).label("max_date"),
        )
        .filter(MarketPrice.crop_id == crop_id)
    )
    if market_id:
        latest_per_market = latest_per_market.filter(MarketPrice.market_id == market_id)
    latest_per_market = latest_per_market.group_by(MarketPrice.market_id).subquery()

    return (
        db.query(MarketPrice)
        .join(
            latest_per_market,
            (MarketPrice.market_id == latest_per_market.c.market_id)
            & (MarketPrice.price_date == latest_per_market.c.max_date),
        )
        .filter(MarketPrice.crop_id == crop_id)
        .order_by(MarketPrice.market_id)
        .all()
    )


def get_price_history(db: Session, crop_id: int, market_id: int | None, days: int) -> list[MarketPrice]:
    since = datetime.date.today() - datetime.timedelta(days=days)
    query = db.query(MarketPrice).filter(
        MarketPrice.crop_id == crop_id,
        MarketPrice.price_date >= since,
    )
    if market_id:
        query = query.filter(MarketPrice.market_id == market_id)
    return query.order_by(MarketPrice.price_date).all()


def get_latest_price_for_market(db: Session, crop_id: int, market_id: int) -> MarketPrice | None:
    return (
        db.query(MarketPrice)
        .filter(MarketPrice.crop_id == crop_id, MarketPrice.market_id == market_id)
        .order_by(desc(MarketPrice.price_date))
        .first()
    )
