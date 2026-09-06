# Taylor Series

A Taylor series, sometimes called a Taylor sequence in informal language, is an
infinite sum of terms used to write a difficult function as a simpler polynomial. It
uses the values of the function's derivatives at a single point.

Navigation:

- Formula registry: [Formula Registry](../notes/formula-registry.md)
- Related concept page: [Mathematical Fundamentals](../mathematical-ontology/Mathematical%20fundamentals.md#taylor-series)

---

## 1. Observation

A Taylor series lets us study a function by zooming in around one chosen point. At that
point, we measure:

- the function's value;
- its slope;
- how its slope changes;
- how those changes keep changing.

Those measurements are the derivatives of the function at that point. The Taylor series
uses them to build a polynomial that behaves like the original function near the chosen
point.

The key idea is:

```text
local derivative information -> polynomial approximation
```

---

## 2. Formula

For a sufficiently well-behaved function near the point `a`, the Taylor series is:

$$
f(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\frac{f'''(a)}{3!}(x-a)^3+\cdots.
$$

More compactly:

$$
f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n.
$$

Here:

- `a` is the point where the function is inspected.
- `f(a)` is the function value at that point.
- `f'(a)`, `f''(a)`, and higher derivatives describe increasingly fine local behavior.
- `n!` means factorial, for example `3! = 3 x 2 x 1 = 6`.

---

## 3. Special Case: Maclaurin Series

When the chosen point is:

$$
a=0,
$$

the Taylor series is called a Maclaurin series:

$$
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots.
$$

This is the same idea, but centered at zero.

---

## 4. Example

For the exponential function:

$$
f(x)=e^x,
$$

every derivative is again `e^x`. At `a = 0`, each derivative has value `1`, because:

$$
e^0=1.
$$

So the Maclaurin series becomes:

$$
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\cdots.
$$

This turns the exponential function into an infinite polynomial.

---

## 5. What To Notice

A Taylor series is local. It is built from what happens at one point, then used to
understand nearby values.

That makes it different from an asymptotic formula. A Taylor series usually describes
behavior near a chosen point, while an asymptotic formula often describes behavior far
away, such as near infinity.

So the Taylor series is a method for turning local change into a usable polynomial
description.
