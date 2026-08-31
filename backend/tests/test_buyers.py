from tests.conftest import register, auth_headers


def test_pending_buyer_not_shown_to_public(client):
    """New buyers are PENDING by default and must NOT appear in the
    farmer-facing buyer list until an admin verifies them."""
    register(client, "9300000001", role="BUYER")
    r = client.get("/api/buyers")
    assert r.status_code == 200
    assert r.json() == []  # the only buyer that exists is PENDING, so nothing shows


def test_public_cannot_use_status_filter_to_see_pending(client):
    """Even if a client explicitly asks for verification_status=PENDING,
    a non-admin caller must still only see VERIFIED buyers."""
    register(client, "9300000002", role="BUYER")
    r = client.get("/api/buyers", params={"verification_status": "PENDING"})
    assert r.status_code == 200
    assert r.json() == []


def test_buyer_can_post_requirement_even_while_pending(client, seeded):
    """Posting a requirement isn't restricted by verification status -
    only farmer-facing *discovery* of the buyer is (per the documented flow)."""
    r = register(client, "9300000003", role="BUYER")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={
        "crop_id": seeded["crop_id"], "required_quantity": 100, "offered_price": 1750,
    }, headers=auth_headers(token))
    assert r2.status_code == 201


def test_buyer_requirement_invalid_crop_returns_404(client, seeded):
    r = register(client, "9300000004", role="BUYER")
    token = r.json()["access_token"]
    r2 = client.post("/api/buyer/requirements", json={
        "crop_id": 99999, "required_quantity": 100,
    }, headers=auth_headers(token))
    assert r2.status_code == 404
