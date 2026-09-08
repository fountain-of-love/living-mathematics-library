---
schema_version: 1
id: OBS-000028
title: Contract-First Prime Field Spectral Review
summary: A prime-field argument should explicitly map each arithmetic contract to its claimed spectral inheritance and status.
kind: method
labels:
  - prime-field
  - spectral-contract
  - review
claim_status: hypothesis
scope: domain-limited
workflow_status: screened
object: prime-field spectral correspondence
domain: prime masks and spectral representations
origin: proposed
provenance:
  file: Untitled.md
  section: Contract-first review
relations:
  supports: []
  depends_on: []
  contrasts_with: []
  supersedes: []
---

# Contract-First Prime Field Spectral Review

## Context

A draft argument was being reviewed for which arithmetic structures of prime masks were already developed and which spectral inheritances still needed proof.

## Observation

The argument becomes more inspectable if every prime-field contract is listed beside its intrinsic arithmetic invariant, its required spectral inheritance, and its proof status.

## Mathematical expression

| Prime-field contract | Intrinsic boundary/invariant | Required spectral inheritance |
|---|---|---|
| Binary exclusion | $B_p(n)\in\{0,1\}$ | Projection or idempotence |
| Periodicity | $B_p(n+p)=B_p(n)$ | Roots-of-unity / Fourier phases |
| Divisor complementarity | $d\leftrightarrow x/d$ | Reflection involution |
| Closure | $d=\sqrt x$ | $x^{1/2}$ balance scale |
| Mask activation | First new exclusion at $p^2$ | Half-scale filtration |
| Recursion | $S_k=S_{k-1}W_k$ | Compatible spectral refinement |
| Nesting | $\mathcal S_{k+1}\subseteq\mathcal S_k$ | Consistent limiting spectrum |
| CRT composition | $P_k=\prod_{j\le k}p_j$ | Tensor / product decomposition |
| Prime locality | Each new mask has one prime generator | Primitive spectral components |
| Prime-power repetition | $p^m$ returns to generator $p$ | von Mangoldt weight $\log p$ |
| Reality | Masks and counting functions are real | Complex-conjugate symmetry |
| Reconstruction | Complete field determines prime states | Spectral completeness / faithfulness |
| Self-duality | $C(x)=x/C(x)$ | Critical-line fixed axis |

## Example

The divisor, activation, recursive, multiplicative, and reflection rows can be marked first, then each row can be assigned one status:

- exact arithmetic
- exact spectral
- preserved
- still to derive

## Claim boundary

This is a review method, not a proof that any spectral inheritance follows from the arithmetic contracts.
