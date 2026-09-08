---
schema_version: 1
id: OBS-000032
title: Arithmetic and Spectral Involutions Should Commute
summary: A faithful representation should intertwine divisor complementarity d <-> x/d with spectral reflection s <-> 1-s.
kind: translation
labels:
  - involution
  - functional-equation
  - spectral-reflection
claim_status: hypothesis
scope: domain-limited
workflow_status: screened
object: divisor complementarity representation
domain: divisor pairs and zeta functional-equation reflection
origin: proposed
provenance:
  file: Untitled 4.md
  section: the arithmetic and spectral involutions commute
relations:
  supports:
    - OBS-000028
  depends_on: []
  contrasts_with: []
  supersedes: []
---

# Arithmetic and Spectral Involutions Should Commute

## Context

The draft already contained divisor complementarity and spectral reflection, but needed a precise compatibility statement between them.

## Observation

A representation map $T$ should intertwine the arithmetic involution $d\mapsto x/d$ with the spectral involution $s\mapsto 1-s$.

## Mathematical expression

The two reflected forms are

$$
d\longleftrightarrow\frac{x}{d},\qquad s\longleftrightarrow 1-s.
$$

Define $\iota_x(d)=x/d$ and $J(s)=1-s$. The desired equivariance condition is

$$
T\circ\iota_x=J\circ T.
$$

## Example

The zeta functional equation uses the reflection $s\leftrightarrow 1-s$, making $J$ the relevant spectral reflection; see [DLMF section 25.4](https://dlmf.nist.gov/25.4).

## Claim boundary

Equivariance alone still allows $J$ to exchange two off-line modes, so this condition does not prove that each individual mode is fixed on the critical line.

## Translation

- **From:** divisor complementarity $d\leftrightarrow x/d$
- **To:** spectral reflection $s\leftrightarrow 1-s$
- **Preserved:** involutive reflection structure
- **Changed:** arithmetic pairing becomes spectral equivariance
- **Requires:** a defined representation map $T$
