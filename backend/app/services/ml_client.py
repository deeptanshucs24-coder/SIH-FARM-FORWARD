"""
Client for M4's price prediction service.

Field names here (predicted_price, range_min, range_max, confidence,
distress_flag) match BOTH M3's actual price_predictions table AND the
Master Plan's Part 4.1 M4 output example exactly:
    {"predicted_price": 1820, "range_min": 1750, "range_max": 1950,
     "confidence": 0.82, "distress_flag": false}
This is the documented contract, not a guess - M4's real service (ml/app.py
in M3's branch) is currently an empty stub, so we still fall back to a mock
matching this exact shape until M4 builds the real thing.
"""
import logging

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


async def predict_price(crop_name: str, market_id: str, target_date: str,
                         current_price: float | None) -> dict:
    payload = {"crop_name": crop_name, "market_id": market_id, "target_date": target_date}
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.post(f"{settings.ML_SERVICE_URL}/predict", json=payload)
            resp.raise_for_status()
            return resp.json()
    except (httpx.HTTPError, httpx.TimeoutException) as exc:
        logger.warning("ML service unavailable (%s) - using mock prediction", exc)
        return _mock_prediction(current_price)


def _mock_prediction(current_price: float | None) -> dict:
    """Deterministic placeholder matching the Master Plan's documented shape.
    Low confidence signals to the frontend that this is a mock, not a real
    model output. distress_flag is always False here - real distress
    detection (current price below fair value) is M4's job."""
    base = float(current_price) if current_price else 1800.0
    return {
        "predicted_price": round(base, 2),
        "range_min": round(base * 0.94, 2),
        "range_max": round(base * 1.08, 2),
        "confidence": 0.5,
        "distress_flag": False,
        "_mocked": True,
    }
