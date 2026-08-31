-- ============================================================
-- MandiSetu — Database Schema (MVP)
-- Owner: M3 (Database & Agriculture Data Pipeline)
-- Database: PostgreSQL
-- ============================================================
-- Run this file FIRST, before loading any data.
-- It creates every table the whole team needs (Part 10 of the plan).
-- ============================================================

-- Enable UUID generation (needed for auto-generated IDs)
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Drop tables if they already exist (so you can re-run this file cleanly).
-- Order matters: drop children before parents (foreign keys).
DROP TABLE IF EXISTS matches CASCADE;
DROP TABLE IF EXISTS buyers_requirements CASCADE;
DROP TABLE IF EXISTS price_predictions CASCADE;
DROP TABLE IF EXISTS market_prices CASCADE;
DROP TABLE IF EXISTS crop_listings CASCADE;
DROP TABLE IF EXISTS markets CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- ------------------------------------------------------------
-- 1. USERS  (farmers, buyers, admins)
-- ------------------------------------------------------------
CREATE TABLE users (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name          VARCHAR(120) NOT NULL,
    phone         VARCHAR(20) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role          VARCHAR(10) NOT NULL CHECK (role IN ('farmer', 'buyer', 'admin')),
    language_pref VARCHAR(5) DEFAULT 'en' CHECK (language_pref IN ('en', 'hi')),
    location_lat  FLOAT,
    location_lng  FLOAT,
    created_at    TIMESTAMP DEFAULT NOW()
);

-- ------------------------------------------------------------
-- 2. MARKETS  (mandis / APMCs with location)
-- ------------------------------------------------------------
CREATE TABLE markets (
    id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name     VARCHAR(150) NOT NULL,
    state    VARCHAR(80),
    district VARCHAR(80),
    lat      FLOAT,
    lng      FLOAT
);

-- ------------------------------------------------------------
-- 3. CROP_LISTINGS  (what a farmer wants to sell)
-- ------------------------------------------------------------
CREATE TABLE crop_listings (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    farmer_id    UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    crop_name    VARCHAR(80) NOT NULL,
    quantity_kg  INT NOT NULL,
    grade        VARCHAR(5),          -- e.g. A / B / C
    harvest_date DATE,
    status       VARCHAR(12) DEFAULT 'listed'
                 CHECK (status IN ('listed', 'interested', 'confirmed')),
    created_at   TIMESTAMP DEFAULT NOW()
);

-- ------------------------------------------------------------
-- 4. MARKET_PRICES  (real Agmarknet price data lands here)
-- ------------------------------------------------------------
CREATE TABLE market_prices (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    market_id         UUID NOT NULL REFERENCES markets(id) ON DELETE CASCADE,
    crop_name         VARCHAR(80) NOT NULL,
    price_per_quintal FLOAT NOT NULL,
    date              DATE NOT NULL
);

-- Index makes "price for crop X at market Y" lookups fast (used everywhere).
CREATE INDEX idx_market_prices_lookup
    ON market_prices (crop_name, market_id, date);

-- ------------------------------------------------------------
-- 5. PRICE_PREDICTIONS  (M4's ML service writes here)
-- ------------------------------------------------------------
CREATE TABLE price_predictions (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    crop_name      VARCHAR(80) NOT NULL,
    market_id      UUID REFERENCES markets(id) ON DELETE CASCADE,
    predicted_price FLOAT,
    range_min      FLOAT,
    range_max      FLOAT,
    confidence     FLOAT,
    distress_flag  BOOLEAN DEFAULT FALSE,
    created_at     TIMESTAMP DEFAULT NOW()
);

-- ------------------------------------------------------------
-- 6. BUYERS_REQUIREMENTS  (optional — what buyers want)
-- ------------------------------------------------------------
CREATE TABLE buyers_requirements (
    id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    buyer_id           UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    crop_name          VARCHAR(80) NOT NULL,
    quantity_needed_kg INT
);

-- ------------------------------------------------------------
-- 7. MATCHES  (farmer listing <-> interested buyer)
-- ------------------------------------------------------------
CREATE TABLE matches (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    listing_id UUID NOT NULL REFERENCES crop_listings(id) ON DELETE CASCADE,
    buyer_id   UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    status     VARCHAR(10) DEFAULT 'pending'
               CHECK (status IN ('pending', 'accepted', 'rejected')),
    created_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================
-- Done. Next: run  data/ingest_agmarknet.py  to load real prices,
-- then  data/seed_demo_data.sql  for demo fallback data.
-- ============================================================
