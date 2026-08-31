"""
Client for M4's price prediction service (POST /api/predict-price).

Falls back to a mocked prediction if M4's service isn't reachable yet -
never blocks the rest of the team. Swap ML_SERVICE_URL in .env once M4 is live.
"""
import logging
import datetime

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


async def predict_price(crop_id: int, market_id: int, target_date: str, current_avg_price: float | None) -> dict:
    payload = {"crop_id": crop_id, "market_id": market_id, "target_date": target_date}
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.post(f"{settings.ML_SERVICE_URL}/predict", json=payload)
            resp.raise_for_status()
            return resp.json()
    except (httpx.HTTPError, httpx.TimeoutException) as exc:
        logger.warning("ML service unavailable (%s) - using mock prediction", exc)
        return _mock_prediction(current_avg_price)


def _mock_prediction(current_avg_price: float | None) -> dict:
    base = float(current_avg_price) if current_avg_price else 1800.0
    return {
        "predicted_price": round(base, 2),
        "predicted_min_price": round(base * 0.94, 2),
        "predicted_max_price": round(base * 1.08, 2),
        "trend": "STABLE",
        "model_name": "mock-fallback",
        "_mocked": True,
    }
