from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from app.core.database import Base


class Buyer(Base):
    """Matches FarmForward_Database_Schema section 2.7.

    NOTE (flag for team): the schema doc lists 'buyers' as a separate entity from
    'users', even though users.role can also be BUYER. We link buyers to a user
    account via user_id so a buyer can log in and manage their own requirements -
    this FK is NOT in the original schema doc and needs team confirmation.
    """
    __tablename__ = "buyers"

    buyer_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True, unique=True)  # extension, confirm with team
    buyer_name = Column(String(150), nullable=False)
    location = Column(String(255), nullable=False, index=True)
    latitude = Column(Numeric(10, 7), nullable=True)
    longitude = Column(Numeric(10, 7), nullable=True)
    contact = Column(String(100), nullable=False)
    verification_status = Column(String(20), nullable=False, default="PENDING", index=True)  # PENDING/VERIFIED/REJECTED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
