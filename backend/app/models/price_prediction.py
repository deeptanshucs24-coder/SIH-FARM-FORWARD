from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, Date, DateTime, func
from app.core.database import Base


class PricePrediction(Base):
    """Matches FarmForward_Database_Schema section 2.9"""
    __tablename__ = "price_predictions"

    prediction_id = Column(Integer, primary_key=True, autoincrement=True)
    crop_id = Column(Integer, ForeignKey("crops.crop_id"), nullable=False, index=True)
    market_id = Column(Integer, ForeignKey("markets.market_id"), nullable=False, index=True)
    prediction_date = Column(Date, nullable=False)
    target_date = Column(Date, nullable=False)
    predicted_price = Column(Numeric(12, 2), nullable=False)
    predicted_min_price = Column(Numeric(12, 2), nullable=True)
    predicted_max_price = Column(Numeric(12, 2), nullable=True)
    trend = Column(String(20), nullable=True)  # INCREASING / DECREASING / STABLE
    model_name = Column(String(80), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
