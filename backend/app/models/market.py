from sqlalchemy import Column, Integer, String, Numeric, DateTime, func, Index
from app.core.database import Base


class Market(Base):
    """Matches FarmForward_Database_Schema section 2.5"""
    __tablename__ = "markets"

    market_id = Column(Integer, primary_key=True, autoincrement=True)
    market_name = Column(String(150), nullable=False)
    location = Column(String(255), nullable=False, index=True)
    latitude = Column(Numeric(10, 7), nullable=True)
    longitude = Column(Numeric(10, 7), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_markets_lat_lng", "latitude", "longitude"),
    )
