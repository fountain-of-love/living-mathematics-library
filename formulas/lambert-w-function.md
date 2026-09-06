# Lambert W Function

The Lambert W function is the function that answers a very specific inverse question:

> If a quantity appears both outside and inside an exponential, how can we solve for it?

It is written as `W`, and it is defined implicitly by

$$
W(z)e^{W(z)}=z.
$$

This page focuses especially on the second real branch, usually written as
`W_{-1}`.

Navigation:

- Formula registry: [Formula Registry](../notes/formula-registry.md)
- Related concept page: [Binet's Formula, Euler's Number, And Number-System Extension](../formula-bonds/binet-euler-number-systems.md)
- Related source note: [Omega as process invariant](constants-as-process-invariants-proposal.md#additional-relevant-signatures)

---

## 0. What To Notice First

Some equations are easy to undo.

If

$$
y=x+3,
$$

then subtract `3`.

If

$$
y=x^2,
$$

then take a square root, with attention to signs.

If

$$
y=e^x,
$$

then take a logarithm.

But the Lambert W function appears when the unknown is entangled in two places:

$$
x e^x.
$$

The unknown is both a multiplier and an exponent. Ordinary logarithms do not isolate it
by themselves.

So Lambert W is an inverse function for the map:

```text
w
  -> w e^w
```

That is the whole seed of the idea.

---

## 1. Definition

The Lambert W function is defined by:

$$
\boxed{W(z)e^{W(z)}=z}.
$$

Equivalently, if

$$
w e^w=z,
$$

then

$$
w=W(z).
$$

This makes `W` the inverse of the function

$$
f(w)=w e^w.
$$

**Observation checkpoint**

The definition does not give `W(z)` by elementary arithmetic. It tells us which value
`W(z)` must be: the number that, when multiplied by its own exponential, returns `z`.

That is why Lambert W appears in problems where growth feeds back into the quantity
being solved for.

---

## 2. Why Branches Appear

For some functions, each input has only one output. But inverse functions can become
multivalued when the original function folds over itself.

The function

$$
f(w)=w e^w
$$

is not one-to-one over all real `w`.

Its derivative is

$$
f'(w)=e^w(w+1).
$$

So the derivative is zero at

$$
w=-1.
$$

At that point,

$$
f(-1)=-\frac1e.
$$

This is the branch point where the two real branches meet.

**What this reflects**

The graph of `w e^w` has a lowest real value at `w = -1`. To the right of `-1`, the
function rises toward `0` and then to infinity. To the left of `-1`, the function also
rises toward `0`, but from negative values of `w` going toward negative infinity.

That creates two possible real `w` values for many negative inputs.

Put differently:

```text
the lower branch exists because w e^w turns around
```

If `w e^w` were one-to-one, its inverse would have only one real branch. The derivative
shows exactly where the turn happens.

---

<a id="lambert-w-real-branches"></a>

## 3. The Two Real Branches

For real `x`, there are two real branches when

$$
-\frac1e\le x<0.
$$

They are:

$$
W_0(x)\in[-1,0)
$$

and

$$
\boxed{W_{-1}(x)\in(-\infty,-1]}.
$$

Both branches satisfy the same defining equation:

$$
W_0(x)e^{W_0(x)}=x,
$$

and

$$
\boxed{W_{-1}(x)e^{W_{-1}(x)}=x}.
$$

So there is no separate elementary equation defining the second real branch. The branch
name tells us **which solution** of the same implicit equation we choose.

Elements at a glance:

| Branch | Real domain | Real range | Meaning |
|---|---|---|---|
| `W_0` | `[-1/e, infinity)` | `[-1, infinity)` | Principal real branch |
| `W_{-1}` | `[-1/e, 0)` | `(-infinity, -1]` | Lower real branch |

---

<a id="lambert-w-second-real-branch"></a>

## 4. The Second Real Branch `W_{-1}`

The branch `W_{-1}` is the real branch that stays at or below `-1`.

It answers:

> Which solution `w <= -1` satisfies `w e^w = x`?

For

$$
-\frac1e<x<0,
$$

there are two real answers to `w e^w = x`:

- one answer lies between `-1` and `0`;
- the other lies below `-1`.

The first is `W_0(x)`. The second is `W_{-1}(x)`.

At the shared endpoint,

$$
W_0(-1/e)=W_{-1}(-1/e)=-1.
$$

**Observation checkpoint**

The subscript `-1` does not mean "take the reciprocal" or "subtract one". It is a
branch label. It names the lower real branch of a multivalued inverse.

**Concrete example**

At

$$
x=-0.1,
$$

there are two real solutions:

$$
W_0(-0.1)\approx -0.1118
$$

and

$$
W_{-1}(-0.1)\approx -3.5772.
$$

Both satisfy the same defining equation:

$$
(-0.1118)e^{-0.1118}\approx-0.1
$$

and

$$
(-3.5772)e^{-3.5772}\approx-0.1.
$$

The first value lies on the upper/principal branch. The second value lies on the
lower branch.

So the most useful definition of the lower real branch is:

$$
\boxed{
W_{-1}(x)
=
\text{the solution }w\le -1\text{ of }we^w=x,
\qquad -1/e\le x<0.
}
$$

---

<a id="lambert-w-parametric-example"></a>

## 5. A Clean Parametric Example

A useful way to build exact examples is to choose the output first.

Set

$$
w=-a
$$

with

$$
a\ge1.
$$

Then

$$
w e^w=(-a)e^{-a}=-ae^{-a}.
$$

Therefore

$$
\boxed{W_{-1}(-ae^{-a})=-a}
$$

for

$$
a\ge1.
$$

For example, choose

$$
a=2.
$$

Then

$$
x=-2e^{-2}=-\frac2{e^2}.
$$

And

$$
W_{-1}\left(-\frac2{e^2}\right)=-2.
$$

This is the corrected version of a common near-example. If one chooses

$$
x=-\frac1{e^2},
$$

then `w = -2` does not work, because

$$
(-2)e^{-2}=-\frac2{e^2},
$$

not

$$
-\frac1{e^2}.
$$

The parameter form avoids the slip: choose the desired `w = -a`, then compute
`x = -ae^{-a}`.

---

<a id="lambert-w-branch-point"></a>

## 6. The Branch Point `(-1/e, -1)`

The point where the two real branches meet is

$$
\boxed{\left(-\frac1e,-1\right)}.
$$

Here the horizontal coordinate is the input

$$
x=-\frac1e,
$$

and the vertical coordinate is the output

$$
w=-1.
$$

To calculate it, start from the defining relation

$$
x=w e^w.
$$

The turning point occurs where

$$
\frac{dx}{dw}=0.
$$

Differentiate:

$$
\frac{dx}{dw}=e^w(1+w).
$$

Set this equal to zero:

$$
e^w(1+w)=0.
$$

Since

$$
e^w\ne0,
$$

we must have

$$
1+w=0,
$$

so

$$
w=-1.
$$

Then substitute into `x = w e^w`:

$$
x=(-1)e^{-1}=-\frac1e.
$$

Therefore the branch point is

$$
\boxed{(x,w)=\left(-\frac1e,-1\right)}.
$$

**Observation checkpoint**

This point is not chosen by convention. It is forced by the geometry of `w e^w`: the
function reaches its real minimum there, so the inverse branches meet there.

---

## 7. What Lambert W Solves

Lambert W solves equations where the unknown appears in a product with its own
exponential.

A simple pattern is:

$$
y=x e^x.
$$

Then

$$
x=W(y).
$$

A slightly disguised pattern is:

$$
u e^u = c.
$$

Then

$$
u=W(c).
$$

Many applied equations can be rearranged into this form: delay equations, growth with
feedback, diode equations, combinatorics, asymptotic inversions, and certain probability
or physics problems.

**Day-to-day analogy**

Logarithms undo exponentials. Square roots undo squaring. Lambert W undoes a specific
kind of self-amplifying expression:

```text
the value times its own exponential
```

That is why it often appears when "growth" and "the thing growing" are algebraically
entangled.

---

<a id="omega-constant"></a>

## 8. Relation To The Omega Constant

The Omega constant is the solution of

$$
\Omega e^\Omega=1.
$$

Using Lambert W notation, this is simply:

$$
\Omega=W(1).
$$

Numerically,

$$
\Omega\approx0.567143\ldots
$$

This is a useful companion example because it shows the same fixed-point pattern:

```text
value
  -> value times its own exponential
  -> prescribed result
```

Related note: [Additional Relevant Signatures](constants-as-process-invariants-proposal.md#additional-relevant-signatures).

---

## 9. What Not To Overclaim

Lambert W is powerful, but the branch structure matters.

First, `W(z)` is not always a single real-valued function. Over the complex plane, it
has branches

$$
W_k(z),
\qquad k\in\mathbb Z.
$$

Second, the branch `W_{-1}` is not the same as the complex branch `W_1`. The notation
`W_{-1}` specifically names the lower real branch on the interval

$$
-\frac1e\le x<0.
$$

Third, when solving real-world equations, choosing the wrong branch can select the
wrong solution. The equation may be algebraically correct while the interpretation is
wrong.

So the precise statement is:

> The second real Lambert W branch, `W_{-1}`, is the lower real solution branch of
> `w e^w = x` for `-1/e <= x < 0`.

---

## 10. Big Picture

The compact bond is:

$$
\boxed{
\text{unknown in base and exponent}
\longrightarrow
w e^w
\longrightarrow
W
\longrightarrow
\text{branch choice}
}
$$

Lambert W belongs to the family of inverse functions:

| Expression | Inverse idea |
|---|---|
| `x + a` | subtract `a` |
| `x^2` | square root, with sign choices |
| `e^x` | logarithm |
| `x e^x` | Lambert W, with branch choices |

After reading this page, the useful mental image is:

```text
Lambert W is the logarithm-like inverse for self-multiplied exponential growth
```

The second real branch `W_{-1}` is not a new equation. It is the lower real path through
the same equation.
