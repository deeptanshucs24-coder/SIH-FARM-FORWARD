from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class UserRegister(BaseModel):
    name: str
    # Digits only, 10-15 chars - matches the project's phone-as-identifier convention.
    phone: str = Field(..., pattern=r"^[0-9]{10,15}$")
    password: str = Field(..., min_length=6)
    # ADMIN is intentionally excluded here - public self-registration must not
    # allow arbitrary admin creation (flagged by team review). Admin accounts
    # are created via scripts/create_admin.py until the team decides on a
    # proper admin workflow - see README "Flag for team".
    role: str = Field(..., pattern="^(FARMER|BUYER)$")
    location: str
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)


class UserLogin(BaseModel):
    phone: str
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    name: str
    phone: str
    role: str
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class UserUpdate(BaseModel):
    """For PUT /api/users/me. Deliberately excludes phone/password/role -
    those need their own dedicated, more careful flows (not in tonight's scope)."""
    name: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut
