import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, func, CheckConstraint
from app.core.database import Base
from app.core.types import GUID


class Match(Base):
    """Matches M3's schema.sql exactly: matches table. Connects a buyer's
    interest to a specific crop_listing - this is the mechanism behind the
    Master Plan's documented flow: 'Farmer selects a market/buyer -> buyer
    sees the listing -> expresses interest ... Farmer tracks status:
    Listed -> Buyer Interested -> Deal Confirmed'."""
    __tablename__ = "matches"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    listing_id = Column(GUID(), ForeignKey("crop_listings.id", ondelete="CASCADE"), nullable=False, index=True)
    buyer_id = Column(GUID(), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    status = Column(String(10), nullable=False, default="pending")  # pending/accepted/rejected
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("status IN ('pending','accepted','rejected')", name="matches_status_check"),
    )
