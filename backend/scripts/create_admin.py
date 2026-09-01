"""
Creates an admin user directly in the database, bypassing the public
/api/register endpoint (which only allows farmer/buyer).

Usage (from backend/, venv active): python3 -m scripts.create_admin
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal, Base, engine
from app.core.security import hash_password
from app.models.user import User
from app.models import market, crop_listing, market_price, price_prediction, buyer_requirement, match  # noqa

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    print("=== Create an admin account (bypasses public registration) ===")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    password = input("Password (min 6 chars): ").strip()

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
        role="admin",
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    print(f"Created admin id={admin.id}, phone={admin.phone}")
finally:
    db.close()
