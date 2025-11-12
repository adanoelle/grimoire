#!/usr/bin/env bash

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

TEMPLATE_PATH="$PROJECT_ROOT/docs/templates/cantrip.py"
CANTRIPS_DIR="$PROJECT_ROOT/packages/cantrips/src/cantrips"

# Check arguments
if [ $# -ne 2 ]; then
    echo -e "${RED}Error: Invalid number of arguments${NC}"
    echo "Usage: $0 <topic> <problem-name>"
    echo ""
    echo "Available topics:"
    ls -1 "$CANTRIPS_DIR" | grep -v "^__" | sed 's/^/  - /'
    echo ""
    echo "Example: $0 arrays_strings reverse_string"
    exit 1
fi

TOPIC=$1
PROBLEM_NAME=$2
TOPIC_DIR="$CANTRIPS_DIR/$TOPIC"
OUTPUT_FILE="$TOPIC_DIR/${PROBLEM_NAME}.py"

# Validate topic exists
if [ ! -d "$TOPIC_DIR" ]; then
    echo -e "${RED}Error: Topic '$TOPIC' does not exist${NC}"
    echo ""
    echo "Available topics:"
    ls -1 "$CANTRIPS_DIR" | grep -v "^__" | sed 's/^/  - /'
    exit 1
fi

# Check if template exists
if [ ! -f "$TEMPLATE_PATH" ]; then
    echo -e "${RED}Error: Template not found at $TEMPLATE_PATH${NC}"
    exit 1
fi

# Check if file already exists
if [ -f "$OUTPUT_FILE" ]; then
    echo -e "${YELLOW}File already exists:${NC} $OUTPUT_FILE"
else
    # Copy template
    cp "$TEMPLATE_PATH" "$OUTPUT_FILE"
    echo -e "${GREEN}✓ Created cantrip:${NC} $OUTPUT_FILE"
    echo ""
    echo "Next steps:"
    echo "  1. Fill in the problem description and constraints"
    echo "  2. Implement your solution"
    echo "  3. Add test cases"
    echo "  4. Document your approach and lessons learned"
    echo "  5. Update $TOPIC_DIR/README.md with your progress"
    echo ""
fi

# Prompt to open in editor
if [ -n "$EDITOR" ]; then
    read -p "Open in editor? (Y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        exec $EDITOR "$OUTPUT_FILE"
    fi
else
    echo -e "${YELLOW}Tip: Set \$EDITOR environment variable to enable editor opening${NC}"
fi
