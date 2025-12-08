"""
SQLite database for cantrips progress tracking.

Handles all database operations including schema creation and migrations.
"""

import json
import sqlite3
from contextlib import contextmanager
from datetime import date, datetime
from pathlib import Path
from typing import Iterator

from .models import (
    CantripsNote,
    DailyActivity,
    MasteryStatus,
    PatternProgress,
    PracticeSession,
    ReviewItem,
    Streak,
)

# Default database location
DEFAULT_DB_PATH = Path.home() / ".grimoire" / "cantrips.db"

SCHEMA_VERSION = 2

SCHEMA = """
-- Practice sessions (primary tracking)
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern_name TEXT NOT NULL,
    cantrip_number INTEGER NOT NULL,
    date DATE NOT NULL,
    time_seconds INTEGER NOT NULL,
    bugs INTEGER NOT NULL DEFAULT 0,
    notes TEXT DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Daily activity (for contribution calendar)
CREATE TABLE IF NOT EXISTS daily_activity (
    date DATE PRIMARY KEY,
    sessions_count INTEGER NOT NULL DEFAULT 0,
    total_time_seconds INTEGER NOT NULL DEFAULT 0,
    patterns_practiced TEXT NOT NULL DEFAULT '[]'
);

-- Spaced repetition queue
CREATE TABLE IF NOT EXISTS review_queue (
    pattern_name TEXT PRIMARY KEY,
    last_reviewed DATE,
    next_review DATE,
    ease_factor REAL DEFAULT 2.5,
    interval_days INTEGER DEFAULT 1,
    repetitions INTEGER DEFAULT 0
);

-- Pattern progress cache (for fast dashboard queries)
CREATE TABLE IF NOT EXISTS pattern_cache (
    pattern_name TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    category TEXT NOT NULL,
    total_sessions INTEGER DEFAULT 0,
    mastery_status TEXT DEFAULT 'Learning',
    last_practice DATE,
    best_times TEXT DEFAULT '{}',
    total_bugs TEXT DEFAULT '{}'
);

-- Schema version tracking
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY
);

-- Persistent cantrip notes (accumulate across sessions)
CREATE TABLE IF NOT EXISTS cantrip_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern_name TEXT NOT NULL,
    cantrip_number INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(pattern_name, cantrip_number)
);

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_sessions_pattern ON sessions(pattern_name);
CREATE INDEX IF NOT EXISTS idx_sessions_date ON sessions(date);
CREATE INDEX IF NOT EXISTS idx_review_next ON review_queue(next_review);
CREATE INDEX IF NOT EXISTS idx_cantrip_notes_pattern ON cantrip_notes(pattern_name);
"""


class Database:
    """SQLite database for cantrips progress tracking."""

    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = db_path or DEFAULT_DB_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    @contextmanager
    def _connection(self) -> Iterator[sqlite3.Connection]:
        """Get a database connection with row factory."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _init_schema(self) -> None:
        """Initialize database schema."""
        with self._connection() as conn:
            conn.executescript(SCHEMA)
            # Check/set schema version
            cursor = conn.execute("SELECT version FROM schema_version LIMIT 1")
            row = cursor.fetchone()
            if row is None:
                conn.execute(
                    "INSERT INTO schema_version (version) VALUES (?)", (SCHEMA_VERSION,)
                )

    # ─────────────────────────────────────────────────────────────────
    # Session Operations
    # ─────────────────────────────────────────────────────────────────

    def log_session(self, session: PracticeSession) -> int:
        """Log a practice session. Returns the session ID."""
        with self._connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO sessions (pattern_name, cantrip_number, date, time_seconds, bugs, notes)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    session.pattern_name,
                    session.cantrip_number,
                    session.date.isoformat(),
                    session.time_seconds,
                    session.bugs,
                    session.notes,
                ),
            )
            session_id = cursor.lastrowid or 0

            # Update related tables
            self._update_daily_activity(conn, session)
            self._update_pattern_cache(conn, session.pattern_name)
            self._update_review_queue(conn, session)

            return session_id

    def get_sessions(
        self,
        pattern_name: str | None = None,
        limit: int = 50,
    ) -> list[PracticeSession]:
        """Get practice sessions, optionally filtered by pattern."""
        with self._connection() as conn:
            if pattern_name:
                cursor = conn.execute(
                    """
                    SELECT * FROM sessions
                    WHERE pattern_name = ?
                    ORDER BY date DESC, created_at DESC
                    LIMIT ?
                    """,
                    (pattern_name, limit),
                )
            else:
                cursor = conn.execute(
                    """
                    SELECT * FROM sessions
                    ORDER BY date DESC, created_at DESC
                    LIMIT ?
                    """,
                    (limit,),
                )
            return [self._row_to_session(row) for row in cursor.fetchall()]

    def _row_to_session(self, row: sqlite3.Row) -> PracticeSession:
        """Convert a database row to a PracticeSession."""
        return PracticeSession(
            id=row["id"],
            pattern_name=row["pattern_name"],
            cantrip_number=row["cantrip_number"],
            date=date.fromisoformat(row["date"]),
            time_seconds=row["time_seconds"],
            bugs=row["bugs"],
            notes=row["notes"],
            created_at=datetime.fromisoformat(row["created_at"])
            if row["created_at"]
            else None,
        )

    # ─────────────────────────────────────────────────────────────────
    # Daily Activity (Contribution Calendar)
    # ─────────────────────────────────────────────────────────────────

    def _update_daily_activity(
        self, conn: sqlite3.Connection, session: PracticeSession
    ) -> None:
        """Update daily activity after a session."""
        date_str = session.date.isoformat()

        # Get current activity for this date
        cursor = conn.execute(
            "SELECT * FROM daily_activity WHERE date = ?", (date_str,)
        )
        row = cursor.fetchone()

        if row:
            patterns = json.loads(row["patterns_practiced"])
            if session.pattern_name not in patterns:
                patterns.append(session.pattern_name)
            conn.execute(
                """
                UPDATE daily_activity
                SET sessions_count = sessions_count + 1,
                    total_time_seconds = total_time_seconds + ?,
                    patterns_practiced = ?
                WHERE date = ?
                """,
                (session.time_seconds, json.dumps(patterns), date_str),
            )
        else:
            conn.execute(
                """
                INSERT INTO daily_activity (date, sessions_count, total_time_seconds, patterns_practiced)
                VALUES (?, 1, ?, ?)
                """,
                (date_str, session.time_seconds, json.dumps([session.pattern_name])),
            )

    def get_daily_activity(self, days: int = 365) -> list[DailyActivity]:
        """Get daily activity for the contribution calendar."""
        with self._connection() as conn:
            cursor = conn.execute(
                """
                SELECT * FROM daily_activity
                WHERE date >= date('now', 'localtime', ?)
                ORDER BY date ASC
                """,
                (f"-{days} days",),
            )
            return [
                DailyActivity(
                    date=date.fromisoformat(row["date"]),
                    sessions_count=row["sessions_count"],
                    total_time_seconds=row["total_time_seconds"],
                    patterns_practiced=json.loads(row["patterns_practiced"]),
                )
                for row in cursor.fetchall()
            ]

    def get_calendar_data(self, days: int = 365) -> dict[str, int]:
        """Get activity counts by date for calendar rendering."""
        with self._connection() as conn:
            cursor = conn.execute(
                """
                SELECT date, sessions_count FROM daily_activity
                WHERE date >= date('now', 'localtime', ?)
                """,
                (f"-{days} days",),
            )
            return {row["date"]: row["sessions_count"] for row in cursor.fetchall()}

    # ─────────────────────────────────────────────────────────────────
    # Pattern Progress
    # ─────────────────────────────────────────────────────────────────

    def _update_pattern_cache(self, conn: sqlite3.Connection, pattern_name: str) -> None:
        """Update pattern cache after a session."""
        # Calculate stats from sessions
        cursor = conn.execute(
            """
            SELECT
                COUNT(*) as total_sessions,
                MAX(date) as last_practice
            FROM sessions
            WHERE pattern_name = ?
            """,
            (pattern_name,),
        )
        row = cursor.fetchone()
        total_sessions = row["total_sessions"] if row else 0
        last_practice = row["last_practice"] if row else None

        # Calculate best times per cantrip
        cursor = conn.execute(
            """
            SELECT cantrip_number, MIN(time_seconds) as best_time
            FROM sessions
            WHERE pattern_name = ? AND bugs = 0
            GROUP BY cantrip_number
            """,
            (pattern_name,),
        )
        best_times = {row["cantrip_number"]: row["best_time"] for row in cursor.fetchall()}

        # Calculate total bugs per cantrip
        cursor = conn.execute(
            """
            SELECT cantrip_number, SUM(bugs) as total_bugs
            FROM sessions
            WHERE pattern_name = ?
            GROUP BY cantrip_number
            """,
            (pattern_name,),
        )
        total_bugs = {row["cantrip_number"]: row["total_bugs"] for row in cursor.fetchall()}

        # Determine mastery status
        status = PatternProgress.calculate_status(total_sessions)

        # Extract display name and category from pattern_name
        parts = pattern_name.split("/")
        category = parts[0] if parts else pattern_name
        display_name = parts[-1] if parts else pattern_name

        # Upsert pattern cache
        conn.execute(
            """
            INSERT INTO pattern_cache
                (pattern_name, display_name, category, total_sessions, mastery_status, last_practice, best_times, total_bugs)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(pattern_name) DO UPDATE SET
                total_sessions = excluded.total_sessions,
                mastery_status = excluded.mastery_status,
                last_practice = excluded.last_practice,
                best_times = excluded.best_times,
                total_bugs = excluded.total_bugs
            """,
            (
                pattern_name,
                display_name,
                category,
                total_sessions,
                status.value,
                last_practice,
                json.dumps(best_times),
                json.dumps(total_bugs),
            ),
        )

    def get_pattern_progress(self, pattern_name: str) -> PatternProgress | None:
        """Get progress for a specific pattern."""
        with self._connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM pattern_cache WHERE pattern_name = ?", (pattern_name,)
            )
            row = cursor.fetchone()
            if not row:
                return None
            return self._row_to_pattern_progress(row)

    def get_all_patterns(self) -> list[PatternProgress]:
        """Get progress for all patterns."""
        with self._connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM pattern_cache ORDER BY category, display_name"
            )
            return [self._row_to_pattern_progress(row) for row in cursor.fetchall()]

    def _row_to_pattern_progress(self, row: sqlite3.Row) -> PatternProgress:
        """Convert a database row to PatternProgress."""
        best_times_raw = json.loads(row["best_times"]) if row["best_times"] else {}
        total_bugs_raw = json.loads(row["total_bugs"]) if row["total_bugs"] else {}

        return PatternProgress(
            pattern_name=row["pattern_name"],
            display_name=row["display_name"],
            category=row["category"],
            total_sessions=row["total_sessions"],
            mastery_status=MasteryStatus(row["mastery_status"]),
            last_practice=date.fromisoformat(row["last_practice"])
            if row["last_practice"]
            else None,
            best_times={int(k): v for k, v in best_times_raw.items()},
            total_bugs={int(k): v for k, v in total_bugs_raw.items()},
        )

    # ─────────────────────────────────────────────────────────────────
    # Spaced Repetition
    # ─────────────────────────────────────────────────────────────────

    def _update_review_queue(
        self, conn: sqlite3.Connection, session: PracticeSession
    ) -> None:
        """Update spaced repetition schedule after a session (SM-2 algorithm)."""
        cursor = conn.execute(
            "SELECT * FROM review_queue WHERE pattern_name = ?",
            (session.pattern_name,),
        )
        row = cursor.fetchone()

        today = date.today()

        if row:
            ease_factor = row["ease_factor"]
            interval = row["interval_days"]
            reps = row["repetitions"]

            # SM-2 inspired algorithm
            if session.bugs == 0:
                # Success: increase interval
                reps += 1
                if reps == 1:
                    interval = 1
                elif reps == 2:
                    interval = 3
                else:
                    interval = int(interval * ease_factor)
                # Adjust ease factor (min 1.3)
                ease_factor = max(1.3, ease_factor + 0.1)
            elif session.bugs <= 2:
                # Partial: keep interval, slight ease decrease
                ease_factor = max(1.3, ease_factor - 0.1)
            else:
                # Failed: reset
                reps = 0
                interval = 1
                ease_factor = max(1.3, ease_factor - 0.2)

            next_review = today.toordinal() + interval
            next_review_date = date.fromordinal(next_review)

            conn.execute(
                """
                UPDATE review_queue
                SET last_reviewed = ?, next_review = ?, ease_factor = ?,
                    interval_days = ?, repetitions = ?
                WHERE pattern_name = ?
                """,
                (
                    today.isoformat(),
                    next_review_date.isoformat(),
                    ease_factor,
                    interval,
                    reps,
                    session.pattern_name,
                ),
            )
        else:
            # First time practicing this pattern
            next_review = today.toordinal() + 1
            next_review_date = date.fromordinal(next_review)
            conn.execute(
                """
                INSERT INTO review_queue
                    (pattern_name, last_reviewed, next_review, ease_factor, interval_days, repetitions)
                VALUES (?, ?, ?, 2.5, 1, 1)
                """,
                (session.pattern_name, today.isoformat(), next_review_date.isoformat()),
            )

    def get_review_queue(self) -> list[ReviewItem]:
        """Get patterns due for review, sorted by priority."""
        with self._connection() as conn:
            cursor = conn.execute(
                """
                SELECT * FROM review_queue
                WHERE next_review <= date('now', 'localtime')
                ORDER BY next_review ASC
                """
            )
            return [self._row_to_review_item(row) for row in cursor.fetchall()]

    def get_upcoming_reviews(self, days: int = 7) -> list[ReviewItem]:
        """Get patterns coming up for review in the next N days."""
        with self._connection() as conn:
            cursor = conn.execute(
                """
                SELECT * FROM review_queue
                WHERE next_review > date('now', 'localtime')
                  AND next_review <= date('now', 'localtime', ?)
                ORDER BY next_review ASC
                """,
                (f"+{days} days",),
            )
            return [self._row_to_review_item(row) for row in cursor.fetchall()]

    def _row_to_review_item(self, row: sqlite3.Row) -> ReviewItem:
        """Convert a database row to ReviewItem."""
        return ReviewItem(
            pattern_name=row["pattern_name"],
            last_reviewed=date.fromisoformat(row["last_reviewed"])
            if row["last_reviewed"]
            else None,
            next_review=date.fromisoformat(row["next_review"])
            if row["next_review"]
            else None,
            ease_factor=row["ease_factor"],
            interval_days=row["interval_days"],
            repetitions=row["repetitions"],
        )

    # ─────────────────────────────────────────────────────────────────
    # Streak Calculation
    # ─────────────────────────────────────────────────────────────────

    def get_streak(self) -> Streak:
        """Calculate current and longest practice streak."""
        with self._connection() as conn:
            # Get all practice dates in descending order
            cursor = conn.execute(
                """
                SELECT DISTINCT date FROM daily_activity
                ORDER BY date DESC
                """
            )
            dates = [date.fromisoformat(row["date"]) for row in cursor.fetchall()]

            if not dates:
                return Streak()

            today = date.today()
            last_practice = dates[0]

            # Calculate current streak
            current_streak = 0
            check_date = today

            for practice_date in dates:
                # Allow for today or yesterday to continue streak
                diff = (check_date - practice_date).days
                if diff <= 1:
                    current_streak += 1
                    check_date = practice_date
                else:
                    break

            # Calculate longest streak (simple approach)
            longest_streak = current_streak
            if len(dates) > 1:
                streak = 1
                for i in range(1, len(dates)):
                    if (dates[i - 1] - dates[i]).days == 1:
                        streak += 1
                        longest_streak = max(longest_streak, streak)
                    else:
                        streak = 1

            return Streak(
                current=current_streak,
                longest=longest_streak,
                last_practice_date=last_practice,
            )

    # ─────────────────────────────────────────────────────────────────
    # Statistics
    # ─────────────────────────────────────────────────────────────────

    def get_today_stats(self) -> DailyActivity:
        """Get today's activity stats."""
        today_str = date.today().isoformat()
        with self._connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM daily_activity WHERE date = ?", (today_str,)
            )
            row = cursor.fetchone()
            if row:
                return DailyActivity(
                    date=date.today(),
                    sessions_count=row["sessions_count"],
                    total_time_seconds=row["total_time_seconds"],
                    patterns_practiced=json.loads(row["patterns_practiced"]),
                )
            return DailyActivity(date=date.today())

    def get_total_stats(self) -> dict[str, int]:
        """Get overall statistics."""
        with self._connection() as conn:
            cursor = conn.execute(
                """
                SELECT
                    COUNT(*) as total_sessions,
                    COUNT(DISTINCT pattern_name) as patterns_practiced,
                    COALESCE(SUM(time_seconds), 0) as total_time_seconds
                FROM sessions
                """
            )
            row = cursor.fetchone()
            return {
                "total_sessions": row["total_sessions"],
                "patterns_practiced": row["patterns_practiced"],
                "total_time_seconds": row["total_time_seconds"],
            }

    def get_recent_sessions(self, limit: int = 10) -> list[PracticeSession]:
        """Get most recent practice sessions.

        Args:
            limit: Maximum number of sessions to return.

        Returns:
            List of recent PracticeSession objects, newest first.
        """
        with self._connection() as conn:
            cursor = conn.execute(
                """
                SELECT * FROM sessions
                ORDER BY date DESC, created_at DESC
                LIMIT ?
                """,
                (limit,),
            )
            return [
                PracticeSession(
                    id=row["id"],
                    pattern_name=row["pattern_name"],
                    cantrip_number=row["cantrip_number"],
                    date=date.fromisoformat(row["date"]),
                    time_seconds=row["time_seconds"],
                    bugs=row["bugs"],
                    notes=row["notes"],
                )
                for row in cursor.fetchall()
            ]

    # ─────────────────────────────────────────────────────────────────
    # Cantrip Notes
    # ─────────────────────────────────────────────────────────────────

    def get_cantrip_note(self, pattern_name: str, cantrip_number: int) -> CantripsNote | None:
        """Get persistent note for a specific cantrip.

        Args:
            pattern_name: Pattern identifier (e.g., "sliding_window/fixed_window").
            cantrip_number: Which cantrip in the pattern (1-5).

        Returns:
            CantripsNote if one exists, None otherwise.
        """
        with self._connection() as conn:
            cursor = conn.execute(
                """
                SELECT * FROM cantrip_notes
                WHERE pattern_name = ? AND cantrip_number = ?
                """,
                (pattern_name, cantrip_number),
            )
            row = cursor.fetchone()
            if row:
                return CantripsNote(
                    id=row["id"],
                    pattern_name=row["pattern_name"],
                    cantrip_number=row["cantrip_number"],
                    content=row["content"],
                    created_at=datetime.fromisoformat(row["created_at"])
                    if row["created_at"]
                    else None,
                    updated_at=datetime.fromisoformat(row["updated_at"])
                    if row["updated_at"]
                    else None,
                )
            return None

    def save_cantrip_note(self, note: CantripsNote) -> int:
        """Save or update a cantrip note (upsert).

        If a note already exists for this pattern/cantrip, it will be updated.
        Otherwise, a new note will be created.

        Args:
            note: The CantripsNote to save.

        Returns:
            The note ID (either existing or newly created).
        """
        with self._connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO cantrip_notes (pattern_name, cantrip_number, content, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(pattern_name, cantrip_number) DO UPDATE SET
                    content = excluded.content,
                    updated_at = CURRENT_TIMESTAMP
                """,
                (note.pattern_name, note.cantrip_number, note.content),
            )
            # Get the ID (either new or existing)
            cursor = conn.execute(
                """
                SELECT id FROM cantrip_notes
                WHERE pattern_name = ? AND cantrip_number = ?
                """,
                (note.pattern_name, note.cantrip_number),
            )
            row = cursor.fetchone()
            return row["id"] if row else 0
