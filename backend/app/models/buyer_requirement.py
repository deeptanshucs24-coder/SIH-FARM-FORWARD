import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from app.core.database import Base
from app.core.types import GUID


class BuyerRequirement(Base):
    """Matches M3's schema.sql exactly: buyers_requirements table.
    NOTE: no separate 'buyers' table exists - a buyer is just a `users` row
    with role='buyer'. This also means the previously-flagged
    'buyers.user_id -> users.id' pending decision is now moot: there's
    nothing to link, since buyers ARE users. No offered_price/status/
    expires_at columns either - M3's real table is minimal."""
    __tablename__ = "buyers_requirements"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    buyer_id = Column(GUID(), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    crop_name = Column(String(80), nullable=False, index=True)
    quantity_needed_kg = Column(Integer, nullable=True)
