"""
🥋 STACK MATCHING - KATA PRACTICE

Master stack-based matching through deliberate practice.

RULES:
1. Code from memory - NO looking at reference!
2. Set timer for each kata
3. Run tests after coding
4. If bugs: understand why, redo tomorrow
5. If perfect: celebrate, repeat until automatic

PROGRESSION:
- Week 1: Code with reference, understand
- Week 2: Code from memory, small bugs OK
- Week 3: Code perfectly in under target time
- Week 4+: Breathing knowledge - teach someone else

PATTERN RECOGNITION:
Use stack matching when:
- ✓ Need to match pairs (parentheses, brackets, braces, tags)
- ✓ Balanced expressions or nested structures
- ✓ "Valid" or "balanced" in problem description
- ✓ Most recent opening must match next closing (LIFO behavior)

TECHNIQUE:
1. Use stack to track opening symbols
2. Hash map for closing → opening lookup (O(1))
3. When closing symbol: check if stack top matches
4. End: stack should be empty for valid expression
"""

"""
# Matching Pattern Core Intuition:

Stack LIFO behavior naturally matches nested structures.
Most recent unmatched opening bracket must match the next closing bracket.

Example: "({[]})"
- Push '(' → stack: ['(']
- Push '{' → stack: ['(', '{']
- Push '[' → stack: ['(', '{', '[']
- See ']', matches '[', pop → stack: ['(', '{']
- See '}', matches '{', pop → stack: ['(']
- See ')', matches '(', pop → stack: []
Valid! (empty stack)

Key Insight: Stack tracks "most recent unmatched opening"
"""

# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY (Learn pattern application):
- LC #20: Valid Parentheses → cantrips/stacks_queues/valid_parentheses.py
- LC #1021: Remove Outermost Parentheses
- LC #1544: Make The String Great

MEDIUM (Pattern combinations):
- LC #921: Minimum Add to Make Parentheses Valid
- LC #1249: Minimum Remove to Make Valid Parentheses
- LC #1541: Minimum Insertions to Balance a Parentheses String

HARD (Advanced variations):
- LC #32: Longest Valid Parentheses (stack stores indices)
- LC #301: Remove Invalid Parentheses (BFS/DFS variation)

PROGRESSION PATH:
1. Master katas 1-2 (is_valid, remove_outer_parentheses)
2. Solve Easy cantrips (build pattern recognition)
3. Master katas 3-4 (min_add_to_make_valid, min_remove_to_make_valid)
4. Tackle Medium cantrips (apply counting and modification patterns)
5. Challenge yourself with kata 5 (longest_valid_parentheses) and Hard cantrips
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1-2:
[ ] Can code katas 1-2 with reference template open
[ ] Understand stack LIFO matching
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 2-3:
[ ] Can code katas 1-2 from memory
[ ] < 5 bugs per week across all katas
[ ] Average time under 2× target time
→ READY FOR: Easy cantrips (LC #20, #1021)

LEVEL 3 (Proficient) - Week 3-4:
[ ] Zero bugs on katas 1-2 for a week
[ ] Consistently under target time
[ ] Can explain while coding
→ READY FOR: Medium cantrips (LC #921, #1249)

LEVEL 4 (Mastered) - Week 4-6:
[ ] 10+ perfect reps on each kata
[ ] Under 80% of target time
[ ] Can code katas 3-5 from memory
[ ] Used successfully in 5+ cantrips
→ READY FOR: Hard cantrips and teaching others

LEVEL 5 (Breathing Knowledge) - Week 6+:
[ ] Pattern recognition is automatic (< 10 sec in new problems)
[ ] Can code all 5 katas in under 22 minutes
[ ] Can teach this pattern to someone else
[ ] Fingers start typing before conscious thought
→ INTERVIEW READY: This pattern is now a superpower

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on katas 1-2 → Start Easy cantrips
- Reach Level 3 (Proficient) → Start Medium cantrips
- If you struggle on a cantrip → Return to katas for more reps
"""


def is_valid(s: str) -> bool:
    """
    KATA 1: Valid Parentheses (LeetCode #20)

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Given a string containing just '(', ')', '{', '}', '[', ']',
    determine if the input string is valid.

    Valid means:
    - Open brackets closed by same type
    - Open brackets closed in correct order
    - Every closing bracket has matching opening bracket

    Edge cases:
    - Empty string (valid)
    - Single character (invalid)
    - All opening or all closing (invalid)
    - Interleaved but not nested properly: "([)]" (invalid)

    Hint if stuck:
    - Use stack to track opening brackets
    - Hash map: closing → opening for quick lookup
    - Check stack non-empty before pop!

    Examples:
        >>> is_valid("()")
        True
        >>> is_valid("()[]{}")
        True
        >>> is_valid("(]")
        False
        >>> is_valid("([)]")
        False

    START CODING BELOW (delete 'pass' and write your solution):
    """
    stack = []
    close_to_open = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in close_to_open:
            # We have a closing symbol
            if stack and stack[-1] == close_to_open[char]:
                # the stack is nonempty and the top of the stack has the matching opening symbol
                stack.pop()
            else:
                # symbols do not match
                return False
        else:
            stack.append(char)

    return True if not stack else False
            


def remove_outer_parentheses(s: str) -> str:
    """
    KATA 2: Remove Outermost Parentheses (LeetCode #1021)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    A valid parentheses string is either empty, "(V)", or "VW"
    where V and W are valid strings. A string is primitive if
    it's non-empty and can't be split into "VW".

    Remove the outermost parentheses of every primitive string
    in the decomposition of s.

    Edge cases:
    - Single primitive: "(())" → "()"
    - Multiple primitives: "()()" → ""
    - Nested: "((()))" → "(())"

    Hint if stuck:
    - Track depth/balance counter
    - When depth becomes 0, you've completed a primitive
    - Only add to result when depth > 1 (not outermost)
    - Don't need a stack, just a counter!

    Examples:
        >>> remove_outer_parentheses("(()())(())")
        "()()()"
        >>> remove_outer_parentheses("(()())(())(()(()))")
        "()()()()(())"
        >>> remove_outer_parentheses("()()")
        ""

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def min_add_to_make_valid(s: str) -> int:
    """
    KATA 3: Minimum Add to Make Parentheses Valid (LeetCode #921)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Return the minimum number of parentheses we must add to make
    the resulting string valid.

    A string is valid if:
    - Every '(' has matching ')'
    - Every ')' has matching '('

    Edge cases:
    - Already valid: "()" → 0
    - All opening: "(((" → 3
    - All closing: ")))" → 3
    - Mixed: "())" → 1, "(((" → 3

    Hint if stuck:
    - Track TWO counters: unmatched '(' and unmatched ')'
    - When '(': increment open counter
    - When ')': if open > 0, decrement open; else increment close
    - Return open + close
    - No stack needed, just counting!

    Examples:
        >>> min_add_to_make_valid("())")
        1
        >>> min_add_to_make_valid("(((")
        3
        >>> min_add_to_make_valid("()))(")
        2

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def min_remove_to_make_valid(s: str) -> str:
    """
    KATA 4: Minimum Remove to Make Valid Parentheses (LeetCode #1249)

    ⏱️  Target time: < 6 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Remove the minimum number of parentheses so that the resulting
    string is valid. Return any valid result.

    Edge cases:
    - Already valid: "a(b)c" → "a(b)c"
    - Extra closing: "a)b(c" → "ab(c" or "ab(c"
    - Extra opening: "a(b(c" → "a(bc" or "abc" or "abc"
    - Multiple solutions possible

    Hint if stuck:
    - Use stack to track indices of unmatched '(' parentheses
    - Track set of indices to remove
    - First pass: find all invalid ')' and unmatched '('
    - Second pass: build result skipping invalid indices
    - OR: Two-pass approach without stack

    Examples:
        >>> min_remove_to_make_valid("lee(t(c)o)de)")
        "lee(t(c)o)de"
        >>> min_remove_to_make_valid("a)b(c)d")
        "ab(c)d"
        >>> min_remove_to_make_valid("))((")
        ""

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def longest_valid_parentheses(s: str) -> int:
    """
    KATA 5: Longest Valid Parentheses (LeetCode #32) [HARD]

    ⏱️  Target time: < 9 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Given a string containing just '(' and ')', find the length
    of the longest valid (well-formed) parentheses substring.

    Edge cases:
    - Empty string → 0
    - All valid: "()" → 2, "(())" → 4
    - Partial valid: "(()" → 2
    - Multiple segments: "()(()" → 2

    Hint if stuck:
    - Stack stores INDICES, not characters!
    - Initialize stack with -1 (base for length calculation)
    - When '(': push index
    - When ')': pop, then calculate length
    - If stack empty after pop: push current index (new base)
    - Track max length seen

    Alternative: Two-pass approach (left-to-right, right-to-left)

    Examples:
        >>> longest_valid_parentheses("(()")
        2
        >>> longest_valid_parentheses(")()())")
        4
        >>> longest_valid_parentheses("")
        0
        >>> longest_valid_parentheses("()(()")
        2

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
Track your practice sessions below. Be honest about bugs!

Date       | Kata | Time  | Bugs | Notes
-----------|------|-------|------|---------------------------------------
2025-12-02 | 1    | 2:56  | 0    | 
YYYY-MM-DD | 1    | MM:SS | N    | Description of any issues or insights
YYYY-MM-DD | 2    | MM:SS | N    | ...

MASTERY CHECKLIST:
For each kata, check off when you achieve:
[ ] Code from memory without hints
[ ] Zero bugs on first run
[ ] Under target time
[ ] Can explain trade-offs
[ ] Automatic pattern recognition
"""


# ============================================================================
# TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("STACK MATCHING - KATA PRACTICE")
    print("=" * 60)
    print()
    print("🥋 Run tests with pytest:")
    print()
    print("   pytest test_kata.py                  # Run all tests")
    print("   pytest test_kata.py -m kata1         # Run kata 1 only")
    print("   pytest test_kata.py -m kata2         # Run kata 2 only")
    print("   pytest test_kata.py -v               # Verbose output")
    print()
    print("Or use justfile commands:")
    print()
    print("   just kata::test stack/matching")
    print("   just kata::practice stack/matching")
    print()
    print("🎯 KATA MASTERY TIPS:")
    print("   - Code from memory, no peeking!")
    print("   - Time yourself")
    print("   - Aim for zero bugs")
    print("   - Practice daily until automatic")
    print()
    print("=" * 60)
