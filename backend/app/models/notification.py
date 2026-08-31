from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, DateTime, func
from app.core.database import Base


class Notification(Base):
    """Matches FarmForward_Database_Schema section 2.12"""
    __tablename__ = "notifications"

    notification_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False, index=True)
    type = Column(String(40), nullable=False)
    title = Column(String(150), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
