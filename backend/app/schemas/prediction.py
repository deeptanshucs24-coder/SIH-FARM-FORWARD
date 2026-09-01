import uuid
import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class PredictPriceRequest(BaseModel):
    crop_name: str = Field(..., min_length=1, max_length=80)
    market_id: uuid.UUID
    target_date: Optional[datetime.date] = None  # defaults to +7 days if omitted


class PricePredictionOut(BaseModel):
    """Field names match M3's price_predictions table AND the Master Plan's
    Part 4.1 M4 output example exactly - this is the documented contract."""
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    crop_name: str
    market_id: Optional[uuid.UUID] = None
    predicted_price: Optional[float] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    confidence: Optional[float] = None
    distress_flag: bool
