from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.user import UserRegister, UserLogin, TokenResponse, UserOut
from app.crud.user import get_user_by_phone, create_user
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/api", tags=["Authentication"])


@router.post(
    "/register",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new FARMER or BUYER account",
    description="Public self-registration is intentionally restricted to FARMER "
                "and BUYER - ADMIN accounts cannot be created through this endpoint "
                "(see scripts/create_admin.py). Returns a JWT immediately, no "
                "separate login step needed after registering.",
)
def register(payload: UserRegister, db: Session = Depends(get_db)):
    if get_user_by_phone(db, payload.phone):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Phone number already registered")

    user = create_user(db, payload)
    token = create_access_token(subject=str(user.user_id), extra_claims={"role": user.role})
    return TokenResponse(access_token=token, user=UserOut.model_validate(user))


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Log in with phone + password",
    description="Returns a JWT bearer token to use in the Authorization header "
                "(Authorization: Bearer <token>) for protected endpoints.",
)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_phone(db, payload.phone)
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid phone number or password",
        )
    token = create_access_token(subject=str(user.user_id), extra_claims={"role": user.role})
    return TokenResponse(access_token=token, user=UserOut.model_validate(user))
