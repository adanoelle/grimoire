"""
Practice command - Guide user through kata practice session.

Interactive practice session with timer and result logging.
"""

import re
import typer
from pathlib import Path
from typing import Optional

from ..utils.discovery import find_kata_pattern
from ..utils.timer import PracticeTimer
from ..utils.mastery import append_practice_session
from ..utils.rendering import console, print_error, print_success, print_warning


def extract_kata_info(kata_file: Path, kata_number: int) -> Optional[dict]:
    """
    Extract information about a specific kata from kata.py.

    Args:
        kata_file: Path to kata.py
        kata_number: Kata number to extract info for

    Returns:
        Dict with: function_name, docstring, target_time
        Or None if kata not found
    """
    try:
        content = kata_file.read_text()
    except Exception:
        return None

    # Find the function that contains "KATA {kata_number}:"
    # Note: Handle return type annotations like "-> float:" between ) and :
    kata_pattern = rf"def\s+(\w+)\([^)]*\)[^:]*:.*?\"\"\".*?KATA\s+{kata_number}:([^\n]+).*?Target[^:]*:\s*([^\n]+).*?\"\"\""

    match = re.search(kata_pattern, content, re.DOTALL | re.IGNORECASE)

    if not match:
        return None

    function_name = match.group(1)
    kata_name = match.group(2).strip()
    target_time = match.group(3).strip()

    # Extract the full docstring for display
    # Find the function and its docstring
    func_start = content.find(f"def {function_name}(")
    if func_start == -1:
        return None

    # Find docstring
    docstring_start = content.find('"""', func_start)
    if docstring_start == -1:
        docstring_start = content.find("'''", func_start)
        delimiter = "'''"
    else:
        delimiter = '"""'

    if docstring_start == -1:
        return None

    docstring_end = content.find(delimiter, docstring_start + 3)
    if docstring_end == -1:
        return None

    docstring = content[docstring_start + 3:docstring_end].strip()

    return {
        "function_name": function_name,
        "kata_name": kata_name,
        "target_time": target_time,
        "docstring": docstring,
    }


def start_practice(
    pattern_name: str,
    kata_number: Optional[int] = None,
    skip_timer: bool = False,
):
    """
    Start an interactive practice session.

    Args:
        pattern_name: Name of the pattern (e.g., "opposite_ends")
        kata_number: Specific kata to practice (if None, ask user)
        skip_timer: Skip the interactive timer

    Raises:
        typer.Exit: If pattern not found or practice cancelled
    """
    # Find the pattern
    pattern_result = find_kata_pattern(pattern_name)

    if pattern_result.is_failure():
        error = pattern_result.error
        print_error(f"Pattern not found: {error.message}")
        raise typer.Exit(1)

    pattern = pattern_result.unwrap()

    # Header
    console.print(f"\n[bold magenta]🥋 {pattern.display_name} - Practice Session[/bold magenta]\n")

    # Ask for kata number if not provided
    if kata_number is None:
        kata_number = typer.prompt("Which kata do you want to practice? (e.g., 1, 2, 3)", type=int)

    # Extract kata info
    kata_info = extract_kata_info(pattern.kata_file, kata_number)

    if not kata_info:
        print_error(f"Kata {kata_number} not found in {pattern.display_name}")
        raise typer.Exit(1)

    # Display kata info
    console.print(f"[bold cyan]Kata {kata_number}: {kata_info['kata_name']}[/bold cyan]")
    console.print(f"[dim]Target time: {kata_info['target_time']}[/dim]")
    console.print(f"[dim]Function: {kata_info['function_name']}[/dim]\n")

    # Show docstring (first 10 lines to avoid spoilers)
    docstring_lines = kata_info["docstring"].split("\n")
    preview_lines = docstring_lines[:15]  # Show enough to see requirements
    console.print("[dim]" + "\n".join(preview_lines) + "[/dim]")
    if len(docstring_lines) > 15:
        console.print("[dim]...[/dim]")
    console.print()

    # Ready prompt
    ready = typer.confirm("Ready to start practicing?", default=True)
    if not ready:
        console.print("[dim]Practice cancelled.[/dim]\n")
        raise typer.Exit(0)

    # Start timer
    timer = PracticeTimer()

    if not skip_timer:
        console.print("\n[bold green]⏱️  Timer started![/bold green]")
        console.print(f"[dim]Open {pattern.kata_file.name} and code your solution.[/dim]")
        console.print(f"[dim]Run tests: runes kata test {pattern_name} -k {kata_number}[/dim]\n")
        timer.start()

        # Wait for user to finish
        typer.prompt("Press Enter when you're done...")
        timer.stop()

        console.print(f"\n[bold]Time elapsed: {timer.elapsed_formatted}[/bold]\n")
    else:
        # Manual entry mode
        time_input = typer.prompt("How long did it take? (e.g., 2:30)")
        timer.elapsed_str = time_input

    # Ask for bugs and notes
    bugs = typer.prompt("How many bugs did you encounter?", type=int, default=0)
    notes = typer.prompt("Notes (optional)", default="", show_default=False)

    # Log the session
    result = append_practice_session(
        pattern.kata_file,
        kata_number=kata_number,
        time_str=timer.elapsed_str if skip_timer else timer.elapsed_formatted,
        bugs=bugs,
        notes=notes,
    )

    if result.is_failure():
        error = result.error
        print_error(f"Could not log practice session: {error.message}")
        raise typer.Exit(1)

    # Success
    print_success(f"✓ Practice session logged to {pattern.display_name}!")
    console.print(f"\n[dim]View your progress: runes kata progress {pattern_name}[/dim]\n")


def quick_log(
    pattern_name: str,
    kata_number: int,
    time: str,
    bugs: int = 0,
    notes: str = "",
):
    """
    Quickly log a practice session without interactive prompts.

    Args:
        pattern_name: Name of the pattern
        kata_number: Kata number practiced
        time: Time taken (e.g., "2:30")
        bugs: Number of bugs encountered
        notes: Optional notes

    Raises:
        typer.Exit: If pattern not found or logging fails
    """
    # Find the pattern
    pattern_result = find_kata_pattern(pattern_name)

    if pattern_result.is_failure():
        error = pattern_result.error
        print_error(f"Pattern not found: {error.message}")
        raise typer.Exit(1)

    pattern = pattern_result.unwrap()

    # Log the session
    result = append_practice_session(
        pattern.kata_file,
        kata_number=kata_number,
        time_str=time,
        bugs=bugs,
        notes=notes,
    )

    if result.is_failure():
        error = result.error
        print_error(f"Could not log practice session: {error.message}")
        raise typer.Exit(1)

    # Success
    print_success(f"✓ Practice session logged!")
    console.print(f"[dim]{pattern.display_name} - Kata {kata_number} - {time} - {bugs} bugs[/dim]\n")
