"""
Two Pointers (Fast & Slow) - Daily Kata Practice

🥋 Floyd's Cycle Detection Algorithm

Code from memory. Time yourself. Achieve zero bugs.
"""


# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY (Learn pattern application):
- LC #141: Linked List Cycle
- LC #876: Middle of the Linked List
- LC #202: Happy Number
- LC #234: Palindrome Linked List (combines with reversal)

MEDIUM (Pattern core):
- LC #142: Linked List Cycle II (find cycle start)
- LC #143: Reorder List (combines with reversal)
- LC #19: Remove Nth Node From End (use distance between pointers)
- LC #287: Find the Duplicate Number (cycle detection in array!)
- LC #457: Circular Array Loop

HARD (Advanced variations):
- LC #25: Reverse Nodes in k-Group (combines with reversal)
- LC #82: Remove Duplicates from Sorted List II

PROGRESSION PATH:
1. Master katas 1-2 (has_cycle, find_middle)
2. Solve Easy cantrips (LC #141, #876, #202)
3. Master kata 3 (detect_cycle_start - the tricky one!)
4. Tackle Medium cantrips (LC #142, #143, #287)
5. Master kata 4 (is_happy_number - creative application)
6. Challenge yourself with Hard cantrips
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1:
[ ] Can code katas 1-2 with reference template open
[ ] Understand why fast-slow detects cycles
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 1-2:
[ ] Can code katas 1-2 from memory
[ ] < 5 bugs per week across all katas
[ ] Average time under 2× target time
→ READY FOR: Easy cantrips (LC #141, #876, #202)

LEVEL 3 (Proficient) - Week 2-3:
[ ] Zero bugs on katas 1-2 for a week
[ ] Consistently under target time
[ ] Can code kata 3 from memory (cycle start is tricky!)
→ READY FOR: Medium cantrips (LC #142, #143)

LEVEL 4 (Mastered) - Week 3-5:
[ ] 10+ perfect reps on each kata
[ ] Under 80% of target time
[ ] Can code kata 4 from memory
[ ] Used successfully in 5+ cantrips
→ READY FOR: Hard cantrips and teaching others

LEVEL 5 (Breathing Knowledge) - Week 5+:
[ ] Pattern recognition is automatic (< 10 sec in new problems)
[ ] Can code all 4 katas in under 12 minutes
[ ] Can teach this pattern to someone else
[ ] Can explain the cycle detection proof
→ INTERVIEW READY: This pattern is now a superpower

THE CYCLE START TRICK (Kata 3):
This is one of the most elegant algorithms in CS.
Understanding WHY it works is interview gold.
Practice explaining the math proof out loud!

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on katas 1-2 → Start Easy cantrips
- Reach Level 3 (Proficient) → Start Medium cantrips
- If you struggle on a cantrip → Return to katas for more reps
- THE RULE: Don't attempt LC #142 until you can code kata 3 perfectly
"""


class ListNode:
    """Linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """
    KATA 1: Detect cycle in linked list (LC #141)

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Edge cases:
    - Empty list → False
    - Single node → False
    - Two nodes with cycle
    - Fast pointer reaches end → no cycle

    Key: Fast moves 2 steps, slow moves 1. If they meet, there's a cycle.

    START CODING BELOW:
    """
    pass

def find_middle(head: ListNode | None) -> ListNode | None:
    """
    KATA 2: Find middle of linked list (LC #876)

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Edge cases:
    - Empty list → None
    - Single node → that node
    - Even length → return second middle

    Key: When fast reaches end, slow is at middle.

    START CODING BELOW:
    """
    pass

def detect_cycle_start(head: ListNode | None) -> ListNode | None:
    """
    KATA 3: Find where cycle begins (LC #142)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    This is ADVANCED! Master kata 1-2 first.

    Algorithm:
    1. Use fast-slow to detect if cycle exists
    2. If cycle found: reset slow to head
    3. Move both 1 step at a time
    4. Where they meet is cycle start

    Edge cases:
    - No cycle → return None
    - Cycle at head → return head

    START CODING BELOW:
    """
    pass

def is_happy_number(n: int) -> bool:
    """
    KATA 4: Happy Number (LC #202)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: Zero bugs, O(log n) time, O(1) space

    This is a CREATIVE use of fast-slow!

    Problem: A happy number reaches 1 when replacing by sum of squares of digits.
    Example: 19 → 1²+9² = 82 → 8²+2² = 68 → ... → 1

    Key insight: Use fast-slow to detect cycle in the sequence!
    - If cycle reaches 1 → happy
    - If cycle doesn't include 1 → not happy

    Helper function you'll need:
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total

    START CODING BELOW:
    """
    pass

# ============================================================================
# TEST HELPERS
# ============================================================================

def create_cycle_list(values: list[int], cycle_pos: int = -1) -> ListNode:
    """Create linked list with optional cycle for testing."""
    pass

# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
MASTERY CHECKLIST:
[ ] Kata 1: Can code has_cycle in < 2 min, zero bugs
[ ] Kata 2: Can code find_middle in < 2 min, zero bugs
[ ] Kata 3: Can code detect_cycle_start in < 4 min, zero bugs
[ ] Kata 4: Can code is_happy_number in < 5 min, zero bugs
[ ] Understand WHY fast-slow works for cycles
[ ] Can explain the algorithm while coding
[ ] Recognize fast-slow pattern in new problems (< 30 sec)

PRACTICE LOG:
Date       | Kata | Time  | Bugs | Notes
-----------|------|-------|------|---------------------------------------


BREATHING KNOWLEDGE:
[ ] All 4 katas in under 12 minutes total
[ ] Zero bugs across all katas
[ ] Can teach this pattern
"""


if __name__ == "__main__":
    print("=" * 60)
    print("TWO POINTERS (FAST & SLOW) - KATA PRACTICE")
    print("=" * 60)
    print()

    # Test kata 1: has_cycle
    print("Testing KATA 1: has_cycle")
    list_no_cycle = create_cycle_list([1, 2, 3, 4])
    list_with_cycle = create_cycle_list([1, 2, 3, 4], cycle_pos=1)

    try:
        assert has_cycle(list_no_cycle) == False, "No cycle test failed"
        assert has_cycle(list_with_cycle) == True, "Cycle test failed"
        print("✅ Kata 1: Passed!")
    except (AssertionError, Exception) as e:
        print(f"❌ Kata 1: {e}")

    print()
    print("Complete remaining katas and run manual tests!")
    print()
    print("=" * 60)
