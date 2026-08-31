"""
Distance and profit calculations owned by M2 for now, since M6 (Maps/Logistics)
hasn't shared a live distance-calculation endpoint yet. This uses the haversine
formula (straight-line distance) as a placeholder - swap for M6's real
road-distance API call once it's ready (see calculate_distance_km below).

Formulas match TRD FR7 / FR9 and PRD Section 14:
  Expected Revenue = Selling Price x Quantity
  Net Profit = Expected Revenue - Transport Cost - Other Applicable Costs
"""
import math

DEFAULT_RATE_PER_KM_PER_UNIT = 2.0  # rupees per km per quintal - placeholder, confirm with M6/M3
DEFAULT_OTHER_COST_RATE = 0.0       # placeholder for mandi fees etc, confirm with team


def calculate_distance_km(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Haversine straight-line distance. TODO: replace with M6's real road-distance
    API (OpenRouteService/Google Maps) once available - see Master Plan Part 5."""
    R = 6371.0  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return round(R * 2 * math.asin(math.sqrt(a)), 2)


def estimate_transport_cost(distance_km: float, quantity: float, rate_per_km_unit: float = DEFAULT_RATE_PER_KM_PER_UNIT) -> float:
    return round(distance_km * quantity * rate_per_km_unit / 100, 2)  # /100: quantity in kg, rate per quintal


def calculate_profit(selling_price: float, quantity: float, transport_cost: float, other_cost: float = DEFAULT_OTHER_COST_RATE) -> dict:
    revenue = round(selling_price * quantity, 2)
    net_profit = round(revenue - transport_cost - other_cost, 2)
    return {
        "expected_revenue": revenue,
        "transport_cost": round(transport_cost, 2),
        "other_cost": round(other_cost, 2),
        "expected_net_profit": net_profit,
    }
