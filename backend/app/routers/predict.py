import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.prediction import PredictPriceRequest, PricePredictionOut
from app.crud.market import get_latest_price_for_market, get_market_by_id
from app.crud.crop import get_crop_by_id
from app.crud.prediction import save_prediction
from app.services import ml_client

router = APIRouter(prefix="/api", tags=["Price Prediction"])


@router.post("/predict-price", response_model=PricePredictionOut, status_code=201)
async def predict_price(payload: PredictPriceRequest, db: Session = Depends(get_db)):
    if not get_crop_by_id(db, payload.crop_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop not found")
    if not get_market_by_id(db, payload.market_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Market not found")

    target_date = payload.target_date or (datetime.date.today() + datetime.timedelta(days=7))

    # Give M4 today's average price as context, if we have one on record.
    latest = get_latest_price_for_market(db, payload.crop_id, payload.market_id)
    current_avg = float(latest.average_price) if latest else None

    result = await ml_client.predict_price(
        crop_id=payload.crop_id,
        market_id=payload.market_id,
        target_date=target_date.isoformat(),
        current_avg_price=current_avg,
    )

    prediction = save_prediction(
        db,
        crop_id=payload.crop_id,
        market_id=payload.market_id,
        prediction_date=datetime.date.today(),
        target_date=target_date,
        predicted_price=result["predicted_price"],
        predicted_min_price=result.get("predicted_min_price"),
        predicted_max_price=result.get("predicted_max_price"),
        trend=result.get("trend"),
        model_name=result.get("model_name"),
    )
    return prediction
