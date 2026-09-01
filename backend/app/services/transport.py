"""
Distance and profit calculations owned by M2 for now, since M6 (Maps/
Logistics) hasn't shared a live distance-calculation endpoint or transport
rate yet. Haversine (straight-line) distance is a placeholder - swap for
M6's real road-distance API once available.

Formulas match TRD FR7/FR9 and PRD Section 14:
  Expected Revenue = Selling Price x Quantity
  Net Profit = Expected Revenue - Transport Cost - Other Applicable Costs
"""
import math

DEFAULT_RATE_PER_KM_PER_QUINTAL = 2.0  # placeholder, confirm with M6/team
DEFAULT_OTHER_COST = 0.0


def calculate_distance_km(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Haversine straight-line distance. TODO: replace with M6's real
    road-distance API (OpenRouteService/Google Maps) once available."""
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return round(R * 2 * math.asin(math.sqrt(a)), 2)


def estimate_transport_cost(distance_km: float, quantity_kg: float,
                             rate_per_km_quintal: float = DEFAULT_RATE_PER_KM_PER_QUINTAL) -> float:
    """Rate is per quintal, quantity is in kg - conversion happens here since
    this function is specific to the kg-based produce/market flow."""
    quintals = quantity_kg / 100
    return round(distance_km * quintals * rate_per_km_quintal, 2)


def calculate_profit(selling_price: float, quantity: float, transport_cost: float,
                      other_cost: float = DEFAULT_OTHER_COST) -> dict:
    """Generic, unit-agnostic: Expected Revenue = Selling Price x Quantity
    (matches TRD FR7 literally). Used directly by the standalone
    /api/calculate-profit endpoint. Callers working in price-per-quintal +
    quantity-in-kg (like recommend-market) must convert quantity to
    quintals themselves BEFORE calling this - see recommend.py."""
    revenue = round(selling_price * quantity, 2)
    net_profit = round(revenue - transport_cost - other_cost, 2)
    return {
        "expected_revenue": revenue,
        "transport_cost": round(transport_cost, 2),
        "other_cost": round(other_cost, 2),
        "expected_net_profit": net_profit,
    }
