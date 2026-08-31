def test_get_crops_returns_seeded_crops(client, seeded):
    r = client.get("/api/crops")
    assert r.status_code == 200
    body = r.json()
    assert len(body) == 1
    assert body[0]["crop_id"] == seeded["crop_id"]
    assert body[0]["crop_name"] == "Onion"
    assert body[0]["variety"] == "Red"


def test_get_crops_empty_when_none_seeded(client):
    r = client.get("/api/crops")
    assert r.status_code == 200
    assert r.json() == []
