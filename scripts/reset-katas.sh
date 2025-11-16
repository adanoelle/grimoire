#!/bin/bash
#
# reset-katas.sh - Reset kata implementations to clean templates
#
# Usage:
#   ./scripts/reset-katas.sh                    # Reset all katas
#   ./scripts/reset-katas.sh binary_search      # Reset specific pattern
#   ./scripts/reset-katas.sh --dry-run          # Preview changes
#
# This script finds all function definitions in kata.py files and resets
# their implementations back to 'pass', preserving docstrings and test code.

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Base directory
KATA_DIR="packages/runes/src/runes/algorithms"

# Dry run mode
DRY_RUN=false
if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN=true
    shift
fi

# Specific pattern filter (optional)
PATTERN_FILTER="${1:-}"

echo -e "${BLUE}════════════════════════════════════════${NC}"
echo -e "${BLUE}   KATA RESET UTILITY${NC}"
echo -e "${BLUE}════════════════════════════════════════${NC}"
echo

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}DRY RUN MODE - No files will be modified${NC}"
    echo
fi

# Function to reset a single kata.py file
reset_kata_file() {
    local file="$1"
    local pattern_name=$(echo "$file" | sed 's|.*algorithms/||' | sed 's|/kata.py||')

    if [ ! -f "$file" ]; then
        echo -e "${YELLOW}⚠️  File not found: $file${NC}"
        return 1
    fi

    echo -e "${BLUE}Processing:${NC} $pattern_name"

    # Create backup
    cp "$file" "${file}.backup"

    # Python script to reset implementations
    python3 << 'PYTHON_SCRIPT' "$file"
import sys
import re

def reset_kata_file(filepath):
    """Reset all function implementations to 'pass' while preserving structure."""

    with open(filepath, 'r') as f:
        content = f.read()

    # Pattern to match function definitions and their bodies
    # This matches from 'def function_name' through the next function/class/EOF
    # while preserving docstrings

    def reset_function(match):
        """Reset a single function's implementation to 'pass'."""
        indent = match.group(1)
        func_def = match.group(2)
        docstring = match.group(3) if match.group(3) else ''

        # Build reset version
        result = f"{indent}{func_def}\n"
        if docstring:
            result += docstring
        result += f"{indent}    pass\n"

        return result

    # Match function definitions with docstrings
    # Captures: (indentation)(def line)(optional docstring)(body)
    pattern = re.compile(
        r'^(\s*)'  # Capture indentation
        r'(def\s+\w+\([^)]*\)\s*(?:->\s*[^:]+)?\s*:)\n'  # Function definition
        r'(\s*"""[\s\S]*?"""\n)?'  # Optional docstring
        r'(?:\s*pass\s*\n|[\s\S]*?(?=\n(?:\s{0}def\s|\s{0}class\s|\s{0}#\s*=|if\s+__name__|$)))',  # Body until next def/class/separator
        re.MULTILINE
    )

    # Count functions reset
    reset_count = 0

    def count_and_reset(match):
        nonlocal reset_count
        reset_count += 1
        return reset_function(match)

    new_content = pattern.sub(count_and_reset, content)

    return new_content, reset_count

if __name__ == '__main__':
    filepath = sys.argv[1]
    new_content, count = reset_kata_file(filepath)

    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)

    print(f"  ✓ Reset {count} function(s)")

PYTHON_SCRIPT

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}  ✓ Successfully reset${NC}"
        # Remove backup on success
        rm "${file}.backup"
        return 0
    else
        echo -e "${YELLOW}  ✗ Error resetting, restored from backup${NC}"
        mv "${file}.backup" "$file"
        return 1
    fi
}

# Find and process kata files
RESET_COUNT=0
TOTAL_COUNT=0

if [ -n "$PATTERN_FILTER" ]; then
    # Reset specific pattern
    KATA_FILES=$(find "$KATA_DIR" -path "*${PATTERN_FILTER}*/kata.py" 2>/dev/null)
else
    # Reset all katas
    KATA_FILES=$(find "$KATA_DIR" -name "kata.py" 2>/dev/null)
fi

if [ -z "$KATA_FILES" ]; then
    echo -e "${YELLOW}No kata files found${NC}"
    if [ -n "$PATTERN_FILTER" ]; then
        echo "Pattern filter: $PATTERN_FILTER"
    fi
    exit 1
fi

while IFS= read -r file; do
    if [ -f "$file" ]; then
        TOTAL_COUNT=$((TOTAL_COUNT + 1))

        if [ "$DRY_RUN" = true ]; then
            pattern_name=$(echo "$file" | sed 's|.*algorithms/||' | sed 's|/kata.py||')
            echo -e "${BLUE}Would reset:${NC} $pattern_name"
        else
            if reset_kata_file "$file"; then
                RESET_COUNT=$((RESET_COUNT + 1))
            fi
        fi
    fi
done <<< "$KATA_FILES"

echo
echo -e "${BLUE}════════════════════════════════════════${NC}"

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}DRY RUN COMPLETE${NC}"
    echo -e "Would reset ${TOTAL_COUNT} kata file(s)"
else
    echo -e "${GREEN}RESET COMPLETE${NC}"
    echo -e "Reset ${RESET_COUNT} of ${TOTAL_COUNT} kata file(s)"

    if [ $RESET_COUNT -ne $TOTAL_COUNT ]; then
        echo -e "${YELLOW}Note: Some files were not reset (see errors above)${NC}"
    fi
fi

echo -e "${BLUE}════════════════════════════════════════${NC}"
echo

# Remind user to commit
if [ "$DRY_RUN" = false ] && [ $RESET_COUNT -gt 0 ]; then
    echo -e "${BLUE}Next steps:${NC}"
    echo "  1. Review changes: git diff packages/runes/src/runes/algorithms"
    echo "  2. Commit: git add packages/runes/src/runes/algorithms/"
    echo "  3. Message: 'kata: reset templates after practice'"
    echo
fi

exit 0
