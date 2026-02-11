<<<<<<< HEAD
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
=======
# URF Prefab System

[Referee Map](REFEREE.md) · [Claims Policy](CLAIMS.md) · Explicit Claims Classification
[Status](STATUS.md) · Stable · Referee bundle frozen (referee-v1.0)
Canonical prefab layer for the Unified Rigidity Framework (URF).

This repository provides:
- Frozen axiom prefab (URF Core Axioms 0.0–0.4)
- Executable JSON schemas
- Deterministic verifier
- Reproducible CI-ready structure

Status:
- Canonical
- Frozen v1.0.0
- Dependency-locked to URF Core

Scope:
- Structural admissibility
- Capacity–locality certification
- No experimental or draft material

References:
- URF Core: https://github.com/inaciovasquez2020/urf-core
- Scientific Infrastructure: https://github.com/inaciovasquez2020/scientific-infrastructure
- Website: https://www.vasquezresearch.com
---

## Documentation & Navigation
- Framework overview: https://inaciovasquez2020.github.io
- Project index: https://inaciovasquez2020.github.io/vasquez-index/
- Infrastructure hub: https://github.com/inaciovasquez2020/scientific-infrastructure

## Technical Notes
* **Integration:** This library is designed to be imported by other repositories within the inaciovasquez2020 organization.
* **Reproducibility:** For stable research results, ensure you are utilizing the specific version referenced in the Vasquez Index dashboard.
* **Dependencies:** Refer to `scientific-infrastructure` for the standard execution environment.

Scientific Infrastructure (Environment & Reproducibility)
https://inaciovasquez2020.github.io/scientific-infrastructure/

## Citation
If you utilize this core logic in your research, please cite it using the following entry:

```bibtex
@manual{Vasquez_URF_Core_2026,
  author = {Vasquez, Inacio F.},
  title  = {urf-core: Foundational Logic for the Universal Reference Frame},
  year   = {2026},
  url    = {[https://github.com/inaciovasquez2020/urf-core](https://github.com/inaciovasquez2020/urf-core)}
}
 (Cross-link scientific-infrastructure as canonical environment layer)
Dependencies
urf-prefab-system
Source: https://github.com/inaciovasquez2020/urf-prefab-system
Tier: Tier-A (frozen)
Version: v0.2.1
Usage
This repository consumes the URF Prefab System for:
Structural prefab definitions
Assumption and invariant discipline
Certification hook alignment
No semantic or execution guarantees are inherited.
>>>>>>> origin/main
