#!/bin/bash
# SessionStart hook: surface (1) overdue Next action dates from the Active
# table in context/applications.md and (2) the open "This week" items in
# TODO.md, injected as context at the start of every session.

DIR="${CLAUDE_PROJECT_DIR:-.}"
APPS="$DIR/context/applications.md"
TODO="$DIR/TODO.md"
TODAY=$(date +%Y-%m-%d)
CTX=""

if [ -f "$APPS" ]; then
  OVERDUE=$(awk -F'|' -v today="$TODAY" '
    /^## Active/ { active=1; next }
    active && /^## / { active=0 }
    active && /^\|/ && $2 !~ /Role/ && $2 !~ /---/ {
      cell=$6
      while (match(cell, /[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/)) {
        d = substr(cell, RSTART, RLENGTH)
        cell = substr(cell, RSTART + RLENGTH)
        if (d <= today) {
          company=$3; action=$6
          gsub(/^ +| +$/, "", company)
          gsub(/^ +| +$/, "", action)
          print "- " company ": due " d " (" action ")"
          break
        }
      }
    }
  ' "$APPS")
  if [ -n "$OVERDUE" ]; then
    CTX="OVERDUE PIPELINE ACTIONS in context/applications.md (today: $TODAY). Surface these to the user before starting other work; follow-ups on live applications outrank new work. Suggest running /follow-up.
$OVERDUE"
  fi
fi

if [ -f "$TODO" ]; then
  WEEK=$(awk '
    /^## This week/ { s=1; next }
    s && /^## / { s=0 }
    s && /^- \[ \]/ { sub(/^- \[ \] /, "- "); print }
  ' "$TODO" | cut -c1-160 | head -12)
  if [ -n "$WEEK" ]; then
    [ -n "$CTX" ] && CTX="$CTX

"
    CTX="${CTX}OPEN ITEMS in the This week section of TODO.md (full details and drafts are in that file). Remind the user these are the current priorities:
$WEEK"
  fi
fi

[ -z "$CTX" ] && exit 0

jq -n --arg ctx "$CTX" '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":$ctx}}'
