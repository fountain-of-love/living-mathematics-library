# §2.9 Difference Equations

Source: [https://dlmf.nist.gov/2.9](https://dlmf.nist.gov/2.9)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.9. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Distinct Characteristic Values
- Coincident Characteristic Values
- Other Approximations

## Keywords

asymptotic solutions of difference equations, characteristic equation, difference equations, coincident characteristic values, with a parameter, Liouville-Green (or WKBJ) approximation, Liouville-Green (or WKBJ) type approximations, for difference equations, transition points, turning points

## Principal Formula Blocks

- Formula block (2.9.1)

```tex
{w(n+2)+f(n)w(n+1)+g(n)w(n)=0},
```

- Formula block (2.9.2)

```tex
\Delta^{2}w(n)+(2+f(n))\Delta w(n)+(1+f(n)+g(n))w(n)=0,
```

- Formula block

```tex
\displaystyle f(n)
```

- Formula block

```tex
\displaystyle g(n)
```

- Formula block (2.9.4)

```tex
\rho_{j}^{n}n^{\alpha_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{n^{s}},
```

- Formula block (2.9.5)

```tex
\rho^{2}+f_{0}\rho+g_{0}=0,
```

- Formula block (2.9.6)

```tex
\alpha_{j}=(f_{1}\rho_{j}+g_{1})/(f_{0}\rho_{j}+2g_{0}),
```

- Formula block (2.9.7)

```tex
\rho_{j}(f_{0}+2\rho_{j})sa_{s,j}=\sum_{r=1}^{s}\left(\rho_{j}^{2}2^{r+1}% \genfrac{(}{)}{0.0pt}{}{\alpha_{j}+r-s}{r+1}+\rho_{j}\sum_{q=0}^{r+1}\genfrac{% (}{)}{0.0pt}{}{\alpha_{j}+r-s}{r+1-q}f_{q}+g_{r+1}\right)a_{s-r,j},
```

- Formula block (2.9.8)

```tex
w_{j}(n)\sim\rho_{j}^{n}n^{\alpha_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{n^{s}},
```

- Formula block (2.9.9)

```tex
w_{j}(n)\sim\rho^{n}\exp\left((-1)^{j}\kappa\sqrt{n}\right)n^{\alpha}\sum_{s=0% }^{\infty}(-1)^{js}\frac{c_{s}}{n^{s/2}},
```

- Formula block (2.9.10)

```tex
\sqrt{g_{0}}\kappa=\sqrt{2f_{0}f_{1}-4g_{1}},
```

- Formula block (2.9.11)

```tex
2g_{0}\alpha^{2}-(f_{0}f_{1}+2g_{0})\alpha+2g_{2}-f_{0}f_{2}=0.
```

- Formula block (2.9.12)

```tex
w_{j}(n)\sim\rho^{n}n^{\alpha_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{n^{s}},
```

- Formula block (2.9.13)

```tex
w_{2}(n)\sim\rho^{n}n^{\alpha_{2}}\sum_{\begin{subarray}{c}s=0\\ s\neq\alpha_{2}-\alpha_{1}\end{subarray}}^{\infty}\frac{b_{s}}{n^{s}}+cw_{1}(n% )\ln n,
```

- Formula block (2.9.14)

```tex
w(n+2)+n^{P}f(n)w(n+1)+n^{Q}g(n)w(n)=0,
```


## Definitions and Symbols

- Keywords: asymptotic solutions of difference equations
- Keywords: asymptotic solutions of difference equations , characteristic equation , difference equations
- Symbols: `f(n)` : function , `g(n)` : function , `n` : nonnegative integer and `w(n)` : solution
- Symbols: `\Delta` : forward difference operator , `f(n)` : function , `g(n)` : function , `n` : nonnegative integer and `w(n)` : solution
- Symbols: `\sim` : Poincar asymptotic expansion , `f(n)` : function , `g(n)` : function , `n` : nonnegative integer , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `n` : nonnegative integer , `a_{s,j}` : coefficients and `\rho_{j}` : roots
- Symbols: `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `f_{s}` : coefficients , `g_{s}` : coefficients and `\rho_{j}` : roots
- Symbols: `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `f_{s}` : coefficients , `g_{s}` : coefficients , `a_{s,j}` : coefficients and `\rho_{j}` : roots
- Symbols: `\sim` : Poincar asymptotic expansion , `n` : nonnegative integer , `a_{s,j}` : coefficients , `\rho_{j}` : roots and `w_{j}(n)` : solutions
- Keywords: asymptotic solutions of difference equations , coincident characteristic values , with a parameter
- Symbols: `\sim` : Poincar asymptotic expansion , `\exp\NVar{z}` : exponential function , `\rho` : roots , `\kappa` , `c` : constant and `w_{j}(n)` : solutions
- Symbols: `\kappa` , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\rho` : roots and `w_{j}(n)` : solutions
- Symbols: `\sim` : Poincar asymptotic expansion , `\ln\NVar{z}` : principal branch of logarithm function , `\rho` : roots , `b_{s}` : coefficients , `c` : constant and `w_{j}(n)` : solutions
- Symbols: `f(n)` : function , `P` : integer , `Q` : integer and `g(n)` : function
- Keywords: Liouville-Green (or WKBJ) approximation , Liouville-Green (or WKBJ) type approximations , asymptotic solutions of difference equations , for difference equations , transition points , turning points , with a parameter

## Subsections

### 2.9(i) Distinct Characteristic Values

- Many special functions that depend on parameters satisfy a three-term linear recurrence relation
- or equivalently the second-order homogeneous linear difference equation
- in which `\Delta` is the forward difference operator ( 3.6(i) ).
- Often `f(n)` and `g(n)` can be expanded in series
- with `g_{0}\neq 0` . (For the case `g_{0}=0` see the final paragraph of  2.9(ii) with `Q` negative.) This situation is analogous to second-order homogeneous linear differential equations with an irregular singularity of rank 1 at infinity ( 2.7(ii) ). Formal solutions are
- where `\rho_{1},\rho_{2}` are the roots of the characteristic equation

Formula blocks:
- Formula block (2.9.1)

```tex
{w(n+2)+f(n)w(n+1)+g(n)w(n)=0},
```

- Formula block (2.9.2)

```tex
\Delta^{2}w(n)+(2+f(n))\Delta w(n)+(1+f(n)+g(n))w(n)=0,
```

- Formula block

```tex
\displaystyle f(n)
```

- Formula block

```tex
\displaystyle g(n)
```

- Formula block (2.9.4)

```tex
\rho_{j}^{n}n^{\alpha_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{n^{s}},
```

- Formula block (2.9.5)

```tex
\rho^{2}+f_{0}\rho+g_{0}=0,
```

- Formula block (2.9.6)

```tex
\alpha_{j}=(f_{1}\rho_{j}+g_{1})/(f_{0}\rho_{j}+2g_{0}),
```

- Formula block (2.9.7)

```tex
\rho_{j}(f_{0}+2\rho_{j})sa_{s,j}=\sum_{r=1}^{s}\left(\rho_{j}^{2}2^{r+1}% \genfrac{(}{)}{0.0pt}{}{\alpha_{j}+r-s}{r+1}+\rho_{j}\sum_{q=0}^{r+1}\genfrac{% (}{)}{0.0pt}{}{\alpha_{j}+r-s}{r+1-q}f_{q}+g_{r+1}\right)a_{s-r,j},
```

- Formula block (2.9.8)

```tex
w_{j}(n)\sim\rho_{j}^{n}n^{\alpha_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{n^{s}},
```


Local metadata:
- Keywords: asymptotic solutions of difference equations , characteristic equation , difference equations
- Symbols: `f(n)` : function , `g(n)` : function , `n` : nonnegative integer and `w(n)` : solution
- Symbols: `\Delta` : forward difference operator , `f(n)` : function , `g(n)` : function , `n` : nonnegative integer and `w(n)` : solution
- Symbols: `\sim` : Poincar asymptotic expansion , `f(n)` : function , `g(n)` : function , `n` : nonnegative integer , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `n` : nonnegative integer , `a_{s,j}` : coefficients and `\rho_{j}` : roots
- Symbols: `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `f_{s}` : coefficients , `g_{s}` : coefficients and `\rho_{j}` : roots
- Symbols: `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `f_{s}` : coefficients , `g_{s}` : coefficients , `a_{s,j}` : coefficients and `\rho_{j}` : roots
- Symbols: `\sim` : Poincar asymptotic expansion , `n` : nonnegative integer , `a_{s,j}` : coefficients , `\rho_{j}` : roots and `w_{j}(n)` : solutions

### 2.9(ii) Coincident Characteristic Values

- When the roots of ( 2.9.5 ) are equal we denote them both by `\rho` . Assume first `2g_{1}\neq f_{0}f_{1}` . Then ( 2.9.1 ) has independent solutions `w_{j}(n)` , `j=1,2` , such that
- where
- `c_{0}=1` , and higher coefficients are determined by formal substitution.
- Alternatively, suppose that `2g_{1}=f_{0}f_{1}` . Then the indices `\alpha_{1},\alpha_{2}` are the roots of
- Provided that `\alpha_{2}-\alpha_{1}` is not zero or an integer, ( 2.9.1 ) has independent solutions `w_{j}(n)` , `j=1,2` , of the form
- with `a_{0,j}=1` and higher coefficients given by ( 2.9.7 ) (in the present case the coefficients of `a_{s,j}` and `a_{s-1,j}` are zero).

Formula blocks:
- Formula block (2.9.9)

```tex
w_{j}(n)\sim\rho^{n}\exp\left((-1)^{j}\kappa\sqrt{n}\right)n^{\alpha}\sum_{s=0% }^{\infty}(-1)^{js}\frac{c_{s}}{n^{s/2}},
```

- Formula block (2.9.10)

```tex
\sqrt{g_{0}}\kappa=\sqrt{2f_{0}f_{1}-4g_{1}},
```

- Formula block (2.9.11)

```tex
2g_{0}\alpha^{2}-(f_{0}f_{1}+2g_{0})\alpha+2g_{2}-f_{0}f_{2}=0.
```

- Formula block (2.9.12)

```tex
w_{j}(n)\sim\rho^{n}n^{\alpha_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{n^{s}},
```

- Formula block (2.9.13)

```tex
w_{2}(n)\sim\rho^{n}n^{\alpha_{2}}\sum_{\begin{subarray}{c}s=0\\ s\neq\alpha_{2}-\alpha_{1}\end{subarray}}^{\infty}\frac{b_{s}}{n^{s}}+cw_{1}(n% )\ln n,
```

- Formula block (2.9.14)

```tex
w(n+2)+n^{P}f(n)w(n+1)+n^{Q}g(n)w(n)=0,
```


Local metadata:
- Keywords: asymptotic solutions of difference equations , coincident characteristic values , with a parameter
- Symbols: `\sim` : Poincar asymptotic expansion , `\exp\NVar{z}` : exponential function , `\rho` : roots , `\kappa` , `c` : constant and `w_{j}(n)` : solutions
- Symbols: `\kappa` , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\rho` : roots and `w_{j}(n)` : solutions
- Symbols: `\sim` : Poincar asymptotic expansion , `\ln\NVar{z}` : principal branch of logarithm function , `\rho` : roots , `b_{s}` : coefficients , `c` : constant and `w_{j}(n)` : solutions
- Symbols: `f(n)` : function , `P` : integer , `Q` : integer and `g(n)` : function

### 2.9(iii) Other Approximations

- For asymptotic approximations to solutions of second-order difference equations analogous to the Liouville-Green (WKBJ) approximation for differential equations ( 2.7(iii) ) see Spigler and Vianello ( 1992 , 1997 ) and Spigler et al. ( 1999 ) . Error bounds and applications are included.
- For discussions of turning points, transition points, and uniform asymptotic expansions for solutions of linear difference equations of the second order see Wang and Wong ( 2003 , 2005 ) .
- For an introduction to, and references for, the general asymptotic theory of linear difference equations of arbitrary order, see Wimp ( 1984 , Appendix B) .
- For applications of asymptotic methods for difference equations to orthogonal polynomials, see, e.g. Wang and Wong ( 2012 ) and Wong ( 2014 ) . These methods are particularly useful when the weight function associated with the orthogonal polynomials is not unique or not even known; see, e.g. Dai et al. ( 2014 ) .

Local metadata:
- Keywords: Liouville-Green (or WKBJ) approximation , Liouville-Green (or WKBJ) type approximations , asymptotic solutions of difference equations , for difference equations , transition points , turning points , with a parameter
