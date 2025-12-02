"""
Pytest tests for Binary Search kata practice.

Quick Reference:
    pytest test_kata.py                              # Run all tests
    pytest test_kata.py::TestKata1ClassicBinarySearch  # Run just kata 1
    pytest test_kata.py -m kata1                     # Run all kata1-level problems
    pytest test_kata.py -m kata6                     # Run kata 6 only
    pytest -k "examples"                             # Run examples only
    pytest -v                                        # Verbose output

Justfile shortcuts (from workspace root):
    just kata::test searching/binary_search
    just binary-search::test
    just binary-search::test-kata1

Mark katas as TODO by decorating with @kata_todo() when not implemented.
Remove the decorator when you've coded the solution in kata.py.
"""

import pytest
import sys
from pathlib import Path
from hypothesis import given, strategies as st, assume

# Add current directory and algorithms directory to path for imports
current_dir = Path(__file__).parent
algorithms_dir = current_dir.parent.parent
sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(algorithms_dir))

from kata import (
    binary_search_classic,
    find_first_occurrence,
    find_last_occurrence,
    search_insert_position,
    search_rotated_array,
    find_peak_element,
)


# ============================================================================
# KATA 1: Classic Binary Search (LeetCode #704)
# Target: < 2 min, ZERO bugs, O(log n) time, O(1) space
# THE MOST IMPORTANT KATA - 100 rep goal!
# ============================================================================

class TestKata1ClassicBinarySearch:
    """Tests for binary_search_classic kata (LeetCode #704)"""

    LEETCODE_EXAMPLES = [
        ([1, 2, 3, 4, 5], 3, 2, "example 1: target in middle"),
        ([1, 2, 3, 4, 5], 6, -1, "example 2: target not found"),
        ([], 1, -1, "example 3: empty array"),
        ([5], 5, 0, "example 4: single element found"),
    ]

    EDGE_CASES = [
        ([5], 3, -1, "edge: single element not found"),
        ([1, 2], 1, 0, "edge: target at start"),
        ([1, 2], 2, 1, "edge: target at end"),
        ([1, 3, 5, 7, 9], 1, 0, "edge: target is first element"),
        ([1, 3, 5, 7, 9], 9, 4, "edge: target is last element"),
        ([-5, -3, 0, 2, 4], 0, 2, "edge: negative numbers"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 6, "edge: larger array"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata1
    @pytest.mark.examples
    @pytest.mark.parametrize("nums,target,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, target, expected, desc):
        """LeetCode canonical examples."""
        assert binary_search_classic(nums, target) == expected

    @pytest.mark.kata1
    @pytest.mark.edge
    @pytest.mark.parametrize("nums,target,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, target, expected, desc):
        """Edge cases for classic binary search."""
        assert binary_search_classic(nums, target) == expected


# ============================================================================
# KATA 2: Find First Occurrence
# Target: < 3 min, zero bugs, O(log n) time, O(1) space
# ============================================================================

class TestKata2FindFirstOccurrence:
    """Tests for find_first_occurrence kata"""

    LEETCODE_EXAMPLES = [
        ([1, 2, 2, 2, 3], 2, 1, "example 1: multiple occurrences, find first"),
        ([2, 2, 2, 2, 2], 2, 0, "example 2: all same elements"),
        ([1, 2, 3], 4, -1, "example 3: target not found"),
    ]

    EDGE_CASES = [
        ([], 1, -1, "edge: empty array"),
        ([5], 5, 0, "edge: single element found"),
        ([5], 3, -1, "edge: single element not found"),
        ([1, 1, 1, 2, 2, 2, 3, 3, 3], 2, 3, "edge: target in middle group"),
        ([1, 2, 3, 4, 5], 1, 0, "edge: first element is target"),
        ([1, 2, 3, 4, 5], 5, 4, "edge: no duplicates, last element"),
        ([1, 1, 1, 1, 1, 1, 1, 2], 2, 7, "edge: target at very end"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata2
    @pytest.mark.examples
    @pytest.mark.parametrize("nums,target,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, target, expected, desc):
        """LeetCode canonical examples."""
        assert find_first_occurrence(nums, target) == expected

    @pytest.mark.kata2
    @pytest.mark.edge
    @pytest.mark.parametrize("nums,target,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, target, expected, desc):
        """Edge cases for find first occurrence."""
        assert find_first_occurrence(nums, target) == expected


# ============================================================================
# KATA 3: Find Last Occurrence
# Target: < 3 min, zero bugs, O(log n) time, O(1) space
# ============================================================================

class TestKata3FindLastOccurrence:
    """Tests for find_last_occurrence kata"""

    LEETCODE_EXAMPLES = [
        ([1, 2, 2, 2, 3], 2, 3, "example 1: multiple occurrences, find last"),
        ([2, 2, 2, 2, 2], 2, 4, "example 2: all same elements"),
        ([1, 2, 3], 4, -1, "example 3: target not found"),
    ]

    EDGE_CASES = [
        ([], 1, -1, "edge: empty array"),
        ([5], 5, 0, "edge: single element found"),
        ([5], 3, -1, "edge: single element not found"),
        ([1, 1, 1, 2, 2, 2, 3, 3, 3], 2, 5, "edge: target in middle group"),
        ([1, 2, 3, 4, 5], 5, 4, "edge: last element is target"),
        ([1, 2, 3, 4, 5], 1, 0, "edge: no duplicates, first element"),
        ([1, 2, 2, 2, 2, 2, 2, 2], 2, 7, "edge: target fills most of array"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata3
    @pytest.mark.examples
    @pytest.mark.parametrize("nums,target,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, target, expected, desc):
        """LeetCode canonical examples."""
        assert find_last_occurrence(nums, target) == expected

    @pytest.mark.kata3
    @pytest.mark.edge
    @pytest.mark.parametrize("nums,target,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, target, expected, desc):
        """Edge cases for find last occurrence."""
        assert find_last_occurrence(nums, target) == expected


# ============================================================================
# KATA 4: Search Insert Position (LeetCode #35)
# Target: < 2 min, zero bugs, O(log n) time, O(1) space
# ============================================================================

class TestKata4SearchInsertPosition:
    """Tests for search_insert_position kata (LeetCode #35)"""

    LEETCODE_EXAMPLES = [
        ([1, 3, 5, 6], 5, 2, "example 1: target found"),
        ([1, 3, 5, 6], 2, 1, "example 2: insert in middle"),
        ([1, 3, 5, 6], 7, 4, "example 3: insert at end"),
        ([1, 3, 5, 6], 0, 0, "example 4: insert at start"),
    ]

    EDGE_CASES = [
        ([], 5, 0, "edge: empty array"),
        ([1], 0, 0, "edge: insert before single element"),
        ([1], 1, 0, "edge: target equals single element"),
        ([1], 2, 1, "edge: insert after single element"),
        ([1, 3], 2, 1, "edge: insert between two elements"),
        ([1, 3, 5, 7, 9], 4, 2, "edge: insert in middle of odd-length array"),
        ([2, 4, 6, 8, 10], 1, 0, "edge: insert before all even numbers"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata4
    @pytest.mark.examples
    @pytest.mark.parametrize("nums,target,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, target, expected, desc):
        """LeetCode canonical examples."""
        assert search_insert_position(nums, target) == expected

    @pytest.mark.kata4
    @pytest.mark.edge
    @pytest.mark.parametrize("nums,target,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, target, expected, desc):
        """Edge cases for search insert position."""
        assert search_insert_position(nums, target) == expected


# ============================================================================
# KATA 5: Search in Rotated Sorted Array (LeetCode #33)
# Target: < 5 min, zero bugs, O(log n) time, O(1) space
# ADVANCED - Master katas 1-4 first!
# ============================================================================

class TestKata5SearchRotatedArray:
    """Tests for search_rotated_array kata (LeetCode #33)"""

    LEETCODE_EXAMPLES = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4, "example 1: target in right half"),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1, "example 2: target not found"),
        ([1], 0, -1, "example 3: single element not found"),
    ]

    EDGE_CASES = [
        ([1], 1, 0, "edge: single element found"),
        ([2, 1], 1, 1, "edge: two elements, find second"),
        ([2, 1], 2, 0, "edge: two elements, find first"),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0, "edge: target is pivot (first element)"),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6, "edge: target is last element"),
        ([4, 5, 6, 7, 0, 1, 2], 6, 2, "edge: target in left sorted half"),
        ([3, 1, 2], 3, 0, "edge: small rotation"),
        ([5, 1, 2, 3, 4], 1, 1, "edge: target right after rotation point"),
        ([1, 2, 3, 4, 5], 3, 2, "edge: not rotated (rotation = 0)"),
    ]

    ALL_CASES = LEETCODE_EXAMPLES + EDGE_CASES

    @pytest.mark.kata5
    @pytest.mark.examples
    @pytest.mark.parametrize("nums,target,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, target, expected, desc):
        """LeetCode canonical examples."""
        assert search_rotated_array(nums, target) == expected

    @pytest.mark.kata5
    @pytest.mark.edge
    @pytest.mark.parametrize("nums,target,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, nums, target, expected, desc):
        """Edge cases for search in rotated array."""
        assert search_rotated_array(nums, target) == expected


# ============================================================================
# KATA 6: Find Peak Element (LeetCode #162)
# Target: < 4 min, zero bugs, O(log n) time, O(1) space
# ADVANCED - Master katas 1-4 first!
# ============================================================================

class TestKata6FindPeakElement:
    """Tests for find_peak_element kata (LeetCode #162)"""

    LEETCODE_EXAMPLES = [
        ([1, 2, 3, 1], "example 1: single peak in middle"),
        ([1, 2, 1, 3, 5, 6, 4], "example 2: multiple peaks"),
    ]

    EDGE_CASES = [
        ([1], "edge: single element is peak"),
        ([2, 1], "edge: peak at start"),
        ([1, 2], "edge: peak at end"),
        ([1, 3, 2], "edge: peak in middle of 3 elements"),
        ([1, 2, 3, 4, 5], "edge: ascending array, peak at end"),
        ([5, 4, 3, 2, 1], "edge: descending array, peak at start"),
        ([1, 2, 3, 2, 1], "edge: symmetric mountain"),
    ]

    def is_valid_peak(self, nums, idx):
        """Helper to check if idx is a valid peak."""
        if not nums:
            return False
        n = len(nums)
        left_ok = idx == 0 or nums[idx] > nums[idx - 1]
        right_ok = idx == n - 1 or nums[idx] > nums[idx + 1]
        return left_ok and right_ok

    @pytest.mark.kata6
    @pytest.mark.examples
    @pytest.mark.parametrize("nums,desc", LEETCODE_EXAMPLES,
                             ids=[t[1] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, nums, desc):
        """LeetCode canonical examples - verify result is a valid peak."""
        result = find_peak_element(nums)
        assert self.is_valid_peak(nums, result), \
            f"Index {result} is not a valid peak in {nums}"

    @pytest.mark.kata6
    @pytest.mark.edge
    @pytest.mark.parametrize("nums,desc", EDGE_CASES,
                             ids=[t[1] for t in EDGE_CASES])
    def test_edge_cases(self, nums, desc):
        """Edge cases - verify result is a valid peak."""
        result = find_peak_element(nums)
        assert self.is_valid_peak(nums, result), \
            f"Index {result} is not a valid peak in {nums}"


# ============================================================================
# PROPERTY-BASED TESTS (Using Hypothesis)
# ============================================================================

class TestKata1Properties:
    """Property-based tests for binary_search_classic (Kata 1)"""

    @given(
        nums=st.lists(st.integers(-1000, 1000), min_size=0, max_size=100).map(sorted),
        target=st.integers(-1000, 1000)
    )
    def test_found_means_element_exists(self, nums, target):
        """If found (>= 0), nums[result] must equal target."""
        result = binary_search_classic(nums, target)
        if result >= 0:
            assert nums[result] == target, \
                f"Found index {result} but nums[{result}]={nums[result]} != {target}"

    @given(
        nums=st.lists(st.integers(-1000, 1000), min_size=0, max_size=100).map(sorted),
        target=st.integers(-1000, 1000)
    )
    def test_not_found_means_element_absent(self, nums, target):
        """If not found (-1), target must not be in array."""
        result = binary_search_classic(nums, target)
        if result == -1:
            assert target not in nums, \
                f"Returned -1 but {target} is in {nums}"

    @given(
        nums=st.lists(st.integers(-1000, 1000), min_size=1, max_size=100).map(sorted)
    )
    def test_search_existing_element_finds_it(self, nums):
        """Searching for an element that exists should find it."""
        target = nums[len(nums) // 2]  # Pick middle element
        result = binary_search_classic(nums, target)
        assert result >= 0, f"Failed to find {target} in {nums}"
        assert nums[result] == target


class TestKata2Properties:
    """Property-based tests for find_first_occurrence (Kata 2)"""

    @given(
        nums=st.lists(st.integers(-100, 100), min_size=1, max_size=50).map(sorted),
        target=st.integers(-100, 100)
    )
    def test_first_occurrence_is_leftmost(self, nums, target):
        """If found, no earlier index should have the same value."""
        result = find_first_occurrence(nums, target)
        if result >= 0:
            assert nums[result] == target
            for i in range(result):
                assert nums[i] != target, \
                    f"Found earlier occurrence at {i}, but returned {result}"


class TestKata3Properties:
    """Property-based tests for find_last_occurrence (Kata 3)"""

    @given(
        nums=st.lists(st.integers(-100, 100), min_size=1, max_size=50).map(sorted),
        target=st.integers(-100, 100)
    )
    def test_last_occurrence_is_rightmost(self, nums, target):
        """If found, no later index should have the same value."""
        result = find_last_occurrence(nums, target)
        if result >= 0:
            assert nums[result] == target
            for i in range(result + 1, len(nums)):
                assert nums[i] != target, \
                    f"Found later occurrence at {i}, but returned {result}"


class TestKata4Properties:
    """Property-based tests for search_insert_position (Kata 4)"""

    @given(
        nums=st.lists(st.integers(-100, 100), min_size=0, max_size=50).map(sorted).map(lambda x: list(dict.fromkeys(x))),
        target=st.integers(-100, 100)
    )
    def test_insert_maintains_sorted_order(self, nums, target):
        """Inserting at result position should maintain sorted order."""
        result = search_insert_position(nums, target)

        # Check bounds
        assert 0 <= result <= len(nums), \
            f"Insert position {result} out of bounds [0, {len(nums)}]"

        # Check sorted order would be maintained
        if result > 0:
            assert nums[result - 1] <= target, \
                f"Element before insert ({nums[result-1]}) > target ({target})"
        if result < len(nums):
            assert target <= nums[result], \
                f"Target ({target}) > element at insert ({nums[result]})"


class TestKata5Properties:
    """Property-based tests for search_rotated_array (Kata 5)"""

    @given(
        nums=st.lists(st.integers(-100, 100), min_size=1, max_size=30, unique=True).map(sorted),
        rotation=st.integers(0, 100)
    )
    def test_finds_element_in_rotated_array(self, nums, rotation):
        """Should find elements that exist in rotated array."""
        # Rotate the array
        n = len(nums)
        rotation = rotation % n
        rotated = nums[rotation:] + nums[:rotation]

        # Pick an element to search for
        target = rotated[n // 2]
        result = search_rotated_array(rotated, target)

        assert result >= 0, f"Failed to find {target} in {rotated}"
        assert rotated[result] == target


class TestKata6Properties:
    """Property-based tests for find_peak_element (Kata 6)"""

    @given(nums=st.lists(st.integers(-1000, 1000), min_size=1, max_size=50, unique=True))
    def test_result_is_valid_peak(self, nums):
        """Result should always be a valid peak index."""
        result = find_peak_element(nums)
        n = len(nums)

        assert 0 <= result < n, f"Index {result} out of bounds"

        left_ok = result == 0 or nums[result] > nums[result - 1]
        right_ok = result == n - 1 or nums[result] > nums[result + 1]

        assert left_ok and right_ok, \
            f"Index {result} (value {nums[result]}) is not a peak in {nums}"
