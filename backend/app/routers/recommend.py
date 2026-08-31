"""
This is M2's core orchestration job (same role as in the original master plan),
following the documented flow:

    Farmer Input -> Current Market Prices -> Historical/Prediction -> Distance
    -> Transportation -> Profit -> Ranking -> Recommendation

Concretely: gather current prices, ask M4 for a fair-price prediction per
candidate market, compute distance/transport/profit off the PREDICTED price,
ask M5 to score/rank the results (falling back to transparent local scoring
if M5 isn't up yet), persist the top result, and hand the frontend one clean
ranked list.
"""
import asyncio
import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db, require_role
from app.schemas.recommendation import RecommendMarketRequest, RecommendMarketResponse, MarketOption
from app.crud.market import get_current_price, get_market_by_id
from app.crud.crop import get_crop_by_id
from app.crud.produce import get_produce_by_id
from app.crud.recommendation import save_recommendation
from app.services import ranking_client, ml_client, transport

router = APIRouter(prefix="/api", tags=["Market Recommendation"])


@router.post(
    "/recommend-market",
    response_model=RecommendMarketResponse,
    summary="Get a ranked list of markets to sell at (FARMER only)",
    description="Runs the full documented flow: current prices -> M4 price "
                "prediction -> distance/transport -> profit -> M5 ranking "
                "(or local fallback). M4/M5 both fall back to mocks if their "
                "services aren't reachable, so this endpoint always returns "
                "a usable result.",
)
async def recommend_market(
    payload: RecommendMarketRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("FARMER")),
):
    if not get_crop_by_id(db, payload.crop_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Crop not found")

    if payload.produce_id is not None:
        produce = get_produce_by_id(db, payload.produce_id)
        if not produce:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce listing not found")
        if produce.farmer_id != current_user.user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not own this produce listing")

    # 1. Find every market that has a recent price for this crop
    price_rows = get_current_price(db, payload.crop_id)
    seen_markets = {}
    for row in price_rows:
        if row.market_id not in seen_markets:  # first hit per market = most recent (query is ordered)
            seen_markets[row.market_id] = row

    valid_markets = []  # (market, price_row) pairs that have usable location data
    for market_id, price_row in seen_markets.items():
        market = get_market_by_id(db, market_id)
        if not market or market.latitude is None or market.longitude is None:
            continue
        valid_markets.append((market, price_row))

    # 2. Ask M4 for a fair-price prediction at each candidate market, in
    # parallel. Target date defaults to a week out - same convention as
    # POST /api/predict-price. Falls back to a mocked prediction per-market
    # if M4 isn't reachable (see ml_client.predict_price).
    target_date = (datetime.date.today() + datetime.timedelta(days=7)).isoformat()
    prediction_tasks = [
        ml_client.predict_price(
            crop_id=payload.crop_id,
            market_id=market.market_id,
            target_date=target_date,
            current_avg_price=float(price_row.average_price),
        )
        for market, price_row in valid_markets
    ]
    predictions = await asyncio.gather(*prediction_tasks) if prediction_tasks else []

    # 3. Build candidates using the PREDICTED price for distance/transport/profit,
    # keeping today's current price alongside it for context/explainability.
    candidates = []
    for (market, price_row), prediction in zip(valid_markets, predictions):
        predicted_price = float(prediction["predicted_price"])
        distance = transport.calculate_distance_km(
            payload.farmer_latitude, payload.farmer_longitude,
            float(market.latitude), float(market.longitude),
        )
        transport_cost = transport.estimate_transport_cost(distance, payload.quantity)
        profit = transport.calculate_profit(predicted_price, payload.quantity, transport_cost)
        candidates.append({
            "market_id": market.market_id,
            "market_name": market.market_name,
            "price": float(price_row.average_price),
            "predicted_price": predicted_price,
            "distance_km": distance,
            "transport_cost": transport_cost,
            "other_cost": profit["other_cost"],
            "expected_profit": profit["expected_net_profit"],
        })

    # 4. Ask M5 to score/rank them; fall back to local scoring if unreachable
    ranked = await ranking_client.rank_markets(
        crop_id=payload.crop_id, quantity=payload.quantity,
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

    if top:
        save_recommendation(
            db,
            farmer_id=current_user.user_id,
            produce_id=payload.produce_id,
            crop_id=payload.crop_id,
            quantity=payload.quantity,
            recommended_type="MARKET",
            recommended_market_id=top.market_id,
            recommended_buyer_id=None,
            expected_price=top.predicted_price,
            transport_cost=top.transport_cost,
            other_cost=top.other_cost,
            expected_profit=top.expected_profit,
        )

    return RecommendMarketResponse(
        crop_id=payload.crop_id,
        quantity=payload.quantity,
        recommendations=options,
        recommended_market_id=top.market_id if top else None,
    )


def _local_rank(candidates: list[dict]) -> list[dict]:
    """Transparent weighted-scoring fallback (Master Plan Part 4.2 style) -
    ranks by expected profit (now derived from predicted price), normalized
    to a 0-1 score, highest first."""
    if not candidates:
        return []
    profits = [c["expected_profit"] for c in candidates]
    lo, hi = min(profits), max(profits)
    spread = (hi - lo) or 1.0
    for c in candidates:
        c["score"] = round((c["expected_profit"] - lo) / spread, 2)
    return sorted(candidates, key=lambda c: c["score"], reverse=True)
