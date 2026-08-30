TECHNICAL REQUIREMENT DOCUMENT

SIH26132

Farmer Market Linkage & Price Discovery

A College-Level Technical Requirement Document

Smart India Hackathon (SIH)
Project Documentation

## 1. Project Overview

The proposed system is an AI-enabled digital platform designed to help farmers make better decisions regarding the sale of their agricultural produce. The platform will provide crop price information, compare prices across different markets, connect farmers with potential buyers, estimate transportation costs, and recommend suitable markets based on expected profitability.

The primary goal is to reduce information gaps between farmers and markets and help farmers make informed, data-driven selling decisions.

## 2. Problem Statement

Farmers often do not have easy access to reliable and timely information about crop prices, market demand, and available buyers. As a result, they may depend on intermediaries or sell their produce at lower prices. Existing platforms generally provide market prices but may not consider factors such as farmer location, quantity of produce, transportation expenses, market demand, and expected price trends while recommending where to sell.

Therefore, there is a need for an integrated platform that provides price discovery and recommends the most suitable and potentially profitable market or buyer for a farmer.

## 3. Objectives

Provide farmers with current and historical crop prices.

Compare prices across multiple markets.

Predict short-term crop price trends using machine learning.

Recommend suitable markets based on expected profit.

Connect farmers with potential buyers and organizations.

Estimate transportation costs.

Provide price and market alerts.

Support regional languages and simple user interaction.

Reduce dependency on intermediaries by improving market information access.

## 4. Proposed Solution

The proposed platform will collect market and agricultural data and process it through a backend system. Farmers will enter information such as crop type, quantity, location, and preferred selling period.

The system will analyze available market prices, estimated transportation costs, demand indicators, and predicted price trends. Based on these parameters, the recommendation engine will rank available markets and buyers and display the options with their estimated selling price and expected profit.

Basic Workflow:

Farmer Input → Data Processing → Price Analysis → AI Prediction → Market/Buyer Comparison → Profit Calculation → Recommendation

## 5. Target Users

### 5.1 Farmers

Register and manage their profile.

Add crop and quantity details.

View current market prices.

Compare nearby markets.

View predicted prices.

Find potential buyers.

Check estimated transportation costs.

Receive recommendations and alerts.

### 5.2 Buyers

Create a buyer profile.

Post crop requirements.

Specify required quantity and expected price.

View available farmer listings.

Contact interested farmers.

### 5.3 Administrator

Manage users.

Manage crop and market information.

Verify buyers.

Monitor system activity.

Manage reported issues.

Monitor data quality.

## 6. Functional Requirements

FR1 – User Registration and Login

The system shall allow farmers and buyers to create accounts using basic details such as name, mobile number, location, and user type. The system shall provide secure login and authentication.

FR2 – Farmer Profile

The system shall allow farmers to maintain their name, location, contact details, crops grown, approximate farm/produce details, and preferred markets.

FR3 – Crop Management

Farmers shall be able to enter crop name, crop variety, quantity, harvest/availability date, and expected selling price.

FR4 – Market Price Discovery

The system shall display current crop prices, historical prices, minimum price, maximum price, average price, and market-wise price comparison.

FR5 – Price Prediction

The system shall use historical market data to estimate future crop prices. Possible machine learning models include Linear Regression, Random Forest, and XGBoost. The prototype may select one model based on dataset performance.

FR6 – Market Recommendation

The system shall recommend markets based on current price, predicted price, distance, transportation cost, quantity, demand, and estimated net profit.

FR7 – Profit Calculation

The system shall calculate estimated profit using: Net Profit = Expected Revenue − Transportation Cost − Applicable Market/Other Costs. Expected Revenue = Expected Selling Price × Quantity.

FR8 – Buyer Linkage

The system shall allow farmers to view relevant buyers based on crop type, quantity, location, and buyer requirements. Buyers shall be able to publish requirements for agricultural produce.

FR9 – Transportation Estimation

The system shall estimate approximate transportation cost based on farmer location, market/buyer location, distance, quantity, and estimated transport rate.

FR10 – Notifications

The system shall provide notifications for significant price changes, favorable selling opportunities, buyer requests, market recommendations, and important system updates.

FR11 – Regional Language Support

The platform should support regional languages to improve accessibility. The initial prototype may support English and one regional language, with additional languages added later.

## 7. Non-Functional Requirements

Performance

The system should provide market recommendations and price information within a reasonable response time.

Scalability

The architecture should allow additional crops, markets, users, and data sources to be added in the future.

Usability

The interface should be simple and mobile-friendly so that users with limited technical knowledge can operate it.

Security

User credentials and personal information must be securely stored. Authentication and authorization should be implemented for protected operations.

Reliability

The system should handle temporary data-source failures gracefully and display the latest available information.

Maintainability

The application should use a modular architecture so individual components can be updated independently.

## 8. AI/ML Requirements

The AI/ML component will primarily focus on crop price prediction and market recommendation.

### 8.1 Input Features

Crop type

Market/location

Historical price

Date/season

Market arrivals

Quantity

Demand indicators

Previous price trends

### 8.2 Output

The model will provide an estimated price for the selected crop and time period. The recommendation system will combine the predicted price with transportation and other costs to identify potentially profitable selling options.

## 9. Data Requirements

Historical crop prices

Current market prices

Market locations

Crop information

Market arrival data

Historical demand/supply information

Transportation distance

Transportation cost estimates

Buyer requirements

For the college prototype, publicly available agricultural datasets and suitable government/open-data sources can be used where permitted.

## 10. Database Requirements

A relational database such as PostgreSQL or MySQL can be used.

Users

Fields: user_id, name, phone, location, role

Crops

Fields: crop_id, crop_name, variety

Farmer_Produce

Fields: produce_id, farmer_id, crop_id, quantity, available_date, expected_price

Markets

Fields: market_id, market_name, location

Market_Prices

Fields: price_id, market_id, crop_id, date, min_price, max_price, average_price

Buyers

Fields: buyer_id, buyer_name, location, contact

Buyer_Requirements

Fields: requirement_id, buyer_id, crop_id, required_quantity, offered_price

## 11. System Architecture

The proposed system can follow a three-layer architecture:

### 11.1 Presentation Layer

Web/mobile interface

Farmer dashboard

Buyer dashboard

Admin dashboard

### 11.2 Application Layer

Authentication

Price processing

Recommendation engine

Profit calculator

Buyer matching

Notification service

### 11.3 Data Layer

User database

Market price database

Crop database

Buyer database

ML model/data storage

User Interface
↓
Backend/API
↓
Business Logic
↓
Recommendation + ML Engine
↓
Database / Market Data Sources

## 12. Suggested Technology Stack

## 13. API Requirements

These endpoints are indicative and can be modified during implementation.

## 14. Security Requirements

Secure password storage.

JWT/session-based authentication.

Role-based access control.

Input validation.

API authentication.

Protection of user information.

Secure communication using HTTPS during deployment.

## 15. Expected Output

For a given farmer input such as crop type, quantity, and location, the system should provide a comparison of available markets including price, distance, transportation cost, and expected profit.

The system will then recommend the market with the best estimated overall return.

## 16. Minimum Viable Product (MVP)

Farmer registration/login

Crop and quantity input

Market price display

Market price comparison

Basic price prediction

Transportation cost estimation

Profit calculation

Market recommendation

Basic buyer linkage

Simple farmer dashboard

## 17. Future Scope

Multilingual voice assistant

Advanced demand forecasting

IoT-based crop/production data

Weather integration

Digital contracts between farmers and buyers

Online transactions

Logistics booking

FPO/cooperative integration

Personalized AI farming and selling recommendations

Expansion to multiple states and crops

## 18. Success Criteria

Provide reliable market price information.

Compare multiple selling options.

Generate a reasonable short-term price prediction.

Calculate approximate net profit.

Recommend a suitable market based on multiple factors.

Connect farmers with relevant buyers.

Provide a simple and accessible user experience.

## 19. Conclusion

SIH26132 aims to create a practical decision-support system that bridges the information gap between farmers and agricultural markets. Instead of only displaying market prices, the proposed system combines price discovery, AI prediction, transportation analysis, buyer linkage, and profit-based recommendations to help farmers make more informed selling decisions.

| Component | Suggested Technologies |
| --- | --- |
| Frontend | React.js / Next.js, HTML, CSS, JavaScript |
| Backend | Python FastAPI / Flask, REST APIs |
| Database | PostgreSQL / MySQL |
| AI/ML | Python, Pandas, NumPy, Scikit-learn, XGBoost |
| Maps & Location | OpenStreetMap or a suitable mapping API |
| Authentication | JWT-based authentication |
| Deployment | Cloud platform such as Render, AWS, Azure, or similar services |

| Module | Indicative API Endpoints |
| --- | --- |
| Authentication | POST /api/register POST /api/login |
| Crops | GET /api/crops POST /api/farmer/produce |
| Market Prices | GET /api/market-prices GET /api/market-prices/history |
| Prediction | POST /api/predict-price |
| Recommendation | POST /api/recommend-market |
| Buyers | GET /api/buyers POST /api/buyer/requirements |
| Profit | POST /api/calculate-profit |

| Market | Price | Distance | Transport Cost | Expected Profit |
| --- | --- | --- | --- | --- |
| Market A | ₹X/kg | XX km | ₹X | ₹X |
| Market B | ₹X/kg | XX km | ₹X | ₹X |
| Market C | ₹X/kg | XX km | ₹X | ₹X |
