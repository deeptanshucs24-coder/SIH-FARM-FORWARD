from tests.conftest import register, auth_headers


def _farmer_token(client, phone="9200000001"):
    r = register(client, phone, role="farmer")
    return r.json()["access_token"]


def test_create_listing_succeeds(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/farmer/produce", json={
        "crop_name": "onion", "quantity_kg": 300, "grade": "A", "harvest_date": "2026-09-10",
    }, headers=auth_headers(token))
    assert r.status_code == 201
    body = r.json()
    assert body["quantity_kg"] == 300
    assert body["crop_name"] == "onion"
    assert body["status"] == "listed"


def test_create_listing_negative_quantity_returns_422(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/farmer/produce", json={"crop_name": "onion", "quantity_kg": -50},
                     headers=auth_headers(token))
    assert r.status_code == 422


def test_create_listing_empty_crop_name_returns_422(client, seeded):
    token = _farmer_token(client)
    r = client.post("/api/farmer/produce", json={"crop_name": "", "quantity_kg": 50},
                     headers=auth_headers(token))
    assert r.status_code == 422


def test_read_own_listings(client, seeded):
    token = _farmer_token(client)
    client.post("/api/farmer/produce", json={"crop_name": "onion", "quantity_kg": 100},
                headers=auth_headers(token))
    r = client.get("/api/farmer/produce", headers=auth_headers(token))
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_read_single_listing_by_owner(client, seeded):
    token = _farmer_token(client)
    created = client.post("/api/farmer/produce", json={"crop_name": "onion", "quantity_kg": 100},
                           headers=auth_headers(token))
    listing_id = created.json()["id"]
    r = client.get(f"/api/farmer/produce/{listing_id}", headers=auth_headers(token))
    assert r.status_code == 200


def test_read_nonexistent_listing_returns_404(client, seeded):
    import uuid
    token = _farmer_token(client)
    r = client.get(f"/api/farmer/produce/{uuid.uuid4()}", headers=auth_headers(token))
    assert r.status_code == 404


def test_read_malformed_id_returns_404(client, seeded):
    """A non-UUID path param should 404, not 500."""
    token = _farmer_token(client)
    r = client.get("/api/farmer/produce/not-a-uuid", headers=auth_headers(token))
    assert r.status_code == 404


def test_update_own_listing(client, seeded):
    token = _farmer_token(client)
    created = client.post("/api/farmer/produce", json={"crop_name": "onion", "quantity_kg": 100},
                           headers=auth_headers(token))
    listing_id = created.json()["id"]
    r = client.patch(f"/api/farmer/produce/{listing_id}", json={"quantity_kg": 250},
                      headers=auth_headers(token))
    assert r.status_code == 200
    assert r.json()["quantity_kg"] == 250


def test_delete_own_listing(client, seeded):
    token = _farmer_token(client)
    created = client.post("/api/farmer/produce", json={"crop_name": "onion", "quantity_kg": 100},
                           headers=auth_headers(token))
    listing_id = created.json()["id"]
    r = client.delete(f"/api/farmer/produce/{listing_id}", headers=auth_headers(token))
    assert r.status_code == 204

    r2 = client.get(f"/api/farmer/produce/{listing_id}", headers=auth_headers(token))
    assert r2.status_code == 404
