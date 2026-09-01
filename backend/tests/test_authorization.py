from tests.conftest import register, auth_headers


def test_buyer_cannot_create_crop_listing(client, seeded):
    r = register(client, "9100000001", role="buyer")
    token = r.json()["access_token"]
    r2 = client.post("/api/farmer/produce", json={
        "crop_name": "onion", "quantity_kg": 100,
    }, headers=auth_headers(token))
    assert r2.status_code == 403


def test_farmer_cannot_post_buyer_requirement(client, seeded):
    r = register(client, "9100000002", role="farmer")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={
        "crop_name": "onion", "quantity_needed_kg": 50,
    }, headers=auth_headers(token))
    assert r2.status_code == 403


def test_farmer_cannot_access_another_farmers_listing(client, seeded):
    r1 = register(client, "9100000003", role="farmer", name="Farmer A")
    token1 = r1.json()["access_token"]
    r2 = register(client, "9100000004", role="farmer", name="Farmer B")
    token2 = r2.json()["access_token"]

    created = client.post("/api/farmer/produce", json={
        "crop_name": "onion", "quantity_kg": 200,
    }, headers=auth_headers(token1))
    listing_id = created.json()["id"]

    r3 = client.get(f"/api/farmer/produce/{listing_id}", headers=auth_headers(token2))
    assert r3.status_code == 403

    r4 = client.patch(f"/api/farmer/produce/{listing_id}", json={"quantity_kg": 999},
                       headers=auth_headers(token2))
    assert r4.status_code == 403

    r5 = client.delete(f"/api/farmer/produce/{listing_id}", headers=auth_headers(token2))
    assert r5.status_code == 403


def test_farmer_cannot_accept_matches_on_another_farmers_listing(client, seeded):
    r1 = register(client, "9100000005", role="farmer", name="Farmer A")
    token1 = r1.json()["access_token"]
    r2 = register(client, "9100000006", role="farmer", name="Farmer B")
    token2 = r2.json()["access_token"]
    r3 = register(client, "9100000007", role="buyer")
    buyer_token = r3.json()["access_token"]

    created = client.post("/api/farmer/produce", json={
        "crop_name": "onion", "quantity_kg": 200,
    }, headers=auth_headers(token1))
    listing_id = created.json()["id"]

    match = client.post(f"/api/farmer/produce/{listing_id}/interest", headers=auth_headers(buyer_token))
    match_id = match.json()["id"]

    r = client.patch(f"/api/farmer/produce/{listing_id}/matches/{match_id}", json={"status": "accepted"},
                      headers=auth_headers(token2))
    assert r.status_code == 403


def test_unauthenticated_cannot_access_protected_endpoint(client, seeded):
    r = client.post("/api/farmer/produce", json={"crop_name": "onion", "quantity_kg": 100})
    assert r.status_code == 401


def test_unauthenticated_cannot_access_own_profile(client):
    r = client.get("/api/users/me")
    assert r.status_code == 401


def test_invalid_jwt_rejected(client):
    r = client.get("/api/users/me", headers=auth_headers("this.is.not.a.valid.jwt"))
    assert r.status_code == 401
