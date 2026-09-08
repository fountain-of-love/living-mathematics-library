---
schema_version: 1
id: OBS-000035
title: Distinguish Discovery from Normalized Observation
summary: Knowledge notes should not describe a normalized numerical pattern as if the repository had discovered a mathematical relationship.
kind: caution
labels:
  - epistemic-status
  - numerical-observation
  - normalization
claim_status: interpretation
scope: domain-limited
workflow_status: screened
object: knowledge-system claim wording
domain: mathematical note curation
origin: proposed
provenance:
  file: Untitled 7.md
  section: untitled caution
relations:
  supports:
    - OBS-000028
  depends_on: []
  contrasts_with: []
  supersedes: []
---

# Distinguish Discovery from Normalized Observation

## Context

Mathematical knowledge notes were being screened for wording that could overstate the epistemic status of a pattern.

## Observation

A repository should distinguish between discovering a relationship and observing a numerical pattern under a particular normalization.

## Mathematical expression

The distinction can be represented as two different claim forms:

$$
\text{repository discovered a relationship}
$$

versus

$$
\text{numerical pattern observed under normalization }N.
$$

## Example

"The repository discovered a relationship" asserts a stronger epistemic state than "a numerical pattern was observed under a particular normalization."

## Claim boundary

This is a wording and provenance caution; it does not judge whether any specific numerical pattern is meaningful, reproducible, or mathematically exact.

## Interpretation

The stronger phrase implies mathematical discovery, while the weaker phrase preserves the actual evidential boundary of a normalized observation.

introduce a mandatory experiment structure:

```yaml
experiment:
  id: exp.prime-mask-001

  question: >
    Does X correlate with Y under transformation Z?

  hypothesis: >
    ...

  objects:
    - ...

  dataset:
    source: ...
    version: ...
    hash: ...

  method:
    ...

  controls:
    - null_model
    - randomized_baseline
    - alternative_normalization

  result:
    statistic: ...
    value: ...
    uncertainty: ...

  interpretation:
    supported: ...
    unsupported: ...

  status: empirical-observation
```
