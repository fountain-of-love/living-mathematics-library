---
id: conjecture.riemann-hypothesis
type: conjecture
status: open
maturity: draft

name: Riemann hypothesis

summary: >
  The Riemann hypothesis states that every non-trivial zero of the Riemann zeta
  function has real part 1/2.

claim: >
  Every non-trivial zero of zeta(s) has real part 1/2.

domains:
  - number-theory
  - complex-analysis

depends_on:
  - concept.riemann-zeta-function
  - concept.complex-zero
  - concept.analytic-continuation

evidence:
  - type: numerical
    status: not-yet-developed
  - type: theoretical-partial-results
    status: not-yet-developed

counterexamples:
  status: not-known
  note: No counterexample is documented in this library or in the checked record.

proof:
  status: unproved
  note: This conjecture is open; numerical evidence must not be treated as proof.

related:
  - concept.riemann-zeta-function
  - experiment.zeta-zero-spacing-001
  - theorem.prime-number-theorem

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.

validation:
  status: unverified
  methods: []
---

# Riemann Hypothesis

## Structured Facts

| Property | Value |
|---|---|
| Type | Conjecture |
| Domain | [[Number Theory]], [[Complex Analysis]] |
| Status | Open |
| Maturity | Draft |
| Depends on | [[Riemann Zeta Function]], [[Complex Zero]], [[Analytic Continuation]] |
| Evidence | Numerical and theoretical partial results not yet developed locally |
| Counterexamples | Not known in this library or checked record |
| Proof | Unproved |
| Sources | Not listed on source page. |

## Prose

The Riemann hypothesis is an open claim about where the non-trivial zeros of the [[Riemann Zeta Function]] lie in the complex plane.

This page must keep the distinction between evidence and proof sharp. Computational checks and observed zero patterns may support exploration, but they do not establish the conjecture.

## Proof-Run Audit

- [x] Object type identified
- [x] Stable ID assigned
- [x] Precise claim recorded
- [x] Dependency links recorded
- [x] Open epistemic status assigned
- [x] Evidence separated from proof
- [x] Counterexample status recorded
- [x] Proof status recorded
- [x] Structured source placeholder used
- [ ] External source linked
- [ ] Equivalent formulations linked
- [ ] Known partial results linked
