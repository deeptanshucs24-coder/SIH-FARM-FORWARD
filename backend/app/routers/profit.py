from fastapi import APIRouter

from app.schemas.profit import ProfitCalculationRequest, ProfitCalculationResponse
from app.services.transport import calculate_profit

router = APIRouter(prefix="/api", tags=["Profit Calculator"])


@router.post(
    "/calculate-profit",
    response_model=ProfitCalculationResponse,
    summary="Calculate expected revenue and net profit",
    description="Matches TRD FR7: Net Profit = Expected Revenue - Transport Cost - "
                "Other Cost. Stateless - no DB write, no auth required, so the "
                "frontend can call it live while the farmer is still typing numbers. "
                "transport_cost is an input here, not computed - the final transport "
                "formula is still a pending team decision (see README).",
)
def profit(payload: ProfitCalculationRequest):
    result = calculate_profit(
        selling_price=payload.selling_price,
        quantity=payload.quantity,
        transport_cost=payload.transport_cost,
        other_cost=payload.other_cost,
    )
    return ProfitCalculationResponse(**result)
