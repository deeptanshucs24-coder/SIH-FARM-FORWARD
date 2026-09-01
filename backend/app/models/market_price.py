import uuid
from sqlalchemy import Column, String, Float, Date, ForeignKey, Index
from app.core.database import Base
from app.core.types import GUID


class MarketPrice(Base):
    """Matches M3's schema.sql exactly: market_prices table.
    A single price_per_quintal value - NOT min/max/average. No unique
    constraint on (market, crop, date) in M3's real DDL, so duplicate rows
    for the same day are technically possible (M3's ingestion script is
    expected to avoid this, but we don't enforce it at the DB level since
    M3's schema doesn't)."""
    __tablename__ = "market_prices"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    market_id = Column(GUID(), ForeignKey("markets.id", ondelete="CASCADE"), nullable=False, index=True)
    crop_name = Column(String(80), nullable=False, index=True)
    price_per_quintal = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    __table_args__ = (
        Index("idx_market_prices_lookup", "crop_name", "market_id", "date"),
    )
