#!/bin/sh
# After a push: wait until GitHub Pages has built HEAD, then run the full check against the live site.
# Usage: sh tools/verify-live.sh   (needs gh logged in, and what tools/check.cjs needs)
set -e
cd "$(dirname "$0")/.."
REPO=ryan-di/design-field-guide
SITE=https://ryan-di.github.io/design-field-guide/
HEAD=$(git rev-parse HEAD)
i=0
while :; do
  r=$(gh api "repos/$REPO/pages/builds/latest" --jq '.commit + " " + .status')
  case "$r" in
    "$HEAD built") echo "Pages built $HEAD"; break ;;
    *errored*) echo "Pages build failed: $r"; exit 1 ;;
  esac
  i=$((i + 1)); [ $i -gt 60 ] && { echo "Timed out waiting for Pages: $r"; exit 1; }
  sleep 5
done
node tools/check.cjs --url "$SITE?v=$(git rev-parse --short HEAD)"
