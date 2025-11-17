"""
Pytest tests for Two Pointers (Opposite Ends) kata practice.

Quick Reference:
    pytest test_kata.py                              # Run all tests
    pytest test_kata.py::TestKata1TwoSum             # Run just kata 1
    pytest test_kata.py::TestKata2Palindrome         # Run just kata 2
    pytest -m kata1                                  # Run all kata1-level problems
    pytest -k "leetcode_examples"                    # Run LeetCode examples only

Justfile shortcuts (from workspace root):
    just kata-test two_sum                           # Test specific kata
    just kata-test-pattern two_pointers              # Test all in pattern
    just kata-test-all                               # Test everything

Mark katas as TODO by decorating with @kata_todo() when not implemented.
Remove the decorator when you've coded the solution in kata.py.
"""

import pytest
import sys
from pathlib import Path

# Add current directory and algorithms directory to path for imports
current_dir = Path(__file__).parent
algorithms_dir = current_dir.parent.parent
sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(algorithms_dir))

from conftest import kata_todo
from kata import (
    two_sum_sorted,
    is_palindrome,
    reverse_string,
    three_sum_closest,
    container_with_most_water,
)


# ============================================================================
# KATA 1: Two Sum Sorted Array
# Target: < 2 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata1TwoSum:
    """Tests for two_sum_sorted kata (LeetCode #167 variant)"""

    # LeetCode canonical examples
    LEETCODE_EXAMPLES = [
        ([2, 7, 11, 15], 9, [0, 1], "example 1: pair at start"),
        ([2, 3, 4], 6, [0, 2], "example 2: pair at middle"),
    ]

    # Edge cases for robustness
    EDGE_CASES = [
        ([1, 2, 3], 10, [], "no solution exists"),
        ([-1, 0, 2, 3], 2, [0, 3], "negative numbers"),
        ([1, 1, 1, 1], 2, [0, 3], "duplicate values"),
    ]

    @pytest.mark.kata1
    @pytest.mark.parametrize("nums,target,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, target, expected, desc):
        """LeetCode canonical examples for two sum sorted."""
        assert two_sum_sorted(nums, target) == expected

    @pytest.mark.kata1
    @pytest.mark.parametrize("nums,target,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, target, expected, desc):
        """Edge cases for two sum sorted."""
        assert two_sum_sorted(nums, target) == expected


# ============================================================================
# KATA 2: Palindrome Number (LeetCode #9)
# Target: < 2 min, zero bugs, O(log n) time, O(1) space
# ============================================================================

class TestKata2Palindrome:
    """Tests for is_palindrome kata (integers, not strings)"""

    # All test cases combined (LeetCode examples + edges)
    ALL_CASES = [
        (121, True, "example 1: basic palindrome"),
        (-121, False, "example 2: negative number"),
        (10, False, "example 3: trailing zero"),
        (0, True, "edge: zero is palindrome"),
        (12321, True, "edge: odd length palindrome"),
        (7, True, "edge: single digit"),
        (123, False, "edge: non-palindrome"),
        (1221, True, "edge: even length palindrome"),
    ]

    @pytest.mark.kata2
    @pytest.mark.parametrize("x,expected,desc",
                             ALL_CASES,
                             ids=[t[2] for t in ALL_CASES])
    def test_all_cases(self, x, expected, desc):
        """All test cases for palindrome number detection."""
        assert is_palindrome(x) == expected


# ============================================================================
# KATA 3: Reverse String In-Place (LeetCode #344)
# Target: < 1.5 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata3ReverseString:
    """Tests for reverse_string kata (in-place modification)"""

    # LeetCode examples
    LEETCODE_EXAMPLES = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"], "example 1: basic reversal"),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"], "example 2: mixed case"),
    ]

    # Edge cases
    EDGE_CASES = [
        ([], [], "empty array"),
        (["a"], ["a"], "single character"),
        (["a", "b"], ["b", "a"], "two characters"),
        (["a", "b", "c", "d"], ["d", "c", "b", "a"], "even length"),
    ]

    @pytest.mark.kata3
    @pytest.mark.parametrize("input_list,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, input_list, expected, desc):
        """LeetCode canonical examples for reverse string."""
        # Make a copy since reverse_string modifies in-place
        s = input_list.copy()
        reverse_string(s)
        assert s == expected

    @pytest.mark.kata3
    @pytest.mark.parametrize("input_list,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, input_list, expected, desc):
        """Edge cases for reverse string."""
        s = input_list.copy()
        reverse_string(s)
        assert s == expected


# ============================================================================
# KATA 4: Three Sum Closest (LeetCode #16) - ADVANCED
# Target: < 4 min, zero bugs, O(n²) time, O(1) space
# ============================================================================

class TestKata4ThreeSumClosest:
    """Tests for three_sum_closest kata (requires mastery of kata 1-2)"""

    ALL_CASES = [
        ([-1, 2, 1, -4], 1, 2, "example 1: basic case"),
        ([0, 0, 0], 1, 0, "example 2: all zeros"),
        ([1, 1, 1], 3, 3, "edge: exactly three elements"),
        ([-5, -3, -1, 0, 2, 4], 1, 1, "edge: negative numbers"),
    ]

    @kata_todo()
    @pytest.mark.kata3  # Advanced kata, requires mastery of earlier katas
    @pytest.mark.parametrize("nums,target,expected,desc",
                             ALL_CASES,
                             ids=[t[3] for t in ALL_CASES])
    def test_all_cases(self, nums, target, expected, desc):
        """All test cases for three sum closest."""
        assert three_sum_closest(nums, target) == expected


# ============================================================================
# KATA 5: Container With Most Water (LeetCode #11) - ADVANCED
# Target: < 3 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata5ContainerWater:
    """Tests for container_with_most_water kata"""

    ALL_CASES = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, "example 1: large container"),
        ([1, 1], 1, "example 2: minimum two elements"),
        ([4, 3, 2, 1, 4], 16, "edge: tallest at ends"),
        ([5, 4, 3, 2, 1], 6, "edge: descending heights"),
        ([1, 2, 3, 4, 5], 6, "edge: ascending heights"),
    ]

    @kata_todo()
    @pytest.mark.kata3  # Advanced kata
    @pytest.mark.parametrize("heights,expected,desc",
                             ALL_CASES,
                             ids=[t[2] for t in ALL_CASES])
    def test_all_cases(self, heights, expected, desc):
        """All test cases for container with most water."""
        assert container_with_most_water(heights) == expected
