# Harmonic And Prime Reciprocal Series

This page compares two infinite sums made from reciprocals:

- the harmonic series, which uses all positive integers;
- the prime reciprocal series, which uses only prime numbers.

Both sums diverge to infinity.

Navigation:

- Formula registry: [Formula Registry](../notes/formula-registry.md)
- Related concept page: [Mathematical Fundamentals](../mathematical-ontology/Mathematical%20fundamentals.md#divergent-series)
- Related bond page: [Divergence, Partial Sums, And Indeterminate Quotients](../formula-bonds/divergence-partial-sums-and-indeterminate-quotients.md)

---

## 1. If The Denominator Runs Over All Positive Integers

If the denominator represents all positive integers, the sum is the harmonic series:

$$
\sum_{n=1}^{\infty}\frac{1}{n}
=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots.
$$

This series diverges:

$$
\sum_{n=1}^{\infty}\frac{1}{n}=\infty.
$$

The terms get smaller, but they do not shrink fast enough for the total sum to settle
on a finite number.

---

## 2. If The Denominator Runs Over Prime Numbers

If the denominator represents only prime numbers, the sum becomes:

$$
\sum_{p\text{ prime}}\frac{1}{p}
=\frac{1}{2}+\frac{1}{3}+\frac{1}{5}+\frac{1}{7}+\cdots.
$$

This series also diverges:

$$
\sum_{p\text{ prime}}\frac{1}{p}=\infty.
$$

This is a theorem of Euler. Even though prime numbers become scarcer as they get
larger, their reciprocals still add up without bound.

---

## 3. What To Notice

Both examples show the same basic lesson:

```text
terms going to zero is necessary for convergence,
but it is not enough.
```

For an infinite sum to converge, the terms must shrink fast enough. The terms
`1/n` shrink to zero, and the prime reciprocals also shrink to zero, but both sums
still grow beyond every finite bound.

The useful question is not only:

```text
Do the terms get smaller?
```

but:

```text
How fast do the terms get smaller?
```
