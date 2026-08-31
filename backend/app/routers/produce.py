from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db, require_role, get_current_user
from app.schemas.produce import FarmerProduceCreate, FarmerProduceUpdate, FarmerProduceOut
from app.crud.produce import (
    create_produce, get_produce_by_farmer, get_produce_by_id,
    update_produce, delete_produce,
)
from app.crud.crop import get_crop_by_id

router = APIRouter(prefix="/api", tags=["Farmer Produce"])


def _get_owned_produce_or_403(db: Session, produce_id: int, current_user):
    """Shared ownership check: 404 if it doesn't exist, 403 if it exists but
    belongs to someone else. A farmer can only see/edit/delete THEIR OWN
    produce - ownership is always derived from the JWT, never from a
    client-supplied farmer_id."""
    produce = get_produce_by_id(db, produce_id)
    if not produce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce listing not found")
    if produce.farmer_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not own this produce listing")
    return produce


@router.post(
    "/farmer/produce",
    response_model=FarmerProduceOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a produce listing (FARMER only)",
)
def add_produce(
    payload: FarmerProduceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("FARMER")),
):
    if not get_crop_by_id(db, payload.crop_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop not found")
    return create_produce(db, current_user.user_id, payload)


@router.get(
    "/farmer/produce",
    response_model=list[FarmerProduceOut],
    summary="List your own produce listings (FARMER only)",
    description="Always the current farmer's own listings - identity comes from the JWT.",
)
def list_my_produce(
    db: Session = Depends(get_db),
    current_user=Depends(require_role("FARMER")),
):
    return get_produce_by_farmer(db, current_user.user_id)


@router.get(
    "/farmer/produce/{produce_id}",
    response_model=FarmerProduceOut,
    summary="Read one of your own produce listings",
    description="404 if it doesn't exist, 403 if it exists but belongs to someone else.",
)
def get_my_produce(
    produce_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return _get_owned_produce_or_403(db, produce_id, current_user)


@router.patch(
    "/farmer/produce/{produce_id}",
    response_model=FarmerProduceOut,
    summary="Partially update one of your own produce listings",
)
def update_my_produce(
    produce_id: int,
    payload: FarmerProduceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("FARMER")),
):
    produce = _get_owned_produce_or_403(db, produce_id, current_user)
    return update_produce(db, produce, payload)


@router.delete(
    "/farmer/produce/{produce_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete one of your own produce listings",
)
def delete_my_produce(
    produce_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("FARMER")),
):
    produce = _get_owned_produce_or_403(db, produce_id, current_user)
    delete_produce(db, produce)
    return None
