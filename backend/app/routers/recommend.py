"""
M2's core orchestration job, following the documented flow:

    Farmer Input -> Current Market Prices -> Prediction -> Distance
    -> Transportation -> Profit -> Ranking -> Recommendation

NOTE on persistence: the previous round persisted the chosen recommendation
to a `recommendations` table. M3's actual implemented schema has NO such
table (only price_predictions, which is per-prediction, not per-
recommendation-request) - so this endpoint is now purely computational: it
reads current prices, calls M4 and M5 (or their mocks), and returns a
result, without writing anything to the database itself. Flagged for team:
if recommendation history needs to be tracked, that's a schema addition
M3 would need to make.
"""
import asyncio
import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db, require_role
from app.schemas.recommendation import RecommendMarketRequest, RecommendMarketResponse, MarketOption
from app.crud.market import get_current_price, get_market_by_id
from app.crud.crop_listing import get_listing_by_id
from app.services import ranking_client, ml_client, transport

router = APIRouter(prefix="/api", tags=["Market Recommendation"])


@router.post(
    "/recommend-market",
    response_model=RecommendMarketResponse,
    summary="Get a ranked list of markets to sell at (farmer only)",
    description="Runs the full documented flow: current prices -> M4 price "
                "prediction -> distance/transport -> profit -> M5 ranking "
                "(or local fallback). Both M4/M5 fall back to mocks if "
                "unreachable. Prices are per-quintal (matches M3's schema); "
                "quantity_kg is converted to quintals internally for the "
                "revenue/profit math.",
)
async def recommend_market(
    payload: RecommendMarketRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("farmer")),
):
    if payload.listing_id is not None:
        listing = get_listing_by_id(db, payload.listing_id)
        if not listing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop listing not found")
        if listing.farmer_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not own this crop listing")

    # 1. Find every market that has a recent price for this crop
    price_rows = get_current_price(db, payload.crop_name)
    seen_markets = {}
    for row in price_rows:
        if row.market_id not in seen_markets:
            seen_markets[row.market_id] = row

    valid_markets = []
    for market_id, price_row in seen_markets.items():
        market = get_market_by_id(db, market_id)
        if not market or market.lat is None or market.lng is None:
            continue
        valid_markets.append((market, price_row))

    # 2. Ask M4 for a fair-price prediction at each candidate market, in parallel.
    target_date = (datetime.date.today() + datetime.timedelta(days=7)).isoformat()
    prediction_tasks = [
        ml_client.predict_price(
            crop_name=payload.crop_name,
            market_id=str(market.id),
            target_date=target_date,
            current_price=float(price_row.price_per_quintal),
        )
        for market, price_row in valid_markets
    ]
    predictions = await asyncio.gather(*prediction_tasks) if prediction_tasks else []

    # 3. Build candidates using the PREDICTED price (per quintal) for
    # distance/transport/profit. quantity_kg is converted to quintals here
    # since market prices are per-quintal - see services/transport.py.
    quintals = payload.quantity_kg / 100
    candidates = []
    for (market, price_row), prediction in zip(valid_markets, predictions):
        predicted_price = float(prediction["predicted_price"]) if prediction.get("predicted_price") is not None \
            else float(price_row.price_per_quintal)
        distance = transport.calculate_distance_km(
            payload.farmer_latitude, payload.farmer_longitude,
            float(market.lat), float(market.lng),
        )
        transport_cost = transport.estimate_transport_cost(distance, payload.quantity_kg)
        profit = transport.calculate_profit(predicted_price, quintals, transport_cost)
        candidates.append({
            "market_id": market.id,
            "market_name": market.name,
            "price": float(price_row.price_per_quintal),
            "predicted_price": predicted_price,
            "distance_km": distance,
            "transport_cost": transport_cost,
            "other_cost": profit["other_cost"],
            "expected_profit": profit["expected_net_profit"],
        })

    # 4. Ask M5 to score/rank them; fall back to local scoring if unreachable
    ranked = await ranking_client.rank_markets(
        crop_name=payload.crop_name, quantity_kg=payload.quantity_kg,
        farmer_lat=payload.farmer_latitude, farmer_lng=payload.farmer_longitude,
        candidate_markets=candidates,
    )
    if ranked is None:
        ranked = _local_rank(candidates)

    options = [MarketOption(
        market_id=c["market_id"], market_name=c["market_name"], price=c["price"],
        predicted_price=c["predicted_price"], distance_km=c["distance_km"],
        transport_cost=c["transport_cost"], other_cost=c["other_cost"],
        expected_profit=c["expected_profit"], score=c["score"],
    ) for c in ranked]

    top = options[0] if options else None

    return RecommendMarketResponse(
        crop_name=payload.crop_name,
        quantity_kg=payload.quantity_kg,
        recommendations=options,
        recommended_market_id=top.market_id if top else None,
    )


def _local_rank(candidates: list[dict]) -> list[dict]:
    """Transparent weighted-scoring fallback (Master Plan Part 4.2 style) -
    ranks by expected profit (derived from predicted price), normalized to
    a 0-1 score, highest first."""
    if not candidates:
        return []
    profits = [c["expected_profit"] for c in candidates]
    lo, hi = min(profits), max(profits)
    spread = (hi - lo) or 1.0
    for c in candidates:
        c["score"] = round((c["expected_profit"] - lo) / spread, 2)
    return sorted(candidates, key=lambda c: c["score"], reverse=True)
