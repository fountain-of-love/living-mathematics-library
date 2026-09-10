# Proof Run 5

- **Status:** Completed first run
- **Purpose:** Five-item pre-scale audit for the Living Mathematics Library contracts.
- **Full audit:** [mathematical-ontology/docs/mathematical-proof-run.md](../mathematical-ontology/docs/mathematical-proof-run.md)
- **Run date:** 2026-09-08

## Run Set

| Kind | Test artifact | Outcome |
|---|---|---|
| Definition / concept | `concept.complex-number` | Pass with source-structure caveat. |
| Theorem | `theorem.fundamental-theorem-of-arithmetic` | Pass after adding theorem contract and explicit counterexample scope. |
| Formula | `formula.euler` | Pass after adding formula provenance fields. |
| Conjecture | `conjecture.riemann-hypothesis` | Pass after separating evidence, proof, and counterexample status. |
| Experiment | `experiment.zeta-zero-spacing-001` | Pass as draft after using explicit absence values for unfinished setup, observations, and does-not-establish boundary. |

## Instantiated Nodes

| Node | File | Result |
|---|---|---|
| `concept.complex-number` | [concept.complex-number.md](./concept.complex-number.md) | Created as draft node. |
| `theorem.fundamental-theorem-of-arithmetic` | [theorem.fundamental-theorem-of-arithmetic.md](./theorem.fundamental-theorem-of-arithmetic.md) | Created as draft node. |
| `formula.euler` | [formula.euler.md](./formula.euler.md) | Updated as draft node. |
| `conjecture.riemann-hypothesis` | [conjecture.riemann-hypothesis.md](./conjecture.riemann-hypothesis.md) | Created as draft node. |
| `experiment.zeta-zero-spacing-001` | [experiment.zeta-zero-spacing-001.md](./experiment.zeta-zero-spacing-001.md) | Created as draft node. |

## What The Run Proved

- The repository can start with five flat node artifacts instead of a full folder tree.
- The page-contract family is healthier than one enormous schema.
- Human Obsidian links and machine stable IDs can coexist.
- Formula provenance needs both source and canonical expressions.
- Missing fields need explicit absence values.
- The process should be reviewed before scaling.

## Euler Formula Audit

- [x] Object type identified
- [x] Stable ID assigned
- [x] Precise statement recorded
- [x] Notation normalized
- [x] Prerequisites linked
- [x] Related concepts linked
- [x] Epistemic status assigned
- [x] Source recorded
- [x] Alternative notation recorded
- [x] Formula relationship recorded
- [ ] Proof page linked
- [ ] Computational experiment linked

## Scaling Gate

Do not populate `vocabulary/`, `concepts/`, `formulas/`, `theorems/`, `conjectures/`, `experiments/`, `bonds/`, `sources/`, or `research/` until these starter pages have been reviewed and any field awkwardness has been folded back into the contracts.
