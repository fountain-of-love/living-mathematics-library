# §3.9 Acceleration of Convergence

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.9, `Acceleration of Convergence`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Sequence Transformations
- Euler's Transformation of Series
- Aitken's  2 -Process
- Shanks' Transformation
- Levin's and Weniger's Transformations
- Applications and Further Transformations

### Subsections

#### 3.9(i) Sequence Transformations

- All sequences (series) in this section are sequences (series) of real or complex numbers.
- A transformation of a convergent sequence $\{s_{n}\}$ with limit $\sigma$ into a sequence $\{t_{n}\}$ is called limit-preserving if $\{t_{n}\}$ converges to the same limit $\sigma$ .
- The transformation is accelerating if it is limit-preserving and if
- Similarly for convergent series if we regard the sum as the limit of the sequence of partial sums.
- It should be borne in mind that a sequence (series) transformation can be effective for one type of sequence (series) but may not accelerate convergence for another type. It may even fail altogether by not being limit-preserving.

Formulas:

Formula 3.9.1:

$$
\lim_{n\to\infty}\frac{t_{n}-\sigma}{s_{n}-\sigma}=0.
$$


Definitions and local symbols:
- Keywords: acceleration of convergence , definition , limit-preserving
- Symbols: $s_{n}$ : sequence , $t_{n}$ : sequence and $\sigma$ : limit

#### 3.9(ii) Euler's Transformation of Series

- If $S=\sum_{k=0}^{\infty}(-1)^{k}a_{k}$ is a convergent series, then
- provided that the right-hand side converges. Here $\Delta$ is the forward difference operator :
- Thus
- Euler's transformation is usually applied to alternating series. Examples are provided by the following analytic transformations of slowly-convergent series into rapidly convergent ones:

Formulas:

Formula 3.9.2:

$$
S=\sum_{k=0}^{\infty}(-1)^{k}2^{-k-1}\Delta^{k}a_{0},
$$

Formula 3.9.3:

$$
\Delta^{k}a_{0}=\Delta^{k-1}a_{1}-\Delta^{k-1}a_{0},
$$

Formula 3.9.4:

$$
\Delta^{k}a_{0}=\sum_{m=0}^{k}(-1)^{m}\genfrac{(}{)}{0.0pt}{}{k}{m}a_{k-m}.
$$

Formula 3.9.5:

$$
\ln 2=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots=\frac{1}{1\cdot 2^{1}}+\frac{1}{2\cdot 2^{2}}+\frac{1}{3\cdot 2^{3}}+\cdots,
$$

Formula 3.9.6:

$$
\frac{\pi}{4}=1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\cdots=\frac{1}{2}\left(1+\frac{1!}{1\cdot 3}+\frac{2!}{3\cdot 5}+\frac{3!}{3\cdot 5\cdot 7}+\cdots\right).
$$


Definitions and local symbols:
- Keywords: Euler's transformation , of series
- Symbols: $\Delta$ : forward difference operator and $S$ : a convergent series
- Symbols: $\Delta$ : forward difference operator
- Symbols: $\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}$ : binomial coefficient and $\Delta$ : forward difference operator
- Symbols: $\ln\NVar{z}$ : principal branch of logarithm function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter and $!$ : factorial (as in $n!$ )

#### 3.9(iii) Aitken's  2 -Process

- This transformation is accelerating if $\{s_{n}\}$ is a linearly convergent sequence , i.e., a sequence for which
- When applied repeatedly, Aitken's process is known as the iterated $\Delta^{2}$ -process . See Brezinski and Redivo Zaglia ( 1991 , pp. 39-42) .

Formulas:

Formula 3.9.7:

$$
t_{n}=s_{n}-\frac{(\Delta s_{n})^{2}}{\Delta^{2}s_{n}}=s_{n}-\frac{(s_{n+1}-s_{n})^{2}}{s_{n+2}-2s_{n+1}+s_{n}}.
$$

Formula 3.9.8:

$$
\lim_{n\to\infty}\frac{s_{n+1}-\sigma}{s_{n}-\sigma}=\rho,
$$


Definitions and local symbols:
- Keywords: Aitken's $\Delta^{2}$ -process , for sequences , iterated
- Symbols: $s_{n}$ : sequence and $t_{n}$ : sequence
- Symbols: $s_{n}$ : sequence

#### 3.9(iv) Shanks' Transformation

- Shanks' transformation is a generalization of Aitken's $\Delta^{2}$ -process. Let $k$ be a fixed positive integer. Then the transformation of the sequence $\{s_{n}\}$ into a sequence $\{t_{n,2k}\}$ is given by
- where $H_{m}$ is the Hankel determinant
- The ratio of the Hankel determinants in ( 3.9.9 ) can be computed recursively by Wynn's epsilon algorithm :
- Then $t_{n,2k}=\varepsilon_{2k}^{(n)}$ . Aitken's $\Delta^{2}$ -process is the case $k=1$ .
- If $s_{n}$ is the $n$ th partial sum of a power series $f$ , then $t_{n,2k}=\varepsilon_{2k}^{(n)}$ is the Pad approximant $[(n+k)/k]_{f}$ ( 3.11(iv) ).
- For further information on the epsilon algorithm see Brezinski and Redivo Zaglia ( 1991 , pp. 78-95) .

Formulas:

Formula 3.9.9:

$$
t_{n,2k}=\frac{H_{k+1}(s_{n})}{H_{k}(\Delta^{2}s_{n})},
$$

Formula 3.9.10:

$$
H_{m}(u_{n})=\begin{vmatrix}u_{n}&u_{n+1}&\cdots&u_{n+m-1}\\ u_{n+1}&u_{n+2}&\cdots&u_{n+m}\\ \vdots&\vdots&\ddots&\vdots\\ u_{n+m-1}&u_{n+m}&\cdots&u_{n+2m-2}\end{vmatrix}.
$$

Formula:

$$
\displaystyle\varepsilon_{-1}^{(n)}
$$

Formula:

$$
\displaystyle\varepsilon_{0}^{(n)}
$$

Formula:

$$
\displaystyle\varepsilon_{m+1}^{(n)}
$$

Formula 3.9.12:

$$
s_{n}=\sum_{j=1}^{n}\frac{(-1)^{j+1}}{j^{2}},
$$


Definitions and local symbols:
- Keywords: Hankel , Shanks' transformation , Wynn's epsilon algorithm , determinants , for sequences
- Symbols: $s_{n}$ : sequence , $t_{n}$ : sequence and $H_{m}(u)$ : Hankel determinant
- Defines: $H_{m}(u)$ : Hankel determinant (locally)
- Symbols: $\det$ : determinant
- Symbols: $s_{n}$ : sequence
- Symbols: $s_{n}$ : sequence
- Symbols: $s_{n}$ : sequence and $t_{n}$ : sequence

#### 3.9(v) Levin's and Weniger's Transformations

- We give a special form of Levin's transformation in which the sequence $s=\{s_{n}\}$ of partial sums $s_{n}=\sum_{j=0}^{n}a_{j}$ is transformed into:
- where $k$ is a fixed nonnegative integer, and
- Sequences that are accelerated by Levin's transformation include logarithmically convergent sequences, i.e., sequences $s_{n}$ converging to $\sigma$ such that
- For further information see Brezinski and Redivo Zaglia ( 1991 , pp. 39-42) .
- In Weniger's transformations the numbers $c_{j,k,n}$ in ( 3.9.13 ) are chosen as follows:
- or

Formulas:

Formula 3.9.13:

$$
{\cal L}_{k}^{(n)}(s)=\frac{\sum_{j=0}^{k}(-1)^{j}\genfrac{(}{)}{0.0pt}{}{k}{j}c_{j,k,n}\ifrac{s_{n+j}}{a_{n+j+1}}}{\sum_{j=0}^{k}(-1)^{j}\genfrac{(}{)}{0.0pt}{}{k}{j}c_{j,k,n}/a_{n+j+1}},
$$

Formula 3.9.14:

$$
c_{j,k,n}=\frac{(n+j+1)^{k-1}}{(n+k+1)^{k-1}}.
$$

Formula 3.9.15:

$$
\lim_{n\to\infty}\frac{s_{n+1}-\sigma}{s_{n}-\sigma}=1.
$$

Formula 3.9.16:

$$
c_{j,k,n}=\frac{{\left(\beta+n+j\right)_{k-1}}}{{\left(\beta+n+k\right)_{k-1}}},
$$

Formula 3.9.17:

$$
c_{j,k,n}=\frac{{\left(-\gamma-n-j\right)_{k-1}}}{{\left(-\gamma-n-k\right)_{k-1}}},
$$


Definitions and local symbols:
- Keywords: Levin's transformations , Weniger's transformation , convergence , for sequences , iterative methods , logarithmic
- Symbols: $\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}$ : binomial coefficient , $s_{n}$ : sequence and $c_{j,k,n}$ : coefficient
- Defines: $c_{j,k,n}$ : coefficient (locally)
- Symbols: $s_{n}$ : sequence and $\sigma$ : limit
- Symbols: ${\left(\NVar{a}\right)_{\NVar{n}}}$ : Pochhammer's symbol (or shifted factorial) , $c_{j,k,n}$ : coefficient and $\beta$ : arbitrary constant
- Symbols: ${\left(\NVar{a}\right)_{\NVar{n}}}$ : Pochhammer's symbol (or shifted factorial) , $\gamma$ : arbitrary constant and $c_{j,k,n}$ : coefficient

#### 3.9(vi) Applications and Further Transformations

- For examples and other transformations for convergent sequences and series, see Wimp ( 1981 , pp. 156-199) , Brezinski and Redivo Zaglia ( 1991 , pp. 55-72) , and Sidi ( 2003 , Chapters 6, 12-13, 15-16, 19-24, and pp. 483-492) .
- For applications to asymptotic expansions, see  2.11(vi) , Olver ( 1997b , pp. 540-543) , and Weniger ( 1989 , 2003 ) .

Definitions and local symbols:
- Keywords: acceleration of convergence , for sequences , for series

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.9](https://dlmf.nist.gov/3.9)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: acceleration of convergence, for sequences, for series, definition, limit-preserving, Euler's transformation, of series, Aitken's  2 -process, iterated, Hankel, Shanks' transformation, Wynn's epsilon algorithm, determinants, Levin's transformations, Weniger's transformation, convergence, iterative methods, logarithmic, Aitken's.

### Source Notes

- See Knopp ( 1964 , pp. 253-255) .
