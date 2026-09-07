# Binet's Formula, Euler's Number, And Number-System Extension

This bond treats **Binet's formula**, the closed form for Fibonacci numbers, together
with Euler's number and Euler's formula.

The guiding question is:

> Why do formulas for simple counting processes sometimes require larger number systems
> than the process itself seems to use?

The connection is not simply that Binet's formula "uses real numbers". The deeper bond
is this:

```text
integer recurrence
  -> characteristic equation
  -> irrational roots
  -> closed form for integers

continuous change
  -> exponential function
  -> Euler's number
  -> complex rotation through Euler's formula
```

Binet's formula shows real numbers emerging from a discrete counting process. Euler's
formula shows the same exponential language extending further into complex numbers and
rotation.

Navigation:

- Bond overview: [Formula Bonds](README.md)
- Formula registry: [Formula Registry](../formula-registry.md)
- Registry entries: [Binet's formula](../formula-registry.md#fibonacci-farey-and-rational-approximation), [Euler's number](../formula-registry.md#constants-and-process-invariants), [Euler's formula](../formula-registry.md#constants-and-process-invariants), [Euler's identity](../formula-registry.md#constants-and-process-invariants)

How to read this page:

1. Start with the difference between stating a process and revealing its hidden shape.
2. Use Euler's number as the example of continuous growth.
3. Use Binet's formula as the example of an integer sequence explained by real modes.
4. Notice how exponential notation links repeated multiplication to continuous change.
5. Use Euler's formula as the next extension, where exponentials describe rotation.

Elements at a glance:

| Element | Plain meaning | What to watch for |
|---|---|---|
| Fibonacci recurrence | A two-memory integer process | Its closed form needs irrational roots |
| Binet's formula | A direct formula for Fibonacci numbers | Irrational parts cancel back into integers |
| Characteristic equation | Algebraic shadow of a recurrence | Its roots are the growth modes |
| Euler's number | The constant of self-proportional change | It appears when compounding becomes continuous |
| Exponential notation | Repeated scaling, extended beyond whole-number repetition | Powers such as `phi^n` can be read through `e` |
| Euler's formula | Exponential form of circular motion | It joins growth language with rotation language |
| Complex number | A number with two coordinated directions | It makes rotation algebraic |

---

## 0. What To Notice First

This page is about a recurring mathematical move:

```text
when the visible rule is simple,
the hidden structure may live in a larger number system
```

Fibonacci numbers look like ordinary counting numbers. You can generate them by adding
two previous integers. Nothing about the list seems to demand irrational numbers.

Continuous growth looks like ordinary increase. You can imagine money earning interest,
a population growing, a cooling object losing heat, or a probability curve changing
smoothly. But when change becomes continuous rather than step-by-step, the number `e`
appears naturally.

Rotation looks geometric. A hand turns on a clock, a wheel spins, a wave oscillates, a
point moves around a circle. Euler's formula shows that this rotational behavior can be
written using the exponential function, once complex numbers are allowed.

So the page follows one teaching thread:

```text
integers are enough to state the process;
larger number systems reveal why the process has its shape.
```

**Observation checkpoint**

The larger number system is not added for decoration. It is added because the original
number system cannot express the structure cleanly. Rationals cannot solve every square
root problem. Real numbers can describe rotation with sine and cosine, but complex
numbers make rotation behave like multiplication.

There is a second theme running underneath the page:

```text
repeated multiplication is discrete;
exponential functions extend repeated multiplication into a continuous language
```

That is why Binet's formula and Euler's number belong in the same conversation. Binet's
formula uses powers of `phi` and `psi`; Euler's number is the natural base of
exponential change. Even when `e` is not visibly written in Binet's formula, the
exponential idea is present.

---

## 1. Euler's Number

Euler's number belongs to the world of growth and change. It appears when a quantity
does not merely grow by fixed jumps, but grows in proportion to its current size.

In daily life, this is the difference between adding the same amount each month and
earning interest on an amount that is itself changing. The more frequently the interest
is compounded, the closer the process moves toward continuous growth.

Euler's number is the real number

$$
e \approx 2.718281828459045\ldots
$$

One defining limit is

$$
e=\lim_{n\to\infty}\left(1+\frac1n\right)^n.
$$

The sequence begins:

$$
\left(1+\frac11\right)^1=2,
$$

$$
\left(1+\frac12\right)^2=2.25,
$$

$$
\left(1+\frac13\right)^3\approx2.370,
$$

$$
\left(1+\frac1{10}\right)^{10}\approx2.594,
$$

$$
\left(1+\frac1{100}\right)^{100}\approx2.705.
$$

As `n` grows, this process approaches `e`.

For a few more reference points:

$$
\left(1+\frac1{1000}\right)^{1000}\approx2.7169,
$$

$$
\left(1+\frac1{10000}\right)^{10000}\approx2.7181.
$$

The values creep upward, but they do not run away to infinity. They settle toward a
specific limiting number.

So `e` is not just a stored decimal. It is the invariant that appears when discrete
compounding is pushed toward continuous growth.

**What this reflects**

```text
the smaller each growth step becomes,
the more the whole process behaves like smooth self-proportional change
```

That is why `e` appears in bank interest, population models, radioactive decay,
normal distributions, and differential equations. The surface examples differ, but the
same structure keeps returning: change is proportional to the current amount.

---

## 2. Why `e` Is Special

If one phrase should stick, it is this:

```text
e^x changes at the rate e^x
```

The essential property is

$$
\frac{d}{dx}e^x=e^x.
$$

The function `e^x` is equal to its own rate of change.

That makes `e` the natural base for continuous growth, decay, differential equations,
probability, and many physical processes.

Some simple values help fix the scale:

$$
e^0=1,
$$

$$
e^1=e,
$$

$$
e^2\approx7.389.
$$

The value grows, but the rule stays self-similar: at each point, the instantaneous
change is proportional to what is already there.

In the language of this workspace:

```text
e
  -> self-consistent continuous change
```

Related source: [e: self-consistent continuous change](constants-as-process-invariants-proposal.md#e-self-consistent-continuous-change).

**Observation checkpoint**

Many functions change. The special thing about `e^x` is that it changes without
changing its form. Its derivative is not merely related to it; it is the same function
again. That is why `e` acts like a fixed point of continuous change.

---

## 3. Why Exponentials Connect `e` To Binet's Formula

Before turning to Fibonacci numbers, pause on the word "power".

In elementary arithmetic, a power such as

$$
2^5
$$

means repeated multiplication:

$$
2\cdot2\cdot2\cdot2\cdot2.
$$

That is a discrete operation. You multiply a whole number of times.

But mathematics extends this idea. Expressions such as

$$
2^{1/2},\qquad 2^\pi,\qquad \varphi^n
$$

still make sense, even when the exponent is not just a counting number. The cleanest
general language for this extension uses `e`:

$$
a^x=e^{x\log a}
$$

for positive `a`.

So powers of the golden ratio can be read as exponential growth:

$$
\varphi^n=e^{n\log\varphi}.
$$

This does not mean Binet's formula is "about `e`" in the same direct way that Euler's
formula is. It means Binet's formula lives in the exponential family: it describes the
Fibonacci sequence by combining growth modes raised to the `n`th power.

**Observation checkpoint**

The Fibonacci recurrence advances one step at a time, but Binet's formula describes the
whole sequence through powers. That is the change of viewpoint:

```text
step rule
  -> exponential modes
```

---

## 4. Binet's Formula

Now switch from continuous change to a discrete recurrence.

The Fibonacci sequence is built by a tiny memory system: keep the previous two values,
add them, and move forward. You can see this in plant spirals, branching models,
tilings, combinatorics, and any situation where the next state depends on two earlier
states rather than one.

The Fibonacci sequence is

$$
0,1,1,2,3,5,8,13,21,34,\ldots
$$

with recurrence

$$
F_{n+2}=F_{n+1}+F_n.
$$

Binet's formula gives the `n`th Fibonacci number directly:

$$
\boxed{
F_n=\frac{\varphi^n-\psi^n}{\sqrt5}
}
$$

where

$$
\varphi=\frac{1+\sqrt5}{2}
$$

and

$$
\psi=\frac{1-\sqrt5}{2}.
$$

This is the strange part:

- the sequence is made of integers;
- the recurrence uses integer addition;
- the closed form uses irrational real numbers;
- the final answer is still always an integer.

For example,

$$
F_5=
\frac{\varphi^5-\psi^5}{\sqrt5}=5.
$$

To see why this is surprising, compare the ingredients with the result:

```text
input ingredients:
  sqrt(5), phi, psi, irrational powers

output:
  the integer 5
```

The formula is not approximating `F_5`. It gives exactly `5`.

The irrational terms are not noise. They are the hidden modes of the recurrence.

This is the first surprise of the page: a formula can use irrational real numbers as
internal machinery while still producing integers at the end.

**What this reflects**

The recurrence is discrete, but it has two underlying growth modes. One mode grows
dominantly; the other fades. Binet's formula combines both modes so precisely that the
irrational parts cancel into whole numbers.

**What Binet's formula is doing**

Binet's formula turns a recursive question into a direct question.

The recursive version asks:

```text
What are the previous two Fibonacci numbers?
Add them.
Repeat until index n.
```

The closed-form version asks:

```text
What are the two growth modes of the recurrence?
Raise them to n.
Combine them.
```

Both descriptions produce the same sequence, but they reveal different things. The
recurrence reveals how to generate Fibonacci numbers. Binet's formula reveals why their
growth has a stable exponential shape.

---

## 5. Where The Irrational Numbers Come From

This section explains why `sqrt(5)` and the golden ratio are not decorative constants.
They are forced by the recurrence.

Start with the recurrence:

$$
F_{n+2}=F_{n+1}+F_n.
$$

Temporarily imagine a solution of the form

$$
F_n=x^n.
$$

Then

$$
x^{n+2}=x^{n+1}+x^n.
$$

Dividing by `x^n` gives

$$
x^2=x+1.
$$

So the recurrence asks us to solve

$$
x^2-x-1=0.
$$

The quadratic formula gives

$$
x=\frac{1\pm\sqrt5}{2}.
$$

These are exactly

$$
\varphi=\frac{1+\sqrt5}{2}
$$

and

$$
\psi=\frac{1-\sqrt5}{2}.
$$

That is where the real numbers enter. We started with an integer recurrence, but the
underlying algebra forces a move beyond the rational numbers.

**Important note**

The temporary guess `F_n = x^n` is not saying Fibonacci numbers literally start as pure
powers. It is a method for detecting the growth modes of the recurrence. Once those
modes are found, Binet's formula combines them in exactly the right way to recover the
integer sequence.

**Observation checkpoint**

The equation `x^2 - x - 1 = 0` is the bridge. It translates a step-by-step recurrence
into an algebraic object whose roots describe the recurrence's long-term behavior.

The two roots have different roles:

| Root | Approximate value | Role |
|---|---:|---|
| `phi` | `1.618...` | Dominant growing mode |
| `psi` | `-0.618...` | Alternating fading correction |

Because `|psi| < 1`, powers of `psi` get small quickly:

$$
\psi^2\approx0.382,\qquad
\psi^5\approx-0.090,\qquad
\psi^{10}\approx0.008.
$$

That fading term is why Fibonacci numbers are so close to

$$
\frac{\varphi^n}{\sqrt5}
$$

for large `n`, even though the exact formula still needs both modes.

This gives a useful consequence:

$$
F_n
=
\operatorname{nearest\ integer}
\left(
\frac{\varphi^n}{\sqrt5}
\right).
$$

Why does rounding work? Because Binet's exact formula is

$$
F_n=\frac{\varphi^n}{\sqrt5}-\frac{\psi^n}{\sqrt5},
$$

and the correction term

$$
\frac{\psi^n}{\sqrt5}
$$

quickly becomes smaller than half a unit in magnitude. Once that happens, the nearest
integer to the dominant term is the Fibonacci number itself.

**What this reveals**

The small fading mode is not mathematically optional. It is what makes the formula
exact. But after a few steps, it becomes small enough that the dominant mode alone
predicts the correct integer by rounding.

Related sources:

- [Fibonacci: Recursive, Iterative, Accumulative, Stateful](constants-as-process-invariants-proposal.md#fibonacci-recursive-iterative-accumulative-stateful)
- [sqrt(5): separation of Fibonacci modes](constants-as-process-invariants-proposal.md#sqrt5-separation-of-fibonacci-modes)

---

## 6. A Second View: The Fibonacci Matrix

There is another useful way to see the same structure. Instead of treating the
Fibonacci recurrence as a list of numbers, treat it as a repeated transformation of a
two-number state.

The state is:

$$
\begin{pmatrix}
F_{n+1}\\
F_n
\end{pmatrix}.
$$

One Fibonacci step sends this state to the next one:

$$
\begin{pmatrix}
F_{n+2}\\
F_{n+1}
\end{pmatrix}
=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}
\begin{pmatrix}
F_{n+1}\\
F_n
\end{pmatrix}.
$$

Call the matrix

$$
A=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}.
$$

Then repeated Fibonacci evolution means repeatedly applying `A`.

The important fact is that this matrix has the same characteristic equation:

$$
\lambda^2-\lambda-1=0.
$$

So its eigenvalues are:

$$
\lambda=\varphi
\quad\text{and}\quad
\lambda=\psi.
$$

This is the matrix version of the same lesson:

```text
Fibonacci recurrence
  -> repeated state transformation
  -> eigenvalues
  -> phi and psi modes
```

**Observation checkpoint**

The symbols changed, but the bond did not. Whether we start with a guessed solution
`F_n = x^n` or with the Fibonacci matrix, the same two numbers appear because they are
the modes preserved by the recurrence.

This also explains why the golden ratio is so stable. Repeatedly applying the Fibonacci
matrix amplifies the `phi` direction and suppresses the `psi` direction. After many
steps, the visible behavior is dominated by `phi`.

Related source: [Discrete evolution](constants-as-process-invariants-proposal.md#discrete-evolution).

---

## 7. Why `sqrt(5)` Requires The Real Numbers

The move from rational numbers to real numbers is not a luxury. It happens because some
perfectly natural equations have no fractional answer.

The rational numbers contain fractions such as

$$
\frac12,\qquad \frac34,\qquad \frac{22}{7}.
$$

But the equation

$$
x^2=5
$$

has no rational solution.

The real numbers fill this kind of gap. There is a precise real number

$$
\sqrt5=2.2360679\ldots
$$

with

$$
2<\sqrt5<3.
$$

Decimal approximations can approach it:

$$
2.2^2=4.84,
$$

$$
2.23^2=4.9729,
$$

$$
2.236^2\approx4.999696.
$$

And even closer:

$$
2.2360679^2\approx5.
$$

The decimal expansion is not the number itself. The decimal is a sequence of better and
better approximations to the real number whose square is exactly `5`.

Binet's formula therefore reveals a pattern seen throughout mathematics:

```text
simple discrete rule
  -> algebraic equation
  -> enlarged number system
  -> clearer closed form
```

**Day-to-day analogy**

Sometimes a problem is easy to operate but hard to understand. You can follow a recipe
without knowing chemistry; you can drive a route without seeing the map. Binet's formula
is the map: it shows the shape behind the repeated Fibonacci updates.

**Observation checkpoint**

The real numbers are not just "decimals". They are what allow limiting positions to
exist as exact objects. Binet's formula needs that exactness: an approximation to
`sqrt(5)` gives an approximation to `F_n`, but the real number `sqrt(5)` belongs to the
exact formula.

---

## 8. Euler's Formula Extends The Pattern

Euler's formula is the next extension in the same spirit. Real numbers let us solve
equations such as `x^2 = 5`. Complex numbers let us solve equations such as `x^2 = -1`
and describe rotation algebraically.

Euler's formula is

$$
\boxed{e^{ix}=\cos x+i\sin x}.
$$

Here `i` is the number satisfying

$$
i^2=-1.
$$

This moves beyond real numbers into complex numbers.

Setting `x = pi` gives

$$
e^{i\pi}=\cos\pi+i\sin\pi.
$$

Since

$$
\cos\pi=-1
$$

and

$$
\sin\pi=0,
$$

we get

$$
e^{i\pi}=-1.
$$

Therefore

$$
\boxed{e^{i\pi}+1=0}.
$$

Euler's identity connects five fundamental constants:

$$
0,\quad1,\quad e,\quad i,\quad\pi.
$$

Related source: [Euler's formula](../mathematical-ontology/Mathematical%20fundamentals.md#eulers-formula).

**What this reflects**

Complex numbers let one value carry both size and direction. Multiplication can then
represent turning, not only scaling. Euler's formula is powerful because it says that
smooth exponential change and circular motion are two views of the same structure when
seen in the complex plane.

**Why this belongs after Binet**

Binet's formula showed that an integer recurrence becomes clearer when we allow real
growth modes. Euler's formula shows that rotation becomes clearer when we allow complex
growth modes.

The pattern is the same:

```text
old setting:
  the rule works, but the structure is hidden

larger setting:
  the structure becomes simple
```

---

## 9. What Not To Overclaim

The bond is strong, but it should be stated carefully.

First, Binet's formula does not mean Fibonacci numbers are "secretly continuous". The
sequence is still indexed discretely:

$$
n=0,1,2,3,\ldots
$$

The continuous-looking objects appear because the closed form analyzes the recurrence's
growth modes.

Second, Euler's number does not replace the golden ratio in Binet's formula. The natural
closed form uses `phi` and `psi`. The connection to `e` comes through the general
language of exponentials:

$$
\varphi^n=e^{n\log\varphi}.
$$

Third, the complex numbers in Euler's formula are not required to compute Fibonacci
numbers. They enter because the same exponential language that describes real growth
also describes rotation when the exponent is imaginary.

Fourth, the approximation

$$
\frac{\varphi^n}{\sqrt5}
$$

is not the same thing as Binet's formula. It becomes a reliable rounding shortcut
because the missing `psi` term fades, not because the `psi` term was never there.

So the precise statement is:

> Binet's formula, Euler's number, and Euler's formula are connected through the wider
> language of exponential modes and number-system extension, not because they are the
> same formula in disguise.

---

## 10. Number-System Progression

The bond can be summarized as a sequence of necessary extensions.

Natural numbers count:

$$
1,2,3,4,\ldots
$$

Fractions require rational numbers:

$$
\frac12,\qquad\frac34,\qquad\frac{22}{7}.
$$

Equations such as

$$
x^2=5
$$

require real numbers:

$$
\sqrt5,\qquad \pi,\qquad e.
$$

Equations such as

$$
x^2=-1
$$

require complex numbers:

$$
i=\sqrt{-1}.
$$

Binet's formula is beautiful because it shows real numbers emerging naturally from a
problem that began as integer counting. Euler's formula then shows that exponential
change, trigonometry, `pi`, and complex rotation are parts of one larger language.

The teaching point is not that bigger number systems are "more advanced" in a vague
sense. Each extension solves a specific expressive problem:

| Extension | Problem it solves |
|---|---|
| Natural numbers | Counting separate things |
| Rational numbers | Comparing parts and wholes |
| Real numbers | Filling limiting and square-root gaps |
| Complex numbers | Representing rotation and roots of negative quantities |

---

## 11. Big Picture

The compact bond is:

$$
\boxed{
\text{Fibonacci recurrence}
\longrightarrow
\text{characteristic roots}
\longrightarrow
\text{Binet's formula}
\longrightarrow
\text{integers through real modes}
}
$$

and

$$
\boxed{
\text{continuous growth}
\longrightarrow
e^x
\longrightarrow
e^{ix}
\longrightarrow
\text{complex rotation}
}
$$

Together they show a recurring mathematical move:

> When a rule is simple but its structure is hidden, enlarge the number system until the
> rule becomes transparent.

After reading this page, the useful mental image is:

```text
number systems are not only bigger containers;
they are better languages for different kinds of structure
```

Binet's formula uses the real-number language to explain an integer recurrence. Euler's
formula uses the complex-number language to explain rotation through exponentials.

The full lesson is:

```text
Fibonacci recurrence:
  discrete rule, integer outputs

Binet's formula:
  real exponential modes, exact integer recovery

Euler's number:
  continuous self-proportional change

Euler's formula:
  complex exponentials as rotation
```

So the bond is not just between two named formulas. It is between two mathematical
habits:

- follow a process step by step;
- enlarge the language until the process reveals its hidden structure.
