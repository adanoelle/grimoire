"""Browser screen for navigating cantrip patterns.

Provides a tree view with:
- Collapsible categories and patterns
- Cantrip details with status indicators
- Fuzzy search capability
"""

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Vertical, Horizontal
from textual.message import Message
from textual.screen import Screen
from textual.widgets import (
    Footer,
    Header,
    Input,
    Static,
    Tree,
)

from cantrips.data import Database
from cantrips.utils.discovery import discover_patterns, PatternInfo, CantripsInfo


class OpenPracticeScreen(Message):
    """Message posted only when Enter is pressed on a cantrip (not on click)."""
    pass


class PatternTree(Tree):
    """Tree widget for browsing patterns."""

    BORDER_TITLE = "Patterns"

    DEFAULT_CSS = """
    PatternTree {
        height: 1fr;
        border: round $primary;
        padding: 1;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__("Cantrip Patterns", **kwargs)
        self.db = db
        self._patterns: list[PatternInfo] = []
        self._cantrip_nodes: dict[str, tuple[PatternInfo, CantripsInfo]] = {}

    BINDINGS = [
        Binding("enter", "open_practice", "Practice", priority=True),
    ]

    def action_select_cursor(self) -> None:
        """Override to ONLY toggle parent nodes, never open practice screen.

        This gets called by both clicks and Enter (Tree's default behavior).
        We neuter it for leaf nodes - Enter is handled by our custom binding.
        """
        if not self.cursor_node:
            return

        # Non-leaf nodes (categories, patterns): toggle expand/collapse
        if self.cursor_node.children:
            self.cursor_node.toggle()
        # Leaf nodes: do nothing here (handled by action_open_practice)

    def action_open_practice(self) -> None:
        """Handle Enter key on leaf nodes - open practice screen.

        This is bound with priority=True so it fires before action_select_cursor.
        """
        if not self.cursor_node:
            return

        # Only open practice for leaf nodes (cantrips)
        if not self.cursor_node.children:
            self.post_message(OpenPracticeScreen())

    def on_mount(self) -> None:
        """Load patterns when mounted."""
        self.load_patterns()

    def _get_category_color(self) -> str:
        """Get the theme's secondary color for category labels."""
        try:
            theme = self.app.current_theme
            # Use secondary color, fallback to cyan if not set
            return theme.secondary or "cyan"
        except Exception:
            return "cyan"

    def load_patterns(self, filter_text: str = "") -> None:
        """Load patterns into tree."""
        self.clear()
        self._patterns = discover_patterns()
        self._cantrip_nodes = {}

        # Get theme color for categories
        category_color = self._get_category_color()

        # Group by category
        categories: dict[str, list[PatternInfo]] = {}
        for pattern in self._patterns:
            if pattern.category not in categories:
                categories[pattern.category] = []
            categories[pattern.category].append(pattern)

        # Build tree
        for category_name in sorted(categories.keys()):
            category_patterns = categories[category_name]

            # Apply filter
            if filter_text:
                category_patterns = [
                    p
                    for p in category_patterns
                    if filter_text.lower() in p.name.lower()
                    or filter_text.lower() in category_name.lower()
                    or any(
                        filter_text.lower() in c.title.lower()
                        for c in p.cantrips
                    )
                ]
                if not category_patterns:
                    continue

            # Add category node with theme color
            display_name = category_name.replace("_", " ").title()
            category_node = self.root.add(
                f"[bold {category_color}]{display_name}[/bold {category_color}]",
                expand=True,
            )

            for pattern in category_patterns:
                # Get status indicator
                status = self._get_pattern_status(pattern)
                pattern_label = f"{pattern.display_name} {status}"
                pattern_node = category_node.add(pattern_label, expand=False)

                # Add cantrips under pattern
                for cantrip in pattern.cantrips:
                    cantrip_status = self._get_cantrip_status(pattern, cantrip)
                    cantrip_label = (
                        f"{cantrip.number}. {cantrip.title[:40]} {cantrip_status}"
                    )
                    node = pattern_node.add_leaf(cantrip_label)
                    # Store reference for selection
                    node_id = str(id(node))
                    self._cantrip_nodes[node_id] = (pattern, cantrip)

        self.root.expand()

    def _get_pattern_status(self, pattern: PatternInfo) -> str:
        """Get status indicator for pattern."""
        if not self.db:
            return "[dim]○[/dim]"

        try:
            progress = self.db.get_pattern_progress(
                f"{pattern.category}/{pattern.name}"
            )
            if progress:
                return f"[{progress.mastery_status.color}]{progress.mastery_status.symbol}[/{progress.mastery_status.color}]"
        except Exception:
            pass
        return "[dim]○[/dim]"

    def _get_cantrip_status(
        self, pattern: PatternInfo, cantrip: CantripsInfo
    ) -> str:
        """Get status indicator for cantrip."""
        if not self.db:
            return "[dim]--[/dim]"

        try:
            progress = self.db.get_pattern_progress(
                f"{pattern.category}/{pattern.name}"
            )
            if progress and cantrip.number in progress.best_times:
                best_time = progress.best_times[cantrip.number]
                minutes = best_time // 60
                seconds = best_time % 60
                if best_time <= cantrip.target_time:
                    return f"[green]✓ {minutes}:{seconds:02d}[/green]"
                else:
                    return f"[yellow]{minutes}:{seconds:02d}[/yellow]"
        except Exception:
            pass
        return "[dim]--[/dim]"

    def get_selected_cantrip(self) -> tuple[PatternInfo, CantripsInfo] | None:
        """Get currently selected cantrip."""
        if self.cursor_node:
            node_id = str(id(self.cursor_node))
            return self._cantrip_nodes.get(node_id)
        return None


class CantripsPreview(Static):
    """Preview panel for selected cantrip."""

    BORDER_TITLE = "Preview"

    DEFAULT_CSS = """
    CantripsPreview {
        height: auto;
        min-height: 10;
        padding: 1;
        border: round $secondary;
    }
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._pattern: PatternInfo | None = None
        self._cantrip: CantripsInfo | None = None

    def set_cantrip(
        self, pattern: PatternInfo | None, cantrip: CantripsInfo | None
    ) -> None:
        """Set the cantrip to preview."""
        self._pattern = pattern
        self._cantrip = cantrip
        # Update border title dynamically
        if pattern and cantrip:
            self.border_title = f"{pattern.category}/{pattern.name}"
        else:
            self.border_title = "Preview"
        self.refresh()

    def render(self) -> str:
        """Render preview."""
        if not self._pattern or not self._cantrip:
            return "[dim]Select a cantrip to preview[/dim]"

        lines = [
            f"[bold]Cantrip {self._cantrip.number}:[/bold] {self._cantrip.title}",
            "",
            f"Target: < {self._cantrip.target_time // 60}:{self._cantrip.target_time % 60:02d}",
            f"Difficulty: {self._cantrip.difficulty}",
        ]

        if self._cantrip.leetcode_id:
            lines.append(f"LeetCode: #{self._cantrip.leetcode_id}")

        if self._cantrip.file_path:
            lines.append("")
            lines.append(f"[dim]File: {self._cantrip.file_path.name}[/dim]")

        lines.append("")
        lines.append("[green]Press Enter to practice[/green]")

        return "\n".join(lines)


class BrowserScreen(Screen):
    """Screen for browsing cantrip patterns."""

    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("/", "search", "Search"),
    ]

    CSS = """
    BrowserScreen {
        background: $surface;
    }

    #browser-container {
        padding: 1 2;
    }

    #search-container {
        height: auto;
        margin-bottom: 1;
    }

    #search-input {
        width: 100%;
        border: round $primary;
    }

    #main-content {
        height: 1fr;
    }

    #tree-container {
        width: 2fr;
    }

    #preview-container {
        width: 1fr;
        margin-left: 1;
    }
    """

    # Widget IDs as constants
    ID_PATTERN_TREE = "pattern-tree"
    ID_PREVIEW = "cantrip-preview"
    ID_SEARCH = "search-input"

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db

    def compose(self) -> ComposeResult:
        """Compose the browser screen."""
        yield Header()
        with Vertical(id="browser-container"):
            # Search bar
            with Container(id="search-container"):
                yield Input(placeholder="Search patterns...", id=self.ID_SEARCH)

            # Main content: tree + preview
            with Horizontal(id="main-content"):
                with Container(id="tree-container"):
                    yield PatternTree(db=self.db, id=self.ID_PATTERN_TREE)
                with Container(id="preview-container"):
                    yield CantripsPreview(id=self.ID_PREVIEW)

        yield Footer()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle search input changes."""
        if event.input.id == self.ID_SEARCH:
            try:
                tree = self.query_one(f"#{self.ID_PATTERN_TREE}", PatternTree)
                tree.load_patterns(filter_text=event.value)
            except Exception as e:
                self.notify(f"Search error: {e}", severity="error")

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        """Handle tree node highlight - update preview on navigation."""
        try:
            tree = self.query_one(f"#{self.ID_PATTERN_TREE}", PatternTree)
            result = tree.get_selected_cantrip()
            preview = self.query_one(f"#{self.ID_PREVIEW}", CantripsPreview)

            if result:
                pattern, cantrip = result
                preview.set_cantrip(pattern, cantrip)
            else:
                preview.set_cantrip(None, None)
        except Exception as e:
            self.notify(f"Preview error: {e}", severity="error")

    def on_open_practice_screen(self, event: OpenPracticeScreen) -> None:
        """Handle Enter key on cantrip - open practice screen.

        This message is only posted from action_select_cursor (Enter key),
        never from clicks, ensuring click = preview only.
        """
        try:
            tree = self.query_one(f"#{self.ID_PATTERN_TREE}", PatternTree)
            result = tree.get_selected_cantrip()

            if result:
                from .practice import PracticeScreen

                pattern, cantrip = result
                self.app.push_screen(PracticeScreen(pattern, cantrip, db=self.db))
        except Exception as e:
            self.notify(f"Error opening practice screen: {e}", severity="error")

    def action_back(self) -> None:
        """Go back to dashboard."""
        self.app.pop_screen()

    def action_search(self) -> None:
        """Focus the search input."""
        try:
            self.query_one(f"#{self.ID_SEARCH}", Input).focus()
        except Exception as e:
            self.notify(f"Error focusing search: {e}", severity="error")
