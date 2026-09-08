# Mathematical Ontology

## Introduction

This folder sketches a mathematical ontology: a way of asking what kind of thing a mathematical object is before asking how to calculate with it. A number, a constant, a rotation, a projection, a zero, a graph, and an invariant may appear in the same formula, but they do not play the same role. The aim of this material is to give each role a clear place.

The guiding intuition is simple enough for a first lesson and deep enough for advanced study: mathematics often becomes understandable when structures, operations, observations, and invariants are kept distinct. A circle can become a wave when it is projected onto an axis. Repeated proportional change becomes exponential behavior in the continuous limit. A natural constant can be read as the fingerprint left behind by a stable relationship.

The material therefore treats mathematics less as a list of formulas and more as a translation system. It asks how one representation becomes another, what is preserved, what is lost, which reference frame is being used, and whether an observed pattern really identifies its source. This makes the notes useful both for learning mathematical fundamentals and for designing machine-readable representations of mathematical meaning.

## Use in Studying the Riemann Hypothesis

This material has been used as an exploratory framework for tackling the Riemann hypothesis. It does not present a proof of the hypothesis; rather, it provides a disciplined way to ask what the relevant mathematical objects are, how they are represented, and which transformations preserve or hide their structure.

In that work, the ontology has helped organize the historical evolution of prime counting: from direct counting of primes, through analytic approximations, to the spectral and zeta-function viewpoint where prime distribution is studied through complex-analytic structure.

It has also supported experiments with alternative representations of prime numbers and prime counting. A prime can be approached as an indivisible integer, a survivor of a sieve, a bit in an exclusion field, a term in an Euler product, a signal in a counting error, or a structure reflected through the zeros of the zeta function. Each representation reveals something and conceals something.

Most importantly, the ontology gives language for separating the mathematical structures, mathematical objects, and roles involved in the Riemann hypothesis. Prime numbers, counting functions, logarithmic scales, zeta zeros, complex phase, analytic continuation, error terms, and spectral patterns are not interchangeable. They form a network of translations, projections, invariants, and reconstruction problems. Studying those roles helps prevent false equivalence while making genuine structural correspondences easier to see.

## Relation to MML and the Semantic Seed Vault

This ontology fits naturally beside [Machine Modelled Language](https://github.com/fountain-of-love/mml-machine-modelled-language), a project that explores executable semantic infrastructure from public knowledge. MML's direction is to represent governed concepts, senses, semantic roles, aliases, and typed relations explicitly, then compile that accepted structure into deterministic weighting operators and reusable semantic state.

The connection is direct: this mathematical ontology supplies a disciplined vocabulary for the mathematical side of that work. Its nodes, bonds, invariants, projections, equivalence classes, metrics, dimensions, and reference frames are the kinds of semantic roles that can prevent a machine system from treating unlike things as if they were merely "related." In that sense, the ontology acts as a mathematical grammar for preserving type, scope, and meaning during translation.

The MML repository also contains a [Semantic Seed Vault](https://github.com/fountain-of-love/mml-machine-modelled-language#scientific-foundation-the-semantic-seed-vault). The vault is described as a durable, human-readable knowledge base for concepts, claims, evidence, contradictions, provenance, and patterns. Its scientific material uses shared roles such as capacity, substrate, activation, gain, storage, boundary, evidence, maturity, and failure to compare domains without pretending those domains are identical.

The mathematical ontology developed here has the same spirit. It preserves mathematical seeds: constants, structures, operations, observations, bonds, failures of translation, and conditions of validity. Where the Seed Vault preserves governed scientific and semantic knowledge, these notes preserve the mathematical translation rules that can help such knowledge become precise, inspectable, and eventually executable.

Together, the two projects support one larger idea:

$$
\text{preserve meaning}
\to
\text{type its relations}
\to
\text{compile stable structure}
\to
\text{navigate knowledge responsibly}.
$$

The Seed Vault keeps knowledge readable and reviewable. MML aims to make governed knowledge executable. This ontology contributes the mathematical discipline needed to say what is being transformed, what remains invariant, and what must not be silently collapsed.

## Table of Contents

The common authoring and graph contract is defined in the [Knowledge Node Spec](./docs/knowledge-node-spec.md), with a deeper legacy/general form in the [Universal Mathematical Knowledge-Node Schema](./docs/universal-mathematical-knowledge-node-schema.md). These documents provide shared identity, provenance, epistemic, relation, and governance fields while keeping schema terms separate from mathematical entities.

The compact terminology interface is defined in the [Mathematical Dictionary](./docs/mathematical-dictionary.md). It establishes shared meanings, canonical terms, relationship labels, stable links, and outward paths toward deeper material without turning each entry into a full textbook treatment.

The working page contracts are split into focused documents: [Concept](./docs/mathematical-concept-spec.md), [Formula](./docs/mathematical-formula-spec.md), [Theorem](./docs/mathematical-theorem-spec.md), [Conjecture](./docs/mathematical-conjecture-spec.md), [Proof](./docs/mathematical-proof-spec.md), [Experiment](./docs/mathematical-experiment-spec.md), [Process](./docs/mathematical-process.md), [Proof Run](./docs/mathematical-proof-run.md), [Proof Run 5](./docs/proof-run-5.md), and [Worklist](./docs/mathematical-worklist.md). These documents keep the ontology usable in practice while the universal schema remains the deeper data model.

| Order | Module | One-Sentence Definition |
|---:|---|---|
| 1 | [Mathematical Fundamentals](./Mathematical%20fundamentals.md) | Broad concept map, vocabulary, topology, and glossary for the workspace. |
| 2 | [The Cake Model of Continuous Decay](./The%20Cake%20Model%20of%20Continuous%20Decay.md) | Introduces recursive proportional removal as a concrete model for continuous decay and the emergence of \(e^{-1}\). |
| 3 | [Asymptotic Normalization and Continuous Change](./Asymptotic%20Normalization%20and%20Continuous%20Change.md) | Explains how many small relative changes converge to exponential behavior governed by \(e\). |
| 4 | [How Rotation Becomes a Wave](./How%20Rotation%20Becomes%20a%20Wave.md) | Shows how circular motion becomes sine and cosine when observed through coordinate projections. |
| 5 | [Natural Constants as Fingerprints of Structure](./Natural%20Constants%20as%20Fingerprints%20of%20Structure.md) | Presents natural constants as stable values forced by operations, constraints, and self-consistency. |
| 6 | [A Periodic Table of Mathematical Constants](./A%20Periodic%20Table%20of%20Mathematical%20Constants.md) | Organizes constants by the primitive relationships that generate them, such as rotation, recursion, scale, and residue. |
| 7 | [Mathematical Bonds and Translation Rules](./Mathematical%20Bonds%20and%20Translation%20Rules.md) | Classifies the transformations that connect mathematical structures, representations, observations, and invariants. |
| 8 | [The Periodic Graph of Mathematical Structure](./The%20Periodic%20Graph%20of%20Mathematical%20Structure.md) | Defines the ontology as a typed graph linking structures, operations, dynamics, representations, observations, events, and invariants. |
| 9 | [A Translation Atlas for Mathematical Objects](./A%20Translation%20Atlas%20for%20Mathematical%20Objects.md) | Extends the ontology with objects, operators, metrics, compatibility rules, and information-preserving translations. |
| 10 | [When Observations Hide Structure](./When%20Observations%20Hide%20Structure.md) | Distinguishes complete translation from normalization, quotienting, projection, and induced observational structure. |
| 11 | [Equivalence and Gauge in Mathematical Translation](./Equivalence%20and%20Gauge%20in%20Mathematical%20Translation.md) | Formalizes equivalence classes, gauge freedom, commutativity, observability, identifiability, and aliasing. |
| 12 | [The Mathematical Compass of Orientation and Dimension](./The%20Mathematical%20Compass%20of%20Orientation%20and%20Dimension.md) | Adds orientation, chirality, reference frames, dimension, networks, and computational separation to the ontology. |

## Course Path

The sequence begins with the broad fundamentals map, continues through concrete examples of decay and rotation, then develops constants, bonds, graph structure, translation rules, observation theory, and finally orientation and dimensional bookkeeping.
