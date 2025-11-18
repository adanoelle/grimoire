"""
Reset command - Reset kata implementations back to pass.

Resets all kata functions in kata.py to 'pass' while preserving:
- Function signatures
- Docstrings
- Mastery tracking section
"""

import re
import typer
from pathlib import Path
from typing import Optional

from ..utils.discovery import find_kata_pattern
from ..utils.rendering import console, print_error, print_success, print_warning
from ..domain import Result, Success, Failure, FileSystemError


def reset_kata_functions(content: str) -> str:
    """
    Reset all function implementations to 'pass' while preserving signatures and docstrings.

    Args:
        content: Original file content

    Returns:
        Modified content with functions reset to pass

    The strategy:
    1. Find each function definition (def ...)
    2. Identify its docstring (if any)
    3. Replace everything after the docstring with 'pass'
    4. Preserve proper indentation
    """
    lines = content.split("\n")
    result_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a function definition
        func_match = re.match(r"^def\s+\w+\([^)]*\)(?:\s*->\s*[^:]+)?:", line)

        if func_match:
            # This is a function definition - add it
            result_lines.append(line)
            i += 1

            # Get the indentation level of the function body
            # (should be 4 spaces more than the def line)
            def_indent = len(line) - len(line.lstrip())
            body_indent = def_indent + 4

            # Check if next line is a docstring
            if i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()

                if next_stripped.startswith('"""') or next_stripped.startswith("'''"):
                    # This is a docstring - preserve it entirely
                    docstring_delimiter = '"""' if '"""' in next_stripped else "'''"
                    result_lines.append(next_line)
                    i += 1

                    # Check if docstring ends on same line
                    if next_stripped.count(docstring_delimiter) >= 2:
                        # Single-line docstring - done, add pass
                        result_lines.append(" " * body_indent + "pass")
                    else:
                        # Multi-line docstring - copy until we find the closing delimiter
                        while i < len(lines):
                            docstring_line = lines[i]
                            result_lines.append(docstring_line)
                            i += 1
                            if docstring_delimiter in docstring_line:
                                # Found end of docstring
                                break

                        # Add pass after docstring
                        result_lines.append(" " * body_indent + "pass")

                    # Skip all remaining lines in this function body
                    # (until we hit a blank line, another def, or dedent)
                    while i < len(lines):
                        peek_line = lines[i]
                        peek_stripped = peek_line.strip()

                        # Stop if we hit:
                        # - A blank line followed by non-indented content
                        # - Another def at same or lower indentation
                        # - A line with less indentation than function body
                        # - Start of mastery section
                        if not peek_stripped:  # Blank line
                            # Peek ahead to see if next line is dedented
                            if i + 1 < len(lines):
                                next_peek = lines[i + 1]
                                next_indent = len(next_peek) - len(next_peek.lstrip())
                                if next_indent <= def_indent and next_peek.strip():
                                    # Next line is dedented and not blank - stop here
                                    break
                            i += 1
                            continue

                        peek_indent = len(peek_line) - len(peek_line.lstrip())

                        if peek_indent <= def_indent:
                            # Dedented - we're out of the function
                            break

                        if peek_line.startswith("def ") or peek_line.startswith("class "):
                            # Another definition - stop here
                            break

                        if "# =" in peek_line and "MASTERY TRACKING" in peek_line:
                            # Hit mastery section - stop
                            break

                        # Still inside function body - skip this line
                        i += 1

                else:
                    # No docstring - just add pass
                    result_lines.append(" " * body_indent + "pass")

                    # Skip the existing function body
                    while i < len(lines):
                        peek_line = lines[i]
                        peek_stripped = peek_line.strip()

                        if not peek_stripped:
                            if i + 1 < len(lines):
                                next_peek = lines[i + 1]
                                next_indent = len(next_peek) - len(next_peek.lstrip())
                                if next_indent <= def_indent and next_peek.strip():
                                    break
                            i += 1
                            continue

                        peek_indent = len(peek_line) - len(peek_line.lstrip())
                        if peek_indent <= def_indent:
                            break

                        i += 1

            # Add blank line after function
            result_lines.append("")

        else:
            # Not a function definition - preserve as-is
            result_lines.append(line)
            i += 1

    return "\n".join(result_lines)


def reset_pattern(
    pattern_name: str,
    force: bool = False,
    dry_run: bool = False,
):
    """
    Reset all kata functions in a pattern back to 'pass'.

    Args:
        pattern_name: Name of the pattern (e.g., "opposite_ends")
        force: Skip confirmation prompt
        dry_run: Show what would be changed without writing

    Raises:
        typer.Exit: If pattern not found or reset fails
    """
    # Find the pattern
    pattern_result = find_kata_pattern(pattern_name)

    if pattern_result.is_failure():
        error = pattern_result.error
        print_error(f"Pattern not found: {error.message}")
        raise typer.Exit(1)

    pattern = pattern_result.unwrap()
    kata_file = pattern.kata_file

    # Read current content
    try:
        content = kata_file.read_text()
    except Exception as e:
        print_error(f"Could not read {kata_file.name}: {e}")
        raise typer.Exit(1)

    # Reset functions
    reset_content = reset_kata_functions(content)

    # Check if anything changed
    if content == reset_content:
        console.print(f"\n[yellow]No changes needed - {pattern.display_name} is already reset.[/yellow]\n")
        return

    # Show diff in dry-run mode
    if dry_run:
        console.print(f"\n[bold cyan]Dry run - changes that would be made to {pattern.display_name}:[/bold cyan]\n")
        console.print("[dim]Functions would be reset to 'pass' (docstrings preserved)[/dim]\n")
        return

    # Confirm unless force flag set
    if not force:
        console.print(f"\n[bold yellow]⚠️  This will reset all kata functions in {pattern.display_name} to 'pass'[/bold yellow]")
        console.print("[dim]Docstrings and mastery tracking will be preserved.[/dim]\n")

        confirm = typer.confirm("Continue?", default=False)
        if not confirm:
            console.print("[dim]Reset cancelled.[/dim]\n")
            raise typer.Exit(0)

    # Create backup before writing
    backup_file = kata_file.with_suffix('.kata.backup')
    try:
        backup_file.write_text(content)
    except Exception as e:
        console.print(f"[yellow]Warning: Could not create backup: {e}[/yellow]")
        # Continue anyway - backup is nice-to-have, not critical

    # Write the reset content
    try:
        kata_file.write_text(reset_content)
        print_success(f"✓ Reset {pattern.display_name} - all kata functions now return 'pass'")
        console.print(f"[dim]File: {kata_file}[/dim]")
        console.print(f"[dim]Backup: {backup_file}[/dim]\n")
    except Exception as e:
        print_error(f"Could not write to {kata_file.name}: {e}")
        raise typer.Exit(1)


def reset_all_patterns(
    force: bool = False,
    dry_run: bool = False,
):
    """
    Reset all kata patterns back to 'pass'.

    Args:
        force: Skip confirmation prompt
        dry_run: Show what would be changed without writing

    Raises:
        typer.Exit: If no patterns found or reset fails
    """
    from ..utils.discovery import find_all_kata_patterns

    patterns = find_all_kata_patterns()

    if not patterns:
        print_error("No kata patterns found.")
        raise typer.Exit(1)

    console.print(f"\n[bold yellow]⚠️  This will reset ALL {len(patterns)} kata patterns to 'pass'[/bold yellow]")
    console.print("[dim]Docstrings and mastery tracking will be preserved.[/dim]\n")

    if dry_run:
        console.print("[bold cyan]Dry run mode - no files will be modified[/bold cyan]\n")
        for pattern in patterns:
            console.print(f"  • {pattern.display_name}")
        console.print()
        return

    if not force:
        confirm = typer.confirm("Are you sure you want to reset ALL patterns?", default=False)
        if not confirm:
            console.print("[dim]Reset cancelled.[/dim]\n")
            raise typer.Exit(0)

    # Reset each pattern
    reset_count = 0
    for pattern in patterns:
        try:
            content = pattern.kata_file.read_text()
            reset_content = reset_kata_functions(content)

            if content != reset_content:
                pattern.kata_file.write_text(reset_content)
                console.print(f"  ✓ Reset {pattern.display_name}")
                reset_count += 1
            else:
                console.print(f"  − {pattern.display_name} (already reset)")

        except Exception as e:
            print_warning(f"  ✗ Failed to reset {pattern.display_name}: {e}")
            continue

    console.print()
    print_success(f"✓ Reset {reset_count}/{len(patterns)} patterns")
    console.print()


def undo_reset_pattern(pattern_name: str):
    """
    Undo the last reset by restoring from backup file.

    Args:
        pattern_name: Pattern to undo (e.g., 'opposite_ends' or 'two_pointers/opposite_ends')
    """
    # Find the pattern
    pattern_result = find_kata_pattern(pattern_name)

    if not pattern_result.is_success():
        print_error(f"Pattern not found: {pattern_name}")
        print_info("Available patterns:")
        for p in find_all_kata_patterns():
            console.print(f"  • {p.name}")
        console.print()
        raise typer.Exit(1)

    pattern = pattern_result.unwrap()
    kata_file = pattern.kata_file
    backup_file = kata_file.with_suffix('.kata.backup')

    # Check if backup exists
    if not backup_file.exists():
        print_error(f"No backup found for {pattern.display_name}")
        console.print(f"[dim]Expected backup at: {backup_file}[/dim]\n")
        console.print("[yellow]Backups are created when you reset a kata.[/yellow]")
        console.print("[dim]Run 'runes kata reset <pattern>' to create a backup.[/dim]\n")
        raise typer.Exit(1)

    # Read backup content
    try:
        backup_content = backup_file.read_text()
    except Exception as e:
        print_error(f"Could not read backup file: {e}")
        raise typer.Exit(1)

    # Show confirmation
    console.print(f"\n[bold yellow]⚠️  This will restore {pattern.display_name} from backup[/bold yellow]")
    console.print(f"[dim]This will overwrite any current work in {kata_file.name}[/dim]\n")

    confirm = typer.confirm("Continue?", default=False)
    if not confirm:
        console.print("[dim]Undo cancelled.[/dim]\n")
        raise typer.Exit(0)

    # Restore from backup
    try:
        kata_file.write_text(backup_content)
        print_success(f"✓ Restored {pattern.display_name} from backup")
        console.print(f"[dim]File: {kata_file}[/dim]\n")
    except Exception as e:
        print_error(f"Could not restore from backup: {e}")
        raise typer.Exit(1)
