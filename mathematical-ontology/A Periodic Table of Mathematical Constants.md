# A Periodic Table of Mathematical Constants

## Guiding Principle

This classification organizes constants by the primitive relationship that makes them emerge, not by numerical size:

$$
\text{operation}
+\text{constraint}
+\text{repetition or self-consistency}
\longrightarrow
\text{characteristic constant}.
$$

This is a structural classification rather than a standard mathematical taxonomy.

## Structural Table

| Family | Symbol | Value | Primitive Operation | Defining Relation or Emergence | What It Stabilizes | Structural Meaning |
|---|---:|---:|---|---|---|---|
| Geometry | \(\pi\) | 3.14159... | rotate, close | \(C/D=\pi\) | circle under scale | constant of closed rotation |
| Geometry | \(\sqrt2\) | 1.41421... | combine orthogonally | \(1^2+1^2=(\sqrt2)^2\) | perpendicular distance | constant of diagonalization |
| Geometry | \(\sqrt3\) | 1.73205... | triangulate | equilateral altitude and diagonal relations | equilateral structure | constant of threefold Euclidean geometry |
| Recursion | \(\varphi\) | 1.61803... | recurse, divide | \(\varphi=1+1/\varphi\) | self-similar subdivision | recursive proportion |
| Recursion | \(\rho\) | 1.32472... | three-step recursion | \(\rho^3=\rho+1\) | higher-order recurrences | higher-order recursive proportion |
| Growth | \(e\) | 2.71828... | compound | \(f'=f\) | proportional growth | continuous change |
| Decay | \(e^{-1}\) | 0.367879... | remove proportionally | \((1-\frac1n)^n\to e^{-1}\) | residual under depletion | continuous survival |
| Scale | \(\ln2\) | 0.693147... | double, translate | \(e^{\ln2}=2\) | doubling in log coordinates | additive unit of doubling |
| Scale | \(\ln10\) | 2.302585... | decimal scale, translate | \(e^{\ln10}=10\) | powers of ten on log scale | additive unit of decimal scaling |
| Discrete-continuous | \(\gamma\) | 0.577215... | sum, integrate | \(H_n-\ln n\to\gamma\) | harmonic-logarithmic gap | discrete-continuous residue |
| Oscillation | \(i\) | \(\sqrt{-1}\) | quarter-turn | \(i^2=-1\) | rotation under multiplication | algebraic unit of phase |
| Oscillation | \(2\pi\) | 6.28318... | complete phase | \(e^{i2\pi}=1\) | full cycle return | angular period |
| Dynamics | \(\delta_F\) | 4.66920... | bifurcate | ratio of period-doubling intervals | approach to chaos | recursive instability scale |
| Dynamics | \(\alpha_F\) | 2.50290... | rescale bifurcations | spatial scaling in period doubling | shape across bifurcations | chaotic self-similarity |
| Continued fractions | \(K\) | 2.68545... | approximate recursively | typical geometric mean of continued-fraction coefficients | generic irrational approximation | continued-fraction complexity |
| Number theory | \(G\) | 0.915965... | alternate, accumulate | \(1-\frac1{3^2}+\frac1{5^2}-\cdots\) | alternating reciprocal-square structure | Catalan's constant |
| Number theory | \(\zeta(2)\) | \(\pi^2/6\) | sum reciprocals | \(\sum n^{-2}=\pi^2/6\) | inverse-square accumulation | bridge between counting and geometry |
| Number theory | \(\zeta(3)\) | 1.202056... | sum cubic reciprocals | \(\sum n^{-3}\) | inverse-cube accumulation | Apery's constant |
| Probability | \(1/\sqrt{2\pi}\) | 0.398942... | aggregate random variation | Gaussian normalization | total probability \(=1\) | random additive fluctuation |

## Transformation Families

### I. Geometry: Relationships in Space

The constants

$$
\sqrt2,\quad \sqrt3,\quad \pi
$$

arise because geometry imposes fixed constraints:

$$
\text{orthogonality}\to\sqrt2,
$$

$$
\text{equilateral geometry}\to\sqrt3,
$$

$$
\text{closure under rotation}\to\pi.
$$

The common pattern is

$$
\text{spatial relation}\to\text{fixed ratio}.
$$

### II. Recursion: Relationships That Reproduce Themselves

For the golden ratio,

$$
\varphi=1+\frac1\varphi.
$$

The relationship survives its own decomposition:

$$
\text{divide the structure}\to\text{recover the same proportion}.
$$

The plastic constant has a related higher-order recurrence:

$$
\rho^3=\rho+1.
$$

These may be called self-reproduction constants.

### III. Exponential Change: Change Acting on Change

The defining property of \(e\) is

$$
\frac{d}{dx}e^x=e^x.
$$

Change and state have the same form. The growth and decay forms are

$$
e^x,\qquad e^{-x}.
$$

For proportional depletion,

$$
\left(1-\frac1n\right)^n\to e^{-1}.
$$

Structurally:

$$
\text{state}
\xrightarrow{\text{relative change}}
\text{new state}
\xrightarrow{\text{relative change}}
\cdots
\to e.
$$

### IV. Phase: Repetition by Rotation

The phase family contains \(i\) and \(\pi\). Multiplication by \(i\) rotates by a quarter turn:

$$
1\to i\to -1\to -i\to 1.
$$

Continuous rotation is expressed by

$$
e^{i\theta}.
$$

The cycle closes at

$$
\theta=2\pi,\qquad e^{i2\pi}=1.
$$

Thus

$$
i=\text{elementary rotational operator},
$$

while

$$
2\pi=\text{complete rotational period}.
$$

Euler's identity joins growth, rotation, and algebraic opposition:

$$
e^{i\pi}+1=0.
$$

### V. Scale Conversion

Scale-conversion constants appear when multiplication is transformed into addition:

$$
2^x=e^{x\ln2},
$$

$$
10^x=e^{x\ln10}.
$$

The constant \(\ln a\) is the natural additive distance corresponding to multiplication by \(a\):

$$
\ln a=\text{natural additive distance for multiplication by }a.
$$

This gives the family

$$
\ln2,\quad \ln3,\quad \ln5,\quad \ldots
$$

### VI. Boundary Constants

Euler's constant \(\gamma\) measures the residual difference between harmonic accumulation and logarithmic growth:

$$
H_n=1+\frac12+\frac13+\cdots+\frac1n\approx\ln n+\gamma,
$$

so

$$
\gamma=\lim_{n\to\infty}(H_n-\ln n).
$$

In structural form,

$$
\text{discrete accumulation}-\text{continuous approximation}=\gamma.
$$

This makes \(\gamma\) a boundary or translation residue: it measures what remains when one mathematical description is mapped into another.

### VII. Universality Constants

The Feigenbaum constant

$$
\delta\approx4.6692016
$$

appears across many nonlinear systems undergoing successive period doublings:

$$
1\to2\to4\to8\to16\to\cdots.
$$

The distances between bifurcation points shrink according to a universal ratio approximately equal to \(\delta\). The microscopic equations may differ, but the same relational architecture produces the same constant:

$$
\text{same relational architecture}\to\text{same constant}.
$$

## Compact Table

| Primitive | Characteristic Constant | Meaning |
|---|---|---|
| Combine perpendicular directions | \(\sqrt2\) | diagonal |
| Triangulate | \(\sqrt3\) | equilateral geometry |
| Self-divide / recurse | \(\varphi\) | recursive proportion |
| Compound | \(e\) | continuous proportional change |
| Deplete | \(e^{-1}\) | continuous residual |
| Rotate | \(\pi\) | curved angular measure |
| Quarter-turn algebraically | \(i\) | phase operator |
| Complete one phase | \(2\pi\) | cycle |
| Double in log space | \(\ln2\) | scale translation |
| Translate discrete to continuous | \(\gamma\) | residual correction |
| Period-double | \(\delta_F\) | route to chaos |
| Recursively approximate irrationals | \(K\) | continued-fraction scale |

Primitive operations can be placed underneath the constants:

$$
\begin{array}{ccl}
\text{intersect / combine} &\to& \sqrt2,\sqrt3,\\
\text{divide} &\to& \varphi,\\
\text{scale} &\to& e,\ln2,\\
\text{rotate} &\to& \pi,i,\\
\text{repeat} &\to& e,\varphi,\delta,\\
\text{discrete}\leftrightarrow\text{continuous} &\to& \gamma.
\end{array}
$$

## Constants as Invariants

Many natural constants may be viewed as invariants left behind by transformations.

For the golden ratio:

$$
x=1+\frac1x
\quad\Rightarrow\quad
x=\varphi.
$$

For the exponential:

$$
f'=f
\quad\Rightarrow\quad
f=e^x.
$$

For the circle:

$$
\frac{C}{D}=\pi.
$$

For the harmonic-logarithmic boundary:

$$
H_n-\ln n\to\gamma.
$$

The compact formulation is

$$
\text{natural constant}
=
\text{invariant left behind by a transformation}.
$$

Equivalently,

$$
\text{primitive operation}
\to
\text{relation}
\to
\text{iteration}
\to
\text{invariant}.
$$

The number is the fingerprint of that invariant.
