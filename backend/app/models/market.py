import uuid
from sqlalchemy import Column, String, Float
from app.core.database import Base
from app.core.types import GUID


class Market(Base):
    """Matches M3's schema.sql exactly: markets table. No created_at column -
    M3's real DDL doesn't have one."""
    __tablename__ = "markets"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    state = Column(String(80), nullable=True)
    district = Column(String(80), nullable=True)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)
