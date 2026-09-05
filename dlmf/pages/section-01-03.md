# §1.3 Determinants, Linear Operators, and Spectral Expansions

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.3, `Determinants, Linear Operators, and Spectral Expansions`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Determinants: Elementary Properties
- Special Determinants
- Infinite Determinants
- Matrices as Linear Operators

### Subsections

#### 1.3(i) Determinants: Elementary Properties

Formulas:

Formula 1.3.1:

$$
\det[a_{jk}]=\begin{vmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{vmatrix}=a_{11}a_{22}-a_{12}a_{21}.
$$

Formula 1.3.2:

$$
\det[a_{jk}]=\begin{vmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ a_{31}&a_{32}&a_{33}\end{vmatrix}=a_{11}\begin{vmatrix}a_{22}&a_{23}\\ a_{32}&a_{33}\end{vmatrix}-a_{12}\begin{vmatrix}a_{21}&a_{23}\\ a_{31}&a_{33}\end{vmatrix}+a_{13}\begin{vmatrix}a_{21}&a_{22}\\ a_{31}&a_{32}\end{vmatrix}=a_{11}a_{22}a_{33}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}.
$$

Formula 1.3.3:

$$
A_{jk}=(-1)^{j+k}M_{jk}.
$$

Formula 1.3.4:

$$
\det[a_{jk}]=\sum^{n}_{\ell=1}a_{j\ell}A_{j\ell}.
$$

Formula 1.3.5:

$$
\displaystyle\det\left(\mathbf{A}^{\mathrm{T}}\right)
$$

Formula 1.3.6:

$$
\displaystyle\det\left({\mathbf{A}}^{-1}\right)
$$

Formula 1.3.7:

$$
\displaystyle\det(\mathbf{A}\mathbf{B})
$$

Formula 1.3.8:

$$
{\begin{vmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{vmatrix}}^{2}\leq(a^{2}_{11}+a^{2}_{12})(a^{2}_{21}+a^{2}_{22}),
$$

Formula 1.3.9:

$$
\det[a_{jk}]^{2}\leq\left(\sum^{n}_{k=1}a^{2}_{1k}\right)\left(\sum^{n}_{k=1}a^{2}_{2k}\right)\dots\left(\sum^{n}_{k=1}a^{2}_{nk}\right).
$$

Formula 1.3.10:

$$
a_{j1}a_{k1}+a_{j2}a_{k2}+\dots+a_{jn}a_{kn}=0
$$


Definitions and local symbols:
- Keywords: cofactor , definition , determinants , minor , notation
- Keywords: cofactor , determinants , minor
- Symbols: $\det$ : determinant , $j$ : integer and $k$ : integer
- Symbols: $\det$ : determinant , $j$ : integer and $k$ : integer
- Defines: $A_{j k}$ : cofactor (locally)
- Symbols: $j$ : integer , $k$ : integer and $M_{j k}$ : minor
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer , $n$ : nonnegative integer and $A_{j k}$ : cofactor
- Keywords: determinants , properties
- Symbols: $\det$ : determinant , $\mathbf{A}^{\mathrm{T}}$ : transpose of matrix , $j$ : integer and $k$ : integer
- Symbols: $\det$ : determinant , ${\mathbf{A}}^{-1}$ : matrix inverse , $j$ : integer and $k$ : integer
- Symbols: $\det$ : determinant , $j$ : integer and $k$ : integer
- Keywords: Hadamard's inequality , Hadamard's inequality for determinants , determinants , inequalities
- Symbols: $\det$ : determinant
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Symbols: $j$ : integer , $k$ : integer and $n$ : nonnegative integer

#### 1.3(ii) Special Determinants

- An alternant is a determinant function of $n$ variables which changes sign when two of the variables are interchanged. Examples:

Formulas:

Formula 1.3.11:

$$
\det[f_{k}(x_{j})],
$$

Formula 1.3.12:

$$
\det[f(x_{j},y_{k})],
$$

Formula 1.3.13:

$$
\begin{vmatrix}1&x_{1}&x^{2}_{1}&\cdots&x^{n-1}_{1}\\ 1&x_{2}&x^{2}_{2}&\cdots&x^{n-1}_{2}\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 1&x_{n}&x^{2}_{n}&\cdots&x_{n}^{n-1}\end{vmatrix}=\prod_{1\leq j<k\leq n}(x_{k}-x_{j}).
$$

Formula 1.3.14:

$$
\det\left[\frac{1}{a_{j}-b_{k}}\right]=(-1)^{n(n-1)/2}\,\prod_{1\leq j<k\leq n}(a_{k}-a_{j})(b_{k}-b_{j})\Bigg/\prod^{n}_{j,k=1}(a_{j}-b_{k}).
$$

Formula 1.3.15:

$$
\begin{vmatrix}a_{1}&a_{2}&\cdots&a_{n}\\ a_{n}&a_{1}&\cdots&a_{n-1}\\ \vdots&\vdots&\ddots&\vdots\\ a_{2}&a_{3}&\cdots&a_{1}\end{vmatrix}=\prod^{n}_{k=1}(a_{1}+a_{2}\omega_{k}+a_{3}\omega_{k}^{2}+\dots+a_{n}\omega_{k}^{n-1}),
$$

Formula 1.3.16:

$$
t_{jk}=(x_{j}+a_{n})(x_{j}+a_{n-1})\cdots(x_{j}+a_{k+1})\,(x_{j}+b_{k})(x_{j}+b_{k-1})\cdots(x_{j}+b_{2}),
$$

Formula 1.3.17:

$$
\det[t_{jk}]=\prod_{1\leq j<k\leq n}(x_{j}-x_{k})\prod_{2\leq j\leq k\leq n}(b_{j}-a_{k}).
$$


Definitions and local symbols:
- Keywords: alternant , alternants , determinant , determinants
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Keywords: Vandermonde , Vandermondian , determinants
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Keywords: Cauchy , Cauchy determinant , determinants
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Keywords: circulant , determinants
- Symbols: $\det$ : determinant , $k$ : integer , $n$ : nonnegative integer and $\omega_{j}$ : roots of unity
- Keywords: Krattenthaler's formula , Krattenthaler's formula for determinants , determinants
- Defines: $t_{j k}$ : elements (locally)
- Symbols: $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer , $n$ : nonnegative integer and $t_{j k}$ : elements

#### 1.3(iii) Infinite Determinants

- Let $a_{j,k}$ be defined for all integer values of $j$ and $k$ , and $D_{n}[a_{j,k}]$ denote the $(2n+1)\times(2n+1)$ determinant
- If $D_{n}[a_{j,k}]$ tends to a limit $L$ as $n\to\infty$ , then we say that the infinite determinant $D_{\infty}[a_{j,k}]$ converges and $D_{\infty}[a_{j,k}]=L$ .
- Of importance for special functions are infinite determinants of Hill's type . These have the property that the double series
- converges ( 1.9(vii) ). Here $\delta_{j,k}$ is the Kronecker delta. Hill-type determinants always converge.
- For further information see Whittaker and Watson ( 1927 , pp. 36-40) and Magnus and Winkler ( 1966 , 2.3) .

Formulas:

Formula 1.3.18:

$$
D_{n}[a_{j,k}]=\begin{vmatrix}a_{-n,-n}&a_{-n,-n+1}&\dots&a_{-n,n}\\ a_{-n+1,-n}&a_{-n+1,-n+1}&\dots&a_{-n+1,n}\\ \vdots&\vdots&\ddots&\vdots\\ a_{n,-n}&a_{n,-n+1}&\dots&a_{n,n}\end{vmatrix}.
$$

Formula 1.3.19:

$$
\sum^{\infty}_{j,k=-\infty}\left|a_{j,k}-\delta_{j,k}\right|
$$


Definitions and local symbols:
- Keywords: Hill's type , convergence , determinants , infinite
- Defines: $D_{n}[a_{j,k}]$ : $(2n+1)\times(2n+1)$ determinant (locally)
- Symbols: $\det$ : determinant , $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Symbols: $\delta_{j,k}$ : Kronecker delta , $j$ : integer , $k$ : integer and $\left|x\right|$ : absolute value of $x$

#### 1.3(iv) Matrices as Linear Operators

Formulas:

Formula 1.3.20:

$$
\mathbf{u}=\sum_{i=1}^{n}c_{i}\mathbf{a}_{i},
$$

Formula 1.3.21:

$$
{\left\|{\mathbf{u}}\right\|}^{2}=\sum_{i=1}^{n}{\left|c_{i}\right|}^{2},
$$


Definitions and local symbols:
- Defines: ${\mathbf{A}}^{*}$ : adjoint of matrix
- Keywords: Parseval's equality , orthonormal expansions
- Symbols: $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors and $n$ : nonnegative integer
- Symbols: $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.3](https://dlmf.nist.gov/1.3)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: cofactor, minor, definition, determinants, notation, properties, Hadamard's inequality, Hadamard's inequality for determinants, inequalities, alternant, alternants, determinant, Vandermonde, Vandermondian, Cauchy, Cauchy determinant, circulant, Krattenthaler's formula, Krattenthaler's formula for determinants, Hill's type, convergence, infinite, Parseval's equality, orthonormal expansions.

### Source Notes

- See Vein and Dale ( 1999 , pp. 51-52, 57, 79-81) . For ( 1.3.17 ) see Bressoud ( 1999 , p. 67) .
- See Axler ( 2015 , Chapter 7 ) or Shilov ( 2013 , pages 181-192) .
