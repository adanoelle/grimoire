"""
Pytest tests for Stack Monotonic kata.

Quick Reference:
    pytest test_kata.py                       # Run all
    pytest test_kata.py::TestDailyTemps       # Run specific
    pytest -m kata4                           # Run by marker
"""

import pytest
import sys
from pathlib import Path
from hypothesis import given, strategies as st

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from kata import (
    daily_temperatures,
    next_greater_element,
    next_greater_elements,
    StockSpanner,
    largest_rectangle_area,
)


class TestDailyTemperatures:
    """Tests for Daily Temperatures kata"""

    LEETCODE_EXAMPLES = [
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0], "example 1: mixed temps"),
        ([30,40,50,60], [1,1,1,0], "example 2: strictly increasing"),
        ([30,60,90], [1,1,0], "example 3: increasing jumps"),
    ]

    EDGE_CASES = [
        ([30], [0], "edge: single day"),
        ([90,80,70,60], [0,0,0,0], "edge: strictly decreasing"),
        ([30,30,30], [0,0,0], "edge: all same temp"),
        ([30,29,31], [2,1,0], "edge: dip then warmer"),
        ([50,50,60], [2,1,0], "edge: equal temps then warmer"),
    ]

    @pytest.mark.kata1
    @pytest.mark.parametrize("temps,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, temps, expected, desc):
        """LeetCode canonical examples."""
        assert daily_temperatures(temps) == expected

    @pytest.mark.kata1
    @pytest.mark.parametrize("temps,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, temps, expected, desc):
        """Edge cases."""
        assert daily_temperatures(temps) == expected


class TestDailyTemperaturesProperties:
    """Property-based tests"""

    @given(st.lists(st.integers(30, 100), min_size=1, max_size=50))
    def test_result_length_matches(self, temps):
        """Result has same length as input."""
        result = daily_temperatures(temps)
        assert len(result) == len(temps)

    @given(st.lists(st.integers(30, 100), min_size=1, max_size=50))
    def test_last_element_always_zero(self, temps):
        """Last day always has 0 (no future days)."""
        result = daily_temperatures(temps)
        assert result[-1] == 0

    @given(st.lists(st.integers(30, 100), min_size=1, max_size=50))
    def test_non_negative_results(self, temps):
        """All results are non-negative."""
        result = daily_temperatures(temps)
        assert all(days >= 0 for days in result)

    @given(st.lists(st.integers(30, 100), min_size=2, max_size=50))
    def test_increasing_sequence(self, temps):
        """Strictly increasing temps: all 1s except last."""
        temps = sorted(set(temps))  # Make strictly increasing
        if len(temps) < 2:
            return
        result = daily_temperatures(temps)
        expected = [1] * (len(temps) - 1) + [0]
        assert result == expected


class TestNextGreaterElement:
    """Tests for Next Greater Element I kata (kata2)"""

    LEETCODE_EXAMPLES = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1], "example 1"),
        ([2, 4], [1, 2, 3, 4], [3, -1], "example 2"),
    ]

    EDGE_CASES = [
        ([1], [1], [-1], "edge: single element"),
        ([4, 3, 2, 1], [4, 3, 2, 1], [-1, -1, -1, -1], "edge: all decreasing"),
        ([1, 2, 3], [1, 2, 3], [2, 3, -1], "edge: nums1 equals nums2"),
        ([3], [1, 2, 3, 4], [4], "edge: single in subset, has greater"),
        ([4], [1, 2, 3, 4], [-1], "edge: single in subset, max element"),
    ]

    @pytest.mark.kata2
    @pytest.mark.parametrize("nums1,nums2,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums1, nums2, expected, desc):
        """LeetCode canonical examples."""
        assert next_greater_element(nums1, nums2) == expected

    @pytest.mark.kata2
    @pytest.mark.parametrize("nums1,nums2,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums1, nums2, expected, desc):
        """Edge cases."""
        assert next_greater_element(nums1, nums2) == expected


class TestNextGreaterElementsCircular:
    """Tests for Next Greater Element II kata (kata3)"""

    LEETCODE_EXAMPLES = [
        ([1, 2, 1], [2, -1, 2], "example 1: wrap around"),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4], "example 2: max in middle"),
    ]

    EDGE_CASES = [
        ([5], [-1], "edge: single element"),
        ([3, 3, 3], [-1, -1, -1], "edge: all same"),
        ([1, 2, 3, 4], [2, 3, 4, -1], "edge: strictly increasing"),
        ([4, 3, 2, 1], [4, 4, 4, 4], "edge: strictly decreasing, all wrap to first"),
        ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5], "edge: max at start"),
    ]

    @pytest.mark.kata3
    @pytest.mark.parametrize("nums,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, expected, desc):
        """LeetCode canonical examples."""
        assert next_greater_elements(nums) == expected

    @pytest.mark.kata3
    @pytest.mark.parametrize("nums,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, nums, expected, desc):
        """Edge cases."""
        assert next_greater_elements(nums) == expected


class TestStockSpanner:
    """Tests for Online Stock Span kata (kata4)"""

    @pytest.mark.kata4
    def test_leetcode_example(self):
        """LeetCode canonical example."""
        ss = StockSpanner()
        prices = [100, 80, 60, 70, 60, 75, 85]
        expected = [1, 1, 1, 2, 1, 4, 6]
        for price, exp in zip(prices, expected):
            assert ss.next(price) == exp

    @pytest.mark.kata4
    def test_single_price(self):
        """Edge: single price always returns 1."""
        ss = StockSpanner()
        assert ss.next(50) == 1

    @pytest.mark.kata4
    def test_strictly_increasing(self):
        """Edge: strictly increasing prices, all spans are 1."""
        ss = StockSpanner()
        prices = [10, 20, 30, 40, 50]
        for price in prices:
            assert ss.next(price) == 1

    @pytest.mark.kata4
    def test_strictly_decreasing(self):
        """Edge: strictly decreasing prices, spans grow."""
        ss = StockSpanner()
        prices = [50, 40, 30, 20, 10]
        expected = [1, 2, 3, 4, 5]
        for price, exp in zip(prices, expected):
            assert ss.next(price) == exp

    @pytest.mark.kata4
    def test_all_same_price(self):
        """Edge: all same price, spans grow."""
        ss = StockSpanner()
        prices = [30, 30, 30, 30, 30]
        expected = [1, 2, 3, 4, 5]
        for price, exp in zip(prices, expected):
            assert ss.next(price) == exp


class TestLargestRectangle:
    """Tests for Largest Rectangle in Histogram kata (kata5)"""

    LEETCODE_EXAMPLES = [
        ([2, 1, 5, 6, 2, 3], 10, "example 1: rectangle height 5, width 2"),
        ([2, 4], 4, "example 2: single bar"),
        ([2, 1, 2], 3, "example 3: full width at height 1"),
    ]

    EDGE_CASES = [
        ([5], 5, "edge: single bar"),
        ([3, 3, 3, 3], 12, "edge: all same height"),
        ([1, 2, 3, 4, 5], 9, "edge: strictly increasing"),
        ([5, 4, 3, 2, 1], 9, "edge: strictly decreasing"),
        ([1], 1, "edge: single bar height 1"),
        ([6, 2, 5, 4, 5, 1, 6], 12, "edge: complex shape"),
    ]

    @pytest.mark.kata5
    @pytest.mark.parametrize("heights,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, heights, expected, desc):
        """LeetCode canonical examples."""
        assert largest_rectangle_area(heights) == expected

    @pytest.mark.kata5
    @pytest.mark.parametrize("heights,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, heights, expected, desc):
        """Edge cases."""
        assert largest_rectangle_area(heights) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
