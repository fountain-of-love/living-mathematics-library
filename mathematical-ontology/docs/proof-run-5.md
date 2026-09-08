# Proof Run 5

- **Status:** Completed first run
- **Purpose:** Canonical five-item proof run for the mathematical contract family.
- **Detailed audit:** [Mathematical Knowledge Engineering Proof Run](./mathematical-proof-run.md)
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

The first run has been instantiated in [Living Mathematics Library](../../living-mathematics-library/):

| Node | File | Result |
|---|---|---|
| `concept.complex-number` | [concept.complex-number.md](../../living-mathematics-library/concept.complex-number.md) | Created as draft node. |
| `theorem.fundamental-theorem-of-arithmetic` | [theorem.fundamental-theorem-of-arithmetic.md](../../living-mathematics-library/theorem.fundamental-theorem-of-arithmetic.md) | Created as draft node. |
| `formula.euler` | [formula.euler.md](../../living-mathematics-library/formula.euler.md) | Updated as draft node. |
| `conjecture.riemann-hypothesis` | [conjecture.riemann-hypothesis.md](../../living-mathematics-library/conjecture.riemann-hypothesis.md) | Created as draft node. |
| `experiment.zeta-zero-spacing-001` | [experiment.zeta-zero-spacing-001.md](../../living-mathematics-library/experiment.zeta-zero-spacing-001.md) | Created as draft node. |

## Result

The five-item proof run found no need to collapse the page contracts into one enormous schema.

It did require these revisions:

- add theorem as a first-class contract;
- preserve explicit absence fields;
- preserve source and canonical formula expressions separately;
- distinguish schema terms from mathematical entities;
- support human-readable Obsidian links backed by stable IDs.

## Scaling Gate

Do not scale the contract family across a large corpus until the detailed proof-run findings have been reviewed.
