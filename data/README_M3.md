# M3 — Database & Data Pipeline (Setup Guide)

This folder is **my part (M3)** of MandiSetu. It does three things:

1. **`schema.sql`** — creates all the database tables the whole team uses.
2. **`ingest_agmarknet.py`** — loads real government mandi prices into the database.
3. **`seed_demo_data.sql`** — loads fixed demo data so the presentation works even if the internet fails.

Follow the steps below in order. Copy-paste the commands exactly.

---

## Step 0 — Install the tools (one time)

You need **PostgreSQL** and **Python** installed.

- PostgreSQL: download from https://www.postgresql.org/download/ — during install, remember the password you set for the `postgres` user.
- Python: download from https://www.python.org/downloads/ — tick **"Add Python to PATH"** during install.

---

## Step 1 — Create the database

Open the terminal (Command Prompt on Windows) and run:

```bash
psql -U postgres -c "CREATE DATABASE mandisetu;"
```

It will ask for the postgres password you set in Step 0. Type it (nothing shows as you type — that's normal) and press Enter.

---

## Step 2 — Tell the script how to reach your database

Run **one** of these, replacing `YOURPASSWORD` with your postgres password:

**Windows (Command Prompt):**
```bash
set DATABASE_URL=postgresql://postgres:YOURPASSWORD@localhost:5432/mandisetu
```

**Mac / Linux:**
```bash
export DATABASE_URL="postgresql://postgres:YOURPASSWORD@localhost:5432/mandisetu"
```

> Keep this terminal window open for the next steps — the setting only lasts while it's open.

---

## Step 3 — Create the tables

From inside the `mandisetu` folder:

```bash
psql -U postgres -d mandisetu -f database/schema.sql
```

You should see a bunch of `CREATE TABLE` messages. That means it worked.

---

## Step 4 — Load the demo data (safe fallback — do this first)

```bash
psql -U postgres -d mandisetu -f data/seed_demo_data.sql
```

This loads farmer "Ramesh", a buyer, 4 markets, and onion prices. The demo now works with zero internet.

**Demo logins:** phone `9990000001`, password `demo1234` (farmer).

---

## Step 5 — Load REAL Agmarknet data (for the "live data" wow-moment)

First install the two Python helpers (one time):

```bash
pip install -r data/requirements.txt
```

Then pick **one** of the two ways:

### Option A — From a downloaded CSV (most reliable)
1. Go to: https://www.data.gov.in/catalog/current-daily-price-various-commodities-various-markets-mandi
2. Click **CSV** under "Export in", fill the small form, download the file.
3. Rename it to `agmarknet_prices.csv` and put it in the `data/` folder.
4. Run:
```bash
python data/ingest_agmarknet.py --csv data/agmarknet_prices.csv
```

### Option B — Live from the API
1. Get a **free API key**: sign up at https://data.gov.in/, open any dataset, click "Data API" — your key is shown at the top.
2. Set it (replace `YOURKEY`):
   - Windows: `set DATA_GOV_API_KEY=YOURKEY`
   - Mac/Linux: `export DATA_GOV_API_KEY="YOURKEY"`
3. Run:
```bash
python data/ingest_agmarknet.py --api --records 500
```

You'll see `[DONE] Inserted N price rows` when it works.

---

## Step 6 — Check it worked

```bash
psql -U postgres -d mandisetu -c "SELECT crop_name, COUNT(*) FROM market_prices GROUP BY crop_name;"
```

If you see rows with counts, **you're done.** Tell M2 (backend) and M4 (ML) the database is ready.

---

## If something breaks

- **"psql not recognized"** → PostgreSQL isn't on your PATH. Reinstall and tick the PATH option, or restart the terminal.
- **"could not connect"** → PostgreSQL isn't running, or the password in `DATABASE_URL` is wrong.
- **API fails** → just use Option A (CSV). The demo data from Step 4 is always enough as a backup.
