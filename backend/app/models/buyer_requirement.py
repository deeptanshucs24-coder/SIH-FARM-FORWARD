from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, DateTime, func, Index
from app.core.database import Base


class BuyerRequirement(Base):
    """Matches FarmForward_Database_Schema section 2.8"""
    __tablename__ = "buyer_requirements"

    requirement_id = Column(Integer, primary_key=True, autoincrement=True)
    buyer_id = Column(Integer, ForeignKey("buyers.buyer_id"), nullable=False, index=True)
    crop_id = Column(Integer, ForeignKey("crops.crop_id"), nullable=False, index=True)
    required_quantity = Column(Numeric(12, 2), nullable=False)
    offered_price = Column(Numeric(12, 2), nullable=True)
    status = Column(String(20), nullable=False, default="OPEN")  # OPEN / FULFILLED / EXPIRED / CANCELLED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        Index("ix_requirements_crop_status", "crop_id", "status"),
    )
