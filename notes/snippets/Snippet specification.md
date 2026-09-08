## Snippet specification

A snippet is a small, stand-alone knowledge unit containing exactly one observation. It should remain understandable even if the originating brain dump disappears.

Each snippet has two layers:

1. Structured metadata for indexing and reproducibility.
2. A short readable explanation of the observation.

### Required metadata

```
---
schema_version: 1
id: OBS-000009
title: Prime Exclusion Activates at p²
summary: A prime p first provides indispensable new exclusion information at p².
kind: prime-property
labels:
  - activation
  - sieve
  - recursion

claim_status: exact
scope: universal
workflow_status: screened

object: least-prime-factor sieve
domain: positive integers
origin: derived

provenance:
  file: ../prime-state-observation-matrix.md
  section: Activation and Growth

relations:
  supports: []
  depends_on:
    - OBS-000008
  contrasts_with: []
  supersedes: []
---
```

### Required body

```
# Prime Exclusion Activates at $p^2$

## Context

One sentence explaining what was being examined when the observation arose.

## Observation

A direct statement of the observation in ordinary language.

## Mathematical expression

The definition, identity, derivation, finite construction, or numerical result
supporting the observation.

## Example

The smallest example that makes the observation visible.

## Claim boundary

A precise statement of what the observation does not establish.
```

### Conditional sections

Include these only when relevant.

#### Translation

```
## Translation

- **From:** periodic divisibility mask
- **To:** active least-prime-witness rule
- **Preserved:** the relation $p\mid n$
- **Changed:** whether the rule contributes information not already supplied
- **Requires:** primes ordered increasingly
```

#### Numerical method

```
## Numerical method

- **Data:** source and range
- **Normalization:** transformation applied
- **Method:** calculation performed
- **Controls:** comparison baseline
- **Artifacts:** scripts, tables, and result files
```

#### Interpretation

```
## Interpretation

A clearly labelled reading of the mathematical result, kept separate from the
result itself.
```

## Controlled vocabulary

Keep claim status and workflow status separate. An exact observation can still be awaiting review.

### `kind`

```
prime-property
translation
method
numerical
analogy
caution
```

### `claim_status`

```
definition
exact
established
finite-observation
numerical-observation
interpretation
analogy
hypothesis
needs-repair
```

### `scope`

```
finite
domain-limited
asymptotic
universal
```

A finite scope may include its bound:

```
scope:
  type: finite
  range: 1 <= n <= 50
```

### `origin`

This identifies where the visible structure came from:

```
derived                 # follows from the mathematical object
measured                # obtained from data
representation-induced  # appears because of a chosen coordinate or transform
proposed                # introduced as a model or hypothesis
```

### `workflow_status`

```
captured
screened
ready
promoted
merged
rejected
```
