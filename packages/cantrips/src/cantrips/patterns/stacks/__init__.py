"""Stack pattern cantrips.

Subpatterns:
- matching: Bracket matching, duplicate removal, valid expressions
- monotonic: Next greater/smaller element problems
- expression_eval: Calculator and expression evaluation
- state_tracking: Min/Max stack, frequency tracking
"""

from . import matching
from . import monotonic
from . import expression_eval
from . import state_tracking

__all__ = [
    "matching",
    "monotonic",
    "expression_eval",
    "state_tracking",
]
