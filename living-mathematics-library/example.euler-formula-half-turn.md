---
id: example.euler-formula-half-turn
type: example
status: established
maturity: draft

name: Euler formula half-turn example

summary: >
  Setting theta = pi in Euler's formula gives a half-turn on the unit circle and
  leads to Euler's identity.

domains:
  - complex-analysis
  - geometry

demonstrates:
  - formula.euler
  - formula.euler-identity
  - concept.rotation

prerequisites:
  - formula.euler
  - concept.unit-circle
  - concept.angle

relations:
  - category: representation
    type: demonstrates
    target: formula.euler
  - category: dependency
    type: specializes-to
    target: formula.euler-identity
  - category: representation
    type: represents
    target: concept.rotation

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.

validation:
  status: unverified
  methods: []
---

# Euler Formula Half-Turn Example

## Structured Facts

| Property | Value |
|---|---|
| Type | Example |
| Domain | [[Complex Analysis]], [[Geometry]] |
| Status | Established |
| Demonstrates | [[Euler's Formula]], [[Euler's Identity]], [[Rotation]] |
| Sources | Not listed on source page. |

## Prose

Set \(\theta=\pi\) in Euler's formula:

\[
e^{i\pi}=\cos(\pi)+i\sin(\pi).
\]

On the unit circle, this is a half-turn from \(1\) to \(-1\). Since \(\cos(\pi)=-1\) and \(\sin(\pi)=0\), the expression becomes:

\[
e^{i\pi}=-1,
\]

or equivalently:

\[
e^{i\pi}+1=0.
\]
