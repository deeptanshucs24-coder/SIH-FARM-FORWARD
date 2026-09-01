from fastapi import APIRouter

from app.schemas.profit import ProfitCalculationRequest, ProfitCalculationResponse
from app.services.transport import calculate_profit

router = APIRouter(prefix="/api", tags=["Profit Calculator"])


@router.post(
    "/calculate-profit",
    response_model=ProfitCalculationResponse,
    summary="Calculate expected revenue and net profit",
    description="Matches TRD FR7: Net Profit = Expected Revenue - Transport "
                "Cost - Other Cost. Stateless, unit-agnostic (pure "
                "selling_price x quantity - no kg/quintal conversion here), "
                "no auth required. transport_cost is an input, not computed - "
                "the final transport formula is still a pending team decision.",
)
def profit(payload: ProfitCalculationRequest):
    result = calculate_profit(
        selling_price=payload.selling_price,
        quantity=payload.quantity,
        transport_cost=payload.transport_cost,
        other_cost=payload.other_cost,
    )
    return ProfitCalculationResponse(**result)
