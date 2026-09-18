#!/usr/bin/env bash
# Builds every generated IG directory (igs/<slug>/) with SUSHI + the HL7
# FHIR IG Publisher, then collects each one's output/ under site/<slug>/
# alongside a small landing page linking to all of them. Continues through
# all IGs even if one fails, so a single CI run reports every broken IG.
set -uo pipefail

SUSHI_CMD="${SUSHI_CMD:-sushi}"
PUBLISHER_JAR="${PUBLISHER_JAR:-$PWD/publisher.jar}"
status=0
shopt -s nullglob

rm -rf site
mkdir -p site
built=()

for dir in igs/*/; do
  name=$(basename "$dir")
  echo "=== Building $name ==="
  if (cd "$dir" && $SUSHI_CMD build . && java -Xmx4g -jar "$PUBLISHER_JAR" -ig ig.ini); then
    mkdir -p "site/$name"
    cp -r "$dir/output/." "site/$name/"
    built+=("$name")
  else
    echo "!!! $name failed to build"
    status=1
  fi
done

{
  echo "<!DOCTYPE html>"
  echo "<html><head><meta charset=\"utf-8\"><title>XMI-to-FSH Implementation Guides</title></head><body>"
  echo "<h1>Implementation Guides</h1>"
  echo "<ul>"
  for name in "${built[@]}"; do
    echo "<li><a href=\"$name/\">$name</a></li>"
  done
  echo "</ul>"
  echo "</body></html>"
} > site/index.html

if [ "$status" -ne 0 ]; then
  echo
  echo "One or more IGs failed to build — see above."
fi
exit "$status"
