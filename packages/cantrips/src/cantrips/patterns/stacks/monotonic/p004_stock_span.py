"""
CANTRIP 4: Online Stock Span (LeetCode #901)

Target: < 8:00 | Difficulty: Medium

Design an algorithm that calculates the span of stock prices.
The span on day i is the maximum number of consecutive days
(including today) with price <= prices[i].

Each price comes one at a time (streaming data).

Pattern: Monotonic decreasing stack with span tracking
- Stack stores (price, span) pairs
- When new price >= stack top price: pop, accumulate span
- Push (current_price, accumulated_span)

Examples:
    >>> ss = StockSpanner()
    >>> ss.next(100)
    1
    >>> ss.next(80)
    1
    >>> ss.next(60)
    1
    >>> ss.next(70)
    2
    >>> ss.next(60)
    1
    >>> ss.next(75)
    4
    >>> ss.next(85)
    6

Edge cases:
    - First price -> span = 1
    - Prices always increasing -> span always 1
    - Prices always decreasing -> span = day_count
    - Price equal to previous -> include in span
"""


class StockSpanner:
    """Calculate stock price spans in O(1) amortized time.

    Time: O(1) amortized per next() call
    Space: O(n) - stack size
    """

    def __init__(self):
        """Initialize the stock spanner."""
        pass

    def next(self, price: int) -> int:
        """Return span for current day's price.

        Args:
            price: Today's stock price.

        Returns:
            Number of consecutive days with price <= today.
        """
        pass
