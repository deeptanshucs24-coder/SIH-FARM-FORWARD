import uuid
import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class MarketOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    state: Optional[str] = None
    district: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None


class MarketPriceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    market_id: uuid.UUID
    crop_name: str
    price_per_quintal: float
    date: datetime.date
