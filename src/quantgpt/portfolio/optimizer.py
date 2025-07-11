"""Portfolio optimizer."""
from typing import Sequence


def optimize_portfolio(prices: Sequence[float]) -> Sequence[float]:
    """Return naive equal-weight allocation."""
    n = len(prices)
    if n == 0:
        raise ValueError("No price data provided")
    weight = 1.0 / n
    return [weight] * n
