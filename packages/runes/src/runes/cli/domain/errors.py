"""
Domain errors for kata practice system.

Error types that can occur during kata operations.
"""

from pathlib import Path
from typing import Optional


class KataError(Exception):
    """Base error for all kata operations."""

    def __init__(self, message: str, details: Optional[dict] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            details_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{self.message} ({details_str})"
        return self.message


class FileSystemError(KataError):
    """Errors related to file operations."""

    @classmethod
    def file_not_found(cls, path: Path) -> "FileSystemError":
        return cls(
            f"File not found: {path.name}",
            details={"path": str(path), "reason": "not_found"},
        )

    @classmethod
    def permission_denied(cls, path: Path) -> "FileSystemError":
        return cls(
            f"Permission denied: {path.name}",
            details={"path": str(path), "reason": "permission"},
        )

    @classmethod
    def directory_not_found(cls, path: Path) -> "FileSystemError":
        return cls(
            f"Directory not found: {path}",
            details={"path": str(path), "reason": "directory_missing"},
        )


class ParseError(KataError):
    """Errors related to parsing kata files."""

    @classmethod
    def no_mastery_section(cls, path: Path) -> "ParseError":
        return cls(
            "No mastery tracking section found",
            details={"path": str(path), "reason": "missing_section"},
        )

    @classmethod
    def malformed_entry(cls, path: Path, line_number: int, content: str) -> "ParseError":
        return cls(
            f"Malformed log entry at line {line_number}",
            details={
                "path": str(path),
                "line": line_number,
                "content": content[:50],
            },
        )

    @classmethod
    def invalid_date_format(cls, date_str: str) -> "ParseError":
        return cls(
            f"Invalid date format: {date_str}",
            details={"date": date_str, "expected_format": "YYYY-MM-DD"},
        )


class ValidationError(KataError):
    """Errors related to input validation."""

    @classmethod
    def invalid_time_format(cls, time_str: str) -> "ValidationError":
        return cls(
            f"Invalid time format: {time_str}",
            details={"time": time_str, "expected_format": "M:SS or MM:SS"},
        )

    @classmethod
    def invalid_kata_number(cls, kata_num: int, max_num: int) -> "ValidationError":
        return cls(
            f"Invalid kata number: {kata_num}",
            details={"kata_number": kata_num, "valid_range": f"1-{max_num}"},
        )

    @classmethod
    def negative_bugs(cls, bugs: int) -> "ValidationError":
        return cls(
            "Bug count cannot be negative",
            details={"bugs": bugs},
        )
