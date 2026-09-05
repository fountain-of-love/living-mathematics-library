# §2.3 Integrals of a Real Variable

Source: [https://dlmf.nist.gov/2.3](https://dlmf.nist.gov/2.3)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.3. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Integration by Parts
- Watson's Lemma
- Laplace's Method
- Method of Stationary Phase
- Coalescing Peak and Endpoint: Bleistein's Method
- Asymptotics of Mellin Transforms

## Source Notes

- See Olver ( 1997b , pp. 66-70, 75-76) .
- See Olver ( 1997b , pp. 71-72) . For ( 2.3.9 ) see Wong ( 1989 , 2.2) . For ( 2.3.12 ) use termwise integration in an analogous manner to that used to prove Watson's lemma (Olver, 1997b , pp. 71-72) .
- See Olver ( 1997b , pp. 80-88) . ( 2.3.18 ) follows from ( 1.10.15 ) and ( 1.10.17 ) by setting `f(t)=p(t)` , `g(t)=\ifrac{q(t)}{\left(p^{\prime}(t)(p(t)-p(a))^{(\lambda/\mu)-1}\right)}` , using Cauchy's integral formula ( 1.9.30 ) for the residue, and integrating by parts. See also Cicuta and Montaldi ( 1975 ) .

## Keywords

Fourier integral, Fourier integrals, Laplace transform, Laplace transforms, asymptotic approximations of integrals, asymptotic expansions, asymptotic expansions for large parameters, error term, integration by parts, variational operator, Watson's lemma, asymptotic expansions of integrals, generalized, Laplace's method, Laplace's method for asymptotic expansions of integrals, extensions, method of stationary phase, Bleistein's method, coalescing peak and endpoint, Mellin transform

## Principal Formula Blocks

- Formula block (2.3.1)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\,\mathrm{d}t
```

- Formula block (2.3.2)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\frac{q^{(s)}(% 0)}{x^{s+1}},
```

- Formula block (2.3.3)

```tex
\sigma_{n}=\sup_{(0,\infty)}(t^{-1}\ln|q^{(n)}(t)/q^{(n)}(0)|)
```

- Formula block

```tex
\int_{a}^{b}e^{ixt}q(t)\,\mathrm{d}t
```

- Formula block (2.3.4)

```tex
\int_{a}^{b}e^{ixt}q(t)\,\mathrm{d}t\sim e^{iax}\sum_{s=0}^{\infty}q^{(s)}(a)% \left(\frac{i}{x}\right)^{s+1}-e^{ibx}\sum_{s=0}^{\infty}q^{(s)}(b)\left(\frac% {i}{x}\right)^{s+1},
```

- Formula block (2.3.5)

```tex
\int_{a}^{\infty}e^{ixt}q(t)\,\mathrm{d}t\sim e^{iax}\sum_{s=0}^{\infty}q^{(s)% }(a)\left(\frac{i}{x}\right)^{s+1},
```

- Formula block (2.3.6)

```tex
\mathcal{V}_{a,b}\left(f(t)\right)=\int_{a}^{b}\left|f^{\prime}(t)\right|\,% \mathrm{d}t;
```

- Formula block (2.3.7)

```tex
q(t)\sim\sum_{s=0}^{\infty}a_{s}t^{(s+\lambda-\mu)/\mu},
```

- Formula block (2.3.8)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\Gamma\left(% \frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+\lambda)/\mu}},
```

- Formula block (2.3.9)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\ln t\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\Gamma'% \left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+\lambda)/\mu}}-(\ln x)% \sum_{s=0}^{\infty}\Gamma\left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+% \lambda)/\mu}},
```

- Formula block (2.3.10)

```tex
|f(t)|\leq A\exp\left(-at^{\kappa}\right),
```

- Formula block (2.3.11)

```tex
q(t)=O\left(\exp\left(bt^{\kappa}\right)\right),
```

- Formula block (2.3.12)

```tex
\int_{0}^{\infty}f(xt)q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\mathscr{M}% \mskip-3.0muf\mskip 3.0mu\left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+% \lambda)/\mu}},
```

- Formula block (2.3.13)

```tex
I(x)=\int_{a}^{b}e^{-xp(t)}q(t)\,\mathrm{d}t
```

- Formula block

```tex
\displaystyle p(t)
```

- Formula block

```tex
\displaystyle q(t)
```

- Formula block (2.3.15)

```tex
\int_{a}^{b}e^{-xp(t)}q(t)\,\mathrm{d}t\sim e^{-xp(a)}\sum_{s=0}^{\infty}% \Gamma\left(\frac{s+\lambda}{\mu}\right)\frac{b_{s}}{x^{(s+\lambda)/\mu}},
```

- Formula block (2.3.16)

```tex
\frac{q(t)}{p^{\prime}(t)}\sim\sum_{s=0}^{\infty}b_{s}v^{(s+\lambda-\mu)/\mu},
```

- Formula block

```tex
\displaystyle b_{0}
```

- Formula block

```tex
\displaystyle b_{1}
```

- Formula block

```tex
\displaystyle b_{2}
```

- Formula block (2.3.18)

```tex
b_{s}=\frac{1}{\mu}\Residue_{t=a}\left[\frac{q(t)}{(p(t)-p(a))^{(\lambda+s)/% \mu}}\right],
```

- Formula block (2.3.19)

```tex
I(x)=\int_{a}^{b}e^{ixp(t)}q(t)\,\mathrm{d}t
```

- Formula block (2.3.20)

```tex
\int_{0}^{\infty}e^{ixt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\exp\left(% \frac{(s+\lambda)\pi i}{2\mu}\right)\Gamma\left(\frac{s+\lambda}{\mu}\right)% \frac{a_{s}}{x^{(s+\lambda)/\mu}},
```

- Formula block (2.3.21)

```tex
P_{s}(t)=\left(\frac{1}{p^{\prime}(t)}\frac{\mathrm{d}}{\mathrm{d}t}\right)^{s% }\frac{q(t)}{p^{\prime}(t)},
```

- Formula block (2.3.22)

```tex
\int e^{ixp(t)}P_{s}(t)p^{\prime}(t)\,\mathrm{d}t,
```

- Formula block (2.3.23)

```tex
\int_{a}^{b}e^{ixp(t)}q(t)\,\mathrm{d}t\sim e^{ixp(a)}\sum_{s=0}^{\infty}\exp% \left(\frac{(s+\lambda)\pi i}{2\mu}\right)\Gamma\left(\frac{s+\lambda}{\mu}% \right)\frac{b_{s}}{x^{(s+\lambda)/\mu}}-e^{ixp(b)}\sum_{s=0}^{\infty}P_{s}(b)% \left(\frac{i}{x}\right)^{s+1},
```

- Formula block (2.3.24)

```tex
I(\alpha,x)=\int_{0}^{k}e^{-xp(\alpha,t)}q(\alpha,t)t^{\lambda-1}\,\mathrm{d}t
```

- Formula block (2.3.25)

```tex
p(\alpha,t)=\tfrac{1}{2}w^{2}-aw+b,
```

- Formula block

```tex
\displaystyle a
```

- Formula block

```tex
\displaystyle b
```

- Formula block (2.3.27)

```tex
w=(2p(\alpha,0)-2p(\alpha,\alpha))^{1/2}\pm(2p(\alpha,t)-2p(\alpha,\alpha))^{1% /2},
```

- Formula block (2.3.28)

```tex
\frac{\mathrm{d}w}{\mathrm{d}t}=\pm\frac{1}{(2p(\alpha,t)-2p(\alpha,\alpha))^{% 1/2}}\frac{\partial p(\alpha,t)}{\partial t}
```

- Formula block (2.3.29)

```tex
I(\alpha,x)=e^{-xp(\alpha,0)}\*\int_{0}^{\kappa}\exp\left(-x\left(\tfrac{1}{2}% w^{2}-aw\right)\right)f(\alpha,w)w^{\lambda-1}\,\mathrm{d}w,
```

- Formula block (2.3.30)

```tex
f(\alpha,w)=q(\alpha,t)\left(\frac{t}{w}\right)^{\lambda-1}\frac{\mathrm{d}t}{% \mathrm{d}w},
```

- Formula block (2.3.31)

```tex
f(\alpha,w)=\sum_{s=0}^{\infty}\phi_{s}(\alpha)(w-a)^{s},
```

- Formula block (2.3.32)

```tex
I(\alpha,x)\sim\frac{e^{-xp(\alpha,0)}}{x^{\lambda/2}}\sum_{s=0}^{\infty}\phi_% {s}(\alpha)\frac{F_{s}(a\sqrt{x})}{x^{s/2}},
```

- Formula block (2.3.33)

```tex
F_{s}(y)=\int_{0}^{\infty}\exp\left(-\tfrac{1}{2}\tau^{2}+y\tau\right)(\tau-y)% ^{s}\tau^{\lambda-1}\,\mathrm{d}\tau.
```


## Definitions and Symbols

- Keywords: Fourier integral , Fourier integrals , Laplace transform , Laplace transforms , asymptotic approximations of integrals , asymptotic expansions , asymptotic expansions for large parameters , error term , integration by parts , variational operator
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral and `q(t)` : infinitely differentiable function
- Keywords: Laplace transform
- Symbols: `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral and `q(t)` : infinitely differentiable function
- Keywords: Laplace transform
- Defines: `\sigma_{n}` (locally)
- Symbols: `\ln\NVar{z}` : principal branch of logarithm function , `(\NVar{a},\NVar{b})` : open interval , `\sup` : least upper bound (supremum) , `q(t)` : infinitely differentiable function and `n` : nonnegative integer
- Symbols: `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : infinitely differentiable function , `a` : left endpoint and `b` : right endpoint
- Symbols: `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : infinitely differentiable function and `a` : left endpoint
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mathcal{V}_{\NVar{a,b}}\left(\NVar{f}\right)` : total variation , `a` : left endpoint and `b` : right endpoint
- Keywords: Laplace transform , Watson's lemma , asymptotic approximations of integrals , asymptotic expansions for large parameters , asymptotic expansions of integrals , generalized
- Defines: `q(t)` : function (locally)
- Symbols: `\sim` : Poincar asymptotic expansion , `a` : positive constant , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : positive constant , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Keywords: Laplace transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function , `a` : positive constant , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\exp\NVar{z}` : exponential function , `f(x)` : function , `A` : positive constant , `a` : positive constant and `\kappa` : positive constant
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\exp\NVar{z}` : exponential function , `b` : positive constant , `\kappa` : positive constant and `q(t)` : function
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function , `a` : positive constant , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Keywords: Laplace's method , Laplace's method for asymptotic expansions of integrals , asymptotic approximations of integrals
- Defines: `I(x)` : integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : real function and `q(t)` : function
- Symbols: `\sim` : Poincar asymptotic expansion , `a` : left endpoint , `p(t)` : real function , `p_{s}` : coefficients , `q(t)` : function , `q_{s}` : coefficients , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : real function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\sim` : Poincar asymptotic expansion , `b` : right endpoint , `p(t)` : real function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `b` : right endpoint , `p_{s}` : coefficients , `q_{s}` : coefficients , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\Residue` : residue , `a` : left endpoint , `b` : right endpoint , `p(t)` : real function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Keywords: Fourier integral , asymptotic approximations of integrals , asymptotic expansions , extensions , method of stationary phase
- Defines: `I(x)` : integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `p(t)` : real function , `a` : left endpoint , `b` : right endpoint and `q(t)` : function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : function , `a_{s}` : coefficients , `\lambda` : positive constant and `\mu` : positive constant
- Defines: `P_{s}(t)` : function (locally)
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `p(t)` : real function and `q(t)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `p(t)` : real function and `P_{s}(t)` : function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `p(t)` : real function , `a` : left endpoint , `b` : right endpoint , `P_{s}(t)` : function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Keywords: Bleistein's method , asymptotic approximations of integrals , coalescing peak and endpoint
- Defines: `I(\alpha,x)` : integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `p(\alpha,t)` : function , `q(\alpha,t)` : function and `\lambda` : positive constant
- Symbols: `p(\alpha,t)` : function , `w` : change of variable , `a(\alpha)` and `b(\alpha)`
- Symbols: `p(\alpha,t)` : function , `a(\alpha)` and `b(\alpha)`
- Symbols: `p(\alpha,t)` : function and `w` : change of variable
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\frac{\partial\NVar{f}}{\partial\NVar{x}}` : partial derivative of `f` with respect to `x` , `\,\partial\NVar{x}` : partial differential of `x` , `p(\alpha,t)` : function and `w` : change of variable
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `I(\alpha,x)` : integral , `p(\alpha,t)` : function , `w` : change of variable , `a(\alpha)` , `f(\alpha,w)` : function , `\kappa=w(k)` and `\lambda` : positive constant
- Defines: `f(\alpha,w)` : function (locally)
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `q(\alpha,t)` : function , `w` : change of variable and `\lambda` : positive constant
- Symbols: `w` : change of variable , `a(\alpha)` , `f(\alpha,w)` : function and `\phi_{s}(\alpha)` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `I(\alpha,x)` : integral , `p(\alpha,t)` : function , `a(\alpha)` , `\phi_{s}(\alpha)` : coefficients , `F_{s}(y)` : function and `\lambda` : positive constant
- Defines: `F_{s}(y)` : function (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral and `\lambda` : positive constant
- Keywords: Mellin transform , asymptotic approximations of integrals

## Subsections

### 2.3(i) Integration by Parts

- Assume that the Laplace transform
- converges for all sufficiently large `x` , and `q(t)` is infinitely differentiable in a neighborhood of the origin. Then
- If, in addition, `q(t)` is infinitely differentiable on `[0,\infty)` and
- is finite and bounded for `n=0,1,2,\dots` , then the `n` th error term (that is, the difference between the integral and `n` th partial sum in ( 2.3.2 )) is bounded in absolute value by `|q^{(n)}(0)/(x^{n}(x-\sigma_{n}))|` when `x` exceeds both `0` and `\sigma_{n}` .
- For the Fourier integral
- assume `a` and `b` are finite, and `q(t)` is infinitely differentiable on `[a,b]` . Then

Formula blocks:
- Formula block (2.3.1)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\,\mathrm{d}t
```

- Formula block (2.3.2)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\frac{q^{(s)}(% 0)}{x^{s+1}},
```

- Formula block (2.3.3)

```tex
\sigma_{n}=\sup_{(0,\infty)}(t^{-1}\ln|q^{(n)}(t)/q^{(n)}(0)|)
```

- Formula block

```tex
\int_{a}^{b}e^{ixt}q(t)\,\mathrm{d}t
```

- Formula block (2.3.4)

```tex
\int_{a}^{b}e^{ixt}q(t)\,\mathrm{d}t\sim e^{iax}\sum_{s=0}^{\infty}q^{(s)}(a)% \left(\frac{i}{x}\right)^{s+1}-e^{ibx}\sum_{s=0}^{\infty}q^{(s)}(b)\left(\frac% {i}{x}\right)^{s+1},
```

- Formula block (2.3.5)

```tex
\int_{a}^{\infty}e^{ixt}q(t)\,\mathrm{d}t\sim e^{iax}\sum_{s=0}^{\infty}q^{(s)% }(a)\left(\frac{i}{x}\right)^{s+1},
```

- Formula block (2.3.6)

```tex
\mathcal{V}_{a,b}\left(f(t)\right)=\int_{a}^{b}\left|f^{\prime}(t)\right|\,% \mathrm{d}t;
```


Local metadata:
- Keywords: Fourier integral , Fourier integrals , Laplace transform , Laplace transforms , asymptotic approximations of integrals , asymptotic expansions , asymptotic expansions for large parameters , error term , integration by parts , variational operator
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral and `q(t)` : infinitely differentiable function
- Keywords: Laplace transform
- Symbols: `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral and `q(t)` : infinitely differentiable function
- Keywords: Laplace transform
- Defines: `\sigma_{n}` (locally)
- Symbols: `\ln\NVar{z}` : principal branch of logarithm function , `(\NVar{a},\NVar{b})` : open interval , `\sup` : least upper bound (supremum) , `q(t)` : infinitely differentiable function and `n` : nonnegative integer
- Symbols: `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : infinitely differentiable function , `a` : left endpoint and `b` : right endpoint
- Symbols: `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : infinitely differentiable function and `a` : left endpoint
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mathcal{V}_{\NVar{a,b}}\left(\NVar{f}\right)` : total variation , `a` : left endpoint and `b` : right endpoint

### 2.3(ii) Watson's Lemma

- Assume again that the integral ( 2.3.1 ) converges for all sufficiently large `x` , but now
- where `\lambda` and `\mu` are positive constants. Then the series obtained by substituting ( 2.3.7 ) into ( 2.3.1 ) and integrating formally term by term yields an asymptotic expansion:
- For the function `\Gamma` see  5.2(i) .
- This result is probably the most frequently used method for deriving asymptotic expansions of special functions. Since `q(t)` need not be continuous (as long as the integral converges), the case of a finite integration range is included. For an extension with more general `t` -powers see Bleistein and Handelsman ( 1975 , 4.1) .
- Other types of singular behavior in the integrand can be treated in an analogous manner. For example,
- provided that the integral on the left-hand side of ( 2.3.9 ) converges for all sufficiently large values of `x` . (In other words, differentiation of ( 2.3.8 ) with respect to the parameter `\lambda` (or `\mu` ) is legitimate.)

Formula blocks:
- Formula block (2.3.7)

```tex
q(t)\sim\sum_{s=0}^{\infty}a_{s}t^{(s+\lambda-\mu)/\mu},
```

- Formula block (2.3.8)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\Gamma\left(% \frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+\lambda)/\mu}},
```

- Formula block (2.3.9)

```tex
\int_{0}^{\infty}e^{-xt}q(t)\ln t\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\Gamma'% \left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+\lambda)/\mu}}-(\ln x)% \sum_{s=0}^{\infty}\Gamma\left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+% \lambda)/\mu}},
```

- Formula block (2.3.10)

```tex
|f(t)|\leq A\exp\left(-at^{\kappa}\right),
```

- Formula block (2.3.11)

```tex
q(t)=O\left(\exp\left(bt^{\kappa}\right)\right),
```

- Formula block (2.3.12)

```tex
\int_{0}^{\infty}f(xt)q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\mathscr{M}% \mskip-3.0muf\mskip 3.0mu\left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}}{x^{(s+% \lambda)/\mu}},
```


Local metadata:
- Keywords: Laplace transform , Watson's lemma , asymptotic approximations of integrals , asymptotic expansions for large parameters , asymptotic expansions of integrals , generalized
- Defines: `q(t)` : function (locally)
- Symbols: `\sim` : Poincar asymptotic expansion , `a` : positive constant , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : positive constant , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Keywords: Laplace transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function , `a` : positive constant , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\exp\NVar{z}` : exponential function , `f(x)` : function , `A` : positive constant , `a` : positive constant and `\kappa` : positive constant
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\exp\NVar{z}` : exponential function , `b` : positive constant , `\kappa` : positive constant and `q(t)` : function
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(x)` : function , `a` : positive constant , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant

### 2.3(iii) Laplace's Method

- When `p(t)` is real and `x` is a large positive parameter, the main contribution to the integral
- derives from the neighborhood of the minimum of `p(t)` in the integration range. Without loss of generality, we assume that this minimum is at the left endpoint `a` . Furthermore:
- Then
- where the coefficients `b_{s}` are defined by the expansion
- in which `v=p(t)-p(a)` . For example,
- In general

Formula blocks:
- Formula block (2.3.13)

```tex
I(x)=\int_{a}^{b}e^{-xp(t)}q(t)\,\mathrm{d}t
```

- Formula block

```tex
\displaystyle p(t)
```

- Formula block

```tex
\displaystyle q(t)
```

- Formula block (2.3.15)

```tex
\int_{a}^{b}e^{-xp(t)}q(t)\,\mathrm{d}t\sim e^{-xp(a)}\sum_{s=0}^{\infty}% \Gamma\left(\frac{s+\lambda}{\mu}\right)\frac{b_{s}}{x^{(s+\lambda)/\mu}},
```

- Formula block (2.3.16)

```tex
\frac{q(t)}{p^{\prime}(t)}\sim\sum_{s=0}^{\infty}b_{s}v^{(s+\lambda-\mu)/\mu},
```

- Formula block

```tex
\displaystyle b_{0}
```

- Formula block

```tex
\displaystyle b_{1}
```

- Formula block

```tex
\displaystyle b_{2}
```

- Formula block (2.3.18)

```tex
b_{s}=\frac{1}{\mu}\Residue_{t=a}\left[\frac{q(t)}{(p(t)-p(a))^{(\lambda+s)/% \mu}}\right],
```


Local metadata:
- Keywords: Laplace's method , Laplace's method for asymptotic expansions of integrals , asymptotic approximations of integrals
- Defines: `I(x)` : integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : real function and `q(t)` : function
- Symbols: `\sim` : Poincar asymptotic expansion , `a` : left endpoint , `p(t)` : real function , `p_{s}` : coefficients , `q(t)` : function , `q_{s}` : coefficients , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : real function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\sim` : Poincar asymptotic expansion , `b` : right endpoint , `p(t)` : real function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `b` : right endpoint , `p_{s}` : coefficients , `q_{s}` : coefficients , `\lambda` : positive constant and `\mu` : positive constant
- Symbols: `\Residue` : residue , `a` : left endpoint , `b` : right endpoint , `p(t)` : real function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant

### 2.3(iv) Method of Stationary Phase

- When the parameter `x` is large the contributions from the real and imaginary parts of the integrand in
- oscillate rapidly and cancel themselves over most of the range. However, cancellation does not take place near the endpoints, owing to lack of symmetry, nor in the neighborhoods of zeros of `p^{\prime}(t)` because `p(t)` changes relatively slowly at these stationary points.
- The first result is the analog of Watson's lemma ( 2.3(ii) ). Assume that `q(t)` again has the expansion ( 2.3.7 ) and this expansion is infinitely differentiable, `q(t)` is infinitely differentiable on `(0,\infty)` , and each of the integrals `\int e^{ixt}q^{(s)}(t)\,\mathrm{d}t` , `s=0,1,2,\dots` , converges at `t=\infty` , uniformly for all sufficiently large `x` . Then
- where the coefficients `a_{s}` are given by ( 2.3.7 ).
- For the more general integral ( 2.3.19 ) we assume, without loss of generality, that the stationary point (if any) is at the left endpoint. Furthermore:
- If `p(b)` is finite, then both endpoints contribute:

Formula blocks:
- Formula block (2.3.19)

```tex
I(x)=\int_{a}^{b}e^{ixp(t)}q(t)\,\mathrm{d}t
```

- Formula block (2.3.20)

```tex
\int_{0}^{\infty}e^{ixt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\exp\left(% \frac{(s+\lambda)\pi i}{2\mu}\right)\Gamma\left(\frac{s+\lambda}{\mu}\right)% \frac{a_{s}}{x^{(s+\lambda)/\mu}},
```

- Formula block (2.3.21)

```tex
P_{s}(t)=\left(\frac{1}{p^{\prime}(t)}\frac{\mathrm{d}}{\mathrm{d}t}\right)^{s% }\frac{q(t)}{p^{\prime}(t)},
```

- Formula block (2.3.22)

```tex
\int e^{ixp(t)}P_{s}(t)p^{\prime}(t)\,\mathrm{d}t,
```

- Formula block (2.3.23)

```tex
\int_{a}^{b}e^{ixp(t)}q(t)\,\mathrm{d}t\sim e^{ixp(a)}\sum_{s=0}^{\infty}\exp% \left(\frac{(s+\lambda)\pi i}{2\mu}\right)\Gamma\left(\frac{s+\lambda}{\mu}% \right)\frac{b_{s}}{x^{(s+\lambda)/\mu}}-e^{ixp(b)}\sum_{s=0}^{\infty}P_{s}(b)% \left(\frac{i}{x}\right)^{s+1},
```


Local metadata:
- Keywords: Fourier integral , asymptotic approximations of integrals , asymptotic expansions , extensions , method of stationary phase
- Defines: `I(x)` : integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `p(t)` : real function , `a` : left endpoint , `b` : right endpoint and `q(t)` : function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : function , `a_{s}` : coefficients , `\lambda` : positive constant and `\mu` : positive constant
- Defines: `P_{s}(t)` : function (locally)
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `p(t)` : real function and `q(t)` : function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `p(t)` : real function and `P_{s}(t)` : function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `p(t)` : real function , `a` : left endpoint , `b` : right endpoint , `P_{s}(t)` : function , `q(t)` : function , `\lambda` : positive constant and `\mu` : positive constant

### 2.3(v) Coalescing Peak and Endpoint: Bleistein's Method

- In the integral
- `k` ( `\leq\infty` ) and `\lambda` are positive constants, `\alpha` is a variable parameter in an interval `\alpha_{1}\leq\alpha\leq\alpha_{2}` with `\alpha_{1}\leq 0` and `0<\alpha_{2}\leq k` , and `x` is a large positive parameter. Assume also that `\ifrac{{\partial}^{2}p(\alpha,t)}{{\partial t}^{2}}` and `q(\alpha,t)` are continuous in `\alpha` and `t` , and for each `\alpha` the minimum value of `p(\alpha,t)` in `[0,k)` is at `t=\alpha` , at which point `\ifrac{\partial p(\alpha,t)}{\partial t}` vanishes, but both `\ifrac{{\partial}^{2}p(\alpha,t)}{{\partial t}^{2}}` and `q(\alpha,t)` are nonzero. When `x\to+\infty` Laplace's method ( 2.3(iii) ) applies, but the form of the resulting approximation is discontinuous at `\alpha=0` . In consequence, the approximation is nonuniform with respect to `\alpha` and deteriorates severely as `\alpha\to 0` .
- A uniform approximation can be constructed by quadratic change of integration variable:
- where `a` and `b` are functions of `\alpha` chosen in such a way that `t=0` corresponds to `w=0` , and the stationary points `t=\alpha` and `w=a` correspond. Thus
- the upper or lower sign being taken according as `t\gtrless\alpha` . The relationship between `t` and `w` is one-to-one, and because
- it is free from singularity at `t=\alpha` .

Formula blocks:
- Formula block (2.3.24)

```tex
I(\alpha,x)=\int_{0}^{k}e^{-xp(\alpha,t)}q(\alpha,t)t^{\lambda-1}\,\mathrm{d}t
```

- Formula block (2.3.25)

```tex
p(\alpha,t)=\tfrac{1}{2}w^{2}-aw+b,
```

- Formula block

```tex
\displaystyle a
```

- Formula block

```tex
\displaystyle b
```

- Formula block (2.3.27)

```tex
w=(2p(\alpha,0)-2p(\alpha,\alpha))^{1/2}\pm(2p(\alpha,t)-2p(\alpha,\alpha))^{1% /2},
```

- Formula block (2.3.28)

```tex
\frac{\mathrm{d}w}{\mathrm{d}t}=\pm\frac{1}{(2p(\alpha,t)-2p(\alpha,\alpha))^{% 1/2}}\frac{\partial p(\alpha,t)}{\partial t}
```

- Formula block (2.3.29)

```tex
I(\alpha,x)=e^{-xp(\alpha,0)}\*\int_{0}^{\kappa}\exp\left(-x\left(\tfrac{1}{2}% w^{2}-aw\right)\right)f(\alpha,w)w^{\lambda-1}\,\mathrm{d}w,
```

- Formula block (2.3.30)

```tex
f(\alpha,w)=q(\alpha,t)\left(\frac{t}{w}\right)^{\lambda-1}\frac{\mathrm{d}t}{% \mathrm{d}w},
```

- Formula block (2.3.31)

```tex
f(\alpha,w)=\sum_{s=0}^{\infty}\phi_{s}(\alpha)(w-a)^{s},
```

- Formula block (2.3.32)

```tex
I(\alpha,x)\sim\frac{e^{-xp(\alpha,0)}}{x^{\lambda/2}}\sum_{s=0}^{\infty}\phi_% {s}(\alpha)\frac{F_{s}(a\sqrt{x})}{x^{s/2}},
```

- Formula block (2.3.33)

```tex
F_{s}(y)=\int_{0}^{\infty}\exp\left(-\tfrac{1}{2}\tau^{2}+y\tau\right)(\tau-y)% ^{s}\tau^{\lambda-1}\,\mathrm{d}\tau.
```


Local metadata:
- Keywords: Bleistein's method , asymptotic approximations of integrals , coalescing peak and endpoint
- Defines: `I(\alpha,x)` : integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `p(\alpha,t)` : function , `q(\alpha,t)` : function and `\lambda` : positive constant
- Symbols: `p(\alpha,t)` : function , `w` : change of variable , `a(\alpha)` and `b(\alpha)`
- Symbols: `p(\alpha,t)` : function , `a(\alpha)` and `b(\alpha)`
- Symbols: `p(\alpha,t)` : function and `w` : change of variable
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\frac{\partial\NVar{f}}{\partial\NVar{x}}` : partial derivative of `f` with respect to `x` , `\,\partial\NVar{x}` : partial differential of `x` , `p(\alpha,t)` : function and `w` : change of variable
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `I(\alpha,x)` : integral , `p(\alpha,t)` : function , `w` : change of variable , `a(\alpha)` , `f(\alpha,w)` : function , `\kappa=w(k)` and `\lambda` : positive constant
- Defines: `f(\alpha,w)` : function (locally)
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `q(\alpha,t)` : function , `w` : change of variable and `\lambda` : positive constant
- Symbols: `w` : change of variable , `a(\alpha)` , `f(\alpha,w)` : function and `\phi_{s}(\alpha)` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `I(\alpha,x)` : integral , `p(\alpha,t)` : function , `a(\alpha)` , `\phi_{s}(\alpha)` : coefficients , `F_{s}(y)` : function and `\lambda` : positive constant
- Defines: `F_{s}(y)` : function (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\int` : integral and `\lambda` : positive constant

### 2.3(vi) Asymptotics of Mellin Transforms

- For the asymptotics of the Mellin transform `\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\int^{\infty}_{0}t^{z-1}f(t% )\,\mathrm{d}t` as `z\to\infty` see Frenzen ( 1987b ) , Sidi ( 1985 , 2011 ) .

Local metadata:
- Keywords: Mellin transform , asymptotic approximations of integrals
