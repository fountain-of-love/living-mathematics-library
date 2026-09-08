---
schema_version: 1
id: OBS-000031
title: CRT Boundary Gives a Finite Spectral Model
summary: A finite prime mask field with period P_k lives on Z/P_kZ, where CRT decomposition and finite Fourier analysis are exact.
kind: translation
labels:
  - crt
  - finite-fourier
  - prime-mask
claim_status: exact
scope: domain-limited
workflow_status: screened
object: finite prime mask field
domain: first k primes and residues modulo P_k
origin: derived
provenance:
  file: Untitled 3.md
  section: the CRT boundary as an exact finite spectral model
relations:
  supports:
    - OBS-000028
  depends_on: []
  contrasts_with: []
  supersedes: []
---

# CRT Boundary Gives a Finite Spectral Model

## Context

Finite prime masks were being connected to spectral language without relying on loose analogy.

## Observation

For the first $k$ primes, the combined mask field has an exact finite period, so it can be studied on $\mathbb Z/P_k\mathbb Z$ using CRT decomposition and finite Fourier transformation.

## Mathematical expression

For the first $k$ primes,

$$
P_k=\prod_{j\le k}p_j.
$$

The finite model follows the sequence

$$
\text{finite masks}\longrightarrow\text{CRT decomposition}\longrightarrow\text{finite Fourier spectrum}.
$$

## Example

For primes $2,3,5$, the period is $P_3=30$, and the mask field can be represented exactly on $\mathbb Z/30\mathbb Z$.

## Claim boundary

The finite CRT and Fourier model is exact at fixed $k$; it does not by itself prove that the finite spectra have a compatible limiting Mellin-scale representation connected to zeta.

## Translation

- **From:** periodic finite prime masks
- **To:** CRT-decomposed finite Fourier spectrum
- **Preserved:** residue-class information modulo $P_k$
- **Changed:** pointwise mask data becomes spectral coefficient data
- **Requires:** fixed finite $k$ before taking any limit
