def test_current_price_returns_only_latest_row(client, seeded):
    r = client.get("/api/market-prices", params={"crop_name": "onion"})
    assert r.status_code == 200
    rows = r.json()
    assert len(rows) == 1  # one market seeded
    assert rows[0]["price_per_quintal"] == 1820.0  # today's, not an older row


def test_price_history_returns_all_days(client, seeded):
    r = client.get("/api/market-prices/history", params={"crop_name": "onion", "days": 30})
    assert r.status_code == 200
    assert len(r.json()) == 3


def test_market_prices_filter_by_market_id(client, seeded):
    r = client.get("/api/market-prices", params={"crop_name": "onion", "market_id": seeded["market_id"]})
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_market_prices_case_insensitive_crop_name(client, seeded):
    r = client.get("/api/market-prices", params={"crop_name": "ONION"})
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_market_prices_unknown_crop_returns_empty_not_404(client, seeded):
    """crop_name is free text (no reference table) - an unpriced crop is a
    valid empty result, not an error."""
    r = client.get("/api/market-prices", params={"crop_name": "durian"})
    assert r.status_code == 200
    assert r.json() == []


def test_market_prices_invalid_market_id_returns_404(client, seeded):
    import uuid
    r = client.get("/api/market-prices", params={"crop_name": "onion", "market_id": str(uuid.uuid4())})
    assert r.status_code == 404


def test_price_history_invalid_market_id_returns_404(client, seeded):
    import uuid
    r = client.get("/api/market-prices/history", params={"crop_name": "onion", "market_id": str(uuid.uuid4())})
    assert r.status_code == 404
