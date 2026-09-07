# Cosine Function

The cosine function describes a smooth wave that repeats over time or angle. It can
also be understood as the horizontal position of a point moving around the unit circle.

Navigation:

- Formula registry: [Formula Registry](../formula-registry.md)
- Related concept page: [Mathematical Fundamentals](../mathematical-ontology/Mathematical%20fundamentals.md#oscillation)
- Related bridge: [Euler's formula](../mathematical-ontology/Mathematical%20fundamentals.md#eulers-formula)

---

## 1. Observations

To show how cosine changes over time, we can draw the cosine function as a moving wave.
When time `t` starts at:

$$
t=0,
$$

cosine begins at its highest point:

$$
1.
$$

After that, its value waves up and down between `1` and `-1`. The x-axis represents
time, and the y-axis represents the value of the cosine.

---

## 2. Important Features

**The starting position $(t=0)$:**  
Unlike sine, which starts at `0`, the cosine wave starts at its maximum value:

$$
\cos(0)=1.
$$

**The wavelength / period:**  
After exactly:

$$
2\pi
$$

radians, approximately `6.28`, the wave has completed one full cycle: down and all the
way back up again. Then the cycle repeats.

**The zeros / x-axis intersections:**  
The wave crosses the x-axis, where its value is `0`, at fixed moments, such as:

$$
t=\frac{\pi}{2}
$$

approximately `1.57`, and:

$$
t=\frac{3\pi}{2}
$$

approximately `4.71`.

This matches the `90` degree right angle from the triangle viewpoint: at a quarter turn
around the unit circle, the horizontal position has moved to zero.

**The troughs:**  
The wave reaches its lowest point, with value `-1`, in the middle of the cycle:

$$
t=\pi
$$

approximately `3.14`.

---

## 3. The Link With A Rotating Circle

You can also visualize this change over time as a point rotating around a wheel: the
unit circle.

Cosine measures how far the point is to the left or right of the center. If the wheel
keeps turning at a constant speed and you plot that horizontal position over time, you
get exactly this smooth cosine wave.

Conceptually:

```text
constant circular rotation -> horizontal position over time -> cosine wave
```

This is why cosine belongs naturally with right triangles, the unit circle, periodic
motion, phasors, and Euler's formula.
