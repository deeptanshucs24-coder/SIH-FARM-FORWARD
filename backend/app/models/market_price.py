from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date, DateTime, func, Index, UniqueConstraint, CheckConstraint
from app.core.database import Base


class MarketPrice(Base):
    """Matches FarmForward_Database_Schema section 2.6. Historical - never overwritten,
    one row per (market, crop, date)."""
    __tablename__ = "market_prices"

    price_id = Column(Integer, primary_key=True, autoincrement=True)
    market_id = Column(Integer, ForeignKey("markets.market_id"), nullable=False, index=True)
    crop_id = Column(Integer, ForeignKey("crops.crop_id"), nullable=False, index=True)
    price_date = Column(Date, nullable=False)
    min_price = Column(Numeric(12, 2), nullable=False)
    max_price = Column(Numeric(12, 2), nullable=False)
    average_price = Column(Numeric(12, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("market_id", "crop_id", "price_date", name="uq_market_crop_date"),
        CheckConstraint("min_price <= average_price", name="ck_min_le_avg"),
        CheckConstraint("average_price <= max_price", name="ck_avg_le_max"),
        Index("ix_prices_crop_date", "crop_id", "price_date"),
        Index("ix_prices_market_crop_date", "market_id", "crop_id", "price_date"),
    )
