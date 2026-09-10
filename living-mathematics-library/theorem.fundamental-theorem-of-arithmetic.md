---
id: theorem.fundamental-theorem-of-arithmetic
type: theorem
status: established
maturity: draft

name: Fundamental theorem of arithmetic

summary: >
  Every integer greater than 1 is either prime or can be represented as a
  product of primes uniquely up to the order of the factors.

claim: >
  Every integer greater than 1 is either prime or can be represented as a
  product of primes, and this representation is unique up to the order of the
  prime factors.

domains:
  - number-theory

assumptions:
  - arithmetic over positive integers
  - standard definition of prime number

depends_on:
  - concept.integer
  - concept.prime-number
  - concept.divisibility
  - concept.factorization

related:
  - concept.unique-factorization
  - theorem.euclids-lemma
  - concept.prime-number

proof:
  status: not-yet-developed
  note: The theorem is established, but this library has not yet written or linked a proof node.

counterexamples:
  status: not-applicable
  scope: Within ordinary arithmetic over positive integers greater than 1.
  outside_scope: not-yet-developed

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.

validation:
  status: unverified
  methods: []
---

# Fundamental Theorem of Arithmetic

## Structured Facts

| Property | Value |
|---|---|
| Type | Theorem |
| Domain | [[Number Theory]] |
| Status | Established |
| Maturity | Draft |
| Depends on | [[Integer]], [[Prime Number]], [[Divisibility]], [[Factorization]] |
| Proof | Not yet developed locally |
| Counterexamples | Not applicable within stated assumptions |
| Sources | Not listed on source page. |

## Prose

The fundamental theorem of arithmetic says that prime numbers are the basic multiplicative building blocks of the positive integers. Once order is ignored, a number greater than 1 has only one prime factorization.

This theorem should eventually link to a proof node, especially one using [[Euclid's Lemma]], but the proof is not duplicated here yet.

## Proof-Run Audit

- [x] Object type identified
- [x] Stable ID assigned
- [x] Precise claim recorded
- [x] Assumptions recorded
- [x] Dependencies linked
- [x] Epistemic status assigned
- [x] Proof status recorded
- [x] Counterexample field preserved
- [x] Counterexample scope recorded
- [x] Structured source placeholder used
- [ ] Proof page linked
- [ ] External source linked
