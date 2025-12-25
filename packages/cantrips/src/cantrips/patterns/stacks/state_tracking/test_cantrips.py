"""
Pytest tests for Stack State Tracking cantrips.

Quick Reference:
    pytest test_cantrips.py                  # Run all
    pytest test_cantrips.py::TestMinStack    # Run specific
    pytest -m cantrip2                       # Run by marker
"""

import pytest
from hypothesis import given, strategies as st

from .p001_min_stack import MinStack
from .p002_max_stack import MaxStack
from .p003_custom_stack import CustomStack
from .p004_freq_stack import FreqStack
from .p005_time_map import TimeMap


class TestMinStack:
    """Tests for Min Stack cantrip."""

    @pytest.mark.cantrip1
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

    @pytest.mark.cantrip1
    def test_single_element(self):
        """Edge: single element."""
        ms = MinStack()
        ms.push(5)
        assert ms.top() == 5
        assert ms.getMin() == 5

    @pytest.mark.cantrip1
    def test_decreasing_sequence(self):
        """Edge: decreasing values (each new min)."""
        ms = MinStack()
        ms.push(5)
        assert ms.getMin() == 5
        ms.push(3)
        assert ms.getMin() == 3
        ms.push(1)
        assert ms.getMin() == 1

    @pytest.mark.cantrip1
    def test_increasing_sequence(self):
        """Edge: increasing values (min stays same)."""
        ms = MinStack()
        ms.push(1)
        assert ms.getMin() == 1
        ms.push(3)
        assert ms.getMin() == 1
        ms.push(5)
        assert ms.getMin() == 1

    @pytest.mark.cantrip1
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

    @pytest.mark.cantrip1
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

    @pytest.mark.cantrip1
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
    """Property-based tests for MinStack."""

    @pytest.mark.cantrip1
    @given(st.lists(st.integers(-1000, 1000), min_size=1, max_size=50))
    def test_min_is_actually_minimum(self, values):
        """getMin() always returns actual minimum."""
        ms = MinStack()
        for val in values:
            ms.push(val)
        assert ms.getMin() == min(values)

    @pytest.mark.cantrip1
    @given(st.lists(st.integers(-1000, 1000), min_size=1, max_size=50))
    def test_top_is_last_pushed(self, values):
        """top() always returns most recently pushed value."""
        ms = MinStack()
        for val in values:
            ms.push(val)
        assert ms.top() == values[-1]


class TestMaxStack:
    """Tests for Max Stack cantrip."""

    @pytest.mark.cantrip2
    def test_leetcode_example(self):
        """LeetCode-style example."""
        ms = MaxStack()
        ms.push(5)
        ms.push(1)
        ms.push(5)
        assert ms.top() == 5
        assert ms.getMax() == 5
        ms.pop()
        assert ms.getMax() == 5

    @pytest.mark.cantrip2
    def test_single_element(self):
        """Edge: single element."""
        ms = MaxStack()
        ms.push(5)
        assert ms.top() == 5
        assert ms.getMax() == 5

    @pytest.mark.cantrip2
    def test_increasing_sequence(self):
        """Edge: increasing values (each new max)."""
        ms = MaxStack()
        ms.push(1)
        assert ms.getMax() == 1
        ms.push(3)
        assert ms.getMax() == 3
        ms.push(5)
        assert ms.getMax() == 5

    @pytest.mark.cantrip2
    def test_decreasing_sequence(self):
        """Edge: decreasing values (max stays same)."""
        ms = MaxStack()
        ms.push(5)
        assert ms.getMax() == 5
        ms.push(3)
        assert ms.getMax() == 5
        ms.push(1)
        assert ms.getMax() == 5

    @pytest.mark.cantrip2
    def test_pop_current_max(self):
        """Edge: popping current max reverts to previous max."""
        ms = MaxStack()
        ms.push(2)
        ms.push(5)
        ms.push(3)
        ms.push(5)
        assert ms.getMax() == 5
        ms.pop()  # Remove second 5
        assert ms.getMax() == 5  # First 5 still there
        ms.pop()  # Remove 3
        assert ms.getMax() == 5
        ms.pop()  # Remove first 5
        assert ms.getMax() == 2  # Revert to original


class TestMaxStackProperties:
    """Property-based tests for MaxStack."""

    @pytest.mark.cantrip2
    @given(st.lists(st.integers(-1000, 1000), min_size=1, max_size=50))
    def test_max_is_actually_maximum(self, values):
        """getMax() always returns actual maximum."""
        ms = MaxStack()
        for val in values:
            ms.push(val)
        assert ms.getMax() == max(values)


class TestCustomStack:
    """Tests for Custom Stack cantrip."""

    @pytest.mark.cantrip3
    def test_leetcode_example(self):
        """LeetCode canonical example."""
        stack = CustomStack(3)
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        stack.push(2)
        stack.push(3)
        stack.push(4)  # Full, ignored
        stack.increment(5, 100)  # Only 3 elements
        stack.increment(2, 100)  # Bottom 2
        assert stack.pop() == 103
        assert stack.pop() == 202
        assert stack.pop() == 201
        assert stack.pop() == -1  # Empty

    @pytest.mark.cantrip3
    def test_push_when_full(self):
        """Edge: push when full is ignored."""
        stack = CustomStack(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)  # Ignored
        assert stack.pop() == 2
        assert stack.pop() == 1

    @pytest.mark.cantrip3
    def test_pop_when_empty(self):
        """Edge: pop when empty returns -1."""
        stack = CustomStack(3)
        assert stack.pop() == -1

    @pytest.mark.cantrip3
    def test_increment_more_than_size(self):
        """Edge: increment k > size increments all elements."""
        stack = CustomStack(5)
        stack.push(1)
        stack.push(2)
        stack.increment(10, 5)  # Only 2 elements
        assert stack.pop() == 7
        assert stack.pop() == 6

    @pytest.mark.cantrip3
    def test_increment_zero(self):
        """Edge: increment 0 elements does nothing."""
        stack = CustomStack(3)
        stack.push(1)
        stack.increment(0, 100)
        assert stack.pop() == 1


class TestFreqStack:
    """Tests for Frequency Stack cantrip."""

    @pytest.mark.cantrip4
    def test_leetcode_example(self):
        """LeetCode canonical example."""
        fs = FreqStack()
        fs.push(5)
        fs.push(7)
        fs.push(5)
        fs.push(7)
        fs.push(4)
        fs.push(5)
        assert fs.pop() == 5  # freq 3
        assert fs.pop() == 7  # freq 2, most recent
        assert fs.pop() == 5  # freq 2
        assert fs.pop() == 4  # freq 1

    @pytest.mark.cantrip4
    def test_single_element(self):
        """Edge: single element."""
        fs = FreqStack()
        fs.push(5)
        assert fs.pop() == 5

    @pytest.mark.cantrip4
    def test_all_same_frequency(self):
        """Edge: all same frequency, pop by recency."""
        fs = FreqStack()
        fs.push(1)
        fs.push(2)
        fs.push(3)
        assert fs.pop() == 3  # Most recent
        assert fs.pop() == 2
        assert fs.pop() == 1

    @pytest.mark.cantrip4
    def test_frequency_changes(self):
        """Edge: frequency changes after pops."""
        fs = FreqStack()
        fs.push(1)
        fs.push(1)
        fs.push(2)
        assert fs.pop() == 1  # freq 2 > freq 1
        assert fs.pop() == 2  # Now both freq 1, 2 is most recent
        assert fs.pop() == 1


class TestTimeMap:
    """Tests for Time Map cantrip."""

    @pytest.mark.cantrip5
    def test_leetcode_example(self):
        """LeetCode canonical example."""
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        assert tm.get("foo", 1) == "bar"
        assert tm.get("foo", 3) == "bar"
        tm.set("foo", "bar2", 4)
        assert tm.get("foo", 4) == "bar2"
        assert tm.get("foo", 5) == "bar2"

    @pytest.mark.cantrip5
    def test_get_nonexistent_key(self):
        """Edge: get before any set."""
        tm = TimeMap()
        assert tm.get("foo", 1) == ""

    @pytest.mark.cantrip5
    def test_get_before_first_timestamp(self):
        """Edge: get with timestamp before all values."""
        tm = TimeMap()
        tm.set("foo", "bar", 5)
        assert tm.get("foo", 1) == ""

    @pytest.mark.cantrip5
    def test_exact_timestamp_match(self):
        """Edge: get with exact timestamp."""
        tm = TimeMap()
        tm.set("foo", "v1", 1)
        tm.set("foo", "v2", 2)
        tm.set("foo", "v3", 3)
        assert tm.get("foo", 2) == "v2"

    @pytest.mark.cantrip5
    def test_multiple_keys(self):
        """Edge: multiple keys."""
        tm = TimeMap()
        tm.set("foo", "f1", 1)
        tm.set("bar", "b1", 2)
        tm.set("foo", "f2", 3)
        assert tm.get("foo", 2) == "f1"
        assert tm.get("bar", 5) == "b1"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
