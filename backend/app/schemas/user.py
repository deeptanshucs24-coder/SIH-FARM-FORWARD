import uuid
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class UserRegister(BaseModel):
    name: str
    phone: str = Field(..., pattern=r"^[0-9]{10,15}$")
    password: str = Field(..., min_length=6)
    # ADMIN still excluded from public self-registration (unchanged decision).
    # Lowercase to match M3's DB CHECK constraint exactly (role IN ('farmer','buyer','admin')).
    role: str = Field(..., pattern="^(farmer|buyer)$")
    language_pref: str = Field("en", pattern="^(en|hi)$")
    # API field names stay friendly (latitude/longitude); mapped internally
    # to M3's location_lat/location_lng columns. NOTE: M3's schema has no
    # free-text "location" column at all - only these two floats.
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)


class UserLogin(BaseModel):
    phone: str
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    phone: str
    role: str
    language_pref: Optional[str] = None
    latitude: Optional[float] = Field(None, validation_alias="location_lat")
    longitude: Optional[float] = Field(None, validation_alias="location_lng")


class UserUpdate(BaseModel):
    """For PUT /api/users/me. Excludes phone/password/role (own dedicated flows)."""
    name: Optional[str] = None
    language_pref: Optional[str] = Field(None, pattern="^(en|hi)$")
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut
