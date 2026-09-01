from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.market import MarketPriceOut
from app.crud.market import get_current_price, get_price_history, get_market_by_id

router = APIRouter(prefix="/api", tags=["Market Prices"])


def _validate_market(db: Session, market_id):
    if market_id is not None and not get_market_by_id(db, market_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Market not found")


@router.get(
    "/market-prices",
    response_model=list[MarketPriceOut],
    summary="Current/latest price per market for a crop (NOT historical rows)",
    description="crop_name is free text (M3's schema has no crops reference "
                "table to validate against) - an unknown or not-yet-priced crop simply "
                "returns an empty list, not a 404. market_id, if given, IS "
                "validated since markets is a real table.",
)
def current_prices(
    crop_name: str = Query(...),
    market_id: str | None = Query(None),
    db: Session = Depends(get_db),
):
    _validate_market(db, market_id)
    return get_current_price(db, crop_name, market_id)


@router.get(
    "/market-prices/history",
    response_model=list[MarketPriceOut],
    summary="Historical price series for a crop over the last N days",
)
def price_history(
    crop_name: str = Query(...),
    market_id: str | None = Query(None),
    days: int = Query(30, ge=1, le=365),
    db: Session = Depends(get_db),
):
    _validate_market(db, market_id)
    return get_price_history(db, crop_name, market_id, days)
