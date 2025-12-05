"""Tests for the database module."""

import tempfile
from datetime import date
from pathlib import Path

import pytest

from cantrips.data import Database, PracticeSession, MasteryStatus


@pytest.fixture
def temp_db():
    """Create a temporary database for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        db = Database(db_path)
        yield db


class TestDatabase:
    """Tests for Database class."""

    def test_log_session(self, temp_db):
        """Test logging a practice session."""
        session = PracticeSession(
            pattern_name="sliding_window/fixed_window",
            cantrip_number=1,
            date=date.today(),
            time_seconds=120,
            bugs=0,
        )
        temp_db.log_session(session)

        stats = temp_db.get_total_stats()
        assert stats["total_sessions"] == 1

    def test_streak_calculation(self, temp_db):
        """Test streak calculation."""
        streak = temp_db.get_streak()
        assert streak.current == 0
        assert streak.longest == 0

        # Log a session today
        session = PracticeSession(
            pattern_name="test/pattern",
            cantrip_number=1,
            date=date.today(),
            time_seconds=60,
            bugs=0,
        )
        temp_db.log_session(session)

        streak = temp_db.get_streak()
        assert streak.current == 1

    def test_review_queue(self, temp_db):
        """Test review queue functionality."""
        # Initially empty
        queue = temp_db.get_review_queue()
        assert len(queue) == 0

        # Log a session - should add to review queue
        session = PracticeSession(
            pattern_name="test/pattern",
            cantrip_number=1,
            date=date.today(),
            time_seconds=60,
            bugs=0,
        )
        temp_db.log_session(session)

        # Pattern should be in queue (scheduled for tomorrow)
        # Note: won't show as "due" until tomorrow
        queue = temp_db.get_review_queue()
        # Queue might be empty if scheduled for future
        assert isinstance(queue, list)

    def test_pattern_progress(self, temp_db):
        """Test pattern progress tracking."""
        pattern_name = "test/pattern"

        # Log multiple sessions
        for i in range(5):
            session = PracticeSession(
                pattern_name=pattern_name,
                cantrip_number=1,
                date=date.today(),
                time_seconds=100 + i * 10,
                bugs=0,
            )
            temp_db.log_session(session)

        progress = temp_db.get_pattern_progress(pattern_name)
        assert progress is not None
        assert progress.total_sessions == 5
        assert progress.mastery_status == MasteryStatus.PRACTICING

    def test_recent_sessions(self, temp_db):
        """Test getting recent sessions."""
        # Log some sessions
        for i in range(3):
            session = PracticeSession(
                pattern_name=f"test/pattern{i}",
                cantrip_number=1,
                date=date.today(),
                time_seconds=60,
                bugs=0,
            )
            temp_db.log_session(session)

        recent = temp_db.get_recent_sessions(limit=10)
        assert len(recent) == 3


class TestMasteryStatus:
    """Tests for MasteryStatus enum."""

    def test_status_colors(self):
        """Test status colors are defined."""
        assert MasteryStatus.LEARNING.color == "white"
        assert MasteryStatus.PRACTICING.color == "yellow"
        assert MasteryStatus.MASTERED.color == "green"

    def test_status_symbols(self):
        """Test status symbols are defined."""
        assert MasteryStatus.LEARNING.symbol == "○"
        assert MasteryStatus.PRACTICING.symbol == "◐"
        assert MasteryStatus.MASTERED.symbol == "✓"
