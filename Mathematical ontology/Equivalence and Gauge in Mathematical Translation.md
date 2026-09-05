# Equivalence and Gauge in Mathematical Translation

## Purpose

The mathematical ontology requires concepts that distinguish genuine structure from artifacts of representation. Two foundational additions are equivalence or gauge freedom and commutativity. Together they make the framework more rigorous by clarifying when representations are genuinely compatible.

## Additional Structural Concepts

| Addition | Why It Matters | Example | Role in the Graph |
|---|---|---|---|
| Equivalence class | Different representations may count as the same for a chosen question | all \(re^{i\theta}\) with \(r>0\) share the same phase after normalization | defines intentionally irrelevant information |
| Gauge freedom | Some coordinates may change without changing the meaningful state | scale \(r\) is ignored when only \(\theta\) matters | distinguishes freedom from missing information |
| Group action | Unifies rotation, reflection, translation, and scaling | \(z\mapsto e^{i\theta}z\) | formalizes primitive transformations |
| Commutativity | Different valid translation paths should produce compatible results | Cartesian \(\to\) polar \(\to\) complex versus Cartesian \(\to\) complex | tests whether translations are complete |
| Observability | Determines whether observations contain enough information to reconstruct the source | \(\Re z\) alone cannot recover arbitrary \(z\) | measures reconstruction power |
| Identifiability | Determines whether one unique source explains the observation | different signals can share zero crossings | prevents overinterpreting patterns |
| Aliasing | Different structures can produce the same sampled observation | sparse samples of different frequencies | identifies observational failure modes |
| Equivariance | Transformed source produces correspondingly transformed observation | rotate input \(\to\) shift phase of output | formalizes structural reflection |
| Renormalization | Removes irrelevant scale and compares recurring structure across scales | \(z\mapsto z/|z|\) | separates scale from pattern |
| Duality | Two descriptions are structurally complementary | geometry \(\leftrightarrow\) spectrum | supplies non-obvious translation routes |
| Adjoint / inverse relation | Observations often have a natural backward partner | projection \(\leftrightarrow\) reconstruction | formalizes reverse inference |
| Conservation law | Some quantity survives every allowed transformation | \(|e^{it}|=1\) | identifies invariant content |

## 1. Gauge Freedom

Let

$$
z=re^{i\theta}.
$$

If magnitude is irrelevant, then

$$
re^{i\theta}\sim se^{i\theta}
$$

for any positive \(r,s\). These states are declared equivalent. The meaningful object is not the individual representative \(z\), but the equivalence class

$$
[z]=\{re^{i\theta}:r>0\}.
$$

Normalization chooses a representative:

$$
\frac{z}{|z|}=e^{i\theta}.
$$

Thus normalization factors out a degree of freedom that the problem has declared irrelevant.

The distinction is essential:

$$
\text{missing coordinate}\neq\text{irrelevant coordinate}.
$$

A missing coordinate may represent lost information. An irrelevant coordinate represents information that the problem intentionally quotients away.

## 2. Commutative Diagrams

Consider three representations:

$$
A=\text{Cartesian},\qquad
B=\text{polar},\qquad
C=\text{complex}.
$$

There may be two translation routes:

$$
A\to B\to C
$$

and

$$
A\to C.
$$

A correct canonical translation should give the same result by either route. This is the role of a commutative diagram:

$$
\begin{array}{ccc}
A &\to& B\\
\downarrow && \downarrow\\
C &=& C.
\end{array}
$$

The central rule is:

$$
\text{independent canonical translation paths should commute}.
$$

If \(A\to B\) and \(B\to C\) are known, but \(A\to C\) is missing, the graph predicts what the missing translation must do for the diagram to commute. This is constrained imputation rather than informal pattern matching.

## 3. Quality Control Through Path Comparison

Suppose the graph contains two translation paths:

$$
A\to B\to C\to D
$$

and

$$
A\to E\to D.
$$

If both are canonical, then the corresponding transformations should satisfy

$$
T_{CD}T_{BC}T_{AB}(A)
\stackrel{?}{=}
T_{ED}T_{AE}(A).
$$

Disagreement is informative. It may indicate one of the following:

1. a coordinate was omitted;
2. one route contained a normalization;
3. one route contained a projection;
4. the representations are not actually equivalent;
5. a genuine structural obstruction has been found.

## 4. Observability and Identifiability

Let

$$
z(t)=e^{it}
$$

and observe

$$
x(t)=\cos t.
$$

The observation reveals phase information, so the source is partly observable. However, it may not uniquely determine the entire source.

**Observability** asks how much hidden state the observations can reveal.

**Identifiability** asks whether exactly one hidden model is compatible with the observations.

The implication

$$
\text{orderly observed pattern}\Rightarrow\text{unique underlying structure}
$$

is not generally valid.

## 5. Aliasing

Aliasing occurs when distinct structures produce the same observation. For example, if an oscillation is sampled too sparsely, different frequencies may produce identical sampled values.

Schematically,

$$
S_1\xrightarrow{O}X
$$

and

$$
S_2\xrightarrow{O}X.
$$

Two different sources lead to the same observation. In the ontology, this is observer-induced equivalence.

Aliasing should be treated as a warning relation: an observation may reflect internal structure, but the source must still be shown to be identifiable.

## 6. Equivariance

Equivariance formalizes structural reflection. Let \(T\) transform the source, and let \(P\) be an observer. If there exists a corresponding transformation \(T'\) of the observation such that

$$
P(Tx)=T'(P(x)),
$$

then \(P\) is equivariant with respect to the transformation.

In words:

$$
\text{transform source, then observe}
=
\text{observe, then transform observation}.
$$

For rotation,

$$
z(t)\mapsto e^{i\alpha}z(t)
$$

becomes a phase shift in its sine and cosine projections. The observable inherits the transformation law of the source.

## 7. Structural Harmony

Two representations may be called harmonious when:

1. canonical translation paths commute;
2. relevant invariants are preserved;
3. transformations are equivariant;
4. observations have predictable induced symmetries.

Thus

$$
\text{harmony}=\text{cross-representation coherence}.
$$

The chain

$$
\text{circle}\leftrightarrow e^{it}\leftrightarrow(\cos t,\sin t)
$$

is harmonious because geometry, algebra, phase, and projection agree.

## 8. Topology and Metric

Topology and metric must remain separate.

| Concept | Question |
|---|---|
| Topology | What is connected, neighboring, or continuous? |
| Metric | How far apart are things? |

A transformation may preserve topology while changing distance. Stretching a circle into an ellipse changes metric geometry but preserves many topological properties.

The pre-observational architecture should therefore include

$$
\text{Object}
+\text{Relations}
+\text{Topology}
+\text{Coordinates}
+\text{Metric}
+\text{Operators}.
$$

Only then should the observational chain be added:

$$
\text{Observer}\to\text{Observable}\to\text{Events}\to\text{Invariants}.
$$

## Framework Diagram

$$
\begin{array}{cccccc}
\text{Object} &\to& \text{Relations} &\to& \text{Topology} &\to \text{State}\\
&&&&\downarrow\\
&&& \text{Representation} \leftrightarrow \text{Coordinates}\\
&&&&\downarrow\\
&&& \text{Metric}+\text{Gauge}\\
&&&&\downarrow\\
&&& \text{Operator / Dynamics}\\
&&&&\downarrow\\
&&& \text{Observer}\\
&&&&\downarrow\\
&&& \text{Observable}\to\text{Events}\to\text{Invariants}.
\end{array}
$$

Compatible representations are connected by commutative paths.

## Course Note

Discovery in the ontology follows the pattern

$$
\text{known nodes}
+\text{known bonds}
+\text{commutativity}
+\text{invariant preservation}
\to
\text{constrained missing bond}.
$$

The graph is therefore not only descriptive. It can be used to ask which relation should exist, provided the relevant transformations are canonical and the invariants are preserved.
