import uuid
import datetime
from pydantic import BaseModel, ConfigDict, Field


class MatchOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    listing_id: uuid.UUID
    buyer_id: uuid.UUID
    status: str
    created_at: datetime.datetime


class MatchStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(accepted|rejected)$")
