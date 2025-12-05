"""Custom themes for cantrips TUI.

Themes are registered in the app and can be switched via Command Palette (Ctrl+P).
"""

from textual.theme import Theme


# Christmas theme - festive red and green with gold accents
CHRISTMAS = Theme(
    name="christmas",
    primary="#c41e3a",       # Christmas red (candy cane)
    secondary="#228b22",     # Forest green (tree)
    accent="#ffd700",        # Gold (ornaments/star)
    foreground="#f5f5f5",    # Snow white text
    background="#1a1a2e",    # Dark night sky
    success="#228b22",       # Green for success
    warning="#ffd700",       # Gold for warnings
    error="#c41e3a",         # Red for errors
    surface="#16213e",       # Darker blue-black
    panel="#0f3460",         # Deep blue panel
    dark=True,
    variables={
        "footer-key-foreground": "#ffd700",
        "block-cursor-text-style": "bold",
    },
)


# All custom themes to register
CUSTOM_THEMES = [
    CHRISTMAS,
]
