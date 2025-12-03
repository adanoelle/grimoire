"""
Pytest tests for Stack Matching kata.

Quick Reference:
    pytest test_kata.py                    # Run all
    pytest test_kata.py::TestValidParens   # Run specific
    pytest -m kata1                        # Run by marker
"""

import pytest
import sys
from pathlib import Path
from hypothesis import given, strategies as st

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from kata import is_valid, remove_duplicates, make_good, min_remove_to_make_valid, longest_valid_parentheses


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


class TestRemoveDuplicates:
    """Tests for Remove All Adjacent Duplicates kata"""

    LEETCODE_EXAMPLES = [
        ("abbaca", "ca", "example 1: chain reaction"),
        ("azxxzy", "ay", "example 2: multiple removals"),
    ]

    EDGE_CASES = [
        ("", "", "edge: empty string"),
        ("a", "a", "edge: single char"),
        ("aa", "", "edge: complete cancellation"),
        ("abcd", "abcd", "edge: no duplicates"),
        ("aabbcc", "", "edge: all pairs cancel"),
        ("abc", "abc", "edge: no adjacent duplicates"),
        ("aabbccdd", "", "edge: multiple pairs all cancel"),
        ("aaaa", "", "edge: all same char"),
        ("ababab", "ababab", "edge: alternating, no adjacent"),
    ]

    @pytest.mark.kata2
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert remove_duplicates(s) == expected

    @pytest.mark.kata2
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert remove_duplicates(s) == expected


class TestRemoveDuplicatesProperties:
    """Property-based tests for Remove All Adjacent Duplicates"""

    @given(st.text(alphabet='ab', min_size=0, max_size=100))
    def test_result_no_adjacent_duplicates(self, s):
        """Result should have no adjacent duplicate characters."""
        result = remove_duplicates(s)
        for i in range(len(result) - 1):
            assert result[i] != result[i + 1], f"Found adjacent duplicates at index {i}"

    @given(st.text(alphabet='abc', min_size=0, max_size=50))
    def test_empty_or_no_dups(self, s):
        """If input has no duplicates, output equals input."""
        has_adjacent_dup = any(s[i] == s[i+1] for i in range(len(s) - 1))
        if not has_adjacent_dup:
            assert remove_duplicates(s) == s


class TestMakeGood:
    """Tests for Make The String Great kata"""

    LEETCODE_EXAMPLES = [
        ("leEeetcode", "leetcode", "example 1: remove Ee"),
        ("abBAcC", "", "example 2: all cancel out"),
        ("s", "s", "example 3: single char"),
    ]

    EDGE_CASES = [
        ("", "", "edge: empty string"),
        ("a", "a", "edge: single lowercase"),
        ("A", "A", "edge: single uppercase"),
        ("aA", "", "edge: simple pair cancels"),
        ("Aa", "", "edge: simple pair cancels (reversed)"),
        ("abc", "abc", "edge: all lowercase, no pairs"),
        ("ABC", "ABC", "edge: all uppercase, no pairs"),
        ("aaBB", "aaBB", "edge: same case duplicates, no bad pairs"),
        ("aAbBcC", "", "edge: all pairs cancel"),
        ("abcCBA", "", "edge: palindrome of cases, chain reaction cancels all"),
        ("abBAcC", "", "edge: chain reaction cancels all"),
        ("aBbCc", "a", "edge: cascading cancellation leaves one"),
        ("xXyYzZ", "", "edge: alternating case all cancel"),
        ("abcDEF", "abcDEF", "edge: no adjacent same letters"),
    ]

    @pytest.mark.kata3
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert make_good(s) == expected

    @pytest.mark.kata3
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert make_good(s) == expected


class TestMakeGoodProperties:
    """Property-based tests for Make The String Great"""

    @given(st.text(alphabet='aAbBcC', min_size=0, max_size=100))
    def test_result_no_bad_pairs(self, s):
        """Result should have no adjacent same-letter different-case pairs."""
        result = make_good(s)
        for i in range(len(result) - 1):
            # Check if adjacent chars are same letter but different case
            if result[i].lower() == result[i + 1].lower():
                # Same letter - they must have same case
                assert result[i] == result[i + 1] or \
                       result[i].islower() == result[i + 1].islower(), \
                       f"Found bad pair at index {i}: '{result[i]}' and '{result[i+1]}'"

    @given(st.text(alphabet='abc', min_size=0, max_size=50))
    def test_all_lowercase_unchanged(self, s):
        """All lowercase strings should be unchanged."""
        assert make_good(s) == s

    @given(st.text(alphabet='ABC', min_size=0, max_size=50))
    def test_all_uppercase_unchanged(self, s):
        """All uppercase strings should be unchanged."""
        assert make_good(s) == s


class TestMinRemoveToMakeValid:
    """Tests for Minimum Remove to Make Valid Parentheses kata"""

    LEETCODE_EXAMPLES = [
        ("lee(t(c)o)de)", "lee(t(c)o)de", "example 1: one extra closing"),
        ("a)b(c)d", "ab(c)d", "example 2: invalid closing at start"),
        ("))((", "", "example 3: all invalid"),
    ]

    EDGE_CASES = [
        ("", "", "edge: empty string"),
        ("(", "", "edge: single opening"),
        (")", "", "edge: single closing"),
        ("()", "()", "edge: already valid pair"),
        ("(()", "()", "edge: one extra opening"),
        ("())", "()", "edge: one extra closing"),
        ("a(b)c", "a(b)c", "edge: already valid with letters"),
        ("(a(b(c)d)e)", "(a(b(c)d)e)", "edge: nested valid"),
        ("(a(b(c", "abc", "edge: cascading unmatched openings"),
        (")a)b)c)", "abc", "edge: all closings invalid"),
        ("())()", "()()", "edge: invalid in middle"),
        ("(a)(b)c)d", "(a)(b)cd", "edge: one extra at end"),
        ("((a)(b", "(a)b", "edge: two extra openings"),
        ("a)b)c(d(e", "abcde", "edge: mixed letters and invalid"),
    ]

    @pytest.mark.kata4
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert min_remove_to_make_valid(s) == expected

    @pytest.mark.kata4
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert min_remove_to_make_valid(s) == expected


class TestMinRemoveProperties:
    """Property-based tests for Minimum Remove to Make Valid Parentheses"""

    @given(st.text(alphabet='()', min_size=0, max_size=100))
    def test_result_is_valid(self, s):
        """Result should always be valid parentheses."""
        result = min_remove_to_make_valid(s)
        # Valid means is_valid returns True
        assert is_valid(result) == True

    @given(st.text(alphabet='()', min_size=0, max_size=50))
    def test_valid_input_unchanged(self, s):
        """If input is already valid, output equals input."""
        if is_valid(s):
            assert min_remove_to_make_valid(s) == s

    @given(st.text(alphabet='abc', min_size=0, max_size=50))
    def test_no_parens_unchanged(self, s):
        """Strings without parentheses should be unchanged."""
        assert min_remove_to_make_valid(s) == s


class TestLongestValidParentheses:
    """Tests for Longest Valid Parentheses kata"""

    LEETCODE_EXAMPLES = [
        ("(()", 2, "example 1: unmatched opening"),
        (")()())", 4, "example 2: middle valid section"),
        ("", 0, "example 3: empty string"),
        ("()(())", 6, "example 4: all valid"),
    ]

    EDGE_CASES = [
        ("(", 0, "edge: single opening"),
        (")", 0, "edge: single closing"),
        ("()", 2, "edge: simple valid pair"),
        ("((", 0, "edge: all opening"),
        ("))", 0, "edge: all closing"),
        ("(())", 4, "edge: nested valid"),
        ("()(()", 2, "edge: first pair valid"),
        ("(()()", 4, "edge: last two pairs valid"),
        ("()()", 4, "edge: two separate pairs"),
        ("()((())", 6, "edge: nested at end"),
        (")()())", 4, "edge: valid in middle"),
        ("(()())", 6, "edge: nested multiple pairs"),
        ("(()()()", 6, "edge: multiple pairs with extra opening"),
        ("()()())", 6, "edge: three pairs with extra closing"),
    ]

    @pytest.mark.kata5
    @pytest.mark.parametrize("s,expected,desc",
                             LEETCODE_EXAMPLES,
                             ids=[t[2] for t in LEETCODE_EXAMPLES])
    def test_leetcode_examples(self, s, expected, desc):
        """LeetCode canonical examples."""
        assert longest_valid_parentheses(s) == expected

    @pytest.mark.kata5
    @pytest.mark.parametrize("s,expected,desc",
                             EDGE_CASES,
                             ids=[t[2] for t in EDGE_CASES])
    def test_edge_cases(self, s, expected, desc):
        """Edge cases."""
        assert longest_valid_parentheses(s) == expected


class TestLongestValidProperties:
    """Property-based tests for Longest Valid Parentheses"""

    @given(st.text(alphabet='()', min_size=0, max_size=100))
    def test_result_is_even(self, s):
        """Valid parentheses substring must have even length."""
        result = longest_valid_parentheses(s)
        assert result % 2 == 0, f"Result {result} is odd"

    @given(st.text(alphabet='()', min_size=0, max_size=100))
    def test_result_not_greater_than_input(self, s):
        """Result cannot be longer than input."""
        result = longest_valid_parentheses(s)
        assert result <= len(s)

    @given(st.text(alphabet='()', min_size=0, max_size=50))
    def test_all_valid_returns_full_length(self, s):
        """If entire string is valid, return full length."""
        if is_valid(s):
            assert longest_valid_parentheses(s) == len(s)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
