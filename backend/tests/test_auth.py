from tests.conftest import register


def test_register_farmer_succeeds(client):
    r = register(client, "9000000001", role="FARMER")
    assert r.status_code == 201
    assert r.json()["user"]["role"] == "FARMER"


def test_register_buyer_succeeds(client):
    r = register(client, "9000000002", role="BUYER")
    assert r.status_code == 201
    assert r.json()["user"]["role"] == "BUYER"


def test_register_admin_is_rejected(client):
    """Critical fix: public registration must NOT allow arbitrary ADMIN creation."""
    r = client.post("/api/register", json={
        "name": "Sneaky Admin", "phone": "9000000003", "password": "test1234",
        "role": "ADMIN", "location": "X",
    })
    assert r.status_code == 422  # rejected by Pydantic pattern validation before it ever reaches the DB


def test_duplicate_phone_rejected(client):
    register(client, "9000000004", role="FARMER")
    r = register(client, "9000000004", role="FARMER")
    assert r.status_code == 409


def test_login_with_correct_password_succeeds(client):
    register(client, "9000000005", role="FARMER", password="correctpw")
    r = client.post("/api/login", json={"phone": "9000000005", "password": "correctpw"})
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_login_with_wrong_password_rejected(client):
    register(client, "9000000006", role="FARMER", password="correctpw")
    r = client.post("/api/login", json={"phone": "9000000006", "password": "wrongpw"})
    assert r.status_code == 401


def test_login_with_unknown_phone_rejected(client):
    r = client.post("/api/login", json={"phone": "9999999999", "password": "whatever1"})
    assert r.status_code == 401
