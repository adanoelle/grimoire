"""Monotonic stack pattern cantrips.

Use monotonic stack when:
- "Next greater element" or "next smaller element"
- "Previous greater/smaller"
- Need O(n) time for array problems that seem like O(n^2)
- Finding spans, ranges, or distances to next/prev element
- Problems about histograms, temperatures, stock prices
"""

from .p001_daily_temperatures import daily_temperatures
from .p002_next_greater_i import next_greater_element
from .p003_next_greater_ii import next_greater_elements
from .p004_stock_span import StockSpanner
from .p005_largest_rectangle import largest_rectangle_area

__all__ = [
    "daily_temperatures",
    "next_greater_element",
    "next_greater_elements",
    "StockSpanner",
    "largest_rectangle_area",
]
