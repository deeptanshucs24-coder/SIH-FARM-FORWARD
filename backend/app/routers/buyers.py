from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db, require_role
from app.schemas.buyer import BuyerOut, BuyerRequirementCreate, BuyerRequirementOut
from app.crud.buyer import list_buyers, create_requirement

router = APIRouter(prefix="/api", tags=["Buyers"])


@router.get(
    "/buyers",
    response_model=list[BuyerOut],
    summary="List buyers",
    description="A buyer is just a users row with role='buyer' - M3's schema "
                "has no separate buyers table and NO verification_status "
                "column anywhere. The PRD's documented PENDING/VERIFIED/"
                "REJECTED buyer-verification flow is therefore not enforced "
                "at the API level right now. Flagged for team - see README.",
)
def get_buyers(db: Session = Depends(get_db)):
    return list_buyers(db)


@router.post(
    "/buyer/requirements",
    response_model=BuyerRequirementOut,
    status_code=201,
    summary="Buyer posts a crop requirement",
)
def post_requirement(
    payload: BuyerRequirementCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("buyer")),
):
    return create_requirement(db, current_user.id, payload)
