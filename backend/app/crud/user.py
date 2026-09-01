import uuid
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRegister, UserUpdate
from app.core.security import hash_password


def get_user_by_phone(db: Session, phone: str) -> User | None:
    return db.query(User).filter(User.phone == phone).first()


def get_user_by_id(db: Session, user_id) -> User | None:
    try:
        uid = uuid.UUID(str(user_id))
    except (ValueError, TypeError):
        return None
    return db.query(User).filter(User.id == uid).first()


def create_user(db: Session, payload: UserRegister) -> User:
    user = User(
        name=payload.name,
        phone=payload.phone,
        password_hash=hash_password(payload.password),
        role=payload.role,
        language_pref=payload.language_pref,
        location_lat=payload.latitude,
        location_lng=payload.longitude,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    # NOTE: no separate 'buyers' table exists in M3's schema, so there is
    # nothing to auto-link here - a buyer is just this same users row.
    return user


def update_user(db: Session, user: User, payload: UserUpdate) -> User:
    updates = payload.model_dump(exclude_unset=True, by_alias=False)
    # Translate friendly API field names to M3's actual column names.
    if "latitude" in updates:
        user.location_lat = updates.pop("latitude")
    if "longitude" in updates:
        user.location_lng = updates.pop("longitude")
    for field, value in updates.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user
