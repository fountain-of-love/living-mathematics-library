---
id: slice.euler-formula
type: framework
status: established
maturity: draft

name: Euler formula vertical slice

summary: >
  A compact vertical slice testing concepts, formulas, examples, teaching,
  provenance, and graph records around Euler's formula.

domains:
  - complex-analysis
  - geometry

entrypoint:
  - formula.euler

nodes:
  - concept.complex-number
  - concept.exponential-function
  - concept.imaginary-unit
  - concept.unit-circle
  - concept.angle
  - formula.euler
  - formula.euler-identity
  - concept.sine-function
  - concept.cosine-function
  - concept.rotation
  - definition.complex-exponential
  - example.euler-formula-half-turn
  - teaching.euler-formula
  - source.dlmf.4.2
  - source.dlmf.4.14

graph_record:
  - graph.euler-formula-slice.json

sources:
  - id: source.not-listed
    role: synthesis
    note: The slice structure is local synthesis from the repository architecture.

validation:
  status: unverified
  methods: []
---

# Euler Formula Vertical Slice

## Structured Facts

| Property | Value |
|---|---|
| Type | Vertical slice |
| Entrypoint | [[Euler's Formula]] |
| Status | Established |
| Maturity | Draft |
| Includes | Concepts, formulas, definition, source nodes, example, teaching page, graph record |

## Result

This slice tests whether the architecture can represent one mathematical object through the full stack:

```text
dictionary interface
   ↓
concept nodes
   ↓
formula node
   ↓
formula bond / specialization
   ↓
example
   ↓
teaching page
   ↓
source provenance
   ↓
machine-readable graph record
```

## Slice Verdict

The architecture is workable at draft scale. The relation category model is now started; the main remaining gaps are source selection for Euler's formula itself, completing the controlled bond vocabulary, and an automated graph builder.
