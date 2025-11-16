"""
Two Pointers: Fast & Slow (Floyd's Cycle Detection)

Core Intuition:
    Fast pointer moves 2 steps, slow pointer moves 1 step.
    If there's a cycle, they will meet. If no cycle, fast reaches end.

When to Use:
    - Detect cycles in linked lists
    - Find middle of linked list
    - Find cycle start point
    - Detect duplicates in array (if values point to indices)

Time Complexity: O(n)
Space Complexity: O(1)

Key Insight:
    In a cycle, fast pointer "laps" slow pointer, guaranteed to meet.
"""


class ListNode:
    """Simple linked list node for examples."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """
    TEMPLATE: Detect if linked list has cycle.

    This is THE canonical fast-slow pointer template.
    Master this first.

    Args:
        head: Head of linked list

    Returns:
        True if cycle exists, False otherwise

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next           # Move 1 step
        fast = fast.next.next      # Move 2 steps

        if slow == fast:           # They met - cycle!
            return True

    return False  # Fast reached end - no cycle


def find_middle(head: ListNode | None) -> ListNode | None:
    """
    TEMPLATE: Find middle node of linked list.

    When fast reaches end, slow is at middle.

    Args:
        head: Head of linked list

    Returns:
        Middle node (for even length, return second middle)

    Time: O(n), Space: O(1)
    """
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Slow is at middle


def detect_cycle_start(head: ListNode | None) -> ListNode | None:
    """
    TEMPLATE: Find where cycle begins (LC #142).

    Advanced variant:
    1. Use fast-slow to detect cycle
    2. Reset one pointer to head
    3. Move both 1 step at a time - they meet at cycle start

    Args:
        head: Head of linked list

    Returns:
        Node where cycle begins, or None if no cycle

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return None

    # Phase 1: Detect if cycle exists
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Phase 2: Find cycle start
    # Reset one pointer to head, move both 1 step at a time
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Meeting point is cycle start


if __name__ == "__main__":
    print("✓ Two Pointers (Fast & Slow) templates loaded")
    print("Study these until you can code them from memory!")
