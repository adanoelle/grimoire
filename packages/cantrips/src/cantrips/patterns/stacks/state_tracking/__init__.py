"""State tracking pattern cantrips.

Use state tracking when:
- Need to track min/max/frequency while maintaining stack operations
- O(1) constraint for queries (can't iterate stack)
- State depends on current stack depth
- "Design a stack that supports..." in problem description
"""

from .p001_min_stack import MinStack
from .p002_max_stack import MaxStack
from .p003_custom_stack import CustomStack
from .p004_freq_stack import FreqStack
from .p005_time_map import TimeMap

__all__ = [
    "MinStack",
    "MaxStack",
    "CustomStack",
    "FreqStack",
    "TimeMap",
]
