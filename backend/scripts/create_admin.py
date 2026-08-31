"""
Creates an ADMIN user directly in the database, bypassing the public
/api/register endpoint (which deliberately only allows FARMER/BUYER).

This is a stopgap until the team decides on a proper admin workflow
(e.g. an invite-only endpoint, a super-admin bootstrap flow, etc).
Flagged in README under "Flag for team".

Usage (from backend/, with venv active):
    python3 -m scripts.create_admin
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal, Base, engine
from app.core.security import hash_password
from app.models.user import User
from app.models import crop, farmer_produce, market, market_price, buyer, buyer_requirement, price_prediction, transport_rate, recommendation, notification  # noqa

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    print("=== Create an ADMIN account (bypasses public registration) ===")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    password = input("Password (min 6 chars): ").strip()
    location = input("Location: ").strip() or "HQ"

    if len(password) < 6:
        print("Password must be at least 6 characters. Aborting.")
        sys.exit(1)

    existing = db.query(User).filter(User.phone == phone).first()
    if existing:
        print(f"A user with phone {phone} already exists (role={existing.role}). Aborting.")
        sys.exit(1)

    admin = User(
        name=name,
        phone=phone,
        password_hash=hash_password(password),
        role="ADMIN",
        location=location,
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    print(f"Created ADMIN user_id={admin.user_id}, phone={admin.phone}")
finally:
    db.close()
