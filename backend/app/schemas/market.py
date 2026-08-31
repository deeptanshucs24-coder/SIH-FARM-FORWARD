import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class MarketOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    market_id: int
    market_name: str
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class MarketPriceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    price_id: int
    market_id: int
    crop_id: int
    price_date: datetime.date
    min_price: float
    max_price: float
    average_price: float
