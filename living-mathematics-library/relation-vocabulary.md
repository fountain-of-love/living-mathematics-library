# Relation Vocabulary

- **Status:** Starter vocabulary
- **Purpose:** Compact relation category and bond vocabulary for Living Mathematics Library nodes.
- **Full working draft:** [mathematical-ontology/docs/relation-vocabulary.md](../mathematical-ontology/docs/relation-vocabulary.md)

## Relation Shape

Use `category` for the broad relation family and `type` for the specific bond.

```yaml
relations:
  - category: representation
    type: represents
    target: concept.rotation
```

## Categories

| Category | Use for |
|---|---|
| `transformation` | Operations, maps, conversions, processes. |
| `structural-property` | Invariants, symmetries, fixed points, periodicity, conservation. |
| `equivalence` | Rewrites, identities, isomorphisms, equivalences. |
| `dependency` | Prerequisites, definitions, derivations, requirements. |
| `evidence` | Proof, support, contradiction, sources, tests. |
| `representation` | Models, expressions, pictures, coordinates, teaching examples. |
| `analogy` | Heuristic comparisons with limits. |

## Classification Hints

- rotation, projection, embedding, derivative, and integral are primarily transformations.
- symmetry, conservation, invariance, fixed point, and periodicity are structural properties or observations.
- resonance, interference, and correction/residue need an explicit category choice because their role depends on context.
