# §2.8 Differential Equations with a Parameter

Source: [https://dlmf.nist.gov/2.8](https://dlmf.nist.gov/2.8)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.8. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Classification of Cases
- Case I: No Transition Points
- Case II: Simple Turning Point
- Case III: Simple Pole
- Multiple and Fractional Turning Points
- Coalescing Transition Points

## Source Notes

- See Olver ( 1997b , pp. 362-363) .
- See Olver ( 1997b , pp. 364-368, 371-373) .
- See Olver ( 1997b , pp. 392-397 and 408-413) .
- See Olver ( 1997b , pp. 435-448) .

## Keywords

asymptotic solutions of differential equations, with a parameter, Liouville transformation, Liouville transformation for differential equations, classification of cases, transition points, turning points, in terms of elementary functions, Airy functions, envelope functions, in terms of Airy functions, Bessel functions, in terms of Bessel functions of fixed order, connection formulas across transition points, fractional or multiple, coalescing transition points, in terms of Bessel functions of variable order

## Principal Formula Blocks

- Formula block (2.8.1)

```tex
\ifrac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}=\left(u^{2}f(z)+g(z)\right)w,
```

- Formula block (2.8.2)

```tex
W=\dot{z}^{-1/2}w,
```

- Formula block (2.8.3)

```tex
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(u^{2}\dot{z}^{2}f(z)+\psi(% \xi)\right)W,
```

- Formula block (2.8.4)

```tex
\psi(\xi)=\dot{z}^{2}g(z)+\dot{z}^{1/2}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}\xi}% ^{2}}(\dot{z}^{-1/2}).
```

- Formula block

```tex
\displaystyle\dot{z}^{2}f(z)
```

- Formula block

```tex
\displaystyle\xi
```

- Formula block

```tex
\displaystyle\tfrac{2}{3}\xi^{3/2}
```

- Formula block

```tex
\displaystyle 2\xi^{1/2}
```

- Formula block (2.8.8)

```tex
\ifrac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(u^{2}\xi^{m}+\psi(\xi)% \right)W,
```

- Formula block (2.8.9)

```tex
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(\frac{u^{2}}{\xi}+\frac{% \rho}{\xi^{2}}\right)W,
```

- Formula block (2.8.10)

```tex
\ifrac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=(u^{2}+\psi(\xi))W,
```

- Formula block (2.8.11)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.12)

```tex
\displaystyle W_{n,2}(u,\xi)
```

- Formula block (2.8.13)

```tex
A_{s+1}(\xi)=-\tfrac{1}{2}A_{s}^{\prime}(\xi)+\tfrac{1}{2}\int\psi(\xi)A_{s}(% \xi)\,\mathrm{d}\xi,
```

- Formula block (2.8.14)

```tex
\ifrac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=(u^{2}\xi+\psi(\xi))W,
```

- Formula block (2.8.15)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.16)

```tex
\displaystyle W_{n,2}(u,\xi)
```

- Formula block (2.8.17)

```tex
B_{s}(\xi)=\begin{cases}\dfrac{1}{2\xi^{1/2}}\displaystyle\int_{0}^{\xi}\left(% \psi(v)A_{s}(v)-A_{s}^{\prime\prime}(v)\right)\dfrac{\,\mathrm{d}v}{v^{1/2}},&% \xi>0,\\ \dfrac{1}{2(-\xi)^{1/2}}\displaystyle\int_{\xi}^{0}\left(\psi(v)A_{s}(v)-A_{s}% ^{\prime\prime}(v)\right)\dfrac{\,\mathrm{d}v}{(-v)^{1/2}},&\xi<0,\end{cases}
```

- Formula block (2.8.18)

```tex
A_{s+1}(\xi)=-\tfrac{1}{2}B_{s}^{\prime}(\xi)+\tfrac{1}{2}\int\psi(\xi)B_{s}(% \xi)\,\mathrm{d}\xi,
```

- Formula block (2.8.19)

```tex
\operatorname{Ai}\left(x\right)=\operatorname{Bi}\left(x\right)
```

- Formula block (2.8.20)

```tex
\operatorname{envAi}\left(x\right)=\operatorname{envBi}\left(x\right)=\left({% \operatorname{Ai}}^{2}\left(x\right)+{\operatorname{Bi}}^{2}\left(x\right)% \right)^{1/2},
```

- Formula block

```tex
\displaystyle\operatorname{envAi}\left(x\right)
```

- Formula block

```tex
\displaystyle\operatorname{envBi}\left(x\right)
```

- Formula block (2.8.22)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.23)

```tex
\displaystyle W_{n,2}(u,\xi)
```

- Formula block (2.8.24)

```tex
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(\frac{u^{2}}{4\xi}+\frac{% \nu^{2}-1}{4\xi^{2}}+\frac{\psi(\xi)}{\xi}\right)W.
```

- Formula block (2.8.25)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.26)

```tex
\displaystyle W_{n,2}(u,\xi)
```

- Formula block (2.8.27)

```tex
B_{s}(\xi)=-A_{s}^{\prime}(\xi)+\frac{1}{\xi^{1/2}}\int_{0}^{\xi}\left(\psi(v)% A_{s}(v)-\left(\nu+\tfrac{1}{2}\right)A_{s}^{\prime}(v)\right)\frac{\,\mathrm{% d}v}{v^{1/2}},
```

- Formula block (2.8.28)

```tex
A_{s+1}(\xi)=\nu B_{s}(\xi)-\xi B_{s}^{\prime}(\xi)+\int\psi(\xi)B_{s}(\xi)\,% \mathrm{d}\xi,
```

- Formula block (2.8.29)

```tex
W_{n,3}(u,\xi)=|\xi|^{1/2}J_{\nu}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-% 1}\frac{A_{s}(\xi)}{u^{2s}}+O\left(\frac{1}{u^{2n-1}}\right)\right)-|\xi|J_{% \nu+1}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-2}\frac{B_{s}(\xi)}{u^{2s+1% }}+O\left(\frac{1}{u^{2n-2}}\right)\right),
```

- Formula block (2.8.30)

```tex
W_{n,4}(u,\xi)=|\xi|^{1/2}Y_{\nu}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-% 1}\frac{A_{s}(\xi)}{u^{2s}}+O\left(\frac{1}{u^{2n-1}}\right)\right)-|\xi|Y_{% \nu+1}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-2}\frac{B_{s}(\xi)}{u^{2s+1% }}+O\left(\frac{1}{u^{2n-2}}\right)\right).
```

- Formula block (2.8.31)

```tex
B_{s}(\xi)=-A_{s}^{\prime}(\xi)+\frac{1}{|\xi|^{1/2}}\int_{\xi}^{0}\left(\psi(% v)A_{s}(v)-\left(\nu+\tfrac{1}{2}\right)A_{s}^{\prime}(v)\right)\frac{\,% \mathrm{d}v}{|v|^{1/2}},
```

- Formula block (2.8.32)

```tex
J_{\nu}(x)+Y_{\nu}(x)=0.
```

- Formula block

```tex
\displaystyle\operatorname{env}\mskip-2.0muJ_{\nu}(x)
```

- Formula block

```tex
\displaystyle\operatorname{env}\mskip-2.0muY_{\nu}(x)
```

- Formula block (2.8.34)

```tex
\operatorname{env}\mskip-2.0muJ_{\nu}(x)=\operatorname{env}\mskip-2.0muY_{\nu}% (x)=\left({J_{\nu}}^{2}(x)+{Y_{\nu}}^{2}(x)\right)^{1/2},
```

- Formula block (2.8.35)

```tex
W_{n,3}(u,\xi)=|\xi|^{1/2}J_{\nu}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n-1}% \frac{A_{s}(\xi)}{u^{2s}}-|\xi|J_{\nu+1}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n% -2}\frac{B_{s}(\xi)}{u^{2s+1}}+|\xi|^{1/2}\operatorname{env}\mskip-2.0muJ_{\nu% }\left(u|\xi|^{1/2}\right)O\left(\frac{1}{u^{2n-1}}\right),
```

- Formula block (2.8.36)

```tex
W_{n,4}(u,\xi)=|\xi|^{1/2}Y_{\nu}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n-1}% \frac{A_{s}(\xi)}{u^{2s}}-|\xi|Y_{\nu+1}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n% -2}\frac{B_{s}(\xi)}{u^{2s+1}}+|\xi|^{1/2}\operatorname{env}\mskip-2.0muY_{\nu% }\left(u|\xi|^{1/2}\right)O\left(\frac{1}{u^{2n-1}}\right),
```


## Definitions and Symbols

- Keywords: asymptotic solutions of differential equations , with a parameter
- Keywords: Liouville transformation , Liouville transformation for differential equations , asymptotic solutions of differential equations , classification of cases , transition points , turning points , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `f(x)` : function , `g(x)` : function , `w` : solution and `u` : large real or complex parameter
- Symbols: `w` : solution , `W` : change of variable and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `f(x)` : function , `u` : large real or complex parameter , `W` : change of variable , `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi` and `\psi(\xi)` : function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `g(x)` : function , `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi` and `\psi(\xi)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `u` : large real or complex parameter , `W` : change of variable and `\psi(\xi)` : function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `u` : large real or complex parameter , `W` : change of variable and `\rho` : limit
- Keywords: asymptotic solutions of differential equations , in terms of elementary functions , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `W_{n,j}(u,\xi)` : solution , `u` : large real or complex parameter and `\psi(\xi)` : function
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\in` : element of , `\mathrm{e}` : base of natural logarithm , `n` : positive integer , `W_{n,j}(u,\xi)` : solution , `A_{s}(\xi)` : coefficients , `\mathbf{\Delta}_{j}(\alpha_{j})` : domain and `u` : large real or complex parameter
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\in` : element of , `\mathrm{e}` : base of natural logarithm , `n` : positive integer , `W_{n,j}(u,\xi)` : solution , `A_{s}(\xi)` : coefficients , `\mathbf{\Delta}_{j}(\alpha_{j})` : domain and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `A_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Defines: `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` and `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)`
- Keywords: Airy functions , asymptotic solutions of differential equations , envelope functions , in terms of Airy functions , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `W_{n,j}(u,\xi)` : solution , `u` : large real or complex parameter and `\psi(\xi)` : function
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function and `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` , `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)` and `c` : root
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` , `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)` and `c` : root
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Defines: `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` and `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)`
- Keywords: Bessel functions , asymptotic solutions of differential equations , envelope functions , in terms of Bessel functions of fixed order , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `u` : large real or complex parameter and `\psi(\xi)` : function
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `I_{\NVar{\nu}}\left(\NVar{z}\right)` : modified Bessel function of the first kind , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `K_{\NVar{\nu}}\left(\NVar{z}\right)` : modified Bessel function of the second kind , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\nu` : real nonnegative constant , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\nu` : real nonnegative constant , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\nu` : real nonnegative constant , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind and `\nu` : real nonnegative constant
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` , `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)` , `\nu` : real nonnegative constant and `X_{\nu}` : smallest positive root
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` , `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)` , `\nu` : real nonnegative constant and `X_{\nu}` : smallest positive root
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Keywords: asymptotic solutions of differential equations , connection formulas across transition points , fractional or multiple , turning points , with a parameter
- Keywords: asymptotic solutions of differential equations , coalescing transition points , in terms of Bessel functions of variable order , with a parameter

## Subsections

### 2.8(i) Classification of Cases

- Many special functions satisfy an equation of the form
- in which `u` is a real or complex parameter, and asymptotic solutions are needed for large `|u|` that are uniform with respect to `z` in a point set `\mathbf{D}` in `\mathbb{R}` or `\mathbb{C}` . For example, `u` can be the order of a Bessel function or degree of an orthogonal polynomial. The form of the asymptotic expansion depends on the nature of the transition points in `\mathbf{D}` , that is, points at which `f(z)` has a zero or singularity. Zeros of `f(z)` are also called turning points .
- There are three main cases. In Case I there are no transition points in `\mathbf{D}` and `g(z)` is analytic. In Case II `f(z)` has a simple zero at `z_{0}` and `g(z)` is analytic at `z_{0}` . In Case III `f(z)` has a simple pole at `z_{0}` and `(z-z_{0})^{2}g(z)` is analytic at `z_{0}` .
- The same approach is used in all three cases. First we apply the Liouville transformation ( 1.13(iv) ) to ( 2.8.1 ). This introduces new variables `W` and `\xi` , related by
- dots denoting differentiations with respect to `\xi` . Then
- where

Formula blocks:
- Formula block (2.8.1)

```tex
\ifrac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}=\left(u^{2}f(z)+g(z)\right)w,
```

- Formula block (2.8.2)

```tex
W=\dot{z}^{-1/2}w,
```

- Formula block (2.8.3)

```tex
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(u^{2}\dot{z}^{2}f(z)+\psi(% \xi)\right)W,
```

- Formula block (2.8.4)

```tex
\psi(\xi)=\dot{z}^{2}g(z)+\dot{z}^{1/2}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}\xi}% ^{2}}(\dot{z}^{-1/2}).
```

- Formula block

```tex
\displaystyle\dot{z}^{2}f(z)
```

- Formula block

```tex
\displaystyle\xi
```

- Formula block

```tex
\displaystyle\tfrac{2}{3}\xi^{3/2}
```

- Formula block

```tex
\displaystyle 2\xi^{1/2}
```

- Formula block (2.8.8)

```tex
\ifrac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(u^{2}\xi^{m}+\psi(\xi)% \right)W,
```

- Formula block (2.8.9)

```tex
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(\frac{u^{2}}{\xi}+\frac{% \rho}{\xi^{2}}\right)W,
```


Local metadata:
- Keywords: Liouville transformation , Liouville transformation for differential equations , asymptotic solutions of differential equations , classification of cases , transition points , turning points , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `f(x)` : function , `g(x)` : function , `w` : solution and `u` : large real or complex parameter
- Symbols: `w` : solution , `W` : change of variable and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `f(x)` : function , `u` : large real or complex parameter , `W` : change of variable , `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi` and `\psi(\xi)` : function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `g(x)` : function , `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi` and `\psi(\xi)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function and `\dot{\NVar{z}}` : derivative of `\NVar{z}` with respect to `\xi`
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `u` : large real or complex parameter , `W` : change of variable and `\psi(\xi)` : function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `u` : large real or complex parameter , `W` : change of variable and `\rho` : limit

### 2.8(ii) Case I: No Transition Points

- The transformed differential equation is
- in which `\xi` ranges over a bounded or unbounded interval or domain `\mathbf{\Delta}` , and `\psi(\xi)` is `C^{\infty}` or analytic on `\mathbf{\Delta}` . The parameter `u` is assumed to be real and positive. Corresponding to each positive integer `n` there are solutions `W_{n,j}(u,\xi)` , `j=1,2` , that depend on arbitrarily chosen reference points `\alpha_{j}` , are `C^{\infty}` or analytic on `\mathbf{\Delta}` , and as `u\to\infty`
- with `A_{0}(\xi)=1` and
- (the constants of integration being arbitrary). The expansions ( 2.8.11 ) and ( 2.8.12 ) are both uniform and differentiable with respect to `\xi` . The regions of validity `\mathbf{\Delta}_{j}(\alpha_{j})` comprise those points `\xi` that can be joined to `\alpha_{j}` in `\mathbf{\Delta}` by a path `\mathscr{Q}_{j}` along which `\Re v` is nondecreasing `(j=1)` or nonincreasing `(j=2)` as `v` passes from `\alpha_{j}` to `\xi` . In addition, `\mathcal{V}_{\mathscr{Q}_{j}}\left(A_{1}\right)` and `\mathcal{V}_{\mathscr{Q}_{j}}\left(A_{n}\right)` must be bounded on `\mathbf{\Delta}_{j}(\alpha_{j})` .
- For error bounds, extensions to pure imaginary or complex `u` , an extension to inhomogeneous differential equations, and examples, see Olver ( 1997b , Chapter 10) . This reference also supplies sufficient conditions to ensure that the solutions `W_{n,1}(u,\xi)` and `W_{n,2}(u,\xi)` having the properties ( 2.8.11 ) and ( 2.8.12 ) are independent of `n` .

Formula blocks:
- Formula block (2.8.10)

```tex
\ifrac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=(u^{2}+\psi(\xi))W,
```

- Formula block (2.8.11)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.12)

```tex
\displaystyle W_{n,2}(u,\xi)
```

- Formula block (2.8.13)

```tex
A_{s+1}(\xi)=-\tfrac{1}{2}A_{s}^{\prime}(\xi)+\tfrac{1}{2}\int\psi(\xi)A_{s}(% \xi)\,\mathrm{d}\xi,
```


Local metadata:
- Keywords: asymptotic solutions of differential equations , in terms of elementary functions , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `W_{n,j}(u,\xi)` : solution , `u` : large real or complex parameter and `\psi(\xi)` : function
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\in` : element of , `\mathrm{e}` : base of natural logarithm , `n` : positive integer , `W_{n,j}(u,\xi)` : solution , `A_{s}(\xi)` : coefficients , `\mathbf{\Delta}_{j}(\alpha_{j})` : domain and `u` : large real or complex parameter
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\in` : element of , `\mathrm{e}` : base of natural logarithm , `n` : positive integer , `W_{n,j}(u,\xi)` : solution , `A_{s}(\xi)` : coefficients , `\mathbf{\Delta}_{j}(\alpha_{j})` : domain and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `A_{s}(\xi)` : coefficients and `\psi(\xi)` : function

### 2.8(iii) Case II: Simple Turning Point

- The transformed differential equation is
- and for simplicity `\xi` is assumed to range over a finite or infinite interval `(\alpha_{1},\alpha_{2})` with `\alpha_{1}<0` , `\alpha_{2}>0` . Again, `u>0` and `\psi(\xi)` is `C^{\infty}` on `(\alpha_{1},\alpha_{2})` . Corresponding to each positive integer `n` there are solutions `W_{n,j}(u,\xi)` , `j=1,2` , that are `C^{\infty}` on `(\alpha_{1},\alpha_{2})` , and as `u\to\infty`
- Here `A_{0}(\xi)=1` ,
- and
- when `s=0,1,2,\dots` . For `\operatorname{Ai}` and `\operatorname{Bi}` see  9.2 . The expansions ( 2.8.15 ) and ( 2.8.16 ) are both uniform and differentiable with respect to `\xi` . These results are valid when `\mathcal{V}_{\alpha_{1},\alpha_{2}}\left(|\xi|^{1/2}B_{0}\right)` and `\mathcal{V}_{\alpha_{1},\alpha_{2}}\left(|\xi|^{1/2}B_{n-1}\right)` are finite.
- An alternative way of representing the error terms in ( 2.8.15 ) and ( 2.8.16 ) is as follows. Let `c=-0.36604\ldots` be the real root of the equation

Formula blocks:
- Formula block (2.8.14)

```tex
\ifrac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=(u^{2}\xi+\psi(\xi))W,
```

- Formula block (2.8.15)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.16)

```tex
\displaystyle W_{n,2}(u,\xi)
```

- Formula block (2.8.17)

```tex
B_{s}(\xi)=\begin{cases}\dfrac{1}{2\xi^{1/2}}\displaystyle\int_{0}^{\xi}\left(% \psi(v)A_{s}(v)-A_{s}^{\prime\prime}(v)\right)\dfrac{\,\mathrm{d}v}{v^{1/2}},&% \xi>0,\\ \dfrac{1}{2(-\xi)^{1/2}}\displaystyle\int_{\xi}^{0}\left(\psi(v)A_{s}(v)-A_{s}% ^{\prime\prime}(v)\right)\dfrac{\,\mathrm{d}v}{(-v)^{1/2}},&\xi<0,\end{cases}
```

- Formula block (2.8.18)

```tex
A_{s+1}(\xi)=-\tfrac{1}{2}B_{s}^{\prime}(\xi)+\tfrac{1}{2}\int\psi(\xi)B_{s}(% \xi)\,\mathrm{d}\xi,
```

- Formula block (2.8.19)

```tex
\operatorname{Ai}\left(x\right)=\operatorname{Bi}\left(x\right)
```

- Formula block (2.8.20)

```tex
\operatorname{envAi}\left(x\right)=\operatorname{envBi}\left(x\right)=\left({% \operatorname{Ai}}^{2}\left(x\right)+{\operatorname{Bi}}^{2}\left(x\right)% \right)^{1/2},
```

- Formula block

```tex
\displaystyle\operatorname{envAi}\left(x\right)
```

- Formula block

```tex
\displaystyle\operatorname{envBi}\left(x\right)
```

- Formula block (2.8.22)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.23)

```tex
\displaystyle W_{n,2}(u,\xi)
```


Local metadata:
- Defines: `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` and `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)`
- Keywords: Airy functions , asymptotic solutions of differential equations , envelope functions , in terms of Airy functions , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `W_{n,j}(u,\xi)` : solution , `u` : large real or complex parameter and `\psi(\xi)` : function
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function and `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` , `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)` and `c` : root
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` , `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)` and `c` : root
- Symbols: `\operatorname{Ai}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{envAi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Ai}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\operatorname{Bi}\left(\NVar{z}\right)` : Airy function , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{envBi}\left(\NVar{x}\right)` : envelope of Airy function `\operatorname{Bi}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter

### 2.8(iv) Case III: Simple Pole

- The transformed equation ( 2.8.8 ) is renormalized as
- We again assume `\xi\in(\alpha_{1},\alpha_{2})` with `-\infty\leq\alpha_{1}<0` , `0<\alpha_{2}\leq\infty` . Also, `\psi(\xi)` is `C^{\infty}` on `(\alpha_{1},\alpha_{2})` , and `u>0` . The constant `\nu` ( `=\sqrt{1+4\rho}` ) is real and nonnegative.
- There are two cases: `\xi\in(0,\alpha_{2})` and `\xi\in(\alpha_{1},0)` . In the former, corresponding to any positive integer `n` there are solutions `W_{n,j}(u,\xi)` , `j=1,2` , that are `C^{\infty}` on `(0,\alpha_{2})` , and as `u\to\infty`
- Here `A_{0}(\xi)=1` ,
- `s=0,1,2,\dots` . For `I_{\nu}` and `K_{\nu}` see  10.25(ii) . The expansions ( 2.8.25 ) and ( 2.8.26 ) are both uniform and differentiable with respect to `\xi` . These results are valid when `\mathcal{V}_{0,\alpha_{2}}\left(\xi^{1/2}B_{0}\right)` and `\mathcal{V}_{0,\alpha_{2}}\left(\xi^{1/2}B_{n-1}\right)` are finite.
- If `\xi\in(\alpha_{1},0)` , then there are solutions `W_{n,j}(u,\xi)` , `j=3,4` , that are `C^{\infty}` on `(\alpha_{1},0)` , and as `u\to\infty`

Formula blocks:
- Formula block (2.8.24)

```tex
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}=\left(\frac{u^{2}}{4\xi}+\frac{% \nu^{2}-1}{4\xi^{2}}+\frac{\psi(\xi)}{\xi}\right)W.
```

- Formula block (2.8.25)

```tex
\displaystyle W_{n,1}(u,\xi)
```

- Formula block (2.8.26)

```tex
\displaystyle W_{n,2}(u,\xi)
```

- Formula block (2.8.27)

```tex
B_{s}(\xi)=-A_{s}^{\prime}(\xi)+\frac{1}{\xi^{1/2}}\int_{0}^{\xi}\left(\psi(v)% A_{s}(v)-\left(\nu+\tfrac{1}{2}\right)A_{s}^{\prime}(v)\right)\frac{\,\mathrm{% d}v}{v^{1/2}},
```

- Formula block (2.8.28)

```tex
A_{s+1}(\xi)=\nu B_{s}(\xi)-\xi B_{s}^{\prime}(\xi)+\int\psi(\xi)B_{s}(\xi)\,% \mathrm{d}\xi,
```

- Formula block (2.8.29)

```tex
W_{n,3}(u,\xi)=|\xi|^{1/2}J_{\nu}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-% 1}\frac{A_{s}(\xi)}{u^{2s}}+O\left(\frac{1}{u^{2n-1}}\right)\right)-|\xi|J_{% \nu+1}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-2}\frac{B_{s}(\xi)}{u^{2s+1% }}+O\left(\frac{1}{u^{2n-2}}\right)\right),
```

- Formula block (2.8.30)

```tex
W_{n,4}(u,\xi)=|\xi|^{1/2}Y_{\nu}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-% 1}\frac{A_{s}(\xi)}{u^{2s}}+O\left(\frac{1}{u^{2n-1}}\right)\right)-|\xi|Y_{% \nu+1}\left(u|\xi|^{1/2}\right)\left(\sum_{s=0}^{n-2}\frac{B_{s}(\xi)}{u^{2s+1% }}+O\left(\frac{1}{u^{2n-2}}\right)\right).
```

- Formula block (2.8.31)

```tex
B_{s}(\xi)=-A_{s}^{\prime}(\xi)+\frac{1}{|\xi|^{1/2}}\int_{\xi}^{0}\left(\psi(% v)A_{s}(v)-\left(\nu+\tfrac{1}{2}\right)A_{s}^{\prime}(v)\right)\frac{\,% \mathrm{d}v}{|v|^{1/2}},
```

- Formula block (2.8.32)

```tex
J_{\nu}(x)+Y_{\nu}(x)=0.
```

- Formula block

```tex
\displaystyle\operatorname{env}\mskip-2.0muJ_{\nu}(x)
```

- Formula block

```tex
\displaystyle\operatorname{env}\mskip-2.0muY_{\nu}(x)
```

- Formula block (2.8.34)

```tex
\operatorname{env}\mskip-2.0muJ_{\nu}(x)=\operatorname{env}\mskip-2.0muY_{\nu}% (x)=\left({J_{\nu}}^{2}(x)+{Y_{\nu}}^{2}(x)\right)^{1/2},
```

- Formula block (2.8.35)

```tex
W_{n,3}(u,\xi)=|\xi|^{1/2}J_{\nu}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n-1}% \frac{A_{s}(\xi)}{u^{2s}}-|\xi|J_{\nu+1}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n% -2}\frac{B_{s}(\xi)}{u^{2s+1}}+|\xi|^{1/2}\operatorname{env}\mskip-2.0muJ_{\nu% }\left(u|\xi|^{1/2}\right)O\left(\frac{1}{u^{2n-1}}\right),
```

- Formula block (2.8.36)

```tex
W_{n,4}(u,\xi)=|\xi|^{1/2}Y_{\nu}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n-1}% \frac{A_{s}(\xi)}{u^{2s}}-|\xi|Y_{\nu+1}\left(u|\xi|^{1/2}\right)\sum_{s=0}^{n% -2}\frac{B_{s}(\xi)}{u^{2s+1}}+|\xi|^{1/2}\operatorname{env}\mskip-2.0muY_{\nu% }\left(u|\xi|^{1/2}\right)O\left(\frac{1}{u^{2n-1}}\right),
```


Local metadata:
- Defines: `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` and `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)`
- Keywords: Bessel functions , asymptotic solutions of differential equations , envelope functions , in terms of Bessel functions of fixed order , with a parameter
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `u` : large real or complex parameter and `\psi(\xi)` : function
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `I_{\NVar{\nu}}\left(\NVar{z}\right)` : modified Bessel function of the first kind , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `K_{\NVar{\nu}}\left(\NVar{z}\right)` : modified Bessel function of the second kind , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\nu` : real nonnegative constant , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\nu` : real nonnegative constant , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `O\left(\NVar{x}\right)` : order not exceeding , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\nu` : real nonnegative constant , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `\psi(\xi)` : function
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind and `\nu` : real nonnegative constant
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` , `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)` , `\nu` : real nonnegative constant and `X_{\nu}` : smallest positive root
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` , `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)` , `\nu` : real nonnegative constant and `X_{\nu}` : smallest positive root
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{env}\mskip-2.0muJ_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `J_{\NVar{\nu}}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter
- Symbols: `Y_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the second kind , `O\left(\NVar{x}\right)` : order not exceeding , `\operatorname{env}\mskip-2.0muY_{\NVar{\nu}}\left(\NVar{x}\right)` : envelope of Bessel function `Y_{\NVar{\nu}}\left(\NVar{x}\right)` , `W_{n,j}(u,\xi)` : solution , `\nu` : real nonnegative constant , `n` : positive integer , `A_{s}(\xi)` : coefficients , `B_{s}(\xi)` : coefficients and `u` : large real or complex parameter

### 2.8(v) Multiple and Fractional Turning Points

- The approach used in preceding subsections for equation ( 2.8.1 ) also succeeds when `z_{0}` is a multiple or fractional turning point . For the former `f(z)` has a zero of multiplicity `\lambda=2,3,4,\dots` and `g(z)` is analytic. For the latter `(z-z_{0})^{-\lambda}f(z)` and `g(z)` are both analytic at `z_{0}` , `\lambda` ( `>-2` ) being a real constant. In both cases uniform asymptotic approximations are obtained in terms of Bessel functions of order `1/(\lambda+2)` . More generally, `g(z)` can have a simple or double pole at `z_{0}` . (In the case of the double pole the order of the approximating Bessel functions is fixed but no longer `1/(\lambda+2)` .) However, in all cases with `\lambda>-2` and `\lambda\neq 0` or `\pm 1` , only uniform asymptotic approximations are available, not uniform asymptotic expansions. For results, including error bounds, see Olver ( 1977c ) .
- For connection formulas for Liouville-Green approximations across these transition points see Olver ( 1977b , a , 1978 ) .

Local metadata:
- Keywords: asymptotic solutions of differential equations , connection formulas across transition points , fractional or multiple , turning points , with a parameter

### 2.8(vi) Coalescing Transition Points

- Corresponding to the problems for integrals outlined in  2.3(v) , 2.4(v) , and 2.4(vi) , there are analogous problems for differential equations.
- For two coalescing turning points see Olver ( 1975a , 1976 ) and Dunster ( 1996a ) ; in this case the uniform approximants are parabolic cylinder functions. (For envelope functions for parabolic cylinder functions see  14.15(v) ).
- For a coalescing turning point and double pole see Boyd and Dunster ( 1986 ) and Dunster ( 1990b ) ; in this case the uniform approximants are Bessel functions of variable order.
- For a coalescing turning point and simple pole see Nestor ( 1984 ) and Dunster ( 1994b ) ; in this case the uniform approximants are Whittaker functions ( 13.14(i) ) with a fixed value of the second parameter.
- For further examples of uniform asymptotic approximations in terms of parabolic cylinder functions see  13.20(iii) , 13.20(iv) , 14.15(v) , 15.12(iii) , 18.24 .
- For further examples of uniform asymptotic approximations in terms of Bessel functions or modified Bessel functions of variable order see  13.21(ii) , 14.15(ii) , 14.15(iv) , 14.20(viii) , 30.9(i) , 30.9(ii) .

Local metadata:
- Keywords: asymptotic solutions of differential equations , coalescing transition points , in terms of Bessel functions of variable order , with a parameter
