from sqlalchemy import Column, Integer, String, DateTime, func, Index
from app.core.database import Base


class Crop(Base):
    """Matches FarmForward_Database_Schema section 2.3"""
    __tablename__ = "crops"

    crop_id = Column(Integer, primary_key=True, autoincrement=True)
    crop_name = Column(String(100), nullable=False, index=True)
    variety = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_crops_name_variety", "crop_name", "variety"),
    )
