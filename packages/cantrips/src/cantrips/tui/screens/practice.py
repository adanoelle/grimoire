"""Practice screen for cantrips.

This screen handles the practice flow:
1. Show cantrip info and requirements
2. Start timer and open editor
3. Run tests and show results inline
4. Log session to database
"""

import subprocess
import os
import time
from datetime import date
from pathlib import Path

from rich.text import Text
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label, Static
from textual.reactive import reactive

from cantrips.data import Database, PracticeSession
from cantrips.utils.discovery import PatternInfo, CantripsInfo


class TimerDisplay(Static):
    """Live timer display widget."""

    DEFAULT_CSS = """
    TimerDisplay {
        text-align: center;
        text-style: bold;
        color: $success;
        padding: 1;
    }

    TimerDisplay.warning {
        color: $warning;
    }

    TimerDisplay.danger {
        color: $error;
    }
    """

    elapsed: reactive[float] = reactive(0.0)
    target_time: reactive[int] = reactive(120)
    running: reactive[bool] = reactive(False)

    def __init__(self, target_time: int = 120, **kwargs) -> None:
        super().__init__(**kwargs)
        self.target_time = target_time
        self._start_time: float | None = None
        self._timer_handle = None  # Track interval handle for cleanup

    def start(self) -> None:
        """Start the timer."""
        self._start_time = time.time()
        self.running = True
        self._timer_handle = self.set_interval(0.1, self._update_time)

    def stop(self) -> float:
        """Stop the timer and return elapsed seconds."""
        self.running = False
        if self._timer_handle:
            self._timer_handle.stop()
            self._timer_handle = None
        # Return accurate elapsed time, not potentially stale reactive value
        return self.get_elapsed()

    def get_elapsed(self) -> float:
        """Get current elapsed time accurately.

        This calculates from _start_time rather than relying on the reactive
        elapsed property, which may be stale if TUI was suspended.
        """
        if self._start_time:
            return time.time() - self._start_time
        return self.elapsed

    def _update_time(self) -> None:
        """Update elapsed time."""
        if self.running and self._start_time:
            self.elapsed = time.time() - self._start_time
            self.refresh()

            # Update style based on time
            if self.elapsed > self.target_time * 1.5:
                self.add_class("danger")
                self.remove_class("warning")
            elif self.elapsed > self.target_time:
                self.add_class("warning")
                self.remove_class("danger")

    def render(self) -> str:
        """Render the timer."""
        minutes = int(self.elapsed) // 60
        seconds = int(self.elapsed) % 60
        target_min = self.target_time // 60
        target_sec = self.target_time % 60
        return f"⏱️  {minutes:02d}:{seconds:02d} / Target: {target_min}:{target_sec:02d}"


class TestResultsPanel(Static):
    """Panel showing test results inline."""

    BORDER_TITLE = "Test Results"

    DEFAULT_CSS = """
    TestResultsPanel {
        height: auto;
        padding: 1;
        border: round $primary;
        margin-top: 1;
    }

    TestResultsPanel .passed {
        color: $success;
    }

    TestResultsPanel .failed {
        color: $error;
    }
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._results: str = ""
        self._passed: int = 0
        self._failed: int = 0

    def set_results(self, output: str, passed: int, failed: int) -> None:
        """Set test results."""
        self._results = output
        self._passed = passed
        self._failed = failed
        # Update border title with status
        total = passed + failed
        if failed == 0:
            self.border_title = f"Test Results [green]✓ {passed}/{total}[/green]"
        else:
            self.border_title = f"Test Results [red]✗ {passed}/{total}[/red]"
        self.refresh()

    def render(self) -> str:
        """Render test results."""
        if not self._results:
            return "[dim]No test results yet[/dim]"

        lines = []
        # Parse and display results
        for line in self._results.split("\n"):
            if "PASSED" in line:
                lines.append(f"[green]✓[/green] {line.strip()}")
            elif "FAILED" in line:
                lines.append(f"[red]✗[/red] {line.strip()}")
            elif "ERROR" in line:
                lines.append(f"[red]![/red] {line.strip()}")
            elif line.strip():
                lines.append(f"  {line.strip()}")

        return "\n".join(lines[:20])  # Limit output


class CantripsInfoPanel(Static):
    """Panel showing cantrip information."""

    DEFAULT_CSS = """
    CantripsInfoPanel {
        height: auto;
        padding: 1;
        border: round $secondary;
    }
    """

    def __init__(
        self,
        pattern: PatternInfo | None = None,
        cantrip: CantripsInfo | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._pattern = pattern
        self._cantrip = cantrip

    def on_mount(self) -> None:
        """Set border title from pattern info."""
        if self._pattern:
            self.border_title = f"{self._pattern.category} / {self._pattern.name}"

    def _get_accent_color(self) -> str:
        """Get the theme's secondary color for accents."""
        try:
            theme = self.app.current_theme
            return theme.secondary or "cyan"
        except Exception:
            return "cyan"

    def render(self) -> str:
        """Render cantrip info."""
        if not self._pattern or not self._cantrip:
            return "[dim]No cantrip selected[/dim]"

        color = self._get_accent_color()
        lines = [
            f"[{color}]Cantrip {self._cantrip.number}:[/{color}] {self._cantrip.title}",
            "",
            f"Target: < {self._cantrip.target_time // 60}:{self._cantrip.target_time % 60:02d}",
            f"Difficulty: {self._cantrip.difficulty}",
        ]

        if self._cantrip.leetcode_id:
            lines.append(f"LeetCode: #{self._cantrip.leetcode_id}")

        return "\n".join(lines)


class PracticeScreen(Screen):
    """Screen for practicing a cantrip."""

    BINDINGS = [
        Binding("escape", "cancel", "Cancel"),
        Binding("e", "edit", "Edit"),
        Binding("t", "test", "Run Tests"),
        Binding("s", "save", "Save Session"),
    ]

    CSS = """
    PracticeScreen {
        background: $surface;
    }

    #practice-container {
        padding: 1 2;
    }

    #info-row {
        height: auto;
        margin-bottom: 1;
    }

    #info-panel {
        width: 2fr;
    }

    #timer-panel {
        width: 1fr;
        margin-left: 1;
    }

    #instructions {
        height: auto;
        padding: 1;
        border: round $primary;
        margin-bottom: 1;
    }

    #actions {
        height: auto;
        margin-top: 1;
    }

    Button {
        margin-right: 1;
    }
    """

    def __init__(
        self,
        pattern: PatternInfo,
        cantrip: CantripsInfo,
        db: Database | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.pattern = pattern
        self.cantrip = cantrip
        self.db = db
        self._timer_started = False
        self._test_passed = 0
        self._test_failed = 0

    def compose(self) -> ComposeResult:
        """Compose the practice screen."""
        yield Header()
        with Vertical(id="practice-container"):
            # Info and timer row
            with Horizontal(id="info-row"):
                yield CantripsInfoPanel(
                    pattern=self.pattern, cantrip=self.cantrip, id="info-panel"
                )
                yield TimerDisplay(
                    target_time=self.cantrip.target_time, id="timer-panel"
                )

            # Instructions
            yield Static(
                """1. Press [green]E[/green] to open your editor and start the timer
2. Write your solution from memory
3. Press [green]T[/green] to run tests when done
4. Press [green]S[/green] to save your session

[dim]Remember: Code from memory, no peeking![/dim]""",
                id="instructions",
            )

            # Test results (hidden initially)
            yield TestResultsPanel(id="test-results")

            # Action buttons
            with Horizontal(id="actions"):
                yield Button("Edit (E)", id="btn-edit", variant="primary", flat=True)
                yield Button("Test (T)", id="btn-test", variant="default", flat=True)
                yield Button("Save (S)", id="btn-save", variant="success", flat=True)
                yield Button("Cancel (Esc)", id="btn-cancel", variant="error", flat=True)

        yield Footer()

    def on_mount(self) -> None:
        """Set up screen on mount.

        - Set border title on instructions panel
        - Focus instructions to prevent accidental button clicks
        """
        try:
            instructions = self.query_one("#instructions")
            instructions.border_title = "Practice Flow"
            instructions.focus()
        except Exception:
            pass  # Not critical if this fails

    def action_edit(self) -> None:
        """Open the cantrip file in editor."""
        if not self.cantrip.file_path:
            self.notify("No file path for this cantrip", severity="error")
            return

        if not self.cantrip.file_path.exists():
            self.notify(f"File not found: {self.cantrip.file_path}", severity="error")
            return

        # Start timer if not started
        try:
            timer = self.query_one("#timer-panel", TimerDisplay)
            if not self._timer_started:
                timer.start()
                self._timer_started = True
        except Exception as e:
            self.notify(f"Timer error: {e}", severity="error")
            return

        # Get editor from environment
        editor = os.environ.get("EDITOR", "vim")

        # Suspend TUI and open editor
        try:
            with self.app.suspend():
                result = subprocess.run(
                    [editor, str(self.cantrip.file_path)],
                    check=False,
                )
                if result.returncode != 0:
                    self.notify(
                        f"Editor exited with code {result.returncode}",
                        severity="warning",
                    )
        except FileNotFoundError:
            self.notify(f"Editor '{editor}' not found", severity="error")
            return
        except Exception as e:
            self.notify(f"Error opening editor: {e}", severity="error")
            return

        self.notify(f"Editor closed. Timer: {int(timer.get_elapsed())}s")

    def action_test(self) -> None:
        """Run tests for this cantrip."""
        if not self.cantrip.file_path:
            self.notify("No file path for this cantrip", severity="error")
            return

        self.notify("Running tests...")

        # Find test file
        test_file = self.cantrip.file_path.parent / "test_cantrips.py"
        if not test_file.exists():
            self.notify("No test file found", severity="error")
            return

        # Run pytest for this specific cantrip
        cantrip_marker = f"cantrip{self.cantrip.number}"
        try:
            result = subprocess.run(
                [
                    "uv", "run", "pytest",
                    str(test_file),
                    "-m", cantrip_marker,
                    "-v",
                    "--tb=short",
                    "-x",
                ],
                capture_output=True,
                text=True,
                cwd=self.cantrip.file_path.parent,
                timeout=30,  # Prevent hanging
            )
        except subprocess.TimeoutExpired:
            self.notify("Tests timed out after 30s", severity="error")
            return
        except Exception as e:
            self.notify(f"Error running tests: {e}", severity="error")
            return

        # Parse results
        output = result.stdout + result.stderr
        self._test_passed = output.count(" PASSED")
        self._test_failed = output.count(" FAILED") + output.count(" ERROR")

        # Update results panel
        try:
            results_panel = self.query_one("#test-results", TestResultsPanel)
            results_panel.set_results(output, self._test_passed, self._test_failed)
        except Exception as e:
            self.notify(f"Error displaying results: {e}", severity="error")

        if self._test_failed == 0 and self._test_passed > 0:
            self.notify("All tests passed!", severity="information")
        else:
            self.notify(
                f"{self._test_failed} tests failed", severity="warning"
            )

    def action_save(self) -> None:
        """Save the practice session."""
        timer = self.query_one("#timer-panel", TimerDisplay)
        elapsed = timer.stop()

        if not self._timer_started:
            self.notify("Start a session first (press E)", severity="warning")
            return

        if self.db:
            session = PracticeSession(
                pattern_name=f"{self.pattern.category}/{self.pattern.name}",
                cantrip_number=self.cantrip.number,
                date=date.today(),
                time_seconds=int(elapsed),
                bugs=self._test_failed,
            )
            self.db.log_session(session)
            self.notify(
                f"Session saved: {int(elapsed)}s, {self._test_failed} bugs",
                severity="information",
            )

        self.app.pop_screen()

    def action_cancel(self) -> None:
        """Cancel and return to previous screen."""
        timer = self.query_one("#timer-panel", TimerDisplay)
        timer.stop()
        self.app.pop_screen()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        button_id = event.button.id
        if button_id == "btn-edit":
            self.action_edit()
        elif button_id == "btn-test":
            self.action_test()
        elif button_id == "btn-save":
            self.action_save()
        elif button_id == "btn-cancel":
            self.action_cancel()
