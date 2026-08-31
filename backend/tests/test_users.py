from tests.conftest import register, auth_headers


def test_get_own_profile(client):
    r = register(client, "9500000001", role="FARMER", name="Ramesh")
    token = r.json()["access_token"]
    r2 = client.get("/api/users/me", headers=auth_headers(token))
    assert r2.status_code == 200
    assert r2.json()["name"] == "Ramesh"


def test_update_own_profile(client):
    r = register(client, "9500000002", role="FARMER")
    token = r.json()["access_token"]
    r2 = client.put("/api/users/me", json={"location": "Pune"}, headers=auth_headers(token))
    assert r2.status_code == 200
    assert r2.json()["location"] == "Pune"


def test_cannot_view_profile_via_another_users_id(client):
    """There is no GET /api/users/{id} - profile access is always self,
    derived from the JWT. This test documents that design choice."""
    r = register(client, "9500000003", role="FARMER")
    token = r.json()["access_token"]
    # Attempting the old-style "client supplies an id" pattern should 404 -
    # no such route exists.
    r2 = client.get("/api/users/1", headers=auth_headers(token))
    assert r2.status_code == 404
