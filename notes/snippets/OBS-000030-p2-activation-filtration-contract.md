---
schema_version: 1
id: OBS-000030
title: p2 Activation Suggests a Filtration Contract
summary: Prime-field horizons can be treated as a filtration, requiring faithful transforms to commute with square-root restriction.
kind: translation
labels:
  - activation
  - filtration
  - square-root-boundary
claim_status: hypothesis
scope: domain-limited
workflow_status: screened
object: prime-field horizon transform
domain: prime masks observed up to x and sqrt(x)
origin: proposed
provenance:
  file: Untitled 2.md
  section: p2-activation into a filtration contract
relations:
  supports:
    - OBS-000028
  depends_on: []
  contrasts_with: []
  supersedes: []
---

# p2 Activation Suggests a Filtration Contract

## Context

The activation rule for prime exclusions at $p^2$ was being translated into a compatibility condition between arithmetic horizons.

## Observation

If prime fields at different horizons form a filtration, then a faithful spectral transform should commute with restriction from $x$ to $\sqrt x$.

## Mathematical expression

The horizon inclusion is

$$
\mathfrak P_{\sqrt x}\hookrightarrow\mathfrak P_x.
$$

A faithful transform $T_x$ should satisfy

$$
T_x(\mathfrak P_x)\big|_{\sqrt x}=T_{\sqrt x}(\mathfrak P_{\sqrt x}).
$$

An off-line relative factor changes under repeated square-root descent:

$$
x^{\beta-1/2}\mapsto x^{(\beta-1/2)/2}\mapsto x^{(\beta-1/2)/4}\mapsto\cdots.
$$

## Example

When the observation horizon descends from $x$ to $\sqrt x$, the relative exponent $\beta-1/2$ is halved in the displayed scaling factor.

## Claim boundary

This formulates a desired compatibility condition; it does not prove that only critical-line modes satisfy the condition.

## Translation

- **From:** $p^2$-activation boundary
- **To:** recursively compatible spectral filtration
- **Preserved:** the inclusion $\mathfrak P_{\sqrt x}\hookrightarrow\mathfrak P_x$
- **Changed:** arithmetic horizon restriction becomes transform compatibility
- **Requires:** a defined transform $T_x$ and a precise restriction operation
