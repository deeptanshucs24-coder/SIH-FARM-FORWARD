import uuid
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class BuyerOut(BaseModel):
    """A buyer IS a user with role='buyer' - M3's schema has no separate
    buyers table, so this is just a trimmed view of that user row.
    NOTE: no verification_status field exists anywhere in M3's schema -
    the PRD's documented PENDING/VERIFIED/REJECTED buyer-verification flow
    is not implemented at the DB level. Flagged for team - see README."""
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    phone: str
    latitude: Optional[float] = Field(None, validation_alias="location_lat")
    longitude: Optional[float] = Field(None, validation_alias="location_lng")


class BuyerRequirementCreate(BaseModel):
    """M3's buyers_requirements table has no offered_price/status/expires_at
    columns - kept minimal to match exactly."""
    crop_name: str = Field(..., min_length=1, max_length=80)
    quantity_needed_kg: Optional[int] = Field(None, gt=0)


class BuyerRequirementOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    buyer_id: uuid.UUID
    crop_name: str
    quantity_needed_kg: Optional[int] = None
