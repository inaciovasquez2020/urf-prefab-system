#!/usr/bin/env bash
set -e
echo "Validating prefab documents"
missing=0
if [ ! -f ASSUMPTIONS.md ]; then
echo "Missing ASSUMPTIONS.md"
missing=1
fi
for f in docs/EXAMPLE_PREFAB.md docs/PREFAB_SCHEMA.md; do
if [ ! -f "$f" ]; then
echo "Missing $f"
missing=1
fi
done
grep -q "A1" ASSUMPTIONS.md || echo "Warning: A1 not found in ASSUMPTIONS.md"
if [ "$missing" -eq 1 ]; then
echo "Validation failed"
exit 1
fi
echo "Validation passed"
