from typing import List, Optional
from pydantic import BaseModel, Field


class RecommendMarketRequest(BaseModel):
    crop_id: int
    quantity: float = Field(..., gt=0)
    farmer_latitude: float = Field(..., ge=-90, le=90)
    farmer_longitude: float = Field(..., ge=-180, le=180)
    produce_id: Optional[int] = None  # link back to a specific listing, if this came from one


class MarketOption(BaseModel):
    """One ranked option in the response - matches PRD Section 6.3 output shape.
    'price' is today's current market price (reference/context). 'predicted_price'
    is M4's fair-price estimate for this market, which is what expected_profit
    and the ranking score are actually computed from - matching the documented
    flow: Current Prices -> Prediction -> Distance -> Transport -> Profit -> Ranking."""
    market_id: int
    market_name: str
    price: float
    predicted_price: float
    distance_km: float
    transport_cost: float
    other_cost: float
    expected_profit: float
    score: float


class RecommendMarketResponse(BaseModel):
    crop_id: int
    quantity: float
    recommendations: List[MarketOption]
    recommended_market_id: Optional[int] = None  # top-ranked option, highlighted per PRD 11
