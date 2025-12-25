"""
Pytest tests for Stack Expression Evaluation cantrips.

Quick Reference:
    pytest test_cantrips.py                # Run all
    pytest test_cantrips.py::TestEvalRPN   # Run specific
    pytest -m cantrip1                     # Run by marker
"""

import pytest
from hypothesis import given, strategies as st

from .p001_eval_rpn import eval_rpn
from .p002_build_array import build_array
from .p003_calculator import calculate
from .p004_calculator_ii import calculate_ii
from .p005_calculator_iii import calculate_iii


class TestEvaluateRPN:
    """Tests for Evaluate RPN cantrip."""

    LEETCODE_EXAMPLES = [
        (["2", "1", "+", "3", "*"], 9, "example 1: (2+1)*3"),
        (["4", "13", "5", "/", "+"], 6, "example 2: 4+(13/5)"),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22, "example 3: complex"),
    ]

    EDGE_CASES = [
        (["3"], 3, "edge: single number"),
        (["2", "1", "+"], 3, "edge: simple addition"),
        (["2", "1", "-"], 1, "edge: simple subtraction"),
        (["2", "3", "*"], 6, "edge: simple multiplication"),
        (["6", "3", "/"], 2, "edge: simple division"),
        (["6", "-3", "/"], -2, "edge: division truncates toward zero"),
        (["-1", "-2", "+"], -3, "edge: negative numbers"),
    ]

    @pytest.mark.cantrip1
    @pytest.mark.parametrize("tokens,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, tokens, expected, desc):
        """LeetCode canonical examples."""
        assert eval_rpn(tokens) == expected

    @pytest.mark.cantrip1
    @pytest.mark.parametrize("tokens,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, tokens, expected, desc):
        """Edge cases."""
        assert eval_rpn(tokens) == expected


class TestEvaluateRPNProperties:
    """Property-based tests."""

    @pytest.mark.cantrip1
    @given(st.integers(-100, 100))
    def test_single_number(self, num):
        """Single number returns itself."""
        assert eval_rpn([str(num)]) == num

    @pytest.mark.cantrip1
    @given(st.integers(-50, 50), st.integers(-50, 50))
    def test_simple_addition(self, a, b):
        """Simple addition works correctly."""
        tokens = [str(a), str(b), "+"]
        assert eval_rpn(tokens) == a + b

    @pytest.mark.cantrip1
    @given(st.integers(-50, 50), st.integers(-50, 50))
    def test_simple_multiplication(self, a, b):
        """Simple multiplication works correctly."""
        tokens = [str(a), str(b), "*"]
        assert eval_rpn(tokens) == a * b


class TestBuildArray:
    """Tests for Build Array With Stack Operations cantrip."""

    LEETCODE_EXAMPLES = [
        ([1, 3], 3, ["Push", "Push", "Pop", "Push"], "example 1: skip 2"),
        ([1, 2, 3], 3, ["Push", "Push", "Push"], "example 2: all consecutive"),
        ([1, 2], 4, ["Push", "Push"], "example 3: early stop"),
    ]

    EDGE_CASES = [
        ([1], 1, ["Push"], "edge: single element"),
        ([2], 2, ["Push", "Pop", "Push"], "edge: skip first"),
        ([1, 2, 3, 4, 5], 5, ["Push", "Push", "Push", "Push", "Push"], "edge: all elements"),
        ([2, 3, 4], 4, ["Push", "Pop", "Push", "Push", "Push"], "edge: start from 2"),
        ([3], 5, ["Push", "Pop", "Push", "Pop", "Push"], "edge: skip to 3"),
    ]

    @pytest.mark.cantrip2
    @pytest.mark.parametrize("target,n,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[3] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, target, n, expected, desc):
        """LeetCode canonical examples."""
        assert build_array(target, n) == expected

    @pytest.mark.cantrip2
    @pytest.mark.parametrize("target,n,expected,desc",
                             EDGE_CASES,
                             ids=[t[3] for t in EDGE_CASES])
    def test_edge_cases(self, target, n, expected, desc):
        """Edge cases."""
        assert build_array(target, n) == expected


class TestCalculator:
    """Tests for Basic Calculator cantrip."""

    LEETCODE_EXAMPLES = [
        ("1 + 1", 2, "example 1: simple addition"),
        (" 2-1 + 2 ", 3, "example 2: mixed with spaces"),
        ("(1+(4+5+2)-3)+(6+8)", 23, "example 3: nested parens"),
    ]

    EDGE_CASES = [
        ("1", 1, "edge: single number"),
        ("-2 + 1", -1, "edge: leading negative"),
        ("2-(3+4)", -5, "edge: paren with subtraction"),
        ("2-(-3)", 5, "edge: double negative"),
        ("1-(2+3-(4+5))", 5, "edge: deeply nested"),
        (" 3 ", 3, "edge: number with spaces"),
    ]

    @pytest.mark.cantrip3
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert calculate(s) == expected

    @pytest.mark.cantrip3
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert calculate(s) == expected


class TestCalculatorII:
    """Tests for Basic Calculator II cantrip."""

    LEETCODE_EXAMPLES = [
        ("3+2*2", 7, "example 1: precedence"),
        (" 3/2 ", 1, "example 2: division truncates"),
        (" 3+5 / 2 ", 5, "example 3: mixed"),
    ]

    EDGE_CASES = [
        ("42", 42, "edge: single number"),
        ("1+1+1", 3, "edge: all addition"),
        ("1-1-1", -1, "edge: all subtraction"),
        ("2*3*4", 24, "edge: all multiplication"),
        ("12/3/2", 2, "edge: all division"),
        ("1+2*3-4/2", 5, "edge: all operators"),
        ("14/3", 4, "edge: truncate toward zero"),
        ("0-2", -2, "edge: negative result"),
    ]

    @pytest.mark.cantrip4
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert calculate_ii(s) == expected

    @pytest.mark.cantrip4
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert calculate_ii(s) == expected


class TestCalculatorIII:
    """Tests for Basic Calculator III cantrip."""

    LEETCODE_EXAMPLES = [
        ("2*(5+5*2)/3+(6/2+8)", 21, "example 1: full expression"),
        ("(2+6*3+5-(3*14/7+2)*5)+3", -12, "example 2: complex nested"),
        ("1+2*3", 7, "example 3: simple precedence"),
    ]

    EDGE_CASES = [
        ("42", 42, "edge: single number"),
        ("(1+2)*3", 9, "edge: parens first"),
        ("2*(3+4)", 14, "edge: multiply paren"),
        ("(1+2)*(3+4)", 21, "edge: two parens"),
        ("((1+2))", 3, "edge: double parens"),
        ("1+(2*3)", 7, "edge: paren in middle"),
        ("2*3+4*5", 26, "edge: two multiplications"),
    ]

    @pytest.mark.cantrip5
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert calculate_iii(s) == expected

    @pytest.mark.cantrip5
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert calculate_iii(s) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
