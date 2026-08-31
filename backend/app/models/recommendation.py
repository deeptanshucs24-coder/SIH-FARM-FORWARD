from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, DateTime, func
from app.core.database import Base


class Recommendation(Base):
    """Matches FarmForward_Database_Schema section 2.11"""
    __tablename__ = "recommendations"

    recommendation_id = Column(Integer, primary_key=True, autoincrement=True)
    farmer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False, index=True)
    produce_id = Column(Integer, ForeignKey("farmer_produce.produce_id"), nullable=True)
    crop_id = Column(Integer, ForeignKey("crops.crop_id"), nullable=False, index=True)
    quantity = Column(Numeric(12, 2), nullable=False)
    recommended_type = Column(String(20), nullable=False)  # MARKET / BUYER
    recommended_market_id = Column(Integer, ForeignKey("markets.market_id"), nullable=True)
    recommended_buyer_id = Column(Integer, ForeignKey("buyers.buyer_id"), nullable=True)
    expected_price = Column(Numeric(12, 2), nullable=False)
    transport_cost = Column(Numeric(12, 2), nullable=False)
    other_cost = Column(Numeric(12, 2), nullable=False, default=0)
    expected_profit = Column(Numeric(12, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
