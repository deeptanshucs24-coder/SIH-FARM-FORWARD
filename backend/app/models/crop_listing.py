import uuid
from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, func, CheckConstraint
from app.core.database import Base
from app.core.types import GUID


class CropListing(Base):
    """Matches M3's schema.sql exactly: crop_listings table.
    NOTE: crop is a free-text crop_name here, NOT a foreign key - M3's real
    schema has no separate 'crops' reference table."""
    __tablename__ = "crop_listings"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    farmer_id = Column(GUID(), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    crop_name = Column(String(80), nullable=False, index=True)
    quantity_kg = Column(Integer, nullable=False)
    grade = Column(String(5), nullable=True)  # e.g. A / B / C
    harvest_date = Column(Date, nullable=True)
    status = Column(String(12), nullable=False, default="listed")  # listed/interested/confirmed
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("status IN ('listed','interested','confirmed')", name="crop_listings_status_check"),
    )
