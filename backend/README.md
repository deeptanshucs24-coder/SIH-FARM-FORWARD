# FarmForward Backend (Member 2 — Core API)

FastAPI backend for SIH26132 — Farmer Market Linkage & Price Discovery.

**This version is aligned with M3's ACTUAL implemented database schema**
(`feature/m3-database`, `database/schema.sql`) — PostgreSQL, UUID primary
keys, 7 tables: `users`, `markets`, `crop_listings`, `market_prices`,
`price_predictions`, `buyers_requirements`, `matches`.

This is a genuine architecture change from the previous round, not a
rename. The earlier version was built against a different schema
interpretation (integer IDs, a separate `crops` reference table, a separate
`buyers` table with verification status). None of that exists in M3's real
schema. Everything below was rebuilt from the API layer down to the
database layer to match M3's actual DDL exactly.

**Status: 65/65 tests passing — verified against BOTH SQLite (fast local
dev) AND a real, locally-installed PostgreSQL instance running M3's actual
`schema.sql` unmodified.** This isn't a claim - see "How this was tested"
below for exactly what was run.

## Owns
- Auth (register/login, JWT, role-based: farmer/buyer, admin handled separately)
- Own-profile endpoints (`/api/users/me`)
- Crop listing CRUD (`crop_listings` table), strictly ownership-scoped via JWT
- Buyer-interest / matches flow (`matches` table) - new this round, see below
- Market price read endpoints (current + historical, crop_name-based)
- Buyer listing + buyer requirements (`buyers_requirements` table)
- Orchestration: `/api/predict-price` (calls M4) and `/api/recommend-market`
  (calls M5, falls back to local scoring), plus a stateless `/api/calculate-profit`

## Setup

### Option A — against a real Postgres instance (recommended, matches production)

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 1. Make sure M3's schema is loaded first (see their data/README_M3.md):
#    psql -U postgres -c "CREATE DATABASE mandisetu;"
#    psql -U postgres -d mandisetu -f database/schema.sql
# 2. Then:
cp .env.example .env              # DATABASE_URL already matches M3's convention
uvicorn app.main:app --reload --port 8000
```

### Option B — SQLite, for quick local iteration without Postgres installed

```bash
# same venv/install steps, then:
cp .env.example .env
# edit .env: DATABASE_URL=sqlite:///./test.db
uvicorn app.main:app --reload --port 8000
```

Either way: Swagger UI at http://localhost:8000/docs, health check at
http://localhost:8000/health.

## Local testing / demo data

```bash
python3 -m scripts.seed_demo_data
```

This mirrors M3's own `data/seed_demo_data.sql` **exactly** - same 4
markets (Nashik/Pune/Lasalgaon/Mumbai Vashi), same fixed UUIDs, same
farmer (Ramesh Patil)/buyer (Sunil Traders)/admin (Agri Officer), same
7-day onion price history. Demo login: phone `9990000001` / password
`demo1234` (farmer).

**Bug found in M3's own seed file:** `data/seed_demo_data.sql`'s comment
says the bcrypt hash corresponds to password `demo1234`, but it doesn't -
independently verified with `passlib.verify()`, it matches neither
`demo1234` nor several other common test passwords. Logging in with M3's
raw SQL-seeded data and that documented password will fail. **Worth
flagging to M3** - not something I changed in their file. Our own
`scripts/seed_demo_data.py` computes a correct hash, so login works if you
seed via this Python script instead.

## Creating an admin account

```bash
python3 -m scripts.create_admin
```

Public registration only allows `farmer`/`buyer` - same reasoning as
before, unchanged this round.

## How this was tested (not just claimed)

1. Installed PostgreSQL 16 locally, created a `mandisetu` database, and ran
   M3's actual `database/schema.sql` **completely unmodified**.
2. Ran M3's actual `data/seed_demo_data.sql` **completely unmodified**.
3. Started this backend against that real database and ran a full manual
   flow: register, login, create a crop listing, view current market prices
   (matching M3's exact seeded numbers), get a market recommendation
   (verified the distance/profit ranking makes geographic sense against the
   real Nashik/Pune/Lasalgaon/Mumbai coordinates), buyer expresses interest,
   farmer accepts it, listing status correctly flows
   listed → interested → confirmed, buyer posts a requirement, price
   prediction persists correctly.
4. Verified directly via `psql` that the data written by the API actually
   landed correctly in M3's real tables.
5. Verified Postgres's own CHECK constraints reject bad data even if
   Pydantic validation were bypassed entirely (tested by inserting directly
   via SQLAlchemy, skipping the API layer) - confirms the DB itself is a
   real last line of defense, not just decoration.
6. Ran the full 65-test pytest suite against SQLite (fast local iteration).
7. Ran the **exact same 65-test suite again with `DATABASE_URL` pointed at
   the real Postgres instance** running M3's schema - all 65 passed there
   too, with zero test changes needed.
8. Compiled every `.py` file, confirmed all 21 API routes register, copied
   to a fresh folder and reinstalled from `requirements.txt` from scratch.

## Major differences from the previous round (read this before reviewing)

This is a full schema realignment, not a patch. Every one of these is a
consequence of M3's actual DDL, not a preference:

| Concept | Previous round | This round (matches M3) |
|---|---|---|
| Primary keys | Integer, auto-increment | **UUID**, `gen_random_uuid()` |
| Crop reference | Separate `crops` table, `crop_id` FK | **No crops table** - `crop_name` is free text everywhere |
| Farmer listings | `farmer_produce` table | **`crop_listings`** table (also has `grade`, `status` fields that didn't exist before) |
| Market prices | `min_price`/`max_price`/`average_price` | **Single `price_per_quintal`** value |
| Buyers | Separate `buyers` table w/ `verification_status` (PENDING/VERIFIED/REJECTED) | **No separate buyers table at all** - a buyer IS a `users` row with `role='buyer'`. **No verification concept exists anywhere in the schema.** |
| Roles | Uppercase (`FARMER`/`BUYER`/`ADMIN`) | **Lowercase** (`farmer`/`buyer`/`admin`) - matches DB CHECK constraint exactly |
| Recommendation persistence | Saved to a `recommendations` table | **No such table exists** - `recommend-market` is now purely computational, nothing persisted |
| Buyer-farmer interest | Didn't exist | **New**: `matches` table + `/interest`, `/matches` endpoints (this table existed in M3's schema with no owner before) |
| `location` (free text) | A field on `users` | **Doesn't exist** - only `location_lat`/`location_lng` floats |
| `expected_price` on produce | Existed | **Doesn't exist** in M3's `crop_listings` table - dropped |

## Flag for team — please confirm

1. **Buyer verification is completely unimplemented at the DB level.**
   The PRD's documented flow (Buyer Registration → PENDING → Admin Review →
   VERIFIED → eligible for farmer-facing linkage) has **no supporting
   column anywhere** in M3's actual schema - not on `users`, not anywhere
   else. `GET /api/buyers` currently returns every buyer, unfiltered. If the
   team wants verification enforced, that requires M3 to add a column
   (e.g. `users.verification_status` or similar) - this is a schema change,
   not something I can safely invent.
2. **`GET /api/crops` is now derived dynamically**, not read from a
   reference table (none exists). It returns the distinct `crop_name`
   values currently present across `market_prices` and `crop_listings`.
   Reasonable adaptation, but flagging since it's an interpretive choice,
   not something either document explicitly specifies.
3. **Recommendation history is no longer persisted anywhere** - the
   `recommendations` table from the previous round doesn't exist in M3's
   schema, and the Master Plan's Part 10 schema (which M3 implemented)
   never included one either. If the team wants recommendation history
   tracked, that's a new table M3 would need to add.
4. **M3's `data/seed_demo_data.sql` has an incorrect password hash** (see
   above) - worth a quick fix on M3's side.
5. **Transport/distance calculation** - still a placeholder (haversine +
   flat rate) in `app/services/transport.py`. Needs M6's real
   formula/provider. Unchanged from previous rounds.
6. **M4 prediction contract** - M4's actual service (`ml/app.py` in M3's
   branch) is currently an empty stub, so the mock fallback is still in
   use. Its shape now matches the Master Plan's Part 4.1 example exactly
   (`predicted_price`/`range_min`/`range_max`/`confidence`/`distress_flag`),
   since that's both the documented contract AND M3's actual
   `price_predictions` table columns - not a guess.
7. **M5 ranking contract** - M5's service doesn't exist yet either; local
   fallback scoring unchanged in spirit from previous rounds.
8. **PATCH vs PUT** for listing updates - used PATCH (partial update),
   consistent with previous rounds' decision.

## Endpoints

| Method | Path | Auth | Purpose |
|---|---|---|---|
| POST | /api/register | - | Register farmer/buyer (not admin) |
| POST | /api/login | - | Login, returns JWT |
| GET | /api/users/me | any | Get your own profile |
| PUT | /api/users/me | any | Update your own profile |
| GET | /api/crops | - | Distinct crop names currently in the system |
| POST | /api/farmer/produce | farmer | Create a crop listing |
| GET | /api/farmer/produce | farmer | List your own listings |
| GET | /api/farmer/produce/{id} | owner only | Read one listing |
| PATCH | /api/farmer/produce/{id} | owner only | Update one listing |
| DELETE | /api/farmer/produce/{id} | owner only | Delete one listing |
| POST | /api/farmer/produce/{id}/interest | buyer | Express interest (creates a match) |
| GET | /api/farmer/produce/{id}/matches | owner only | View interested buyers |
| PATCH | /api/farmer/produce/{id}/matches/{match_id} | owner only | Accept/reject a match |
| GET | /api/market-prices?crop_name=&market_id= | - | Current price per market |
| GET | /api/market-prices/history?crop_name=&market_id=&days= | - | Historical price series |
| POST | /api/predict-price | - | Get + store a fair-price prediction (calls M4) |
| POST | /api/recommend-market | farmer | Ranked market list (calls M5) |
| GET | /api/buyers | - | List buyers (all - no verification filter exists) |
| POST | /api/buyer/requirements | buyer | Post a crop requirement |
| POST | /api/calculate-profit | - | Stateless revenue/profit calculator |
| GET | /health | - | Health check |

## Project structure

```
app/
├── main.py                 # FastAPI app, router registration, lifespan, error handler
├── core/
│   ├── config.py             # env settings
│   ├── database.py           # SQLAlchemy engine/session
│   ├── security.py           # JWT + bcrypt
│   └── types.py               # NEW - portable UUID column type (Postgres native / SQLite fallback)
├── models/                   # One file per M3 table (7 total) - column names match schema.sql exactly
│   ├── user.py
│   ├── market.py
│   ├── crop_listing.py
│   ├── market_price.py
│   ├── price_prediction.py
│   ├── buyer_requirement.py
│   └── match.py               # NEW
├── schemas/                    # Pydantic - crop_name/UUID/quintal-aware throughout
├── crud/                        # DB access - one file per model, UUID-safe lookups
├── services/
│   ├── ml_client.py               # M4 - now matches the real documented contract exactly
│   ├── ranking_client.py          # M5
│   └── transport.py               # distance + profit math (unit-conversion-aware, placeholder pending M6)
├── dependencies.py            # get_db, get_current_user, require_role
└── routers/
    ├── auth.py
    ├── users.py
    ├── crops.py                   # now dynamic (no reference table)
    ├── produce.py                 # crop_listings CRUD + matches flow
    ├── market_prices.py
    ├── predict.py
    ├── recommend.py                # no longer persists anything (no table for it)
    ├── buyers.py
    └── profit.py
scripts/
├── seed_demo_data.py          # mirrors M3's real seed data exactly, with a correct password hash
└── create_admin.py
tests/                          # 65 pytest tests, verified against SQLite AND real Postgres
```

## Next steps for M2

- [ ] Bring the "Flag for team" list to the discussion - especially #1 (buyer verification) and #3 (recommendation persistence), since those are schema gaps, not implementation choices
- [ ] Tell M3 about the seed-data password hash bug
- [ ] Confirm M4's real `/predict` contract once `ml/app.py` is built (currently an empty stub)
- [ ] Confirm M5's real ranking contract once that service exists
- [ ] Get real transport rate + distance logic from M6
- [ ] Once confirmed, merge into `feature/backend`
