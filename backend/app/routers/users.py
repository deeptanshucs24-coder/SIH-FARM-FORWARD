from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.schemas.user import UserOut, UserUpdate
from app.crud.user import update_user

router = APIRouter(prefix="/api", tags=["User Profile"])


@router.get("/users/me", response_model=UserOut, summary="Get your own profile (from JWT)")
def get_my_profile(current_user=Depends(get_current_user)):
    return current_user


@router.put("/users/me", response_model=UserOut, summary="Update your own profile (from JWT)")
def update_my_profile(
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return update_user(db, current_user, payload)
