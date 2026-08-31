from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date, DateTime, func, Index
from app.core.database import Base


class FarmerProduce(Base):
    """Matches FarmForward_Database_Schema section 2.4"""
    __tablename__ = "farmer_produce"

    produce_id = Column(Integer, primary_key=True, autoincrement=True)
    farmer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False, index=True)
    crop_id = Column(Integer, ForeignKey("crops.crop_id"), nullable=False, index=True)
    quantity = Column(Numeric(12, 2), nullable=False)
    available_date = Column(Date, nullable=False)
    expected_price = Column(Numeric(12, 2), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        Index("ix_produce_crop_date", "crop_id", "available_date"),
    )
