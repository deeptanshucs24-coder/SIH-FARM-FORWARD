from tests.conftest import register, auth_headers


def _farmer_token(client, phone="9200000001"):
    r = register(client, phone, role="FARMER")
    return r.json()["access_token"]


def test_create_produce_succeeds(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 300, "available_date": "2026-09-10",
        "expected_price": 1800,
    }, headers=auth_headers(token))
    assert r.status_code == 201
    body = r.json()
    assert body["quantity"] == 300
    assert body["crop_id"] == seeded["crop_id"]


def test_create_produce_with_invalid_crop_returns_404(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/farmer/produce", json={
        "crop_id": 99999, "quantity": 300, "available_date": "2026-09-10",
    }, headers=auth_headers(token))
    assert r.status_code == 404


def test_create_produce_with_negative_quantity_returns_422(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": -50, "available_date": "2026-09-10",
    }, headers=auth_headers(token))
    assert r.status_code == 422


def test_read_own_produce_list(client, seeded):
    token = _farmer_token(client)
    client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-09-10",
    }, headers=auth_headers(token))
    r = client.get("/api/farmer/produce", headers=auth_headers(token))
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_read_single_produce_by_owner(client, seeded):
    token = _farmer_token(client)
    created = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-09-10",
    }, headers=auth_headers(token))
    produce_id = created.json()["produce_id"]
    r = client.get(f"/api/farmer/produce/{produce_id}", headers=auth_headers(token))
    assert r.status_code == 200


def test_read_nonexistent_produce_returns_404(client, seeded):
    token = _farmer_token(client)
    r = client.get("/api/farmer/produce/99999", headers=auth_headers(token))
    assert r.status_code == 404


def test_update_own_produce(client, seeded):
    token = _farmer_token(client)
    created = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-09-10",
    }, headers=auth_headers(token))
    produce_id = created.json()["produce_id"]
    r = client.patch(f"/api/farmer/produce/{produce_id}", json={"quantity": 250},
                      headers=auth_headers(token))
    assert r.status_code == 200
    assert r.json()["quantity"] == 250


def test_delete_own_produce(client, seeded):
    token = _farmer_token(client)
    created = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-09-10",
    }, headers=auth_headers(token))
    produce_id = created.json()["produce_id"]
    r = client.delete(f"/api/farmer/produce/{produce_id}", headers=auth_headers(token))
    assert r.status_code == 204

    r2 = client.get(f"/api/farmer/produce/{produce_id}", headers=auth_headers(token))
    assert r2.status_code == 404
