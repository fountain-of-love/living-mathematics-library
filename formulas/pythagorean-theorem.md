# Pythagorean Theorem

The Pythagorean theorem is a mathematical formula for a right triangle. It says that
the two shorter sides and the long diagonal side are connected by:

$$
a^2+b^2=c^2.
$$

Here, `a` and `b` are the two shorter sides that meet at the right angle, and `c` is
the hypotenuse: the slanted side opposite the right angle. The hypotenuse is always
the longest side of a right triangle.

Navigation:

- Formula registry: [Formula Registry](../notes/formula-registry.md)
- Related concept page: [Mathematical Fundamentals](../mathematical-ontology/Mathematical%20fundamentals.md#pythagorean-theorem)
- Related observation: [Mathematical Constants As Process Invariants](constants-as-process-invariants-proposal.md#sqrt2-incommensurability)

---

## 1. Observation

The Pythagorean theorem helps you calculate a missing side in a right triangle.

Important parts of the formula:

**The short sides:**  
`a` and `b` are the sides attached to the right angle.

**The hypotenuse:**  
`c` is the slanted side opposite the right angle. It is the longest side.

**A square:**  
Squaring a number means multiplying it by itself:

$$
2^2=2\times2=4.
$$

The core relationship is:

$$
a^2+b^2=c^2.
$$

This means the square built on the hypotenuse has the same area as the two squares
built on the shorter sides combined.

---

## 2. Calculating The Hypotenuse

To calculate the hypotenuse `c`, square `a` and `b`, add those squares together, and
then take the square root:

$$
c=\sqrt{a^2+b^2}.
$$

For example, if:

$$
a=3,\qquad b=4,
$$

then:

$$
c=\sqrt{3^2+4^2}
$$

$$
c=\sqrt{9+16}
$$

$$
c=\sqrt{25}=5.
$$

So the missing hypotenuse is:

$$
c=5.
$$

---

## 3. Calculating A Short Side

To calculate one of the shorter sides, start from the hypotenuse squared and subtract
the square of the known short side.

If `b` and `c` are known, then:

$$
a=\sqrt{c^2-b^2}.
$$

If `a` and `c` are known, then:

$$
b=\sqrt{c^2-a^2}.
$$

For example, if:

$$
c=5,\qquad b=4,
$$

then:

$$
a=\sqrt{5^2-4^2}
$$

$$
a=\sqrt{25-16}
$$

$$
a=\sqrt{9}=3.
$$

So the missing short side is:

$$
a=3.
$$

---

## 4. What To Notice

The formula is not just about numbers. It is a bridge between length and area:

- `a` and `b` measure the two perpendicular directions.
- `a^2` and `b^2` measure the square areas built from those directions.
- `c` measures the diagonal distance created by combining both directions.

So the theorem explains how a two-direction movement becomes one diagonal distance.
This is why it sits naturally next to distance, radius, coordinates, and the unit
circle.
