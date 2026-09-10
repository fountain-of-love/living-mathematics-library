---
id: formula.euler
type: formula
status: established
maturity: draft

name: Euler's formula

summary: >
  Euler's formula connects complex exponentials with sine and cosine.

statement: |
  e^(iθ) = cos(θ) + i sin(θ)

source_expression: |
  e^(iθ) = cos(θ) + i sin(θ)

canonical_expression: |
  e^{i\theta} = \cos(\theta) + i\sin(\theta)

equivalence:
  status: established
  reason: notation normalization

domains:
  - complex-analysis
  - geometry

prerequisites:
  - concept.complex-number
  - concept.exponential-function
  - concept.imaginary-unit
  - concept.angle
  - concept.sine-function
  - concept.cosine-function

objects:
  - concept.complex-number
  - concept.exponential-function
  - concept.imaginary-unit
  - concept.sine-function
  - concept.cosine-function

related:
  - formula.euler-identity
  - concept.unit-circle
  - concept.rotation
  - concept.fourier-transform
  - definition.complex-exponential
  - example.euler-formula-half-turn
  - teaching.euler-formula

relations:
  - category: representation
    type: expresses
    target: concept.complex-number
  - category: representation
    type: expresses
    target: concept.exponential-function
  - category: representation
    type: expresses
    target: concept.sine-function
  - category: representation
    type: expresses
    target: concept.cosine-function
  - category: dependency
    type: uses
    target: concept.imaginary-unit
  - category: representation
    type: represents
    target: concept.rotation
  - category: representation
    type: geometric-model
    target: concept.unit-circle
  - category: representation
    type: parameterized-by
    target: concept.angle
  - category: dependency
    type: derives-from
    target: definition.complex-exponential
  - category: dependency
    type: specializes-to
    target: formula.euler-identity
    condition: "θ = π"

bonds:
  - type: special-case
    target: formula.euler-identity
    condition: "θ = π"

proof:
  status: not-yet-developed
  sources:
    - id: source.not-listed
      role: proof
      note: Not listed on source page.

verification:
  type: proof
  status: not-yet-developed

notation:
  canonical: "e^(iθ) = cos(θ) + i sin(θ)"
  alternatives:
    - "exp(iθ) = cos θ + i sin θ"

notation_notes:
  - "The starter statement uses plain-text exponent notation; the canonical expression uses LaTeX notation."
  - "Both forms encode the same identity."

sources:
  - id: source.not-listed
    role: reference
    note: No specific source statement for Euler's formula has been selected yet.
  - id: source.dlmf.4.2
    role: component-reference
    note: Local DLMF source for exponential-function context.
  - id: source.dlmf.4.14
    role: component-reference
    note: Local DLMF source for sine and cosine context.

validation:
  status: unverified
  methods: []
---

# Euler's Formula

## Structured Facts

| Property | Value |
|---|---|
| Type | Formula |
| Domain | [[Complex Analysis]], [[Geometry]] |
| Status | Established |
| Maturity | Draft |
| Prerequisites | [[Complex Number]], [[Exponential Function]], [[Imaginary Unit]], [[Angle]], [[Sine Function]], [[Cosine Function]] |
| Related | [[Euler's Identity]], [[Unit Circle]], [[Rotation]], [[Fourier Transform]] |
| Sources | Formula source not yet selected; component context from [[DLMF §4.2 Definitions]] and [[DLMF §4.14 Definitions and Periodicity]]. |

## Prose

Euler's formula says that complex exponential motion can be represented through the ordinary trigonometric coordinates of the unit circle.

It is useful here as a bridge between [[Complex Number]], [[Imaginary Unit]], [[Rotation]], [[Unit Circle]], [[Sine Function]], [[Cosine Function]], and later Fourier-style decompositions. The page is intentionally compact: deeper proof, historical source work, examples, and teaching material become linked artifacts rather than being folded into this one formula page.

## Slice Links

- Example: [[Euler Formula Half-Turn Example]]
- Teaching: [[Teaching Euler's Formula]]
- Graph record: [graph.euler-formula-slice.json](./graph.euler-formula-slice.json)

## Proof-Run Audit

- [x] Object type identified
- [x] Stable ID assigned
- [x] Precise statement recorded
- [x] Notation normalized
- [x] Prerequisites linked
- [x] Related concepts linked
- [x] Epistemic status assigned
- [x] Source recorded
- [x] Alternative notation recorded
- [x] Formula relationship recorded
- [ ] Proof page linked
- [ ] Local proof or verification completed
- [ ] Computational experiment linked
