The current mathematics repository architecture

The schema is **small, typed, provenance-first, and extensible**. The repository already has conceptual ingredients: vocabulary, concepts, formulas, formula bonds, experiments, references, and raw research and explicitly wants graph navigation by definition, example, transformation, invariant, source, evidence, limitation, and open question.

The key is to make those things **actual nodes and typed edges**, without turning the repository into a giant ontology project.

## 1. The proposed model

Define a mathematical knowledge node as:

```
NODE
│
├── identity
├── classification
├── meaning
├── mathematical content
├── relationships
├── provenance
├── epistemic status
├── validation
└── presentation
```

And use one universal frontmatter contract, with type-specific extensions.
The core schema:

# Mathematical Knowledge Node Schema

## 1. Purpose

A Mathematical Knowledge Node is a durable, addressable unit of mathematical knowledge.

The node must be:

- readable as Markdown by humans;
- addressable by a stable identifier;
- classifiable by mathematical type;
- connected to other nodes through typed relationships;
- explicit about provenance and epistemic status;
- honest about unknown or unverified information;
- usable as an input to graph-building and machine-assisted reasoning.

Markdown is the human interface. YAML frontmatter provides the structured interface.

---

## 2. Universal node contract

Every canonical knowledge node SHOULD contain:

```
---
id: <stable-id>
type: <node-type>
name: <canonical-name>

status: <knowledge-status>
maturity: <development-status>

domains:
  - <domain>

summary: >
  One-sentence definition or orientation.

aliases:
  - <alternative-name>

prerequisites:
  - <node-id>

relations:
  - type: <relation-type>
    target: <node-id>

sources:
  - id: <source-id>
    role: <source-role>

validation:
  status: <validation-status>

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---
```

The body of the Markdown document contains the human-readable mathematical exposition.

---

# 3. Stable identity

## `id`

Every node receives a permanent identifier.

Recommended form:

```
concept.complex-number
formula.euler
theorem.prime-number-theorem
conjecture.riemann-hypothesis
experiment.zeta-zero-spacing-001
definition.group
source.dlmf
```

IDs should be semantic, stable, lowercase, and independent of filenames.

A filename may change.

The node ID should not.

---

## `type`

The first version should support:

```
vocabulary
concept
definition
formula
theorem
lemma
proposition
corollary
conjecture
proof
example
teaching
counterexample
algorithm
transformation
invariant
experiment
observation
framework
historical-event
person
source
research-question
```

`teaching` is a presentation-oriented node type. It may teach or sequence mathematical nodes, but it must not change the epistemic status of the mathematics it presents.

Do not require every type to have a separate folder immediately.

The type primarily tells a machine:

> What kind of thing is this?

---

# 4. Knowledge status

`status` describes the epistemic status of the mathematical claim.

Controlled vocabulary:

```
established
defined
proved
disproved
conjectured
empirical
experimental
heuristic
speculative
historical
open
unknown
```

Examples:

```
status: established
```

for a standard mathematical concept.

```
status: conjectured
```

for the Riemann Hypothesis.

```
status: experimental
```

for a numerical pattern observed in an experiment.

This field is deliberately separate from `maturity`.

---

# 5. Development maturity

`maturity` describes the state of the repository's treatment of the node, not the truth of the mathematics.

Controlled vocabulary:

```
seed
draft
developing
reviewed
mature
deprecated
```

For example:

```
status: established
maturity: seed
```

means:

> The mathematics is established, but our documentation is still minimal.

Whereas:

```
status: experimental
maturity: mature
```

means:

> This is a well-documented experiment, but the result remains experimental.

Never use maturity as a substitute for epistemic status.

---

# 6. Canonical name and aliases

```
name: Fourier transform

aliases:
  - Fourier transformation
  - Fourier integral transform
```

Aliases are navigation aids.

They do not create additional mathematical entities unless explicitly declared as separate nodes.

---

# 7. Domains

Use broad mathematical domains rather than overly detailed taxonomies.

Examples:

```
domains:
  - analysis
  - complex-analysis
```

or:

```
domains:
  - number-theory
  - analytic-number-theory
```

Possible initial vocabulary:

```
arithmetic
algebra
geometry
topology
analysis
complex-analysis
number-theory
probability
statistics
combinatorics
logic
set-theory
differential-equations
dynamical-systems
mathematical-physics
numerical-analysis
category-theory
```

Do not attempt to settle the entire classification of mathematics at v0.1.

---

# 8. Summary

Every node should have a short summary.

For example:

```
summary: >
  A complex number is a number of the form a + bi,
  where a and b are real numbers and i² = -1.
```

This is the machine-readable "one sentence first" interface.

The full explanation belongs in the Markdown body.

---

# 9. Prerequisites

```
prerequisites:
  - concept.real-number
  - concept.ordered-pair
```

This means:

> These nodes are useful or necessary for understanding this node.

Prerequisites are directional.

If:

```
A → B
```

means "A is a prerequisite for B", then B should not also declare A as a prerequisite of B unless that is genuinely meaningful.

---

# 10. Typed relations

The graph should not use a generic `related-to` relation except as a last resort.

Use two relation layers:

1. `category`: the broad kind of relation.
2. `type`: the specific bond or predicate inside that category.

Core relation categories:

```
transformation
structural-property
equivalence
dependency
evidence
representation
analogy
```

The bond family is a controlled vocabulary within the chosen category. For example, `rotation`, `projection`, `embedding`, `derivative`, and `integral` usually participate as operations or transformations. `symmetry`, `conservation`, `invariance`, `fixed point`, and `periodicity` are structural properties or observations. `resonance`, `interference`, and `correction/residue` need an explicit category choice because they can play different roles in different contexts.

Example bond types include:

| Category | Bond types |
|---|---|
| `transformation` | `transforms-to`, `projects-to`, `embeds`, `differentiates`, `integrates` |
| `structural-property` | `preserves`, `has-invariant`, `has-symmetry`, `has-fixed-point`, `has-periodicity` |
| `equivalence` | `equivalent-to`, `approximately-equivalent-to`, `normalizes-to` |
| `dependency` | `defines`, `depends-on`, `required-for`, `derived-from`, `special-case-of`, `extends` |
| `evidence` | `supports`, `does-not-support`, `evidence-for`, `evidence-against`, `tests`, `cites` |
| `representation` | `represents`, `expresses`, `example-of`, `explains` |
| `analogy` | `analogous-to`, `contrasts-with`, `confused-with` |

Example:

```
relations:
  - category: dependency
    type: special-case-of
    target: formula.euler
  - category: transformation
    type: transforms-to
    target: formula.euler-identity
  - category: dependency
    type: prerequisite-for
    target: concept.fourier-transform
```

The graph then carries meaning rather than merely connectivity.

---

# 11. Formula-specific fields

A formula node MAY additionally contain:

```
expression: |
  e^{i\theta} = \cos(\theta) + i\sin(\theta)

notation:
  canonical: |
    e^{i\theta} = \cos(\theta) + i\sin(\theta)

  alternatives:
    - |
      \exp(i\theta) = \cos\theta + i\sin\theta

variables:
  - symbol: theta
    meaning: angle
    domain: real-number

conditions:
  - theta: real-number
```

This separates:

> the mathematical object

from:

> the notation used to express it.

That distinction is particularly important when material comes from multiple sources.

---

# 12. Definition-specific fields

```
defined_term: group

definition: >
  A set equipped with a binary operation satisfying closure,
  associativity, identity, and inverse axioms.
```

Definitions should identify what they define:

```
defines:
  - concept.group
```

---

# 13. Theorem-specific fields

```
claim: >
  Every integer greater than 1 can be represented as a product
  of prime numbers, uniquely up to ordering.

hypotheses:
  - concept.integer
  - condition.integer-greater-than-one

conclusion:
  - concept.unique-prime-factorization
```

A theorem should additionally have:

```
proof:
  status: proved
  node: proof.fundamental-theorem-of-arithmetic
```

or:

```
proof:
  status: not-yet-added
```

The latter must **not** imply that the theorem itself is unproved.

---

# 14. Conjecture-specific fields

```
claim: >
  Every non-trivial zero of the Riemann zeta function
  has real part 1/2.

proof:
  status: open

evidence:
  - type: numerical
    node: experiment.riemann-zero-verification

known-results:
  - theorem.zero-free-region
```

The distinction is essential:

```
conjecture status = open
documentation maturity = mature
numerical evidence = strong
proof = absent
```

These are four different facts.

---

# 15. Experiment-specific fields

Experiments should have a stronger contract.

```
question: >
  Does the observed spacing of zeta zeros exhibit
  the proposed scaling pattern?

hypothesis: >
  ...

method:
  node: experiment-method.zeta-zero-spacing
  code: experiments/zeta-zero-spacing.py

data:
  source: data/zeta-zero-spacing.csv

result: >
  ...

supports:
  - observation.zeta-zero-spacing-pattern

does-not-establish:
  - conjecture.riemann-hypothesis

limitations:
  - finite-sample
  - numerical-precision
  - model-selection
```

This is one of the most important safeguards in the entire schema.

An experiment must explicitly say what it **does not establish**.

That fits the repository's existing principle that experiments and established mathematics must remain distinguishable. GitHub+1 

---

# 16. Provenance

Every externally sourced mathematical claim should be traceable.

Use:

```
sources:
  - id: source.dlmf.4.2
    role: reference
  - id: source.hardy-wright
    role: textbook
```

Possible source roles:

```
primary
definition
proof
reference
historical
notation
data
validation
secondary
```

A source node can contain:

```
id: source.dlmf.4.2
type: source

name: NIST Digital Library of Mathematical Functions
source-kind: reference

locator: "Section 4.2"

url: <URL>

accessed: 2026-09-07
```

The important principle is:

> A source is itself a node.

That allows provenance to become part of the graph.

---

# 17. Validation

Use a separate validation object.

```
validation:
  status: verified
  checked: 2026-09-07
  methods:
    - source-comparison
    - symbolic-check
```

Controlled vocabulary:

```
unverified
partially-verified
verified
machine-checked
human-reviewed
source-confirmed
```

Multiple methods may coexist.

For example:

```
validation:
  status: verified
  methods:
    - source-confirmed
    - symbolic-check
```

---

# 18. Absence must be explicit

Never interpret a missing field as "none exists."

Use:

```
proof:
  status: unknown
```

or:

```
counterexample:
  status: not-known
```

or:

```
experiment:
  status: not-applicable
```

Distinguish:

```
unknown
not-known
not-applicable
not-yet-checked
not-yet-added
none-known
```

This is directly inspired by the strongest knowledge-engineering lesson in `gemstones`: empty fields should remain honest rather than silently becoming false completeness. GitHub 

---

# 19. Presentation metadata

Because the repository has an explicit teaching philosophy, nodes may also carry:

```
teaching:
  level:
    - secondary
    - undergraduate

  ordinary-picture: true

  university-checkpoint: true
```

But teaching metadata must never become part of the mathematical truth model.

It describes presentation, not mathematics.

---

# 20. Complete example: Euler's formula

```
---
id: formula.euler
type: formula
name: Euler's formula

status: established
maturity: reviewed

domains:
  - complex-analysis
  - geometry

summary: >
  Euler's formula connects complex exponentials with
  sine and cosine.

aliases:
  - Euler formula

prerequisites:
  - concept.complex-number
  - concept.exponential-function
  - concept.sine-function
  - concept.cosine-function

expression: |
  e^{i\theta} = \cos(\theta) + i\sin(\theta)

variables:
  - symbol: theta
    meaning: real angle
    domain: real-number

conditions:
  - theta is real

relations:
  - category: representation
    type: represents
    target: concept.rotation

  - category: dependency
    type: special-case-of
    target: definition.complex-exponential

  - category: dependency
    type: derives
    target: formula.euler-identity

  - type: prerequisite-for
    target: concept.fourier-transform

sources:
  - id: source.dlmf
    role: reference

validation:
  status: verified
  methods:
    - source-confirmed
    - symbolic-check

teaching:
  level:
    - secondary
    - undergraduate
  ordinary-picture: true
  university-checkpoint: true

created: 2026-09-07
updated: 2026-09-07
---
```

Then the Markdown body can remain beautifully human:

```
# Euler's Formula

## The Ordinary Picture

Imagine a point moving around a circle...

## The Mathematical Object

...

## The Formula

\[
e^{i\theta}=\cos\theta+i\sin\theta
\]

## What Changes Representation?

The same rotational structure can be described using
complex exponentials rather than coordinates on a circle.

## Common Confusion

...

## University Checkpoint

What structure is preserved when rotation is represented
as multiplication by a complex exponential?

## Sources

...
```

This is exactly the dual interface we want:

**human-readable Markdown + machine-readable node.**

---

# 21. The graph is then almost automatic

From those fields, a graph generator can construct:

```
Complex Number
      │
      ├── prerequisite-for ──→ Euler's Formula
      │                            │
      │                            ├── represents ──→ Rotation
      │                            │
      │                            ├── derives ──→ Euler's Identity
      │                            │
      │                            └── prerequisite-for ──→ Fourier Transform
      │
      └── related-to ──→ Complex Plane
```

And separately:

```
Euler's Formula
      │
      └── source ──→ DLMF
                         │
                         └── source-confirmed
```

And separately again:

```
Euler's Formula
      │
      └── validation
              ├── symbolic-check
              └── source-confirmed
```

This is why I strongly recommend **typed edges rather than a generic "related" graph**.

---
# 22. The minimum viable schema

I would **not** make all of the above mandatory.

For v0.1, only require:

```
id:
type:
name:
status:
maturity:
summary:
```

And strongly recommend:

```
domains:
prerequisites:
relations:
sources:
validation:
```

Everything else is type-specific.

This matters because `gemstones` succeeded partly by having a reusable contract without requiring the entire universe to be encoded before a page can exist. GitHub 

---

# 23. The folder structure I would use

I would change the current repository only modestly:

```
living-mathematics-library/
│
├── schema/
│   ├── knowledge-node-spec.md
│   ├── relation-vocabulary.md
│   ├── status-vocabulary.md
│   └── validation-rules.md
│
├── dictionary/
│   └── mathematical-dictionary.md
│
├── concepts/
├── definitions/
├── formulas/
├── theorems/
├── conjectures/
├── proofs/
├── transformations/
├── invariants/
├── examples/
├── counterexamples/
├── experiments/
├── bonds/
├── sources/
├── research/
└── ...
```

But I would **not migrate everything immediately**.

Start with maybe **five canonical nodes**:

```
concept.complex-number
formula.euler
concept.fourier-transform
conjecture.riemann-hypothesis
experiment.zeta-zero-spacing-001
```

Those five expose almost every important design problem.

---

# 24. One critical rule: Markdown remains authoritative

I would explicitly establish:

> **The Markdown node is the canonical human-readable source of truth.**

The graph is derived from it.

So:

```
Markdown
   ↓
frontmatter parser
   ↓
node records
   ↓
graph.json
   ↓
indexes / visualization / AI retrieval
```

Not:

```
database
   ↓
generate Markdown
```

at least initially.

That preserves the openness and inspectability of GitHub while allowing machine use later.

It also fits `gemstones`, where the reusable Markdown contract, dictionary, process, and proof-run are the core engineering artifacts. GitHub 

---

# 25. The resulting architecture

I would describe the finished system like this:

```
                         SOURCES
                            │
                       provenance
                            │
                            ▼
┌───────────┐       ┌──────────────┐
│ VOCABULARY│──────▶│     NODE     │
└───────────┘       └──────┬───────┘
                           │
            ┌──────────────┼───────────────┐
            ▼              ▼               ▼
        CONCEPT         FORMULA          THEOREM
            │              │               │
            │              ▼               ▼
            │            BOND            PROOF
            │              │
            └──────────────┼───────────────┐
                           ▼               ▼
                     TRANSFORMATION    EXPERIMENT
                           │               │
                           └───────┬───────┘
                                   ▼
                                EVIDENCE
```

Running through the entire graph:

```
identity
type
status
provenance
validation
prerequisites
relationships
representation
invariants
limitations
```

That is the architecture I would actually build.

## My strongest recommendation

Call it:

> **Mathematical Knowledge Node Schema v0.1**

The ontology can emerge from the nodes.

This is an important distinction.

The current `mathematical-ontology` work is ambitious. It already distinguishes objects, structures, operations, observations, invariants, projections, and translations.  When we  encode all of that directly into a formal ontology now, we risk spending months designing the model instead of discovering what the corpus actually needs.

Instead:

**nodes → relationships → repeated patterns → ontology.**

That is the \ incremental spirit that makes an experiment useful: one specification, one repeatable process, a dictionary interface, and a small proof run before scaling. 

### The first five-node proof run I'd use

I would make these the test suite:

1. **Concept:** `concept.complex-number`
2. **Formula:** `formula.euler`
3. **Theorem:** `theorem.fundamental-theorem-of-arithmetic`
4. **Conjecture:** `conjecture.riemann-hypothesis`
5. **Experiment:** `experiment.zeta-zero-spacing-001`

If the schema can represent those five cleanly **without awkward exceptions**, there is a foundation.
