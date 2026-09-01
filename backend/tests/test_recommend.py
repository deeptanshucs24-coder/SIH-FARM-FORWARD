from tests.conftest import register, auth_headers


def _farmer_token(client, phone="9500000001"):
    r = register(client, phone, role="farmer")
    return r.json()["access_token"]


def test_predict_price_uses_mock_fallback(client, seeded):
    r = client.post("/api/predict-price", json={
        "crop_name": seeded["crop_name"], "market_id": seeded["market_id"],
    })
    assert r.status_code == 201
    body = r.json()
    assert body["predicted_price"] == 1820.0  # matches today's seeded price (mock bases off it)
    assert body["distress_flag"] is False
    assert "range_min" in body and "range_max" in body


def test_predict_price_invalid_market_returns_404(client, seeded):
    import uuid
    r = client.post("/api/predict-price", json={"crop_name": "onion", "market_id": str(uuid.uuid4())})
    assert r.status_code == 404


def test_recommend_market_requires_auth(client, seeded):
    r = client.post("/api/recommend-market", json={
        "crop_name": seeded["crop_name"], "quantity_kg": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
    })
    assert r.status_code == 401


def test_recommend_market_returns_ranked_list(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/recommend-market", json={
        "crop_name": seeded["crop_name"], "quantity_kg": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
    }, headers=auth_headers(token))
    assert r.status_code == 200
    body = r.json()
    assert len(body["recommendations"]) == 1
    assert body["recommended_market_id"] == seeded["market_id"]
    option = body["recommendations"][0]
    assert "predicted_price" in option
    assert option["predicted_price"] == option["price"]  # mock bases prediction off current price


def test_recommend_market_invalid_coordinates_rejected(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/recommend-market", json={
        "crop_name": seeded["crop_name"], "quantity_kg": 100,
        "farmer_latitude": 200.0, "farmer_longitude": 73.0,
    }, headers=auth_headers(token))
    assert r.status_code == 422


def test_recommend_market_with_someone_elses_listing_returns_403(client, seeded):
    token_a = _farmer_token(client, "9500000002")
    created = client.post("/api/farmer/produce", json={
        "crop_name": seeded["crop_name"], "quantity_kg": 100,
    }, headers=auth_headers(token_a))
    listing_id = created.json()["id"]

    token_b = _farmer_token(client, "9500000003")
    r = client.post("/api/recommend-market", json={
        "crop_name": seeded["crop_name"], "quantity_kg": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
        "listing_id": listing_id,
    }, headers=auth_headers(token_b))
    assert r.status_code == 403


def test_recommend_market_profit_math_uses_quintal_conversion(client, seeded):
    """quantity_kg=100 means 1 quintal. transport_cost for a ~0km distance
    should be ~0, so expected_profit should be close to predicted_price * 1."""
    token = _farmer_token(client)
    r = client.post("/api/recommend-market", json={
        "crop_name": seeded["crop_name"], "quantity_kg": 100,
        "farmer_latitude": 19.99, "farmer_longitude": 73.78,
    }, headers=auth_headers(token))
    option = r.json()["recommendations"][0]
    # 100kg = 1 quintal, so revenue should equal predicted_price (per quintal) x 1
    expected_revenue = option["predicted_price"] * 1
    assert abs((option["expected_profit"] + option["transport_cost"]) - expected_revenue) < 0.01
