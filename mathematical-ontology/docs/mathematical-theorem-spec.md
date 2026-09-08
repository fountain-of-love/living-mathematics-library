# Mathematical Theorem Spec

- **Status:** Draft 0.1
- **Purpose:** Page contract for established mathematical claims.
- **Companion:** [Mathematical Proof Spec](./mathematical-proof-spec.md)

## 1. Role

A theorem page records an established mathematical claim under explicit assumptions and scope.

It should state the claim, dependencies, proof status, known scope limits, and counterexample state without pretending that undocumented information is absent.

## 2. Contract Shape

Theorem pages begin with a compact contract:

```yaml
id: theorem.pythagorean-theorem
type: theorem
status: established

name: Pythagorean theorem

claim: >
  In a Euclidean right triangle, the square of the hypotenuse equals
  the sum of the squares of the other two sides.

assumptions:
  - Euclidean geometry
  - right triangle

depends_on:
  - concept.euclidean-plane
  - concept.right-triangle

proof:
  status: not-yet-developed

counterexamples:
  status: not-applicable
  scope: Within the stated assumptions.
  outside_scope: not-yet-developed

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.
```

The Markdown body may then add explanation, equivalent forms, examples, proof links, or boundary cases.

## 3. Required Fields

Every theorem page should include:

- `id`;
- `type`;
- `status`;
- `name`;
- `claim`;
- `assumptions`;
- `depends_on`;
- `proof`;
- `counterexamples`;
- `sources` or a clear provenance note.

## 4. Absence Discipline

Do not omit `proof`, `counterexamples`, or `sources` merely because they are unfinished.

Use values from [Mathematical Process](./mathematical-process.md):

- `unknown`;
- `not-applicable`;
- `not-yet-verified`;
- `not-yet-developed`;
- `open`;
- `not-known`.

## 5. Review Checklist

- The claim is precise and scoped.
- Assumptions are explicit.
- The proof status is visible even when the proof is not written locally.
- Counterexample status is scoped and explicit.
- Missing information is marked honestly instead of deleted.
- The page links to deeper references rather than reproducing entire surrounding domains.
