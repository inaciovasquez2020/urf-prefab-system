#!/usr/bin/env bash
set -e

echo "Reproducing URF Prefab System sanity checks"

if [ -f lakefile.lean ]; then
echo "Lean project detected"
lake update
lake build
else
echo "No Lean project detected, skipping Lean build"
fi

echo "Repository structure:"
find . -maxdepth 2 -type f

echo "Reproduction complete"
