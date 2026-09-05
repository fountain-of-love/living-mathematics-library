# §1.1 Special Notation

## Mathematical Content

This section defines the default meanings of variables, integer indices, scalar products, vector and matrix operations, adjoints, traces, and operator notation used throughout Chapter 1.

### Mathematical Narrative

- For notation outside this local Chapter 1 convention table, DLMF points to its global notation section for special functions.
- Variables and indices are scoped by mathematical role: real variables, complex variables, integers, nonnegative integers, vectors, matrices, distributions, and linear operators.
- Matrix notation distinguishes inverse, identity, determinant, trace, exponential trace, adjoint, complex conjugate, transpose, and Hermitian conjugate.
- The source notes that physics, applied mathematics, and engineering literature often write complex conjugation with a star and Hermitian conjugation with a dagger.

### Notation Table

| Symbol | Mathematical Meaning |
|---|---|
| $x,y$ | real variables. |
| $z$ | complex variable in  1.2(i) , 1.9 - 1.11 , real variable in  1.5 - 1.6 . |
| $w$ | complex variable in  1.9 - 1.11 . |
| $j,k,\ell$ | integers. |
| $m,n$ | nonnegative integers, unless specified otherwise. |
| $\left\langle f,g\right\rangle$ | inner, or scalar, product for real or complex vectors or functions. |
| $L^{2}\left(X,\,\mathrm{d}\alpha\right)$ | the space of all Lebesgue-Stieltjes measurable functions on $X$ which are square integrable with respect to $\,\mathrm{d}\alpha$ . |
| $\phi$ | a testing function. |
| $\left\langle\Lambda,\phi\right\rangle$ | action of distribution $\Lambda$ on test function $\phi$ . |
| $\deg$ | degree. |
| primes | derivatives with respect to the variable, except where indicated otherwise. |
| $\mathbf{u}$ , $\mathbf{v}$ | column vectors. |
| $\mathbf{E}_{n}$ | the space of all $n$ -dimensional vectors. |
| $\mathbf{A}$ | or $[a_{i,j}]$ or $[a_{ij}]$ matrix with elements $a_{i,j}$ or $a_{ij}$ . |
| ${\mathbf{A}}^{-1}$ | inverse of the square matrix $\mathbf{A}$ |
| $\mathbf{I}$ | identity matrix |
| $\det(\mathbf{A})$ | determinant of the square matrix $\mathbf{A}$ |
| $\operatorname{tr}(\mathbf{A})$ | trace of the square matrix $\mathbf{A}$ |
| $\operatorname{etr}\left(\mathbf{A}\right)$ | exponential of $\operatorname{tr}(\mathbf{A})$ |
| ${\mathbf{A}}^{*}$ | adjoint of the square matrix $\mathbf{A}$ |
| $\overline{\mathbf{A}}$ | complex conjugate of the matrix $\mathbf{A}$ |
| $\mathbf{A}^{\mathrm{T}}$ | transpose of the matrix $\mathbf{A}$ |
| ${\mathbf{A}}^{{\rm H}}$ | Hermitian conjugate of the matrix $\mathbf{A}$ |
| $\mathcal{L}$ | linear operator defined on a manifold $\mathcal{M}$ |
| ${\mathcal{L}}^{*}$ | adjoint of $\mathcal{L}$ defined on the dual manifold ${\mathcal{M}}^{*}$ |

## Rendering and Source Details

### Source

- Source: [https://dlmf.nist.gov/1.1](https://dlmf.nist.gov/1.1)
- Observed version: 1.2.7, release date 2026-06-15.

### Source Metadata

- Permalink: http://dlmf.nist.gov/1.1
- Addition (effective with 1.2.0): A sentence was added at the end of this section.
- See also: Annotations for Ch.1

### Notation Rendering Details

This table separates DLMF's HTML/math metadata from the mathematical meaning above. `Obsidian inline math` is the Markdown rendering form to use in notes; `DLMF display` is the source page's HTML display mode.

| Obsidian inline math | TeX alt text | DLMF display | Semantic titles |
|---|---|---|---|
| $x,y$ | `x,y` | inline | - |
| $z$ | `z` | inline | variable |
| $w$ | `w` | inline | variable |
| $j,k,\ell$ | `j,k,\ell` | inline | integer |
| $m,n$ | `m,n` | inline | nonnegative integer |
| $\left\langle f,g\right\rangle$ | `\left\langle f,g\right\rangle` | inline | inner product over functions |
| $L^{2}\left(X,\,\mathrm{d}\alpha\right)$ | `L^{2}\left(X,\,\mathrm{d}\alpha\right)` | inline | Lebesgue-Stieltjes measurable, square integrable, complex-valued functions, differential of  |
| $X$ | `X` | inline | - |
| $\,\mathrm{d}\alpha$ | `\,\mathrm{d}\alpha` | inline | differential of  |
| $\phi$ | `\phi` | inline | - |
| $\left\langle\Lambda,\phi\right\rangle$ | `\left\langle\Lambda,\phi\right\rangle` | inline | action of distribution on test function |
| $\Lambda$ | `\Lambda` | inline | - |
| $\deg$ | `\deg` | inline | - |
| $\mathbf{u}$ | `\mathbf{u}` | inline | - |
| $\mathbf{v}$ | `\mathbf{v}` | inline | - |
| $\mathbf{E}_{n}$ | `\mathbf{E}_{n}` | inline | E n : space of n -dimensional vectors, real or complex |
| $n$ | `n` | inline | nonnegative integer |
| $\mathbf{A}$ | `\mathbf{A}` | inline | - |
| $[a_{i,j}]$ | `[a_{i,j}]` | inline | integer |
| $[a_{ij}]$ | `[a_{ij}]` | inline | integer |
| $a_{i,j}$ | `a_{i,j}` | inline | integer |
| $a_{ij}$ | `a_{ij}` | inline | integer |
| ${\mathbf{A}}^{-1}$ | `{\mathbf{A}}^{-1}` | inline | matrix inverse |
| $\mathbf{I}$ | `\mathbf{I}` | inline | identity matrix |
| $\det(\mathbf{A})$ | `\det(\mathbf{A})` | inline | determinant |
| $\operatorname{tr}(\mathbf{A})$ | `\operatorname{tr}(\mathbf{A})` | inline | trace of matrix |
| $\operatorname{etr}\left(\mathbf{A}\right)$ | `\operatorname{etr}\left(\mathbf{A}\right)` | inline | exponential of trace |
| ${\mathbf{A}}^{*}$ | `{\mathbf{A}}^{*}` | inline | adjoint of matrix |
| $\overline{\mathbf{A}}$ | `\overline{\mathbf{A}}` | inline | complex conjugate |
| $\mathbf{A}^{\mathrm{T}}$ | `\mathbf{A}^{\mathrm{T}}` | inline | transpose of matrix |
| ${\mathbf{A}}^{{\rm H}}$ | `{\mathbf{A}}^{{\rm H}}` | inline | Hermitian conjugate of matrix |
| $\mathcal{L}$ | `\mathcal{L}` | inline | - |
| $\mathcal{M}$ | `\mathcal{M}` | inline | - |
| ${\mathcal{L}}^{*}$ | `{\mathcal{L}}^{*}` | inline | adjoint of matrix |
| ${\mathcal{M}}^{*}$ | `{\mathcal{M}}^{*}` | inline | adjoint of matrix |
| $\overline{a}$ | `\overline{a}` | inline | complex conjugate |
| $a^{*}$ | `a^{*}` | inline | - |
| $a$ | `a` | inline | - |
| $\mathbf{A}^{{\dagger}}$ | `\mathbf{A}^{{\dagger}}` | inline | - |

### Semantic Titles and Cross References

| Symbol | Encoded semantic titles | Cross references in meaning |
|---|---|---|
| $x,y$ | - | - |
| $z$ | $z$: variable | [1.2(i)](https://dlmf.nist.gov/1.2#i) - 1.2(i) Binomial Coefficients  1.2 Elementary Algebra  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods; [1.9](https://dlmf.nist.gov/1.9) - 1.9 Calculus of a Complex Variable  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods; [1.11](https://dlmf.nist.gov/1.11) - 1.11 Zeros of Polynomials  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods; [1.5](https://dlmf.nist.gov/1.5) - 1.5 Calculus of Two or More Variables  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods; [1.6](https://dlmf.nist.gov/1.6) - 1.6 Vectors and Vector-Valued Functions  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods |
| $w$ | $w$: variable | [1.9](https://dlmf.nist.gov/1.9) - 1.9 Calculus of a Complex Variable  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods; [1.11](https://dlmf.nist.gov/1.11) - 1.11 Zeros of Polynomials  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods |
| $j,k,\ell$ | $j,k,\ell$: integer | - |
| $m,n$ | $m,n$: nonnegative integer | - |
| $\left\langle f,g\right\rangle$ | $\left\langle f,g\right\rangle$: inner product over functions | - |
| $L^{2}\left(X,\,\mathrm{d}\alpha\right)$ | $L^{2}\left(X,\,\mathrm{d}\alpha\right)$: Lebesgue-Stieltjes measurable, square integrable, complex-valued functions, differential of  | - |
| $\phi$ | - | - |
| $\left\langle\Lambda,\phi\right\rangle$ | $\left\langle\Lambda,\phi\right\rangle$: action of distribution on test function | - |
| $\deg$ | - | - |
| primes | - | - |
| $\mathbf{u}$ , $\mathbf{v}$ | - | - |
| $\mathbf{E}_{n}$ | $\mathbf{E}_{n}$: E n : space of n -dimensional vectors, real or complex | - |
| $\mathbf{A}$ | - | - |
| ${\mathbf{A}}^{-1}$ | ${\mathbf{A}}^{-1}$: matrix inverse | - |
| $\mathbf{I}$ | $\mathbf{I}$: identity matrix | - |
| $\det(\mathbf{A})$ | $\det(\mathbf{A})$: determinant | - |
| $\operatorname{tr}(\mathbf{A})$ | $\operatorname{tr}(\mathbf{A})$: trace of matrix | - |
| $\operatorname{etr}\left(\mathbf{A}\right)$ | $\operatorname{etr}\left(\mathbf{A}\right)$: exponential of trace | - |
| ${\mathbf{A}}^{*}$ | ${\mathbf{A}}^{*}$: adjoint of matrix | - |
| $\overline{\mathbf{A}}$ | $\overline{\mathbf{A}}$: complex conjugate | - |
| $\mathbf{A}^{\mathrm{T}}$ | $\mathbf{A}^{\mathrm{T}}$: transpose of matrix | - |
| ${\mathbf{A}}^{{\rm H}}$ | ${\mathbf{A}}^{{\rm H}}$: Hermitian conjugate of matrix | - |
| $\mathcal{L}$ | - | - |
| ${\mathcal{L}}^{*}$ | ${\mathcal{L}}^{*}$: adjoint of matrix | - |

### Related Links

| Label | URL | Source title |
|---|---|---|
| http://dlmf.nist.gov/1.1 | https://dlmf.nist.gov/1.1 | - |
| Ch.1 | https://dlmf.nist.gov/1#info | Chapter 1 Algebraic and Analytic Methods |
| Notation for the Special Functions | https://dlmf.nist.gov/front/introduction#notations | In Mathematical Introduction |
| 1.2(i) | https://dlmf.nist.gov/1.2#i | 1.2(i) Binomial Coefficients  1.2 Elementary Algebra  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods |
| 1.9 | https://dlmf.nist.gov/1.9 | 1.9 Calculus of a Complex Variable  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods |
| 1.11 | https://dlmf.nist.gov/1.11 | 1.11 Zeros of Polynomials  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods |
| 1.5 | https://dlmf.nist.gov/1.5 | 1.5 Calculus of Two or More Variables  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods |
| 1.6 | https://dlmf.nist.gov/1.6 | 1.6 Vectors and Vector-Valued Functions  Topics of Discussion  Chapter 1 Algebraic and Analytic Methods |

## Retrieval Coverage

- Notation rows extracted: 25.
- Unique math elements extracted: 39.
- Related links extracted: 8.
- Prose was summarized rather than mirrored verbatim; mathematical symbols, meanings, semantic titles, and links were extracted structurally.
