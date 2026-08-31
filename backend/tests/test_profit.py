def test_profit_calculation_basic(client):
    r = client.post("/api/calculate-profit", json={
        "selling_price": 1800, "quantity": 100, "transport_cost": 500, "other_cost": 50,
    })
    assert r.status_code == 200
    body = r.json()
    assert body["expected_revenue"] == 180000.0
    assert body["expected_net_profit"] == 180000.0 - 500 - 50


def test_profit_calculation_zero_costs(client):
    r = client.post("/api/calculate-profit", json={"selling_price": 1000, "quantity": 10})
    assert r.status_code == 200
    body = r.json()
    assert body["transport_cost"] == 0
    assert body["other_cost"] == 0
    assert body["expected_net_profit"] == 10000.0


def test_profit_calculation_negative_price_rejected(client):
    r = client.post("/api/calculate-profit", json={"selling_price": -100, "quantity": 10})
    assert r.status_code == 422


def test_profit_calculation_negative_quantity_rejected(client):
    r = client.post("/api/calculate-profit", json={"selling_price": 100, "quantity": -10})
    assert r.status_code == 422


def test_profit_calculation_no_auth_required(client):
    """Stateless calculator - the frontend can call it live without a login."""
    r = client.post("/api/calculate-profit", json={"selling_price": 500, "quantity": 5})
    assert r.status_code == 200
