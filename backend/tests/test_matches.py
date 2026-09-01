from tests.conftest import register, auth_headers


def _setup_listing(client, seeded):
    r = register(client, "9250000001", role="farmer")
    farmer_token = r.json()["access_token"]
    created = client.post("/api/farmer/produce", json={"crop_name": "onion", "quantity_kg": 100},
                           headers=auth_headers(farmer_token))
    return farmer_token, created.json()["id"]


def test_buyer_express_interest_creates_pending_match(client, seeded):
    farmer_token, listing_id = _setup_listing(client, seeded)
    r = register(client, "9250000002", role="buyer")
    buyer_token = r.json()["access_token"]

    r2 = client.post(f"/api/farmer/produce/{listing_id}/interest", headers=auth_headers(buyer_token))
    assert r2.status_code == 201
    assert r2.json()["status"] == "pending"


def test_expressing_interest_bumps_listing_status_to_interested(client, seeded):
    farmer_token, listing_id = _setup_listing(client, seeded)
    r = register(client, "9250000003", role="buyer")
    buyer_token = r.json()["access_token"]

    client.post(f"/api/farmer/produce/{listing_id}/interest", headers=auth_headers(buyer_token))
    r2 = client.get(f"/api/farmer/produce/{listing_id}", headers=auth_headers(farmer_token))
    assert r2.json()["status"] == "interested"


def test_farmer_can_view_matches_on_own_listing(client, seeded):
    farmer_token, listing_id = _setup_listing(client, seeded)
    r = register(client, "9250000004", role="buyer")
    buyer_token = r.json()["access_token"]
    client.post(f"/api/farmer/produce/{listing_id}/interest", headers=auth_headers(buyer_token))

    r2 = client.get(f"/api/farmer/produce/{listing_id}/matches", headers=auth_headers(farmer_token))
    assert r2.status_code == 200
    assert len(r2.json()) == 1


def test_accepting_a_match_confirms_the_listing(client, seeded):
    farmer_token, listing_id = _setup_listing(client, seeded)
    r = register(client, "9250000005", role="buyer")
    buyer_token = r.json()["access_token"]
    match = client.post(f"/api/farmer/produce/{listing_id}/interest", headers=auth_headers(buyer_token))
    match_id = match.json()["id"]

    r2 = client.patch(f"/api/farmer/produce/{listing_id}/matches/{match_id}", json={"status": "accepted"},
                       headers=auth_headers(farmer_token))
    assert r2.status_code == 200
    assert r2.json()["status"] == "accepted"

    r3 = client.get(f"/api/farmer/produce/{listing_id}", headers=auth_headers(farmer_token))
    assert r3.json()["status"] == "confirmed"


def test_rejecting_a_match_does_not_confirm_the_listing(client, seeded):
    farmer_token, listing_id = _setup_listing(client, seeded)
    r = register(client, "9250000006", role="buyer")
    buyer_token = r.json()["access_token"]
    match = client.post(f"/api/farmer/produce/{listing_id}/interest", headers=auth_headers(buyer_token))
    match_id = match.json()["id"]

    client.patch(f"/api/farmer/produce/{listing_id}/matches/{match_id}", json={"status": "rejected"},
                 headers=auth_headers(farmer_token))
    r = client.get(f"/api/farmer/produce/{listing_id}", headers=auth_headers(farmer_token))
    assert r.json()["status"] == "interested"  # not confirmed


def test_express_interest_on_nonexistent_listing_returns_404(client, seeded):
    import uuid
    r = register(client, "9250000007", role="buyer")
    buyer_token = r.json()["access_token"]
    r2 = client.post(f"/api/farmer/produce/{uuid.uuid4()}/interest", headers=auth_headers(buyer_token))
    assert r2.status_code == 404


def test_farmer_cannot_express_interest(client, seeded):
    """Only buyers express interest - a farmer trying it should be blocked by role."""
    farmer_token, listing_id = _setup_listing(client, seeded)
    r = client.post(f"/api/farmer/produce/{listing_id}/interest", headers=auth_headers(farmer_token))
    assert r.status_code == 403
