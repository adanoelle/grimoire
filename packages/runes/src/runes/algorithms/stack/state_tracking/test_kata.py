"""
Pytest tests for Stack State Tracking kata.

Quick Reference:
    pytest test_kata.py                  # Run all
    pytest test_kata.py::TestMinStack    # Run specific
    pytest -m kata2                      # Run by marker
"""

import pytest
from hypothesis import given, strategies as st
from kata import MinStack


class TestMinStack:
    """Tests for Min Stack kata"""

    @pytest.mark.kata2
    def test_leetcode_example(self):
        """LeetCode canonical example."""
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        assert ms.getMin() == -3
        ms.pop()
        assert ms.top() == 0
        assert ms.getMin() == -2

    @pytest.mark.kata2
    def test_single_element(self):
        """Edge: single element."""
        ms = MinStack()
        ms.push(5)
        assert ms.top() == 5
        assert ms.getMin() == 5

    @pytest.mark.kata2
    def test_decreasing_sequence(self):
        """Edge: decreasing values (each new min)."""
        ms = MinStack()
        ms.push(5)
        assert ms.getMin() == 5
        ms.push(3)
        assert ms.getMin() == 3
        ms.push(1)
        assert ms.getMin() == 1

    @pytest.mark.kata2
    def test_increasing_sequence(self):
        """Edge: increasing values (min stays same)."""
        ms = MinStack()
        ms.push(1)
        assert ms.getMin() == 1
        ms.push(3)
        assert ms.getMin() == 1
        ms.push(5)
        assert ms.getMin() == 1

    @pytest.mark.kata2
    def test_pop_current_min(self):
        """Edge: popping current min reverts to previous min."""
        ms = MinStack()
        ms.push(2)
        ms.push(0)
        ms.push(3)
        ms.push(0)
        assert ms.getMin() == 0
        ms.pop()  # Remove second 0
        assert ms.getMin() == 0  # First 0 still there
        ms.pop()  # Remove 3
        assert ms.getMin() == 0
        ms.pop()  # Remove first 0
        assert ms.getMin() == 2  # Revert to original

    @pytest.mark.kata2
    def test_all_same_values(self):
        """Edge: all elements same value."""
        ms = MinStack()
        ms.push(1)
        ms.push(1)
        ms.push(1)
        assert ms.getMin() == 1
        ms.pop()
        assert ms.getMin() == 1
        ms.pop()
        assert ms.getMin() == 1

    @pytest.mark.kata2
    def test_negative_numbers(self):
        """Edge: negative numbers."""
        ms = MinStack()
        ms.push(-5)
        ms.push(-2)
        ms.push(-10)
        assert ms.getMin() == -10
        assert ms.top() == -10
        ms.pop()
        assert ms.getMin() == -5


class TestMinStackProperties:
    """Property-based tests"""

    @given(st.lists(st.integers(-1000, 1000), min_size=1, max_size=50))
    def test_min_is_actually_minimum(self, values):
        """getMin() always returns actual minimum."""
        ms = MinStack()
        for val in values:
            ms.push(val)

        assert ms.getMin() == min(values)

    @given(st.lists(st.integers(-1000, 1000), min_size=1, max_size=50))
    def test_top_is_last_pushed(self, values):
        """top() always returns most recently pushed value."""
        ms = MinStack()
        for val in values:
            ms.push(val)

        assert ms.top() == values[-1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
