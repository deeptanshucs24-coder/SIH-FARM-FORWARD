def test_crops_empty_when_no_data(client):
    r = client.get("/api/crops")
    assert r.status_code == 200
    assert r.json() == []


def test_crops_derived_from_market_prices(client, seeded):
    r = client.get("/api/crops")
    assert r.status_code == 200
    assert r.json() == ["onion"]


def test_crops_includes_crop_listing_names_too(client, seeded):
    from tests.conftest import register, auth_headers
    r = register(client, "9300000001", role="farmer")
    token = r.json()["access_token"]
    client.post("/api/farmer/produce", json={"crop_name": "brinjal", "quantity_kg": 50},
                headers=auth_headers(token))
    r2 = client.get("/api/crops")
    assert set(r2.json()) == {"onion", "brinjal"}
