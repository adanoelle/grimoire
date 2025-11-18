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
from hypothesis import given, strategies as st

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
# KATA 2: Valid Palindrome (LeetCode #125)
# Target: < 2 min, zero bugs, O(n) time, O(1) space
# ============================================================================

class TestKata2Palindrome:
    """Tests for is_palindrome kata (LeetCode #125 - Valid Palindrome)"""

    # LeetCode examples + edge cases for string palindromes
    ALL_CASES = [
        ("A man, a plan, a canal: Panama", True, "example 1: classic palindrome with spaces/punctuation"),
        ("race a car", False, "example 2: not a palindrome"),
        (" ", True, "example 3: single space"),
        ("", True, "edge: empty string"),
        ("a", True, "edge: single character"),
        ("ab", False, "edge: two chars non-palindrome"),
        ("aa", True, "edge: two chars palindrome"),
        ("Madam", True, "edge: mixed case palindrome"),
        ("0P", False, "edge: alphanumeric non-palindrome"),
        (".,", True, "edge: all non-alphanumeric"),
    ]

    @pytest.mark.kata2
    @pytest.mark.parametrize("s,expected,desc",
                             ALL_CASES,
                             ids=[t[2] for t in ALL_CASES])
    def test_all_cases(self, s, expected, desc):
        """All test cases for string palindrome detection."""
        assert is_palindrome(s) == expected


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


# ============================================================================
# PROPERTY-BASED TESTS (Using Hypothesis)
# ============================================================================

class TestKata1Properties:
    """Property-based tests for two_sum_sorted (Kata 1)"""

    @given(
        nums=st.lists(st.integers(-1000, 1000), min_size=0, max_size=100).map(sorted),
        target=st.integers(-2000, 2000)
    )
    def test_solution_validity(self, nums, target):
        """If solution exists, the sum of the two numbers equals target."""
        result = two_sum_sorted(nums, target)
        if result:
            assert len(result) == 2, "Result should contain exactly 2 indices"
            i, j = result
            assert 0 <= i < len(nums), "First index out of bounds"
            assert 0 <= j < len(nums), "Second index out of bounds"
            assert i < j, "Indices should be in order (i < j)"
            assert nums[i] + nums[j] == target, f"Sum {nums[i]} + {nums[j]} != {target}"

    @given(st.lists(st.integers(-100, 100), min_size=2, max_size=50).map(sorted))
    def test_always_finds_sum_of_endpoints(self, nums):
        """Should always find the sum of first and last elements."""
        target = nums[0] + nums[-1]
        result = two_sum_sorted(nums, target)
        assert result is not None, f"Should find {nums[0]} + {nums[-1]} = {target}"
        i, j = result
        assert nums[i] + nums[j] == target


class TestKata2Properties:
    """Property-based tests for is_palindrome (Kata 2)"""

    @given(st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=0, max_size=50))
    def test_lowercase_letters_symmetry(self, s):
        """For lowercase letters only, palindrome means string equals its reverse."""
        result = is_palindrome(s)
        expected = (s == s[::-1])
        assert result == expected, f"Palindrome check for '{s}' should be {expected}"

    @given(st.text(min_size=0, max_size=30))
    def test_single_char_always_palindrome(self, base):
        """Single character strings are always palindromes."""
        if len(base) == 1 and base.isalnum():
            assert is_palindrome(base) == True

    @given(st.text(alphabet="!@#$%^&*() ", min_size=0, max_size=20))
    def test_no_alphanumeric_always_true(self, s):
        """Strings with no alphanumeric characters should be considered palindromes."""
        if not any(c.isalnum() for c in s):
            assert is_palindrome(s) == True, f"Non-alphanumeric string '{s}' should be palindrome"

    @given(st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll')), min_size=1, max_size=20))
    def test_case_insensitivity(self, s):
        """Palindrome check should be case-insensitive."""
        # If s is palindrome, changing case shouldn't affect result
        if s.isalpha():
            lower_result = is_palindrome(s.lower())
            upper_result = is_palindrome(s.upper())
            mixed_result = is_palindrome(s)
            # All should agree (either all True or all False)
            assert lower_result == upper_result == mixed_result, \
                f"Case variants of '{s}' should have same palindrome status"
