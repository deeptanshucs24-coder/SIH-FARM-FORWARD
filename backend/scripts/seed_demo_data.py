"""
Quick demo-data seeder so you have something to test against immediately.
Run with: python3 -m scripts.seed_demo_data   (from the backend/ folder, venv active)

This is NOT the real Agmarknet ingestion pipeline (that's M3's job) - just
enough fake rows to prove every endpoint works end to end.
"""
import datetime
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal, Base, engine
from app.models.crop import Crop
from app.models.market import Market
from app.models.market_price import MarketPrice
from app.models import user, farmer_produce, buyer, buyer_requirement, price_prediction, transport_rate, recommendation, notification  # noqa

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    if db.query(Crop).count() > 0:
        print("Demo data already present, skipping.")
    else:
        onion = Crop(crop_name="Onion", variety="Red")
        tomato = Crop(crop_name="Tomato", variety="Hybrid")
        db.add_all([onion, tomato])
        db.commit()
        db.refresh(onion)
        db.refresh(tomato)

        nashik = Market(market_name="Nashik APMC", location="Nashik, Maharashtra", latitude=19.9975, longitude=73.7898)
        pune = Market(market_name="Pune Mandi", location="Pune, Maharashtra", latitude=18.5204, longitude=73.8567)
        db.add_all([nashik, pune])
        db.commit()
        db.refresh(nashik)
        db.refresh(pune)

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        two_days_ago = today - datetime.timedelta(days=2)

        db.add_all([
            # Onion @ Nashik - 3 days of history, today's row is the "current" price
            MarketPrice(market_id=nashik.market_id, crop_id=onion.crop_id, price_date=two_days_ago,
                        min_price=1600, max_price=1850, average_price=1720),
            MarketPrice(market_id=nashik.market_id, crop_id=onion.crop_id, price_date=yesterday,
                        min_price=1650, max_price=1900, average_price=1780),
            MarketPrice(market_id=nashik.market_id, crop_id=onion.crop_id, price_date=today,
                        min_price=1700, max_price=1950, average_price=1820),

            # Onion @ Pune - only today, to prove the fix also works with sparse history
            MarketPrice(market_id=pune.market_id, crop_id=onion.crop_id, price_date=today,
                        min_price=1650, max_price=1850, average_price=1750),

            # Tomato @ Nashik
            MarketPrice(market_id=nashik.market_id, crop_id=tomato.crop_id, price_date=today,
                        min_price=900, max_price=1200, average_price=1050),
        ])
        db.commit()
        print(f"Seeded: crops(onion={onion.crop_id}, tomato={tomato.crop_id}), "
              f"markets(nashik={nashik.market_id}, pune={pune.market_id})")
        print("Onion@Nashik has 3 days of price history - use this to verify "
              "/api/market-prices returns only today's row while "
              "/api/market-prices/history returns all 3.")
finally:
    db.close()
