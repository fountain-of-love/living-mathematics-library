# Universal Mathematical Knowledge-Node Schema

- **Status:** Draft 0.1
- **Schema identifier:** `math-node/0.1`
- **Purpose:** A common architecture for durable, human-readable, and machine-actionable mathematical knowledge.
- **Working companion:** [Knowledge Node Spec](./knowledge-node-spec.md)

## 1. Design Principle

Every item of mathematical knowledge is represented by the same node envelope and one type-specific payload.

The working page contracts use stable IDs of the form `concept.complex-number`, `formula.euler`, and `conjecture.riemann-hypothesis`. This schema's `title` field corresponds to the working-contract `name` field.

The initial knowledge-node types are:

```text
concept
formula
theorem
definition
conjecture
experiment
source
historical-event
person
proof
counterexample
analogy
```

The node `type` says **what kind of knowledge record this is**. It does not say what mathematical role its subject plays. Mathematical roles belong in `classification.semantic_roles` and may include `structure`, `operation`, `dynamics`, `representation`, `observation`, `event`, and `invariant`.

For example, Euler's formula has node type `formula`, but it may be classified semantically as a `representation` and a bridge between operations and dynamics. Keeping these two axes separate prevents unlike objects from being collapsed into a single taxonomy.

The schema follows five rules:

1. **One envelope:** identity, content, classification, provenance, relations, and governance have the same shape for every node.
2. **One discriminator:** `type` selects the rules for `attributes`.
3. **Explicit epistemic status:** established results, open claims, experiments, and analogies must not be confused.
4. **Typed edges:** relations state how two nodes are connected, not merely that they are related.
5. **Traceable claims:** externally acquired knowledge points to a `source` node and, where possible, a precise locator.

## 2. Canonical Node Envelope

The following YAML is the canonical authoring shape. JSON serializations use the same field names and values.

```yaml
schema_version: math-node/0.1
id: <type>.<stable-slug>
type: concept

title: Human-readable canonical title, also called `name` in page contracts
language: en
aliases: []
summary: One self-contained sentence describing the node.
content:
  statement: The principal mathematical or historical content.
  explanation: Optional Markdown explanation.
  notation: []

classification:
  branches: []
  semantic_roles: []
  keywords: []

epistemic:
  status: established
  scope: ""
  assumptions: []
  caveats: []

attributes: {}

relations: []
provenance: []

governance:
  maturity: seed
  review_status: unreviewed
  created_at: YYYY-MM-DD
  updated_at: YYYY-MM-DD
  deprecated: false
  replaced_by: null
```

### 2.1 Required Common Fields

| Field | Type | Requirement |
|---|---|---|
| `schema_version` | string | Required. Exactly `math-node/0.1` for this version. |
| `id` | string | Required. Stable, unique, lowercase identifier in the form `<type>.<stable-slug>`, with no meaning derived from its file path. |
| `type` | enum | Required. One of the twelve node types defined by this specification. |
| `title` | string | Required. Canonical display name. |
| `language` | string | Required. BCP 47 language tag for the human-readable fields. |
| `aliases` | alias[] | Required; may be empty. Alternative names must not create duplicate nodes. |
| `summary` | string | Required. A concise, context-independent description. |
| `content` | object | Required. Holds the primary statement and human explanation. |
| `classification` | object | Required. Separates subject classification from node type. |
| `epistemic` | object | Required. Records status, scope, assumptions, and caveats. |
| `attributes` | object | Required. Validated according to `type`. |
| `relations` | relation[] | Required; may be empty. Typed edges to other nodes. |
| `provenance` | provenance[] | Required; may be empty only for original or self-evident local material. |
| `governance` | object | Required. Records maturity, review state, and lifecycle. |

### 2.2 Alias

An alias is explicit about language and context:

```yaml
aliases:
  - name: Pythagoras's theorem
    language: en
    context: alternate spelling
```

`name` is required. `language` and `context` are optional. Symbols such as `PNT` or `RH` may also be aliases when their context is stated.

### 2.3 Content and Notation

```yaml
content:
  statement: In a Euclidean right triangle, the square of the hypotenuse...
  explanation: A Markdown explanation of meaning and use.
  notation:
    - symbol: c
      latex: c
      meaning: Length of the hypotenuse
      constraints: c > 0
```

`content.statement` is required. `explanation` and `notation` may be empty. Mathematical expressions use LaTeX without display delimiters so that renderers can choose inline or display presentation.

### 2.4 Classification

```yaml
classification:
  branches:
    - geometry
    - algebra
  semantic_roles:
    - structure
    - invariant
  keywords:
    - right triangle
    - Euclidean norm
```

`branches` names mathematical disciplines. `semantic_roles` describes the subject's role in the ontology graph. `keywords` supports discovery but has no formal meaning.

The initial semantic-role vocabulary is:

```text
structure, operation, dynamics, representation, observation, event, invariant,
object, operator, metric, reference-frame, equivalence-class, translation
```

More than one role is allowed. New roles may be proposed without inventing a new knowledge-node type.

### 2.5 Schema Terms Vs Mathematical Entities

Schema terms describe the record. They are the grammar of the knowledge system.

Mathematical entities describe mathematics. They are the subject matter being represented.

Examples of schema terms include `status`, `source`, `prerequisite`, `relationship`, `proof`, and `example`.

Examples of mathematical entities include complex number, group, ring, field, derivative, integral, and Fourier transform.

Machine reasoning must not collapse these layers. `status` is a field about a node; it is not itself a mathematical entity. `Fourier transform` is a mathematical entity; it is not a schema field.

Schema terms should be rendered as contract fields or inline code, not as mathematical concept links. Mathematical entities should receive stable IDs and may be rendered as human-facing Obsidian links.

### 2.6 Epistemic State

| Status | Meaning |
|---|---|
| `established` | Accepted under the stated assumptions and mathematical context. |
| `conditional` | Valid only if explicitly named unproved assumptions hold. |
| `open` | Neither proved nor refuted in the stated scope. |
| `refuted` | Disproved in the stated scope. |
| `experimental` | Supported primarily by computation, measurement, or exploration. |
| `heuristic` | Useful reasoning without the force of proof. |
| `interpretive` | Historical, pedagogical, or conceptual interpretation. |
| `disputed` | Reliable sources materially disagree. |

Status is always qualified by `scope` and `assumptions`. A statement can be established in Euclidean geometry and false in a different geometry without contradiction.

### 2.7 Explicit Absence

Empty fields are honest when their absence is explicit.

Do not silently remove missing information from a node when the field matters to interpretation. A missing `counterexamples` field must not be interpreted as "there are no counterexamples." It may only mean "this node has not recorded counterexample information."

Use these values when a field is known to be incomplete, unavailable, or not applicable:

| Value | Meaning |
|---|---|
| `unknown` | The ontology does not currently know the value. |
| `not-applicable` | The field does not apply to this node. |
| `not-yet-verified` | The field has been filled or claimed but has not been checked. |
| `not-yet-developed` | The section or field is intentionally deferred. |
| `open` | The mathematical question is unresolved in the stated scope. |
| `not-known` | No example, proof, source, or counterexample is documented in this ontology or in the checked record. |

When extracting from a source, prefer source-specific wording such as `Not listed on source page.` over deleting the field.

### 2.8 Governance

`maturity` records how fully the node has been developed:

```text
seed -> structured -> reviewed -> canonical
```

`review_status` is one of `unreviewed`, `in-review`, `approved`, or `changes-requested`. Maturity and review status are independent: a structurally complete node may still be unreviewed.

Identifiers are immutable. Renaming a title or moving a file does not change `id`. When two nodes are merged, the retired node remains addressable with `deprecated: true` and `replaced_by` set to the surviving node ID.

## 3. Type-Specific Attributes

Only `attributes` changes shape by node type. Fields marked **required** are the minimum contract for that type.

### 3.1 `concept`

A mathematical idea or object whose identity persists across particular statements or notations.

```yaml
attributes:
  definition: Required compact working definition.
  characteristic_properties: []
  examples: []
  non_examples: []
```

`definition` is required. It gives the concept node a self-contained working meaning; a separate authoritative or convention-specific `definition` node may provide the full definition through `defined-by`.

### 3.2 `formula`

A symbolic relation or computational expression.

```yaml
attributes:
  expressions:
    - source_expression: Required expression as observed in the source or local note.
      canonical_expression: Required normalized expression used by this ontology.
      equivalence:
        status: established
        reason: algebraic rewriting
      notation_notes: []
  variables: []
  conditions: []
  equality_kind: exact
```

`expressions` is required and non-empty. Each expression preserves formula provenance by separating observed source notation from canonical ontology notation. `equivalence.status` should be `established`, `not-yet-verified`, `unknown`, or another explicit absence value when appropriate. `equality_kind` is one of `exact`, `identity`, `definition`, `approximation`, `asymptotic`, `inequality`, or `recurrence`.

### 3.3 `theorem`

A mathematical proposition asserted as established within an explicit scope.

```yaml
attributes:
  hypotheses: []
  conclusion: Required proposition.
  proof_ids: []
  formal_system: Optional named axiomatic setting.
```

`conclusion` is required. A theorem's `epistemic.status` must be `established` or `conditional`. Each `proof_id` must resolve to a `proof` node that points back with `proves`.

### 3.4 `definition`

A record that introduces or fixes mathematical meaning.

```yaml
attributes:
  definiendum: Required term or symbol being defined.
  defining_statement: Required definition.
  domain: Required mathematical context.
  conventions: []
```

Definitions establish meaning rather than empirical truth. Conflicting conventions should be represented as scoped definition nodes, not silently merged.

### 3.5 `conjecture`

A mathematically precise proposition not established in the stated scope.

```yaml
attributes:
  proposition: Required proposition.
  evidence_for: []
  evidence_against: []
  resolution: null
```

`proposition` is required. Status is normally `open`, `conditional`, `refuted`, or `experimental`. If resolved, preserve this node and point `resolution` to the theorem or counterexample that resolved it.

### 3.6 `experiment`

A reproducible computational or empirical mathematical investigation.

```yaml
attributes:
  question: Required question or hypothesis.
  method: Required procedure.
  inputs: []
  outputs: []
  environment: {}
  reproducibility:
    artifacts: []
    random_seed: null
```

`question` and `method` are required. Inputs, code or notebook locations, software versions, precision, and random seeds should be recorded whenever they affect reproduction.

### 3.7 `source`

A citable origin of claims, formulas, proof presentations, data, or historical information.

```yaml
attributes:
  source_kind: book
  citation: Required human-readable citation.
  authors: []
  published_at: null
  version: null
  url: null
  accessed_at: null
  identifiers: {}
```

`source_kind` and `citation` are required. Suggested kinds are `article`, `book`, `web-page`, `dataset`, `software`, `manuscript`, `lecture`, `correspondence`, and `archive`.

### 3.8 `historical-event`

A temporally situated occurrence in mathematical history.

```yaml
attributes:
  start_date: Required date or date fragment.
  end_date: null
  date_precision: year
  location: null
  participants: []
  significance: Required historical significance.
```

`start_date`, `date_precision`, and `significance` are required. Approximate or disputed dates belong in `epistemic.caveats`; they must not be presented with false precision.

### 3.9 `person`

A person participating in the creation, communication, or history of mathematics.

```yaml
attributes:
  names:
    - value: Required full name.
      usage: canonical
  born: null
  died: null
  affiliations: []
```

`names` is required and non-empty. Contributions are represented as typed relations to mathematical nodes, preferably qualified by sources; biographical claims require provenance.

### 3.10 `proof`

A structured mathematical argument establishing a proposition under stated assumptions.

```yaml
attributes:
  proves: theorem.target-id
  strategy: Required proof strategy.
  steps: []
  dependencies: []
  completeness: complete
```

`proves`, `strategy`, and `steps` are required. `completeness` is one of `sketch`, `partial`, `complete`, or `machine-checked`. Machine-checked proofs should also record the proof assistant, version, and artifact.

### 3.11 `counterexample`

A construction showing that a universal or otherwise scoped proposition is false.

```yaml
attributes:
  refutes: Required target node ID.
  construction: Required object or case.
  verification: Required explanation or computation.
  minimality: null
```

`refutes`, `construction`, and `verification` are required. Refutation applies only to the target's recorded scope; a counterexample must not overstate what it disproves.

### 3.12 `analogy`

A deliberately limited mapping used to transfer intuition between domains.

```yaml
attributes:
  source_domain: Required familiar domain.
  target_domain: Required mathematical domain.
  mappings: []
  preserved_structure: []
  limitations: []
```

Both domains, at least one mapping, and at least one limitation are required. An analogy has `epistemic.status: heuristic` or `interpretive`; it cannot serve as a proof or as the sole evidence for a theorem.

## 4. Typed Relations

Every relation is directed and has this shape:

```yaml
relations:
  - category: evidence
    type: proved-by
    target: proof.euclid-pythagorean
    qualifiers:
      scope: Euclidean plane geometry
    provenance_refs:
      - prov-1
```

`category`, `type`, and `target` are required. `qualifiers` and `provenance_refs` may be empty. `type` is the specific bond predicate inside the broader relation category. Older drafts may use `predicate`; normalize that to `type` during ingestion. Inverse relations are declared by the vocabulary and may be computed; they need not be stored twice.

### 4.1 Relation Categories

| Category | Meaning | Examples |
|---|---|---|
| `transformation` | Operation, map, process, or conversion. | rotation, projection, embedding, derivative, integral |
| `structural-property` | Property, invariant, regularity, or observation. | symmetry, conservation, invariance, fixed point, periodicity |
| `equivalence` | Sameness, rewrite, isomorphism, or identity. | equivalent-to, rewrites-to, isomorphic-to |
| `dependency` | Prerequisite, assumption, construction, or derivation input. | depends-on, requires, derives-from, defined-by |
| `evidence` | Proof, counterexample, source, support, contradiction, or empirical evidence. | proves, refutes, supports, cites |
| `representation` | One object, model, picture, or coordinate system expressing another. | expresses, represents, models, parameterized-by |
| `analogy` | Heuristic cross-domain comparison with limits. | analogous-to, resembles, maps-onto |

The bond family is controlled within the appropriate category. Do not flatten all bonds into an untyped list, and do not confuse a transformation with a structural property merely because both are mathematically nearby.

### 4.2 Core Relation Vocabulary

| Category | Type | Inverse | Intended connection |
|---|---|---|---|
| `dependency` | `defines` | `defined-by` | Definition to concept, symbol, or object. |
| `representation` | `expresses` | `expressed-by` | Formula to concept, theorem, or relation. |
| `representation` | `states` | `stated-by` | Node to a formal or narrative statement. |
| `evidence` | `proves` | `proved-by` | Proof to theorem or resolved conjecture. |
| `evidence` | `refutes` | `refuted-by` | Counterexample or proof to a claim. |
| `evidence` | `supports` | `supported-by` | Evidence that raises confidence without proving. |
| `evidence` | `contradicts` | `contradicted-by` | Scoped logical or evidential tension. |
| `dependency` | `derives-from` | `derives` | Formal or explanatory derivation. |
| `dependency` | `depends-on` | `dependency-of` | Required mathematical dependency. |
| `dependency` | `generalizes` | `specializes` | Broader-to-narrower mathematical scope. |
| `equivalence` | `equivalent-to` | `equivalent-to` | Equivalence under stated conditions. |
| `equivalence` | `approximates` | `approximated-by` | Inexact relation with an explicit regime or error. |
| `representation` | `exemplifies` | `exemplified-by` | Instance-to-pattern connection. |
| `analogy` | `analogous-to` | `analogous-to` | Heuristic comparison with stated limits. |
| `evidence` | `cites` | `cited-by` | Explicit use of a source. |
| `evidence` | `attributed-to` | `credited-with` | Historically sourced attribution. |
| `dependency` | `precedes` | `follows` | Historical or logical ordering. |
| `dependency` | `supersedes` | `superseded-by` | New node replaces an older account without erasing it. |

Relations with conditions, transformations, error bounds, or disputed attribution must put those qualifications in `qualifiers`. A generic `related-to` edge should be avoided when a more precise predicate is available.

## 5. Provenance

Provenance records why a node or relation may be trusted and where it can be checked.

```yaml
provenance:
  - id: prov-1
    source_id: source.euclid-elements-heath
    locator:
      work_part: Book I, Proposition 47
      page: null
      url_fragment: null
    supports:
      - content.statement
      - attributes.conclusion
    note: Translation and numbering follow the cited edition.
```

Each entry requires `id`, `source_id`, and at least one value in `supports`. `source_id` must resolve to a `source` node. `locator` should be as precise as the source permits. A URL alone is not sufficient when version, section, equation, theorem number, timestamp, or page is available.

Original local reasoning may use an empty `provenance` array while at maturity `seed`. Promotion to `reviewed` or `canonical` requires provenance for historical claims, attributions, imported definitions, and nontrivial mathematical claims.

## 6. Validation Invariants

A conforming node satisfies all of these rules:

1. `id` is globally unique and never changes after publication.
2. `type` is one of the twelve declared node types.
3. `attributes` satisfies the contract selected by `type`.
4. In a published graph, every relation target, proof reference, resolution, replacement, participant, and provenance source resolves to an existing node. An ingestion tool may temporarily quarantine unresolved references outside the canonical node.
5. Every mathematical assertion states its applicable scope and assumptions when they are not universal or obvious from the formal context; interpretation-critical missing fields use explicit absence values rather than silent omission; formula normalizations preserve source expressions, canonical expressions, and equivalence status.
6. `theorem` nodes are `established` or `conditional`; unresolved propositions are `conjecture` nodes.
7. `proof.attributes.proves` agrees with a `proves` relation, and the target points back through the derived inverse `proved-by`.
8. `counterexample.attributes.refutes` agrees with a `refutes` relation.
9. An `analogy` records limitations and is never treated as deductive evidence.
10. An `experiment` records enough environment and artifact information to explain its reproducibility limits.
11. Imported or attributed claims have provenance, including an access date and observed version when the source can change.
12. Deprecation preserves history: a deprecated node is not deleted and names its replacement when one exists.
13. Relations use the most specific valid predicate; semantic similarity alone does not imply identity, equivalence, causation, or proof; schema terms must not be promoted into mathematical concept nodes unless the node explicitly documents the schema.

## 7. Complete Node Example

This node assumes that the referenced formula, proof, source, and concept nodes also exist in the surrounding graph.

```yaml
schema_version: math-node/0.1
id: theorem.pythagorean-theorem
type: theorem

title: Pythagorean theorem
language: en
aliases:
  - name: Pythagoras's theorem
    language: en
    context: alternate spelling
summary: Relates the side lengths of a right triangle in Euclidean geometry.
content:
  statement: For a right triangle with legs a and b and hypotenuse c, a^2 + b^2 = c^2.
  explanation: The theorem identifies the squared Euclidean length as an additive invariant across orthogonal components.
  notation:
    - symbol: a, b
      latex: a,b
      meaning: Lengths of the two legs
      constraints: a > 0 and b > 0
    - symbol: c
      latex: c
      meaning: Length of the hypotenuse
      constraints: c > 0

classification:
  branches:
    - Euclidean geometry
    - linear algebra
  semantic_roles:
    - invariant
    - translation
  keywords:
    - right triangle
    - Euclidean norm

epistemic:
  status: established
  scope: Euclidean geometry
  assumptions:
    - The triangle has one right angle.
  caveats:
    - The unmodified formula does not describe arbitrary triangles in non-Euclidean geometry.

attributes:
  hypotheses:
    - a, b, and c are side lengths of a Euclidean right triangle.
    - c is opposite the right angle.
  conclusion: a^2 + b^2 = c^2
  proof_ids:
    - proof.euclid-elements-i-47
  formal_system: Euclidean plane geometry

relations:
  - category: representation
    type: expressed-by
    target: formula.pythagorean-identity
    qualifiers: {}
    provenance_refs:
      - prov-1
  - category: evidence
    type: proved-by
    target: proof.euclid-elements-i-47
    qualifiers:
      presentation: Euclid's geometric proof
    provenance_refs:
      - prov-1
  - category: dependency
    type: depends-on
    target: definition.right-triangle
    qualifiers:
      role: supplies the right-angle hypothesis
    provenance_refs: []

provenance:
  - id: prov-1
    source_id: source.euclid-elements-book-i
    locator:
      work_part: Proposition 47
      page: null
      url_fragment: null
    supports:
      - content.statement
      - attributes.conclusion
    note: Historical attribution and proposition numbering require an edition-specific source node.

governance:
  maturity: structured
  review_status: unreviewed
  created_at: 2026-09-07
  updated_at: 2026-09-07
  deprecated: false
  replaced_by: null
```

## 8. Authoring and Storage Convention

Use one Markdown file per node. Store the canonical fields as YAML front matter and the longer `content.explanation` as Markdown when authoring comfort matters. A serializer may combine the front matter and body into the canonical envelope.

Recommended paths are organizational, not semantic identities:

```text
nodes/
  concepts/
  formulas/
  theorems/
  definitions/
  conjectures/
  experiments/
  sources/
  historical-events/
  people/
  proofs/
  counterexamples/
  analogies/
```

Filenames use deterministic lowercase slugs. The permanent `id`, not the folder or filename, is the source of truth.

## 9. Extension Rule

The common envelope is the stable boundary. Extensions belong under a namespaced key in `attributes` or `classification`, never as uncoordinated top-level fields. A proposed thirteenth node type should be added only when its identity, required attributes, epistemic behavior, and relations cannot be expressed clearly by an existing type.

This keeps the schema small enough to understand, strict enough to validate, and open enough to grow with the ontology.
