import uuid
import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class CropListingCreate(BaseModel):
    crop_name: str = Field(..., min_length=1, max_length=80)
    quantity_kg: int = Field(..., gt=0)
    grade: Optional[str] = Field(None, max_length=5)
    harvest_date: Optional[datetime.date] = None


class CropListingUpdate(BaseModel):
    """Partial update - only fields the farmer wants to change need to be sent."""
    quantity_kg: Optional[int] = Field(None, gt=0)
    grade: Optional[str] = Field(None, max_length=5)
    harvest_date: Optional[datetime.date] = None
    status: Optional[str] = Field(None, pattern="^(listed|interested|confirmed)$")


class CropListingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    farmer_id: uuid.UUID
    crop_name: str
    quantity_kg: int
    grade: Optional[str] = None
    harvest_date: Optional[datetime.date] = None
    status: str
    created_at: datetime.datetime
