from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from app.core.database import Base


class User(Base):
    """Matches FarmForward_Database_Schema section 2.2"""
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, index=True)  # FARMER / BUYER / ADMIN
    location = Column(String(255), nullable=False)
    latitude = Column(Numeric(10, 7), nullable=True)
    longitude = Column(Numeric(10, 7), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
