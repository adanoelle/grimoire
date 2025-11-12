#!/bin/bash
# 8-week sprint progress report for grimoire

# Adjust this to your actual sprint start date
SPRINT_START="${1:-2024-12-20}"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 GRIMOIRE 8-WEEK SPRINT REPORT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Calculate days/weeks elapsed
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    START_EPOCH=$(date -j -f "%Y-%m-%d" "$SPRINT_START" +%s 2>/dev/null)
    if [ $? -ne 0 ]; then
        echo "❌ Invalid date format. Use: YYYY-MM-DD"
        echo "Usage: $0 [SPRINT_START_DATE]"
        echo "Example: $0 2024-12-20"
        exit 1
    fi
else
    # Linux
    START_EPOCH=$(date -d "$SPRINT_START" +%s 2>/dev/null)
    if [ $? -ne 0 ]; then
        echo "❌ Invalid date format. Use: YYYY-MM-DD"
        echo "Usage: $0 [SPRINT_START_DATE]"
        echo "Example: $0 2024-12-20"
        exit 1
    fi
fi

NOW_EPOCH=$(date +%s)
DAYS_ELAPSED=$(( (NOW_EPOCH - START_EPOCH) / 86400 ))
WEEKS_ELAPSED=$(( DAYS_ELAPSED / 7 + 1 ))

# Cap at 8 weeks
if [ $WEEKS_ELAPSED -gt 8 ]; then
    WEEKS_ELAPSED=8
fi

echo "📅 Sprint Progress:"
echo "   Start Date: $SPRINT_START"
echo "   Day: $DAYS_ELAPSED / 56"
echo "   Week: $WEEKS_ELAPSED / 8"
echo ""

# Total counts
TOTAL=$(git log --oneline --since="$SPRINT_START" --no-merges | wc -l | tr -d ' ')
DSA=$(git log --oneline --since="$SPRINT_START" --grep="cantrips" --no-merges | wc -l | tr -d ' ')
SYSTEMS=$(git log --oneline --since="$SPRINT_START" --grep="incantations" --no-merges | wc -l | tr -d ' ')

echo "📈 Total Progress:"
echo "   Total commits: $TOTAL"
echo "   DSA sessions: $DSA"
echo "   Systems sessions: $SYSTEMS"
echo ""

# Target tracking (rough estimates: 2-3 problems per session)
DSA_TARGET=120
SYSTEMS_TARGET=20
DSA_ESTIMATE=$((DSA * 2))  # Assume ~2 problems per commit
SYS_ESTIMATE=$SYSTEMS       # Assume ~1 design or concept per commit

DSA_PROGRESS=$((DSA_ESTIMATE * 100 / DSA_TARGET))
SYS_PROGRESS=$((SYS_ESTIMATE * 100 / SYSTEMS_TARGET))

echo "🎯 Estimated Progress (based on commits):"
echo "   DSA Problems: ~$DSA_ESTIMATE / $DSA_TARGET ($DSA_PROGRESS%)"
echo "   Systems Work: ~$SYS_ESTIMATE / $SYSTEMS_TARGET ($SYS_PROGRESS%)"
echo ""

# Pace check
EXPECTED_DSA=$((DSA_TARGET * WEEKS_ELAPSED / 8))
EXPECTED_SYS=$((SYSTEMS_TARGET * WEEKS_ELAPSED / 8))

echo "📊 Pace Check (Week $WEEKS_ELAPSED/8):"
echo "   DSA: ~$DSA_ESTIMATE / ~$EXPECTED_DSA expected ($(((DSA_ESTIMATE * 100) / EXPECTED_DSA))%)"
echo "   Systems: ~$SYS_ESTIMATE / ~$EXPECTED_SYS expected ($(((SYS_ESTIMATE * 100) / EXPECTED_SYS))%)"
echo ""

# Recent work
echo "📝 Last 10 study commits:"
git log --oneline --grep="cantrips\|incantations" --no-merges --color=always | head -10
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔮 The grimoire grows stronger every day!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Tip: Update this estimate with actual numbers in your READMEs"
