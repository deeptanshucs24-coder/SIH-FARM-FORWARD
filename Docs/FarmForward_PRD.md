TECHNICAL / PRODUCT DESIGN DOCUMENT

SIH26132

Farmer Market Linkage & Price Discovery

College-Level Product Design / Development Document

Smart India Hackathon (SIH)

## 1. Product Overview

Farmer Market Linkage & Price Discovery is a digital platform designed to help farmers make informed decisions about where, when, and to whom to sell agricultural produce. It combines market price information, price prediction, buyer linkage, transportation cost estimation, and profit-based recommendations in one platform.

The core product idea is simple: farmers should not only know the market price, but also understand which selling option can provide the best expected return.

## 2. Problem & User Pain Points

Limited access to reliable and timely market price information.

Different prices across nearby markets make selling decisions difficult.

Farmers may not know the most profitable market after transportation expenses.

Dependence on intermediaries can reduce bargaining power.

Finding suitable buyers for a specific crop and quantity can be difficult.

Existing platforms may display prices without giving personalized recommendations.

Complex interfaces can make digital tools difficult for some farmers to use.

## 3. Target Users

### 3.1 Farmer

The primary user is a farmer who wants to sell harvested or upcoming produce at a suitable price while minimizing unnecessary costs.

### 3.2 Buyer

Buyers such as wholesalers, retailers, processors, FPOs, and other verified organizations can publish requirements and find relevant produce.

### 3.3 Administrator

The administrator manages users, verifies buyers, monitors listings, and maintains platform information.

## 4. Product Goals

Improve access to market information.

Make price comparison simple.

Identify potentially profitable markets.

Improve direct farmer–buyer connectivity.

Reduce information asymmetry.

Provide a simple mobile-friendly experience.

Use AI/ML for useful price and market insights.

## 5. User Personas

## 6. Main User Journey

Register/Login

Enter crop and quantity

Confirm location

View current market prices

View predicted price trend

Compare markets and buyers

Check transportation cost

View expected net profit

Receive recommended selling option

Contact buyer or choose market

## 7. Product Value Proposition

The platform goes beyond displaying prices. It converts market information into a practical selling recommendation by considering price, distance, transportation cost, quantity, demand indicators, and predicted price trends.

Know the Price → Compare Options → Calculate Profit → Make the Decision

## 8. Key Product Features

## 9. Product Modules

Authentication & User Profile

Farmer Produce Management

Market Price Discovery

AI Price Prediction

Market Recommendation

Profit & Cost Calculator

Buyer Marketplace

Notifications & Alerts

Language/Voice Accessibility

Admin Management

## 10. Farmer Dashboard

The dashboard should present the most important information at a glance:

Current crop prices

Recommended market

Expected price

Estimated transportation cost

Expected net profit

Available buyer offers

Price alerts

Recent recommendations

## 11. Market Recommendation Design

The recommendation screen should show multiple selling options in a simple comparison format.

The recommended option should be highlighted while allowing the farmer to review alternatives.

## 12. Price Prediction Experience

Price prediction should be presented as an estimate, not a guaranteed future price.

Selected crop and market

Current price

Historical trend

Predicted price range

Expected trend: increasing, decreasing, or stable

Prediction period

## 13. Farmer–Buyer Linkage

The buyer section matches farmers with potential buyers using crop type, quantity, location, and buyer requirements.

Verified buyer profile

Crop required

Required quantity

Offered/expected price

Buyer location

Contact/request option

## 14. Profit Calculation

Expected Revenue = Selling Price × Quantity

Net Profit = Expected Revenue − Transportation Cost − Other Applicable Costs

## 15. Complete Product Workflow

Farmer Input
↓
Crop + Quantity + Location
↓
Market & Buyer Data
↓
Price Analysis + AI Prediction
↓
Transportation & Cost Analysis
↓
Profit Estimation
↓
Market/Buyer Ranking
↓
Selling Recommendation

## 16. UI/UX Design Principles

Mobile-first interface.

Simple navigation with minimal steps.

Clear numbers and visual indicators for prices and profits.

Simple language and icons.

Regional-language support.

Optional voice interaction.

Avoid information overload.

Clearly distinguish estimated values from actual prices.

## 17. Suggested Product Screens

## 18. Product Architecture Overview

The product will use a frontend application connected to backend APIs. The backend handles business logic, user management, price processing, recommendation logic, and communication with the database and AI/ML components.

Frontend
↓
Backend APIs
↓
Business & Recommendation Logic
↓
AI/ML Services
↓
Database + Market Data

## 19. MVP – Minimum Viable Product

Farmer registration/login

Crop and quantity entry

Market price comparison

Basic historical price visualization

Basic price prediction

Transportation cost estimation

Expected profit calculation

Market recommendation

Basic buyer listings

Farmer dashboard

## 20. Future Product Enhancements

Regional-language voice assistant

Advanced demand forecasting

Weather-aware recommendations

Transport booking and logistics integration

Digital contracts

Online payments

FPO/cooperative integration

Personalized recommendations

Expansion to additional crops, markets, and regions

## 21. Expected Product Impact

## 22. Product Success Metrics

Usefulness and reliability of market price information.

Performance of the price prediction model.

Quality of market recommendations.

Number of relevant buyer matches.

Time required to obtain a selling recommendation.

User engagement with alerts and recommendations.

Usability based on prototype feedback.

## 23. Conclusion

The Farmer Market Linkage & Price Discovery platform is a practical digital product that converts agricultural market data into actionable selling decisions. Its core value lies in combining price discovery, AI-based prediction, buyer linkage, transportation analysis, and profit estimation in one simple workflow. The product can begin as a focused college-level MVP and later expand into a larger agricultural market intelligence platform.

| Persona | Goal | Pain Point | Product Need |
| --- | --- | --- | --- |
| Small/Mid-size Farmer | Sell profitably | Limited market information | Simple recommendation |
| Agricultural Buyer | Find produce | Difficulty finding suppliers | Crop/quantity-based listings |
| Platform Admin | Maintain trust | User/data management | Verification dashboard |

| Feature | Purpose |
| --- | --- |
| Market Price Discovery | View current and historical prices across available markets. |
| Price Prediction | Estimate short-term crop price trends from historical data. |
| Smart Market Recommendation | Rank markets using expected profitability and suitability. |
| Profit Calculator | Estimate revenue, transport cost, other costs, and net profit. |
| Buyer Linkage | Help farmers discover relevant verified buyers. |
| Buyer Requirements | Allow buyers to publish crop and quantity requirements. |
| Transportation Estimation | Estimate transport expenses from distance and quantity. |
| Price Alerts | Notify users about significant or favorable price changes. |
| Regional Language Support | Make the platform easier to use for local farmers. |
| Admin Dashboard | Manage users, buyers, listings, and platform data. |

| Market | Price/kg | Distance | Transport | Expected Profit | Recommendation |
| --- | --- | --- | --- | --- | --- |
| Market A | ₹X | XX km | ₹X | ₹X | Suitable |
| Market B | ₹X | XX km | ₹X | ₹X | Best Option |
| Market C | ₹X | XX km | ₹X | ₹X | Alternative |

| Screen | Purpose |
| --- | --- |
| Landing Screen | Project identity and entry points. |
| Login / Registration | Authentication and user type selection. |
| Farmer Dashboard | Prices, recommendations, alerts, and quick actions. |
| Add Produce | Crop, variety, quantity, availability date, and expected price. |
| Market Comparison | Price, distance, transport, and profit comparison. |
| Price Prediction | Historical trend and estimated future price. |
| Buyer Marketplace | Buyer requirements and relevant offers. |
| Recommendation Result | Best market/buyer with explanation. |
| Notifications | Price and buyer alerts. |
| Profile | Farmer/buyer information and preferences. |
| Admin Dashboard | User, buyer, market, and listing management. |

| Impact Area | Expected Outcome |
| --- | --- |
| Better Information | Farmers get easier access to relevant market information. |
| Improved Decision Making | Farmers compare selling options using multiple factors. |
| Higher Profit Potential | Recommendations focus on estimated net returns. |
| Better Market Access | Direct buyer linkage can increase access to customers. |
| Reduced Information Asymmetry | The information gap between farmers and markets is reduced. |
| Digital Inclusion | Simple and multilingual design improves accessibility. |
