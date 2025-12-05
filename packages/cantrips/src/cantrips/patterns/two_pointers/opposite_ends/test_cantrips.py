"""
Tests for Opposite Ends Two Pointers cantrips.

Run tests:
    pytest test_cantrips.py                    # All tests
    pytest test_cantrips.py -m cantrip1        # Just cantrip 1
    pytest test_cantrips.py -k "examples"      # Just examples
"""

import pytest

from p001_two_sum_sorted import two_sum_sorted
from p002_is_palindrome import is_palindrome
from p003_reverse_string import reverse_string
from p004_three_sum import three_sum
from p005_container_water import max_area


class TestCantrip1:
    """Tests for two_sum_sorted (LeetCode #167)."""

    EXAMPLES = [
        ([2, 7, 11, 15], 9, [1, 2], "standard case"),
        ([2, 3, 4], 6, [1, 3], "answer at ends"),
        ([-1, 0], -1, [1, 2], "negative numbers"),
    ]

    EDGE_CASES = [
        ([1, 2, 3, 4, 5], 9, [4, 5], "answer at right end"),
        ([1, 2, 3, 4, 5], 3, [1, 2], "answer at left end"),
        ([0, 0, 3, 4], 0, [1, 2], "zeros"),
    ]

    @pytest.mark.cantrip1
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "nums,target,expected,desc", EXAMPLES, ids=[t[3] for t in EXAMPLES]
    )
    def test_examples(self, nums, target, expected, desc):
        assert two_sum_sorted(nums, target) == expected

    @pytest.mark.cantrip1
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "nums,target,expected,desc", EDGE_CASES, ids=[t[3] for t in EDGE_CASES]
    )
    def test_edge_cases(self, nums, target, expected, desc):
        assert two_sum_sorted(nums, target) == expected


class TestCantrip2:
    """Tests for is_palindrome (LeetCode #125)."""

    EXAMPLES = [
        ("A man, a plan, a canal: Panama", True, "with punctuation"),
        ("race a car", False, "not palindrome"),
        (" ", True, "single space"),
    ]

    EDGE_CASES = [
        ("", True, "empty string"),
        ("a", True, "single char"),
        (".,", True, "only punctuation"),
        ("Aa", True, "case insensitive"),
    ]

    @pytest.mark.cantrip2
    @pytest.mark.examples
    @pytest.mark.parametrize("s,expected,desc", EXAMPLES, ids=[t[2] for t in EXAMPLES])
    def test_examples(self, s, expected, desc):
        assert is_palindrome(s) == expected

    @pytest.mark.cantrip2
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "s,expected,desc", EDGE_CASES, ids=[t[2] for t in EDGE_CASES]
    )
    def test_edge_cases(self, s, expected, desc):
        assert is_palindrome(s) == expected


class TestCantrip3:
    """Tests for reverse_string (LeetCode #344)."""

    @pytest.mark.cantrip3
    @pytest.mark.examples
    def test_hello(self):
        s = ["h", "e", "l", "l", "o"]
        reverse_string(s)
        assert s == ["o", "l", "l", "e", "h"]

    @pytest.mark.cantrip3
    @pytest.mark.examples
    def test_hannah(self):
        s = ["H", "a", "n", "n", "a", "h"]
        reverse_string(s)
        assert s == ["h", "a", "n", "n", "a", "H"]

    @pytest.mark.cantrip3
    @pytest.mark.edge
    def test_empty(self):
        s = []
        reverse_string(s)
        assert s == []

    @pytest.mark.cantrip3
    @pytest.mark.edge
    def test_single(self):
        s = ["a"]
        reverse_string(s)
        assert s == ["a"]


class TestCantrip4:
    """Tests for three_sum (LeetCode #15)."""

    @pytest.mark.cantrip4
    @pytest.mark.examples
    def test_example_1(self):
        result = three_sum([-1, 0, 1, 2, -1, -4])
        # Sort for comparison
        result = sorted([sorted(t) for t in result])
        expected = sorted([sorted(t) for t in [[-1, -1, 2], [-1, 0, 1]]])
        assert result == expected

    @pytest.mark.cantrip4
    @pytest.mark.examples
    def test_no_triplets(self):
        assert three_sum([0, 1, 1]) == []

    @pytest.mark.cantrip4
    @pytest.mark.examples
    def test_zeros(self):
        assert three_sum([0, 0, 0]) == [[0, 0, 0]]

    @pytest.mark.cantrip4
    @pytest.mark.edge
    def test_empty(self):
        assert three_sum([]) == []

    @pytest.mark.cantrip4
    @pytest.mark.edge
    def test_two_elements(self):
        assert three_sum([0, 0]) == []


class TestCantrip5:
    """Tests for max_area (LeetCode #11)."""

    EXAMPLES = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, "standard case"),
        ([1, 1], 1, "two elements"),
    ]

    EDGE_CASES = [
        ([4, 3, 2, 1, 4], 16, "symmetric"),
        ([1, 2, 1], 2, "three elements"),
        ([2, 3, 4, 5, 18, 17, 6], 17, "tall at end"),
    ]

    @pytest.mark.cantrip5
    @pytest.mark.examples
    @pytest.mark.parametrize(
        "height,expected,desc", EXAMPLES, ids=[t[2] for t in EXAMPLES]
    )
    def test_examples(self, height, expected, desc):
        assert max_area(height) == expected

    @pytest.mark.cantrip5
    @pytest.mark.edge
    @pytest.mark.parametrize(
        "height,expected,desc", EDGE_CASES, ids=[t[2] for t in EDGE_CASES]
    )
    def test_edge_cases(self, height, expected, desc):
        assert max_area(height) == expected
