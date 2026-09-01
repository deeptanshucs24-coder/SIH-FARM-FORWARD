"""
Quick demo-data seeder for local testing (SQLite or Postgres).

This deliberately mirrors M3's actual data/seed_demo_data.sql - same
market names/coordinates/fixed UUIDs, same farmer/buyer names - so demo
data lines up identically whether you seed via M3's raw SQL against
Postgres or this Python script (e.g. for quick SQLite-based local dev).

NOTE: M3's own seed_demo_data.sql has a bug - the bcrypt hash included
there does NOT actually correspond to the documented password "demo1234"
(verified independently). This script computes a REAL, correct hash for
"demo1234" so login actually works. Worth flagging to M3/the team.

Run with: python3 -m scripts.seed_demo_data   (from backend/, venv active)
"""
import datetime
import uuid
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal, Base, engine
from app.core.security import hash_password
from app.models.user import User
from app.models.market import Market
from app.models.market_price import MarketPrice
from app.models.crop_listing import CropListing
from app.models.buyer_requirement import BuyerRequirement
from app.models import price_prediction, match  # noqa - register with metadata

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Same fixed UUIDs as M3's data/seed_demo_data.sql, for consistency.
NASHIK = uuid.UUID("11111111-1111-1111-1111-111111111111")
PUNE = uuid.UUID("22222222-2222-2222-2222-222222222222")
LASALGAON = uuid.UUID("33333333-3333-3333-3333-333333333333")
MUMBAI_VASHI = uuid.UUID("44444444-4444-4444-4444-444444444444")
RAMESH = uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
SUNIL = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb")
AGRI_OFFICER = uuid.UUID("cccccccc-cccc-cccc-cccc-cccccccccccc")
RAMESH_LISTING = uuid.UUID("dddddddd-dddd-dddd-dddd-dddddddddddd")

try:
    if db.query(Market).count() > 0:
        print("Demo data already present, skipping.")
    else:
        demo_hash = hash_password("demo1234")  # correctly computed, unlike M3's SQL file

        db.add_all([
            Market(id=NASHIK, name="Nashik APMC", state="Maharashtra", district="Nashik", lat=19.9975, lng=73.7898),
            Market(id=PUNE, name="Pune Mandi", state="Maharashtra", district="Pune", lat=18.5204, lng=73.8567),
            Market(id=LASALGAON, name="Lasalgaon APMC", state="Maharashtra", district="Nashik", lat=20.1500, lng=74.2400),
            Market(id=MUMBAI_VASHI, name="Mumbai Vashi APMC", state="Maharashtra", district="Thane", lat=19.0760, lng=72.9987),
        ])
        db.add_all([
            User(id=RAMESH, name="Ramesh Patil", phone="9990000001", password_hash=demo_hash,
                 role="farmer", language_pref="hi", location_lat=19.9900, location_lng=73.7800),
            User(id=SUNIL, name="Sunil Traders", phone="9990000002", password_hash=demo_hash,
                 role="buyer", language_pref="en", location_lat=18.5204, location_lng=73.8567),
            User(id=AGRI_OFFICER, name="Agri Officer", phone="9990000003", password_hash=demo_hash,
                 role="admin", language_pref="en", location_lat=19.9975, location_lng=73.7898),
        ])
        db.commit()

        today = datetime.date.today()
        prices = [
            (NASHIK, "onion", 1720, today - datetime.timedelta(days=6)),
            (NASHIK, "onion", 1760, today - datetime.timedelta(days=5)),
            (NASHIK, "onion", 1780, today - datetime.timedelta(days=4)),
            (NASHIK, "onion", 1800, today - datetime.timedelta(days=3)),
            (NASHIK, "onion", 1810, today - datetime.timedelta(days=2)),
            (NASHIK, "onion", 1815, today - datetime.timedelta(days=1)),
            (NASHIK, "onion", 1820, today),
            (PUNE, "onion", 1680, today - datetime.timedelta(days=3)),
            (PUNE, "onion", 1720, today - datetime.timedelta(days=1)),
            (PUNE, "onion", 1750, today),
            (LASALGAON, "onion", 1700, today - datetime.timedelta(days=2)),
            (LASALGAON, "onion", 1740, today),
            (MUMBAI_VASHI, "onion", 1850, today - datetime.timedelta(days=1)),
            (MUMBAI_VASHI, "onion", 1870, today),
            (NASHIK, "tomato", 1200, today),
            (PUNE, "tomato", 1150, today),
            (NASHIK, "wheat", 2400, today),
            (PUNE, "wheat", 2380, today),
        ]
        db.add_all([
            MarketPrice(market_id=m, crop_name=c, price_per_quintal=p, date=d) for m, c, p, d in prices
        ])

        db.add(CropListing(
            id=RAMESH_LISTING, farmer_id=RAMESH, crop_name="onion",
            quantity_kg=500, grade="A", harvest_date=today, status="listed",
        ))
        db.add(BuyerRequirement(buyer_id=SUNIL, crop_name="onion", quantity_needed_kg=1000))
        db.commit()

        print("Seeded (mirrors M3's data/seed_demo_data.sql exactly, same fixed UUIDs).")
        print("Demo login: phone 9990000001 / password demo1234 (farmer Ramesh)")
        print("            phone 9990000002 / password demo1234 (buyer Sunil)")
        print("Onion @ Nashik has 7 days of price history for testing current-vs-history.")
finally:
    db.close()
