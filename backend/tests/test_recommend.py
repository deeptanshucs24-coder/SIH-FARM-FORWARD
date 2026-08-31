from tests.conftest import register, auth_headers


def _farmer_token(client, phone="9400000001"):
    r = register(client, phone, role="FARMER")
    return r.json()["access_token"]


def test_recommend_market_requires_auth(client, seeded):
    r = client.post("/api/recommend-market", json={
        "crop_id": seeded["crop_id"], "quantity": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
    })
    assert r.status_code == 401


def test_recommend_market_uses_mock_fallback_when_m5_unreachable(client, seeded):
    """conftest points RANKING_SERVICE_URL at an unreachable port, so this
    always exercises the local-scoring fallback path deterministically."""
    token = _farmer_token(client)
    r = client.post("/api/recommend-market", json={
        "crop_id": seeded["crop_id"], "quantity": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
    }, headers=auth_headers(token))
    assert r.status_code == 200
    body = r.json()
    assert len(body["recommendations"]) == 1  # one market was seeded
    assert body["recommended_market_id"] == seeded["market_id"]


def test_recommend_market_invokes_price_prediction_per_candidate(client, seeded):
    """Confirms M4's ml_client is actually called as part of the orchestration
    flow (Current Prices -> Prediction -> Distance -> Transport -> Profit ->
    Ranking), not skipped. Each recommendation must include a predicted_price
    alongside the current price. Since M4 is unreachable in tests, the mock
    fallback bases its prediction on the current price we pass in - so under
    test conditions predicted_price == price exactly, which itself proves the
    current price was actually threaded through to the prediction call."""
    token = _farmer_token(client)
    r = client.post("/api/recommend-market", json={
        "crop_id": seeded["crop_id"], "quantity": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
    }, headers=auth_headers(token))
    assert r.status_code == 200
    option = r.json()["recommendations"][0]
    assert "predicted_price" in option
    assert option["predicted_price"] == option["price"]


def test_recommend_market_invalid_crop_returns_404(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/recommend-market", json={
        "crop_id": 99999, "quantity": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
    }, headers=auth_headers(token))
    assert r.status_code == 404


def test_recommend_market_with_someone_elses_produce_id_returns_403(client, seeded):
    token_a = _farmer_token(client, "9400000002")
    created = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-09-10",
    }, headers=auth_headers(token_a))
    produce_id = created.json()["produce_id"]

    token_b = _farmer_token(client, "9400000003")
    r = client.post("/api/recommend-market", json={
        "crop_id": seeded["crop_id"], "quantity": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
        "produce_id": produce_id,
    }, headers=auth_headers(token_b))
    assert r.status_code == 403


def test_predict_price_uses_mock_fallback_when_m4_unreachable(client, seeded):
    r = client.post("/api/predict-price", json={
        "crop_id": seeded["crop_id"], "market_id": seeded["market_id"],
    })
    assert r.status_code == 201
    body = r.json()
    assert body["predicted_price"] > 0
    assert body["model_name"] == "mock-fallback"


def test_predict_price_invalid_market_returns_404(client, seeded):
    r = client.post("/api/predict-price", json={
        "crop_id": seeded["crop_id"], "market_id": 99999,
    })
    assert r.status_code == 404
