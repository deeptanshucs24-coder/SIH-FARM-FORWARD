from tests.conftest import register


def test_register_farmer_succeeds(client):
    r = register(client, "9000000001", role="farmer")
    assert r.status_code == 201
    assert r.json()["user"]["role"] == "farmer"


def test_register_buyer_succeeds(client):
    r = register(client, "9000000002", role="buyer")
    assert r.status_code == 201
    assert r.json()["user"]["role"] == "buyer"


def test_register_admin_is_rejected(client):
    r = client.post("/api/register", json={
        "name": "Sneaky Admin", "phone": "9000000003", "password": "test1234", "role": "admin",
    })
    assert r.status_code == 422


def test_register_uppercase_role_rejected(client):
    """M3's DB CHECK constraint requires lowercase exactly - confirm we
    validate that at the API layer too, not just rely on the DB to reject it."""
    r = client.post("/api/register", json={
        "name": "X", "phone": "9000000009", "password": "test1234", "role": "FARMER",
    })
    assert r.status_code == 422


def test_duplicate_phone_rejected(client):
    register(client, "9000000004", role="farmer")
    r = register(client, "9000000004", role="farmer")
    assert r.status_code == 409


def test_login_with_correct_password_succeeds(client):
    register(client, "9000000005", role="farmer", password="correctpw")
    r = client.post("/api/login", json={"phone": "9000000005", "password": "correctpw"})
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_login_with_wrong_password_rejected(client):
    register(client, "9000000006", role="farmer", password="correctpw")
    r = client.post("/api/login", json={"phone": "9000000006", "password": "wrongpw"})
    assert r.status_code == 401


def test_login_with_unknown_phone_rejected(client):
    r = client.post("/api/login", json={"phone": "9999999999", "password": "whatever1"})
    assert r.status_code == 401


def test_register_response_id_is_valid_uuid(client):
    import uuid
    r = register(client, "9000000007", role="farmer")
    user_id = r.json()["user"]["id"]
    uuid.UUID(user_id)  # raises ValueError if not a valid UUID
