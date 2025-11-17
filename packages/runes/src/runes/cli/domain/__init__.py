"""
Domain layer for kata practice system.

Pure business logic, domain models, and error types.
"""

from .errors import KataError, ParseError, FileSystemError, ValidationError
from .result import Result, Success, Failure

__all__ = [
    "KataError",
    "ParseError",
    "FileSystemError",
    "ValidationError",
    "Result",
    "Success",
    "Failure",
]
