from sqlalchemy.orm import Session

from app.models.user import User
from app.models.buyer import Buyer
from app.schemas.user import UserRegister, UserUpdate
from app.core.security import hash_password


def get_user_by_phone(db: Session, phone: str) -> User | None:
    return db.query(User).filter(User.phone == phone).first()


def get_user_by_id(db: Session, user_id) -> User | None:
    try:
        uid = int(user_id)
    except (ValueError, TypeError):
        return None
    return db.query(User).filter(User.user_id == uid).first()


def create_user(db: Session, payload: UserRegister) -> User:
    user = User(
        name=payload.name,
        phone=payload.phone,
        password_hash=hash_password(payload.password),
        role=payload.role,
        location=payload.location,
        latitude=payload.latitude,
        longitude=payload.longitude,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # If registering as a buyer, auto-create a linked buyer profile (PENDING
    # verification) so they can post requirements right away.
    # NOTE: this link (buyers.user_id) is an extension beyond the official
    # schema doc - flagged for team confirmation, see models/buyer.py.
    if payload.role == "BUYER":
        buyer = Buyer(
            user_id=user.user_id,
            buyer_name=payload.name,
            location=payload.location,
            latitude=payload.latitude,
            longitude=payload.longitude,
            contact=payload.phone,
            verification_status="PENDING",
        )
        db.add(buyer)
        db.commit()

    return user


def update_user(db: Session, user: User, payload: UserUpdate) -> User:
    updates = payload.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user
