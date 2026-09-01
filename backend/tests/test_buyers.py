from tests.conftest import register, auth_headers


def test_buyers_list_includes_registered_buyer(client):
    register(client, "9400000001", role="buyer", name="Buyer One")
    r = client.get("/api/buyers")
    assert r.status_code == 200
    assert len(r.json()) == 1
    assert r.json()[0]["name"] == "Buyer One"


def test_buyers_list_excludes_farmers(client):
    register(client, "9400000002", role="farmer")
    register(client, "9400000003", role="buyer")
    r = client.get("/api/buyers")
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_buyer_can_post_requirement(client, seeded):
    r = register(client, "9400000004", role="buyer")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={
        "crop_name": "onion", "quantity_needed_kg": 500,
    }, headers=auth_headers(token))
    assert r2.status_code == 201
    assert r2.json()["crop_name"] == "onion"


def test_buyer_requirement_negative_quantity_rejected(client, seeded):
    r = register(client, "9400000005", role="buyer")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={
        "crop_name": "onion", "quantity_needed_kg": -5,
    }, headers=auth_headers(token))
    assert r2.status_code == 422


def test_buyer_requirement_without_quantity_is_optional(client, seeded):
    """M3's schema allows quantity_needed_kg to be NULL."""
    r = register(client, "9400000006", role="buyer")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={"crop_name": "onion"},
                      headers=auth_headers(token))
    assert r2.status_code == 201
    assert r2.json()["quantity_needed_kg"] is None
