# L'Hopital's Rule

L'Hopital's rule is a calculus method for evaluating limits that first appear as
indeterminate quotients, especially:

$$
\frac{0}{0}
\qquad\text{or}\qquad
\frac{\infty}{\infty}.
$$

It works by comparing the rates of change of the numerator and denominator.

Navigation:

- Formula registry: [Formula Registry](../notes/formula-registry.md)
- Related concept page: [Mathematical Fundamentals](../mathematical-ontology/Mathematical%20fundamentals.md#indeterminate-form)
- Related bond page: [Divergence, Partial Sums, And Indeterminate Quotients](../formula-bonds/divergence-partial-sums-and-indeterminate-quotients.md)

---

## 1. Observation

An expression such as:

$$
\frac{\infty}{\infty}
$$

does not automatically equal `1`, and it does not automatically equal infinity. It is
an indeterminate form, meaning the expression does not determine one answer by itself.

Different growth rates can produce different limits.

---

## 2. Formula

If direct substitution gives:

$$
\frac{0}{0}
$$

or:

$$
\frac{\pm\infty}{\pm\infty},
$$

then, under the usual differentiability conditions:

$$
\lim_{x\to c}\frac{f(x)}{g(x)}
=
\lim_{x\to c}\frac{f'(x)}{g'(x)}.
$$

This means we compare the derivative of the top function with the derivative of the
bottom function.

---

## 3. Growth-Rate Example

Consider:

$$
\lim_{x\to\infty}\frac{5x}{x}.
$$

Both the top and the bottom grow to infinity, so direct substitution has the shape:

$$
\frac{\infty}{\infty}.
$$

L'Hopital's rule compares their derivatives:

$$
\frac{d}{dx}(5x)=5,
\qquad
\frac{d}{dx}(x)=1.
$$

So:

$$
\lim_{x\to\infty}\frac{5x}{x}
=
\lim_{x\to\infty}\frac{5}{1}
=5.
$$

Even though both functions go to infinity, the numerator grows five times as fast as
the denominator.

---

## 4. Requirements

Use L'Hopital's rule only when:

- the limit first has the form `0/0` or `infinity/infinity`;
- the numerator and denominator are differentiable near the limiting point;
- the derivative of the denominator is not zero near the limiting point;
- the new derivative quotient has a limit, or can be analyzed further.

It is not a general instruction to differentiate every fraction. If a limit is already
ordinary, using the rule can give the wrong result.

---

## 5. What To Notice

L'Hopital's rule turns a question about size into a question about speed:

```text
Which function grows faster?
```

That is why it is useful for expressions that look like `infinity/infinity`. The
symbolic shape alone is not the answer. The growth rates decide the limit.
