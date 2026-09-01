"""
Shared pytest fixtures. Uses SQLite by default (fast, no external
dependency), but the exact same suite can be pointed at a real Postgres
instance by setting DATABASE_URL before running pytest - the fixtures work
identically either way (drop/create tables per test function).

ML_SERVICE_URL/RANKING_SERVICE_URL point at unreachable ports on purpose,
so every run exercises the mock-fallback path deterministically.
"""
import os
import sys
import pathlib
import datetime

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

if "DATABASE_URL" not in os.environ:
    _TEST_DB_PATH = pathlib.Path(__file__).resolve().parent / "test_pytest.db"
    os.environ["DATABASE_URL"] = f"sqlite:///{_TEST_DB_PATH}"
os.environ.setdefault("ML_SERVICE_URL", "http://localhost:9999")
os.environ.setdefault("RANKING_SERVICE_URL", "http://localhost:9998")
os.environ.setdefault("JWT_SECRET_KEY", "test-secret-not-for-production")

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402
from app.core.database import Base, engine, SessionLocal  # noqa: E402
from app.models.market import Market  # noqa: E402
from app.models.market_price import MarketPrice  # noqa: E402


@pytest.fixture
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def seeded(client):
    """One market (with coordinates) and 3 days of onion price history -
    enough to test current-price, history, and recommend-market meaningfully."""
    db = SessionLocal()
    try:
        market = Market(name="Nashik APMC", state="Maharashtra", district="Nashik", lat=19.99, lng=73.78)
        db.add(market)
        db.commit()
        db.refresh(market)

        today = datetime.date.today()
        db.add_all([
            MarketPrice(market_id=market.id, crop_name="onion",
                        price_per_quintal=1720, date=today - datetime.timedelta(days=2)),
            MarketPrice(market_id=market.id, crop_name="onion",
                        price_per_quintal=1780, date=today - datetime.timedelta(days=1)),
            MarketPrice(market_id=market.id, crop_name="onion",
                        price_per_quintal=1820, date=today),
        ])
        db.commit()
        return {"market_id": str(market.id), "crop_name": "onion"}
    finally:
        db.close()


def register(client, phone, role="farmer", **kwargs):
    payload = {
        "name": kwargs.get("name", "Test User"),
        "phone": phone,
        "password": kwargs.get("password", "test1234"),
        "role": role,
        "language_pref": kwargs.get("language_pref", "en"),
        "latitude": kwargs.get("latitude", 19.99),
        "longitude": kwargs.get("longitude", 73.78),
    }
    return client.post("/api/register", json=payload)


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}
