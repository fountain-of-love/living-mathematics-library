# §2.4 Contour Integrals

Source: [https://dlmf.nist.gov/2.4](https://dlmf.nist.gov/2.4)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.4. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Watson's Lemma
- Inverse Laplace Transforms
- Laplace's Method
- Saddle Points
- Coalescing Saddle Points: Chester, Friedman, and Ursell's Method
- Other Coalescing Critical Points

## Source Notes

- See Olver ( 1997b , pp. 112-118) .
- See Wong ( 1989 , p. 31) and Olver ( 1997b , pp. 315-320) .
- See Olver ( 1997b , pp. 121-125) .
- See Olver ( 1997b , pp. 125-127) .

## Keywords

Laplace transform, Watson's lemma, asymptotic approximations of integrals, asymptotic expansions, asymptotic expansions for large parameters, asymptotic expansions of integrals, inverse Laplace transforms, Haar's method, Laplace's method, Laplace's method for asymptotic expansions of integrals, method of steepest descents, saddle points, Chester-Friedman-Ursell method, coalescing, coalescing critical points, coalescing saddle points

## Principal Formula Blocks

- Formula block (2.4.1)

```tex
\int_{0}^{\infty}e^{-zt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\Gamma\left(% \frac{s+\lambda}{\mu}\right)\frac{a_{s}}{z^{(s+\lambda)/\mu}}
```

- Formula block (2.4.2)

```tex
Q(z)=\int_{0}^{\infty}e^{-zt}q(t)\,\mathrm{d}t
```

- Formula block (2.4.3)

```tex
q(t)=\frac{1}{2\pi i}\lim\limits_{\eta\to\infty}\int_{\sigma-i\eta}^{\sigma+i% \eta}e^{tz}Q(z)\,\mathrm{d}z,
```

- Formula block (2.4.4)

```tex
Q(z)\sim\sum_{s=0}^{\infty}\Gamma\left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}% }{z^{(s+\lambda)/\mu}},
```

- Formula block (2.4.5)

```tex
q(t)=\frac{1}{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}e^{tz}Q(z)\,\mathrm% {d}z,
```

- Formula block (2.4.6)

```tex
f(t)=\frac{1}{2\pi i}\lim\limits_{\eta\to\infty}\int_{\sigma-i\eta}^{\sigma+i% \eta}e^{tz}F(z)\,\mathrm{d}z
```

- Formula block (2.4.7)

```tex
q(t)-f(t)=\frac{e^{\sigma t}}{2\pi}\lim\limits_{\eta\to\infty}\int_{-\eta}^{% \eta}e^{it\tau}(Q(\sigma+i\tau)-F(\sigma+i\tau))\,\mathrm{d}\tau.
```

- Formula block (2.4.8)

```tex
q(t)=f(t)+o\left(e^{ct}\right),
```

- Formula block (2.4.9)

```tex
q(t)=f(t)+o\left(t^{-m}e^{ct}\right),
```

- Formula block (2.4.10)

```tex
I(z)=\int_{a}^{b}e^{-zp(t)}q(t)\,\mathrm{d}t,
```

- Formula block

```tex
\displaystyle p(t)
```

- Formula block

```tex
\displaystyle q(t)
```

- Formula block (2.4.12)

```tex
I(z)\sim e^{-zp(a)}\sum_{s=0}^{\infty}\Gamma\left(\frac{s+\lambda}{\mu}\right)% \frac{b_{s}}{z^{(s+\lambda)/\mu}}
```

- Formula block (2.4.13)

```tex
|\theta+\mu\omega+\operatorname{ph}p_{0}|\leq\tfrac{1}{2}\pi.
```

- Formula block (2.4.14)

```tex
I(z)=\int_{t_{0}}^{b}e^{-zp(t)}q(t)\,\mathrm{d}t-\int_{t_{0}}^{a}e^{-zp(t)}q(t% )\,\mathrm{d}t,
```

- Formula block (2.4.15)

```tex
\int_{a}^{b}e^{-zp(t)}q(t)\,\mathrm{d}t\sim 2e^{-zp(t_{0})}\sum_{s=0}^{\infty}% \Gamma\left(s+\tfrac{1}{2}\right)\frac{b_{2s}}{z^{s+(1/2)}},
```

- Formula block

```tex
\displaystyle b_{0}
```

- Formula block

```tex
\displaystyle b_{2}
```

- Formula block (2.4.17)

```tex
I(\alpha,z)=\int_{\mathscr{P}}e^{-zp(\alpha,t)}q(\alpha,t)\,\mathrm{d}t
```

- Formula block (2.4.18)

```tex
p(\alpha,t)=\tfrac{1}{3}w^{3}+aw^{2}+bw+c,
```

- Formula block (2.4.19)

```tex
I(\alpha,z)=e^{-cz}\int_{\mathscr{Q}}\exp\left(-z\left(\tfrac{1}{3}w^{3}+aw^{2% }+bw\right)\right)f(\alpha,w)\,\mathrm{d}w,
```

- Formula block (2.4.20)

```tex
f(\alpha,w)=q(\alpha,t)\frac{\mathrm{d}t}{\mathrm{d}w}=q(\alpha,t)\frac{w^{2}+% 2aw+b}{\ifrac{\partial p(\alpha,t)}{\partial t}}.
```

- Formula block (2.4.21)

```tex
w=z^{-1/3}v-a,
```


## Definitions and Symbols

- Keywords: Laplace transform , Watson's lemma , asymptotic approximations of integrals , asymptotic expansions , asymptotic expansions for large parameters , asymptotic expansions of integrals , inverse Laplace transforms
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\lambda` : constant , `a` : left endpoint , `q(t)` : analytic function and `\mu` : positive constant
- Keywords: Haar's method , asymptotic approximations of integrals , asymptotic expansions , inverse Laplace transforms
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `q(t)` : analytic function and `Q(z)` : Laplace transform of `q(t)`
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : analytic function , `Q(z)` : Laplace transform of `q(t)` and `\sigma` : constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\lambda` : constant , `a` : left endpoint , `\mu` : positive constant and `Q(z)` : Laplace transform of `q(t)`
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : analytic function , `Q(z)` : Laplace transform of `q(t)` and `\sigma` : constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `\sigma` : constant , `F(z)` : comparison function and `f(x)` : inverse transform of comparison function
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : analytic function , `Q(z)` : Laplace transform of `q(t)` , `\sigma` : constant , `F(z)` : comparison function and `f(x)` : inverse transform of comparison function
- Symbols: `\mathrm{e}` : base of natural logarithm , `o\left(\NVar{x}\right)` : order less than , `q(t)` : analytic function , `c` : real constant and `f(x)` : inverse transform of comparison function
- Symbols: `\mathrm{e}` : base of natural logarithm , `o\left(\NVar{x}\right)` : order less than , `q(t)` : analytic function , `c` : real constant and `f(x)` : inverse transform of comparison function
- Keywords: Laplace's method , Laplace's method for asymptotic expansions of integrals , asymptotic approximations of integrals
- Defines: `I(z)` : contour integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : analytic function and `q(t)` : analytic function
- Symbols: `\lambda` : constant , `a` : left endpoint , `p(t)` : analytic function , `q(t)` : analytic function , `p_{s}` : coefficients , `q_{s}` : coefficients and `\mu` : positive constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `\lambda` : constant , `a` : left endpoint , `b` : right endpoint , `I(z)` : contour integral , `p(t)` : analytic function and `\mu` : positive constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{ph}` : phase , `\omega` : angle , `p_{s}` : coefficients , `\theta_{j}` : angles and `\mu` : positive constant
- Keywords: asymptotic approximations of integrals , method of steepest descents , saddle points
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `I(z)` : contour integral , `p(t)` : analytic function and `q(t)` : analytic function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : analytic function and `q(t)` : analytic function
- Symbols: `b` : right endpoint , `p(t)` : analytic function and `q(t)` : analytic function
- Keywords: Chester-Friedman-Ursell method , asymptotic approximations of integrals , coalescing , coalescing critical points , coalescing saddle points , saddle points
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\mathscr{P}` : contour , `p(t)` : analytic function , `q(t)` : analytic function and `I(\alpha,z)` : integral
- Symbols: `p(t)` : analytic function , `w` : change of variable , `a` , `b` and `c` : real constant
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `I(\alpha,z)` : integral , `w` : change of variable , `a` , `b` , `\mathscr{Q}` : countour , `f(\alpha,w)` : function and `c` : real constant
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\frac{\partial\NVar{f}}{\partial\NVar{x}}` : partial derivative of `f` with respect to `x` , `\,\partial\NVar{x}` : partial differential of `x` , `p(t)` : analytic function , `q(t)` : analytic function , `w` : change of variable , `a` , `b` and `f(\alpha,w)` : function
- Symbols: `w` : change of variable and `a`
- Keywords: asymptotic approximations of integrals , coalescing critical points

## Subsections

### 2.4(i) Watson's Lemma

- The result in  2.3(ii) carries over to a complex parameter `z` . Except that `\lambda` is now permitted to be complex, with `\Re\lambda>0` , we assume the same conditions on `q(t)` and also that the Laplace transform in ( 2.3.8 ) converges for all sufficiently large values of `\Re z` . Then
- as `z\to\infty` in the sector `|\operatorname{ph}z|\leq\frac{1}{2}\pi-\delta` ( `<\frac{1}{2}\pi` ), with `z^{(s+\lambda)/\mu}` assigned its principal value.
- If `q(t)` is analytic in a sector `\alpha_{1}<\operatorname{ph}t<\alpha_{2}` containing `\operatorname{ph}t=0` , then the region of validity may be increased by rotation of the integration paths. We assume that in any closed sector with vertex `t=0` and properly interior to `\alpha_{1}<\operatorname{ph}t<\alpha_{2}` , the expansion ( 2.3.7 ) holds as `t\to 0` , and `q(t)=O\left(e^{\sigma|t|}\right)` as `t\to\infty` , where `\sigma` is a constant. Then ( 2.4.1 ) is valid in any closed sector with vertex `z=0` and properly interior to `-\alpha_{2}-\frac{1}{2}\pi<\operatorname{ph}z<-\alpha_{1}+\frac{1}{2}\pi` . (The branches of `t^{(s+\lambda-\mu)/\mu}` and `z^{(s+\lambda)/\mu}` are extended by continuity.)
- For examples and extensions (including uniformity and loop integrals) see Olver ( 1997b , Chapter 4) , Wong ( 1989 , Chapter 1) , and Temme ( 1985 ) .

Formula blocks:
- Formula block (2.4.1)

```tex
\int_{0}^{\infty}e^{-zt}q(t)\,\mathrm{d}t\sim\sum_{s=0}^{\infty}\Gamma\left(% \frac{s+\lambda}{\mu}\right)\frac{a_{s}}{z^{(s+\lambda)/\mu}}
```


Local metadata:
- Keywords: Laplace transform , Watson's lemma , asymptotic approximations of integrals , asymptotic expansions , asymptotic expansions for large parameters , asymptotic expansions of integrals , inverse Laplace transforms
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\lambda` : constant , `a` : left endpoint , `q(t)` : analytic function and `\mu` : positive constant

### 2.4(ii) Inverse Laplace Transforms

- On the interval `0<t<\infty` let `q(t)` be differentiable and `e^{-ct}q(t)` be absolutely integrable, where `c` is a real constant. Then the Laplace transform
- is continuous in `\Re z\geq c` and analytic in `\Re z>c` , and by inversion ( 1.14(iii) )
- where `\sigma` ( `\geq c` ) is a constant.
- Now assume that `c>0` and we are given a function `Q(z)` that is both analytic and has the expansion
- in the half-plane `\Re z\geq c` . Here `\Re\lambda>0` , `\mu>0` , and `z^{(s+\lambda)/\mu}` has its principal value. Assume also ( 2.4.4 ) is differentiable. Then by integration by parts the integral
- is seen to converge absolutely at each limit, and be independent of `\sigma\in[c,\infty)` . Furthermore, as `t\to 0+` , `q(t)` has the expansion ( 2.3.7 ).

Formula blocks:
- Formula block (2.4.2)

```tex
Q(z)=\int_{0}^{\infty}e^{-zt}q(t)\,\mathrm{d}t
```

- Formula block (2.4.3)

```tex
q(t)=\frac{1}{2\pi i}\lim\limits_{\eta\to\infty}\int_{\sigma-i\eta}^{\sigma+i% \eta}e^{tz}Q(z)\,\mathrm{d}z,
```

- Formula block (2.4.4)

```tex
Q(z)\sim\sum_{s=0}^{\infty}\Gamma\left(\frac{s+\lambda}{\mu}\right)\frac{a_{s}% }{z^{(s+\lambda)/\mu}},
```

- Formula block (2.4.5)

```tex
q(t)=\frac{1}{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}e^{tz}Q(z)\,\mathrm% {d}z,
```

- Formula block (2.4.6)

```tex
f(t)=\frac{1}{2\pi i}\lim\limits_{\eta\to\infty}\int_{\sigma-i\eta}^{\sigma+i% \eta}e^{tz}F(z)\,\mathrm{d}z
```

- Formula block (2.4.7)

```tex
q(t)-f(t)=\frac{e^{\sigma t}}{2\pi}\lim\limits_{\eta\to\infty}\int_{-\eta}^{% \eta}e^{it\tau}(Q(\sigma+i\tau)-F(\sigma+i\tau))\,\mathrm{d}\tau.
```

- Formula block (2.4.8)

```tex
q(t)=f(t)+o\left(e^{ct}\right),
```

- Formula block (2.4.9)

```tex
q(t)=f(t)+o\left(t^{-m}e^{ct}\right),
```


Local metadata:
- Keywords: Haar's method , asymptotic approximations of integrals , asymptotic expansions , inverse Laplace transforms
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `q(t)` : analytic function and `Q(z)` : Laplace transform of `q(t)`
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : analytic function , `Q(z)` : Laplace transform of `q(t)` and `\sigma` : constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\lambda` : constant , `a` : left endpoint , `\mu` : positive constant and `Q(z)` : Laplace transform of `q(t)`
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : analytic function , `Q(z)` : Laplace transform of `q(t)` and `\sigma` : constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `\sigma` : constant , `F(z)` : comparison function and `f(x)` : inverse transform of comparison function
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `q(t)` : analytic function , `Q(z)` : Laplace transform of `q(t)` , `\sigma` : constant , `F(z)` : comparison function and `f(x)` : inverse transform of comparison function
- Symbols: `\mathrm{e}` : base of natural logarithm , `o\left(\NVar{x}\right)` : order less than , `q(t)` : analytic function , `c` : real constant and `f(x)` : inverse transform of comparison function
- Symbols: `\mathrm{e}` : base of natural logarithm , `o\left(\NVar{x}\right)` : order less than , `q(t)` : analytic function , `c` : real constant and `f(x)` : inverse transform of comparison function

### 2.4(iii) Laplace's Method

- Let `\mathscr{P}` denote the path for the contour integral
- in which `a` is finite, `b` is finite or infinite, and `\omega` is the angle of slope of `\mathscr{P}` at `a` , that is, `\lim(\operatorname{ph}\left(t-a\right))` as `t\to a` along `\mathscr{P}` . Assume that `p(t)` and `q(t)` are analytic on an open domain `\mathbf{T}` that contains `\mathscr{P}` , with the possible exceptions of `t=a` and `t=b` . Other assumptions are:
- Then
- as `z\to\infty` in the sector `\theta_{1}\leq\operatorname{ph}z\leq\theta_{2}` . The coefficients `b_{s}` are determined as in  2.3(iii) , the branch of `\operatorname{ph}p_{0}` being chosen to satisfy
- For examples see Olver ( 1997b , Chapter 4) . For error bounds see Boyd ( 1993 ) .

Formula blocks:
- Formula block (2.4.10)

```tex
I(z)=\int_{a}^{b}e^{-zp(t)}q(t)\,\mathrm{d}t,
```

- Formula block

```tex
\displaystyle p(t)
```

- Formula block

```tex
\displaystyle q(t)
```

- Formula block (2.4.12)

```tex
I(z)\sim e^{-zp(a)}\sum_{s=0}^{\infty}\Gamma\left(\frac{s+\lambda}{\mu}\right)% \frac{b_{s}}{z^{(s+\lambda)/\mu}}
```

- Formula block (2.4.13)

```tex
|\theta+\mu\omega+\operatorname{ph}p_{0}|\leq\tfrac{1}{2}\pi.
```


Local metadata:
- Keywords: Laplace's method , Laplace's method for asymptotic expansions of integrals , asymptotic approximations of integrals
- Defines: `I(z)` : contour integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : analytic function and `q(t)` : analytic function
- Symbols: `\lambda` : constant , `a` : left endpoint , `p(t)` : analytic function , `q(t)` : analytic function , `p_{s}` : coefficients , `q_{s}` : coefficients and `\mu` : positive constant
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `\lambda` : constant , `a` : left endpoint , `b` : right endpoint , `I(z)` : contour integral , `p(t)` : analytic function and `\mu` : positive constant
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{ph}` : phase , `\omega` : angle , `p_{s}` : coefficients , `\theta_{j}` : angles and `\mu` : positive constant

### 2.4(iv) Saddle Points

- Now suppose that in ( 2.4.10 ) the minimum of `\Re\left(zp(t)\right)` on `\mathscr{P}` occurs at an interior point `t_{0}` . Temporarily assume that `\theta` `(=\operatorname{ph}z)` is fixed, so that `t_{0}` is independent of `z` . We may subdivide
- and apply the result of  2.4(iii) to each integral on the right-hand side, the role of the series ( 2.4.11 ) being played by the Taylor series of `p(t)` and `q(t)` at `t=t_{0}` . If `p^{\prime}(t_{0})\neq 0` , then `\mu=1` , `\lambda` is a positive integer, and the two resulting asymptotic expansions are identical. Thus the right-hand side of ( 2.4.14 ) reduces to the error terms. However, if `p^{\prime}(t_{0})=0` , then `\mu\geq 2` and different branches of some of the fractional powers of `p_{0}` are used for the coefficients `b_{s}` ; again see  2.3(iii) . In consequence, the asymptotic expansion obtained from ( 2.4.14 ) is no longer null.
- Zeros of `p^{\prime}(t)` are called saddle points (or cols ) owing to the shape of the surface `|p(t)|` , `t\in\mathbb{C}` , in their vicinity. Cases in which `p^{\prime}(t_{0})\neq 0` are usually handled by deforming the integration path in such a way that the minimum of `\Re\left(zp(t)\right)` is attained at a saddle point or at an endpoint. Additionally, it may be advantageous to arrange that `\Im\left(zp(t)\right)` is constant on the path: this will usually lead to greater regions of validity and sharper error bounds. Paths on which `\Im\left(zp(t)\right)` is constant are also the ones on which `|\exp\left(-zp(t)\right)|` decreases most rapidly. For this reason the name method of steepest descents is often used. However, for the purpose of simply deriving the asymptotic expansions the use of steepest descent paths is not essential.
- In the commonest case the interior minimum `t_{0}` of `\Re\left(zp(t)\right)` is a simple zero of `p^{\prime}(t)` . The final expansion then has the form
- in which
- with `p,q` and their derivatives evaluated at `t_{0}` . The branch of `\omega_{0}=\operatorname{ph}\left(p^{\prime\prime}(t_{0})\right)` is the one satisfying `|\theta+2\omega+\omega_{0}|\leq\frac{1}{2}\pi` , where `\omega` is the limiting value of `\operatorname{ph}\left(t-t_{0}\right)` as `t\to t_{0}` from `b` .

Formula blocks:
- Formula block (2.4.14)

```tex
I(z)=\int_{t_{0}}^{b}e^{-zp(t)}q(t)\,\mathrm{d}t-\int_{t_{0}}^{a}e^{-zp(t)}q(t% )\,\mathrm{d}t,
```

- Formula block (2.4.15)

```tex
\int_{a}^{b}e^{-zp(t)}q(t)\,\mathrm{d}t\sim 2e^{-zp(t_{0})}\sum_{s=0}^{\infty}% \Gamma\left(s+\tfrac{1}{2}\right)\frac{b_{2s}}{z^{s+(1/2)}},
```

- Formula block

```tex
\displaystyle b_{0}
```

- Formula block

```tex
\displaystyle b_{2}
```


Local metadata:
- Keywords: asymptotic approximations of integrals , method of steepest descents , saddle points
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `I(z)` : contour integral , `p(t)` : analytic function and `q(t)` : analytic function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\sim` : Poincar asymptotic expansion , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `a` : left endpoint , `b` : right endpoint , `p(t)` : analytic function and `q(t)` : analytic function
- Symbols: `b` : right endpoint , `p(t)` : analytic function and `q(t)` : analytic function

### 2.4(v) Coalescing Saddle Points: Chester, Friedman, and Ursell's Method

- Consider the integral
- in which `z` is a large real or complex parameter, `p(\alpha,t)` and `q(\alpha,t)` are analytic functions of `t` and continuous in `t` and a second parameter `\alpha` . Suppose that on the integration path `\mathscr{P}` there are two simple zeros of `\ifrac{\partial p(\alpha,t)}{\partial t}` that coincide for a certain value `\widehat{\alpha}` of `\alpha` . The problem of obtaining an asymptotic approximation to `I(\alpha,z)` that is uniform with respect to `\alpha` in a region containing `\widehat{\alpha}` is similar to the problem of a coalescing endpoint and saddle point outlined in  2.3(v) .
- The change of integration variable is given by
- with `a` and `b` chosen so that the zeros of `\ifrac{\partial p(\alpha,t)}{\partial t}` correspond to the zeros `w_{1}(\alpha),w_{2}(\alpha)` , say, of the quadratic `w^{2}+2aw+b` . Then
- where `\mathscr{Q}` is the `w` -map of `\mathscr{P}` , and
- The function `f(\alpha,w)` is analytic at `w=w_{1}(\alpha)` and `w=w_{2}(\alpha)` when `\alpha\neq\widehat{\alpha}` , and at the confluence of these points when `\alpha=\widehat{\alpha}` . For large `|z|` , `I(\alpha,z)` is approximated uniformly by the integral that corresponds to ( 2.4.19 ) when `f(\alpha,w)` is replaced by a constant. By making a further change of variable

Formula blocks:
- Formula block (2.4.17)

```tex
I(\alpha,z)=\int_{\mathscr{P}}e^{-zp(\alpha,t)}q(\alpha,t)\,\mathrm{d}t
```

- Formula block (2.4.18)

```tex
p(\alpha,t)=\tfrac{1}{3}w^{3}+aw^{2}+bw+c,
```

- Formula block (2.4.19)

```tex
I(\alpha,z)=e^{-cz}\int_{\mathscr{Q}}\exp\left(-z\left(\tfrac{1}{3}w^{3}+aw^{2% }+bw\right)\right)f(\alpha,w)\,\mathrm{d}w,
```

- Formula block (2.4.20)

```tex
f(\alpha,w)=q(\alpha,t)\frac{\mathrm{d}t}{\mathrm{d}w}=q(\alpha,t)\frac{w^{2}+% 2aw+b}{\ifrac{\partial p(\alpha,t)}{\partial t}}.
```

- Formula block (2.4.21)

```tex
w=z^{-1/3}v-a,
```


Local metadata:
- Keywords: Chester-Friedman-Ursell method , asymptotic approximations of integrals , coalescing , coalescing critical points , coalescing saddle points , saddle points
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `\mathscr{P}` : contour , `p(t)` : analytic function , `q(t)` : analytic function and `I(\alpha,z)` : integral
- Symbols: `p(t)` : analytic function , `w` : change of variable , `a` , `b` and `c` : real constant
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\int` : integral , `I(\alpha,z)` : integral , `w` : change of variable , `a` , `b` , `\mathscr{Q}` : countour , `f(\alpha,w)` : function and `c` : real constant
- Symbols: `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\frac{\partial\NVar{f}}{\partial\NVar{x}}` : partial derivative of `f` with respect to `x` , `\,\partial\NVar{x}` : partial differential of `x` , `p(t)` : analytic function , `q(t)` : analytic function , `w` : change of variable , `a` , `b` and `f(\alpha,w)` : function
- Symbols: `w` : change of variable and `a`

### 2.4(vi) Other Coalescing Critical Points

- The problems sketched in  2.3(v) and 2.4(v) involve only two of many possibilities for the coalescence of endpoints, saddle points, and singularities in integrals associated with the special functions. For a coalescing saddle point and a pole see Wong ( 1989 , Chapter 7) and van der Waerden ( 1951 ) ; in this case the uniform approximants are complementary error functions. For a coalescing saddle point and endpoint see Olver ( 1997b , Chapter 9) and Wong ( 1989 , Chapter 7) ; if the endpoint is an algebraic singularity then the uniform approximants are parabolic cylinder functions with fixed parameter, and if the endpoint is not a singularity then the uniform approximants are complementary error functions.
- For two coalescing saddle points and an endpoint see Leubner and Ritsch ( 1986 ) . For two coalescing saddle points and an algebraic singularity see Temme ( 1986 ) , Jin and Wong ( 1998 ) . For a coalescing saddle point, a pole, and a branch point see Ciarkowski ( 1989 ) . For many coalescing saddle points see  36.12 . For double integrals with two coalescing stationary points see Qiu and Wong ( 2000 ) . See also Khwaja and Olde Daalhuis ( 2013 ) and Temme ( 2015 ) .

Local metadata:
- Keywords: asymptotic approximations of integrals , coalescing critical points
