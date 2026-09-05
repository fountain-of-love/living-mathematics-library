# §2.7 Differential Equations

Source: [https://dlmf.nist.gov/2.7](https://dlmf.nist.gov/2.7)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.7. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Regular Singularities: Fuchs-Frobenius Theory
- Irregular Singularities of Rank 1
- Liouville-Green (WKBJ) Approximation
- Numerically Satisfactory Solutions

## Source Notes

- See Olver ( 1997b , pp. 148-152) .
- See Olver ( 1997b , pp. 229-236) , Olver ( 1994a ) , Olde Daalhuis and Olver ( 1994 ) , and Olde Daalhuis ( 1998a ) .
- See Olver ( 1997b , pp. 190-200) .
- See Olver ( 1997b , pp. 154-155) .

## Keywords

Fuchs-Frobenius theory, classification of singularities, differential equations, indices differing by an integer, indicial equation, ordinary point, regular singularity, Fabry's transformation, Stokes multipliers, asymptotic solutions of differential equations, characteristic equation, coincident characteristic values, irregular singularities of rank 1, irregular singularity, rank of singularity, resurgence, Liouville-Green (or WKBJ) approximations, Liouville-Green (or WKBJ) approximation, Liouville-Green approximation theorem, dominant solutions, error-control function, recessive solutions, numerically satisfactory solutions

## Principal Formula Blocks

- Formula block (2.7.1)

```tex
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}+f(z)\frac{\mathrm{d}w}{\mathrm{d}z% }+g(z)w=0
```

- Formula block

```tex
\displaystyle f(z)
```

- Formula block

```tex
\displaystyle g(z)
```

- Formula block (2.7.3)

```tex
Q(\alpha)\equiv\alpha(\alpha-1)+f_{0}\alpha+g_{0}=0.
```

- Formula block (2.7.4)

```tex
w_{j}(z)=(z-z_{0})^{\alpha_{j}}\sum_{s=0}^{\infty}a_{s,j}(z-z_{0})^{s},
```

- Formula block (2.7.5)

```tex
Q(\alpha_{j}+s)a_{s,j}=-\sum_{r=0}^{s-1}\left((\alpha_{j}+r)f_{s-r}+g_{s-r}% \right)a_{r,j},
```

- Formula block (2.7.6)

```tex
w_{2}(z)=(z-z_{0})^{\alpha_{2}}\sum_{\begin{subarray}{c}s=0\\ s\neq\alpha_{1}-\alpha_{2}\end{subarray}}^{\infty}b_{s}(z-z_{0})^{s}+cw_{1}(z)% \ln\left(z-z_{0}\right),
```

- Formula block (2.7.8)

```tex
e^{\lambda_{j}z}z^{\mu_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{z^{s}},
```

- Formula block (2.7.9)

```tex
\lambda^{2}+f_{0}\lambda+g_{0}=0,
```

- Formula block (2.7.10)

```tex
\mu_{j}=-(f_{1}\lambda_{j}+g_{1})/(f_{0}+2\lambda_{j}),
```

- Formula block (2.7.11)

```tex
(f_{0}+2\lambda_{j})sa_{s,j}=(s-\mu_{j})(s-1-\mu_{j})a_{s-1,j}+\sum_{r=1}^{s}% \left(\lambda_{j}f_{r+1}+g_{r+1}-(s-r-\mu_{j})f_{r}\right)a_{s-r,j},
```

- Formula block (2.7.12)

```tex
\displaystyle a_{s,1}
```

- Formula block (2.7.13)

```tex
\displaystyle a_{s,2}
```

- Formula block (2.7.14)

```tex
w_{j}(z)\sim e^{\lambda_{j}z}((\lambda_{2}-\lambda_{1})z)^{\mu_{j}}\sum_{s=0}^% {\infty}\frac{a_{s,j}}{z^{s}}
```

- Formula block (2.7.15)

```tex
-\tfrac{3}{2}\pi+\delta\leq\operatorname{ph}\left((\lambda_{2}-\lambda_{1})z% \right)\leq\tfrac{3}{2}\pi-\delta,
```

- Formula block (2.7.16)

```tex
-\tfrac{1}{2}\pi+\delta\leq\operatorname{ph}\left((\lambda_{2}-\lambda_{1})z% \right)\leq\tfrac{5}{2}\pi-\delta,
```

- Formula block

```tex
\displaystyle w_{1}(z)
```

- Formula block

```tex
\displaystyle w_{2}(z)
```

- Formula block

```tex
\displaystyle\Lambda_{1}
```

- Formula block

```tex
\displaystyle\Lambda_{2}
```

- Formula block

```tex
\displaystyle w
```

- Formula block

```tex
\displaystyle t
```

- Formula block (2.7.20)

```tex
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}x}^{2}}=(f(x)+g(x))w
```

- Formula block (2.7.21)

```tex
\displaystyle w_{1}(x)
```

- Formula block (2.7.22)

```tex
\displaystyle w_{2}(x)
```

- Formula block (2.7.23)

```tex
|\epsilon_{j}(x)|,\;\;\tfrac{1}{2}f^{-1/2}(x)|\epsilon_{j}^{\prime}(x)|\leq% \exp\left(\tfrac{1}{2}\mathcal{V}_{a_{j},x}\left(F\right)\right)-1,
```

- Formula block (2.7.24)

```tex
F(x)=\int\left(\frac{1}{f^{1/4}}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}}% \left(\frac{1}{f^{1/4}}\right)-\frac{g}{f^{1/2}}\right)\,\mathrm{d}x,
```

- Formula block (2.7.25)

```tex
\mathcal{V}_{a_{j},x}\left(F\right)=\left|\int_{a_{j}}^{x}\left|\frac{1}{f^{1/% 4}(t)}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}t}^{2}}\left(\frac{1}{f^{1/4}(t)}% \right)-\frac{g(t)}{f^{1/2}(t)}\right|\,\mathrm{d}t\right|.
```

- Formula block (2.7.26)

```tex
w_{1}(x)\sim f^{-1/4}(x)\exp\left(\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.27)

```tex
w_{2}(x)\sim f^{-1/4}(x)\exp\left(-\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.28)

```tex
w_{3}(x)\sim f^{-1/4}(x)\exp\left(\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.29)

```tex
w_{4}(x)\sim f^{-1/4}(x)\exp\left(-\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.30)

```tex
w_{1}(x)/w_{4}(x)\to 0,
```

- Formula block (2.7.31)

```tex
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}x}^{2}}=(x+\ln x)w,
```

- Formula block (2.7.32)

```tex
f^{1/2}=x^{1/2}+\tfrac{1}{2}x^{-1/2}\ln x+O\left(x^{-3/2}(\ln x)^{2}\right),
```

- Formula block (2.7.33)

```tex
\displaystyle w_{2}(x)
```

- Formula block (2.7.34)

```tex
\displaystyle w_{3}(x)
```

- Formula block (2.7.35)

```tex
\ifrac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}=w
```

- Formula block (2.7.36)

```tex
w(z)=Aw_{1}(z)+Bw_{2}(z),
```

- Formula block (2.7.37)

```tex
w(z)=Cw_{3}(z)+Dw_{4}(z),
```


## Definitions and Symbols

- Keywords: Fuchs-Frobenius theory , classification of singularities , differential equations , indices differing by an integer , indicial equation , ordinary point , regular singularity
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `w` : DE solution , `f(z)` : analytic function and `g(z)` : analytic function
- Symbols: `f(z)` : analytic function , `g(z)` : analytic function , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\equiv` : equals by definition , `f_{s}` : coefficients , `g_{s}` : coefficients and `Q(\alpha)` : indicial function
- Symbols: `\in` : element of , `\mathbf{N}` : punctured neighborhood , `w_{j}(z)` : solutions and `a_{n}` : coefficients
- Symbols: `f_{s}` : coefficients , `g_{s}` : coefficients , `Q(\alpha)` : indicial function and `a_{n}` : coefficients
- Symbols: `\in` : element of , `\ln\NVar{z}` : principal branch of logarithm function , `b_{s}` : coefficients , `c` : constant , `\mathbf{N}` : punctured neighborhood and `w_{j}(z)` : solutions
- Keywords: Fabry's transformation , Stokes multipliers , asymptotic solutions of differential equations , characteristic equation , coincident characteristic values , differential equations , irregular singularities of rank 1 , irregular singularity , rank of singularity , resurgence
- Symbols: `f(z)` : analytic function , `g(z)` : analytic function , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `a_{s,j}` : coefficients , `\lambda_{j}` : roots and `\mu_{j}` : quantities
- Symbols: `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\lambda_{j}` : roots , `\mu_{j}` : quantities , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `\Lambda_{j}` : constants
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `\Lambda_{j}` : constants
- Symbols: `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `w_{j}(z)` : solutions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{ph}` : phase , `\lambda_{j}` : roots and `\delta` : arbitrary small positive constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{ph}` : phase , `\lambda_{j}` : roots and `\delta` : arbitrary small positive constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\mu_{j}` : quantities , `C_{1}` , `C_{2}` : Stokes multipliers and `w_{j}(z)` : solutions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\mu_{j}` : quantities , `\Lambda_{j}` : constants and `C_{1}` , `C_{2}` : Stokes multipliers
- Symbols: `\mathrm{e}` : base of natural logarithm , `w` : DE solution and `f_{s}` : coefficients
- Keywords: Liouville-Green (or WKBJ) approximations , Liouville-Green (or WKBJ) approximation , Liouville-Green approximation theorem , asymptotic solutions of differential equations
- Keywords: asymptotic solutions of differential equations , differential equations , dominant solutions , error-control function , error-control function , recessive solutions
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` and `w` : DE solution
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `\epsilon_{j}(x)` : function and `w_{j}(z)` : solutions
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `\epsilon_{j}(x)` : function and `w_{j}(z)` : solutions
- Symbols: `\exp\NVar{z}` : exponential function , `\mathcal{V}_{\NVar{a,b}}\left(\NVar{f}\right)` : total variation , `(a_{1},a_{2})` : interval , `\epsilon_{j}(x)` : function and `F` : error-control function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `F` : error-control function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mathcal{V}_{\NVar{a,b}}\left(\NVar{f}\right)` : total variation , `(a_{1},a_{2})` : interval and `F` : error-control function
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Keywords: Liouville-Green (or WKBJ) approximations , Liouville-Green (or WKBJ) approximation , asymptotic solutions of differential equations
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\ln\NVar{z}` : principal branch of logarithm function and `w` : DE solution
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding and `\ln\NVar{z}` : principal branch of logarithm function
- Symbols: `\sim` : asymptotic equality , `\exp\NVar{z}` : exponential function and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\exp\NVar{z}` : exponential function and `w_{j}(z)` : solutions
- Keywords: asymptotic solutions of differential equations , differential equations , numerically satisfactory solutions
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` and `w` : DE solution
- Symbols: `w` : DE solution , `A` : constant , `B` : constant and `w_{j}(z)` : solutions
- Symbols: `w` : DE solution , `C` : constant , `D` : constant and `w_{j}(z)` : solutions

## Subsections

### 2.7(i) Regular Singularities: Fuchs-Frobenius Theory

- An ordinary point of the differential equation
- is one at which the coefficients `f(z)` and `g(z)` are analytic. All solutions are analytic at an ordinary point, and their Taylor-series expansions are found by equating coefficients.
- Other points `z_{0}` are singularities of the differential equation. If both `(z-z_{0})f(z)` and `(z-z_{0})^{2}g(z)` are analytic at `z_{0}` , then `z_{0}` is a regular singularity (or singularity of the first kind ). All other singularities are classified as irregular .
- In a punctured neighborhood `\mathbf{N}` of a regular singularity `z_{0}`
- with at least one of the coefficients `f_{0}` , `g_{0}` , `g_{1}` nonzero. Let `\alpha_{1}` , `\alpha_{2}` denote the indices or exponents , that is, the roots of the indicial equation
- Provided that `\alpha_{1}-\alpha_{2}` is not zero or an integer, equation ( 2.7.1 ) has independent solutions `w_{j}(z)` , `j=1,2` , such that

Formula blocks:
- Formula block (2.7.1)

```tex
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}+f(z)\frac{\mathrm{d}w}{\mathrm{d}z% }+g(z)w=0
```

- Formula block

```tex
\displaystyle f(z)
```

- Formula block

```tex
\displaystyle g(z)
```

- Formula block (2.7.3)

```tex
Q(\alpha)\equiv\alpha(\alpha-1)+f_{0}\alpha+g_{0}=0.
```

- Formula block (2.7.4)

```tex
w_{j}(z)=(z-z_{0})^{\alpha_{j}}\sum_{s=0}^{\infty}a_{s,j}(z-z_{0})^{s},
```

- Formula block (2.7.5)

```tex
Q(\alpha_{j}+s)a_{s,j}=-\sum_{r=0}^{s-1}\left((\alpha_{j}+r)f_{s-r}+g_{s-r}% \right)a_{r,j},
```

- Formula block (2.7.6)

```tex
w_{2}(z)=(z-z_{0})^{\alpha_{2}}\sum_{\begin{subarray}{c}s=0\\ s\neq\alpha_{1}-\alpha_{2}\end{subarray}}^{\infty}b_{s}(z-z_{0})^{s}+cw_{1}(z)% \ln\left(z-z_{0}\right),
```


Local metadata:
- Keywords: Fuchs-Frobenius theory , classification of singularities , differential equations , indices differing by an integer , indicial equation , ordinary point , regular singularity
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `w` : DE solution , `f(z)` : analytic function and `g(z)` : analytic function
- Symbols: `f(z)` : analytic function , `g(z)` : analytic function , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\equiv` : equals by definition , `f_{s}` : coefficients , `g_{s}` : coefficients and `Q(\alpha)` : indicial function
- Symbols: `\in` : element of , `\mathbf{N}` : punctured neighborhood , `w_{j}(z)` : solutions and `a_{n}` : coefficients
- Symbols: `f_{s}` : coefficients , `g_{s}` : coefficients , `Q(\alpha)` : indicial function and `a_{n}` : coefficients
- Symbols: `\in` : element of , `\ln\NVar{z}` : principal branch of logarithm function , `b_{s}` : coefficients , `c` : constant , `\mathbf{N}` : punctured neighborhood and `w_{j}(z)` : solutions

### 2.7(ii) Irregular Singularities of Rank 1

- If the singularities of `f(z)` and `g(z)` at `z_{0}` are no worse than poles, then `z_{0}` has rank `\ell-1` , where `\ell` is the least integer such that `(z-z_{0})^{\ell}f(z)` and `(z-z_{0})^{2\ell}g(z)` are analytic at `z_{0}` . Thus a regular singularity has rank 0. The most common type of irregular singularity for special functions has rank 1 and is located at infinity. Then
- these series converging in an annulus `|z|>a` , with at least one of `f_{0}` , `g_{0}` , `g_{1}` nonzero.
- Formal solutions are
- where `\lambda_{1}` , `\lambda_{2}` are the roots of the characteristic equation
- `a_{0,j}=1` , and
- when `s=1,2,\dots` . The construction fails iff `\lambda_{1}=\lambda_{2}` , that is, when `f_{0}^{2}=4g_{0}` : this case is treated below.

Formula blocks:
- Formula block

```tex
\displaystyle f(z)
```

- Formula block

```tex
\displaystyle g(z)
```

- Formula block (2.7.8)

```tex
e^{\lambda_{j}z}z^{\mu_{j}}\sum_{s=0}^{\infty}\frac{a_{s,j}}{z^{s}},
```

- Formula block (2.7.9)

```tex
\lambda^{2}+f_{0}\lambda+g_{0}=0,
```

- Formula block (2.7.10)

```tex
\mu_{j}=-(f_{1}\lambda_{j}+g_{1})/(f_{0}+2\lambda_{j}),
```

- Formula block (2.7.11)

```tex
(f_{0}+2\lambda_{j})sa_{s,j}=(s-\mu_{j})(s-1-\mu_{j})a_{s-1,j}+\sum_{r=1}^{s}% \left(\lambda_{j}f_{r+1}+g_{r+1}-(s-r-\mu_{j})f_{r}\right)a_{s-r,j},
```

- Formula block (2.7.12)

```tex
\displaystyle a_{s,1}
```

- Formula block (2.7.13)

```tex
\displaystyle a_{s,2}
```

- Formula block (2.7.14)

```tex
w_{j}(z)\sim e^{\lambda_{j}z}((\lambda_{2}-\lambda_{1})z)^{\mu_{j}}\sum_{s=0}^% {\infty}\frac{a_{s,j}}{z^{s}}
```

- Formula block (2.7.15)

```tex
-\tfrac{3}{2}\pi+\delta\leq\operatorname{ph}\left((\lambda_{2}-\lambda_{1})z% \right)\leq\tfrac{3}{2}\pi-\delta,
```

- Formula block (2.7.16)

```tex
-\tfrac{1}{2}\pi+\delta\leq\operatorname{ph}\left((\lambda_{2}-\lambda_{1})z% \right)\leq\tfrac{5}{2}\pi-\delta,
```

- Formula block

```tex
\displaystyle w_{1}(z)
```

- Formula block

```tex
\displaystyle w_{2}(z)
```

- Formula block

```tex
\displaystyle\Lambda_{1}
```

- Formula block

```tex
\displaystyle\Lambda_{2}
```

- Formula block

```tex
\displaystyle w
```

- Formula block

```tex
\displaystyle t
```


Local metadata:
- Keywords: Fabry's transformation , Stokes multipliers , asymptotic solutions of differential equations , characteristic equation , coincident characteristic values , differential equations , irregular singularities of rank 1 , irregular singularity , rank of singularity , resurgence
- Symbols: `f(z)` : analytic function , `g(z)` : analytic function , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `a_{s,j}` : coefficients , `\lambda_{j}` : roots and `\mu_{j}` : quantities
- Symbols: `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\lambda_{j}` : roots , `\mu_{j}` : quantities , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities , `f_{s}` : coefficients and `g_{s}` : coefficients
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `\Lambda_{j}` : constants
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `\Lambda_{j}` : constants
- Symbols: `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `w_{j}(z)` : solutions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{ph}` : phase , `\lambda_{j}` : roots and `\delta` : arbitrary small positive constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{ph}` : phase , `\lambda_{j}` : roots and `\delta` : arbitrary small positive constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\mu_{j}` : quantities , `C_{1}` , `C_{2}` : Stokes multipliers and `w_{j}(z)` : solutions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\mu_{j}` : quantities , `\Lambda_{j}` : constants and `C_{1}` , `C_{2}` : Stokes multipliers
- Symbols: `\mathrm{e}` : base of natural logarithm , `w` : DE solution and `f_{s}` : coefficients

### 2.7(iii) Liouville-Green (WKBJ) Approximation

- For irregular singularities of nonclassifiable rank, a powerful tool for finding the asymptotic behavior of solutions, complete with error bounds, is as follows:

Formula blocks:
- Formula block (2.7.20)

```tex
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}x}^{2}}=(f(x)+g(x))w
```

- Formula block (2.7.21)

```tex
\displaystyle w_{1}(x)
```

- Formula block (2.7.22)

```tex
\displaystyle w_{2}(x)
```

- Formula block (2.7.23)

```tex
|\epsilon_{j}(x)|,\;\;\tfrac{1}{2}f^{-1/2}(x)|\epsilon_{j}^{\prime}(x)|\leq% \exp\left(\tfrac{1}{2}\mathcal{V}_{a_{j},x}\left(F\right)\right)-1,
```

- Formula block (2.7.24)

```tex
F(x)=\int\left(\frac{1}{f^{1/4}}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}}% \left(\frac{1}{f^{1/4}}\right)-\frac{g}{f^{1/2}}\right)\,\mathrm{d}x,
```

- Formula block (2.7.25)

```tex
\mathcal{V}_{a_{j},x}\left(F\right)=\left|\int_{a_{j}}^{x}\left|\frac{1}{f^{1/% 4}(t)}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}t}^{2}}\left(\frac{1}{f^{1/4}(t)}% \right)-\frac{g(t)}{f^{1/2}(t)}\right|\,\mathrm{d}t\right|.
```

- Formula block (2.7.26)

```tex
w_{1}(x)\sim f^{-1/4}(x)\exp\left(\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.27)

```tex
w_{2}(x)\sim f^{-1/4}(x)\exp\left(-\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.28)

```tex
w_{3}(x)\sim f^{-1/4}(x)\exp\left(\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.29)

```tex
w_{4}(x)\sim f^{-1/4}(x)\exp\left(-\int f^{1/2}(x)\,\mathrm{d}x\right),
```

- Formula block (2.7.30)

```tex
w_{1}(x)/w_{4}(x)\to 0,
```

- Formula block (2.7.31)

```tex
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}x}^{2}}=(x+\ln x)w,
```

- Formula block (2.7.32)

```tex
f^{1/2}=x^{1/2}+\tfrac{1}{2}x^{-1/2}\ln x+O\left(x^{-3/2}(\ln x)^{2}\right),
```

- Formula block (2.7.33)

```tex
\displaystyle w_{2}(x)
```

- Formula block (2.7.34)

```tex
\displaystyle w_{3}(x)
```


Local metadata:
- Keywords: Liouville-Green (or WKBJ) approximations , Liouville-Green (or WKBJ) approximation , Liouville-Green approximation theorem , asymptotic solutions of differential equations
- Keywords: asymptotic solutions of differential equations , differential equations , dominant solutions , error-control function , error-control function , recessive solutions
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` and `w` : DE solution
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `\epsilon_{j}(x)` : function and `w_{j}(z)` : solutions
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `\epsilon_{j}(x)` : function and `w_{j}(z)` : solutions
- Symbols: `\exp\NVar{z}` : exponential function , `\mathcal{V}_{\NVar{a,b}}\left(\NVar{f}\right)` : total variation , `(a_{1},a_{2})` : interval , `\epsilon_{j}(x)` : function and `F` : error-control function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `F` : error-control function
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mathcal{V}_{\NVar{a,b}}\left(\NVar{f}\right)` : total variation , `(a_{1},a_{2})` : interval and `F` : error-control function
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral , `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Symbols: `(a_{1},a_{2})` : interval and `w_{j}(z)` : solutions
- Keywords: Liouville-Green (or WKBJ) approximations , Liouville-Green (or WKBJ) approximation , asymptotic solutions of differential equations
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\ln\NVar{z}` : principal branch of logarithm function and `w` : DE solution
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding and `\ln\NVar{z}` : principal branch of logarithm function
- Symbols: `\sim` : asymptotic equality , `\exp\NVar{z}` : exponential function and `w_{j}(z)` : solutions
- Symbols: `\sim` : asymptotic equality , `\exp\NVar{z}` : exponential function and `w_{j}(z)` : solutions

### 2.7(iv) Numerically Satisfactory Solutions

- One pair of independent solutions of the equation
- is `w_{1}(z)=e^{z}` , `w_{2}(z)=e^{-z}` . Another is `w_{3}(z)=\cosh z` , `w_{4}(z)=\sinh z` . In theory either pair may be used to construct any other solution
- or
- where `A,B,C,D` are constants. From the numerical standpoint, however, the pair `w_{3}(z)` and `w_{4}(z)` has the drawback that severe numerical cancellation can occur with certain combinations of `C` and `D` , for example if `C` and `D` are equal, or nearly equal, and `z` , or `\Re z` , is large and negative. This kind of cancellation cannot take place with `w_{1}(z)` and `w_{2}(z)` , and for this reason, and following Miller ( 1950 ) , we call `w_{1}(z)` and `w_{2}(z)` a numerically satisfactory pair of solutions.
- The solutions `w_{1}(z)` and `w_{2}(z)` are respectively recessive and dominant as `\Re z\to-\infty` , and vice versa as `\Re z\to+\infty` . This is characteristic of numerically satisfactory pairs. In a neighborhood, or sectorial neighborhood of a singularity, one member has to be recessive. In consequence, if a differential equation has more than one singularity in the extended plane, then usually more than two standard solutions need to be chosen in order to have numerically satisfactory representations everywhere.
- In oscillatory intervals, and again following Miller ( 1950 ) , we call a pair of solutions numerically satisfactory if asymptotically they have the same amplitude and are `\tfrac{1}{2}\pi` out of phase.

Formula blocks:
- Formula block (2.7.35)

```tex
\ifrac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}=w
```

- Formula block (2.7.36)

```tex
w(z)=Aw_{1}(z)+Bw_{2}(z),
```

- Formula block (2.7.37)

```tex
w(z)=Cw_{3}(z)+Dw_{4}(z),
```


Local metadata:
- Keywords: asymptotic solutions of differential equations , differential equations , numerically satisfactory solutions
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` and `w` : DE solution
- Symbols: `w` : DE solution , `A` : constant , `B` : constant and `w_{j}(z)` : solutions
- Symbols: `w` : DE solution , `C` : constant , `D` : constant and `w_{j}(z)` : solutions
