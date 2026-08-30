# FarmForward — Database Schema & Application Flow

> This document fills the implementation-level gaps in the supplied PRD/PDT and TRD.
> It is derived from the entities, fields, workflows, modules, APIs, and requirements already specified in those documents.

---

## 1. Coverage Check

### 1.1 Database schema in the supplied documents

The TRD **does contain a database outline**, including these tables and fields:

- `Users`: `user_id`, `name`, `phone`, `location`, `role`
- `Crops`: `crop_id`, `crop_name`, `variety`
- `Farmer_Produce`: `produce_id`, `farmer_id`, `crop_id`, `quantity`, `available_date`, `expected_price`
- `Markets`: `market_id`, `market_name`, `location`
- `Market_Prices`: `price_id`, `market_id`, `crop_id`, `date`, `min_price`, `max_price`, `average_price`
- `Buyers`: `buyer_id`, `buyer_name`, `location`, `contact`
- `Buyer_Requirements`: `requirement_id`, `buyer_id`, `crop_id`, `required_quantity`, `offered_price`

However, this is **not yet a complete implementation-ready database schema**. The supplied documents do not define, in a complete way:

- Primary-key declarations
- Foreign-key relationships
- Data types
- Nullability
- Unique constraints
- Check constraints
- Indexes
- Notification storage
- Price-alert storage
- Prediction-result storage
- Recommendation-result/history storage
- Transport-rate data storage
- Buyer verification state
- User authentication credential fields
- Timestamps/audit fields
- Optional location coordinates needed for distance calculation

### 1.2 Application flow in the supplied documents

The documents **do contain a high-level application/product flow**.

The PRD gives the main user journey:

`Register/Login → Crop & Quantity → Location → Current Prices → Predicted Trend → Compare Markets/Buyers → Transportation Cost → Expected Net Profit → Recommendation → Contact Buyer / Choose Market`

The TRD gives the technical workflow:

`Farmer Input → Data Processing → Price Analysis → AI Prediction → Market/Buyer Comparison → Profit Calculation → Recommendation`

The PRD also gives the product workflow:

`Farmer Input → Crop + Quantity + Location → Market & Buyer Data → Price Analysis + AI Prediction → Transportation & Cost Analysis → Profit Estimation → Market/Buyer Ranking → Selling Recommendation`

So the flow exists, but it is **high-level**. What is missing is a detailed screen-by-screen and role-by-role application flow, including API calls, validation, database writes/reads, and decision branches.

---

# 2. Proposed Database Schema

## 2.1 Design principles

- Relational database: PostgreSQL or MySQL, as proposed in the TRD.
- Use a generated primary key for each entity.
- Use foreign keys to preserve relationships.
- Keep market-price records historical rather than overwriting them.
- Keep prediction and recommendation outputs separate from raw market data.
- Store buyer verification state because buyer verification is an administrator responsibility.
- Store timestamps for operational records.
- Store coordinates where required for distance and transportation estimation.

---

## 2.2 `users`

Stores farmer, buyer, and administrator accounts.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `user_id` | BIGINT | PK | Unique user identifier |
| `name` | VARCHAR(120) | NOT NULL | User name |
| `phone` | VARCHAR(20) | UNIQUE, NOT NULL | Mobile number |
| `password_hash` | VARCHAR(255) | NOT NULL | Secure password hash |
| `role` | VARCHAR(20) | NOT NULL | `FARMER`, `BUYER`, or `ADMIN` |
| `location` | VARCHAR(255) | NOT NULL | User location |
| `latitude` | DECIMAL(10,7) | NULL | Location latitude |
| `longitude` | DECIMAL(10,7) | NULL | Location longitude |
| `created_at` | TIMESTAMP | NOT NULL | Account creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes**

- Unique index on `phone`
- Index on `role`

---

## 2.3 `crops`

Stores supported crop information.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `crop_id` | BIGINT | PK | Unique crop identifier |
| `crop_name` | VARCHAR(100) | NOT NULL | Crop name |
| `variety` | VARCHAR(100) | NULL | Crop variety |
| `created_at` | TIMESTAMP | NOT NULL | Creation time |

**Indexes**

- Index on `crop_name`
- Composite index on (`crop_name`, `variety`)

---

## 2.4 `farmer_produce`

Stores produce entered by farmers.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `produce_id` | BIGINT | PK | Unique produce record |
| `farmer_id` | BIGINT | FK → `users.user_id`, NOT NULL | Farmer |
| `crop_id` | BIGINT | FK → `crops.crop_id`, NOT NULL | Crop |
| `quantity` | DECIMAL(12,2) | NOT NULL | Available quantity |
| `available_date` | DATE | NOT NULL | Harvest/availability date |
| `expected_price` | DECIMAL(12,2) | NULL | Farmer's expected selling price |
| `created_at` | TIMESTAMP | NOT NULL | Creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes**

- Index on `farmer_id`
- Index on `crop_id`
- Composite index on (`crop_id`, `available_date`)

---

## 2.5 `markets`

Stores market locations.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `market_id` | BIGINT | PK | Unique market identifier |
| `market_name` | VARCHAR(150) | NOT NULL | Market name |
| `location` | VARCHAR(255) | NOT NULL | Market location |
| `latitude` | DECIMAL(10,7) | NULL | Market latitude |
| `longitude` | DECIMAL(10,7) | NULL | Market longitude |
| `created_at` | TIMESTAMP | NOT NULL | Creation time |

**Indexes**

- Index on `location`
- Index on (`latitude`, `longitude`)

---

## 2.6 `market_prices`

Stores current and historical crop prices by market.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `price_id` | BIGINT | PK | Unique price record |
| `market_id` | BIGINT | FK → `markets.market_id`, NOT NULL | Market |
| `crop_id` | BIGINT | FK → `crops.crop_id`, NOT NULL | Crop |
| `price_date` | DATE | NOT NULL | Date of price |
| `min_price` | DECIMAL(12,2) | NOT NULL | Minimum price |
| `max_price` | DECIMAL(12,2) | NOT NULL | Maximum price |
| `average_price` | DECIMAL(12,2) | NOT NULL | Average price |
| `created_at` | TIMESTAMP | NOT NULL | Record creation time |

**Constraints**

- `min_price <= average_price`
- `average_price <= max_price`
- Unique (`market_id`, `crop_id`, `price_date`)

**Indexes**

- Composite index on (`crop_id`, `price_date`)
- Composite index on (`market_id`, `crop_id`, `price_date`)

---

## 2.7 `buyers`

Stores buyer profiles and verification status.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `buyer_id` | BIGINT | PK | Unique buyer identifier |
| `buyer_name` | VARCHAR(150) | NOT NULL | Buyer/organization name |
| `location` | VARCHAR(255) | NOT NULL | Buyer location |
| `latitude` | DECIMAL(10,7) | NULL | Buyer latitude |
| `longitude` | DECIMAL(10,7) | NULL | Buyer longitude |
| `contact` | VARCHAR(100) | NOT NULL | Contact information |
| `verification_status` | VARCHAR(20) | NOT NULL | `PENDING`, `VERIFIED`, `REJECTED` |
| `created_at` | TIMESTAMP | NOT NULL | Creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes**

- Index on `verification_status`
- Index on `location`

---

## 2.8 `buyer_requirements`

Stores produce requirements posted by buyers.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `requirement_id` | BIGINT | PK | Unique requirement |
| `buyer_id` | BIGINT | FK → `buyers.buyer_id`, NOT NULL | Buyer |
| `crop_id` | BIGINT | FK → `crops.crop_id`, NOT NULL | Required crop |
| `required_quantity` | DECIMAL(12,2) | NOT NULL | Required quantity |
| `offered_price` | DECIMAL(12,2) | NULL | Offered/expected price |
| `status` | VARCHAR(20) | NOT NULL | Requirement state |
| `created_at` | TIMESTAMP | NOT NULL | Creation time |
| `expires_at` | TIMESTAMP | NULL | Optional expiry |

**Indexes**

- Composite index on (`crop_id`, `status`)
- Index on `buyer_id`

---

## 2.9 `price_predictions`

Stores AI/ML prediction outputs.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `prediction_id` | BIGINT | PK | Unique prediction |
| `crop_id` | BIGINT | FK → `crops.crop_id`, NOT NULL | Crop |
| `market_id` | BIGINT | FK → `markets.market_id`, NOT NULL | Market |
| `prediction_date` | DATE | NOT NULL | Date prediction was generated |
| `target_date` | DATE | NOT NULL | Period being predicted |
| `predicted_price` | DECIMAL(12,2) | NOT NULL | Estimated future price |
| `predicted_min_price` | DECIMAL(12,2) | NULL | Lower estimated range |
| `predicted_max_price` | DECIMAL(12,2) | NULL | Upper estimated range |
| `trend` | VARCHAR(20) | NULL | `INCREASING`, `DECREASING`, or `STABLE` |
| `model_name` | VARCHAR(80) | NULL | Model used |
| `created_at` | TIMESTAMP | NOT NULL | Prediction creation time |

This supports the PRD/TRD requirement to show current price, historical trend, predicted range, expected trend, and prediction period.

---

## 2.10 `transport_rates`

Stores the rate used for transportation-cost estimation.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `transport_rate_id` | BIGINT | PK | Unique rate |
| `rate_per_km_unit` | DECIMAL(12,2) | NOT NULL | Rate basis |
| `unit_name` | VARCHAR(30) | NOT NULL | Quantity unit |
| `effective_from` | DATE | NOT NULL | Rate start |
| `effective_to` | DATE | NULL | Rate end |
| `created_at` | TIMESTAMP | NOT NULL | Creation time |

The exact rate formula is an implementation decision because the supplied documents specify the inputs but do not prescribe a fixed numerical transport-rate formula.

---

## 2.11 `recommendations`

Stores the result of a farmer's market/buyer recommendation request.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `recommendation_id` | BIGINT | PK | Unique recommendation |
| `farmer_id` | BIGINT | FK → `users.user_id`, NOT NULL | Farmer |
| `produce_id` | BIGINT | FK → `farmer_produce.produce_id`, NULL | Related produce |
| `crop_id` | BIGINT | FK → `crops.crop_id`, NOT NULL | Crop |
| `quantity` | DECIMAL(12,2) | NOT NULL | Quantity considered |
| `recommended_type` | VARCHAR(20) | NOT NULL | `MARKET` or `BUYER` |
| `recommended_market_id` | BIGINT | FK → `markets.market_id`, NULL | Recommended market |
| `recommended_buyer_id` | BIGINT | FK → `buyers.buyer_id`, NULL | Recommended buyer |
| `expected_price` | DECIMAL(12,2) | NOT NULL | Expected selling price |
| `transport_cost` | DECIMAL(12,2) | NOT NULL | Estimated transport cost |
| `other_cost` | DECIMAL(12,2) | NOT NULL | Other applicable costs |
| `expected_profit` | DECIMAL(12,2) | NOT NULL | Estimated net profit |
| `created_at` | TIMESTAMP | NOT NULL | Recommendation time |

---

## 2.12 `notifications`

Stores alerts and system notifications.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `notification_id` | BIGINT | PK | Unique notification |
| `user_id` | BIGINT | FK → `users.user_id`, NOT NULL | Recipient |
| `type` | VARCHAR(40) | NOT NULL | Notification type |
| `title` | VARCHAR(150) | NOT NULL | Notification title |
| `message` | TEXT | NOT NULL | Notification content |
| `is_read` | BOOLEAN | NOT NULL DEFAULT FALSE | Read state |
| `created_at` | TIMESTAMP | NOT NULL | Creation time |

Possible notification types follow the TRD/PRD requirements:

- Price change
- Favorable selling opportunity
- Buyer request
- Market recommendation
- System update

---

# 3. Entity Relationships

```text
USERS
  │
  ├──< FARMER_PRODUCE >── CROPS
  │
  ├──< NOTIFICATIONS
  │
  └──< RECOMMENDATIONS >── CROPS
                         │
                         ├── MARKETS
                         └── BUYERS

CROPS
  ├──< MARKET_PRICES >── MARKETS
  ├──< BUYER_REQUIREMENTS >── BUYERS
  └──< PRICE_PREDICTIONS >── MARKETS

TRANSPORT_RATES
  └── used by transportation-cost calculation
```

---

# 4. Application Flow

## 4.1 Authentication flow

```text
Landing Screen
      ↓
Login / Registration
      ↓
Select User Type
      ↓
Enter Basic Details
      ↓
Backend Validation
      ↓
Create / Authenticate User
      ↓
JWT / Session
      ↓
Role-Based Dashboard
```

### Farmer

`Login → Farmer Dashboard`

### Buyer

`Login → Buyer Dashboard`

### Administrator

`Login → Admin Dashboard`

---

# 5. Farmer Application Flow

## 5.1 Main farmer flow

```text
Farmer Dashboard
      ↓
Add Produce
      ↓
Select Crop + Variety
      ↓
Enter Quantity
      ↓
Enter Availability Date
      ↓
Confirm Location
      ↓
Request Market Analysis
      ↓
Fetch Current Market Prices
      ↓
Fetch Historical Prices
      ↓
Generate Price Prediction
      ↓
Calculate Distance
      ↓
Estimate Transportation Cost
      ↓
Calculate Expected Profit
      ↓
Match Buyer Requirements
      ↓
Rank Markets / Buyers
      ↓
Recommendation Result
      ↓
Farmer Reviews Best Option + Alternatives
      ↓
Contact Buyer OR Choose Market
```

---

## 5.2 Farmer dashboard flow

The dashboard should surface the information specified in the PRD:

```text
Farmer Dashboard
├── Current Crop Prices
├── Recommended Market
├── Expected Price
├── Estimated Transportation Cost
├── Expected Net Profit
├── Available Buyer Offers
├── Price Alerts
└── Recent Recommendations
```

---

# 6. Market Recommendation Flow

## 6.1 Inputs

The recommendation request should use:

- Crop
- Quantity
- Farmer location
- Current market prices
- Predicted prices
- Market distance
- Transportation cost
- Demand indicators
- Other applicable costs

These factors are explicitly identified in the PRD/TRD as inputs to recommendation logic.

## 6.2 Processing

```text
Farmer Input
    ↓
Find Relevant Markets
    ↓
Get Current Prices
    ↓
Get Historical Prices
    ↓
Generate / Retrieve Prediction
    ↓
Calculate Distance
    ↓
Estimate Transport Cost
    ↓
Calculate Revenue
    ↓
Subtract Transport + Other Costs
    ↓
Calculate Expected Net Profit
    ↓
Rank Options
```

## 6.3 Output

```text
Market A
Price: ₹X/kg
Distance: XX km
Transport: ₹X
Expected Profit: ₹X

Market B
Price: ₹X/kg
Distance: XX km
Transport: ₹X
Expected Profit: ₹X

Market C
Price: ₹X/kg
Distance: XX km
Transport: ₹X
Expected Profit: ₹X

             ↓

Recommended Option
```

The recommendation should highlight the best estimated option while allowing the farmer to compare alternatives.

---

# 7. Price Prediction Flow

```text
Crop + Market + Target Period
              ↓
      Historical Market Data
              ↓
        Feature Preparation
              ↓
          ML Model
              ↓
       Predicted Price
              ↓
  Predicted Range + Trend
              ↓
        Farmer Display
```

The TRD identifies possible models as Linear Regression, Random Forest, and XGBoost. The prototype may select one according to dataset performance.

---

# 8. Buyer Linkage Flow

## Farmer side

```text
Farmer Produce
      ↓
Crop + Quantity + Location
      ↓
Find Matching Buyer Requirements
      ↓
Filter Verified Buyers
      ↓
Rank Relevant Buyers
      ↓
Display Buyer Offers
      ↓
Contact / Request
```

## Buyer side

```text
Buyer Dashboard
      ↓
Create Requirement
      ↓
Select Crop
      ↓
Enter Required Quantity
      ↓
Enter Offered Price
      ↓
Publish Requirement
      ↓
Matching Farmer Listings Become Discoverable
```

---

# 9. Buyer Verification Flow

```text
Buyer Registration
      ↓
Verification Status = PENDING
      ↓
Admin Dashboard
      ↓
Review Buyer
      ↓
Approve / Reject
      ↓
VERIFIED buyer becomes eligible
for farmer-facing buyer linkage
```

---

# 10. Transportation Cost Flow

```text
Farmer Location
      +
Market / Buyer Location
      ↓
Distance Calculation
      ↓
Quantity
      ↓
Transport Rate
      ↓
Estimated Transportation Cost
      ↓
Profit Calculator
```

The supplied TRD requires transportation estimation based on farmer location, destination location, distance, quantity, and estimated transport rate. It does not define a fixed mathematical formula or rate table, so that part must be finalized during implementation.

---

# 11. Profit Calculation Flow

The supplied documents define:

```text
Expected Revenue = Selling Price × Quantity

Net Profit =
Expected Revenue
− Transportation Cost
− Applicable Market / Other Costs
```

Application flow:

```text
Expected Selling Price
        ×
Quantity
        ↓
Expected Revenue
        ↓
− Transportation Cost
        ↓
− Other Applicable Costs
        ↓
Expected Net Profit
```

---

# 12. Notification Flow

```text
System Event
     ↓
Check Notification Condition
     ↓
Create Notification
     ↓
Store in Notifications
     ↓
Display in User Dashboard
```

Supported notification purposes from the requirements:

- Significant price changes
- Favorable selling opportunities
- Buyer requests
- Market recommendations
- Important system updates

---

# 13. Screen-to-API Flow

## Authentication

| Screen | Action | API |
|---|---|---|
| Registration | Create account | `POST /api/register` |
| Login | Authenticate | `POST /api/login` |

## Farmer

| Screen | Action | API |
|---|---|---|
| Add Produce | Save produce | `POST /api/farmer/produce` |
| Crop Selection | Load crops | `GET /api/crops` |
| Market Prices | Load current prices | `GET /api/market-prices` |
| Price History | Load historical data | `GET /api/market-prices/history` |
| Price Prediction | Generate prediction | `POST /api/predict-price` |
| Recommendation | Rank markets | `POST /api/recommend-market` |
| Profit | Calculate profit | `POST /api/calculate-profit` |
| Buyers | Load buyer options | `GET /api/buyers` |

## Buyer

| Screen | Action | API |
|---|---|---|
| Buyer Requirement | Publish requirement | `POST /api/buyer/requirements` |

The supplied TRD explicitly describes these endpoints as indicative and states that they can be modified during implementation.

---

# 14. Role-Based Application Flow

```text
                    ┌───────────────┐
                    │ Authentication│
                    └───────┬───────┘
                            ↓
                     Role Detection
                     /      |                          /       |                          ↓        ↓        ↓
              FARMER     BUYER     ADMIN
                ↓          ↓         ↓
          Farmer App   Buyer App  Admin App
                ↓          ↓         ↓
          Produce &     Buyer      User/Data
          Analysis     Requirements Management
                ↓          ↓         ↓
          Market/Buyer   Farmer     Verification
          Recommendation Matching   & Monitoring
```

---

# 15. End-to-End System Flow

```text
                    FARMER
                       │
                       ▼
             Crop + Quantity + Location
                       │
                       ▼
                 Backend API
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    Market Data     Buyer Data    User Data
          │            │            │
          └────────────┼────────────┘
                       ▼
                Business Logic
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Price Analysis        Buyer Matching
             │                   │
             ▼                   │
        AI Prediction            │
             │                   │
             └─────────┬─────────┘
                       ▼
             Distance + Transport
                       │
                       ▼
                 Profit Engine
                       │
                       ▼
               Ranking Engine
                       │
                       ▼
             Selling Recommendation
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Choose Market       Contact Buyer
```

---

# 16. Implementation Boundary

### Already covered by PRD/TRD

- Product goals
- Target users
- User journeys
- Functional requirements
- Non-functional requirements
- AI/ML requirements
- High-level database entities
- High-level architecture
- Indicative APIs
- MVP scope
- Future scope
- High-level application workflow

### Added here because they were not sufficiently specified

- Full relational table structure
- Primary/foreign-key relationships
- Constraints and indexes
- Prediction persistence
- Recommendation persistence
- Notifications persistence
- Transport-rate persistence
- Detailed farmer flow
- Detailed buyer flow
- Buyer verification flow
- Screen-to-API mapping
- End-to-end role-based application flow
- Detailed data-processing sequence

### Still requires implementation decisions

- Exact database engine/version
- Exact latitude/longitude provider
- Exact map/distance API
- Exact transport pricing formula
- Exact ML model after dataset evaluation
- Exact notification delivery mechanism
- Exact authentication token/session expiry
- Exact buyer contact/request mechanism
- Exact admin screens and moderation rules
