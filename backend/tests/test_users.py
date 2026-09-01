from tests.conftest import register, auth_headers


def test_get_own_profile(client):
    r = register(client, "9600000001", role="farmer", name="Ramesh")
    token = r.json()["access_token"]
    r2 = client.get("/api/users/me", headers=auth_headers(token))
    assert r2.status_code == 200
    assert r2.json()["name"] == "Ramesh"


def test_update_own_profile_coordinates(client):
    r = register(client, "9600000002", role="farmer")
    token = r.json()["access_token"]
    r2 = client.put("/api/users/me", json={"latitude": 20.0, "longitude": 74.0},
                     headers=auth_headers(token))
    assert r2.status_code == 200
    assert r2.json()["latitude"] == 20.0
    assert r2.json()["longitude"] == 74.0


def test_update_own_profile_language(client):
    r = register(client, "9600000003", role="farmer")
    token = r.json()["access_token"]
    r2 = client.put("/api/users/me", json={"language_pref": "hi"}, headers=auth_headers(token))
    assert r2.status_code == 200
    assert r2.json()["language_pref"] == "hi"


def test_update_profile_invalid_language_rejected(client):
    r = register(client, "9600000004", role="farmer")
    token = r.json()["access_token"]
    r2 = client.put("/api/users/me", json={"language_pref": "fr"}, headers=auth_headers(token))
    assert r2.status_code == 422
