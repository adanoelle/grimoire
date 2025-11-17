"""
Pytest tests for [PATTERN NAME] kata practice.

Quick Reference:
    pytest test_kata.py                              # Run all tests
    pytest test_kata.py::TestKata1FunctionName       # Run just kata 1
    pytest test_kata.py::TestKata2FunctionName       # Run just kata 2
    pytest -m kata1                                  # Run all kata1-level problems
    pytest -k "leetcode_examples"                    # Run LeetCode examples only

Justfile shortcuts (from workspace root):
    just kata-test function_name                     # Test specific kata
    just kata-test-pattern pattern_name              # Test all in pattern
    just kata-test-all                               # Test everything

From pattern directory:
    just test                                        # Run all tests
    just test-one TestKata1FunctionName              # Run specific kata class
    just test-examples                               # Run LeetCode examples only

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
    # TODO: Import your kata functions here
    # Example:
    # function_name_1,
    # function_name_2,
    # function_name_3,
)


# ============================================================================
# KATA 1: [Function Name] ([LeetCode #XXX if applicable])
# Target: < X min, zero bugs, O(?) time, O(?) space
# ============================================================================

class TestKata1FunctionName:
    """Tests for function_name_1 kata"""

    # LeetCode canonical examples (if from LeetCode)
    LEETCODE_EXAMPLES = [
        # (input1, input2, expected, "description"),
        # Example:
        # ([2, 7, 11, 15], 9, [0, 1], "example 1: basic case"),
        # ([2, 3, 4], 6, [0, 2], "example 2: pair in middle"),
    ]

    # Edge cases for robustness
    EDGE_CASES = [
        # (input1, input2, expected, "description"),
        # Example:
        # ([], 5, [], "empty input"),
        # ([1, 2], 10, [], "no solution"),
    ]

    @kata_todo()  # Remove when implemented
    @pytest.mark.kata1
    @pytest.mark.parametrize("input1,input2,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, input1, input2, expected, desc):
        """LeetCode canonical examples."""
        # TODO: Adjust parameters based on function signature
        assert function_name_1(input1, input2) == expected

    @kata_todo()  # Remove when implemented
    @pytest.mark.kata1
    @pytest.mark.parametrize("input1,input2,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, input1, input2, expected, desc):
        """Edge cases for robustness."""
        # TODO: Adjust parameters based on function signature
        assert function_name_1(input1, input2) == expected


# ============================================================================
# KATA 2: [Function Name] ([LeetCode #XXX if applicable])
# Target: < X min, zero bugs, O(?) time, O(?) space
# ============================================================================

class TestKata2FunctionName:
    """Tests for function_name_2 kata"""

    # Combine all test cases (examples + edges) if it's simpler
    ALL_CASES = [
        # (input, expected, "description"),
        # Example:
        # (121, True, "example 1: basic palindrome"),
        # (-121, False, "example 2: negative number"),
        # (0, True, "edge: zero"),
    ]

    @kata_todo()  # Remove when implemented
    @pytest.mark.kata2
    @pytest.mark.parametrize("input_val,expected,desc",
                             ALL_CASES,
                             ids=[t[2] for t in ALL_CASES])
    def test_all_cases(self, input_val, expected, desc):
        """All test cases for function_name_2."""
        # TODO: Adjust parameters based on function signature
        assert function_name_2(input_val) == expected


# ============================================================================
# KATA 3: [Function Name] - ADVANCED (if applicable)
# Target: < X min, zero bugs, O(?) time, O(?) space
# ============================================================================

class TestKata3FunctionName:
    """Tests for function_name_3 kata (advanced)"""

    ALL_CASES = [
        # (input, expected, "description"),
    ]

    @kata_todo()  # Remove when implemented
    @pytest.mark.kata3  # Advanced kata marker
    @pytest.mark.parametrize("input_val,expected,desc",
                             ALL_CASES,
                             ids=[t[2] for t in ALL_CASES])
    def test_all_cases(self, input_val, expected, desc):
        """All test cases for function_name_3."""
        # TODO: Adjust parameters based on function signature
        assert function_name_3(input_val) == expected


# ============================================================================
# SPECIAL CASES: In-Place Modification Functions
# ============================================================================

"""
For functions that modify in-place (like reverse_string):

class TestKata3ReverseString:
    LEETCODE_EXAMPLES = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"], "example 1"),
    ]

    @pytest.mark.kata3
    @pytest.mark.parametrize("input_list,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, input_list, expected, desc):
        # Make a copy since function modifies in-place
        s = input_list.copy()
        reverse_string(s)
        assert s == expected
"""


# ============================================================================
# MIGRATION GUIDE: Convert Doctest to Pytest
# ============================================================================

"""
1. EXTRACT TEST DATA from kata.py docstrings:

   From kata.py:
       >>> two_sum_sorted([2, 7, 11, 15], 9)
       [0, 1]

   To test_kata.py:
       LEETCODE_EXAMPLES = [
           ([2, 7, 11, 15], 9, [0, 1], "example 1: basic case"),
       ]

2. USE CLASS-BASED ORGANIZATION:
   - One class per kata function
   - TestKata1, TestKata2, TestKata3, etc.
   - Clear visual boundaries in file

3. USE PARAMETRIZE FOR MULTIPLE CASES:
   - Store test data in class constants (LEETCODE_EXAMPLES, EDGE_CASES, ALL_CASES)
   - Use @pytest.mark.parametrize to run multiple test cases
   - Provide descriptive IDs for each test case

4. MARK DIFFICULTY LEVELS:
   - @pytest.mark.kata1 for basic/fundamental katas
   - @pytest.mark.kata2 for medium complexity
   - @pytest.mark.kata3 for advanced/hard katas

5. MARK IMPLEMENTATION STATUS:
   - Add @kata_todo() when not yet implemented
   - Remove decorator after implementing
   - Tests show as 's' (skipped) when TODO

6. HANDLE IN-PLACE MODIFICATIONS:
   - Always copy input before passing to function
   - Use input_list.copy() for lists
   - Assert on the modified copy

7. RUNNING TESTS:
   - `just test-one TestKata1TwoSum` - Run specific kata class
   - `pytest -m kata1` - Run all kata1-level problems
   - `pytest -k leetcode_examples` - Run only LeetCode examples

COMPLETE EXAMPLE:

From kata.py:
    def two_sum_sorted(nums: list[int], target: int) -> list[int]:
        '''
        Example:
            two_sum_sorted([2, 7, 11, 15], 9) → [0, 1]
        '''
        pass

To test_kata.py:
    class TestKata1TwoSum:
        LEETCODE_EXAMPLES = [
            ([2, 7, 11, 15], 9, [0, 1], "example 1"),
            ([2, 3, 4], 6, [0, 2], "example 2"),
        ]

        EDGE_CASES = [
            ([], 5, [], "empty array"),
            ([1, 2, 3], 10, [], "no solution"),
        ]

        @kata_todo()  # Remove when implemented
        @pytest.mark.kata1
        @pytest.mark.parametrize("nums,target,expected,desc",
                                 LEETCODE_EXAMPLES,
                                 ids=[t[3] for t in LEETCODE_EXAMPLES])
        def test_leetcode_examples(self, nums, target, expected, desc):
            assert two_sum_sorted(nums, target) == expected

        @kata_todo()
        @pytest.mark.kata1
        @pytest.mark.parametrize("nums,target,expected,desc",
                                 EDGE_CASES,
                                 ids=[t[3] for t in EDGE_CASES])
        def test_edge_cases(self, nums, target, expected, desc):
            assert two_sum_sorted(nums, target) == expected
"""
