"""
Client for M5's market ranking service. Falls back to a transparent local
scoring formula (Master Plan Part 4.2 style) if M5 isn't reachable yet.
"""
import logging

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


async def rank_markets(crop_name: str, quantity_kg: int, farmer_lat: float, farmer_lng: float,
                        candidate_markets: list[dict]) -> list[dict] | None:
    """candidate_markets: list of dicts with market_id/market_name/price/
    predicted_price/distance_km/transport_cost/other_cost/expected_profit.
    Returns None if the remote service isn't reachable, so the caller falls
    back to local scoring (see routers/recommend.py)."""
    payload = {
        "crop_name": crop_name,
        "quantity_kg": quantity_kg,
        "farmer_location": {"lat": farmer_lat, "lng": farmer_lng},
        "candidate_markets": [
            {**c, "market_id": str(c["market_id"])} for c in candidate_markets
        ],
    }
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.post(f"{settings.RANKING_SERVICE_URL}/rank", json=payload)
            resp.raise_for_status()
            return resp.json().get("ranked_markets")
    except (httpx.HTTPError, httpx.TimeoutException) as exc:
        logger.warning("Ranking service unavailable (%s) - falling back to local scoring", exc)
        return None
