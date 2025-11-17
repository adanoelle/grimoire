"""
Pytest configuration and custom fixtures for algorithm kata practice.

This conftest.py is automatically loaded by pytest when running tests
in the algorithms directory and its subdirectories.
"""

import pytest


def pytest_configure(config):
    """Register custom markers for kata practice."""
    config.addinivalue_line(
        "markers",
        "kata_todo: mark test as a kata that hasn't been implemented yet (shows as TODO)"
    )
    config.addinivalue_line(
        "markers",
        "kata1: kata difficulty level 1 (easiest)"
    )
    config.addinivalue_line(
        "markers",
        "kata2: kata difficulty level 2 (medium)"
    )
    config.addinivalue_line(
        "markers",
        "kata3: kata difficulty level 3 (harder)"
    )


def kata_todo(reason="Not yet implemented"):
    """
    Custom decorator to mark unimplemented kata tests.

    This is more semantic than @pytest.mark.skip for kata practice.
    Shows as "TODO" in test output instead of "SKIP".

    Usage:
        @kata_todo()
        def test_kata_2_palindrome():
            assert is_palindrome("racecar") == True

    Args:
        reason: Optional reason why kata is not yet implemented

    Returns:
        pytest.mark.skip decorator with TODO formatting
    """
    return pytest.mark.skip(reason=f"TODO: {reason}")


# Export for easy importing
__all__ = ["kata_todo"]
