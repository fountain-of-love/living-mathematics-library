# §2.1 Definitions and Elementary Properties

Source: [https://dlmf.nist.gov/2.1](https://dlmf.nist.gov/2.1)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.1. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Asymptotic and Order Symbols
- Integration and Differentiation
- Asymptotic Expansions
- Uniform Asymptotic Expansions
- Generalized Asymptotic Expansions

## Source Notes

- See Olver ( 1997b , pp. 4-8) .
- See Olver ( 1997b , pp. 8-11) .
- See Olver ( 1997b , pp. 16-22) .
- See Olver ( 1997b , pp. 24-27) .

## Keywords

asymptotic and order symbols, definition, Ritt's theorem, differentiation, differentiation of asymptotic approximations, integration, Poincar type, algebraic operations, asymptotic approximations and expansions, logarithms of, null, powers of, substitution of, uniqueness, uniform, asymptotic scale or sequence, generalized

## Principal Formula Blocks

- Formula block (2.1.1)

```tex
\displaystyle f(x)\sim\phi(x)
```

- Formula block (2.1.2)

```tex
\displaystyle f(x)=o\left(\phi(x)\right)
```

- Formula block (2.1.3)

```tex
\displaystyle f(x)=O\left(\phi(x)\right)
```

- Formula block (2.1.4)

```tex
\tanh x\sim x,
```

- Formula block (2.1.5)

```tex
e^{-x}=o\left(1\right),
```

- Formula block (2.1.6)

```tex
\sin\left(\pi x+x^{-1}\right)=O\left(x^{-1}\right),
```

- Formula block (2.1.7)

```tex
e^{ix}=O\left(1\right),
```

- Formula block (2.1.8)

```tex
\sum_{s=n}^{\infty}a_{s}z^{s}=O\left(z^{n}\right),
```

- Formula block (2.1.9)

```tex
e^{z}=1+z+O\left(z^{2}\right),
```

- Formula block

```tex
\displaystyle o\left(\phi\right)
```

- Formula block

```tex
\displaystyle o\left(\phi\right)+o\left(\phi\right)
```

- Formula block (2.1.11)

```tex
\displaystyle\int_{x}^{\infty}f(t)\,\mathrm{d}t
```

- Formula block (2.1.12)

```tex
\displaystyle\int f(x)\,\mathrm{d}x
```

- Formula block (2.1.13)

```tex
f(x)=\sum_{s=0}^{n-1}a_{s}x^{-s}+O\left(x^{-n}\right)
```

- Formula block (2.1.14)

```tex
f(x)\sim a_{0}+a_{1}x^{-1}+a_{2}x^{-2}+\cdots,
```

- Formula block (2.1.15)

```tex
x^{n}\left(f(x)-\sum_{s=0}^{n-1}a_{s}x^{-s}\right)\to a_{n},
```

- Formula block (2.1.16)

```tex
f(x)\sim a_{0}+a_{1}(x-c)+a_{2}(x-c)^{2}+\cdots,
```

- Formula block (2.1.17)

```tex
0+0\cdot z^{-1}+0\cdot z^{-2}+\cdots,
```

- Formula block

```tex
\left|x^{n}\left(f(u,x)-\sum_{s=0}^{n-1}a_{s}(u)x^{-s}\right)\right|
```

- Formula block (2.1.18)

```tex
f(u,x)\sim\sum_{s=0}^{\infty}a_{s}(u)x^{-s}
```

- Formula block (2.1.19)

```tex
\phi_{s+1}(x)=o\left(\phi_{s}(x)\right),
```

- Formula block (2.1.20)

```tex
f(x)=\sum_{s=0}^{n-1}f_{s}(x)+O\left(\phi_{n}(x)\right),
```

- Formula block (2.1.21)

```tex
f(x)\sim\sum_{s=0}^{\infty}f_{s}(x);\;\;\{\phi_{s}(x)\},
```


## Definitions and Symbols

- Keywords: asymptotic and order symbols , definition
- Defines: `\sim` : asymptotic equality
- Defines: `o\left(\NVar{x}\right)` : order less than
- Defines: `O\left(\NVar{x}\right)` : order not exceeding
- Symbols: `\sim` : asymptotic equality , `\mathbb{C}` : complex plane and `\tanh\NVar{z}` : hyperbolic tangent function
- Symbols: `\mathrm{e}` : base of natural logarithm , `o\left(\NVar{x}\right)` : order less than and `\mathbb{R}` : real line
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathbb{Z}` : set of all integers and `\sin\NVar{z}` : sine function
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\in` : element of , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `\mathbb{R}` : real line
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathbb{C}` : complex plane , `a_{s}` : coefficients and `n` : nonnegative integer
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathbb{C}` : complex plane and `\mathrm{e}` : base of natural logarithm
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding and `o\left(\NVar{x}\right)` : order less than
- Keywords: Ritt's theorem , asymptotic and order symbols , differentiation , differentiation of asymptotic approximations , integration
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\Re` : real part , `f(x)` : continuous function and `\nu` : complex constant
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function , `\Re` : real part , `f(x)` : continuous function and `\nu` : complex constant
- Defines: `\sim` : Poincar asymptotic expansion
- Keywords: Poincar type , algebraic operations , asymptotic approximations and expansions , differentiation , integration , logarithms of , null , powers of , substitution of , uniqueness
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : function , `n` : nonnegative integer and `a_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `f(x)` : function , `\mathbf{X}` : unbounded set and `a_{s}` : coefficients
- Symbols: `f(x)` : function , `\mathbf{X}` : unbounded set , `n` : nonnegative integer and `a_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `f(x)` : function , `\mathbf{X}` : unbounded set , `c` : limit point and `a_{s}` : coefficients
- Keywords: asymptotic approximations and expansions , uniform
- Symbols: `\sim` : Poincar asymptotic expansion , `u` : parameter (or set) , `f(u,x)` : function and `a_{s}(u)` : coefficients
- Keywords: asymptotic approximations and expansions , asymptotic scale or sequence , generalized
- Symbols: `o\left(\NVar{x}\right)` : order less than , `\mathbf{X}` : point set , `c` : limit point and `\phi_{s}(x)` : sequence of functions
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathbf{X}` : point set , `c` : limit point , `\phi_{s}(x)` : sequence of functions , `f(x)` : function and `n` : nonnegative integer
- Symbols: `\mathbf{X}` : point set , `c` : limit point , `\phi_{s}(x)` : sequence of functions and `f(x)` : function

## Subsections

### 2.1(i) Asymptotic and Order Symbols

- Let `\mathbf{X}` be a point set with a limit point `c` . As `x\to c` in `\mathbf{X}`
- The symbol `O` can also apply to the whole set `\mathbf{X}` , and not just as `x\to c` .

Formula blocks:
- Formula block (2.1.1)

```tex
\displaystyle f(x)\sim\phi(x)
```

- Formula block (2.1.2)

```tex
\displaystyle f(x)=o\left(\phi(x)\right)
```

- Formula block (2.1.3)

```tex
\displaystyle f(x)=O\left(\phi(x)\right)
```

- Formula block (2.1.4)

```tex
\tanh x\sim x,
```

- Formula block (2.1.5)

```tex
e^{-x}=o\left(1\right),
```

- Formula block (2.1.6)

```tex
\sin\left(\pi x+x^{-1}\right)=O\left(x^{-1}\right),
```

- Formula block (2.1.7)

```tex
e^{ix}=O\left(1\right),
```

- Formula block (2.1.8)

```tex
\sum_{s=n}^{\infty}a_{s}z^{s}=O\left(z^{n}\right),
```

- Formula block (2.1.9)

```tex
e^{z}=1+z+O\left(z^{2}\right),
```

- Formula block

```tex
\displaystyle o\left(\phi\right)
```

- Formula block

```tex
\displaystyle o\left(\phi\right)+o\left(\phi\right)
```


Local metadata:
- Keywords: asymptotic and order symbols , definition
- Defines: `\sim` : asymptotic equality
- Defines: `o\left(\NVar{x}\right)` : order less than
- Defines: `O\left(\NVar{x}\right)` : order not exceeding
- Symbols: `\sim` : asymptotic equality , `\mathbb{C}` : complex plane and `\tanh\NVar{z}` : hyperbolic tangent function
- Symbols: `\mathrm{e}` : base of natural logarithm , `o\left(\NVar{x}\right)` : order less than and `\mathbb{R}` : real line
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathbb{Z}` : set of all integers and `\sin\NVar{z}` : sine function
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\in` : element of , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `\mathbb{R}` : real line
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathbb{C}` : complex plane , `a_{s}` : coefficients and `n` : nonnegative integer
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathbb{C}` : complex plane and `\mathrm{e}` : base of natural logarithm
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding and `o\left(\NVar{x}\right)` : order less than

### 2.1(ii) Integration and Differentiation

- Integration of asymptotic and order relations is permissible, subject to obvious convergence conditions. For example, suppose `f(x)` is continuous and `f(x)\sim x^{\nu}` as `x\to+\infty` in `\mathbb{R}` , where `\nu` ( `\in\mathbb{C}` ) is a constant. Then
- Differentiation requires extra conditions. For example, if `f(z)` is analytic for all sufficiently large `|z|` in a sector `\mathbf{S}` and `f(z)=O\left(z^{\nu}\right)` as `z\to\infty` in `\mathbf{S}` , `\nu` being real, then `f^{\prime}(z)=O\left(z^{\nu-1}\right)` as `z\to\infty` in any closed sector properly interior to `\mathbf{S}` and with the same vertex ( Ritt's theorem ). This result also holds with both `O` 's replaced by `o` 's.

Formula blocks:
- Formula block (2.1.11)

```tex
\displaystyle\int_{x}^{\infty}f(t)\,\mathrm{d}t
```

- Formula block (2.1.12)

```tex
\displaystyle\int f(x)\,\mathrm{d}x
```


Local metadata:
- Keywords: Ritt's theorem , asymptotic and order symbols , differentiation , differentiation of asymptotic approximations , integration
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\Re` : real part , `f(x)` : continuous function and `\nu` : complex constant
- Symbols: `\sim` : asymptotic equality , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function , `\Re` : real part , `f(x)` : continuous function and `\nu` : complex constant

### 2.1(iii) Asymptotic Expansions

- Let `\sum a_{s}x^{-s}` be a formal power series (convergent or divergent) and for each positive integer `n` ,
- as `x\to\infty` in an unbounded set `\mathbf{X}` in `\mathbb{R}` or `\mathbb{C}` . Then `\sum a_{s}x^{-s}` is a Poincar asymptotic expansion , or simply asymptotic expansion , of `f(x)` as `x\to\infty` in `\mathbf{X}` . Symbolically,
- Condition ( 2.1.13 ) is equivalent to
- for each `n=0,1,2,\dots` . If `\sum a_{s}x^{-s}` converges for all sufficiently large `|x|` , then it is automatically the asymptotic expansion of its sum as `x\to\infty` in `\mathbb{C}` .
- If `c` is a finite limit point of `\mathbf{X}` , then
- means that for each `n` , the difference between `f(x)` and the `n` th partial sum on the right-hand side is `O\left((x-c)^{n}\right)` as `x\to c` in `\mathbf{X}` .

Formula blocks:
- Formula block (2.1.13)

```tex
f(x)=\sum_{s=0}^{n-1}a_{s}x^{-s}+O\left(x^{-n}\right)
```

- Formula block (2.1.14)

```tex
f(x)\sim a_{0}+a_{1}x^{-1}+a_{2}x^{-2}+\cdots,
```

- Formula block (2.1.15)

```tex
x^{n}\left(f(x)-\sum_{s=0}^{n-1}a_{s}x^{-s}\right)\to a_{n},
```

- Formula block (2.1.16)

```tex
f(x)\sim a_{0}+a_{1}(x-c)+a_{2}(x-c)^{2}+\cdots,
```

- Formula block (2.1.17)

```tex
0+0\cdot z^{-1}+0\cdot z^{-2}+\cdots,
```


Local metadata:
- Defines: `\sim` : Poincar asymptotic expansion
- Keywords: Poincar type , algebraic operations , asymptotic approximations and expansions , differentiation , integration , logarithms of , null , powers of , substitution of , uniqueness
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : function , `n` : nonnegative integer and `a_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `f(x)` : function , `\mathbf{X}` : unbounded set and `a_{s}` : coefficients
- Symbols: `f(x)` : function , `\mathbf{X}` : unbounded set , `n` : nonnegative integer and `a_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `f(x)` : function , `\mathbf{X}` : unbounded set , `c` : limit point and `a_{s}` : coefficients

### 2.1(iv) Uniform Asymptotic Expansions

- If the set `\mathbf{X}` in  2.1(iii) is a closed sector `\alpha\leq\operatorname{ph}x\leq\beta` , then by definition the asymptotic property ( 2.1.13 ) holds uniformly with respect to `\operatorname{ph}x\in[\alpha,\beta]` as `|x|\to\infty` . The asymptotic property may also hold uniformly with respect to parameters. Suppose `u` is a parameter (or set of parameters) ranging over a point set (or sets) `\mathbf{U}` , and for each nonnegative integer `n`
- is bounded as `x\to\infty` in `\mathbf{X}` , uniformly for `u\in\mathbf{U}` . (The coefficients `a_{s}(u)` may now depend on `u` .) Then
- as `x\to\infty` in `\mathbf{X}` , uniformly with respect to `u\in\mathbf{U}` .
- Similarly for finite limit point `c` in place of `\infty` .

Formula blocks:
- Formula block

```tex
\left|x^{n}\left(f(u,x)-\sum_{s=0}^{n-1}a_{s}(u)x^{-s}\right)\right|
```

- Formula block (2.1.18)

```tex
f(u,x)\sim\sum_{s=0}^{\infty}a_{s}(u)x^{-s}
```


Local metadata:
- Keywords: asymptotic approximations and expansions , uniform
- Symbols: `\sim` : Poincar asymptotic expansion , `u` : parameter (or set) , `f(u,x)` : function and `a_{s}(u)` : coefficients

### 2.1(v) Generalized Asymptotic Expansions

- Let `\phi_{s}(x)` , `s=0,1,2,\dots` , be a sequence of functions defined in `\mathbf{X}` such that for each `s`
- where `c` is a finite, or infinite, limit point of `\mathbf{X}` . Then `\{\phi_{s}(x)\}` is an asymptotic sequence or scale . Suppose also that `f(x)` and `f_{s}(x)` satisfy
- for `n=0,1,2,\dots` . Then `\sum f_{s}(x)` is a generalized asymptotic expansion of `f(x)` with respect to the scale `\{\phi_{s}(x)\}` . Symbolically,
- As in  2.1(iv) , generalized asymptotic expansions can also have uniformity properties with respect to parameters. For an example see  14.15(i) .
- Care is needed in understanding and manipulating generalized asymptotic expansions. Many properties enjoyed by Poincar expansions (for example, multiplication) do not always carry over. It can even happen that a generalized asymptotic expansion converges, but its sum is not the function being represented asymptotically; for an example see  18.15(iii) .

Formula blocks:
- Formula block (2.1.19)

```tex
\phi_{s+1}(x)=o\left(\phi_{s}(x)\right),
```

- Formula block (2.1.20)

```tex
f(x)=\sum_{s=0}^{n-1}f_{s}(x)+O\left(\phi_{n}(x)\right),
```

- Formula block (2.1.21)

```tex
f(x)\sim\sum_{s=0}^{\infty}f_{s}(x);\;\;\{\phi_{s}(x)\},
```


Local metadata:
- Keywords: asymptotic approximations and expansions , asymptotic scale or sequence , generalized
- Symbols: `o\left(\NVar{x}\right)` : order less than , `\mathbf{X}` : point set , `c` : limit point and `\phi_{s}(x)` : sequence of functions
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathbf{X}` : point set , `c` : limit point , `\phi_{s}(x)` : sequence of functions , `f(x)` : function and `n` : nonnegative integer
- Symbols: `\mathbf{X}` : point set , `c` : limit point , `\phi_{s}(x)` : sequence of functions and `f(x)` : function
