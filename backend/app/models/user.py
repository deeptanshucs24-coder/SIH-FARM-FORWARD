import uuid
from sqlalchemy import Column, String, Float, DateTime, func, CheckConstraint
from app.core.database import Base
from app.core.types import GUID


class User(Base):
    """Matches M3's schema.sql exactly: users table."""
    __tablename__ = "users"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(120), nullable=False)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(10), nullable=False)  # 'farmer' / 'buyer' / 'admin' - lowercase, matches DB CHECK
    language_pref = Column(String(5), nullable=True, default="en")  # 'en' / 'hi'
    location_lat = Column(Float, nullable=True)
    location_lng = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("role IN ('farmer','buyer','admin')", name="users_role_check"),
        CheckConstraint("language_pref IN ('en','hi')", name="users_language_pref_check"),
    )
