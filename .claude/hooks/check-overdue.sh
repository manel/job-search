#!/bin/bash
# SessionStart hook: surface (1) overdue next_action_on dates from the
# frontmatter of open records in applications/records/ and (2) the open
# "This week" items in TODO.md, injected as context at the start of every
# session.

DIR="${CLAUDE_PROJECT_DIR:-.}"
RECORDS="$DIR/applications/records"
TODO="$DIR/TODO.md"
TODAY=$(date +%Y-%m-%d)
CTX=""

if [ -d "$RECORDS" ]; then
  OVERDUE=$(awk -v today="$TODAY" '
    FNR == 1 { fm=0; company=""; status=""; action=""; due="" }
    /^---$/ { fm++; if (fm == 2) emit(); next }
    fm == 1 && /^company:/ { company=val($0) }
    fm == 1 && /^status:/ { status=val($0) }
    fm == 1 && /^next_action:/ { action=val($0) }
    fm == 1 && /^next_action_on:/ { due=val($0) }
    function val(s) { sub(/^[a-z_]+: */, "", s); gsub(/^"|"$/, "", s); return s }
    function emit() {
      if (status ~ /^(rejected|skipped|stale|withdrawn|role-closed|hired)$/) return
      if (due !~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/ || due > today) return
      print due "\t- " company " (" status "): due " due " (" substr(action, 1, 140) ")"
    }
  ' "$RECORDS"/*.md | sort | cut -f2-)
  if [ -n "$OVERDUE" ]; then
    CTX="OVERDUE PIPELINE ACTIONS in applications/records/ (today: $TODAY). Surface these to the user before starting other work; follow-ups on live applications outrank new work. Suggest running /follow-up.
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

WATCH="$DIR/sourcing/posting-watch.tsv"
if [ -f "$WATCH" ]; then
  WATCHED=$(grep -v '^#' "$WATCH" | while IFS=$'\t' read -r board title loc note added; do
    [ -z "$board" ] && continue
    curl -s --max-time 5 "https://boards-api.greenhouse.io/v1/boards/$board/jobs" |
      python3 -I -c '
import json, re, sys
board, title, loc, note = sys.argv[1:5]
try:
    jobs = json.load(sys.stdin)["jobs"]
except Exception:
    print(f"- {board}: board unreachable, not checked ({note})"); sys.exit()
hits = [j for j in jobs if re.search(title, j["title"], re.I) and re.search(loc, j["location"]["name"], re.I)]
for j in hits:
    t, l, u, url = j["title"], j["location"]["name"], j["updated_at"][:10], j["absolute_url"]
    print(f"- LIVE {board}: {t} | {l} | updated {u} | {url} ({note})")
if not hits:
    print(f"- {board}: not posted yet ({note}, watching since {sys.argv[5]})")
' "$board" "$title" "$loc" "$note" "$added"
  done)
  if [ -n "$WATCHED" ]; then
    [ -n "$CTX" ] && CTX="$CTX

"
    CTX="${CTX}POSTING WATCH (sourcing/posting-watch.tsv). Tell the user the status of each line in one sentence. For a LIVE match, suggest /assess-fit on the URL and removing the line once assessed:
$WATCHED"
  fi
fi

[ -z "$CTX" ] && exit 0

jq -n --arg ctx "$CTX" '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":$ctx}}'
