import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class FarmerProduceCreate(BaseModel):
    crop_id: int
    quantity: float = Field(..., gt=0)
    available_date: datetime.date
    expected_price: Optional[float] = Field(None, ge=0)


class FarmerProduceUpdate(BaseModel):
    """Partial update - only fields the farmer wants to change need to be sent."""
    quantity: Optional[float] = Field(None, gt=0)
    available_date: Optional[datetime.date] = None
    expected_price: Optional[float] = Field(None, ge=0)


class FarmerProduceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    produce_id: int
    farmer_id: int
    crop_id: int
    quantity: float
    available_date: datetime.date
    expected_price: Optional[float] = None
    created_at: datetime.datetime
