"""
Pytest tests for Sliding Window (Variable Size) kata practice.

Quick Reference:
    pytest test_kata.py                              # Run all tests
    pytest test_kata.py::TestKata1LongestSubstring   # Run just kata 1
    pytest test_kata.py::TestKata2MinSubarrayLen     # Run just kata 2
    pytest -m kata1                                  # Run all kata1-level problems
    pytest -k "examples"                             # Run examples only

Justfile shortcuts (from workspace root):
    just kata::test sliding_window/variable_window
    just variable-window::test
    just variable-window::test-kata1

Mark katas as TODO by decorating with @kata_todo() when not implemented.
Remove the decorator when you've coded the solution in kata.py.
"""

import pytest
import sys
from pathlib import Path
from hypothesis import given, strategies as st

# Add current directory and algorithms directory to path for imports
current_dir = Path(__file__).parent
algorithms_dir = current_dir.parent.parent
sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(algorithms_dir))

from conftest import kata_todo
from kata import (
    length_of_longest_substring,
    min_subarray_len,
    total_fruit,
    length_of_longest_substring_k_distinct,
    num_subarray_product_less_than_k,
    min_window,
    subarrays_with_k_distinct,
)


# ============================================================================
# KATA 1: Longest Substring Without Repeating Characters (LeetCode #3)
# Target: < 3 min, zero bugs, O(n) time, O(alphabet) space
# ============================================================================

class TestKata1LongestSubstring:
    """Tests for length_of_longest_substring kata (LeetCode #3)"""

    LEETCODE_EXAMPLES = [
        ("abcabcbb", 3, "example 1: 'abc' is longest"),
        ("bbbbb", 1, "example 2: all same character"),
        ("pwwkew", 3, "example 3: 'wke' is longest"),
    ]

    EDGE_CASES = [
        ("", 0, "edge: empty string"),
        ("a", 1, "edge: single character"),
        ("au", 2, "edge: two distinct characters"),
        ("dvdf", 3, "edge: repeat after gap"),
        ("abcdefghij", 10, "edge: all distinct"),
        ("abba", 2, "edge: palindrome pattern"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata1
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert length_of_longest_substring(s) == expected

    @pytest.mark.kata1
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases for longest substring."""
        assert length_of_longest_substring(s) == expected


# ============================================================================
# KATA 2: Minimum Size Subarray Sum (LeetCode #209)
# Target: < 3.5 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata2MinSubarrayLen:
    """Tests for min_subarray_len kata (LeetCode #209)"""

    LEETCODE_EXAMPLES = [
        (7, [2, 3, 1, 2, 4, 3], 2, "example 1: [4,3] has sum 7"),
        (4, [1, 4, 4], 1, "example 2: single element 4"),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0, "example 3: impossible"),
    ]

    EDGE_CASES = [
        (15, [1, 2, 3, 4, 5], 5, "edge: entire array needed"),
        (3, [1, 1], 0, "edge: impossible with short array"),
        (100, [100], 1, "edge: single element exact match"),
        (5, [2, 3, 1, 1, 1, 1, 1], 2, "edge: minimal at start"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata2
    @pytest.mark.parametrize("target,nums,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, target, nums, expected, desc):
        """LeetCode canonical examples."""
        assert min_subarray_len(target, nums) == expected

    @pytest.mark.kata2
    @pytest.mark.parametrize("target,nums,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, target, nums, expected, desc):
        """Edge cases for min subarray length."""
        assert min_subarray_len(target, nums) == expected


# ============================================================================
# KATA 3: Fruit Into Baskets (LeetCode #904)
# Target: < 4 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata3TotalFruit:
    """Tests for total_fruit kata (LeetCode #904)"""

    LEETCODE_EXAMPLES = [
        ([1, 2, 1], 3, "example 1: all fruit can be picked"),
        ([0, 1, 2, 2], 3, "example 2: [1,2,2] is longest"),
        ([1, 2, 3, 2, 2], 4, "example 3: [2,3,2,2] is longest"),
    ]

    EDGE_CASES = [
        ([1], 1, "edge: single tree"),
        ([1, 1, 1, 1], 4, "edge: all same type"),
        ([1, 2, 1, 2, 1, 2], 6, "edge: alternating two types"),
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5, "edge: complex pattern"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata3
    @pytest.mark.parametrize("fruits,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, fruits, expected, desc):
        """LeetCode canonical examples."""
        assert total_fruit(fruits) == expected

    @pytest.mark.kata3
    @pytest.mark.parametrize("fruits,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, fruits, expected, desc):
        """Edge cases for fruit into baskets."""
        assert total_fruit(fruits) == expected


# ============================================================================
# KATA 4: Longest Substring with At Most K Distinct Characters (LeetCode #340)
# Target: < 4 min, zero bugs, O(n) time, O(k) space
# ============================================================================

class TestKata4LongestKDistinct:
    """Tests for length_of_longest_substring_k_distinct kata (LeetCode #340)"""

    LEETCODE_EXAMPLES = [
        ("eceba", 2, 3, "example 1: 'ece' has 2 distinct"),
        ("aa", 1, 2, "example 2: all same character"),
    ]

    EDGE_CASES = [
        ("", 2, 0, "edge: empty string"),
        ("a", 2, 1, "edge: single character"),
        ("abcde", 3, 3, "edge: k < unique chars"),
        ("abcde", 10, 5, "edge: k > unique chars"),
        ("aaabbbccc", 2, 6, "edge: consecutive groups"),
        ("abaccc", 2, 4, "edge: 'accc' is longest"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata4
    @pytest.mark.parametrize("s,k,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, k, expected, desc):
        """LeetCode canonical examples."""
        assert length_of_longest_substring_k_distinct(s, k) == expected

    @pytest.mark.kata4
    @pytest.mark.parametrize("s,k,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, s, k, expected, desc):
        """Edge cases for k distinct characters."""
        assert length_of_longest_substring_k_distinct(s, k) == expected


# ============================================================================
# KATA 5: Subarray Product Less Than K (LeetCode #713)
# Target: < 4.5 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata5SubarrayProduct:
    """Tests for num_subarray_product_less_than_k kata (LeetCode #713)"""

    LEETCODE_EXAMPLES = [
        ([10, 5, 2, 6], 100, 8, "example 1: 8 valid subarrays"),
        ([1, 2, 3], 0, 0, "example 2: k=0, no valid subarrays"),
    ]

    EDGE_CASES = [
        ([1, 1, 1], 2, 6, "edge: all elements are 1"),
        ([10], 10, 0, "edge: single element not less than k"),
        ([10], 11, 1, "edge: single element less than k"),
        ([1, 2, 3, 4], 10, 7, "edge: multiple valid windows"),
        ([100, 200], 50, 0, "edge: all products too large"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata5
    @pytest.mark.parametrize("nums,k,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, k, expected, desc):
        """LeetCode canonical examples."""
        assert num_subarray_product_less_than_k(nums, k) == expected

    @pytest.mark.kata5
    @pytest.mark.parametrize("nums,k,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, k, expected, desc):
        """Edge cases for subarray product."""
        assert num_subarray_product_less_than_k(nums, k) == expected


# ============================================================================
# KATA 6: Minimum Window Substring (LeetCode #76)
# Target: < 5 min, zero bugs, O(n) time, O(t) space
# ============================================================================

class TestKata6MinWindow:
    """Tests for min_window kata (LeetCode #76)"""

    LEETCODE_EXAMPLES = [
        ("ADOBECODEBANC", "ABC", "BANC", "example 1: BANC contains ABC"),
        ("a", "a", "a", "example 2: exact match"),
        ("a", "aa", "", "example 3: impossible"),
    ]

    EDGE_CASES = [
        ("", "a", "", "edge: empty s"),
        ("a", "", "", "edge: empty t"),
        ("aa", "aa", "aa", "edge: exact full match"),
        ("cabwefgewcwaefgcf", "cae", "cwae", "edge: multiple valid windows"),
        ("bba", "ab", "ba", "edge: chars in different order"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata6
    @pytest.mark.parametrize("s,t,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[c[3] for c in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, t, expected, desc):
        """LeetCode canonical examples."""
        assert min_window(s, t) == expected

    @pytest.mark.kata6
    @pytest.mark.parametrize("s,t,expected,desc",
                             EDGE_CASES,
                             ids=[c[3] for c in EDGE_CASES])
    def test_edge_cases(self, s, t, expected, desc):
        """Edge cases for minimum window substring."""
        assert min_window(s, t) == expected


# ============================================================================
# KATA 7: Subarrays with K Different Integers (LeetCode #992)
# Target: < 5 min, zero bugs, O(n) time, O(k) space
# ============================================================================

class TestKata7SubarraysKDistinct:
    """Tests for subarrays_with_k_distinct kata (LeetCode #992)"""

    LEETCODE_EXAMPLES = [
        ([1, 2, 1, 2, 3], 2, 7, "example 1: 7 subarrays with exactly 2 distinct"),
        ([1, 2, 1, 3, 4], 3, 3, "example 2: 3 subarrays with exactly 3 distinct"),
    ]

    EDGE_CASES = [
        ([1, 1, 1, 1], 1, 10, "edge: all same, k=1 -> n*(n+1)/2"),
        ([1, 2, 3], 4, 0, "edge: k > unique elements"),
        ([1, 2], 2, 1, "edge: exactly one valid subarray"),
        ([1, 2, 1, 2], 2, 6, "edge: alternating pattern"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata7
    @pytest.mark.parametrize("nums,k,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[c[3] for c in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, k, expected, desc):
        """LeetCode canonical examples."""
        assert subarrays_with_k_distinct(nums, k) == expected

    @pytest.mark.kata7
    @pytest.mark.parametrize("nums,k,expected,desc",
                             EDGE_CASES,
                             ids=[c[3] for c in EDGE_CASES])
    def test_edge_cases(self, nums, k, expected, desc):
        """Edge cases for subarrays with k distinct."""
        assert subarrays_with_k_distinct(nums, k) == expected


# ============================================================================
# PROPERTY-BASED TESTS (Using Hypothesis)
# ============================================================================

class TestKata1Properties:
    """Property-based tests for length_of_longest_substring (Kata 1)"""

    @given(s=st.text(alphabet="abc", min_size=0, max_size=50))
    def test_length_within_bounds(self, s):
        """Result should be between 0 and len(s)."""
        result = length_of_longest_substring(s)
        assert 0 <= result <= len(s), f"Length {result} not in range [0, {len(s)}]"

    @given(s=st.text(alphabet="abcdefghij", min_size=1, max_size=20))
    def test_all_distinct_returns_length(self, s):
        """If all characters are distinct, return full length."""
        if len(set(s)) == len(s):  # All distinct
            result = length_of_longest_substring(s)
            assert result == len(s), f"All distinct should return {len(s)}, got {result}"


class TestKata2Properties:
    """Property-based tests for min_subarray_len (Kata 2)"""

    @given(
        target=st.integers(1, 100),
        nums=st.lists(st.integers(1, 50), min_size=1, max_size=30)
    )
    def test_result_within_bounds(self, target, nums):
        """Result should be 0 or between 1 and len(nums)."""
        result = min_subarray_len(target, nums)
        assert 0 <= result <= len(nums), f"Length {result} not in range [0, {len(nums)}]"

    @given(nums=st.lists(st.integers(1, 100), min_size=1, max_size=30))
    def test_single_max_element_meets_target(self, nums):
        """If target equals max element, result should be 1."""
        target = max(nums)
        result = min_subarray_len(target, nums)
        assert result == 1, f"Max element {target} should require length 1, got {result}"


class TestKata3Properties:
    """Property-based tests for total_fruit (Kata 3)"""

    @given(fruits=st.lists(st.integers(0, 9), min_size=1, max_size=30))
    def test_result_within_bounds(self, fruits):
        """Result should be between 1 and len(fruits)."""
        result = total_fruit(fruits)
        assert 1 <= result <= len(fruits), f"Result {result} not in range [1, {len(fruits)}]"

    @given(fruit_type=st.integers(0, 5))
    def test_single_type_returns_full_length(self, fruit_type):
        """If all same type, return full length."""
        fruits = [fruit_type] * 10
        result = total_fruit(fruits)
        assert result == 10, "All same type should return full length"


class TestKata4Properties:
    """Property-based tests for length_of_longest_substring_k_distinct (Kata 4)"""

    @given(
        s=st.text(alphabet="abc", min_size=0, max_size=30),
        k=st.integers(0, 5)
    )
    def test_result_within_bounds(self, s, k):
        """Result should be between 0 and len(s)."""
        result = length_of_longest_substring_k_distinct(s, k)
        assert 0 <= result <= len(s), f"Result {result} not in range [0, {len(s)}]"

    @given(s=st.text(alphabet="abc", min_size=1, max_size=20))
    def test_k_zero_returns_zero(self, s):
        """If k=0, result should be 0."""
        result = length_of_longest_substring_k_distinct(s, 0)
        assert result == 0, "k=0 should return 0"


class TestKata5Properties:
    """Property-based tests for num_subarray_product_less_than_k (Kata 5)"""

    @given(
        nums=st.lists(st.integers(1, 10), min_size=1, max_size=20),
        k=st.integers(1, 100)
    )
    def test_count_non_negative(self, nums, k):
        """Count should always be non-negative."""
        result = num_subarray_product_less_than_k(nums, k)
        assert result >= 0, "Count cannot be negative"

    @given(nums=st.lists(st.integers(1, 10), min_size=1, max_size=20))
    def test_k_less_than_one_returns_zero(self, nums):
        """If k <= 1, result should be 0 (all products >= 1)."""
        result = num_subarray_product_less_than_k(nums, 1)
        assert result == 0, "k<=1 should return 0"


class TestKata6Properties:
    """Property-based tests for min_window (Kata 6)"""

    @given(
        s=st.text(alphabet="ABC", min_size=0, max_size=30),
        t=st.text(alphabet="ABC", min_size=0, max_size=10)
    )
    def test_result_contains_all_chars(self, s, t):
        """If result is non-empty, it must contain all chars of t."""
        result = min_window(s, t)
        if result:
            from collections import Counter
            result_count = Counter(result)
            t_count = Counter(t)
            for char, count in t_count.items():
                assert result_count.get(char, 0) >= count

    @given(s=st.text(alphabet="ABC", min_size=1, max_size=20))
    def test_empty_t_returns_empty(self, s):
        """If t is empty, result should be empty."""
        result = min_window(s, "")
        assert result == "", "Empty t should return empty string"


class TestKata7Properties:
    """Property-based tests for subarrays_with_k_distinct (Kata 7)"""

    @given(
        nums=st.lists(st.integers(1, 5), min_size=1, max_size=20),
        k=st.integers(0, 6)
    )
    def test_count_non_negative(self, nums, k):
        """Count should always be non-negative."""
        result = subarrays_with_k_distinct(nums, k)
        assert result >= 0, "Count cannot be negative"

    @given(nums=st.lists(st.integers(1, 5), min_size=1, max_size=20))
    def test_k_zero_returns_zero(self, nums):
        """If k=0, result should be 0."""
        result = subarrays_with_k_distinct(nums, 0)
        assert result == 0, "k=0 should return 0"
