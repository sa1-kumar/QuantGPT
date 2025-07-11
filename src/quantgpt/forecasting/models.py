"""Forecasting models."""
from typing import Sequence


class PriceForecaster:
    """Placeholder forecasting model."""

    def __init__(self, prices: Sequence[float]):
        self.prices = list(prices)

    def forecast(self, steps: int = 1) -> Sequence[float]:
        """Return a naive forecast using the last observed price."""
        if not self.prices:
            raise ValueError("No price data provided")
        return [self.prices[-1]] * steps
