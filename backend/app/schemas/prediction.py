import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PredictPriceRequest(BaseModel):
    crop_id: int
    market_id: int
    target_date: Optional[datetime.date] = None  # defaults to today+1 if omitted


class PricePredictionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, protected_namespaces=())

    prediction_id: int
    crop_id: int
    market_id: int
    prediction_date: datetime.date
    target_date: datetime.date
    predicted_price: float
    predicted_min_price: Optional[float] = None
    predicted_max_price: Optional[float] = None
    trend: Optional[str] = None
    model_name: Optional[str] = None
