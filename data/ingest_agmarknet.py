"""
============================================================
MandiSetu — Agmarknet Data Ingestion
Owner: M3 (Database & Agriculture Data Pipeline)
============================================================
WHAT THIS DOES
  Loads real mandi price data into the `markets` and `market_prices`
  tables. Two ways to get data:

    MODE 1 (recommended for demo): --csv path/to/file.csv
        Reads a CSV you downloaded from data.gov.in. Works offline,
        so it's your safe demo-day fallback.

    MODE 2 (live): --api
        Pulls current prices from the data.gov.in API. Needs a free
        API key (see README_M3.md). Good for a "live data" demo moment.

HOW TO RUN  (examples)
    python ingest_agmarknet.py --csv agmarknet_prices.csv
    python ingest_agmarknet.py --api --records 500

The Agmarknet CSV/API columns are:
    State, District, Market, Commodity, Variety, Grade,
    Arrival_Date, Min_Price, Max_Price, Modal_Price
We store Market -> markets table, and Modal_Price -> market_prices.
============================================================
"""

import argparse
import csv
import os
import sys
import uuid
from datetime import datetime

import psycopg as psycopg2                    # PostgreSQL driver
import requests                    # only used in --api mode

# ------------------------------------------------------------
# DATABASE CONNECTION
# Reads connection info from an env var if present, else uses defaults.
# Set it once in your terminal so you don't hardcode a password:
#   export DATABASE_URL="postgresql://user:pass@localhost:5432/mandisetu"
# ------------------------------------------------------------
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/mandisetu"
)

# data.gov.in "Current Daily Price of Various Commodities" resource id.
API_RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"
API_BASE = f"https://api.data.gov.in/resource/{API_RESOURCE_ID}"
# Free sample key from data.gov.in — replace with your own for real use.
API_KEY = os.getenv("DATA_GOV_API_KEY", "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b")

# Only load these crops for the MVP (keeps the demo focused + fast).
TARGET_CROPS = {"onion", "tomato", "potato", "wheat", "rice",
                "maize", "brinjal", "bhindi(ladies finger)", "green chilli", "cauliflower", "cabbage", "carrot", "cucumbar(kheera)", "banana"}


def connect():
    """Open a database connection, or exit with a clear message."""
    try:
        return psycopg2.connect(DATABASE_URL)
    except Exception as e:
        sys.exit(f"[ERROR] Could not connect to the database:\n  {e}\n"
                 f"Check your DATABASE_URL and that Postgres is running.")


def to_float(value):
    """Turn a price string into a number; return None if it's junk."""
    try:
        return float(str(value).replace(",", "").strip())
    except (ValueError, TypeError):
        return None


def parse_date(value):
    """Agmarknet dates look like 05/09/2026 or 2026-09-05. Handle both."""
    value = str(value).strip()
    for fmt in ("%d/%m/%Y", "%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def get_or_create_market(cur, market_cache, name, state, district):
    """Return the UUID for a market, creating the row if it's new.
    market_cache avoids hitting the DB for markets we've already seen."""
    key = (name or "").lower().strip()
    if not key:
        return None
    if key in market_cache:
        return market_cache[key]

    cur.execute("SELECT id FROM markets WHERE LOWER(name) = %s", (key,))
    row = cur.fetchone()
    if row:
        market_cache[key] = row[0]
        return row[0]

    new_id = str(uuid.uuid4())
    cur.execute(
        "INSERT INTO markets (id, name, state, district, lat, lng) "
        "VALUES (%s, %s, %s, %s, NULL, NULL)",
        (new_id, name.strip(), state, district)
    )
    market_cache[key] = new_id
    return new_id


def insert_rows(rows):
    """Take a list of dict rows (already cleaned) and write to DB."""
    conn = connect()
    cur = conn.cursor()
    market_cache = {}
    inserted, skipped = 0, 0

    for r in rows:
        crop = (r.get("commodity") or "").lower().strip()
        if crop not in TARGET_CROPS:
            skipped += 1
            continue

        price = to_float(r.get("modal_price"))
        date_ = parse_date(r.get("arrival_date"))
        if price is None or date_ is None:
            skipped += 1
            continue

        market_id = get_or_create_market(
            cur, market_cache,
            r.get("market"), r.get("state"), r.get("district")
        )
        if not market_id:
            skipped += 1
            continue

        cur.execute(
            "INSERT INTO market_prices "
            "(market_id, crop_name, price_per_quintal, date) "
            "VALUES (%s, %s, %s, %s)",
            (market_id, crop, price, date_)
        )
        inserted += 1

    conn.commit()
    cur.close()
    conn.close()
    print(f"[DONE] Inserted {inserted} price rows. Skipped {skipped}.")
    print(f"[INFO] Markets in cache this run: {len(market_cache)}")


def load_from_csv(path):
    """Read a downloaded Agmarknet CSV and normalise column names."""
    if not os.path.exists(path):
        sys.exit(f"[ERROR] CSV not found: {path}")

    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        # Normalise headers: lower-case, spaces/x0020 -> underscore.
        for raw in reader:
            r = {k.lower().strip().replace("_x0020_", "_").replace("_x0020_", "_").replace("_x0020_", "_").replace(" ", "_"): v
                 for k, v in raw.items()}
            rows.append({
                "state":        r.get("state"),
                "district":     r.get("district") or r.get("district_name"),
                "market":       r.get("market") or r.get("market_name"),
                "commodity":    r.get("commodity"),
                "arrival_date": r.get("arrival_date") or r.get("price_date"),
                "modal_price":  r.get("modal_price"),
            })
    print(f"[INFO] Read {len(rows)} rows from CSV.")
    insert_rows(rows)


def load_from_api(limit):
    """Pull current prices live from data.gov.in."""
    print("[INFO] Fetching live data from data.gov.in ...")
    params = {"api-key": API_KEY, "format": "json", "limit": limit}
    try:
        resp = requests.get(API_BASE, params=params, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        sys.exit(f"[ERROR] API request failed:\n  {e}\n"
                 f"Tip: use --csv mode instead for a reliable offline load.")

    records = resp.json().get("records", [])
    print(f"[INFO] API returned {len(records)} records.")
    rows = [{
        "state":        rec.get("state"),
        "district":     rec.get("district"),
        "market":       rec.get("market"),
        "commodity":    rec.get("commodity"),
        "arrival_date": rec.get("arrival_date"),
        "modal_price":  rec.get("modal_price"),
    } for rec in records]
    insert_rows(rows)


def main():
    p = argparse.ArgumentParser(description="Load Agmarknet prices into DB.")
    p.add_argument("--csv", help="Path to a downloaded Agmarknet CSV file.")
    p.add_argument("--api", action="store_true", help="Pull live from data.gov.in.")
    p.add_argument("--records", type=int, default=500,
                   help="Max records to pull in --api mode (default 500).")
    args = p.parse_args()

    if args.csv:
        load_from_csv(args.csv)
    elif args.api:
        load_from_api(args.records)
    else:
        p.print_help()
        print("\n[HINT] Give me either --csv <file> or --api.")


if __name__ == "__main__":
    main()
