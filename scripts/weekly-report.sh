#!/bin/bash
# Weekly progress report for grimoire

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 GRIMOIRE WEEKLY REPORT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Date range (cross-platform)
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    START_DATE=$(date -v-7d +"%Y-%m-%d")
else
    # Linux
    START_DATE=$(date -d "7 days ago" +"%Y-%m-%d")
fi
END_DATE=$(date +"%Y-%m-%d")

echo "📅 Week: $START_DATE to $END_DATE"
echo ""

# Commit counts
TOTAL=$(git log --oneline --since="1 week ago" --no-merges | wc -l | tr -d ' ')
DSA=$(git log --oneline --since="1 week ago" --grep="cantrips" --no-merges | wc -l | tr -d ' ')
SYSTEMS=$(git log --oneline --since="1 week ago" --grep="incantations" --no-merges | wc -l | tr -d ' ')
RUNES=$(git log --oneline --since="1 week ago" --grep="runes" --no-merges | wc -l | tr -d ' ')

echo "📈 Commits:"
echo "   Total: $TOTAL"
echo "   DSA (cantrips): $DSA"
echo "   Systems (incantations): $SYSTEMS"
echo "   Foundations (runes): $RUNES"
echo ""

# Work log
echo "📝 This week's work:"
git log --oneline --since="1 week ago" --no-merges --grep="cantrips\|incantations" --color=always | head -15
echo ""

# Topics covered (extract from commit scopes)
echo "🎯 Topics covered:"
git log --oneline --since="1 week ago" --no-merges | grep -oE "\([a-z-]+\)" | sort | uniq -c | sort -rn
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔮 Keep building your grimoire!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
