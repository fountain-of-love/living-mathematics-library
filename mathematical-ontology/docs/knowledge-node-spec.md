# Knowledge Node Spec

- **Status:** Draft 0.1
- **Purpose:** Minimal stable contract for mathematical knowledge nodes.
- **Architecture source:** [Mathematics Repository Architecture](./mathematics-repository-architecture.md)

## 1. Role

A knowledge node is a durable Markdown artifact with a small structured contract.

Markdown remains the canonical human-readable source of truth. Structured fields make the page parseable for graph construction, validation, and AI retrieval.

## 2. Minimum Contract

For v0.1, every published node should provide:

```yaml
id: concept.example
type: concept
name: Example
status: established
maturity: seed
summary: >
  One-sentence definition or orientation.
```

Strongly recommended fields:

```yaml
domains: []
prerequisites: []
relations: []
sources:
  - id: source.example
    role: reference
validation:
  status: unverified
  methods: []
```

Type-specific contracts add only what that node kind needs.

## 3. Provenance And Validation

A source is itself a node.

Source references should be structured when possible:

```yaml
sources:
  - id: source.dlmf.4.2
    role: reference
```

Suggested source roles:

- `primary`;
- `definition`;
- `proof`;
- `reference`;
- `historical`;
- `notation`;
- `data`;
- `validation`;
- `secondary`.

Validation is separate from provenance:

```yaml
validation:
  status: verified
  checked: 2026-09-07
  methods:
    - source-confirmed
    - symbolic-check
```

Validation status vocabulary:

- `unverified`;
- `partially-verified`;
- `verified`;
- `machine-checked`;
- `human-reviewed`;
- `source-confirmed`.

## 4. Schema Terms Vs Mathematical Entities

Schema terms describe the record. They are the grammar of the knowledge system.

Mathematical entities describe the mathematics. They are the subject matter being represented.

| Schema term | Meaning |
|---|---|
| `id` | Stable machine identifier for a node. |
| `type` | Contract family used by the node. |
| `status` | Epistemic state of the mathematical claim or artifact. |
| `maturity` | Development state of the local page. |
| `source` | Provenance record or cited authority. |
| `prerequisite` | Directional dependency for understanding. |
| `relationship` | Typed edge between nodes. |
| `proof` | Evidence structure for a claim. |
| `example` | Illustrative instance or boundary test. |

| Mathematical entity | Example |
|---|---|
| Number-like object | complex number, real number |
| Algebraic object | group, ring, field |
| Analytic object | derivative, integral, Fourier transform |
| Formula | Euler's formula |
| Claim | Fundamental theorem of arithmetic, Riemann hypothesis |
| Experiment | zeta zero spacing experiment |

Do not confuse the two layers. `status` is not a mathematical object. `Fourier transform` is not a schema field. This distinction is critical for machine reasoning.

### 4.1 Namespace Rule

Schema terms belong to contract vocabularies:

```yaml
status: established
proof:
  status: not-yet-developed
sources:
  - source.dlmf
```

Mathematical entities belong to mathematical node namespaces:

```yaml
prerequisites:
  - concept.real-number
objects:
  - concept.complex-number
  - concept.exponential-function
related:
  - formula.euler
```

Do not create mathematical concept nodes for schema grammar merely because a page mentions the word. For example, `status`, `source`, `prerequisite`, `relationship`, `proof`, and `example` are not dictionary concepts unless the page is explicitly documenting the schema itself.

### 4.2 Link Rendering Rule

Use Markdown or Obsidian links for mathematical entities:

```markdown
[[Complex Number]]
[[Integral]]
[[Fourier Transform]]
```

Use inline code for schema terms:

```markdown
`status`
`source`
`prerequisite`
`proof`
```

This prevents graph builders from mistaking the schema's own vocabulary for mathematical content.

## 5. Human Links And Stable IDs

Use Obsidian links for human navigation:

```markdown
[[Complex Number]]
[[Exponential Function]]
[[Euler's Formula]]
```

Use stable IDs in structured fields:

```yaml
related:
  - concept.complex-number
  - concept.exponential-function
  - formula.euler
```

The display name may change. The stable ID should not.

## 6. Graph Direction

The graph is derived from Markdown nodes:

```text
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

Do not make a database the initial source of truth.

## 7. Validation Rules

- Every node has a stable ID.
- Every node separates schema terms from mathematical entities.
- Every node states epistemic status separately from page maturity.
- Schema terms are rendered as code or contract fields, not as mathematical concept links.
- Required fields are present or explicitly marked with an absence value.
- Source notation is preserved before canonical formula normalization.
- Relations use stable IDs behind human-friendly links.
- Sources are structured as source-node references where possible.
- Validation is recorded separately from provenance.
- Markdown prose remains readable without inspecting generated graph data.
