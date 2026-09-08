# Mathematical Design Principles

- **Status:** Draft 0.1
- **Purpose:** Philosophy and guardrails for the Living Mathematics Library.
- **Companion:** [Mathematical Process](./mathematical-process.md)

## 1. Dictionary As Interface

The dictionary establishes shared meanings, canonical terms, relationship labels, and stable links.

It should point outward toward deeper material instead of absorbing every surrounding domain.

## 2. One Sentence First

A mathematical object may enter the graph as a one-sentence definition.

The lifecycle is:

```text
mentioned
   ↓
dictionary entry
   ↓
stable concept
   ↓
deep concept page
   ↓
specialized sub-concepts
```

Future deep links extend this rule. The library may reserve a conceptual place with an Obsidian link before the full node exists.

## 3. Portal, Don't Duplicate

If another knowledge source owns a subject better, link to it rather than recreating it poorly.

The library is a map of mathematics, not an attempt to become the entire internet.

## 4. Empty Fields Are Honest

Missing information should be explicit.

Silence must not imply truth, absence, proof, or completeness.

## 5. Structured Tables Plus Prose

Tables carry stable facts.

Prose preserves nuance, intuition, mathematical character, and warnings.

## 6. Human Links, Stable IDs

Use Obsidian links for human navigation and stable IDs behind the scenes.

Human surface:

```markdown
[[Complex Number]]
```

Machine surface:

```yaml
related:
  - concept.complex-number
```

## 7. Nodes Before Ontology

Let the ontology emerge from repeated node patterns.

The growth path is:

```text
nodes -> relationships -> repeated patterns -> ontology
```

## 8. Do Not Scale Before Proof Run

Before applying a new specification across a large corpus, run the five-item proof run and revise the specs from the findings.
