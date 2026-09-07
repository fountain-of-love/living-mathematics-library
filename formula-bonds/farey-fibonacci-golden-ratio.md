# Farey Neighbors, Fibonacci Ratios, And The Golden Ratio

This page explains a bond between three ideas that can look unrelated at first:

- Farey sequences, which organize fractions by denominator size;
- Fibonacci ratios, which come from a simple recurrence;
- the golden ratio, which appears as the limiting shape of that recurrence.

The guiding question is:

> Why do Fibonacci fractions behave like especially good neighbors among rational
> approximations?

This bond is close to the statement that "Farey sequences contain Fibonacci ratios",
but the precise relationship is more careful and more interesting:

```text
Fibonacci recurrence
  -> consecutive Fibonacci ratios
  -> convergents of [1;1,1,1,...]
  -> golden ratio

Farey neighbors
  -> determinant condition bc - ad = 1
  -> close rational approximations
```

Fibonacci fractions sit at the intersection because consecutive Fibonacci ratios satisfy
the same determinant-1 structure that makes Farey neighbors special.

Navigation:

- Bond overview: [Formula Bonds](README.md)
- Formula registry: [Formula Registry](../formula-registry.md)
- Registry entries: [Fibonacci recurrence](../formula-registry.md#fibonacci-farey-and-rational-approximation), [Farey determinant condition](../formula-registry.md#fibonacci-farey-and-rational-approximation), [Golden-ratio continued fraction](../formula-registry.md#fibonacci-farey-and-rational-approximation)

How to read this page:

1. Start with the everyday problem of simple fractions.
2. Learn what Farey sequences organize.
3. Learn what Fibonacci ratios approach.
4. Notice the determinant-1 condition where the two structures meet.

Elements at a glance:

| Element | Plain meaning | What to watch for |
|---|---|---|
| Farey sequence | Fractions sorted by size under a denominator limit | Neighboring fractions are "best available" at that resolution |
| Fibonacci ratio | Ratio of neighboring Fibonacci numbers | The ratios squeeze toward the golden ratio |
| Golden ratio | Stable limiting ratio of the Fibonacci recurrence | It is forced by `r = 1 + 1/r` |
| Stern-Brocot tree | A fraction-building tree using mediants | It reveals paths of increasingly good rational approximations |

---

## 0. What To Notice First

Before the formulas, notice the ordinary problem underneath.

Fractions are how we compare quantities when whole numbers are too coarse: half a cup,
three quarters of an hour, two thirds of a vote, a screen aspect ratio, a gear ratio, a
musical interval, a recipe scaled down for fewer people. In daily life, we often want a
fraction that is both **accurate** and **simple**.

For example, `355/113` is a famous rational approximation to `pi`. It is not valuable
because it is a random fraction. It is valuable because its denominator is still
reasonably small while the approximation is surprisingly good.

Farey sequences study this exact tension:

```text
How good can a fraction be if we limit the denominator?
```

Fibonacci ratios enter because they form a disciplined chain of fractions that approach
the golden ratio through the continued-fraction rule of repeated `1`s. The golden ratio
is the limiting direction of that chain.

---

## 1. Farey Sequences

Imagine lining up all the simplest fractions between `0` and `1`, but only allowing
denominators up to a chosen size. That is a Farey sequence.

If the denominator limit is small, the sequence is coarse. You can only express a few
positions. If the denominator limit grows, more fractions become available and the line
between `0` and `1` becomes more finely resolved.

This is why Farey sequences are a natural classroom example of a deeper idea:

```text
mathematics often studies approximation under constraint
```

The Farey sequence of order `n`, written here as $\mathcal F_n$, is the increasing
list of all reduced fractions

$$
\frac ab
$$

between `0` and `1` whose denominator satisfies `b <= n`.

For example,

$$
\mathcal F_3=
\left\{
\frac01,\frac13,\frac12,\frac23,\frac11
\right\}.
$$

And

$$
\mathcal F_5=
\left\{
\frac01,\frac15,\frac14,\frac13,\frac25,\frac12,
\frac35,\frac23,\frac34,\frac45,\frac11
\right\}.
$$

The key structural fact is:

if

$$
\frac ab < \frac cd
$$

are consecutive terms in a Farey sequence, then

$$
bc-ad=1.
$$

This determinant condition is the main bridge to Fibonacci numbers.

What does a Farey sequence reflect?

- It reflects **resolution**: increasing `n` lets you see finer fractional positions.
- It reflects **simplicity**: only fractions with small enough denominators are allowed.
- It reflects **neighbor structure**: consecutive entries are the closest available
  rational positions at that resolution.

You meet this idea any time a continuous quantity must be represented by a small
integer ratio: choosing gear teeth, dividing time signatures, approximating a slope on
a pixel grid, resizing images by integer dimensions, or choosing a recipe ratio that
humans can measure.

**Observation checkpoint**

In $\mathcal F_5$, compare `1/2` and `3/5`. They are close, but no allowed reduced
fraction with denominator `5` or less fits between them. The sequence is not merely
listing fractions; it is showing the best resolution available under the limit.

---

## 2. Fibonacci Ratios

The Fibonacci sequence is a different kind of object. It is not primarily about
approximating fractions. It is about a state that grows by remembering its two previous
states.

The Fibonacci sequence is

$$
1,1,2,3,5,8,13,21,34,\ldots
$$

with recurrence

$$
F_{k+1}=F_k+F_{k-1}.
$$

Fractions formed from consecutive Fibonacci numbers are

$$
\frac12,\quad
\frac23,\quad
\frac35,\quad
\frac58,\quad
\frac8{13},\quad
\frac{13}{21},\ldots
$$

These fractions alternate around the reciprocal of the golden ratio:

$$
\frac1\varphi\approx0.618034.
$$

For example,

$$
\frac35=0.6,\qquad
\frac58=0.625,\qquad
\frac8{13}\approx0.61538,\qquad
\frac{13}{21}\approx0.61905.
$$

Using the reciprocal fractions instead,

$$
\frac21,\quad
\frac32,\quad
\frac53,\quad
\frac85,\quad
\frac{13}{8},\quad
\frac{21}{13},\ldots
$$

gives approximations to

$$
\varphi=\frac{1+\sqrt5}{2}\approx1.618034.
$$

For example,

$$
\frac85=1.6,\qquad
\frac{13}{8}=1.625,\qquad
\frac{21}{13}\approx1.61538.
$$

**What to observe**

The fractions do not approach `varphi` from only one side. They overshoot, undershoot,
and then overshoot again, each time with smaller error. This alternating squeeze is the
signature of a rational approximation process.

**Day-to-day analogy**

Imagine adjusting a dial when the exact setting is not available. One setting is a bit
too low, the next is a bit too high, and each later pair brackets the target more
tightly. Fibonacci ratios behave like that around `varphi`.

---

## 3. Why The Golden Ratio Appears

Now ask the important question: why this limit and not some other number?

Let

$$
r_n=\frac{F_{n+1}}{F_n}.
$$

Because

$$
F_{n+1}=F_n+F_{n-1},
$$

we get

$$
r_n
=
1+\frac{F_{n-1}}{F_n}
=
1+\frac{1}{F_n/F_{n-1}}.
$$

If the ratios approach a limiting value `r`, then

$$
r=1+\frac1r.
$$

Multiplying by `r`,

$$
r^2=r+1,
$$

so

$$
r^2-r-1=0.
$$

The positive solution is

$$
\boxed{r=\frac{1+\sqrt5}{2}=\varphi}.
$$

So the golden ratio is not an arbitrary number that happens to appear in Fibonacci
fractions. It is the limiting ratio forced by the Fibonacci recurrence itself.

The important observation is that a recurrence can have a "shape". In this case, the
shape is a stable ratio. After enough steps, the sequence keeps growing, but the
relationship between neighboring terms settles toward `varphi`.

---

## 4. The Farey Bond

Now return to Farey sequences. Farey neighbors are not just near each other on the
number line. They satisfy a very strict arithmetic test: their cross-products differ by
exactly `1`.

Compare neighboring Fibonacci fractions:

$$
\frac{F_n}{F_{n+1}}
\quad\text{and}\quad
\frac{F_{n+1}}{F_{n+2}}.
$$

Cassini's identity says

$$
F_{n+1}^2-F_nF_{n+2}=(-1)^n.
$$

Therefore the cross-product difference of these two fractions is always `1` in
absolute value:

$$
\left|F_{n+1}^2-F_nF_{n+2}\right|=1.
$$

Example:

$$
\frac35
\quad\text{and}\quad
\frac58.
$$

Their cross products are

$$
3\cdot8=24
$$

and

$$
5\cdot5=25,
$$

so

$$
5\cdot5-3\cdot8=1.
$$

That is exactly the determinant condition that characterizes neighboring Farey
fractions.

Consequently, Fibonacci fractions naturally appear as very close rational neighbors in
Farey structures.

This is the actual bond:

```text
Fibonacci recurrence creates neighboring ratios.
Farey theory recognizes best-available rational neighbors.
The determinant-1 condition is where the two languages touch.
```

**Observation checkpoint**

The determinant is not measuring ordinary distance on the number line. It is measuring
an arithmetic kind of adjacency. Two fractions can be visually close, but the Farey
condition says something stronger: at the chosen denominator scale, there is no simpler
fraction sitting between them.

---

## 5. The Necessary Correction

The statement

> As order increases, consecutive terms in Farey sequences feature ratios of adjacent
> Fibonacci numbers.

is too broad.

A Farey sequence contains many fractions, and most consecutive pairs are not Fibonacci
fractions. For example, in $\mathcal F_5$, the consecutive fractions

$$
\frac13,\frac25
$$

are not ratios of adjacent Fibonacci numbers.

The accurate version is:

> Certain important chains of Farey neighbors are generated by Fibonacci numbers, and
> those Fibonacci fractions give increasingly good rational approximations to the
> golden ratio or its reciprocal.

This correction matters because it protects the idea from becoming mystical. The
connection is real, but it is specific: Fibonacci fractions form special paths through
the rational-approximation landscape; they do not explain every neighboring pair in
every Farey sequence.

---

## 6. Stern-Brocot And Continued Fractions

The deeper structure becomes clearer in the Stern-Brocot tree.

The Stern-Brocot tree is another way of organizing fractions. Instead of listing all
fractions up to a denominator limit, it builds new fractions between old ones. If Farey
sequences feel like a sorted catalogue, the Stern-Brocot tree feels like a family tree.

The everyday intuition is interpolation: if one available setting is too low and the
next is too high, try the simplest setting between them. This appears when tuning,
scaling, choosing ratios, or refining a measurement without jumping immediately to
large denominators.

Starting with

$$
\frac01,\qquad\frac11,
$$

insert the mediant

$$
\frac{a+c}{b+d}
$$

between neighboring fractions

$$
\frac ab,\frac cd.
$$

For example,

$$
\frac01,\frac11
$$

produces

$$
\frac12.
$$

Repeated mediants produce the rational-number structure closely related to Farey
sequences.

The golden ratio has continued fraction

$$
\varphi=[1;1,1,1,1,\ldots].
$$

Its convergents are

$$
1,\quad
2,\quad
\frac32,\quad
\frac53,\quad
\frac85,\quad
\frac{13}{8},\ldots
$$

whose numerators and denominators are consecutive Fibonacci numbers.

That is why Fibonacci denominators keep appearing when one follows the best rational
approximations to `varphi`.

**What this adds to the Farey view**

Farey sequences show what the available neighbors are at a fixed denominator limit.
The Stern-Brocot tree shows how one can walk from rough approximations to refined
approximations. Continued fractions describe that walk symbolically. For the golden
ratio, the repeated `1`s in the continued fraction are what make Fibonacci numbers
appear again and again.

---

## 7. Big Picture

The bond can be summarized as:

$$
\boxed{
\text{Fibonacci recurrence}
\longrightarrow
\text{Fibonacci ratios}
\longrightarrow
\varphi
}
$$

and

$$
\boxed{
\text{Farey neighbors}
\longrightarrow
bc-ad=1
\longrightarrow
\text{excellent rational approximations}
}
$$

The shared invariant is the determinant-1 condition:

$$
bc-ad=1.
$$

So the most interesting claim is not simply that Farey sequences contain Fibonacci
numbers. It is that Farey theory, continued fractions, Fibonacci numbers, and the
golden ratio are different views of the same theory of rational approximation.

After reading this page, the useful mental image is:

```text
fractions are not only numbers;
they are positions in a constrained approximation landscape
```

Farey sequences map the landscape. Fibonacci ratios trace a special path through it.
The golden ratio is the limit that path approaches.
