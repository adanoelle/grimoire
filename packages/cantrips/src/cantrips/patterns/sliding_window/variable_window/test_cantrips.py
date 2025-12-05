"""
Tests for Variable Window Sliding Window cantrips.

Run tests:
    pytest test_cantrips.py                    # All tests
    pytest test_cantrips.py -m cantrip1        # Just cantrip 1
    pytest test_cantrips.py -k "examples"      # Just examples
    pytest test_cantrips.py -v                 # Verbose output
"""

import pytest

from p001_length_of_longest_substring import length_of_longest_substring
from p002_min_subarray_len import min_subarray_len
from p003_total_fruit import total_fruit
from p004_k_distinct import length_of_longest_substring_k_distinct
from p005_subarray_product import num_subarray_product_less_than_k


# ============================================================================
# CANTRIP 1: Longest Substring Without Repeating Characters (LeetCode #3)
# ============================================================================


class TestCantrip1:
    """Tests for length_of_longest_substring (LeetCode #3)."""

    EXAMPLES = [
        ("abcabcbb", 3, "standard case"),
        ("bbbbb", 1, "all same"),
        ("pwwkew", 3, "best at end"),
    ]

    EDGE_CASES = [
        ("", 0, "empty string"),
        ("a", 1, "single char"),
        ("au", 2, "two unique"),
        ("aab", 2, "duplicate at start"),
        ("dvdf", 3, "duplicate in middle"),
    ]

    @pytest.mark.cantrip1
    @pytest.mark.examples
    @pytest.mark.parametrize("s,expected,desc", EXAMPLES, ids=[t[2] for t in EXAMPLES])
    def test_examples(self, s, expected, desc):
        """LeetCode examples."""
        assert length_of_longest_substring(s) == expected

    @pytest.mark.cantrip1
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "s,expected,desc", EDGE_CASES, ids=[t[2] for t in EDGE_CASES]
    )
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert length_of_longest_substring(s) == expected


# ============================================================================
# CANTRIP 2: Minimum Size Subarray Sum (LeetCode #209)
# ============================================================================


class TestCantrip2:
    """Tests for min_subarray_len (LeetCode #209)."""

    EXAMPLES = [
        (7, [2, 3, 1, 2, 4, 3], 2, "standard case"),
        (4, [1, 4, 4], 1, "single element"),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0, "no valid subarray"),
    ]

    EDGE_CASES = [
        (100, [1, 2, 3, 4, 5], 0, "impossible target"),
        (15, [1, 2, 3, 4, 5], 5, "need entire array"),
        (6, [10, 2, 3], 1, "single element sufficient"),
        (3, [1, 1, 1, 1, 1, 1, 1], 3, "minimum three needed"),
    ]

    @pytest.mark.cantrip2
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "target,nums,expected,desc", EXAMPLES, ids=[t[3] for t in EXAMPLES]
    )
    def test_examples(self, target, nums, expected, desc):
        """LeetCode examples."""
        assert min_subarray_len(target, nums) == expected

    @pytest.mark.cantrip2
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "target,nums,expected,desc", EDGE_CASES, ids=[t[3] for t in EDGE_CASES]
    )
    def test_edge_cases(self, target, nums, expected, desc):
        """Edge cases."""
        assert min_subarray_len(target, nums) == expected


# ============================================================================
# CANTRIP 3: Fruit Into Baskets (LeetCode #904)
# ============================================================================


class TestCantrip3:
    """Tests for total_fruit (LeetCode #904)."""

    EXAMPLES = [
        ([1, 2, 1], 3, "all fit in 2 baskets"),
        ([0, 1, 2, 2], 3, "start with 3 types"),
        ([1, 2, 3, 2, 2], 4, "best window at end"),
    ]

    EDGE_CASES = [
        ([1], 1, "single fruit"),
        ([1, 1, 1, 1], 4, "all same type"),
        ([1, 2, 1, 2, 1, 2], 6, "alternating types"),
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5, "complex pattern"),
    ]

    @pytest.mark.cantrip3
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "fruits,expected,desc", EXAMPLES, ids=[t[2] for t in EXAMPLES]
    )
    def test_examples(self, fruits, expected, desc):
        """LeetCode examples."""
        assert total_fruit(fruits) == expected

    @pytest.mark.cantrip3
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "fruits,expected,desc", EDGE_CASES, ids=[t[2] for t in EDGE_CASES]
    )
    def test_edge_cases(self, fruits, expected, desc):
        """Edge cases."""
        assert total_fruit(fruits) == expected


# ============================================================================
# CANTRIP 4: K Distinct Characters (LeetCode #340)
# ============================================================================


class TestCantrip4:
    """Tests for length_of_longest_substring_k_distinct (LeetCode #340)."""

    EXAMPLES = [
        ("eceba", 2, 3, "standard case"),
        ("aa", 1, 2, "single char repeated"),
    ]

    EDGE_CASES = [
        ("", 2, 0, "empty string"),
        ("a", 0, 0, "k is zero"),
        ("aabbcc", 3, 6, "k >= unique chars"),
        ("aabbcc", 1, 2, "k is 1"),
        ("abcdef", 3, 3, "all unique, k=3"),
    ]

    @pytest.mark.cantrip4
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "s,k,expected,desc", EXAMPLES, ids=[t[3] for t in EXAMPLES]
    )
    def test_examples(self, s, k, expected, desc):
        """LeetCode examples."""
        assert length_of_longest_substring_k_distinct(s, k) == expected

    @pytest.mark.cantrip4
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "s,k,expected,desc", EDGE_CASES, ids=[t[3] for t in EDGE_CASES]
    )
    def test_edge_cases(self, s, k, expected, desc):
        """Edge cases."""
        assert length_of_longest_substring_k_distinct(s, k) == expected


# ============================================================================
# CANTRIP 5: Subarray Product Less Than K (LeetCode #713)
# ============================================================================


class TestCantrip5:
    """Tests for num_subarray_product_less_than_k (LeetCode #713)."""

    EXAMPLES = [
        ([10, 5, 2, 6], 100, 8, "standard case"),
        ([1, 2, 3], 0, 0, "k is zero"),
    ]

    EDGE_CASES = [
        ([1, 1, 1], 2, 6, "all products < k"),
        ([10, 10, 10], 10, 0, "no valid subarrays"),
        ([1], 2, 1, "single element"),
        ([10], 100, 1, "single element < k"),
        ([10], 10, 0, "single element == k"),
    ]

    @pytest.mark.cantrip5
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "nums,k,expected,desc", EXAMPLES, ids=[t[3] for t in EXAMPLES]
    )
    def test_examples(self, nums, k, expected, desc):
        """LeetCode examples."""
        assert num_subarray_product_less_than_k(nums, k) == expected

    @pytest.mark.cantrip5
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "nums,k,expected,desc", EDGE_CASES, ids=[t[3] for t in EDGE_CASES]
    )
    def test_edge_cases(self, nums, k, expected, desc):
        """Edge cases."""
        assert num_subarray_product_less_than_k(nums, k) == expected
