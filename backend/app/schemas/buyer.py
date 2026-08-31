import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class BuyerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    buyer_id: int
    buyer_name: str
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    contact: str
    verification_status: str


class BuyerRequirementCreate(BaseModel):
    crop_id: int
    required_quantity: float = Field(..., gt=0)
    offered_price: Optional[float] = None
    expires_at: Optional[datetime.datetime] = None


class BuyerRequirementOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    requirement_id: int
    buyer_id: int
    crop_id: int
    required_quantity: float
    offered_price: Optional[float] = None
    status: str
    created_at: datetime.datetime
    expires_at: Optional[datetime.datetime] = None
