import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.prediction import PredictPriceRequest, PricePredictionOut
from app.crud.market import get_latest_price_for_market, get_market_by_id
from app.crud.prediction import save_prediction
from app.services import ml_client

router = APIRouter(prefix="/api", tags=["Price Prediction"])


@router.post(
    "/predict-price",
    response_model=PricePredictionOut,
    status_code=201,
    summary="Get + store a fair-price prediction for a crop at a market",
)
async def predict_price(payload: PredictPriceRequest, db: Session = Depends(get_db)):
    if not get_market_by_id(db, payload.market_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Market not found")

    target_date = payload.target_date or (datetime.date.today() + datetime.timedelta(days=7))

    latest = get_latest_price_for_market(db, payload.crop_name, payload.market_id)
    current_price = float(latest.price_per_quintal) if latest else None

    result = await ml_client.predict_price(
        crop_name=payload.crop_name,
        market_id=str(payload.market_id),
        target_date=target_date.isoformat(),
        current_price=current_price,
    )

    prediction = save_prediction(
        db,
        crop_name=payload.crop_name,
        market_id=payload.market_id,
        predicted_price=result.get("predicted_price"),
        range_min=result.get("range_min"),
        range_max=result.get("range_max"),
        confidence=result.get("confidence"),
        distress_flag=result.get("distress_flag", False),
    )
    return prediction
