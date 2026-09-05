# The Periodic Graph of Mathematical Structure

## Core Model

Before adding more constants or bonds, the ontology must distinguish different kinds of mathematical objects. An operator such as \(i\), an invariant such as \(\pi\), an observation such as \(\cos t\), and an event such as a zero should not be treated as the same kind of node.

The appropriate structure is a typed directed multigraph with observation layers:

$$
\text{Structure}
\to
\text{Operation}
\to
\text{Dynamics}
\to
\text{Representation}
\to
\text{Observation}
\to
\text{Event}
\to
\text{Invariant}.
$$

Translation and feedback bonds connect the layers.

## 1. Seven Node Classes

| Layer | Node Type | Question Answered | Examples |
|---|---|---|---|
| \(S\) | Structure | What exists? | circle, line, recurrence, lattice, multiplicative space |
| \(O\) | Operation | What can be done to it? | rotate, scale, divide, reflect, recurse |
| \(D\) | Dynamics | What trajectory does repeated operation generate? | \(e^{it}\), exponential growth, Fibonacci sequence |
| \(R\) | Representation | In what coordinates or language is it expressed? | Cartesian, polar, logarithmic, complex, Fourier |
| \(V\) | Observation | Through what lens is it inspected? | \(\Re\), \(\Im\), magnitude, derivative, projection |
| \(E\) | Event | What distinguished occurrence is detected? | zero, crossing, closure, maximum, fixed point |
| \(I\) | Invariant | What stable relationship survives? | \(\pi,e,\varphi,\sqrt2,\gamma\) |

The generic grammar is

$$
S\xrightarrow{O}D
\xrightarrow{\text{encode}}R
\xrightarrow{V}E
\xrightarrow{\text{stabilize}}I.
$$

This grammar is not purely linear; it contains feedback.

## 2. Cyclic Structure

An invariant can constrain or reconstruct the structure that generated it:

$$
S\to O\to D\to R\to V\to E\to I\to S.
$$

For example,

$$
\frac{C}{D}=\pi
$$

does not merely record a property of circles. Once known, \(\pi\) becomes part of how circular geometry is defined and reconstructed.

Similarly,

$$
\varphi^2=\varphi+1
$$

does not only emerge from Fibonacci recursion. It can also generate golden recursive structures.

The ontology therefore contains two directions:

$$
\text{generation}\to
\qquad\text{and}\qquad
\leftarrow\text{reconstruction}.
$$

This makes the structure a periodic graph rather than a periodic list.

## 3. Three Topological Zones

### A. Generative Domain

$$
S\to O\to D.
$$

Structure produces behavior.

Examples:

$$
\text{circle}\xrightarrow{\text{rotate}}e^{it},
$$

$$
(F_n,F_{n+1})
\xrightarrow{\text{recurse}}
(F_{n+1},F_n+F_{n+1}).
$$

This is the source system.

### B. Translational and Observational Domain

$$
D\to R\to V.
$$

The underlying system need not change. Instead, its expression or inspection changes.

Example:

$$
e^{it}=\cos t+i\sin t,
$$

followed by

$$
\Re(e^{it})=\cos t.
$$

The first line is representation. The second line is observation.

### C. Emergent Domain

$$
V\to E\to I.
$$

Observations generate distinguished events. Repeated or structurally stable events reveal invariants.

Example:

$$
\cos t=0
$$

at

$$
t=\frac{\pi}{2}+k\pi.
$$

The zero is the event. The spacing \(\pi\) is the invariant.

The pattern is

$$
\text{observable events}\to\text{stable relation}\to\text{constant}.
$$

## 4. Primary Bond Types

### Type G: Generative Bonds

Generative bonds create a new state or trajectory:

$$
S/O\to D.
$$

Examples include iteration, recursion, compounding, rotation, translation, reflection, bifurcation, and flow.

Characteristic question: what happens when this relation is applied?

### Type T: Translational Bonds

Translational bonds preserve the underlying mathematical object while changing its representation:

$$
D/R\leftrightarrow R.
$$

Examples include Cartesian-polar translation, linear-logarithmic translation, discrete-continuous translation, time-frequency translation, exponential-logarithmic translation, and complex-trigonometric translation.

Canonical example:

$$
e^{it}\leftrightarrow \cos t+i\sin t.
$$

These bonds express the principle:

$$
\text{same structure, different language}.
$$

### Type P: Projection Bonds

Projection bonds intentionally discard dimensions or information:

$$
R\to V.
$$

Examples:

$$
z\mapsto\Re z,\qquad
z\mapsto |z|,\qquad
(x,y,z)\mapsto(x,y),\qquad
f(t)\mapsto f(t_0).
$$

Projection can create apparent phenomena that do not exist in the complete state. For instance,

$$
|e^{it}|=1
$$

but

$$
\Re(e^{it})=\cos t
$$

has zeros.

Thus an observed zero may be produced by projection rather than by a zero of the full system.

### Type \(D_e\): Event-Detection Bonds

Event-detection bonds connect an observable to distinguished states:

$$
V\to E.
$$

Examples include zero, crossing, intersection, maximum, minimum, closure, resonance, synchronization, fixed point, and bifurcation threshold.

Example:

$$
\cos t\xrightarrow{\text{zero}}t=\frac{\pi}{2}+k\pi.
$$

A zero is not an operation such as rotation. It is an event condition.

### Type I: Invariance Bonds

Invariance bonds connect repeated events or transformations to stable quantities:

$$
E/D\to I.
$$

Examples include fixed ratio, period, conserved magnitude, limiting value, asymptotic residue, eigenvalue, scaling constant, and universality constant.

Examples:

$$
\frac{F_{n+1}}{F_n}\to\varphi,
$$

$$
\left(1+\frac1n\right)^n\to e,
$$

$$
H_n-\ln n\to\gamma,
$$

$$
e^{i(t+2\pi)}=e^{it}.
$$

These are the bonds through which the periodic-table elements emerge.

### Type R: Reconstruction Bonds

Reconstruction bonds close the topology:

$$
I/E\to S/D.
$$

Once an invariant is known, it may reconstruct part of the generating structure.

Examples:

$$
\pi+r\to C=2\pi r,
$$

$$
\varphi\to x_{n+1}\approx\varphi x_n,
$$

$$
\text{spectrum}\to\text{possible source dynamics}.
$$

These are inverse or reconstruction bonds.

## 5. Macro-Topology

The complete macro-topology is

$$
S
\xrightarrow{G}
D
\xrightarrow{T}
R
\xrightarrow{P}
V
\xrightarrow{D_e}
E
\xrightarrow{I}
I
\xrightarrow{R^{-1}}
S.
$$

Read verbally:

$$
\text{structure}
\to
\text{generated dynamics}
\to
\text{translated representation}
\to
\text{projected observable}
\to
\text{detected event}
\to
\text{stabilized invariant}
\to
\text{reconstructed structure}.
$$

## 6. Bond Metadata

Every bond should carry metadata in addition to its family.

| Property | Possibilities | Example |
|---|---|---|
| Direction | directed / symmetric | \(\exp\leftrightarrow\log\) |
| Reversibility | reversible / lossy / conditionally reversible | complex \(\to\) real is lossy |
| Dimension | preserve / reduce / increase | projection reduces |
| Information | preserve / compress / expand | Fourier transform preserves; magnitude loses phase |
| Dynamics | static / iterative / continuous | recursion is iterative |
| Locality | local / global | derivative is local; integral is global |
| Linearity | linear / nonlinear | projection is linear; \(x^2\) is nonlinear |
| Scale | additive / multiplicative / logarithmic | log translates multiplication |
| Temporal role | instantaneous / cumulative / asymptotic | limit is asymptotic |
| Closure | open / periodic / fixed-point / convergent | rotation is periodic |

Two bonds may share a name while behaving very differently. A projection from \((x,y,z)\) to \((x,y)\) loses a dimension, whereas a coordinate transformation may be fully reversible.

## 7. Typed Roles of Constants

Constants should not all be classified only as invariant nodes. The same constant can participate in several roles.

For \(i\):

$$
i^2=-1
$$

shows an algebraic element role, while

$$
z\mapsto iz
$$

shows an operator role.

For \(\pi\), roles include:

1. circle invariant: \(C/D=\pi\);
2. phase scale: \(2\pi\);
3. zero-spacing constant for sine and cosine;
4. normalization factor in Fourier analysis;
5. geometric coefficient in higher-dimensional formulas.

For \(e\), roles include:

1. limit invariant;
2. exponential base;
3. eigenfunction scaling constant;
4. continuous compounding constant.

The graph is therefore closer to a typed directed multi-hypergraph than to a conventional network. A relation such as

$$
e^{i\pi}+1=0
$$

connects \(e,i,\pi,1,0\) through a structural motif. This is a hyperedge.

## 8. Three Graph Levels

### Level 1: Elements

Recognizable mathematical constants and primitive objects:

$$
e,\pi,i,\varphi,\sqrt2,\gamma,\delta,\ldots
$$

### Level 2: Bonds

Primitive transformations:

$$
\text{rotate, recurse, scale, project, log, differentiate},\ldots
$$

### Level 3: Motifs

Reusable combinations of bonds.

Rotation motif:

$$
\text{rotation}
\to
\text{complex exponential}
\to
\text{projection}
\to
\text{oscillation}
\to
\text{zero / period}
\to
\pi.
$$

Recursive-growth motif:

$$
\text{recursion}
\to
\text{ratio}
\to
\text{iteration}
\to
\text{fixed point}
\to
\varphi.
$$

Continuous-growth motif:

$$
\text{relative change}
\to
\text{compounding}
\to
\text{refinement}
\to
\text{continuous limit}
\to
e.
$$

Motifs are reusable mathematical structures built from elements and bonds.

## 9. Frozen Taxonomy

| Category | Contents |
|---|---|
| Nodes | \(S,O,D,R,V,E,I\) |
| Primary bond families | \(G\): generative; \(T\): translation; \(P\): projection; \(D_e\): event detection; \(I\): invariance/emergence; \(R\): reconstruction |
| Bond properties | direction, reversibility, information, dimension, linearity, locality, scale, time, closure |
| Higher structures | motifs, cycles, hyperedges |

The canonical grammar is

$$
\text{Structure}
\xrightarrow{\text{generate}}
\text{Dynamics}
\xrightarrow{\text{translate}}
\text{Representation}
\xrightarrow{\text{project}}
\text{Observable}
\xrightarrow{\text{detect}}
\text{Event}
\xrightarrow{\text{stabilize}}
\text{Invariant}
\xrightarrow{\text{reconstruct}}
\text{Structure}.
$$

The final reconstruction arrow turns the classification from a static taxonomy into a topology.

## Course Note

The thirty primitive bond names should be classified into the six primary bond families rather than treated as peers. This gives the ontology both clarity and extensibility: new relations can be added by assigning node types, bond family, metadata, and motif membership.
