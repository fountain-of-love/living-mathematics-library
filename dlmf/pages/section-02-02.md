# §2.2 Transcendental Equations

Source: [https://dlmf.nist.gov/2.2](https://dlmf.nist.gov/2.2)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.2. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Source Notes

- See Olver ( 1997b , pp. 11-16) and Fabijonas and Olver ( 1999 ) .

## Keywords

asymptotic solutions, asymptotic solutions of transcendental equations, transcendental equations, Lagrange's formula, Lagrange's formula for reversion of series, asymptotic approximations and expansions, asymptotic approximations of integrals, reversion of, reversion of series

## Mathematical Narrative

- Let `f(x)` be continuous and strictly increasing when `a<x<\infty` and
- Then for `y>f(a)` the equation `f(x)=y` has a unique root `x=x(y)` in `(a,\infty)` , and

## Principal Formula Blocks

- Formula block (2.2.1)

```tex
f(x)\sim x,
```

- Formula block (2.2.2)

```tex
x(y)\sim y,
```

- Formula block (2.2.3)

```tex
t^{2}-\ln t=y.
```

- Formula block (2.2.4)

```tex
t=y^{\frac{1}{2}}\left(1+o\left(1\right)\right),
```

- Formula block (2.2.5)

```tex
t^{2}=y+\ln t=y+\tfrac{1}{2}\ln y+o\left(1\right),
```

- Formula block (2.2.6)

```tex
t=y^{\frac{1}{2}}\left(1+\tfrac{1}{4}y^{-1}\ln y+o\left(y^{-1}\right)\right),
```

- Formula block (2.2.7)

```tex
f(x)\sim x+f_{0}+f_{1}x^{-1}+f_{2}x^{-2}+\cdots,
```

- Formula block (2.2.8)

```tex
x\sim y-F_{0}-F_{1}y^{-1}-F_{2}y^{-2}-\cdots,
```


## Definitions and Symbols

- Keywords: asymptotic solutions , asymptotic solutions of transcendental equations , transcendental equations
- Symbols: `\sim` : asymptotic equality and `f(x)` : function
- Symbols: `\sim` : asymptotic equality and `y` : root
- Keywords: Lagrange's formula , Lagrange's formula for reversion of series , asymptotic approximations and expansions , asymptotic approximations of integrals , asymptotic solutions of transcendental equations , reversion of , reversion of series
- Symbols: `\ln\NVar{z}` : principal branch of logarithm function and `y` : root
- Symbols: `o\left(\NVar{x}\right)` : order less than and `y` : root
- Symbols: `o\left(\NVar{x}\right)` : order less than , `\ln\NVar{z}` : principal branch of logarithm function and `y` : root
- Symbols: `o\left(\NVar{x}\right)` : order less than , `\ln\NVar{z}` : principal branch of logarithm function and `y` : root
- Symbols: `\sim` : Poincar asymptotic expansion , `f(x)` : function and `f_{s}` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `y` : root and `F_{s}` : coefficients
