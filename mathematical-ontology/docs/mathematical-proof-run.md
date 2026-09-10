# Mathematical Knowledge Engineering Proof Run

- **Status:** Completed first run 0.1
- **Purpose:** Standard pre-scale audit for the mathematical page-contract family.
- **Companion:** [Mathematical Process](./mathematical-process.md)
- **Run date:** 2026-09-08

## 1. Rule

Do not scale a new mathematical specification across hundreds of objects before running a five-item proof run.

The proof run is a small engineering audit. It checks whether the dictionary, process, absence vocabulary, formula provenance rule, and page contracts work on representative mathematical artifacts before the repository commits to a large rollout.

## 2. Five-Item Run Set

| Kind | Test artifact | Contract | Why this artifact is in the run |
|---|---|---|---|
| Definition / concept | `concept.complex-number` | [Concept Spec](./mathematical-concept-spec.md) | Tests whether a core definition can stay compact while linking prerequisites and uses. |
| Theorem | `theorem.fundamental-theorem-of-arithmetic` | [Theorem Spec](./mathematical-theorem-spec.md) | Tests assumptions, proof status, dependency links, and counterexample scope. |
| Formula | `formula.euler` | [Formula Spec](./mathematical-formula-spec.md) | Tests formula provenance, notation normalization, objects, and verification status. |
| Conjecture | `conjecture.riemann-hypothesis` | [Conjecture Spec](./mathematical-conjecture-spec.md) | Tests open status, evidence, dependencies, proof status, and counterexample language. |
| Experiment | `experiment.zeta-zero-spacing-001` | [Experiment Spec](./mathematical-experiment-spec.md) | Tests computational evidence, reproducibility, interpretation limits, and promotion paths. |

## 3. Applied Contract Sketches

These sketches were used to instantiate the first five flat starter nodes in [Living Mathematics Library](../../living-mathematics-library/). The nodes are draft pages, not final deep pages.

| Node | File |
|---|---|
| `concept.complex-number` | [concept.complex-number.md](../../living-mathematics-library/concept.complex-number.md) |
| `theorem.fundamental-theorem-of-arithmetic` | [theorem.fundamental-theorem-of-arithmetic.md](../../living-mathematics-library/theorem.fundamental-theorem-of-arithmetic.md) |
| `formula.euler` | [formula.euler.md](../../living-mathematics-library/formula.euler.md) |
| `conjecture.riemann-hypothesis` | [conjecture.riemann-hypothesis.md](../../living-mathematics-library/conjecture.riemann-hypothesis.md) |
| `experiment.zeta-zero-spacing-001` | [experiment.zeta-zero-spacing-001.md](../../living-mathematics-library/experiment.zeta-zero-spacing-001.md) |

### 3.1 `concept.complex-number`

```yaml
id: concept.complex-number
type: concept
status: established

name: Complex number

definition: >
  A number expressible as a + bi, where a,b are real
  and i^2 = -1.

prerequisites:
  - concept.real-number

related:
  - concept.complex-plane
  - concept.imaginary-unit

used_by:
  - formula.euler

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.
```

### 3.2 `theorem.fundamental-theorem-of-arithmetic`

```yaml
id: theorem.fundamental-theorem-of-arithmetic
type: theorem
status: established

name: Fundamental theorem of arithmetic

claim: >
  Every integer greater than 1 is either prime or can be expressed
  as a product of primes, uniquely up to the order of the factors.

assumptions:
  - arithmetic over positive integers

depends_on:
  - concept.integer
  - concept.prime-number
  - concept.divisibility

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

### 3.3 `formula.euler`

```yaml
id: formula.euler
type: formula
status: established

name: Euler's formula

source_expression: |
  e^(i theta) = cos(theta) + i sin(theta)

canonical_expression: |
  e^{i\theta} = \cos(\theta) + i\sin(\theta)

equivalence:
  status: established
  reason: notation normalization

notation_notes:
  - "theta is written canonically as \\theta."
  - "Function names are written canonically with LaTeX operators."

objects:
  - concept.complex-number
  - concept.exponential-function
  - concept.sine-function
  - concept.cosine-function

relations:
  - category: dependency
    type: derives
    target: formula.euler-identity
  - category: representation
    type: represents
    target: concept.rotation

verification:
  type: proof
  status: not-yet-developed

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.
```

### 3.4 `conjecture.riemann-hypothesis`

```yaml
id: conjecture.riemann-hypothesis
type: conjecture
status: open

name: Riemann hypothesis

claim: >
  Every non-trivial zero of zeta(s) has real part 1/2.

depends_on:
  - concept.riemann-zeta-function
  - concept.complex-zero

evidence:
  - numerical
  - theoretical-partial-results

counterexamples:
  status: not-known
  note: No counterexample is documented in this library or in the checked record.

proof:
  status: unproved

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.
```

### 3.5 `experiment.zeta-zero-spacing-001`

```yaml
id: experiment.zeta-zero-spacing-001
type: experiment
status: experimental

name: Zeta zero spacing experiment

question: >
  What spacing patterns appear among computed non-trivial zeros
  of the Riemann zeta function?

setup:
  inputs: not-yet-developed
  parameters: not-yet-developed
  algorithms: not-yet-developed
  data_sources: not-yet-developed

procedure:
  status: not-yet-developed

observations:
  status: not-yet-developed

interpretation:
  status: not-yet-developed

limitations:
  - not-yet-developed

follow_up:
  - Compare observations with known random-matrix-theory references.

does-not-establish:
  - conjecture.riemann-hypothesis

sources_and_artifacts:
  - id: source.not-listed
    role: artifact
    note: Not listed on source page.
```

## 4. Contract Audit Checklists

### 4.1 `concept.complex-number`

- [x] Object type identified
- [x] Stable ID assigned
- [x] One-sentence definition recorded
- [x] Prerequisites linked
- [x] Related concepts linked
- [x] Epistemic status assigned
- [x] Source field preserved
- [x] Empty source information marked honestly
- [ ] Structured external source linked
- [ ] Deep concept page created

### 4.2 `theorem.fundamental-theorem-of-arithmetic`

- [x] Object type identified
- [x] Stable ID assigned
- [x] Precise claim recorded
- [x] Assumptions recorded
- [x] Dependencies linked
- [x] Epistemic status assigned
- [x] Proof status recorded
- [x] Counterexample field preserved
- [x] Counterexample scope recorded
- [ ] Proof page linked
- [ ] Structured source linked

### 4.3 `formula.euler`

- [x] Object type identified
- [x] Stable ID assigned
- [x] Precise statement recorded
- [x] Source expression recorded
- [x] Notation normalized
- [x] Equivalence status recorded
- [x] Prerequisites linked
- [x] Related concepts linked
- [x] Epistemic status assigned
- [x] Source field preserved
- [x] Alternative notation recorded
- [x] Formula relationship recorded
- [ ] Proof page linked
- [ ] Computational experiment linked

### 4.4 `conjecture.riemann-hypothesis`

- [x] Object type identified
- [x] Stable ID assigned
- [x] Precise claim recorded
- [x] Dependency links recorded
- [x] Open epistemic status assigned
- [x] Evidence separated from proof
- [x] Counterexample status recorded
- [x] Proof status recorded
- [ ] Structured source linked
- [ ] Equivalent formulations linked
- [ ] Known partial results linked

### 4.5 `experiment.zeta-zero-spacing-001`

- [x] Object type identified
- [x] Stable ID assigned
- [x] Research question recorded
- [x] Experimental status assigned
- [x] Setup fields preserved
- [x] Missing setup marked honestly
- [x] Observation fields preserved
- [x] Limitations field preserved
- [x] Follow-up recorded
- [x] Does-not-establish boundary recorded
- [ ] Code artifact linked
- [ ] Data artifact linked
- [ ] Reproducibility check completed

## 5. Findings

### 5.1 What Worked?

- The contract family handled five different mathematical artifact types without needing one oversized schema.
- The one-sentence-first rule worked well for `concept.complex-number`.
- Structured facts plus prose gave the concept page both a predictable machine-readable spine and room for human explanation.
- `theorem.fundamental-theorem-of-arithmetic` showed why theorem pages need explicit `assumptions`, `proof`, and `counterexamples`.
- `formula.euler` confirmed that source notation and canonical notation must be separate fields.
- `conjecture.riemann-hypothesis` kept evidence, proof status, and counterexample status distinct.
- `experiment.zeta-zero-spacing-001` showed that unfinished computational work can still be represented honestly through explicit absence values.

### 5.2 What Fields Were Awkward?

- `sources: Not listed on source page.` is useful for extraction, but final canonical pages should prefer structured source records.
- Formula `relations` need controlled bond vocabulary inside the broader relation categories. The category layer now exists, but the bond lists are still early.
- Theorem `counterexamples.status: not-applicable` needs scope text, otherwise it can be mistaken for a global claim.
- Experiment setup wants nested fields, while the current experiment spec is still mostly section-oriented.

### 5.3 What Distinctions Were Missing?

- `definition` and `concept` are related but not identical. A concept can have several scoped definitions.
- `verification` and `proof` are related but not identical. A formula can be verified by proof, computation, source authority, or convention.
- `not-known` must mean "not documented here or in the checked record," not "mathematically impossible."
- `source_expression` should preserve observed notation even when the source's meaning is later normalized.
- Schema terms such as `status`, `source`, and `proof` must remain separate from mathematical entities such as complex number, integral, and Fourier transform.
- Obsidian display links should support human navigation while stable IDs support machine reasoning behind the scenes.

### 5.4 What Could Be Automated?

- ID generation from canonical names.
- Checking that every contract has required fields.
- Detecting silent omissions of interpretation-critical fields.
- Comparing `source_expression` and `canonical_expression` for recorded equivalence.
- Reporting unresolved concept IDs such as `concept.real-number` or `concept.complex-zero`.
- Building backlinks from `used_by`, `depends_on`, `objects`, and `relations`.

### 5.5 What Did The AI Misunderstand?

- It initially preferred a single universal schema when the better working pattern is a family of smaller contracts.
- It treated missing fields as things to omit until the absence vocabulary made incompleteness explicit.
- It risked rewriting formulas into canonical notation without preserving the source expression.
- It suggested proof-run candidates before documenting the proof run as an actual audit artifact.
- It did not initially distinguish "the dictionary as interface" from "the ontology as full domain model" sharply enough.

## 6. Spec Revisions Made From This Run

- Keep the page-contract family separate from the universal schema.
- Add theorem as a first-class contract.
- Add explicit absence vocabulary to the process and universal schema.
- Add formula provenance with `source_expression`, `canonical_expression`, `equivalence`, and `notation_notes`.
- Treat proof run as a required pre-scale practice, not a nice-to-have suggestion.
- Add the schema-term/entity distinction to the node spec and process.
- Add stable-ID guidance behind Obsidian display links.
- Add structured tables plus prose as the default human/machine page shape.

## 7. Scaling Gate

Before applying these specifications across a large batch of mathematical objects, confirm:

- the five-item proof run has been reviewed;
- awkward fields have either been accepted or revised;
- missing distinctions have been added to the relevant specs;
- automation candidates have been triaged;
- the AI misunderstanding list has been converted into guardrails.

If these checks are not complete, do not scale.
