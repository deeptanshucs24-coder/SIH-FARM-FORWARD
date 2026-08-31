def test_current_price_returns_only_latest_row_per_market(client, seeded):
    """The bug this guards against: an earlier version returned every
    historical row here instead of just the latest one per market."""
    r = client.get("/api/market-prices", params={"crop_id": seeded["crop_id"]})
    assert r.status_code == 200
    rows = r.json()
    assert len(rows) == 1  # only one market was seeded -> exactly one row
    assert rows[0]["average_price"] == 1820.0  # today's price, not an older one


def test_price_history_returns_all_days(client, seeded):
    r = client.get("/api/market-prices/history", params={"crop_id": seeded["crop_id"], "days": 30})
    assert r.status_code == 200
    rows = r.json()
    assert len(rows) == 3  # all 3 seeded days


def test_price_history_respects_day_filter(client, seeded):
    # days=1 means "since 1 day ago" -> includes today AND yesterday (>= boundary)
    r = client.get("/api/market-prices/history", params={"crop_id": seeded["crop_id"], "days": 1})
    assert r.status_code == 200
    assert len(r.json()) == 2

    # days=2 -> includes all 3 seeded rows (today, yesterday, 2 days ago)
    r2 = client.get("/api/market-prices/history", params={"crop_id": seeded["crop_id"], "days": 2})
    assert r2.status_code == 200
    assert len(r2.json()) == 3

    # days below the endpoint's minimum (1) is rejected as invalid input
    r3 = client.get("/api/market-prices/history", params={"crop_id": seeded["crop_id"], "days": 0})
    assert r3.status_code == 422


def test_market_prices_filter_by_market_id(client, seeded):
    r = client.get("/api/market-prices", params={
        "crop_id": seeded["crop_id"], "market_id": seeded["market_id"],
    })
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_market_prices_invalid_crop_returns_404(client, seeded):
    r = client.get("/api/market-prices", params={"crop_id": 99999})
    assert r.status_code == 404


def test_price_history_invalid_crop_returns_404(client, seeded):
    r = client.get("/api/market-prices/history", params={"crop_id": 99999})
    assert r.status_code == 404
