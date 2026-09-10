---
id: formula.euler-identity
type: formula
status: established
maturity: draft

name: Euler's identity

summary: >
  Euler's identity is the special case of Euler's formula at theta = pi.

source_expression: |
  e^(iπ) + 1 = 0

canonical_expression: |
  e^{i\pi} + 1 = 0

equivalence:
  status: established
  reason: notation normalization

domains:
  - complex-analysis
  - geometry

prerequisites:
  - formula.euler
  - concept.angle

objects:
  - concept.complex-number
  - concept.exponential-function
  - concept.imaginary-unit

relations:
  - category: dependency
    type: specializes
    target: formula.euler
    condition: "theta = pi"

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.

validation:
  status: unverified
  methods: []
---

# Euler's Identity

## Structured Facts

| Property | Value |
|---|---|
| Type | Formula |
| Domain | [[Complex Analysis]], [[Geometry]] |
| Status | Established |
| Maturity | Draft |
| Prerequisites | [[Euler's Formula]], [[Angle]] |
| Relation | Specializes [[Euler's Formula]] at \(\theta=\pi\) |
| Sources | Not listed on source page. |

## Prose

Euler's identity is the compact special case \(e^{i\pi}+1=0\). It belongs in the Euler slice because it tests whether formula-to-formula specialization can be represented cleanly.
