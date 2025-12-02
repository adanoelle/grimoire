"""
Pytest tests for Stack Expression Evaluation kata.

Quick Reference:
    pytest test_kata.py                # Run all
    pytest test_kata.py::TestEvalRPN   # Run specific
    pytest -m kata3                    # Run by marker
"""

import pytest
import sys
from pathlib import Path
from hypothesis import given, strategies as st

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from kata import eval_rpn


class TestEvaluateRPN:
    """Tests for Evaluate RPN kata"""

    LEETCODE_EXAMPLES = [
        (["2","1","+","3","*"], 9, "example 1: (2+1)*3"),
        (["4","13","5","/","+"], 6, "example 2: 4+(13/5)"),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22, "example 3: complex"),
    ]

    EDGE_CASES = [
        (["3"], 3, "edge: single number"),
        (["2","1","+"], 3, "edge: simple addition"),
        (["2","1","-"], 1, "edge: simple subtraction"),
        (["2","3","*"], 6, "edge: simple multiplication"),
        (["6","3","/"], 2, "edge: simple division"),
        (["6","-3","/"], -2, "edge: division truncates toward zero"),
        (["-1","-2","+"], -3, "edge: negative numbers"),
    ]

    @pytest.mark.kata3
    @pytest.mark.parametrize("tokens,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, tokens, expected, desc):
        """LeetCode canonical examples."""
        assert eval_rpn(tokens) == expected

    @pytest.mark.kata3
    @pytest.mark.parametrize("tokens,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, tokens, expected, desc):
        """Edge cases."""
        assert eval_rpn(tokens) == expected


class TestEvaluateRPNProperties:
    """Property-based tests"""

    @given(st.integers(-100, 100))
    def test_single_number(self, num):
        """Single number returns itself."""
        assert eval_rpn([str(num)]) == num

    @given(st.integers(-50, 50), st.integers(-50, 50))
    def test_simple_addition(self, a, b):
        """Simple addition works correctly."""
        tokens = [str(a), str(b), "+"]
        assert eval_rpn(tokens) == a + b

    @given(st.integers(-50, 50), st.integers(-50, 50))
    def test_simple_multiplication(self, a, b):
        """Simple multiplication works correctly."""
        tokens = [str(a), str(b), "*"]
        assert eval_rpn(tokens) == a * b


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
