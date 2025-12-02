"""
Pytest tests for Stack Matching kata.

Quick Reference:
    pytest test_kata.py                    # Run all
    pytest test_kata.py::TestValidParens   # Run specific
    pytest -m kata1                        # Run by marker
"""

import pytest
from hypothesis import given, strategies as st
from kata import is_valid


class TestValidParentheses:
    """Tests for Valid Parentheses kata"""

    LEETCODE_EXAMPLES = [
        ("()", True, "example 1: simple pair"),
        ("()[]{}", True, "example 2: multiple types"),
        ("(]", False, "example 3: wrong closing"),
        ("([)]", False, "example 4: interleaved"),
        ("{[]}", True, "example 5: properly nested"),
    ]

    EDGE_CASES = [
        ("", True, "edge: empty string"),
        ("(", False, "edge: unclosed opening"),
        (")", False, "edge: closing without opening"),
        ("((", False, "edge: all opening"),
        ("))", False, "edge: all closing"),
        ("(())", True, "edge: nested same type"),
        ("[", False, "edge: single opening"),
        ("]", False, "edge: single closing"),
    ]

    @pytest.mark.kata1
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert is_valid(s) == expected

    @pytest.mark.kata1
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert is_valid(s) == expected


class TestValidParenthesesProperties:
    """Property-based tests"""

    @given(st.text(alphabet='()[]{}', min_size=0, max_size=100))
    def test_odd_length_invalid(self, s):
        """Odd length strings are always invalid."""
        if len(s) % 2 == 1:
            assert is_valid(s) == False

    @given(st.text(alphabet='()[]{}', min_size=0, max_size=100))
    def test_empty_valid(self, s):
        """Empty string is valid."""
        if len(s) == 0:
            assert is_valid(s) == True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
