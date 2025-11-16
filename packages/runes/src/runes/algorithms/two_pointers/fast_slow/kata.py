"""
Two Pointers (Fast & Slow) - Daily Kata Practice

🥋 Floyd's Cycle Detection Algorithm

Code from memory. Time yourself. Achieve zero bugs.
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
