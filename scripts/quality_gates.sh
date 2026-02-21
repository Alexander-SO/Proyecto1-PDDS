#!/usr/bin/env sh
set -eu

echo "== Quality Gates =="

# --- Gate 1: Coverage (initial baseline) ---
# If coverage.xml exists, parse line-rate (Cobertura XML format)
if [ -f coverage.xml ]; then
  LINE_RATE=$(python - << 'PY'
import xml.etree.ElementTree as ET
tree = ET.parse("coverage.xml")
root = tree.getroot()
print(root.attrib.get("line-rate", "0"))
PY
)
  # line-rate is 0..1 float
  COVERAGE_PERCENT=$(python - << PY
lr=float("$LINE_RATE")
print(int(round(lr*100)))
PY
)
  echo "Coverage: ${COVERAGE_PERCENT}%"
  MIN_COVERAGE=0
  if [ "$COVERAGE_PERCENT" -lt "$MIN_COVERAGE" ]; then
    echo "FAIL: Coverage ${COVERAGE_PERCENT}% < ${MIN_COVERAGE}%"
    exit 1
  fi
else
  echo "WARNING: coverage.xml not found. Skipping coverage gate (initial phase)."
fi

# --- Gate 2: Cyclomatic Complexity ---
# Fail if any item has rank C/D/E/F.
echo "Checking cyclomatic complexity with radon..."
radon cc -s conduit/apps > radon_cc.txt

if grep -qE " - [CDEF] \(" radon_cc.txt; then
  echo "FAIL: Complexity gate violated (found C or worse)."
  echo "Offenders:"
  grep -nE " - [CDEF] \(" radon_cc.txt || true
  exit 1
fi

echo "PASS: All quality gates satisfied."
