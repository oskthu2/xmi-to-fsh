#!/usr/bin/env bash
# Runs `sushi build .` inside every generated IG directory (igs/<slug>/),
# validating each one independently. Continues through all of them even if
# one fails, so a single CI run reports every broken IG at once instead of
# stopping at the first.
set -uo pipefail

SUSHI_CMD="${SUSHI_CMD:-npx sushi}"
status=0
shopt -s nullglob

for dir in igs/*/; do
  name=$(basename "$dir")
  echo "=== Validating $name ==="
  if ! (cd "$dir" && $SUSHI_CMD build .); then
    echo "!!! $name failed SUSHI validation"
    status=1
  fi
done

if [ "$status" -ne 0 ]; then
  echo
  echo "One or more IGs failed FSH validation — see above."
fi
exit "$status"
