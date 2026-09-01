from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.market import list_distinct_crop_names

router = APIRouter(prefix="/api", tags=["Crops"])


@router.get(
    "/crops",
    response_model=list[str],
    summary="List crop names currently in the system",
    description="ADAPTED FROM ORIGINAL DESIGN: M3's actual schema has no "
                "separate 'crops' reference table - a crop is just a free-text "
                "crop_name string on crop_listings/market_prices. This endpoint "
                "derives the list dynamically (distinct crop_name values) "
                "instead of reading a fixed table. Flagged for team awareness.",
)
def get_crops(db: Session = Depends(get_db)):
    return list_distinct_crop_names(db)
