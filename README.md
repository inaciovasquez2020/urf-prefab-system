URF Prefab System
Purpose
A prefab-style structural layer for assembling URF-compliant components with explicit assumptions, invariants, and reduction boundaries.
CI status
https://github.com/inaciovasquez2020/urf-prefab-system/actions/workflows/ci.yml
What this repository contains
Structural definitions and interfaces for prefab URF components
Explicit assumption tracking
Clear separation between proven structure and conditional extensions
What this repository does not claim
No completeness or optimality theorems
No claims beyond explicitly listed assumptions
No closed-form solutions to downstream URF problems
Navigation
STATUS.md: proven, conditional, open items
ASSUMPTIONS.md: explicit assumption index
REFEREE_MAP.md: guided reading paths
Status
Active, scope-locked, externally reviewable

## Quickstart (60 seconds)

```bash
lake update
lake build


---

## 3) Add STATUS document
```zsh
cat > STATUS.md <<'EOF'
# Repository Status — URF Prefab System

Code: Stable
Formalization: Lean 4 / Lake
CI: Enforced

## What this repo guarantees
- Deterministic Lean builds under the declared toolchain
- Canonical prefab definitions typecheck and elaborate

## What it verifies
- Structural correctness of prefab system modules
- Importability of the canonical root namespace

## What it does not claim
- No claim of completeness beyond included modules
- No claim of downstream application correctness
