#!/usr/bin/env python3
"""
reset_katas.py - Reset kata implementations to clean templates

Usage:
    python scripts/reset_katas.py                    # Reset all katas
    python scripts/reset_katas.py binary_search      # Reset specific pattern
    python scripts/reset_katas.py --dry-run          # Preview changes

This script resets all function implementations in kata.py files back to 'pass',
preserving docstrings, comments, and the practice log section.
"""

import re
import sys
from pathlib import Path
from typing import Tuple


def reset_function_implementations(content: str) -> Tuple[str, int]:
    """
    Reset all function implementations to 'pass'.

    Preserves:
    - Function signatures
    - Docstrings
    - Section comments
    - Practice logs
    - Test code

    Returns:
        Tuple of (new_content, number_of_functions_reset)
    """
    lines = content.split('\n')
    result = []
    i = 0
    reset_count = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a function definition
        if re.match(r'^def \w+\(', line):
            # Found a function definition
            indent = len(line) - len(line.lstrip())
            base_indent = ' ' * indent
            body_indent = ' ' * (indent + 4)

            # Add function definition line
            result.append(line)
            i += 1

            # Check for and preserve docstring
            if i < len(lines) and lines[i].strip().startswith('"""'):
                # Check if it's a one-line docstring
                if lines[i].count('"""') >= 2:
                    # One-line docstring like: """This is a docstring"""
                    result.append(lines[i])
                    i += 1
                else:
                    # Multi-line docstring
                    result.append(lines[i])
                    i += 1

                    # Continue until end of docstring (closing """)
                    while i < len(lines):
                        result.append(lines[i])
                        # Check if this line has the closing """
                        if '"""' in lines[i]:
                            i += 1
                            break
                        i += 1

            # Now skip the implementation until we hit:
            # - Another function at same/lower indent
            # - A section marker (# ====)
            # - if __name__
            # - End of file
            skipped_impl = False
            while i < len(lines):
                next_line = lines[i]
                next_indent = len(next_line) - len(next_line.lstrip())

                # Check if we've hit the end of this function
                if next_line.strip() == '':
                    # Empty line - could be end of function
                    # Look ahead to see what's next
                    if i + 1 < len(lines):
                        lookahead = lines[i + 1]
                        lookahead_indent = len(lookahead) - len(lookahead.lstrip())

                        # Next line is at same or lower indent and non-empty
                        if lookahead.strip() and lookahead_indent <= indent:
                            # End of function
                            break
                    i += 1
                    continue

                # Hit another def/class at same or lower indent
                if next_indent <= indent and (
                    next_line.lstrip().startswith('def ') or
                    next_line.lstrip().startswith('class ')
                ):
                    break

                # Hit section marker
                if next_line.strip().startswith('# ==='):
                    break

                # Hit if __name__
                if 'if __name__' in next_line:
                    break

                # Skip this line (part of old implementation)
                skipped_impl = True
                i += 1

            # Add 'pass' as the implementation
            if skipped_impl or i >= len(lines) or lines[i].strip() == '':
                result.append(f'{body_indent}pass')
                reset_count += 1

        else:
            # Not a function definition, keep as-is
            result.append(line)
            i += 1

    return '\n'.join(result), reset_count


def reset_kata_file(filepath: Path, dry_run: bool = False) -> bool:
    """
    Reset a single kata file.

    Returns:
        True if successful, False otherwise
    """
    if not filepath.exists():
        print(f"⚠️  File not found: {filepath}")
        return False

    try:
        # Read original content
        original_content = filepath.read_text()

        # Reset implementations
        new_content, reset_count = reset_function_implementations(original_content)

        if dry_run:
            print(f"  Would reset {reset_count} function(s)")
            return True

        # Write back
        filepath.write_text(new_content)
        print(f"  ✓ Reset {reset_count} function(s)")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Reset kata implementations to clean templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/reset_katas.py                    # Reset all katas
  python scripts/reset_katas.py binary_search      # Reset specific pattern
  python scripts/reset_katas.py --dry-run          # Preview changes
        """
    )
    parser.add_argument(
        'pattern',
        nargs='?',
        default=None,
        help='Pattern to reset (e.g., binary_search, two_pointers). If omitted, resets all.'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )

    args = parser.parse_args()

    # Print header
    print("=" * 60)
    print("   KATA RESET UTILITY")
    print("=" * 60)
    print()

    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be modified")
        print()

    # Find kata files
    kata_dir = Path('packages/runes/src/runes/algorithms')

    if not kata_dir.exists():
        print(f"❌ Kata directory not found: {kata_dir}")
        print("   Are you running from grimoire root?")
        sys.exit(1)

    if args.pattern:
        # Find specific pattern
        kata_files = list(kata_dir.glob(f'**/{args.pattern}*/kata.py'))
        if not kata_files:
            kata_files = list(kata_dir.glob(f'**/*{args.pattern}*/kata.py'))
    else:
        # Find all kata files
        kata_files = list(kata_dir.glob('**/kata.py'))

    if not kata_files:
        print(f"⚠️  No kata files found")
        if args.pattern:
            print(f"   Pattern: {args.pattern}")
        sys.exit(1)

    # Sort for consistent order
    kata_files.sort()

    # Reset each file
    success_count = 0
    for kata_file in kata_files:
        # Get pattern name for display
        pattern_name = str(kata_file.relative_to(kata_dir)).replace('/kata.py', '')

        print(f"📝 {pattern_name}")

        if reset_kata_file(kata_file, dry_run=args.dry_run):
            success_count += 1

        print()

    # Print summary
    print("=" * 60)
    if args.dry_run:
        print(f"🔍 DRY RUN COMPLETE")
        print(f"   Would reset {success_count} of {len(kata_files)} file(s)")
    else:
        print(f"✅ RESET COMPLETE")
        print(f"   Reset {success_count} of {len(kata_files)} file(s)")

        if success_count < len(kata_files):
            print(f"   ⚠️  {len(kata_files) - success_count} file(s) had errors")
    print("=" * 60)
    print()

    # Next steps
    if not args.dry_run and success_count > 0:
        print("📋 Next steps:")
        print("   1. Review: git diff packages/runes/src/runes/algorithms")
        print("   2. If happy: git add packages/runes/src/runes/algorithms/")
        print("   3. Commit: git commit -m 'kata: reset templates after practice'")
        print()


if __name__ == '__main__':
    main()
