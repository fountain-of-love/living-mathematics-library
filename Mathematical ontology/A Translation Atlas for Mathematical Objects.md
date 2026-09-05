# A Translation Atlas for Mathematical Objects

## Purpose

Vectors, sets, and bit operators must be represented explicitly in the ontology. They allow the framework to distinguish mathematical objects, representations, operators, metrics, and observations:

$$
\text{mathematical object}
\to
\text{representation}
\to
\text{operator}
\to
\text{metric}
\to
\text{observation}.
$$

Translations can occur between compatible layers. When several representations of the same structure are known, a missing representation can sometimes be derived rather than guessed.

## 1. Expanded Classes of Mathematical Objects

| Class | Mathematical Units / Objects | Typical Structure | Example |
|---|---|---|---|
| Scalar | numbers, constants | magnitude | \(3,\pi,e,\varphi\) |
| Bit | \(0,1\) | binary state | prime / excluded |
| Bit vector | \(\{0,1\}^n\) | multiple binary states | sieve row |
| Vector | \(\mathbb R^n,\mathbb C^n\) | magnitude and direction | \((x,y)\) |
| Point | coordinate tuple | location | \((r,\theta)\) |
| Set | \(A\subseteq X\) | membership | primes, survivors |
| Sequence | \((a_n)\) | ordered discrete states | Fibonacci |
| Function | \(f:X\to Y\) | mapping | \(\cos t\) |
| Relation | \(R\subseteq A\times B\) | connectivity or constraint | divisibility |
| Graph | \(G=(V,E)\) | relational topology | number graph |
| Matrix | \(A_{ij}\) | structured relations | exclusion matrix |
| Field | value at every point | distributed state | \(f(x,t)\) |
| Measure | \(\mu(A)\) | quantity over sets | probability |
| Distribution | \(P(X)\) | weighted possibilities | Gaussian |
| Manifold / space | geometric domain | continuous geometry | circle, sphere |
| Spectrum | \(\{\lambda_k\}\) | modal or frequency structure | Fourier spectrum |

This forms a periodic table of mathematical units.

## 2. Operator Families

| Operator Family | Primitive Operators | Acts On | Structural Meaning |
|---|---|---|---|
| Arithmetic | \(+,-,\times,\div\) | scalars | combine magnitude |
| Boolean | AND, OR, NOT, XOR | bits | logical composition |
| Set | \(\cap,\cup,\setminus,{}^c\) | sets | membership composition |
| Vector | \(+,\cdot,\times\) | vectors | combine direction and magnitude |
| Matrix | multiplication, transpose, inverse | vectors and matrices | transform coordinates |
| Geometric | rotate, reflect, scale, translate | points and vectors | change geometry |
| Recursive | iterate, recurse | sequences and states | feed output into input |
| Differential | \(d/dx,\nabla,\Delta\) | functions and fields | local change |
| Integral | \(\int,\sum\) | functions and sequences | accumulation |
| Projection | \(P(x)\) | vectors and spaces | reduce dimensions |
| Normalization | \(x/\|x\|\) | vectors and states | remove scale |
| Transform | Fourier, Laplace, Mellin | functions and measures | change observation domain |
| Threshold | \(x>c\), sign, indicator | scalars and functions | convert continuous to discrete |
| Factorization | prime decomposition, eigendecomposition | integers and matrices | reveal components |
| Composition | \(f\circ g\) | mappings | chain transformations |

Boolean algebra and set algebra are structurally equivalent:

$$
A\cap B\leftrightarrow A\land B,
$$

$$
A\cup B\leftrightarrow A\lor B,
$$

$$
A^c\leftrightarrow \neg A.
$$

A prime bitfield can therefore be viewed both as a Boolean system and as a set-theoretic system.

## 3. Representation Systems

| Representation | Typical Object | Coordinates | Particularly Exposes |
|---|---|---|---|
| Binary | state or membership | \(0,1\) | inclusion / exclusion |
| Integer | count | \(n\) | discreteness |
| Cartesian | geometric point | \((x,y)\) | independent axes |
| Polar | geometric point | \((r,\theta)\) | magnitude and phase |
| Complex | rotation or state | \(z=x+iy\) | phase and magnitude together |
| Exponential | growth or rotation | \(re^{i\theta}\) | multiplicative evolution |
| Logarithmic | scale | \(u=\log x\) | multiplication as translation |
| Vector | multidimensional state | \((x_1,\ldots,x_n)\) | direction and components |
| Matrix | relational system | \(A_{ij}\) | interactions |
| Set | membership | \(\{x:\ldots\}\) | logical structure |
| Graph | relations | vertices and edges | topology |
| Sequence | discrete evolution | \(a_n\) | iteration |
| Continuous function | trajectory | \(f(t)\) | smooth dynamics |
| Spectral | modes | \((A_k,\omega_k,\phi_k)\) | frequencies |
| Probability | uncertain state | \(P(x)\) | likelihood |

For a planar geometric state,

$$
(x,y)\leftrightarrow(r,\theta)\leftrightarrow re^{i\theta}
$$

are compatible representations of the same object.

## 4. Canonical Translation Table

| Source | Target | Translation | Preserves | Reveals | Potential Loss |
|---|---|---|---|---|---|
| Cartesian | Polar | \(r=\sqrt{x^2+y^2}\), \(\theta=\operatorname{atan2}(y,x)\) | geometry | magnitude and phase | origin ambiguity |
| Polar | Cartesian | \(x=r\cos\theta\), \(y=r\sin\theta\) | geometry | axis components | none |
| Polar | Complex | \(z=re^{i\theta}\) | geometry | algebraic rotation | none |
| Complex | Cartesian | \(z=x+iy\) | full state | real and imaginary components | none |
| Complex | Real projection | \(z\mapsto\Re z\) | one component | oscillation | imaginary component lost |
| Rotation | Oscillation | \(e^{it}\mapsto\cos t\) | phase timing | wave behavior | radial and imaginary information |
| Set | Bit vector | \(1_A(x)\) | membership | computational representation | none if universe is fixed |
| Bit vector | Set | \(\{x:b_x=1\}\) | membership | semantic object | universe required |
| Boolean AND | Set intersection | \(a\land b\leftrightarrow A\cap B\) | logical relation | set interpretation | none |
| Boolean OR | Set union | \(a\lor b\leftrightarrow A\cup B\) | logical relation | membership aggregation | none |
| Boolean NOT | Complement | \(\neg a\leftrightarrow A^c\) | negation | exclusion | universe required |
| XOR | Symmetric difference | \(A\triangle B\) | parity difference | changed membership | common membership discarded |
| Scalar sequence | Vector | \((a_1,\ldots,a_n)\) | values | geometric state | ordering convention required |
| Vector | Magnitude | \(\|v\|\) | size | amplitude | direction lost |
| Vector | Unit vector | \(v/\|v\|\) | direction | orientation | magnitude lost |
| Matrix | Graph | \(A_{ij}\neq0\Rightarrow i\to j\) | connectivity | topology | weights may be lost |
| Graph | Matrix | adjacency matrix | relations | algebraic processing | depends on node ordering |
| Sequence | Function | interpolation or continuum limit | trend | continuous dynamics | discrete details may vanish |
| Function | Sequence | \(f(n)\) | samples | computable discrete structure | between-sample behavior |
| Multiplicative scale | Log scale | \(u=\ln x\) | order | multiplication as addition | zero and negative domain issues |
| Time domain | Frequency domain | Fourier transform | information under conditions | modes | localization changes |
| Multiplicative domain | Mellin domain | Mellin transform | scale structure | scale frequencies | direct locality changes |
| Function | Derivative | \(f\mapsto f'\) | local relation | rate | constant offset |
| Function | Integral | \(f\mapsto\int f\) | accumulated relation | global quantity | integration constant |
| Data | Probability distribution | normalization / statistics | aggregate structure | uncertainty | individual detail |

This table functions as a translation atlas.

## 5. Metrics as a Separate Axis

The same object can be represented differently and measured differently. Thus:

$$
\text{object}\neq\text{representation}\neq\text{metric}.
$$

| Metric | Applied To | Measures | Example |
|---|---|---|---|
| Euclidean | vectors | straight distance | \(\sqrt{x^2+y^2}\) |
| Manhattan | vectors and grids | axis distance | \(\sum_i |x_i-y_i|\) |
| Angular | vectors | directional separation | \(\theta\) |
| Hamming | bit vectors | number of differing bits | \(d_H(101,111)=1\) |
| Jaccard | sets | membership overlap | \(|A\cap B|/|A\cup B|\) |
| Cosine | vectors | directional similarity | \(u\cdot v/(\|u\|\|v\|)\) |
| Edit distance | strings and sequences | transformation cost | insert / delete / substitute |
| Graph distance | graphs | shortest relational path | hops |
| \(L^p\) norm | functions and vectors | magnitude | \(\|f\|_p\) |
| Entropy | distributions | uncertainty | \(H(X)\) |
| KL divergence | distributions | informational discrepancy | \(D_{KL}(P\|Q)\) |
| Spectral distance | spectra | modal difference | eigenvalue comparison |

## 6. Layered Translation Types

| Bond Type | From \(\to\) To | Example |
|---|---|---|
| Object translation | object \(\to\) equivalent object | set \(\leftrightarrow\) bit vector |
| Coordinate translation | coordinates \(\to\) coordinates | Cartesian \(\leftrightarrow\) polar |
| Representation translation | representation \(\to\) representation | complex \(\leftrightarrow\) trigonometric |
| Domain translation | domain \(\to\) domain | time \(\leftrightarrow\) frequency |
| Scale translation | scale \(\to\) scale | linear \(\leftrightarrow\) logarithmic |
| Logical translation | logic \(\to\) set structure | AND \(\leftrightarrow\) intersection |
| Dimensional translation | \(nD\to mD\) | vector \(\to\) projection |
| Metric translation | metric \(\to\) metric | Hamming \(\leftrightarrow\) normalized Hamming |
| Discrete-continuous translation | sequence \(\leftrightarrow\) function | recurrence \(\leftrightarrow\) ODE approximation |
| Local-global translation | local \(\to\) accumulated | derivative \(\leftrightarrow\) integral |
| Structural-spectral translation | structure \(\to\) modes | matrix \(\leftrightarrow\) eigenvalues |
| Generative-observational translation | dynamics \(\to\) observable | rotation \(\to\) cosine |
| Semantic-computational translation | meaning \(\to\) encoding | set membership \(\to\) bit |
| Algebraic-geometric translation | equation \(\to\) geometry | \(x^2+y^2=r^2\leftrightarrow\) circle |
| Probabilistic translation | state \(\to\) distribution | deterministic ensemble \(\to\) probability |

## 7. Compatibility Matrix

Instead of asking only which translations are already known, the ontology should ask which classes should logically permit a translation.

| From / To | Scalar | Vector | Set | Bits | Geometry | Function | Spectrum | Graph |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Scalar | yes | yes | conditional | yes | yes | yes | yes | conditional |
| Vector | yes | yes | conditional | conditional | yes | yes | yes | yes |
| Set | yes | yes | yes | yes | yes | yes | conditional | yes |
| Bits | yes | yes | yes | yes | conditional | yes | yes | yes |
| Geometry | yes | yes | yes | conditional | yes | yes | yes | yes |
| Function | yes | yes | yes | yes | yes | yes | yes | yes |
| Spectrum | yes | yes | conditional | yes | yes | yes | yes | yes |
| Graph | yes | yes | yes | yes | yes | yes | yes | yes |

Conditional cells are research questions. They may require additional structure, a chosen universe, a metric, a sampling convention, or a representation map.

## 8. Information Preservation

Safe imputation requires explicit information accounting.

| Translation | Reversible? | Information |
|---|---|---|
| Cartesian \(\leftrightarrow\) polar | mostly yes | preserved, except origin ambiguity |
| Set \(\leftrightarrow\) bit vector | yes, with known universe | preserved |
| Complex \(\leftrightarrow (x,y)\) | yes | preserved |
| Complex \(\to\) real | no | lossy |
| Vector \(\to\) norm | no | strongly lossy |
| Time \(\leftrightarrow\) Fourier spectrum | yes under suitable conditions | preserved but redistributed |
| Matrix \(\to\) eigenvalues | generally no | lossy |
| Graph \(\to\) adjacency matrix | yes with node labeling | preserved |
| Function \(\to\) sampled values | generally no | potentially lossy |
| Integer \(\to\) prime factorization | yes | preserved |
| Multiplicative \(\to\) logarithmic | yes for positive values | preserved |
| Continuous \(\to\) threshold bits | no | compressed |

Three especially useful bond classes are:

$$
\begin{aligned}
\text{Isomorphism} &: \text{lossless and reversible},\\
\text{Embedding} &: \text{lossless into richer structure},\\
\text{Projection} &: \text{lossy reduction}.
\end{aligned}
$$

Translations that cannot be exactly inverted belong to approximation or inference.

## 9. Path Completion

If the graph contains

$$
A\leftrightarrow B
$$

and

$$
B\leftrightarrow C,
$$

then it is natural to ask whether a direct relation

$$
A\leftrightarrow C
$$

exists. This is path completion in the periodic graph.

Examples:

$$
\text{set}
\leftrightarrow
\text{bit vector}
\leftrightarrow
\text{vector}
\leftrightarrow
\text{geometry}.
$$

This explains how a set may acquire a geometric representation, as in many embedding methods.

Another example:

$$
\text{rotation}
\leftrightarrow
\text{complex exponential}
\leftrightarrow
\text{Fourier mode}
\leftrightarrow
\text{frequency}.
$$

This connects geometry and spectrum.

A third example:

$$
\text{set}
\leftrightarrow
\text{bitfield}
\leftrightarrow
\text{Boolean algebra}
\leftrightarrow
\text{polynomial algebra}
\leftrightarrow
\text{spectral representation}.
$$

## 10. Revised Topology

The expanded ontology has horizontal and vertical bonds:

$$
\begin{array}{ccccccc}
\textbf{OBJECT} &\to& \textbf{REPRESENTATION} &\to& \textbf{OPERATOR} &\to& \textbf{STATE}\\
&& \downarrow &&&& \downarrow\\
&& \textbf{COORDINATE} &&&& \textbf{DYNAMICS}\\
&& \downarrow &&&& \downarrow\\
&& \textbf{METRIC} &\to& \textbf{OBSERVER} &\to& \textbf{EVENT}\\
&&&&&& \downarrow\\
&&&&&& \textbf{INVARIANT}.
\end{array}
$$

| Layer | Contains |
|---|---|
| Objects | scalars, vectors, bits, sets, graphs, fields |
| Representations | binary, Cartesian, polar, complex, logarithmic, spectral |
| Operators | Boolean, set, vector, geometric, recursive, transform |
| Metrics | Euclidean, angular, Hamming, Jaccard, entropy |
| Dynamics | iteration, growth, rotation, flow, oscillation |
| Observers | projection, sampling, transform, derivative |
| Events | zero, crossing, closure, resonance, fixed point |
| Invariants | \(\pi,e,\varphi,\sqrt2,\gamma,\ldots\) |
| Bonds | translations between compatible nodes |

Each bond should include:

$$
(\text{source},\text{target},\text{operator},\text{reversible?},\text{lossy?},
\text{dimension change},\text{metric},\text{conditions}).
$$

The conditions field is crucial for safe imputation.

## Course Note

Discovery in the periodic graph follows the rule

$$
\text{missing edge}
+\text{compatible types}
+\text{composable known paths}
+\text{preserved invariants}
\Rightarrow
\text{candidate translation}.
$$

The ontology becomes a mathematical translation engine when each candidate translation is checked for type compatibility, information preservation, and invariant consistency.
