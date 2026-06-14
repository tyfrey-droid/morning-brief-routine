#!/usr/bin/env bash
# Outputs article URLs cited in the last N archive briefs (default 4).
# Use as a dedup blocklist: run at the start of each brief generation.
# Usage: bash scripts/seen-urls.sh [N=4]
#
# Example:
#   SEEN=$(bash scripts/seen-urls.sh 4)
#   echo "$SEEN" | grep -F "https://insideevs.com/news/797914" && echo "DUPLICATE"

ARCHIVE_DIR="$(cd "$(dirname "$0")/.." && pwd)/archive"
N="${1:-4}"

mapfile -t FILES < <(ls -1 "$ARCHIVE_DIR"/*.html 2>/dev/null | sort -r | head -n "$N")

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "(no archive files found)" >&2
  exit 0
fi

printf "# Seen URLs from %d most recent archive briefs:\n" "${#FILES[@]}" >&2
for f in "${FILES[@]}"; do printf "#   %s\n" "$(basename "$f")" >&2; done

grep -hoP '(?<=href=")[^"]+' "${FILES[@]}" \
  | grep -v 'fonts\.google\|fonts\.gstatic' \
  | grep -vE '^https?://[^/]+/?$' \
  | sort -u
