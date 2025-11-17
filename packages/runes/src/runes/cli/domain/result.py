"""
Result type for explicit error handling.

Simple implementation of the Result pattern for functional error handling.
"""

from typing import TypeVar, Generic, Callable, Any
from dataclasses import dataclass

T = TypeVar("T")
E = TypeVar("E", bound=Exception)


@dataclass(frozen=True)
class Success(Generic[T]):
    """Successful result containing a value."""

    value: T

    def is_success(self) -> bool:
        return True

    def is_failure(self) -> bool:
        return False

    def unwrap(self) -> T:
        """Get the success value."""
        return self.value

    def unwrap_or(self, default: T) -> T:
        """Get the success value or default."""
        return self.value

    def map(self, func: Callable[[T], Any]) -> "Result[Any, E]":
        """Apply function to success value."""
        try:
            return Success(func(self.value))
        except Exception as e:
            return Failure(e)

    def __repr__(self) -> str:
        return f"Success({self.value!r})"


@dataclass(frozen=True)
class Failure(Generic[E]):
    """Failed result containing an error."""

    error: E

    def is_success(self) -> bool:
        return False

    def is_failure(self) -> bool:
        return True

    def unwrap(self) -> Any:
        """Raises the error (use when you know it's Success)."""
        raise self.error

    def unwrap_or(self, default: T) -> T:
        """Return default value on failure."""
        return default

    def map(self, func: Callable) -> "Result[Any, E]":
        """Mapping over failure returns the failure."""
        return self

    def __repr__(self) -> str:
        return f"Failure({self.error!r})"


# Type alias for Result
Result = Success[T] | Failure[E]


def wrap_result(func: Callable[..., T]) -> Callable[..., Result[T, Exception]]:
    """
    Decorator to wrap a function to return Result instead of raising.

    Usage:
        @wrap_result
        def risky_operation(x: int) -> int:
            if x < 0:
                raise ValueError("x must be positive")
            return x * 2

        result = risky_operation(5)
        if result.is_success():
            print(result.unwrap())  # 10
    """

    def wrapper(*args: Any, **kwargs: Any) -> Result[T, Exception]:
        try:
            return Success(func(*args, **kwargs))
        except Exception as e:
            return Failure(e)

    return wrapper
