from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.market import MarketPriceOut
from app.crud.market import get_current_price, get_price_history, get_market_by_id
from app.crud.crop import get_crop_by_id

router = APIRouter(prefix="/api", tags=["Market Prices"])


def _validate_crop_and_market(db: Session, crop_id: int, market_id: int | None):
    if not get_crop_by_id(db, crop_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop not found")
    if market_id is not None and not get_market_by_id(db, market_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Market not found")


@router.get(
    "/market-prices",
    response_model=list[MarketPriceOut],
    summary="Current/latest price per market for a crop (NOT historical rows)",
    description="Returns exactly one row per market: the most recent price on "
                "record for the given crop. Optionally filter to a single market.",
)
def current_prices(
    crop_id: int = Query(..., description="Crop to look up"),
    market_id: int | None = Query(None, description="Optional: restrict to one market"),
    db: Session = Depends(get_db),
):
    _validate_crop_and_market(db, crop_id, market_id)
    return get_current_price(db, crop_id, market_id)


@router.get(
    "/market-prices/history",
    response_model=list[MarketPriceOut],
    summary="Historical price series for a crop over the last N days",
    description="Returns every price row within the given day range - unlike "
                "/market-prices, this deliberately includes older rows.",
)
def price_history(
    crop_id: int = Query(..., description="Crop to look up"),
    market_id: int | None = Query(None, description="Optional: restrict to one market"),
    days: int = Query(30, ge=1, le=365, description="How many days back to include"),
    db: Session = Depends(get_db),
):
    _validate_crop_and_market(db, crop_id, market_id)
    return get_price_history(db, crop_id, market_id, days)
