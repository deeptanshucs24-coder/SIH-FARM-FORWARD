import uuid
from typing import List, Optional
from pydantic import BaseModel, Field


class RecommendMarketRequest(BaseModel):
    crop_name: str = Field(..., min_length=1, max_length=80)
    quantity_kg: int = Field(..., gt=0)
    farmer_latitude: float = Field(..., ge=-90, le=90)
    farmer_longitude: float = Field(..., ge=-180, le=180)
    listing_id: Optional[uuid.UUID] = None  # link back to a specific listing, if this came from one


class MarketOption(BaseModel):
    """'price' is today's current market price (reference/context).
    'predicted_price' is M4's fair-price estimate, which is what
    expected_profit and the ranking score are actually computed from -
    matching the documented flow: Current Prices -> Prediction -> Distance
    -> Transport -> Profit -> Ranking."""
    market_id: uuid.UUID
    market_name: str
    price: float
    predicted_price: float
    distance_km: float
    transport_cost: float
    other_cost: float
    expected_profit: float
    score: float


class RecommendMarketResponse(BaseModel):
    crop_name: str
    quantity_kg: int
    recommendations: List[MarketOption]
    recommended_market_id: Optional[uuid.UUID] = None
