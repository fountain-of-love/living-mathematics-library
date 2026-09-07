# Series That Sum To One

The reciprocal terms `1/n` do not add up to exactly `1` as a standard infinite series.
The harmonic series diverges instead. But related series can equal `1` if we change the
terms, the signs, or the operation.

Navigation:

- Formula registry: [Formula Registry](../formula-registry.md)
- Related page: [Harmonic And Prime Reciprocal Series](harmonic-and-prime-reciprocal-series.md)
- Related bond page: [Divergence, Partial Sums, And Indeterminate Quotients](../formula-bonds/divergence-partial-sums-and-indeterminate-quotients.md)

---

## 1. Geometric Series

A classic infinite sum that equals `1` is:

$$
\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n
=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\cdots
=1.
$$

Here each term is half the previous term. The terms shrink fast enough that the total
approaches exactly `1`.

---

## 2. Alternating Harmonic Series

If the harmonic series is given alternating signs, it no longer diverges to infinity:

$$
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}
=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots.
$$

This converges to:

$$
\ln(2)\approx0.693.
$$

This is finite and close to `1`, but it is not equal to `1`.

---

## 3. Partial Sums

The ordinary harmonic series does not become exactly `1` as an infinite sum:

$$
1+\frac{1}{2}+\frac{1}{3}+\cdots.
$$

But its first partial sum is exactly:

$$
1.
$$

After the second term, it has already passed `1`:

$$
1+\frac{1}{2}=1.5.
$$

So the harmonic series starts at `1`, then keeps growing without bound.

---

## 4. Telescoping Series

A related series of unit fractions can sum to exactly `1`:

$$
\sum_{n=1}^{\infty}\frac{1}{n(n+1)}
=\frac{1}{2}+\frac{1}{6}+\frac{1}{12}+\frac{1}{20}+\cdots
=1.
$$

The reason is that:

$$
\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}.
$$

So the sum becomes:

$$
\left(1-\frac{1}{2}\right)
+\left(\frac{1}{2}-\frac{1}{3}\right)
+\left(\frac{1}{3}-\frac{1}{4}\right)
+\cdots.
$$

Most neighboring terms cancel. That cancellation is called telescoping.

---

## 5. What To Notice

Getting a total of `1` depends on the structure of the series:

- geometric shrinking can converge to `1`;
- alternating signs can turn divergence into finite convergence;
- stopping at a finite partial sum changes the question;
- telescoping terms can cancel almost everything.

The symbol `1/n` by itself is not enough to decide the total. The operation, signs,
indexing, and stopping rule all matter.
