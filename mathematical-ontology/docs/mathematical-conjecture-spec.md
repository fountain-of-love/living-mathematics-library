# Mathematical Conjecture Spec

- **Status:** Draft 0.1
- **Purpose:** Page contract for open mathematical claims.
- **Companion:** [Mathematical Proof Spec](./mathematical-proof-spec.md)

## 1. Role

A conjecture page records a precise mathematical claim whose proof status is open, conditional, disputed, or not yet established.

It should keep the claim, dependencies, evidence, counterexample status, and proof status separate. This prevents evidence from quietly becoming proof.

## 2. Contract Shape

Conjecture pages begin with a compact contract:

```yaml
id: conjecture.riemann-hypothesis
type: conjecture
status: open

name: Riemann hypothesis

claim: >
  Every non-trivial zero of zeta(s) has real part 1/2.

depends_on:
  - concept.riemann-zeta-function

evidence:
  - numerical
  - theoretical-partial-results

counterexamples:
  status: not-known
  note: No counterexample is documented in this library.

proof:
  status: unproved

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.
```

The Markdown body may then add context, equivalent formulations, partial results, failed approaches, or links to proof attempts.

## 3. Required Fields

Every conjecture page should include:

- `id`;
- `type`;
- `status`;
- `name`;
- `claim`;
- `depends_on`;
- `evidence`;
- `counterexamples`;
- `proof`;
- `sources` or a clear provenance note.

## 4. Recommended Fields

Use these when they clarify the state of the problem:

- `equivalent_forms`;
- `known_cases`;
- `partial_results`;
- `failed_approaches`;
- `related_conjectures`;
- `deeper_references`.

## 5. Empty Field Discipline

Do not omit `evidence`, `counterexamples`, `proof`, or `sources` merely because they are incomplete.

Use explicit values from [Mathematical Process](./mathematical-process.md), such as `unknown`, `not-applicable`, `not-yet-verified`, `not-yet-developed`, `open`, and `not-known`.

## 6. Status Vocabulary

Use the weakest honest status:

- `open`;
- `conditional`;
- `proved`;
- `refuted`;
- `disputed`;
- `historical`.

## 7. Review Checklist

- The claim is precise enough to be true or false.
- Dependencies are explicit.
- Evidence is separated from proof.
- Counterexample status is stated honestly.
- The proof status is not stronger than the accepted mathematical record.
- Missing information is explicit rather than silently absent.
- Equivalent formulations do not silently replace the primary claim.
