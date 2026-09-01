import uuid
from sqlalchemy import Column, String, Float, Boolean, DateTime, ForeignKey, func
from app.core.database import Base
from app.core.types import GUID


class PricePrediction(Base):
    """Matches M3's schema.sql exactly: price_predictions table.
    Field names (predicted_price, range_min, range_max, confidence,
    distress_flag) match the Master Plan's Part 4.1 M4 output example
    exactly - this IS the documented M4 contract, not a guess."""
    __tablename__ = "price_predictions"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    crop_name = Column(String(80), nullable=False, index=True)
    market_id = Column(GUID(), ForeignKey("markets.id", ondelete="CASCADE"), nullable=True, index=True)
    predicted_price = Column(Float, nullable=True)
    range_min = Column(Float, nullable=True)
    range_max = Column(Float, nullable=True)
    confidence = Column(Float, nullable=True)
    distress_flag = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, server_default=func.now())
