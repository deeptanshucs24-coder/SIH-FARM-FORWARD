"""
Shared pytest fixtures. Uses a real (file-based) SQLite database so behavior
matches production SQL semantics closely, with tables dropped/recreated
before every single test function for full isolation - no test can leak
state into another.

ML_SERVICE_URL/RANKING_SERVICE_URL are pointed at unreachable ports on
purpose, so every test run exercises the mock-fallback path deterministically
(no real M4/M5 service needed to run the test suite).
"""
import os
import sys
import pathlib
import datetime

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

_TEST_DB_PATH = pathlib.Path(__file__).resolve().parent / "test_pytest.db"
os.environ["DATABASE_URL"] = f"sqlite:///{_TEST_DB_PATH}"
os.environ["ML_SERVICE_URL"] = "http://localhost:9999"
os.environ["RANKING_SERVICE_URL"] = "http://localhost:9998"
os.environ["JWT_SECRET_KEY"] = "test-secret-not-for-production"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402
from app.core.database import Base, engine, SessionLocal  # noqa: E402
from app.models.crop import Crop  # noqa: E402
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
    """One crop, one market, and 3 days of price history (today + 2 back) -
    enough to test both current-price and history endpoints meaningfully."""
    db = SessionLocal()
    try:
        crop = Crop(crop_name="Onion", variety="Red")
        db.add(crop)
        db.commit()
        db.refresh(crop)

        market = Market(market_name="Nashik APMC", location="Nashik", latitude=19.99, longitude=73.78)
        db.add(market)
        db.commit()
        db.refresh(market)

        today = datetime.date.today()
        db.add_all([
            MarketPrice(market_id=market.market_id, crop_id=crop.crop_id,
                        price_date=today - datetime.timedelta(days=2),
                        min_price=1600, max_price=1850, average_price=1720),
            MarketPrice(market_id=market.market_id, crop_id=crop.crop_id,
                        price_date=today - datetime.timedelta(days=1),
                        min_price=1650, max_price=1900, average_price=1780),
            MarketPrice(market_id=market.market_id, crop_id=crop.crop_id,
                        price_date=today,
                        min_price=1700, max_price=1950, average_price=1820),
        ])
        db.commit()
        return {"crop_id": crop.crop_id, "market_id": market.market_id}
    finally:
        db.close()


def register(client, phone, role="FARMER", **kwargs):
    payload = {
        "name": kwargs.get("name", "Test User"),
        "phone": phone,
        "password": kwargs.get("password", "test1234"),
        "role": role,
        "location": kwargs.get("location", "Nashik"),
        "latitude": kwargs.get("latitude", 19.99),
        "longitude": kwargs.get("longitude", 73.78),
    }
    return client.post("/api/register", json=payload)


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}
