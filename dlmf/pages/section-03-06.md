# §3.6 Linear Difference Equations

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.6, `Linear Difference Equations`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Introduction
- Homogeneous Equations
- Miller's Algorithm
- Inhomogeneous Equations
- Olver's Algorithm
- Examples
- Linear Difference Equations of Other Orders

### Subsections

#### 3.6(i) Introduction

- Many special functions satisfy second-order recurrence relations, or difference equations, of the form
- or equivalently,
- where $\Delta w_{n-1}=w_{n}-w_{n-1}$ , $\Delta^{2}w_{n-1}=\Delta w_{n}-\Delta w_{n-1}$ , and $n\in\mathbb{Z}$ . If $d_{n}=0$ , $\forall n$ , then the difference equation is homogeneous ; otherwise it is inhomogeneous .
- Difference equations are simple and attractive for computation. In practice, however, problems of severe instability often arise and in  3.6(ii) - 3.6(vii) we show how these difficulties may be overcome.

Formulas:

Formula 3.6.1:

$$
a_{n}w_{n+1}-b_{n}w_{n}+c_{n}w_{n-1}=d_{n},
$$

Formula 3.6.2:

$$
a_{n}\Delta^{2}w_{n-1}+(2a_{n}-b_{n})\Delta w_{n-1}+(a_{n}-b_{n}+c_{n})w_{n-1}=d_{n},
$$


Definitions and local symbols:
- Defines: $\Delta$ : forward difference operator
- Defines: $a_{n}$ : coefficient (locally) , $b_{n}$ : coefficient (locally) , $c_{n}$ : coefficient (locally) and $d_{n}$ : coefficient (locally)
- Symbols: $w_{n}$ : sequence
- Symbols: $\Delta$ : forward difference operator , $w_{n}$ : sequence , $a_{n}$ : coefficient , $b_{n}$ : coefficient , $c_{n}$ : coefficient and $d_{n}$ : coefficient

#### 3.6(ii) Homogeneous Equations

- Given numerical values of $w_{0}$ and $w_{1}$ , the solution $w_{n}$ of the equation
- with $a_{n}\neq 0$ , $\forall n$ , can be computed recursively for $n=2,3,\dots$ . Unless exact arithmetic is being used, however, each step of the calculation introduces rounding errors. These errors have the effect of perturbing the solution by unwanted small multiples of $w_{n}$ and of an independent solution $g_{n}$ , say. This is of little consequence if the wanted solution is growing in magnitude at least as fast as any other solution of ( 3.6.3 ), and the recursion process is stable .
- But suppose that $w_{n}$ is a nontrivial solution such that
- Then $w_{n}$ is said to be a recessive (equivalently, minimal or distinguished ) solution as $n\to\infty$ , and it is unique except for a constant factor. In this situation the unwanted multiples of $g_{n}$ grow more rapidly than the wanted solution, and the computations are unstable . Stability can be restored, however, by backward recursion , provided that $c_{n}\neq 0$ , $\forall n$ : starting from $w_{N}$ and $w_{N+1}$ , with $N$ large, equation ( 3.6.3 ) is applied to generate in succession $w_{N-1},w_{N-2},\dots,w_{0}$ . The unwanted multiples of $g_{n}$ now decay in comparison with $w_{n}$ , hence are of little consequence.
- The values of $w_{N}$ and $w_{N+1}$ needed to begin the backward recursion may be available, for example, from asymptotic expansions ( 2.9 ). However, there are alternative procedures that do not require $w_{N}$ and $w_{N+1}$ to be known in advance. These are described in  3.6(iii) and 3.6(v) .

Formulas:

Formula 3.6.3:

$$
a_{n}w_{n+1}-b_{n}w_{n}+c_{n}w_{n-1}=0,
$$

Formula 3.6.4:

$$
w_{n}/g_{n}\to 0,
$$


Definitions and local symbols:
- Keywords: backward recursion , backward recursion method , difference equations , distinguished solutions , homogeneous equations , minimal solutions , numerical solution , recessive solutions , stability
- Symbols: $w_{n}$ : sequence , $a_{n}$ : coefficient , $b_{n}$ : coefficient and $c_{n}$ : coefficient
- Symbols: $w_{n}$ : sequence and $g_{n}$ : solution

#### 3.6(iii) Miller's Algorithm

- Because the recessive solution of a homogeneous equation is the fastest growing solution in the backward direction, it occurred to J.C.P. Miller ( Bickley et al. ( 1952 , pp. xvi-xvii) ) that arbitrary "trial values" can be assigned to $w_{N}$ and $w_{N+1}$ , for example, $1$ and $0$ . A "trial solution" is then computed by backward recursion, in the course of which the original components of the unwanted solution $g_{n}$ die away. It therefore remains to apply a normalizing factor $\Lambda$ . The process is then repeated with a higher value of $N$ , and the normalized solutions compared. If agreement is not within a prescribed tolerance the cycle is continued.
- The normalizing factor $\Lambda$ can be the true value of $w_{0}$ divided by its trial value, or $\Lambda$ can be chosen to satisfy a known property of the wanted solution of the form
- where the $\lambda$ 's are constants. The latter method is usually superior when the true value of $w_{0}$ is zero or pathologically small.
- For further information on Miller's algorithm, including examples, convergence proofs, and error analyses, see Wimp ( 1984 , Chapter 4) , Gautschi ( 1967 , 1997b ) , and Olver ( 1964a ) . See also Gautschi ( 1967 ) and Gil et al. ( 2007a , Chapter 4) for the computation of recessive solutions via continued fractions.

Formulas:

Formula 3.6.5:

$$
\sum_{n=0}^{\infty}\lambda_{n}w_{n}=1,
$$


Definitions and local symbols:
- Keywords: Miller's algorithm , difference equations , homogeneous equations , normalizing factor , numerical solution
- Symbols: $w_{n}$ : sequence and $\lambda_{n}$ : constants

#### 3.6(iv) Inhomogeneous Equations

- Similar principles apply to equation ( 3.6.1 ) when $a_{n}c_{n}\neq 0$ , $\forall n$ , and $d_{n}\neq 0$ for some, or all, values of $n$ . If, as $n\to\infty$ , the wanted solution $w_{n}$ grows (decays) in magnitude at least as fast as any solution of the corresponding homogeneous equation, then forward (backward) recursion is stable.
- A new problem arises, however, if, as $n\to\infty$ , the asymptotic behavior of $w_{n}$ is intermediate to those of two independent solutions $f_{n}$ and $g_{n}$ of the corresponding inhomogeneous equation (the complementary functions). More precisely, assume that $f_{0}\neq 0$ , $g_{n}\neq 0$ for all sufficiently large $n$ , and as $n\to\infty$
- Then computation of $w_{n}$ by forward recursion is unstable. If it also happens that $f_{n}/w_{n}\to 0$ as $n\to\infty$ , then computation of $w_{n}$ by backward recursion is unstable as well. However, $w_{n}$ can be computed successfully in these circumstances by boundary-value methods , as follows.
- Let us assume the normalizing condition is of the form $w_{0}=\lambda$ , where $\lambda$ is a constant, and then solve the following tridiagonal system of algebraic equations for the unknowns $w_{1}^{(N)},w_{2}^{(N)},\dots,w_{N-1}^{(N)}$ ; see  3.2(ii) . Here $N$ is an arbitrary positive integer.
- Then as $N\to\infty$ with $n$ fixed, $w_{n}^{(N)}\to w_{n}$ .

Formulas:

Formula:

$$
\displaystyle f_{n}/g_{n}
$$

Formula:

$$
\displaystyle w_{n}/g_{n}
$$

Formula 3.6.7:

$$
\begin{bmatrix}-b_{1}&a_{1}&&&0\\ c_{2}&-b_{2}&a_{2}\\ &\ddots&\ddots&\ddots\\ &&c_{N-2}&-b_{N-2}&a_{N-2}\\ 0&&&c_{N-1}&-b_{N-1}\end{bmatrix}\begin{bmatrix}w_{1}^{(N)}\\ w_{2}^{(N)}\\ \vdots\\ w_{N-2}^{(N)}\\ w_{N-1}^{(N)}\end{bmatrix}=\begin{bmatrix}d_{1}-c_{1}\lambda\\ d_{2}\\ \vdots\\ d_{N-2}\\ d_{N-1}\end{bmatrix}.
$$


Definitions and local symbols:
- Keywords: backward recursion method , boundary-value methods , boundary-value methods or problems , difference equations , inhomogeneous equations , numerical solution
- Symbols: $w_{n}$ : sequence and $g_{n}$ : solution
- Symbols: $w_{n}$ : sequence , $N$ : arbitrary positive integer , $a_{n}$ : coefficient , $b_{n}$ : coefficient , $c_{n}$ : coefficient , $d_{n}$ : coefficient and $\lambda$ : constant

#### 3.6(v) Olver's Algorithm

- To apply the method just described a succession of values can be prescribed for the arbitrary integer $N$ and the results compared. However, a more powerful procedure combines the solution of the algebraic equations with the determination of the optimum value of $N$ . It is applicable equally to the computation of the recessive solution of the homogeneous equation ( 3.6.3 ) or the computation of any solution $w_{n}$ of the inhomogeneous equation ( 3.6.1 ) for which the conditions of  3.6(iv) are satisfied.
- Suppose again that $f_{0}\neq 0$ , $w_{0}$ is given, and we wish to calculate $w_{1},w_{2},\dots,w_{M}$ to a prescribed relative accuracy $\epsilon$ for a given value of $M$ . We first compute, by forward recurrence, the solution $p_{n}$ of the homogeneous equation ( 3.6.3 ) with initial values $p_{0}=0$ , $p_{1}=1$ . At the same time we construct a sequence $e_{n}$ , $n=0,1,\dots$ , defined by
- beginning with $e_{0}=w_{0}$ . (This part of the process is equivalent to forward elimination.) The computation is continued until a value $N$ ( $\geq M$ ) is reached for which
- Then $w_{n}$ is generated by backward recursion from
- starting with $w_{N}=0$ . (This part of the process is back substitution.)
- An example is included in the next subsection. For further information, including a more general form of normalizing condition, other examples, convergence proofs, and error analyses, see Olver ( 1967a ) , Olver and Sookne ( 1972 ) , and Wimp ( 1984 , Chapter 6) .

Formulas:

Formula 3.6.8:

$$
a_{n}e_{n}=c_{n}e_{n-1}-d_{n}p_{n},
$$

Formula 3.6.9:

$$
\left|\frac{e_{N}}{p_{N}p_{N+1}}\right|\leq\epsilon\min_{1\leq n\leq M}\left|\frac{e_{n}}{p_{n}p_{n+1}}\right|.
$$

Formula 3.6.10:

$$
p_{n+1}w_{n}=p_{n}w_{n+1}+e_{n},
$$


Definitions and local symbols:
- Keywords: Olver's algorithm , difference equations
- Defines: $e_{n}$ : sequence (locally)
- Symbols: $p_{n}$ : solutions , $a_{n}$ : coefficient , $c_{n}$ : coefficient and $d_{n}$ : coefficient
- Symbols: $N$ : arbitrary positive integer , $\epsilon$ : relative accuracy , $M$ : order , $p_{n}$ : solutions and $e_{n}$ : sequence
- Symbols: $w_{n}$ : sequence , $p_{n}$ : solutions and $e_{n}$ : sequence

#### 3.6(vi) Examples

Formulas:

Formula 3.6.11:

$$
w_{n+1}-2nw_{n}+w_{n-1}=0,
$$

Formula 3.6.12:

$$
J_{n}\left(1\right)\sim\frac{1}{(2\pi n)^{1/2}}\left(\frac{e}{2n}\right)^{n},
$$

Formula 3.6.13:

$$
Y_{n}\left(1\right)\sim\left(\frac{2}{\pi n}\right)^{1/2}\left(\frac{2n}{e}\right)^{n},
$$

Formula 3.6.14:

$$
w_{n+1}-2nw_{n}+w_{n-1}=-(2/\pi)(1-(-1)^{n}),
$$

Formula 3.6.15:

$$
\displaystyle\mathbf{E}_{2n}\left(1\right)
$$

Formula 3.6.16:

$$
\displaystyle\mathbf{E}_{2n+1}\left(1\right)
$$


Definitions and local symbols:
- Keywords: Bessel functions , Miller's algorithm , computation by recursion , difference equations
- Symbols: $w_{n}$ : sequence
- Symbols: $J_{\NVar{\nu}}\left(\NVar{z}\right)$ : Bessel function of the first kind , $\sim$ : asymptotic equality , $\pi$ : the ratio of the circumference of a circle to its diameter and $\mathrm{e}$ : base of natural logarithm
- Symbols: $Y_{\NVar{\nu}}\left(\NVar{z}\right)$ : Bessel function of the second kind , $\sim$ : asymptotic equality , $\pi$ : the ratio of the circumference of a circle to its diameter and $\mathrm{e}$ : base of natural logarithm
- Keywords: Anger-Weber functions , computation
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter and $w_{n}$ : sequence
- Symbols: $\mathbf{E}_{\NVar{\nu}}\left(\NVar{z}\right)$ : Weber function , $\sim$ : asymptotic equality and $\pi$ : the ratio of the circumference of a circle to its diameter
- Symbols: $\mathbf{E}_{\NVar{\nu}}\left(\NVar{z}\right)$ : Weber function , $\sim$ : asymptotic equality and $\pi$ : the ratio of the circumference of a circle to its diameter
- Symbols: $\mathbf{E}_{\NVar{\nu}}\left(\NVar{z}\right)$ : Weber function , $w_{n}$ : sequence , $p_{n}$ : solutions and $e_{n}$ : sequence
- Keywords: Olver's algorithm , difference equations

#### 3.6(vii) Linear Difference Equations of Other Orders

- Similar considerations apply to the first-order equation
- Thus in the inhomogeneous case it may sometimes be necessary to recur backwards to achieve stability. For analyses and examples see Gautschi ( 1997b ) .
- For a difference equation of order $k$ ( $\geq 3$ ),
- or for systems of $k$ first-order inhomogeneous equations, boundary-value methods are the rule rather than the exception. Typically $k-\ell$ conditions are prescribed at the beginning of the range, and $\ell$ conditions at the end. Here $\ell\in[0,k]$ , and its actual value depends on the asymptotic behavior of the wanted solution in relation to those of the other solutions. Within this framework forward and backward recursion may be regarded as the special cases $\ell=0$ and $\ell=k$ , respectively.
- For further information see Wimp ( 1984 , Chapters 7-8) , Cash and Zahar ( 1994 ) , and Lozier ( 1980 ) .

Formulas:

Formula 3.6.17:

$$
a_{n}w_{n+1}-b_{n}w_{n}=d_{n}.
$$

Formula 3.6.18:

$$
a_{n,k}w_{n+k}+a_{n,k-1}w_{n+k-1}+\dots+a_{n,0}w_{n}=d_{n},
$$


Definitions and local symbols:
- Keywords: boundary-value methods , boundary-value methods or problems , difference equations , numerical solution
- Symbols: $w_{n}$ : sequence , $a_{n}$ : coefficient , $b_{n}$ : coefficient and $d_{n}$ : coefficient
- Symbols: $w_{n}$ : sequence , $a_{n}$ : coefficient and $d_{n}$ : coefficient

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.6](https://dlmf.nist.gov/3.6)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: difference equations, numerical solution, backward recursion, backward recursion method, distinguished solutions, homogeneous equations, minimal solutions, recessive solutions, stability, Miller's algorithm, normalizing factor, boundary-value methods, boundary-value methods or problems, inhomogeneous equations, Olver's algorithm, Bessel functions, computation by recursion, Anger-Weber functions, computation.

### Source Notes

- See Olver ( 1967a ) .
