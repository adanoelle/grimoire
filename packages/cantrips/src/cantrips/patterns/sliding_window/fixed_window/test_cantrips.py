"""
Tests for Fixed Window Sliding Window cantrips.

Run tests:
    pytest test_cantrips.py                    # All tests
    pytest test_cantrips.py -m cantrip1        # Just cantrip 1
    pytest test_cantrips.py -k "examples"      # Just examples
    pytest test_cantrips.py -v                 # Verbose output
"""

import pytest

from p001_find_max_average import find_max_average
from p002_num_of_subarrays import num_of_subarrays
from p003_count_good_substrings import count_good_substrings
from p004_check_inclusion import check_inclusion
from p005_find_anagrams import find_anagrams


# ============================================================================
# CANTRIP 1: Maximum Average Subarray I (LeetCode #643)
# ============================================================================


class TestCantrip1:
    """Tests for find_max_average (LeetCode #643)."""

    EXAMPLES = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75, "mixed positive/negative"),
        ([5], 1, 5.0, "single element"),
    ]

    EDGE_CASES = [
        ([1, 2, 3, 4, 5], 5, 3.0, "k equals length"),
        ([1, 2, 3, 4, 5], 1, 5.0, "k equals 1"),
        ([-1, -2, -3, -4], 2, -1.5, "all negative"),
        ([5, 5, 5, 5], 2, 5.0, "all equal"),
        ([100, 200, 300, 400], 2, 350.0, "large ascending"),
    ]

    @pytest.mark.cantrip1
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "nums,k,expected,desc", EXAMPLES, ids=[t[3] for t in EXAMPLES]
    )
    def test_examples(self, nums, k, expected, desc):
        """LeetCode examples."""
        result = find_max_average(nums, k)
        assert abs(result - expected) < 0.001

    @pytest.mark.cantrip1
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "nums,k,expected,desc", EDGE_CASES, ids=[t[3] for t in EDGE_CASES]
    )
    def test_edge_cases(self, nums, k, expected, desc):
        """Edge cases."""
        result = find_max_average(nums, k)
        assert abs(result - expected) < 0.001


# ============================================================================
# CANTRIP 2: Number of Sub-arrays of Size K (LeetCode #1343)
# ============================================================================


class TestCantrip2:
    """Tests for num_of_subarrays (LeetCode #1343)."""

    EXAMPLES = [
        ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3, "some meet threshold"),
        ([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5, 6, "most meet threshold"),
    ]

    EDGE_CASES = [
        ([1, 1, 1, 1, 1], 1, 0, 5, "all meet (k=1)"),
        ([1, 1, 1, 1, 1], 3, 10, 0, "none meet"),
        ([5, 10, 15], 2, 7, 2, "all meet"),
        ([1, 2, 3], 3, 0, 1, "threshold 0"),
        ([10, 20, 30, 40], 2, 25, 2, "half meet"),
    ]

    @pytest.mark.cantrip2
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "arr,k,threshold,expected,desc", EXAMPLES, ids=[t[4] for t in EXAMPLES]
    )
    def test_examples(self, arr, k, threshold, expected, desc):
        """LeetCode examples."""
        assert num_of_subarrays(arr, k, threshold) == expected

    @pytest.mark.cantrip2
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "arr,k,threshold,expected,desc", EDGE_CASES, ids=[t[4] for t in EDGE_CASES]
    )
    def test_edge_cases(self, arr, k, threshold, expected, desc):
        """Edge cases."""
        assert num_of_subarrays(arr, k, threshold) == expected


# ============================================================================
# CANTRIP 3: Good Substrings (LeetCode #1876)
# ============================================================================


class TestCantrip3:
    """Tests for count_good_substrings (LeetCode #1876)."""

    EXAMPLES = [
        ("xyzzaz", 1, "some repeating"),
        ("aababcabc", 4, "multiple good"),
    ]

    EDGE_CASES = [
        ("a", 0, "length < 3"),
        ("ab", 0, "length < 3"),
        ("abc", 1, "exactly 3 distinct"),
        ("aaa", 0, "all same"),
        ("abcdef", 4, "all distinct"),
        ("aabbaabb", 0, "no good"),
    ]

    @pytest.mark.cantrip3
    @pytest.mark.examples
    @pytest.mark.parametrize("s,expected,desc", EXAMPLES, ids=[t[2] for t in EXAMPLES])
    def test_examples(self, s, expected, desc):
        """LeetCode examples."""
        assert count_good_substrings(s) == expected

    @pytest.mark.cantrip3
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "s,expected,desc", EDGE_CASES, ids=[t[2] for t in EDGE_CASES]
    )
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert count_good_substrings(s) == expected


# ============================================================================
# CANTRIP 4: Permutation in String (LeetCode #567)
# ============================================================================


class TestCantrip4:
    """Tests for check_inclusion (LeetCode #567)."""

    EXAMPLES = [
        ("ab", "eidbaooo", True, "permutation exists"),
        ("ab", "eidboaoo", False, "no permutation"),
    ]

    EDGE_CASES = [
        ("a", "a", True, "single char match"),
        ("a", "b", False, "single char no match"),
        ("ab", "a", False, "s1 longer"),
        ("abc", "bbbca", True, "permutation at end"),
        ("abc", "ccccbbbbaaaa", False, "chars present but not contiguous"),
        ("adc", "dcda", True, "permutation exists"),
    ]

    @pytest.mark.cantrip4
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "s1,s2,expected,desc", EXAMPLES, ids=[t[3] for t in EXAMPLES]
    )
    def test_examples(self, s1, s2, expected, desc):
        """LeetCode examples."""
        assert check_inclusion(s1, s2) == expected

    @pytest.mark.cantrip4
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "s1,s2,expected,desc", EDGE_CASES, ids=[t[3] for t in EDGE_CASES]
    )
    def test_edge_cases(self, s1, s2, expected, desc):
        """Edge cases."""
        assert check_inclusion(s1, s2) == expected


# ============================================================================
# CANTRIP 5: Find All Anagrams (LeetCode #438)
# ============================================================================


class TestCantrip5:
    """Tests for find_anagrams (LeetCode #438)."""

    EXAMPLES = [
        ("cbaebabacd", "abc", [0, 6], "two anagrams"),
        ("abab", "ab", [0, 1, 2], "overlapping"),
    ]

    EDGE_CASES = [
        ("a", "a", [0], "single char match"),
        ("a", "b", [], "single char no match"),
        ("abc", "abcd", [], "p longer than s"),
        ("aaaaaaa", "aaa", [0, 1, 2, 3, 4], "repeated char"),
        ("baa", "aa", [1], "anagram at end"),
    ]

    @pytest.mark.cantrip5
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "s,p,expected,desc", EXAMPLES, ids=[t[3] for t in EXAMPLES]
    )
    def test_examples(self, s, p, expected, desc):
        """LeetCode examples."""
        assert find_anagrams(s, p) == expected

    @pytest.mark.cantrip5
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "s,p,expected,desc", EDGE_CASES, ids=[t[3] for t in EDGE_CASES]
    )
    def test_edge_cases(self, s, p, expected, desc):
        """Edge cases."""
        assert find_anagrams(s, p) == expected
