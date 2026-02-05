URF Prefab System

Status: CORE / CANONICAL / FROZEN v1

This repository defines the URF Prefab Mode System: a typed algebra for building admissible systems by construction.

Contents
lean/
  URF–CMI Subadditivity axiom and core prefab skeleton
certs/
  Certificate JSON schema for prefab compositions
src/
  Minimal verifier enforcing structural invariants

This repository includes an executable admissibility checker for textual claims, exposed as the command `urf-llm-check`. The checker enforces Cycle-Local Rigidity (CLR) and Archimedean Kernel Rigidity (AKR) constraints by rejecting responses that assert perpetual local homogeneity under rich cycle overlap or persistent global effects without local support under decay. Usage: pipe text to standard input and receive an ACCEPT or REJECT verdict.

Core results (intended to be mirrored by the manuscript PDF)
- URF–CMI Subadditivity (primitive axiom)
- Prefab Composition Admissibility (PCA)
- CURF categorical semantics (interfaces as bounded-information morphisms)
- Sink Closure necessity (no sink implies unbounded EntropyDepth)
- Typecheck ⇔ Certificate verification (meta-theorem)

No applications, tutorials, or GUI are included here.
