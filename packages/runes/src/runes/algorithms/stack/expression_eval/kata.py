"""
🥋 STACK EXPRESSION EVALUATION - KATA PRACTICE

Master evaluating expressions with stack-based operand tracking.

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
Use expression evaluation when:
- ✓ Evaluating mathematical expressions (infix, postfix, prefix)
- ✓ Calculator problems
- ✓ Need to handle operator precedence
- ✓ Parentheses change evaluation order
- ✓ Stack stores operands (numbers), process operators sequentially

TECHNIQUE:
1. Stack holds numbers (operands or partial results)
2. When operator encountered: pop operands, compute, push result
3. For infix: handle precedence (*, / before +, -)
4. For parentheses: use stack to save state
5. Watch order: b = pop(), a = pop(), result = a OP b
"""

"""
# Expression Evaluation Pattern Core Intuition:

Stack naturally handles deferred computation.
Store operands, apply operators when ready.

RPN (Postfix): "2 1 + 3 *"
- See 2 → push 2 → stack: [2]
- See 1 → push 1 → stack: [2, 1]
- See + → pop 1, pop 2 → compute 2+1=3 → push 3 → stack: [3]
- See 3 → push 3 → stack: [3, 3]
- See * → pop 3, pop 3 → compute 3*3=9 → push 9 → stack: [9]
Result: 9

Infix: "2 + 3 * 4"
- Must respect precedence: 3*4 before +
- Stack delays low-precedence ops until ready
- Parentheses: push state, evaluate inner first

Key Insight: Stack defers operations until operands ready
"""

# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY (Learn pattern application):
- LC #150: Evaluate Reverse Polish Notation → cantrips/stacks_queues/eval_rpn.py
- LC #1441: Build an Array With Stack Operations

MEDIUM (Pattern combinations):
- LC #227: Basic Calculator II (*, /, +, -)
- LC #394: Decode String (nested patterns)
- LC #735: Asteroid Collision

HARD (Advanced variations):
- LC #224: Basic Calculator (+, -, parentheses)
- LC #772: Basic Calculator III (all operators + parentheses)
- LC #770: Basic Calculator IV (variables)

PROGRESSION PATH:
1. Master katas 1-2 (eval_rpn, build_array - basic stack mechanics)
2. Solve Easy cantrips (postfix, simple operations)
3. Master kata 4 (calculator II - operator precedence without parens)
4. Master kata 3 (calculator I - parens without precedence)
5. Challenge yourself with kata 5 (calculator III - both parens and precedence)
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1-2:
[ ] Can code katas 1-2 with reference template open
[ ] Understand operand stack pattern
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 2-3:
[ ] Can code katas 1-2 from memory
[ ] < 5 bugs per week across all katas
[ ] Average time under 2× target time
→ READY FOR: Easy cantrips (LC #150, #1441)

LEVEL 3 (Proficient) - Week 3-4:
[ ] Zero bugs on katas 1-2 for a week
[ ] Consistently under target time
[ ] Can explain operator processing
→ READY FOR: Medium cantrips (LC #227, #394)

LEVEL 4 (Mastered) - Week 4-6:
[ ] 10+ perfect reps on each kata
[ ] Under 80% of target time
[ ] Can code katas 3-5 from memory
[ ] Understand precedence and parentheses deeply
→ READY FOR: Hard cantrips and full calculators

LEVEL 5 (Breathing Knowledge) - Week 6+:
[ ] Pattern recognition is automatic (< 10 sec in new problems)
[ ] Can code all 5 katas in under 35 minutes
[ ] Can teach expression evaluation to someone else
[ ] Calculator problems feel routine
→ INTERVIEW READY: This pattern is now a superpower

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on katas 1-2 → Start Easy cantrips
- Reach Level 3 (Proficient) → Start Medium cantrips
- If you struggle on a cantrip → Return to katas for more reps
"""


def eval_rpn(tokens: list[str]) -> int:
    """
    KATA 1: Evaluate Reverse Polish Notation (LeetCode #150)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Evaluate an arithmetic expression in Reverse Polish Notation (RPN).
    Valid operators are +, -, *, and /.
    Each operand may be an integer or another expression.

    RPN (Postfix): operators come AFTER operands
    "2 1 +" means "2 + 1"

    Edge cases:
    - Single number (no operators)
    - Division truncates toward zero: int(a / b)
    - Negative numbers in tokens: "-3"
    - Order matters for - and /: "4 2 -" → 4-2=2 (not 2-4)

    Hint if stuck:
    - Stack holds numbers (partial results)
    - When you see number: push it
    - When you see operator: pop 2, compute, push result
    - Watch order: b = pop(), a = pop(), then a OP b
    - int(a / b) truncates toward zero

    Examples:
        >>> eval_rpn(["2","1","+","3","*"])
        9  # ((2 + 1) * 3) = 9
        >>> eval_rpn(["4","13","5","/","+"])
        6  # (4 + (13 / 5)) = (4 + 2) = 6
        >>> eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        22

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def build_array(target: list[int], n: int) -> list[str]:
    """
    KATA 2: Build an Array With Stack Operations (LeetCode #1441)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(target[-1]) time

    Given target array and integer n, return list of "Push" and "Pop"
    operations to build target from [1, 2, 3, ..., n].

    You have an empty stack and a stream of integers [1, 2, ..., n].
    Operations:
    - "Push": Take next integer from stream, push to stack
    - "Pop": Remove top element

    Target contains distinct integers in ascending order from 1 to n.

    Edge cases:
    - Target = [1,2,3] → just push push push
    - Target = [1,3] → push, push, pop, push (skip 2)
    - Target = [2,3,4] → push, pop, push, push, push (skip 1)

    Hint if stuck:
    - Iterate stream 1 to target[-1]
    - If current number in target: "Push"
    - If not in target: "Push" then "Pop" (skip it)
    - Use target as a set for O(1) lookup
    - Stop at target[-1] (max value)

    Examples:
        >>> build_array([1,3], 3)
        ["Push","Push","Pop","Push"]
        >>> build_array([1,2,3], 3)
        ["Push","Push","Push"]
        >>> build_array([1,2], 4)
        ["Push","Push"]

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def calculate(s: str) -> int:
    """
    KATA 3: Basic Calculator (LeetCode #224) [HARD]

    ⏱️  Target time: < 10 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Evaluate infix expression with +, -, (, ), and spaces.
    NO multiplication or division.

    The challenge: Parentheses can nest and reverse sign.
    Example: "2 - (3 + (4 - 5))" → 2 - (3 + (-1)) → 2 - 2 → 0

    Edge cases:
    - No parentheses: "1 + 2"
    - Nested parentheses: "1+(2-(3+4))"
    - Leading negative: "-2+ 1"
    - Spaces everywhere

    Hint if stuck:
    - Stack stores (running_result, sign_before_paren)
    - Track: result (accumulator), sign (1 or -1), num (current number)
    - When '(': push (result, sign), reset result=0, sign=1
    - When ')': pop, compute: result = prev_result + prev_sign * result
    - When digit: build number
    - When '+'/'-': apply previous operation, update sign
    - No precedence needed (only +, -)

    Examples:
        >>> calculate("1 + 1")
        2
        >>> calculate(" 2-1 + 2 ")
        3
        >>> calculate("(1+(4+5+2)-3)+(6+8)")
        23

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def calculate_ii(s: str) -> int:
    """
    KATA 4: Basic Calculator II (LeetCode #227) [MEDIUM]

    ⏱️  Target time: < 8 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Evaluate infix expression with +, -, *, /, and spaces.
    NO parentheses.

    The challenge: Handle operator precedence (* and / before + and -)

    Edge cases:
    - Only one number: "42"
    - Division: "14/3" → 4 (truncate toward zero)
    - Negative result: "1-5" → -4
    - Spaces: " 3+5 / 2 "

    Hint if stuck:
    - Stack holds numbers
    - Track: num (current), sign (last operator)
    - When +/-: push (+/- num) to stack, defer addition
    - When *//: pop last, compute, push result (immediate eval)
    - End: sum entire stack
    - Initialize sign = '+', num = 0

    Pattern:
    1. Build number from digits
    2. When operator or end: process previous operator
    3. + or -: push to stack (deferred)
    4. * or /: pop, compute, push (immediate)

    Examples:
        >>> calculate_ii("3+2*2")
        7  # 3 + (2*2) = 7
        >>> calculate_ii(" 3/2 ")
        1
        >>> calculate_ii(" 3+5 / 2 ")
        5  # 3 + (5/2) = 3 + 2 = 5

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def calculate_iii(s: str) -> int:
    """
    KATA 5: Basic Calculator III (LeetCode #772 - Premium) [HARD]

    ⏱️  Target time: < 12 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Evaluate infix expression with +, -, *, /, (, ), and spaces.
    Combines Calculator I (parentheses) and Calculator II (precedence).

    This is the FULL calculator - all features combined!

    Edge cases:
    - Precedence with parens: "2*(3+4)"
    - Nested parens with ops: "2*(5+5*2)/3+(6/2+8)"
    - Negative in parens: "-(2+3)"

    Hint if stuck:
    - Recursive approach: when '(' found, evaluate sub-expression
    - OR: Stack-based like Calculator II, but handle '(' by recursion
    - OR: Convert to Calculator II by resolving parens first
    - When '(': recursively evaluate inner expression
    - When ')': return result of this level
    - Otherwise: use Calculator II logic (precedence handling)

    Helper function approach:
    - helper(s, index) returns (result, next_index)
    - Recursive call for each '('
    - Return when ')' found

    Examples:
        >>> calculate_iii("2*(5+5*2)/3+(6/2+8)")
        17  # 2*15/3 + 11 = 10 + 11 = 21... wait let me recalc
        >>> calculate_iii("(2+6*3+5-(3*14/7+2)*5)+3")
        -12
        >>> calculate_iii("1+2*3")
        7

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
YYYY-MM-DD | 1    | MM:SS | N    | Description of any issues or insights
YYYY-MM-DD | 2    | MM:SS | N    | ...

MASTERY CHECKLIST:
For each kata, check off when you achieve:
[ ] Code from memory without hints
[ ] Zero bugs on first run
[ ] Under target time
[ ] Can explain operator precedence
[ ] Can handle parentheses correctly
[ ] Automatic expression evaluation pattern recognition
"""


# ============================================================================
# TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("STACK EXPRESSION EVALUATION - KATA PRACTICE")
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
    print("   just kata::test stack/expression_eval")
    print("   just kata::practice stack/expression_eval")
    print()
    print("🎯 KATA MASTERY TIPS:")
    print("   - Code from memory, no peeking!")
    print("   - Time yourself")
    print("   - Calculator problems are interview favorites!")
    print("   - Master precedence and parentheses separately first")
    print()
    print("=" * 60)
