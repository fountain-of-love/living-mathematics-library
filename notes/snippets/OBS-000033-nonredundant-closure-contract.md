---
schema_version: 1
id: OBS-000033
title: Nonredundant Closure Requires Atomic Fixed Modes
summary: Spectral symmetry of the whole is insufficient if off-line reflected pairs can combine symmetrically without each mode being fixed.
kind: caution
labels:
  - closure
  - reflected-orbits
  - critical-line
claim_status: hypothesis
scope: domain-limited
workflow_status: screened
object: spectral closure analogue
domain: reflected divisor pairs and spectral modes
origin: proposed
provenance:
  file: Untitled 5.md
  section: a nonredundant-closure contract
relations:
  supports:
    - OBS-000028
  depends_on:
    - OBS-000032
  contrasts_with: []
  supersedes: []
---

# Nonredundant Closure Requires Atomic Fixed Modes

## Context

The divisor test closes at $\sqrt x$, and the draft needed a spectral analogue strong enough to face the Riemann-hypothesis question.

## Observation

Global spectral symmetry is not enough: a faithful closure argument must explain whether reflected two-dimensional orbits are allowed, or whether each irreducible mode must itself be fixed by reflection.

## Mathematical expression

Arithmetic closure keeps one side of each complementary divisor pair:

$$
d\longleftrightarrow \frac{x}{d},\qquad d\le \sqrt x.
$$

The spectral question is whether closure permits pairs $\{s,1-s\}$ with $s\ne 1-s$, or forces the fixed condition

$$
s=1-s.
$$

## Example

A symmetric sum of two off-line reflected terms can respect the global reflection $s\leftrightarrow 1-s$ even when neither term is individually fixed.

## Claim boundary

This identifies a proof obligation; it does not establish that irreducible spectral modes must be fixed by reflection.

## Interpretation

The RH-facing target is an argument that atomic spectral components, not only their aggregate, inherit the fixed boundary.
