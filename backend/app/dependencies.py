from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.security import decode_access_token
from app.crud.user import get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")
oauth2_scheme_optional = OAuth2PasswordBearer(tokenUrl="/api/login", auto_error=False)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None or "sub" not in payload:
        raise credentials_exception

    user = get_user_by_id(db, payload["sub"])
    if user is None:
        raise credentials_exception
    return user


def get_current_user_optional(
    token: Optional[str] = Depends(oauth2_scheme_optional), db: Session = Depends(get_db)
):
    """Like get_current_user, but returns None instead of raising 401 when no
    token is given. Used by endpoints that behave differently for logged-in
    vs anonymous callers (e.g. GET /api/buyers) without requiring login."""
    if not token:
        return None
    payload = decode_access_token(token)
    if payload is None or "sub" not in payload:
        return None
    return get_user_by_id(db, payload["sub"])


def require_role(*allowed_roles: str):
    """Usage: Depends(require_role('FARMER', 'ADMIN'))"""

    def checker(user=Depends(get_current_user)):
        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires role: {', '.join(allowed_roles)}",
            )
        return user

    return checker
