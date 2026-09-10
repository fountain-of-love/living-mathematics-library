# Knowledge Node Spec

- **Status:** Starter spec
- **Purpose:** Minimal stable contract for mathematical knowledge nodes.
- **Full working draft:** [mathematical-ontology/docs/knowledge-node-spec.md](../mathematical-ontology/docs/knowledge-node-spec.md)

## Minimum Contract

Every published node should begin with a small structured contract:

```yaml
id: concept.example
type: concept
name: Example
status: established
maturity: seed
summary: >
  One-sentence definition or orientation.
```

Strongly recommended:

```yaml
domains: []
prerequisites: []
relations:
  - category: dependency
    type: depends-on
    target: concept.example-prerequisite
sources:
  - id: source.example
    role: reference
validation:
  status: unverified
  methods: []
```

## Provenance And Validation

A source is itself a node.

Validation is separate from provenance:

```yaml
validation:
  status: verified
  methods:
    - source-confirmed
    - symbolic-check
```

Relations use [Relation Vocabulary](./relation-vocabulary.md): `category` names the broad relation family, while `type` names the specific bond inside that category.

## Schema Terms Vs Mathematical Entities

Schema terms describe the record:

- `status`
- `source`
- `prerequisite`
- `relationship`
- `proof`
- `example`

Mathematical entities describe mathematics:

- complex number
- group
- ring
- field
- derivative
- integral
- Fourier transform

Presentation artifacts such as `teaching` pages may organize how mathematics is explained, but they must not change the truth status of the mathematical nodes they teach.

Do not turn schema terms into mathematical concept links unless documenting the schema itself.

## Human Links And Stable IDs

Human Markdown:

```markdown
[[Complex Number]]
[[Exponential Function]]
[[Euler's Formula]]
```

Machine structure:

```yaml
related:
  - concept.complex-number
  - concept.exponential-function
  - formula.euler
```

Markdown remains the canonical human-readable source of truth. The graph is derived from Markdown, not the other way around.

## Worked Example

See [formula.euler.md](./formula.euler.md) for the first full starter node using:

- structured contract fields;
- structured facts table;
- human-readable prose;
- Obsidian display links;
- stable IDs behind the scenes;
- proof-run checklist.
