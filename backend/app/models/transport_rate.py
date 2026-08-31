from sqlalchemy import Column, Integer, Numeric, String, Date, DateTime, func
from app.core.database import Base


class TransportRate(Base):
    """Matches FarmForward_Database_Schema section 2.10"""
    __tablename__ = "transport_rates"

    transport_rate_id = Column(Integer, primary_key=True, autoincrement=True)
    rate_per_km_unit = Column(Numeric(12, 2), nullable=False)
    unit_name = Column(String(30), nullable=False)  # e.g. "per quintal per km"
    effective_from = Column(Date, nullable=False)
    effective_to = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
