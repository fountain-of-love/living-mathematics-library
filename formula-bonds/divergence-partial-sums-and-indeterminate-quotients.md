# Divergence, Partial Sums, And Indeterminate Quotients

Guiding question:

> If two sums both grow without bound, can we divide them and simply get `1`?

The short answer is: only when we compare the same finite partial sum with itself, or
when a limit proves that the two growing quantities stay in the right proportion.

Navigation:

- Formula bonds overview: [Formula Bonds](README.md)
- Formula registry: [Formula Registry](../formula-registry.md)
- Source page: [Harmonic And Prime Reciprocal Series](../formulas/harmonic-and-prime-reciprocal-series.md)
- Source page: [Series That Sum To One](../formulas/series-that-sum-to-one.md)
- Source page: [L'Hopital's Rule](../formulas/lhopitals-rule.md)

---

## Elements At A Glance

| Element | Role |
|---|---|
| Harmonic series | Shows that shrinking terms can still add up without bound |
| Prime reciprocal series | Shows that even sparse denominators can still diverge |
| Partial sum | Turns an infinite process into a finite number |
| Indeterminate form | Warns that `infinity/infinity` has no automatic value |
| L'Hopital's rule | Compares growth rates through derivatives |

---

## 1. Divergence Is Not A Number

When we write:

$$
\sum_{n=1}^{\infty}\frac{1}{n}=\infty,
$$

we are not saying that the series equals a normal number called infinity. We are saying
that its partial sums grow beyond every finite bound.

The partial sums are:

$$
H_N=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{N}.
$$

For every fixed `N`, this is a finite number.

Observation checkpoint:

> Divergence describes the behavior of a process, not a finished finite value.

---

## 2. Dividing A Finite Partial Sum By Itself

For every fixed `N`:

$$
\frac{H_N}{H_N}=1.
$$

This is ordinary arithmetic. The numerator and denominator are the same finite number.

But this does not mean:

$$
\frac{\infty}{\infty}=1.
$$

The first expression is a finite identity. The second is an indeterminate symbolic
shape.

---

## 3. Why Infinity Over Infinity Is Indeterminate

The form:

$$
\frac{\infty}{\infty}
$$

does not decide a value by itself.

For example:

$$
\lim_{x\to\infty}\frac{x}{x}=1,
$$

but:

$$
\lim_{x\to\infty}\frac{5x}{x}=5,
$$

and:

$$
\lim_{x\to\infty}\frac{x}{x^2}=0.
$$

All three have the same rough shape, `infinity/infinity`, but the limits are different.
The answer depends on relative growth.

---

## 4. The Bond

The bond between these ideas is the move from object to process:

```text
finite partial sum -> growing sequence of partial sums -> limit comparison
```

At the finite level, identical quantities divide to `1`.

At the infinite-process level, the question becomes:

```text
Do these two growing processes grow at the same rate?
```

That is why a limit method, such as L'Hopital's rule for differentiable functions, is
needed in calculus. It does not treat infinity as a cancellable number. It studies how
the numerator and denominator approach their limiting behavior.

---

## 5. Final Mental Image

Think of divergence as two runners who never stop running. Saying both are "far away"
does not tell you whether one is twice as far, five times as far, or falling behind.

The ratio is not decided by the word "infinity". It is decided by the growth pattern.
