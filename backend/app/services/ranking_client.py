"""
Client for M5's market ranking service (POST /api/recommend-market).

Falls back to a simple local ranking (based on whatever market prices are
already in the DB) if M5's service isn't reachable yet.
"""
import logging

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


async def rank_markets(crop_id: int, quantity: float, farmer_lat: float, farmer_lng: float,
                        candidate_markets: list[dict]) -> list[dict] | None:
    """candidate_markets: list of {market_id, market_name, price, latitude, longitude}
    Returns None if the remote service isn't reachable, so the caller can fall back
    to its own local scoring logic (see routers/recommend.py)."""
    payload = {
        "crop_id": crop_id,
        "quantity": quantity,
        "farmer_location": {"lat": farmer_lat, "lng": farmer_lng},
        "candidate_markets": candidate_markets,
    }
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.post(f"{settings.RANKING_SERVICE_URL}/rank", json=payload)
            resp.raise_for_status()
            return resp.json().get("ranked_markets")
    except (httpx.HTTPError, httpx.TimeoutException) as exc:
        logger.warning("Ranking service unavailable (%s) - falling back to local scoring", exc)
        return None
