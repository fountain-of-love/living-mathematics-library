# §3.10 Continued Fractions

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.10, `Continued Fractions`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Introduction
- Relations to Power Series
- Numerical Evaluation of Continued Fractions

### Subsections

#### 3.10(i) Introduction

- See  1.12 for relevant properties of continued fractions, including the following definitions:
- $C_{n}$ is the $n$ th approximant or convergent to $C$ .

Formulas:

Formula 3.10.1:

$$
C=b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cdots}},
$$

Formula 3.10.2:

$$
C_{n}=b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cdots}}\frac{a_{n}}{b_{n}}=\frac{A_{n}}{B_{n}}.
$$


Definitions and local symbols:
- Defines: $C$ : continued fraction (locally)
- Defines: $A_{n}$ : continued fraction numerator (locally) , $B_{n}$ : continued fraction denominator (locally) and $C_{n}$ : continued fraction approximant (locally)

#### 3.10(ii) Relations to Power Series

- Every convergent, asymptotic, or formal series
- can be converted into a continued fraction $C$ of type ( 3.10.1 ), and with the property that the $n$ th convergent $C_{n}=A_{n}/B_{n}$ to $C$ is equal to the $n$ th partial sum of the series in ( 3.10.3 ), that is,
- For instance, if none of the $u_{n}$ vanish, then we can define
- However, other continued fractions with the same limit may converge in a much larger domain of the complex plane than the fraction given by ( 3.10.4 ) and ( 3.10.5 ). For example, by converting the Maclaurin expansion of $\operatorname{arctan}z$ ( 4.24.3 ), we obtain a continued fraction with the same region of convergence ( $\left|z\right|\leq 1$ , $z\neq\pm\mathrm{i}$ ), whereas the continued fraction ( 4.25.4 ) converges for all $z\in\mathbb{C}$ except on the branch cuts from $i$ to $i\infty$ and $-i$ to $-i\infty$ .

Formulas:

Formula 3.10.3:

$$
u_{0}+u_{1}+u_{2}+\cdots
$$

Formula 3.10.4:

$$
\frac{A_{n}}{B_{n}}=u_{0}+u_{1}+\dots+u_{n},
$$

Formula:

$$
\displaystyle b_{0}
$$

Formula:

$$
\displaystyle b_{1}
$$

Formula:

$$
\displaystyle a_{1}
$$

Formula:

$$
\displaystyle b_{n}
$$

Formula:

$$
\displaystyle a_{n}
$$

Formula 3.10.6:

$$
C=\cfrac{a_{0}}{1-\cfrac{a_{1}z}{1-\cfrac{a_{2}z}{1-\cdots}}}
$$

Formula 3.10.7:

$$
f(z)=c_{0}+c_{1}z+c_{2}z^{2}+\cdots
$$

Formula:

$$
\displaystyle e_{0}^{n}
$$

Formula:

$$
\displaystyle q_{1}^{n}
$$

Formula:

$$
\displaystyle e_{j}^{k}
$$

Formula:

$$
\displaystyle q_{j+1}^{k}
$$

Formula:

$$
\displaystyle a_{0}
$$

Formula:

$$
\displaystyle a_{2}
$$

Formula:

$$
\displaystyle a_{3}
$$

Formula:

$$
\displaystyle a_{4}
$$

Formula:

$$
\ldots.
$$

Formula 3.10.11:

$$
C=\cfrac{\beta_{0}}{1-\alpha_{0}z-\cfrac{\beta_{1}z^{2}}{1-\alpha_{1}z-\cfrac{\beta_{2}z^{2}}{1-\alpha_{2}z-\cdots}}}
$$


Definitions and local symbols:
- Keywords: continued fractions , relation to power series
- Defines: $u_{n}$ : series (locally)
- Symbols: $A_{n}$ : continued fraction numerator , $B_{n}$ : continued fraction denominator and $u_{n}$ : series
- Symbols: $u_{n}$ : series
- Keywords: $S$ -fraction , Stieltjes fraction , Stieltjes fraction ( $S$ -fraction) , continued fractions , relation to power series
- Symbols: $C$ : continued fraction
- Defines: $c_{n}$ : coefficients (locally)
- Keywords: continued fractions , quotient-difference algorithm , quotient-difference scheme , rhombus rule , stability
- Symbols: $e_{j}^{k}$ : element and $q_{j}^{k}$ : element
- Symbols: $c_{n}$ : coefficients , $e_{j}^{k}$ : element and $q_{j}^{k}$ : element
- Symbols: $e_{j}^{k}$ : element and $q_{j}^{k}$ : element
- Symbols: $c_{n}$ : coefficients , $e_{j}^{k}$ : element and $q_{j}^{k}$ : element
- Keywords: $J$ -fraction , Jacobi fraction , Jacobi fraction ( $J$ -fraction) , associated , continued fractions
- Symbols: $C$ : continued fraction

#### 3.10(iii) Numerical Evaluation of Continued Fractions

Formulas:

Formula:

$$
\displaystyle u_{n}
$$

Formula:

$$
\displaystyle u_{k}
$$

Formula 3.10.13:

$$
C=\cfrac{a_{0}}{1-\cfrac{a_{1}}{1-\cfrac{a_{2}}{1-\cdots}}}
$$

Formula 3.10.14:

$$
C=\sum_{k=0}^{\infty}t_{k},
$$

Formula:

$$
\displaystyle t_{0}
$$

Formula:

$$
\displaystyle t_{k}
$$

Formula:

$$
\displaystyle\rho_{0}
$$

Formula:

$$
\displaystyle\rho_{k}
$$

Formula:

$$
\displaystyle C_{0}
$$

Formula:

$$
\displaystyle D_{1}
$$

Formula:

$$
\displaystyle\nabla C_{1}
$$

Formula:

$$
\displaystyle C_{1}
$$

Formula:

$$
\displaystyle D_{n}
$$

Formula:

$$
\displaystyle\nabla C_{n}
$$

Formula:

$$
\displaystyle C_{n}
$$


Definitions and local symbols:
- Keywords: continued fractions , forward recurrence , numerical evaluation
- Keywords: backward recurrence , continued fractions , numerical evaluation
- Symbols: $u_{n}$ : series
- Keywords: continued fractions , forward series recurrence , numerical evaluation
- Symbols: $C$ : continued fraction
- Symbols: $C$ : continued fraction
- Keywords: Steed's algorithm , for continued fractions
- Symbols: $C_{n}$ : continued fraction approximant
- Symbols: $C_{n}$ : continued fraction approximant

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.10](https://dlmf.nist.gov/3.10)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: continued fractions, relation to power series, S -fraction, Stieltjes fraction, Stieltjes fraction ( S -fraction), quotient-difference algorithm, quotient-difference scheme, rhombus rule, stability, J -fraction, Jacobi fraction, Jacobi fraction ( J -fraction), associated, forward recurrence, numerical evaluation, backward recurrence, forward series recurrence, Steed's algorithm, for continued fractions, -fraction, Jacobi fraction (, Stieltjes fraction (.

### Source Notes

- See Blanch ( 1964 ) . For the original source of the quotient-difference algorithm see Rutishauser ( 1957 ) .
- See Wall ( 1948 , pp. 17-19) , Barnett et al. ( 1974 ) , and Barnett ( 1981a ) .
