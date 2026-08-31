from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.crop import CropOut
from app.crud.crop import list_crops

router = APIRouter(prefix="/api", tags=["Crops"])


@router.get(
    "/crops",
    response_model=list[CropOut],
    summary="List all supported crops",
    description="Reference data populated by M3's data pipeline (crop_name + variety).",
)
def get_crops(db: Session = Depends(get_db)):
    return list_crops(db)
