"""Expression evaluation pattern cantrips.

Use expression evaluation when:
- Evaluating mathematical expressions (infix, postfix, prefix)
- Calculator problems
- Need to handle operator precedence
- Parentheses change evaluation order
- Stack stores operands (numbers), process operators sequentially
"""

from .p001_eval_rpn import eval_rpn
from .p002_build_array import build_array
from .p003_calculator import calculate
from .p004_calculator_ii import calculate_ii
from .p005_calculator_iii import calculate_iii

__all__ = [
    "eval_rpn",
    "build_array",
    "calculate",
    "calculate_ii",
    "calculate_iii",
]
