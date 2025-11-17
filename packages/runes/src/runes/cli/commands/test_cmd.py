"""
Test command - Run pytest tests for kata patterns.

Execute tests for a specific pattern, optionally filtering by kata number.
"""

import subprocess
import typer
from pathlib import Path
from typing import Optional

from ..utils.discovery import find_kata_pattern
from ..utils.rendering import console, print_error, print_success, print_warning


def run_tests(
    pattern_name: str,
    kata_number: Optional[int] = None,
    verbose: bool = False,
):
    """
    Run pytest tests for a kata pattern.

    Args:
        pattern_name: Name of the pattern (e.g., "opposite_ends", "binary_search")
        kata_number: Optional specific kata to test (1, 2, 3, etc.)
        verbose: Show verbose pytest output

    Raises:
        typer.Exit: If pattern not found or no tests available
    """
    # Find the pattern
    pattern_result = find_kata_pattern(pattern_name)

    if pattern_result.is_failure():
        error = pattern_result.error
        print_error(f"Pattern not found: {error.message}")
        raise typer.Exit(1)

    pattern = pattern_result.unwrap()

    # Check if pattern has pytest tests
    if not pattern.has_pytest:
        print_error(
            f"Pattern '{pattern.display_name}' doesn't have pytest tests yet.\n"
            f"Legacy patterns use doctest. Run: python {pattern.kata_file.name}"
        )
        raise typer.Exit(1)

    # Build pytest command
    test_file = pattern.test_file
    pytest_args = ["pytest"]

    # Add test file path
    pytest_args.append(str(test_file))

    # Filter by kata number if specified
    if kata_number:
        # Use pytest mark to filter: -m kata1, -m kata2, etc.
        pytest_args.extend(["-m", f"kata{kata_number}"])
        console.print(f"\n[bold cyan]Running tests for Kata {kata_number}...[/bold cyan]\n")
    else:
        console.print(f"\n[bold cyan]Running all tests for {pattern.display_name}...[/bold cyan]\n")

    # Add verbosity if requested
    if verbose:
        pytest_args.append("-v")
    else:
        # Use concise output by default
        pytest_args.append("-q")

    # Add color output
    pytest_args.append("--color=yes")

    # Change to pattern directory (so pytest can find imports)
    original_cwd = Path.cwd()
    try:
        # Run pytest
        result = subprocess.run(
            pytest_args,
            cwd=pattern.path,
            capture_output=False,  # Show output directly
        )

        # Print summary based on exit code
        console.print()
        if result.returncode == 0:
            print_success("✓ All tests passed!")
        elif result.returncode == 1:
            print_error("✗ Some tests failed")
            raise typer.Exit(1)
        elif result.returncode == 2:
            print_error("✗ Test execution was interrupted")
            raise typer.Exit(1)
        elif result.returncode == 5:
            print_warning("No tests were collected")
        else:
            print_error(f"✗ pytest exited with code {result.returncode}")
            raise typer.Exit(1)

    except FileNotFoundError:
        print_error(
            "pytest not found. Install it with:\n"
            "  uv add pytest  # or pip install pytest"
        )
        raise typer.Exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Tests interrupted by user[/yellow]")
        raise typer.Exit(130)
    finally:
        # Restore working directory (though this doesn't matter for CLI)
        pass


def run_all_tests(verbose: bool = False):
    """
    Run all pytest tests for all migrated patterns.

    Args:
        verbose: Show verbose pytest output

    Raises:
        typer.Exit: If no migrated patterns found
    """
    from ..utils.discovery import find_all_kata_patterns

    patterns = find_all_kata_patterns()
    migrated = [p for p in patterns if p.has_pytest]

    if not migrated:
        print_error("No migrated patterns with pytest tests found.")
        raise typer.Exit(1)

    console.print(f"\n[bold cyan]Running tests for {len(migrated)} migrated patterns...[/bold cyan]\n")

    # Build pytest command to run all test_kata.py files
    pytest_args = ["pytest"]

    # Add all test files
    for pattern in migrated:
        pytest_args.append(str(pattern.test_file))

    # Add verbosity
    if verbose:
        pytest_args.append("-v")
    else:
        pytest_args.append("-q")

    # Add color output
    pytest_args.append("--color=yes")

    # Run from algorithms directory
    from ..utils.discovery import get_algorithms_dir
    algorithms_dir = get_algorithms_dir()

    try:
        result = subprocess.run(
            pytest_args,
            cwd=algorithms_dir,
            capture_output=False,
        )

        console.print()
        if result.returncode == 0:
            print_success("✓ All tests passed!")
        elif result.returncode == 1:
            print_error("✗ Some tests failed")
            raise typer.Exit(1)
        else:
            print_error(f"✗ pytest exited with code {result.returncode}")
            raise typer.Exit(1)

    except FileNotFoundError:
        print_error("pytest not found. Install it with: uv add pytest")
        raise typer.Exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Tests interrupted by user[/yellow]")
        raise typer.Exit(130)
