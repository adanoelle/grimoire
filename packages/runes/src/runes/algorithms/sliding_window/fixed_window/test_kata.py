"""
Pytest tests for Sliding Window (Fixed Size) kata practice.

Quick Reference:
    pytest test_kata.py                              # Run all tests
    pytest test_kata.py::TestKata1MaxAverage         # Run just kata 1
    pytest test_kata.py::TestKata2NumSubarrays       # Run just kata 2
    pytest -m kata1                                  # Run all kata1-level problems
    pytest -k "examples"                             # Run examples only

Justfile shortcuts (from workspace root):
    just kata::test sliding_window/fixed_window
    just fixed-window::test
    just fixed-window::test-kata1

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
    find_max_average,
    num_of_subarrays,
    count_good_substrings,
    check_inclusion,
    find_anagrams,
)


# ============================================================================
# KATA 1: Maximum Average Subarray I (LeetCode #643)
# Target: < 2 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata1MaxAverage:
    """Tests for find_max_average kata (LeetCode #643)"""

    LEETCODE_EXAMPLES = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75, "example 1: mixed positive/negative"),
        ([5], 1, 5.0, "example 2: single element"),
    ]

    EDGE_CASES = [
        ([1, 2, 3, 4, 5], 5, 3.0, "edge: k equals length"),
        ([1, 2, 3, 4, 5], 1, 5.0, "edge: k equals 1, max element"),
        ([-1, -2, -3, -4], 2, -1.5, "edge: all negative numbers"),
        ([5, 5, 5, 5], 2, 5.0, "edge: all equal elements"),
        ([100, 200, 300, 400], 2, 350.0, "edge: large ascending"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata1
    @pytest.mark.parametrize("nums,k,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, k, expected, desc):
        """LeetCode canonical examples."""
        result = find_max_average(nums, k)
        assert abs(result - expected) < 0.001, f"Expected {expected}, got {result}"

    @pytest.mark.kata1
    @pytest.mark.parametrize("nums,k,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, k, expected, desc):
        """Edge cases for maximum average subarray."""
        result = find_max_average(nums, k)
        assert abs(result - expected) < 0.001, f"Expected {expected}, got {result}"


# ============================================================================
# KATA 2: Number of Sub-arrays of Size K and Average >= Threshold (LeetCode #1343)
# Target: < 2.5 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata2NumSubarrays:
    """Tests for num_of_subarrays kata (LeetCode #1343)"""

    LEETCODE_EXAMPLES = [
        ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3, "example 1: some subarrays meet threshold"),
        ([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5, 6, "example 2: most subarrays meet threshold"),
    ]

    EDGE_CASES = [
        ([1, 1, 1, 1, 1], 1, 0, 5, "edge: all meet threshold (k=1)"),
        ([1, 1, 1, 1, 1], 3, 10, 0, "edge: none meet threshold"),
        ([5, 10, 15], 2, 7, 2, "edge: all subarrays meet threshold"),
        ([1, 2, 3], 3, 0, 1, "edge: threshold is 0"),
        ([10, 20, 30, 40], 2, 25, 2, "edge: exactly half meet threshold"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata2
    @pytest.mark.parametrize("arr,k,threshold,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[4] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, arr, k, threshold, expected, desc):
        """LeetCode canonical examples."""
        assert num_of_subarrays(arr, k, threshold) == expected

    @pytest.mark.kata2
    @pytest.mark.parametrize("arr,k,threshold,expected,desc",
                             EDGE_CASES,
                             ids=[t[4] for t in EDGE_CASES])
    def test_edge_cases(self, arr, k, threshold, expected, desc):
        """Edge cases for num of subarrays."""
        assert num_of_subarrays(arr, k, threshold) == expected


# ============================================================================
# KATA 3: Substrings of Size Three with Distinct Characters (LeetCode #1876)
# Target: < 2 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata3GoodSubstrings:
    """Tests for count_good_substrings kata (LeetCode #1876)"""

    LEETCODE_EXAMPLES = [
        ("xyzzaz", 1, "example 1: some repeating characters"),
        ("aababcabc", 4, "example 2: multiple good substrings"),
    ]

    EDGE_CASES = [
        ("a", 0, "edge: length < 3"),
        ("ab", 0, "edge: length < 3"),
        ("abc", 1, "edge: length == 3, all distinct"),
        ("aaa", 0, "edge: all same character"),
        ("abcdef", 4, "edge: all distinct characters"),
        ("aabbaabb", 0, "edge: no good substrings"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata3
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert count_good_substrings(s) == expected

    @pytest.mark.kata3
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases for good substrings."""
        assert count_good_substrings(s) == expected


# ============================================================================
# KATA 4: Permutation in String (LeetCode #567)
# Target: < 4 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata4CheckInclusion:
    """Tests for check_inclusion kata (LeetCode #567)"""

    LEETCODE_EXAMPLES = [
        ("ab", "eidbaooo", True, "example 1: permutation exists"),
        ("ab", "eidboaoo", False, "example 2: no permutation"),
    ]

    EDGE_CASES = [
        ("a", "a", True, "edge: single character match"),
        ("a", "b", False, "edge: single character no match"),
        ("ab", "a", False, "edge: s1 longer than s2"),
        ("abc", "bbbca", True, "edge: permutation at end"),
        ("abc", "ccccbbbbaaaa", False, "edge: all chars present but not contiguous"),
        ("adc", "dcda", True, "edge: permutation exists"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata4
    @pytest.mark.parametrize("s1,s2,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s1, s2, expected, desc):
        """LeetCode canonical examples."""
        assert check_inclusion(s1, s2) == expected

    @pytest.mark.kata4
    @pytest.mark.parametrize("s1,s2,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, s1, s2, expected, desc):
        """Edge cases for permutation in string."""
        assert check_inclusion(s1, s2) == expected


# ============================================================================
# KATA 5: Find All Anagrams in a String (LeetCode #438)
# Target: < 4.5 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata5FindAnagrams:
    """Tests for find_anagrams kata (LeetCode #438)"""

    LEETCODE_EXAMPLES = [
        ("cbaebabacd", "abc", [0, 6], "example 1: two anagrams found"),
        ("abab", "ab", [0, 1, 2], "example 2: overlapping anagrams"),
    ]

    EDGE_CASES = [
        ("a", "a", [0], "edge: single character match"),
        ("a", "b", [], "edge: single character no match"),
        ("abc", "abcd", [], "edge: p longer than s"),
        ("aaaaaaa", "aaa", [0, 1, 2, 3, 4], "edge: repeated character"),
        ("baa", "aa", [1], "edge: anagram at end only"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata5
    @pytest.mark.parametrize("s,p,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, p, expected, desc):
        """LeetCode canonical examples."""
        assert find_anagrams(s, p) == expected

    @pytest.mark.kata5
    @pytest.mark.parametrize("s,p,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, s, p, expected, desc):
        """Edge cases for find all anagrams."""
        assert find_anagrams(s, p) == expected


# ============================================================================
# PROPERTY-BASED TESTS (Using Hypothesis)
# ============================================================================

class TestKata1Properties:
    """Property-based tests for find_max_average (Kata 1)"""

    @given(
        nums=st.lists(st.integers(-100, 100), min_size=1, max_size=50),
        k=st.integers(1, 10)
    )
    def test_average_within_bounds(self, nums, k):
        """The maximum average should be between min and max of array."""
        if k > len(nums):
            return  # Skip invalid inputs

        result = find_max_average(nums, k)
        min_val = min(nums)
        max_val = max(nums)
        assert min_val <= result <= max_val, \
            f"Average {result} not in range [{min_val}, {max_val}]"

    @given(nums=st.lists(st.integers(-100, 100), min_size=1, max_size=50))
    def test_k_equals_length_returns_total_average(self, nums):
        """When k equals array length, should return average of entire array."""
        k = len(nums)
        result = find_max_average(nums, k)
        expected = sum(nums) / len(nums)
        assert abs(result - expected) < 0.001


class TestKata2Properties:
    """Property-based tests for num_of_subarrays (Kata 2)"""

    @given(
        arr=st.lists(st.integers(0, 100), min_size=1, max_size=30),
        k=st.integers(1, 10),
        threshold=st.integers(0, 100)
    )
    def test_count_non_negative(self, arr, k, threshold):
        """Count should always be non-negative."""
        if k > len(arr):
            return

        result = num_of_subarrays(arr, k, threshold)
        assert result >= 0, "Count cannot be negative"

    @given(
        arr=st.lists(st.integers(0, 100), min_size=1, max_size=30),
        k=st.integers(1, 10)
    )
    def test_count_upper_bound(self, arr, k):
        """Count cannot exceed number of possible windows."""
        if k > len(arr):
            return

        max_windows = len(arr) - k + 1
        result = num_of_subarrays(arr, k, 0)  # threshold=0, all should pass
        assert result <= max_windows, f"Count {result} exceeds max windows {max_windows}"


class TestKata3Properties:
    """Property-based tests for count_good_substrings (Kata 3)"""

    @given(s=st.text(alphabet="abc", min_size=0, max_size=50))
    def test_count_non_negative(self, s):
        """Count should always be non-negative."""
        result = count_good_substrings(s)
        assert result >= 0, "Count cannot be negative"

    @given(s=st.text(alphabet="abc", min_size=0, max_size=50))
    def test_count_upper_bound(self, s):
        """Count cannot exceed possible windows."""
        result = count_good_substrings(s)
        max_possible = max(0, len(s) - 2)
        assert result <= max_possible, f"Count {result} exceeds max {max_possible}"


class TestKata4Properties:
    """Property-based tests for check_inclusion (Kata 4)"""

    @given(s1=st.text(alphabet="abcde", min_size=1, max_size=10))
    def test_string_contains_itself_permutation(self, s1):
        """A string always contains a permutation of itself."""
        result = check_inclusion(s1, s1)
        assert result == True, f"'{s1}' should contain permutation of itself"

    @given(
        s1=st.text(alphabet="abc", min_size=1, max_size=5),
        s2=st.text(alphabet="xyz", min_size=1, max_size=10)
    )
    def test_disjoint_alphabets_return_false(self, s1, s2):
        """If alphabets are disjoint, no permutation can exist."""
        # Only test if alphabets are truly disjoint
        s1_chars = set(s1)
        s2_chars = set(s2)
        if not (s1_chars & s2_chars):  # No overlap
            result = check_inclusion(s1, s2)
            assert result == False, "Disjoint alphabets cannot have permutation"


class TestKata5Properties:
    """Property-based tests for find_anagrams (Kata 5)"""

    @given(
        s=st.text(alphabet="abc", min_size=0, max_size=30),
        p=st.text(alphabet="abc", min_size=1, max_size=5)
    )
    def test_result_list_sorted(self, s, p):
        """Result indices should be in ascending order."""
        result = find_anagrams(s, p)
        assert result == sorted(result), "Indices should be sorted"

    @given(
        s=st.text(alphabet="abc", min_size=0, max_size=30),
        p=st.text(alphabet="abc", min_size=1, max_size=5)
    )
    def test_indices_within_bounds(self, s, p):
        """All returned indices should be valid."""
        result = find_anagrams(s, p)
        for idx in result:
            assert 0 <= idx <= len(s) - len(p), f"Index {idx} out of bounds"
