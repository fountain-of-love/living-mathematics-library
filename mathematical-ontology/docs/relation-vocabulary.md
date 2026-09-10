# Relation Vocabulary

- **Status:** Draft 0.1
- **Purpose:** Controlled vocabulary for mathematical relation categories and bond predicates.
- **Companion:** [Knowledge Node Spec](./knowledge-node-spec.md)

## 1. Principle

A relation has two layers:

1. `category`: the broad kind of connection.
2. `type`: the specific bond or predicate inside that category.

This prevents unlike mathematical links from being collapsed into one flat `related` bucket.

```yaml
relations:
  - category: representation
    type: represents
    target: concept.rotation
```

## 2. Relation Categories

| Category | Meaning | Typical bond types |
|---|---|---|
| `transformation` | An operation, map, process, or conversion that changes or transports mathematical structure. | `rotates`, `projects`, `embeds`, `differentiates`, `integrates`, `transforms` |
| `structural-property` | A property, invariant, observed regularity, or constraint of an object or system. | `has-symmetry`, `has-invariant`, `has-fixed-point`, `has-periodicity`, `conserves` |
| `equivalence` | A sameness, rewrite, isomorphism, identity, or interchangeable form under stated conditions. | `equivalent-to`, `rewrites-to`, `isomorphic-to`, `same-as`, `normalizes-to` |
| `dependency` | A prerequisite, assumption, derivation input, or construction dependency. | `depends-on`, `requires`, `derives-from`, `defined-by`, `uses` |
| `evidence` | Support, contradiction, proof, counterexample, source, or empirical observation. | `proves`, `supports`, `contradicts`, `refutes`, `cites`, `source` |
| `representation` | A way one object, formula, model, coordinate system, or picture expresses another. | `expresses`, `represents`, `models`, `parameterized-by`, `geometric-model` |
| `analogy` | A heuristic comparison between domains with stated limits. | `analogous-to`, `resembles`, `suggests`, `maps-onto` |

## 3. Mathematical Entity Roles

Some mathematical entities often appear as bond labels, but they should still keep their own mathematical identity.

| Entity or phenomenon | Primary relation category | Notes |
|---|---|---|
| rotation | `transformation` | Often represented by Euler's formula or a matrix. |
| projection | `transformation` | Usually loses information unless qualified otherwise. |
| embedding | `transformation` | Often structure-preserving; state preserved structure explicitly. |
| derivative | `transformation` | Operation taking a function to a rate-of-change object. |
| integral | `transformation` | Operation accumulating or transforming quantities. |
| symmetry | `structural-property` | May be witnessed by transformations but is itself a property. |
| conservation | `structural-property` | Often appears as an invariant under evolution. |
| invariance | `structural-property` | Must name the transformation or group action under which it is invariant. |
| fixed point | `structural-property` | A point unchanged by a specified transformation. |
| periodicity | `structural-property` | Repetition under translation, rotation, or another operation. |
| resonance | `structural-property` or `evidence` | Category depends on whether it is a property of a system or an observed signal. |
| interference | `structural-property` or `evidence` | Often an observed interaction pattern; specify scope. |
| correction / residue | `transformation` or `evidence` | Use `transformation` for corrective operations; use `evidence` when a residue measures a remaining discrepancy. |

## 4. Bond Discipline

The bond family is a controlled vocabulary inside the relation category.

Prefer:

```yaml
category: transformation
type: projects
target: concept.subspace
```

over:

```yaml
type: projection
target: concept.subspace
```

when the edge is an action performed between nodes.

Prefer:

```yaml
category: structural-property
type: has-periodicity
target: concept.periodicity
```

when the edge records a property or observation.

## 5. Review Checklist

- Every relation has a `category`, `type`, and `target`.
- The `category` is one of the seven controlled categories.
- The `type` belongs naturally inside the chosen category.
- Mathematical entities are not reduced to schema terms.
- Transformations and structural properties are not confused.
- Evidence is not treated as proof unless the relation type is explicitly `proves`.
- Analogies state their limits elsewhere in the node.
