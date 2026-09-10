---
id: teaching.euler-formula
type: teaching
status: established
maturity: draft

name: Teaching Euler's formula

summary: >
  A teaching-oriented page for explaining Euler's formula as rotation on the
  unit circle before presenting it as a complex-analytic identity.

domains:
  - complex-analysis
  - geometry

teaches:
  - formula.euler

audience:
  level:
    - secondary
    - undergraduate
  ordinary_picture: true
  university_checkpoint: true

prerequisites:
  - concept.complex-number
  - concept.imaginary-unit
  - concept.unit-circle
  - concept.angle
  - concept.sine-function
  - concept.cosine-function

relations:
  - category: representation
    type: teaches
    target: formula.euler
  - category: representation
    type: uses-picture
    target: concept.unit-circle
  - category: representation
    type: uses-example
    target: example.euler-formula-half-turn

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.

validation:
  status: unverified
  methods: []
---

# Teaching Euler's Formula

## Structured Facts

| Property | Value |
|---|---|
| Type | Teaching page |
| Domain | [[Complex Analysis]], [[Geometry]] |
| Status | Established |
| Maturity | Draft |
| Teaches | [[Euler's Formula]] |
| Uses | [[Unit Circle]], [[Euler Formula Half-Turn Example]] |
| Sources | Not listed on source page. |

## Ordinary Picture

Imagine a point moving around the unit circle. The angle tells you how far it has rotated. The coordinates of the point are \((\cos\theta,\sin\theta)\).

Euler's formula says that the same motion can be written as one complex number:

\[
e^{i\theta}=\cos\theta+i\sin\theta.
\]

## University Checkpoint

At the more formal level, this page should eventually connect the picture to the complex exponential, power series, and analytic continuation. Those details are deliberately linked outward rather than duplicated here.
