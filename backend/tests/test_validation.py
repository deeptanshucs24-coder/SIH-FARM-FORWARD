from tests.conftest import register, auth_headers


# --- Phone number validation ---

def test_register_rejects_non_numeric_phone(client):
    r = client.post("/api/register", json={
        "name": "X", "phone": "98abc43210", "password": "test1234",
        "role": "FARMER", "location": "X",
    })
    assert r.status_code == 422


def test_register_rejects_too_short_phone(client):
    r = client.post("/api/register", json={
        "name": "X", "phone": "12345", "password": "test1234",
        "role": "FARMER", "location": "X",
    })
    assert r.status_code == 422


def test_register_accepts_valid_10_digit_phone(client):
    r = register(client, "9123456789", role="FARMER")
    assert r.status_code == 201


# --- Coordinate bounds ---

def test_register_rejects_latitude_out_of_range(client):
    r = client.post("/api/register", json={
        "name": "X", "phone": "9123456780", "password": "test1234",
        "role": "FARMER", "location": "X", "latitude": 91.0, "longitude": 73.0,
    })
    assert r.status_code == 422


def test_register_rejects_longitude_out_of_range(client):
    r = client.post("/api/register", json={
        "name": "X", "phone": "9123456781", "password": "test1234",
        "role": "FARMER", "location": "X", "latitude": 19.0, "longitude": 181.0,
    })
    assert r.status_code == 422


def test_register_accepts_boundary_coordinates(client):
    """-90/90 and -180/180 are valid boundary values, not out of range."""
    r = client.post("/api/register", json={
        "name": "X", "phone": "9123456782", "password": "test1234",
        "role": "FARMER", "location": "X", "latitude": 90.0, "longitude": -180.0,
    })
    assert r.status_code == 201


def test_recommend_market_rejects_invalid_latitude(client, seeded):
    r = register(client, "9123456783", role="FARMER")
    token = r.json()["access_token"]
    r2 = client.post("/api/recommend-market", json={
        "crop_id": seeded["crop_id"], "quantity": 100,
        "farmer_latitude": 200.0, "farmer_longitude": 73.0,
    }, headers=auth_headers(token))
    assert r2.status_code == 422


# --- Invalid IDs ---

def test_market_prices_invalid_market_id_returns_404(client, seeded):
    r = client.get("/api/market-prices", params={"crop_id": seeded["crop_id"], "market_id": 99999})
    assert r.status_code == 404


def test_market_prices_history_invalid_market_id_returns_404(client, seeded):
    r = client.get("/api/market-prices/history", params={"crop_id": seeded["crop_id"], "market_id": 99999})
    assert r.status_code == 404


# --- Invalid dates ---

def test_create_produce_rejects_malformed_date(client, seeded):
    r = register(client, "9123456784", role="FARMER")
    token = r.json()["access_token"]
    r2 = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "not-a-real-date",
    }, headers=auth_headers(token))
    assert r2.status_code == 422


def test_create_produce_rejects_impossible_calendar_date(client, seeded):
    r = register(client, "9123456785", role="FARMER")
    token = r.json()["access_token"]
    r2 = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-02-30",
    }, headers=auth_headers(token))
    assert r2.status_code == 422


# --- Required fields ---

def test_register_missing_required_field_returns_422(client):
    r = client.post("/api/register", json={
        "name": "X", "phone": "9123456786", "role": "FARMER", "location": "X",
        # password missing
    })
    assert r.status_code == 422


def test_buyer_requirement_rejects_negative_quantity(client, seeded):
    r = register(client, "9123456787", role="BUYER")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={
        "crop_id": seeded["crop_id"], "required_quantity": -5,
    }, headers=auth_headers(token))
    assert r2.status_code == 422
