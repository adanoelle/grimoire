"""Tests for the discovery module."""

import pytest

from cantrips.utils.discovery import (
    discover_patterns,
    get_pattern,
    get_cantrip_file,
    PatternInfo,
    CantripsInfo,
)


class TestDiscovery:
    """Tests for pattern discovery."""

    def test_discover_patterns(self):
        """Test that patterns are discovered."""
        patterns = discover_patterns()
        assert len(patterns) > 0

        # Check structure
        for pattern in patterns:
            assert isinstance(pattern, PatternInfo)
            assert pattern.name
            assert pattern.category
            assert pattern.path.exists()

    def test_pattern_has_cantrips(self):
        """Test that patterns have cantrips."""
        patterns = discover_patterns()

        for pattern in patterns:
            assert len(pattern.cantrips) > 0
            for cantrip in pattern.cantrips:
                assert isinstance(cantrip, CantripsInfo)
                assert cantrip.number > 0
                assert cantrip.name

    def test_get_pattern(self):
        """Test getting a specific pattern."""
        pattern = get_pattern("sliding_window/fixed_window")
        assert pattern is not None
        assert pattern.name == "fixed_window"
        assert pattern.category == "sliding_window"

    def test_get_pattern_not_found(self):
        """Test getting a non-existent pattern."""
        pattern = get_pattern("nonexistent/pattern")
        assert pattern is None

    def test_get_cantrip_file(self):
        """Test getting a cantrip file path."""
        path = get_cantrip_file("sliding_window/fixed_window", 1)
        assert path is not None
        assert path.exists()
        assert "p001_" in path.name

    def test_cantrip_file_not_found(self):
        """Test getting a non-existent cantrip file."""
        path = get_cantrip_file("sliding_window/fixed_window", 99)
        assert path is None


class TestPatternInfo:
    """Tests for PatternInfo dataclass."""

    def test_full_name(self):
        """Test full_name property."""
        patterns = discover_patterns()
        if patterns:
            pattern = patterns[0]
            assert pattern.full_name == f"{pattern.category}/{pattern.name}"

    def test_cantrip_count(self):
        """Test cantrip_count property."""
        patterns = discover_patterns()
        if patterns:
            pattern = patterns[0]
            assert pattern.cantrip_count == len(pattern.cantrips)
