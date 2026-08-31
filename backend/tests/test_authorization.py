from tests.conftest import register, auth_headers


def test_buyer_cannot_add_farmer_produce(client, seeded):
    r = register(client, "9100000001", role="BUYER")
    token = r.json()["access_token"]
    r2 = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-09-10",
    }, headers=auth_headers(token))
    assert r2.status_code == 403


def test_farmer_cannot_post_buyer_requirement(client, seeded):
    r = register(client, "9100000002", role="FARMER")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={
        "crop_id": seeded["crop_id"], "required_quantity": 50,
    }, headers=auth_headers(token))
    assert r2.status_code == 403


def test_farmer_cannot_access_another_farmers_produce(client, seeded):
    r1 = register(client, "9100000003", role="FARMER", name="Farmer A")
    token1 = r1.json()["access_token"]
    r2 = register(client, "9100000004", role="FARMER", name="Farmer B")
    token2 = r2.json()["access_token"]

    created = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 200, "available_date": "2026-09-10",
    }, headers=auth_headers(token1))
    produce_id = created.json()["produce_id"]

    r3 = client.get(f"/api/farmer/produce/{produce_id}", headers=auth_headers(token2))
    assert r3.status_code == 403

    r4 = client.patch(f"/api/farmer/produce/{produce_id}", json={"quantity": 999},
                       headers=auth_headers(token2))
    assert r4.status_code == 403

    r5 = client.delete(f"/api/farmer/produce/{produce_id}", headers=auth_headers(token2))
    assert r5.status_code == 403


def test_unauthenticated_cannot_access_protected_endpoint(client, seeded):
    r = client.post("/api/farmer/produce", json={
        "crop_id": seeded["crop_id"], "quantity": 100, "available_date": "2026-09-10",
    })
    assert r.status_code == 401


def test_unauthenticated_cannot_access_own_profile(client):
    r = client.get("/api/users/me")
    assert r.status_code == 401


def test_invalid_jwt_rejected(client):
    r = client.get("/api/users/me", headers=auth_headers("this.is.not.a.valid.jwt"))
    assert r.status_code == 401
