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
from textual.screen import Screen, ModalScreen
from textual.widgets import Button, Footer, Header, Label, Static, TextArea
from textual.reactive import reactive

from cantrips.data import Database, PracticeSession
from cantrips.data.models import CantripsHints
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
    """

    def __init__(self, **kwargs) -> None:
        super().__init__("[dim]No test results yet[/dim]", **kwargs)

    def _extract_description(self, test_line: str) -> str:
        """Extract just the description from a pytest test line."""
        import re
        match = re.search(r'\[([^\]]+)\]', test_line)
        if match:
            return match.group(1)
        if "::" in test_line:
            name = test_line.split("::")[-1]
            name = re.sub(r'\s+(PASSED|FAILED).*$', '', name)
            return name
        return test_line.split()[0] if test_line else "unknown"

    def set_results(self, output: str, passed: int, failed: int) -> None:
        """Set test results using update() instead of render()."""
        # Update border title
        total = passed + failed
        if failed == 0:
            self.border_title = f"Test Results [green]✓ {passed}/{total}[/green]"
        else:
            self.border_title = f"Test Results [red]✗ {passed}/{total}[/red]"

        # Parse and format results
        lines = []
        in_failure_block = False

        for line in output.split("\n"):
            stripped = line.strip()

            if "FAILURES" in stripped and stripped.startswith("="):
                in_failure_block = True
                continue
            if stripped.startswith("=") and in_failure_block:
                in_failure_block = False
                continue

            if not stripped or stripped.startswith("=") or stripped.startswith("-"):
                continue
            if any(skip in stripped for skip in [
                "platform ", "rootdir:", "cachedir:", "configfile:",
                "hypothesis profile", "plugins:", "collecting", "collected",
                "-- Docs:", "warnings summary", "PytestUnknownMarkWarning",
                "PytestConfigWarning", "short test summary"
            ]):
                continue
            if stripped.endswith("s") and (" passed" in stripped or " failed" in stripped):
                if "in " in stripped and "selected" not in stripped:
                    continue

            if " PASSED" in stripped:
                desc = self._extract_description(stripped)
                lines.append(f"[green]✓[/green] {desc}")
            elif " FAILED" in stripped:
                desc = self._extract_description(stripped)
                lines.append(f"[red]✗[/red] {desc}")
            elif in_failure_block:
                if stripped.startswith("E "):
                    lines.append(f"    [red]{stripped}[/red]")
                elif stripped.startswith(">"):
                    lines.append(f"    [yellow]{stripped}[/yellow]")
                elif "assert" in stripped.lower() or "=" in stripped:
                    lines.append(f"    [dim]{stripped}[/dim]")

        # Use update() to set content - this is the key!
        content = "\n".join(lines[:50]) if lines else "[dim]No test results[/dim]"
        self.update(content)


class HintPanel(Static):
    """Collapsible panel for progressive hints.

    Provides three levels of hints that can be revealed progressively:
        - Level 1: Pattern name only
        - Level 2: Pattern name + approach steps
        - Level 3: Full hints including edge cases

    Press H to cycle through levels (hidden -> 1 -> 2 -> 3 -> hidden).
    """

    DEFAULT_CSS = """
    HintPanel {
        height: auto;
        max-height: 15;
        padding: 1;
        border: round $warning;
        margin-top: 1;
        display: none;
    }

    HintPanel.visible {
        display: block;
    }
    """

    hint_level: reactive[int] = reactive(0)  # 0=hidden, 1-3=levels

    def __init__(self, hints: CantripsHints | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self._hints = hints or CantripsHints()

    def on_mount(self) -> None:
        """Set initial border title."""
        self.border_title = "Hints [H to show]"

    def advance_level(self) -> None:
        """Advance to next hint level (cycles 0 -> 1 -> 2 -> 3 -> 0)."""
        self.hint_level = (self.hint_level + 1) % 4
        if self.hint_level == 0:
            self.remove_class("visible")
            self.border_title = "Hints [H to show]"
        else:
            self.add_class("visible")
            self.border_title = f"Hints [Level {self.hint_level}/3]"
        self._update_content()

    def _update_content(self) -> None:
        """Update the displayed hint content based on level."""
        if self.hint_level == 0:
            content = ""
        elif self.hint_level == 1:
            content = self._hints.level_1 or "[dim]No pattern hint available[/dim]"
        elif self.hint_level == 2:
            content = self._hints.level_2 or "[dim]No approach hints available[/dim]"
        else:  # level 3
            content = self._hints.level_3 or "[dim]No edge case hints available[/dim]"
        self.update(content)

    def has_hints(self) -> bool:
        """Check if hints are available."""
        return self._hints.has_hints()


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


class NotesInputModal(ModalScreen[PracticeSession | None]):
    """Modal screen for entering session notes before saving.

    Shows session stats (time, bugs) and allows entering notes.
    Returns the PracticeSession with notes filled in, or None if cancelled.
    """

    CSS = """
    NotesInputModal {
        align: center middle;
    }

    #notes-dialog {
        width: 70;
        height: auto;
        max-height: 30;
        padding: 1 2;
        border: round $primary;
        background: $surface;
    }

    #notes-header {
        text-align: center;
        margin-bottom: 1;
    }

    #session-stats {
        margin-bottom: 1;
        padding: 1;
        border: round $secondary;
    }

    #notes-input {
        height: 6;
        margin-top: 1;
        margin-bottom: 1;
    }

    #previous-note-preview {
        margin-bottom: 1;
        max-height: 4;
    }

    #notes-buttons {
        height: auto;
        align: center middle;
    }

    #notes-buttons Button {
        margin: 0 1;
    }
    """

    BINDINGS = [
        Binding("escape", "cancel", "Cancel"),
        Binding("ctrl+s", "save", "Save", priority=True),
    ]

    def __init__(
        self,
        session: PracticeSession,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.session = session

    def compose(self) -> ComposeResult:
        with Container(id="notes-dialog"):
            yield Static(
                "[bold]Save Practice Session[/bold]",
                id="notes-header",
            )

            # Session stats
            time_display = f"{self.session.time_seconds // 60}:{self.session.time_seconds % 60:02d}"
            bugs_color = "green" if self.session.bugs == 0 else "red"
            yield Static(
                f"⏱️  Time: [cyan]{time_display}[/cyan]   |   "
                f"🐛 Bugs: [{bugs_color}]{self.session.bugs}[/{bugs_color}]",
                id="session-stats",
            )

            # Notes input
            yield TextArea(
                placeholder="What did you learn? Any bugs to remember? (optional)",
                id="notes-input",
            )

            # Buttons
            with Horizontal(id="notes-buttons"):
                yield Button("Save (Ctrl+S)", id="btn-save", variant="primary")
                yield Button("Skip Notes", id="btn-skip", variant="default")

    def on_mount(self) -> None:
        """Focus the notes input on mount."""
        try:
            self.query_one("#notes-input", TextArea).focus()
        except Exception:
            pass

    def action_save(self) -> None:
        """Save with notes and dismiss."""
        try:
            notes_input = self.query_one("#notes-input", TextArea)
            self.session.notes = notes_input.text
        except Exception:
            pass
        self.dismiss(self.session)

    def action_cancel(self) -> None:
        """Cancel and dismiss without saving."""
        self.dismiss(None)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "btn-save":
            self.action_save()
        elif event.button.id == "btn-skip":
            # Save without notes
            self.dismiss(self.session)


class PracticeScreen(Screen):
    """Screen for practicing a cantrip."""

    BINDINGS = [
        Binding("escape", "cancel", "Cancel"),
        Binding("e", "edit", "Edit"),
        Binding("t", "test", "Run Tests"),
        Binding("s", "save", "Save Session"),
        Binding("h", "toggle_hints", "Hints"),
        Binding("n", "show_notes", "Notes"),
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
        self._strategy_notes: str = ""  # Loaded from .notes.md file on mount

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

            # Previous notes reminder (if any - updated on mount)
            yield Static("", id="previous-notes")

            # Instructions
            yield Static(
                """1. Press [green]E[/green] to open your editor and start the timer
2. Write your solution from memory
3. Press [green]T[/green] to run tests when done
4. Press [green]S[/green] to save your session
5. Press [yellow]H[/yellow] if you need hints (progressive reveal)

[dim]Remember: Code from memory, no peeking! Hints affect learning.[/dim]""",
                id="instructions",
            )

            # Hints panel (hidden by default)
            yield HintPanel(hints=self.cantrip.hints, id="hint-panel")

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
        - Load strategy notes from filesystem
        - Focus instructions to prevent accidental button clicks
        """
        try:
            instructions = self.query_one("#instructions")
            instructions.border_title = "Practice Flow"
            instructions.focus()
        except Exception:
            pass  # Not critical if this fails

        # Load strategy notes from .notes.md file
        self._load_strategy_notes()

    def _load_strategy_notes(self) -> None:
        """Load strategy notes from the .notes.md file."""
        if not self.cantrip.file_path:
            return

        notes_path = self.cantrip.file_path.with_suffix(".notes.md")
        if notes_path.exists():
            try:
                self._strategy_notes = notes_path.read_text()
                notes_widget = self.query_one("#previous-notes", Static)
                # Show first non-header line as preview
                lines = [l for l in self._strategy_notes.split("\n")
                        if l.strip() and not l.startswith("#")]
                if lines:
                    preview = lines[0][:80]
                    if len(lines[0]) > 80:
                        preview += "..."
                    notes_widget.update(f"[dim]📝 Notes: {preview} [N to edit][/dim]")
                else:
                    notes_widget.update("[dim]📝 Notes file exists [N to edit][/dim]")
            except Exception:
                pass
        else:
            try:
                notes_widget = self.query_one("#previous-notes", Static)
                notes_widget.update("[dim]Press [yellow]N[/yellow] to create strategy notes[/dim]")
            except Exception:
                pass

    def action_toggle_hints(self) -> None:
        """Toggle hint visibility and advance level."""
        try:
            hint_panel = self.query_one("#hint-panel", HintPanel)
            hint_panel.advance_level()

            if hint_panel.hint_level > 0:
                self.notify(f"Hint level {hint_panel.hint_level}/3", severity="information")
        except Exception as e:
            self.notify(f"Hint error: {e}", severity="error")

    def action_show_notes(self) -> None:
        """Open strategy notes file in editor."""
        if not self.cantrip.file_path:
            self.notify("No file path for this cantrip", severity="error")
            return

        # Strategy notes live next to the cantrip file
        notes_path = self.cantrip.file_path.with_suffix(".notes.md")

        # Create with template if doesn't exist
        if not notes_path.exists():
            template = f"""# {self.cantrip.title}

## Strategy


## Key Insights


## Common Mistakes

"""
            notes_path.write_text(template)
            self.notify("Created new notes file", severity="information")

        # Open in editor
        editor = os.environ.get("EDITOR", "vim")
        try:
            with self.app.suspend():
                subprocess.run([editor, str(notes_path)], check=False)
        except Exception as e:
            self.notify(f"Error opening editor: {e}", severity="error")
            return

        # Reload notes after editing
        self._load_strategy_notes()
        self.notify("Notes saved", severity="information")

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

        # Find test file and determine marker style
        # cantrips package: test_cantrips.py with cantrip{n} markers
        # runes package: test_kata.py with kata{n} markers
        test_file = self.cantrip.file_path.parent / "test_cantrips.py"
        marker = f"cantrip{self.cantrip.number}"
        if not test_file.exists():
            test_file = self.cantrip.file_path.parent / "test_kata.py"
            marker = f"kata{self.cantrip.number}"
        if not test_file.exists():
            self.notify("No test file found", severity="error")
            return
        try:
            result = subprocess.run(
                [
                    "uv", "run", "pytest",
                    str(test_file),
                    "-m", marker,
                    "-vv",
                    "--tb=short",
                    "-W", "ignore",  # Suppress warnings
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
        """Save the practice session with optional notes."""
        timer = self.query_one("#timer-panel", TimerDisplay)
        elapsed = timer.stop()

        if not self._timer_started:
            self.notify("Start a session first (press E)", severity="warning")
            return

        # Create session object
        pattern_name = f"{self.pattern.category}/{self.pattern.name}"
        session = PracticeSession(
            pattern_name=pattern_name,
            cantrip_number=self.cantrip.number,
            date=date.today(),
            time_seconds=int(elapsed),
            bugs=self._test_failed,
        )

        def handle_notes_result(result: PracticeSession | None) -> None:
            """Handle the result from the notes modal."""
            if result is None:
                # User cancelled - restart timer and stay on screen
                timer.start()
                self.notify("Save cancelled", severity="information")
                return

            if self.db:
                # Save the session (notes stored in sessions table)
                self.db.log_session(result)

                self.notify(
                    f"Session saved: {int(elapsed)}s, {self._test_failed} bugs",
                    severity="information",
                )

            self.app.pop_screen()

        # Push the notes modal
        self.app.push_screen(
            NotesInputModal(session),
            callback=handle_notes_result,
        )

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
