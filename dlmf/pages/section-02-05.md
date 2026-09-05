# §2.5 Mellin Transform Methods

Source: [https://dlmf.nist.gov/2.5](https://dlmf.nist.gov/2.5)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.5. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Introduction
- Extensions
- Laplace Transforms with Small Parameters

## Source Notes

- See Wong ( 1989 , pp. 147-153, 155-157) and Doetsch ( 1955 , 6.5) .
- See Wong ( 1989 , pp. 157-162) .
- See Wong ( 1989 , pp. 167-171) .

## Keywords

Mellin transform methods, asymptotic approximations of integrals, Mellin transform, Parseval-type formulas, analytic properties, convolution integrals, definition, inversion, locally integrable, extensions, multidimensional integrals, Laplace transform, asymptotic expansions for small parameters, exponential integrals, small argument

## Principal Formula Blocks

- Formula block (2.5.1)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\int_{0}^{\infty}t^{z-1}f(t% )\,\mathrm{d}t,
```

- Formula block (2.5.2)

```tex
f(t)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}t^{-z}\mathscr{M}\mskip-3.0% muf\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.3)

```tex
I(x)=\int_{0}^{\infty}f(t)\,h(xt)\,\mathrm{d}t,
```

- Formula block (2.5.4)

```tex
\mathscr{M}\mskip-3.0muI\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muf% \mskip 3.0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right).
```

- Formula block (2.5.5)

```tex
I(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}x^{-z}\mathscr{M}\mskip-3.0% muf\mskip 3.0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z% \right)\,\mathrm{d}z,
```

- Formula block (2.5.6)

```tex
I(x)=\sum\limits_{d<\Re z<c}\Residue\left[x^{-z}\mathscr{M}\mskip-3.0muf\mskip 3% .0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\right]+% E(x),
```

- Formula block (2.5.7)

```tex
E(x)=\frac{1}{2\pi i}\int_{d-i\infty}^{d+i\infty}x^{-z}\mathscr{M}\mskip-3.0% muf\mskip 3.0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z% \right)\,\mathrm{d}z.
```

- Formula block (2.5.8)

```tex
I(x)=\int_{0}^{\infty}\frac{{J_{\nu}}^{2}\left(xt\right)}{1+t}\,\mathrm{d}t,
```

- Formula block (2.5.9)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(1-z\right)=\frac{\pi}{\sin\left(\pi z% \right)},
```

- Formula block (2.5.10)

```tex
\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)=\frac{2^{z-1}\Gamma\left(% \nu+\frac{1}{2}z\right)}{{\Gamma}^{2}\left(1-\frac{1}{2}z\right)\Gamma\left(1+% \nu-\frac{1}{2}z\right)\Gamma\left(z\right)}\frac{\pi}{\sin\left(\pi z\right)},
```

- Formula block (2.5.11)

```tex
\Residue_{z=n}\left[x^{-z}\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(1-z\right)% \mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\right]=(a_{n}\ln x+b_{n})x^% {-n},
```

- Formula block (2.5.12)

```tex
\displaystyle a_{n}
```

- Formula block (2.5.13)

```tex
\displaystyle b_{n}
```

- Formula block (2.5.14)

```tex
|\Gamma\left(x+iy\right)|=\sqrt{2\pi}e^{-\pi|y|/2}|y|^{x-(1/2)}\left(1+o\left(% 1\right)\right),
```

- Formula block (2.5.15)

```tex
I(x)=-\sum_{s=0}^{2n}(a_{s}\ln x+b_{s})x^{-s}+O\left(x^{-2n-1+\epsilon}\right),
```

- Formula block (2.5.16)

```tex
I(x)=\sum_{s=0}^{n-1}(c_{s}\ln x+d_{s})x^{-2s-1}+O\left(x^{-2n-1+\epsilon}% \right),
```

- Formula block (2.5.17)

```tex
f(t)\sim\sum_{s=0}^{\infty}a_{s}t^{\alpha_{s}},
```

- Formula block (2.5.18)

```tex
h(t)\sim\exp\left(i\kappa t^{p}\right)\sum_{s=0}^{\infty}b_{s}t^{-\beta_{s}},
```

- Formula block (2.5.19)

```tex
f(t)=O\left(t^{-b}\right),
```

- Formula block (2.5.20)

```tex
h(t)=O\left(t^{c}\right),
```

- Formula block (2.5.21)

```tex
\displaystyle f_{1}(t)
```

- Formula block (2.5.22)

```tex
\displaystyle f_{2}(t)
```

- Formula block (2.5.23)

```tex
\displaystyle h_{1}(t)
```

- Formula block (2.5.24)

```tex
\displaystyle h_{2}(t)
```

- Formula block (2.5.25)

```tex
a_{s}/\left(z+\alpha_{s}\right).
```

- Formula block (2.5.26)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muf_{1% }\mskip 3.0mu\left(z\right)+\mathscr{M}\mskip-3.0muf_{2}\mskip 3.0mu\left(z\right)
```

- Formula block (2.5.27)

```tex
-b_{s}/\left(z-\beta_{s}\right).
```

- Formula block (2.5.28)

```tex
\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muh_{1% }\mskip 3.0mu\left(z\right)+\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)
```

- Formula block (2.5.29)

```tex
I(x)=\sum\limits_{j,k=1}^{2}I_{jk}(x),
```

- Formula block (2.5.30)

```tex
I_{jk}(x)=\int_{0}^{\infty}f_{j}(t)h_{k}(xt)\,\mathrm{d}t.
```

- Formula block (2.5.31)

```tex
I_{21}(x)=0,
```

- Formula block (2.5.32)

```tex
G_{jk}(z)=\mathscr{M}\mskip-3.0muf_{j}\mskip 3.0mu\left(1-z\right)\mathscr{M}% \mskip-3.0muh_{k}\mskip 3.0mu\left(z\right).
```

- Formula block (2.5.33)

```tex
I_{jk}(x)=\frac{1}{2\pi i}\int_{p_{jk}-i\infty}^{p_{jk}+i\infty}x^{-z}G_{jk}(z% )\,\mathrm{d}z.
```

- Formula block (2.5.34)

```tex
\sup_{p_{jk}\leq x\leq q_{jk}}\left|G_{jk}(x+iy)\right|\to 0,
```

- Formula block (2.5.35)

```tex
I_{jk}(x)=\sum_{p_{jk}<\Re z<q_{jk}}\Residue\left[-x^{-z}G_{jk}(z)\right]+E_{% jk}(x),
```

- Formula block (2.5.36)

```tex
E_{jk}(x)=\frac{1}{2\pi i}\int_{q_{jk}-i\infty}^{q_{jk}+i\infty}x^{-z}G_{jk}(z% )\,\mathrm{d}z=o\left(x^{-q_{jk}}\right)
```

- Formula block (2.5.37)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=\int_{0}^{\infty}h(t)e^% {-\zeta t}\,\mathrm{d}t.
```

- Formula block (2.5.38)

```tex
\zeta\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=I_{1}(x)+I_{2}(x),
```

- Formula block (2.5.39)

```tex
I_{j}(x)=\int_{0}^{\infty}e^{-t}h_{j}(xt)\,\mathrm{d}t,
```

- Formula block (2.5.40)

```tex
I_{j}(x)=\frac{1}{2\pi i}\int_{p_{j}-i\infty}^{p_{j}+i\infty}x^{-z}\Gamma\left% (1-z\right)\mathscr{M}\mskip-3.0muh_{j}\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.41)

```tex
I_{1}(x)=\mathscr{M}\mskip-3.0muh_{1}\mskip 3.0mu\left(1\right)x^{-1}+\frac{1}% {2\pi i}\int_{\rho-i\infty}^{\rho+i\infty}x^{-z}\Gamma\left(1-z\right)\mathscr% {M}\mskip-3.0muh_{1}\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.42)

```tex
I_{2}(x)=\sum_{\Re\beta_{0}\leq\Re z\leq 1}\Residue\left[-x^{-z}\Gamma\left(1-% z\right)\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)\right]+\frac{1}% {2\pi i}\int_{\rho-i\infty}^{\rho+i\infty}x^{-z}\Gamma\left(1-z\right)\mathscr% {M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)\,\mathrm{d}z.
```

- Formula block (2.5.43)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=\mathscr{M}\mskip-3.0% muh_{1}\mskip 3.0mu\left(1\right)+\sum_{\Re\beta_{0}\leq\Re z\leq 1}\Residue% \left[-\zeta^{z-1}\Gamma\left(1-z\right)\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0% mu\left(z\right)\right]+\sum\limits_{1<\Re z<l}\Residue\left[-\zeta^{z-1}% \Gamma\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\right% ]+\frac{1}{2\pi i}\int_{l-\delta-i\infty}^{l-\delta+i\infty}\zeta^{z-1}\Gamma% \left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.44)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)\sim\sum_{n=0}^{\infty}b% _{n}\Gamma\left(1-\beta_{n}\right)\zeta^{\beta_{n}-1}+\sum\limits_{n=0}^{% \infty}\frac{(-\zeta)^{n}}{n!}\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(n+1% \right),
```

- Formula block (2.5.45)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=\int_{0}^{\infty}\frac{% e^{-\zeta t}}{1+t}\,\mathrm{d}t,
```

- Formula block (2.5.46)

```tex
\Residue_{z=k}\left[-\zeta^{z-1}\Gamma\left(1-z\right)\pi\csc\left(\pi z\right% )\right]=\left(-\ln\zeta+\psi\left(k\right)\right)\dfrac{\zeta^{k-1}}{(k-1)!},
```

- Formula block (2.5.47)

```tex
\Residue_{z=1}\left[-\zeta^{z-1}\Gamma\left(1-z\right)\mathscr{M}\mskip-3.0muh% _{2}\mskip 3.0mu\left(z\right)\right]=\left(-\ln\zeta-\gamma\right)-\mathscr{M% }\mskip-3.0muh_{1}\mskip 3.0mu\left(1\right),
```

- Formula block (2.5.48)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)\sim(-\ln\zeta)\sum_{k=0% }^{\infty}\frac{\zeta^{k}}{k!}+\sum_{k=0}^{\infty}\psi\left(k+1\right)\frac{% \zeta^{k}}{k!},
```

- Formula block (2.5.49)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=e^{\zeta}E_{1}\left(% \zeta\right);
```


## Definitions and Symbols

- Keywords: Mellin transform methods , asymptotic approximations of integrals
- Keywords: Mellin transform , Parseval-type formulas , analytic properties , convolution integrals , definition , inversion , locally integrable
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `f(x)` : locally integrable function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : locally integrable function and `c` : point
- Keywords: Mellin transform
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : locally integrable function , `I(x)` : convolution integral and `h(x)` : function
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function , `I(x)` : convolution integral and `h(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : locally integrable function , `c` : point , `I(x)` : convolution integral and `h(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\Re` : real part , `\Residue` : residue , `f(x)` : locally integrable function , `c` : point , `I(x)` : convolution integral , `h(x)` : function , `d` : point and `E(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : locally integrable function , `h(x)` : function , `d` : point and `E(x)` : function
- Keywords: Mellin transform
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `I(x)` : convolution integral
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\Re` : real part , `\sin\NVar{z}` : sine function and `f(t)=1/(1+t)` : function
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\Re` : real part , `\sin\NVar{z}` : sine function , `h(t)={J_{\nu}}^{2}\left(t\right)` : function and `f(t)=1/(1+t)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\ln\NVar{z}` : principal branch of logarithm function , `\Residue` : residue , `h(t)={J_{\nu}}^{2}\left(t\right)` : function , `a_{n}` : coefficients , `b_{n}` : coefficients and `f(t)=1/(1+t)` : function
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function and `a_{n}` : coefficients
- Symbols: `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `\ln\NVar{z}` : principal branch of logarithm function , `a_{n}` : coefficients and `b_{n}` : coefficients
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `o\left(\NVar{x}\right)` : order less than
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\ln\NVar{z}` : principal branch of logarithm function , `a_{n}` : coefficients , `b_{n}` : coefficients , `\epsilon` : parameter and `I(x)` : convolution integral
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\ln\NVar{z}` : principal branch of logarithm function , `\epsilon` : parameter , `c` : point , `I(x)` : convolution integral and `d` : point
- Keywords: Mellin transform methods , asymptotic approximations of integrals , extensions , multidimensional integrals
- Symbols: `\sim` : Poincar asymptotic expansion , `f(x)` : locally integrable function and `a_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\exp\NVar{z}` : exponential function , `\mathrm{i}` : imaginary unit , `h(x)` : locally integrable function , `\kappa` : real , `p` : positive and `b` : right endpoint
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : locally integrable function and `b` : right endpoint
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `h(x)` : locally integrable function and `c` : point
- Symbols: `f(x)` : locally integrable function and `f_{j}(t)` : truncated functions
- Symbols: `f(x)` : locally integrable function and `f_{j}(t)` : truncated functions
- Symbols: `h(x)` : locally integrable function
- Symbols: `h(x)` : locally integrable function
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\Re` : real part , `f(x)` : locally integrable function , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions , `b` : right endpoint and `c` : point
- Symbols: `a_{s}` : coefficients
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function and `f_{j}(t)` : truncated functions
- Keywords: Mellin transform
- Symbols: `b` : right endpoint
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function and `h(x)` : locally integrable function
- Symbols: `I(x)` : convolution integral
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions and `I(x)` : convolution integral
- Symbols: `I(x)` : convolution integral
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\Re` : real part , `f(x)` : locally integrable function , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions , `D_{jk}` : domain , `b` : right endpoint and `c` : point
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions and `G_{jk}(z)` : function
- Keywords: Mellin transform
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `G_{jk}(z)` : function , `p_{jk}` : real number and `I(x)` : convolution integral
- Symbols: `\mathrm{i}` : imaginary unit , `\sup` : least upper bound (supremum) , `G_{jk}(z)` : function , `p_{jk}` : real number and `q_{jk}>p_{jk}` : real number
- Symbols: `\Re` : real part , `\Residue` : residue , `G_{jk}(z)` : function , `p_{jk}` : real number , `q_{jk}>p_{jk}` : real number , `E_{jk}(x)` : function and `I(x)` : convolution integral
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `o\left(\NVar{x}\right)` : order less than , `G_{jk}(z)` : function , `q_{jk}>p_{jk}` : real number and `E_{jk}(x)` : function
- Keywords: Laplace transform , asymptotic expansions for small parameters
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral and `h(x)` : locally integrable function
- Keywords: Laplace transform
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `h(x)` : locally integrable function and `I_{j}(x)` : integral
- Keywords: Laplace transform
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `h(x)` : locally integrable function and `I_{j}(x)` : integral
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `h(x)` : locally integrable function , `I_{j}(x)` : integral and `p_{j}` : real numbers
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `h(x)` : locally integrable function , `I_{j}(x)` : integral and `\rho` : parameter
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `\Re` : real part , `\Residue` : residue , `h(x)` : locally integrable function , `I_{j}(x)` : integral and `\rho` : parameter
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `\Re` : real part , `\Residue` : residue , `h(x)` : locally integrable function and `\delta` : arbitrary small positive constant
- Keywords: Laplace transform , Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\sim` : Poincar asymptotic expansion , `!` : factorial (as in `n!` ) , `h(x)` : locally integrable function and `b` : right endpoint
- Keywords: Laplace transform , Mellin transform
- Keywords: Laplace transform , asymptotic expansions for small parameters , exponential integrals , small argument
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\Re` : real part and `h(x)` : locally integrable function
- Keywords: Laplace transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\csc\NVar{z}` : cosecant function , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function and `\Residue` : residue
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\gamma` : Euler's constant , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\ln\NVar{z}` : principal branch of logarithm function , `\Residue` : residue and `h(x)` : locally integrable function
- Keywords: Mellin transform
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\sim` : Poincar asymptotic expansion , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function and `h(x)` : locally integrable function
- Keywords: Laplace transform
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\mathrm{e}` : base of natural logarithm , `E_{1}\left(\NVar{z}\right)` : exponential integral and `h(x)` : locally integrable function
- Keywords: Laplace transform

## Subsections

### 2.5(i) Introduction

- Let `f(t)` be a locally integrable function on `(0,\infty)` , that is, `\int_{\rho}^{T}f(t)\,\mathrm{d}t` exists for all `\rho` and `T` satisfying `0<\rho<T<\infty` . The Mellin transform of `f(t)` is defined by
- when this integral converges. The domain of analyticity of `\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)` is usually an infinite strip `a<\Re z<b` parallel to the imaginary axis. The inversion formula is given by
- with `a<c<b` .
- One of the two convolution integrals associated with the Mellin transform is of the form
- and
- If `\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(1-z\right)` and `\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)` have a common strip of analyticity `a<\Re z<b` , then

Formula blocks:
- Formula block (2.5.1)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\int_{0}^{\infty}t^{z-1}f(t% )\,\mathrm{d}t,
```

- Formula block (2.5.2)

```tex
f(t)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}t^{-z}\mathscr{M}\mskip-3.0% muf\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.3)

```tex
I(x)=\int_{0}^{\infty}f(t)\,h(xt)\,\mathrm{d}t,
```

- Formula block (2.5.4)

```tex
\mathscr{M}\mskip-3.0muI\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muf% \mskip 3.0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right).
```

- Formula block (2.5.5)

```tex
I(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}x^{-z}\mathscr{M}\mskip-3.0% muf\mskip 3.0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z% \right)\,\mathrm{d}z,
```

- Formula block (2.5.6)

```tex
I(x)=\sum\limits_{d<\Re z<c}\Residue\left[x^{-z}\mathscr{M}\mskip-3.0muf\mskip 3% .0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\right]+% E(x),
```

- Formula block (2.5.7)

```tex
E(x)=\frac{1}{2\pi i}\int_{d-i\infty}^{d+i\infty}x^{-z}\mathscr{M}\mskip-3.0% muf\mskip 3.0mu\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z% \right)\,\mathrm{d}z.
```

- Formula block (2.5.8)

```tex
I(x)=\int_{0}^{\infty}\frac{{J_{\nu}}^{2}\left(xt\right)}{1+t}\,\mathrm{d}t,
```

- Formula block (2.5.9)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(1-z\right)=\frac{\pi}{\sin\left(\pi z% \right)},
```

- Formula block (2.5.10)

```tex
\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)=\frac{2^{z-1}\Gamma\left(% \nu+\frac{1}{2}z\right)}{{\Gamma}^{2}\left(1-\frac{1}{2}z\right)\Gamma\left(1+% \nu-\frac{1}{2}z\right)\Gamma\left(z\right)}\frac{\pi}{\sin\left(\pi z\right)},
```

- Formula block (2.5.11)

```tex
\Residue_{z=n}\left[x^{-z}\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(1-z\right)% \mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\right]=(a_{n}\ln x+b_{n})x^% {-n},
```

- Formula block (2.5.12)

```tex
\displaystyle a_{n}
```

- Formula block (2.5.13)

```tex
\displaystyle b_{n}
```

- Formula block (2.5.14)

```tex
|\Gamma\left(x+iy\right)|=\sqrt{2\pi}e^{-\pi|y|/2}|y|^{x-(1/2)}\left(1+o\left(% 1\right)\right),
```

- Formula block (2.5.15)

```tex
I(x)=-\sum_{s=0}^{2n}(a_{s}\ln x+b_{s})x^{-s}+O\left(x^{-2n-1+\epsilon}\right),
```

- Formula block (2.5.16)

```tex
I(x)=\sum_{s=0}^{n-1}(c_{s}\ln x+d_{s})x^{-2s-1}+O\left(x^{-2n-1+\epsilon}% \right),
```


Local metadata:
- Keywords: Mellin transform , Parseval-type formulas , analytic properties , convolution integrals , definition , inversion , locally integrable
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `f(x)` : locally integrable function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : locally integrable function and `c` : point
- Keywords: Mellin transform
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : locally integrable function , `I(x)` : convolution integral and `h(x)` : function
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function , `I(x)` : convolution integral and `h(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : locally integrable function , `c` : point , `I(x)` : convolution integral and `h(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\Re` : real part , `\Residue` : residue , `f(x)` : locally integrable function , `c` : point , `I(x)` : convolution integral , `h(x)` : function , `d` : point and `E(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : locally integrable function , `h(x)` : function , `d` : point and `E(x)` : function
- Keywords: Mellin transform
- Symbols: `J_{\NVar{\nu}}\left(\NVar{z}\right)` : Bessel function of the first kind , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `I(x)` : convolution integral
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\Re` : real part , `\sin\NVar{z}` : sine function and `f(t)=1/(1+t)` : function
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\Re` : real part , `\sin\NVar{z}` : sine function , `h(t)={J_{\nu}}^{2}\left(t\right)` : function and `f(t)=1/(1+t)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\ln\NVar{z}` : principal branch of logarithm function , `\Residue` : residue , `h(t)={J_{\nu}}^{2}\left(t\right)` : function , `a_{n}` : coefficients , `b_{n}` : coefficients and `f(t)=1/(1+t)` : function

### 2.5(ii) Extensions

- Let `f(t)` and `h(t)` be locally integrable on `(0,\infty)` and
- where `\Re\alpha_{s}>\Re\alpha_{s^{\prime}}` for `s>s^{\prime}` , and `\Re\alpha_{s}\to+\infty` as `s\to\infty` . Also, let
- where `\kappa` is real, `p>0` , `\Re\beta_{s}>\Re\beta_{s^{\prime}}` for `s>s^{\prime}` , and `\Re\beta_{s}\to+\infty` as `s\to\infty` . To ensure that the integral ( 2.5.3 ) converges we assume that
- with `b+\Re\beta_{0}>1` , and
- with `c+\Re\alpha_{0}>-1` . To apply the Mellin transform method outlined in  2.5(i) , we require the transforms `\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(1-z\right)` and `\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)` to have a common strip of analyticity. This, in turn, requires `-b<\Re\alpha_{0}` , `-c<\Re\beta_{0}` , and either `-c<\Re\alpha_{0}+1` or `1-b<\Re\beta_{0}` . Following Handelsman and Lew ( 1970 , 1971 ) we now give an extension of this method in which none of these conditions is required.
- First, we introduce the truncated functions `f_{1}(t)` and `f_{2}(t)` defined by

Formula blocks:
- Formula block (2.5.17)

```tex
f(t)\sim\sum_{s=0}^{\infty}a_{s}t^{\alpha_{s}},
```

- Formula block (2.5.18)

```tex
h(t)\sim\exp\left(i\kappa t^{p}\right)\sum_{s=0}^{\infty}b_{s}t^{-\beta_{s}},
```

- Formula block (2.5.19)

```tex
f(t)=O\left(t^{-b}\right),
```

- Formula block (2.5.20)

```tex
h(t)=O\left(t^{c}\right),
```

- Formula block (2.5.21)

```tex
\displaystyle f_{1}(t)
```

- Formula block (2.5.22)

```tex
\displaystyle f_{2}(t)
```

- Formula block (2.5.23)

```tex
\displaystyle h_{1}(t)
```

- Formula block (2.5.24)

```tex
\displaystyle h_{2}(t)
```

- Formula block (2.5.25)

```tex
a_{s}/\left(z+\alpha_{s}\right).
```

- Formula block (2.5.26)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muf_{1% }\mskip 3.0mu\left(z\right)+\mathscr{M}\mskip-3.0muf_{2}\mskip 3.0mu\left(z\right)
```

- Formula block (2.5.27)

```tex
-b_{s}/\left(z-\beta_{s}\right).
```

- Formula block (2.5.28)

```tex
\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muh_{1% }\mskip 3.0mu\left(z\right)+\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)
```

- Formula block (2.5.29)

```tex
I(x)=\sum\limits_{j,k=1}^{2}I_{jk}(x),
```

- Formula block (2.5.30)

```tex
I_{jk}(x)=\int_{0}^{\infty}f_{j}(t)h_{k}(xt)\,\mathrm{d}t.
```

- Formula block (2.5.31)

```tex
I_{21}(x)=0,
```

- Formula block (2.5.32)

```tex
G_{jk}(z)=\mathscr{M}\mskip-3.0muf_{j}\mskip 3.0mu\left(1-z\right)\mathscr{M}% \mskip-3.0muh_{k}\mskip 3.0mu\left(z\right).
```

- Formula block (2.5.33)

```tex
I_{jk}(x)=\frac{1}{2\pi i}\int_{p_{jk}-i\infty}^{p_{jk}+i\infty}x^{-z}G_{jk}(z% )\,\mathrm{d}z.
```

- Formula block (2.5.34)

```tex
\sup_{p_{jk}\leq x\leq q_{jk}}\left|G_{jk}(x+iy)\right|\to 0,
```

- Formula block (2.5.35)

```tex
I_{jk}(x)=\sum_{p_{jk}<\Re z<q_{jk}}\Residue\left[-x^{-z}G_{jk}(z)\right]+E_{% jk}(x),
```

- Formula block (2.5.36)

```tex
E_{jk}(x)=\frac{1}{2\pi i}\int_{q_{jk}-i\infty}^{q_{jk}+i\infty}x^{-z}G_{jk}(z% )\,\mathrm{d}z=o\left(x^{-q_{jk}}\right)
```


Local metadata:
- Keywords: Mellin transform methods , asymptotic approximations of integrals , extensions , multidimensional integrals
- Symbols: `\sim` : Poincar asymptotic expansion , `f(x)` : locally integrable function and `a_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\exp\NVar{z}` : exponential function , `\mathrm{i}` : imaginary unit , `h(x)` : locally integrable function , `\kappa` : real , `p` : positive and `b` : right endpoint
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : locally integrable function and `b` : right endpoint
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `h(x)` : locally integrable function and `c` : point
- Symbols: `f(x)` : locally integrable function and `f_{j}(t)` : truncated functions
- Symbols: `f(x)` : locally integrable function and `f_{j}(t)` : truncated functions
- Symbols: `h(x)` : locally integrable function
- Symbols: `h(x)` : locally integrable function
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\Re` : real part , `f(x)` : locally integrable function , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions , `b` : right endpoint and `c` : point
- Symbols: `a_{s}` : coefficients
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function and `f_{j}(t)` : truncated functions
- Keywords: Mellin transform
- Symbols: `b` : right endpoint
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function and `h(x)` : locally integrable function
- Symbols: `I(x)` : convolution integral
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions and `I(x)` : convolution integral
- Symbols: `I(x)` : convolution integral
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\Re` : real part , `f(x)` : locally integrable function , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions , `D_{jk}` : domain , `b` : right endpoint and `c` : point
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(x)` : locally integrable function , `h(x)` : locally integrable function , `f_{j}(t)` : truncated functions and `G_{jk}(z)` : function

### 2.5(iii) Laplace Transforms with Small Parameters

- Let `h(t)` satisfy ( 2.5.18 ) and ( 2.5.20 ) with `c>-1` , and consider the Laplace transform
- Put `x=1/\zeta` and break the integration range at `t=1` , as in ( 2.5.23 ) and ( 2.5.24 ). Then
- where
- Since `\mathscr{M}\mskip-3.0mue^{-t}\mskip 3.0mu\left(z\right)=\Gamma\left(z\right)` , by the Parseval formula ( 2.5.5 ), there are real numbers `p_{1}` and `p_{2}` such that `-c<p_{1}<1` , `p_{2}<\min(1,\Re\beta_{0})` , and
- Since `\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)` is analytic for `\Re z>-c` , by ( 2.5.14 ),
- for any `\rho` satisfying `1<\rho<2` . Similarly, since `\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)` can be continued analytically to a meromorphic function (when `\kappa=0` ) or to an entire function (when `\kappa\neq 0` ), we can choose `\rho` so that `\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)` has no poles in `1<\Re z\leq\rho<2` . Thus

Formula blocks:
- Formula block (2.5.37)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=\int_{0}^{\infty}h(t)e^% {-\zeta t}\,\mathrm{d}t.
```

- Formula block (2.5.38)

```tex
\zeta\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=I_{1}(x)+I_{2}(x),
```

- Formula block (2.5.39)

```tex
I_{j}(x)=\int_{0}^{\infty}e^{-t}h_{j}(xt)\,\mathrm{d}t,
```

- Formula block (2.5.40)

```tex
I_{j}(x)=\frac{1}{2\pi i}\int_{p_{j}-i\infty}^{p_{j}+i\infty}x^{-z}\Gamma\left% (1-z\right)\mathscr{M}\mskip-3.0muh_{j}\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.41)

```tex
I_{1}(x)=\mathscr{M}\mskip-3.0muh_{1}\mskip 3.0mu\left(1\right)x^{-1}+\frac{1}% {2\pi i}\int_{\rho-i\infty}^{\rho+i\infty}x^{-z}\Gamma\left(1-z\right)\mathscr% {M}\mskip-3.0muh_{1}\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.42)

```tex
I_{2}(x)=\sum_{\Re\beta_{0}\leq\Re z\leq 1}\Residue\left[-x^{-z}\Gamma\left(1-% z\right)\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)\right]+\frac{1}% {2\pi i}\int_{\rho-i\infty}^{\rho+i\infty}x^{-z}\Gamma\left(1-z\right)\mathscr% {M}\mskip-3.0muh_{2}\mskip 3.0mu\left(z\right)\,\mathrm{d}z.
```

- Formula block (2.5.43)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=\mathscr{M}\mskip-3.0% muh_{1}\mskip 3.0mu\left(1\right)+\sum_{\Re\beta_{0}\leq\Re z\leq 1}\Residue% \left[-\zeta^{z-1}\Gamma\left(1-z\right)\mathscr{M}\mskip-3.0muh_{2}\mskip 3.0% mu\left(z\right)\right]+\sum\limits_{1<\Re z<l}\Residue\left[-\zeta^{z-1}% \Gamma\left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\right% ]+\frac{1}{2\pi i}\int_{l-\delta-i\infty}^{l-\delta+i\infty}\zeta^{z-1}\Gamma% \left(1-z\right)\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(z\right)\,\mathrm{d}z,
```

- Formula block (2.5.44)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)\sim\sum_{n=0}^{\infty}b% _{n}\Gamma\left(1-\beta_{n}\right)\zeta^{\beta_{n}-1}+\sum\limits_{n=0}^{% \infty}\frac{(-\zeta)^{n}}{n!}\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(n+1% \right),
```

- Formula block (2.5.45)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=\int_{0}^{\infty}\frac{% e^{-\zeta t}}{1+t}\,\mathrm{d}t,
```

- Formula block (2.5.46)

```tex
\Residue_{z=k}\left[-\zeta^{z-1}\Gamma\left(1-z\right)\pi\csc\left(\pi z\right% )\right]=\left(-\ln\zeta+\psi\left(k\right)\right)\dfrac{\zeta^{k-1}}{(k-1)!},
```

- Formula block (2.5.47)

```tex
\Residue_{z=1}\left[-\zeta^{z-1}\Gamma\left(1-z\right)\mathscr{M}\mskip-3.0muh% _{2}\mskip 3.0mu\left(z\right)\right]=\left(-\ln\zeta-\gamma\right)-\mathscr{M% }\mskip-3.0muh_{1}\mskip 3.0mu\left(1\right),
```

- Formula block (2.5.48)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)\sim(-\ln\zeta)\sum_{k=0% }^{\infty}\frac{\zeta^{k}}{k!}+\sum_{k=0}^{\infty}\psi\left(k+1\right)\frac{% \zeta^{k}}{k!},
```

- Formula block (2.5.49)

```tex
\mathscr{L}\mskip-3.0muh\mskip 3.0mu\left(\zeta\right)=e^{\zeta}E_{1}\left(% \zeta\right);
```


Local metadata:
- Keywords: Laplace transform , asymptotic expansions for small parameters
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral and `h(x)` : locally integrable function
- Keywords: Laplace transform
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `h(x)` : locally integrable function and `I_{j}(x)` : integral
- Keywords: Laplace transform
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `h(x)` : locally integrable function and `I_{j}(x)` : integral
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `h(x)` : locally integrable function , `I_{j}(x)` : integral and `p_{j}` : real numbers
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `h(x)` : locally integrable function , `I_{j}(x)` : integral and `\rho` : parameter
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `\Re` : real part , `\Residue` : residue , `h(x)` : locally integrable function , `I_{j}(x)` : integral and `\rho` : parameter
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `\Re` : real part , `\Residue` : residue , `h(x)` : locally integrable function and `\delta` : arbitrary small positive constant
- Keywords: Laplace transform , Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\sim` : Poincar asymptotic expansion , `!` : factorial (as in `n!` ) , `h(x)` : locally integrable function and `b` : right endpoint
- Keywords: Laplace transform , Mellin transform
- Keywords: Laplace transform , asymptotic expansions for small parameters , exponential integrals , small argument
- Symbols: `\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Laplace transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\Re` : real part and `h(x)` : locally integrable function
- Keywords: Laplace transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\csc\NVar{z}` : cosecant function , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function and `\Residue` : residue
