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

from kata import daily_temperatures


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

    @pytest.mark.kata4
    @pytest.mark.parametrize("temps,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, temps, expected, desc):
        """LeetCode canonical examples."""
        assert daily_temperatures(temps) == expected

    @pytest.mark.kata4
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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
