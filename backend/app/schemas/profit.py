from pydantic import BaseModel, Field


class ProfitCalculationRequest(BaseModel):
    """Matches TRD FR7 / PRD Section 14."""
    selling_price: float = Field(..., gt=0, description="Price per unit")
    quantity: float = Field(..., gt=0)
    transport_cost: float = Field(0, ge=0)
    other_cost: float = Field(0, ge=0)


class ProfitCalculationResponse(BaseModel):
    expected_revenue: float
    transport_cost: float
    other_cost: float
    expected_net_profit: float
