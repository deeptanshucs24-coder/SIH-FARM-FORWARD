-- ============================================================
-- MandiSetu — Demo Seed Data (fallback for demo day)
-- Owner: M3
-- ============================================================
-- Run this AFTER schema.sql. It gives you guaranteed data so the
-- demo works even if the live API / ingestion fails on stage.
-- Prices here match the Part 14 demo script (Nashik onion story).
-- Passwords below are bcrypt hashes of the word:  demo1234
-- ============================================================

-- ---- MARKETS (fixed UUIDs so we can reference them below) ----
INSERT INTO markets (id, name, state, district, lat, lng) VALUES
  ('11111111-1111-1111-1111-111111111111', 'Nashik APMC',     'Maharashtra', 'Nashik', 19.9975, 73.7898),
  ('22222222-2222-2222-2222-222222222222', 'Pune Mandi',      'Maharashtra', 'Pune',   18.5204, 73.8567),
  ('33333333-3333-3333-3333-333333333333', 'Lasalgaon APMC',  'Maharashtra', 'Nashik', 20.1500, 74.2400),
  ('44444444-4444-4444-4444-444444444444', 'Mumbai Vashi APMC','Maharashtra','Thane',  19.0760, 72.9987);

-- ---- USERS: one farmer (Ramesh), one buyer, one admin ----
INSERT INTO users (id, name, phone, password_hash, role, language_pref, location_lat, location_lng) VALUES
  ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'Ramesh Patil', '9990000001',
   '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy', 'farmer', 'hi', 19.9900, 73.7800),
  ('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', 'Sunil Traders', '9990000002',
   '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy', 'buyer', 'en', 18.5204, 73.8567),
  ('cccccccc-cccc-cccc-cccc-cccccccccccc', 'Agri Officer', '9990000003',
   '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy', 'admin', 'en', 19.9975, 73.7898);

-- ---- MARKET PRICES (onion, last 7 days, per quintal) ----
-- Nashik trends higher; used to show "sell at Nashik" recommendation.
INSERT INTO market_prices (market_id, crop_name, price_per_quintal, date) VALUES
  -- Nashik APMC
  ('11111111-1111-1111-1111-111111111111', 'onion', 1720, CURRENT_DATE - 6),
  ('11111111-1111-1111-1111-111111111111', 'onion', 1760, CURRENT_DATE - 5),
  ('11111111-1111-1111-1111-111111111111', 'onion', 1780, CURRENT_DATE - 4),
  ('11111111-1111-1111-1111-111111111111', 'onion', 1800, CURRENT_DATE - 3),
  ('11111111-1111-1111-1111-111111111111', 'onion', 1810, CURRENT_DATE - 2),
  ('11111111-1111-1111-1111-111111111111', 'onion', 1815, CURRENT_DATE - 1),
  ('11111111-1111-1111-1111-111111111111', 'onion', 1820, CURRENT_DATE),
  -- Pune Mandi
  ('22222222-2222-2222-2222-222222222222', 'onion', 1680, CURRENT_DATE - 3),
  ('22222222-2222-2222-2222-222222222222', 'onion', 1720, CURRENT_DATE - 1),
  ('22222222-2222-2222-2222-222222222222', 'onion', 1750, CURRENT_DATE),
  -- Lasalgaon
  ('33333333-3333-3333-3333-333333333333', 'onion', 1700, CURRENT_DATE - 2),
  ('33333333-3333-3333-3333-333333333333', 'onion', 1740, CURRENT_DATE),
  -- Mumbai Vashi
  ('44444444-4444-4444-4444-444444444444', 'onion', 1850, CURRENT_DATE - 1),
  ('44444444-4444-4444-4444-444444444444', 'onion', 1870, CURRENT_DATE),
  -- A couple of extra crops so other demos work
  ('11111111-1111-1111-1111-111111111111', 'tomato', 1200, CURRENT_DATE),
  ('22222222-2222-2222-2222-222222222222', 'tomato', 1150, CURRENT_DATE),
  ('11111111-1111-1111-1111-111111111111', 'wheat',  2400, CURRENT_DATE),
  ('22222222-2222-2222-2222-222222222222', 'wheat',  2380, CURRENT_DATE);

-- ---- A sample crop listing (Ramesh's onions) ----
INSERT INTO crop_listings (id, farmer_id, crop_name, quantity_kg, grade, harvest_date, status) VALUES
  ('dddddddd-dddd-dddd-dddd-dddddddddddd',
   'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
   'onion', 500, 'A', CURRENT_DATE, 'listed');

-- ---- A sample buyer requirement ----
INSERT INTO buyers_requirements (buyer_id, crop_name, quantity_needed_kg) VALUES
  ('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', 'onion', 1000);

-- ============================================================
-- Demo login: phone 9990000001 / password demo1234  (farmer Ramesh)
--             phone 9990000002 / password demo1234  (buyer)
-- ============================================================
