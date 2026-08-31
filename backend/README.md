# FarmForward Backend (Member 2 — Core API)

FastAPI backend for SIH26132 — Farmer Market Linkage & Price Discovery.
Matches the team's official `FarmForward_Database_Schema` and TRD (11-table schema).

**Status: M2 baseline complete for tonight.** Everything under M2's
responsibility that can be finished without M3/M4/M5/M6/team decisions is
done, tested, and ready for `feature/m2-backend`. **63/63 tests passing.**
Pending items are listed under "Flag for team" below - intentionally left
as placeholders per tonight's scope.

## Owns
- Auth (register/login, JWT, role-based access: FARMER / BUYER, ADMIN handled separately)
- Own-profile endpoints (`/api/users/me`)
- Farmer produce CRUD, strictly ownership-scoped via JWT
- Market price read endpoints (current + historical - correctly distinct)
- Buyer listing (verification-gated) + buyer requirements
- Orchestration: `/api/predict-price` (calls M4) and `/api/recommend-market`
  (calls M5, falls back to local scoring), plus a stateless `/api/calculate-profit`
- Input validation (phone format, coordinate bounds, quantities/prices, dates, IDs)
- Centralized error handling (no raw tracebacks/DB errors ever reach the client)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # edit DATABASE_URL, JWT_SECRET_KEY, etc.
uvicorn app.main:app --reload --port 8000
```

Swagger UI: http://localhost:8000/docs
Health check: http://localhost:8000/health

## Local testing without Postgres

Set `DATABASE_URL=sqlite:///./test.db` in `.env`. Tables auto-create on
startup. Then seed some demo data:

```bash
python3 -m scripts.seed_demo_data
```

Adds 2 crops, 2 markets, and 3 days of price history for Onion @ Nashik -
enough to see the current-vs-historical distinction yourself:
`GET /api/market-prices?crop_id=1&market_id=1` returns exactly 1 row
(today's), `GET /api/market-prices/history?crop_id=1&market_id=1` returns
all 3.

## Running the test suite

```bash
python3 -m pytest tests/ -v
```

**63/63 tests passing**, across 12 test files. Covers: authentication,
authorization/ownership, full produce CRUD, current-vs-historical prices,
profit calculation, buyer verification gating, both orchestration endpoints'
mock-fallback behavior, health check, crops listing, input validation (phone
format, lat/lng bounds, invalid IDs, malformed/impossible dates, missing
fields, negative quantities), and the centralized error handler.

Tests use an isolated file-based SQLite database, wiped and rebuilt before
every test function. `ML_SERVICE_URL`/`RANKING_SERVICE_URL` point at
unreachable ports during tests on purpose, so the mock-fallback path runs
deterministically without needing real M4/M5 services.

**Warnings:** 32, all from third-party libraries (`passlib`'s use of Python's
deprecated `crypt` module, `python-jose`'s use of deprecated
`datetime.utcnow()`) - none from our code.

## Creating an admin account

Public registration only allows `FARMER`/`BUYER`. To create an admin:

```bash
python3 -m scripts.create_admin
```

Interactive prompt, bypasses the public API's role restriction entirely by
writing directly to the database.

## Talking to M4 / M5 before they're ready

`app/services/ml_client.py` calls `ML_SERVICE_URL/predict`.
`app/services/ranking_client.py` calls `RANKING_SERVICE_URL/rank`.
Both fall back automatically if unreachable. The fallback logic is cleanly
separated from the orchestration routers (`predict.py`, `recommend.py`) -
swapping in real contracts should only touch these two client files.

---

## Changes made tonight — final adjustment (on top of the previous baseline)

**The one change requested:** the documented flow puts price prediction
*before* distance/transport/profit/ranking
(`Current Prices -> Prediction -> Distance -> Transport -> Profit -> Ranking`),
but `recommend-market` was skipping the prediction step entirely and computing
profit straight off today's current price. Fixed:

- `recommend-market` now calls the existing `ml_client.predict_price()`
  (M4's abstraction, same mock-fallback as `/api/predict-price` uses) for
  every candidate market, in parallel, before computing distance/transport/profit.
- Distance/transport/profit/ranking are now computed from the **predicted**
  price, not the raw current price. Today's current price is still returned
  alongside it (`price` field) for context/explainability.
- `MarketOption` response schema gained a `predicted_price` field.
- The recommendation saved to the DB now stores the predicted price as
  `expected_price`, not the current price.
- No M4 contract was invented or finalized - this only wires the *existing*
  client/mock abstraction into the flow, exactly as asked.
- **1 new test** (63 total) specifically proving the prediction step is
  actually invoked and threaded through correctly, not just present in code.

Nothing else touched. `buyers.user_id`, M4/M5 contracts, M6 transport/distance,
PATCH vs PUT, and the admin workflow remain exactly as pending team decisions.

## Changes from the round before that

1. **Phone number format validation** - `UserRegister.phone` now requires
   10-15 digits only (was previously any string of that length).
2. **Latitude/longitude bounds** - added `-90 to 90` / `-180 to 180`
   validation to `UserRegister`, `UserUpdate`, and `RecommendMarketRequest`.
3. **`market_id` existence check** added to both `GET /api/market-prices`
   and `GET /api/market-prices/history` (previously only `crop_id` was
   checked; an invalid `market_id` silently returned an empty list instead
   of a clear 404).
4. **Centralized error handling** - a catch-all exception handler in
   `main.py` now logs full details server-side but only ever returns a
   generic `{"detail": "Internal server error"}` to the client for anything
   unexpected. Existing deliberate errors (404/403/409/422/etc) are
   untouched.
5. **API documentation improved** across `auth.py`, `crops.py`,
   `produce.py`, `market_prices.py`, `profit.py` - added `summary`/
   `description` to every endpoint so `/docs` is self-explanatory for M1.
6. **17 new tests** (45 → 62 → 63): `test_health.py`, `test_crops.py`,
   `test_error_handling.py`, and `test_validation.py` (phone format,
   coordinate bounds, invalid market IDs, malformed/impossible dates,
   missing required fields, negative quantities).
7. Switched `@app.on_event("startup")` to FastAPI's `lifespan` pattern
   (carried over from last round, confirmed still clean this round).

## Flag for team — please confirm tomorrow

Unchanged from the previous round, per tonight's instructions not to
finalize these:

1. **Admin creation workflow.** Currently `scripts/create_admin.py` only -
   needs a real team decision (invite-only endpoint? bootstrap-only? manual
   DB access?).
2. **`buyers.user_id → users.user_id` link.** Present exactly as before - a
   buyer's account auto-links to a `buyers` row on registration. **Not** in
   the official schema doc, needs M3/team sign-off. See
   `app/models/buyer.py` and `app/crud/user.py`.
3. **Transport/distance calculation.** Still a placeholder (haversine +
   flat rate) in `app/services/transport.py`. Needs M6's real
   formula/provider.
4. **M4 prediction contract.** Mock fallback unchanged in
   `app/services/ml_client.py`, ready to swap once M4 shares their contract.
5. **M5 ranking contract.** Same, in `app/services/ranking_client.py`.
6. **PATCH vs. PUT for produce updates.** Used PATCH since updates are
   partial - confirm this matches what M1 expects.
7. **`notifications` and `transport_rates` tables** still have no
   endpoints - intentionally out of scope for the MVP.

## Endpoints

| Method | Path                                | Auth              | Purpose |
|--------|--------------------------------------|-------------------|---------|
| POST   | /api/register                       | -                 | Register farmer/buyer (NOT admin) |
| POST   | /api/login                          | -                 | Login, returns JWT |
| GET    | /api/users/me                       | any               | Get your own profile |
| PUT    | /api/users/me                       | any               | Update your own profile |
| GET    | /api/crops                          | -                 | List all crops |
| POST   | /api/farmer/produce                 | FARMER            | Create a produce listing |
| GET    | /api/farmer/produce                 | FARMER            | List your own produce |
| GET    | /api/farmer/produce/{produce_id}    | owner only        | Read one listing |
| PATCH  | /api/farmer/produce/{produce_id}    | owner only        | Update one listing |
| DELETE | /api/farmer/produce/{produce_id}    | owner only        | Delete one listing |
| GET    | /api/market-prices?crop_id=&market_id= | -              | Current price per market (latest date only) |
| GET    | /api/market-prices/history?crop_id=&days= | -           | Historical price series |
| POST   | /api/predict-price                  | -                 | Get + store a fair-price prediction (calls M4) |
| POST   | /api/recommend-market                | FARMER            | Ranked market list with profit breakdown (calls M5) |
| GET    | /api/buyers?verification_status=    | optional (admin sees all) | List buyers (non-admin: VERIFIED only) |
| POST   | /api/buyer/requirements             | BUYER             | Buyer posts a crop requirement |
| POST   | /api/calculate-profit               | -                 | Stateless revenue/profit calculator |
| GET    | /health                             | -                 | Health check |

Full request/response schemas, validation rules, and auth requirements are
auto-documented at `/docs`.

## Project structure

```
app/
├── main.py                 # FastAPI app, router registration, lifespan startup, error handler
├── core/
│   ├── config.py            # env settings (.env)
│   ├── database.py          # SQLAlchemy engine/session
│   └── security.py          # JWT + bcrypt helpers
├── models/                   # SQLAlchemy ORM models - one file per table (11 total)
├── schemas/                   # Pydantic request/response schemas + validation
├── crud/                       # DB access functions
├── services/
│   ├── ml_client.py             # calls M4's price prediction service
│   ├── ranking_client.py        # calls M5's market ranking service
│   └── transport.py             # distance + profit math (placeholder until M6)
├── dependencies.py           # get_db, get_current_user, get_current_user_optional, require_role
└── routers/
    ├── auth.py
    ├── users.py
    ├── crops.py
    ├── produce.py                # full CRUD, ownership-scoped
    ├── market_prices.py
    ├── predict.py
    ├── recommend.py              # orchestration endpoint
    ├── buyers.py
    └── profit.py
scripts/
├── seed_demo_data.py        # fake crops/markets/multi-day prices for local testing
└── create_admin.py          # isolated admin-account creation
tests/                        # 63 pytest tests, isolated DB per test
├── conftest.py
├── test_auth.py
├── test_authorization.py
├── test_produce.py
├── test_prices.py
├── test_profit.py
├── test_buyers.py
├── test_recommend.py
├── test_users.py
├── test_crops.py
├── test_health.py
├── test_validation.py
└── test_error_handling.py
```

## Database tables (matches FarmForward_Database_Schema)

`users`, `crops`, `farmer_produce`, `markets`, `market_prices`, `buyers`,
`buyer_requirements`, `price_predictions`, `transport_rates`,
`recommendations`, `notifications`.

Primary keys use `Integer` (not `BIGINT`) for SQLite-testing compatibility.
Postgres handles this fine at hackathon scale.

## Next steps for M2

- [ ] Bring the "Flag for team" list to tomorrow's discussion
- [ ] Swap `.env` DATABASE_URL to M3's real Postgres connection string once shared
- [ ] Confirm M4's `/predict` request/response fields match `ml_client.py`
- [ ] Confirm M5's `/rank` request/response fields match `ranking_client.py`
- [ ] Get real transport rate + distance logic from M6, replace placeholders in `transport.py`
- [ ] Decide on the admin-creation workflow properly
- [ ] Once the team confirms the above, merge into `feature/m2-backend`
