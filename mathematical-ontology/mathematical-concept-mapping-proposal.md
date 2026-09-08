# Mathematical Concept Mapping Proposal

## Purpose

This document proposes a simple mapping table for mathematical concepts that can grow from the smallest possible observation: a dot.

The central idea is:

> A mathematical object is not only a shape or value. It is an observation inside a context.

A dot, line, circle, signal, spectrum, and phase trace can sometimes describe the same underlying relation from different observational frames. The drift begins when the representation is treated as the thing itself, instead of as a projection of something being observed.

## Working Distinctions

| Term           | Working meaning                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------- |
| Observation    | A registered distinction: something is noticed, selected, sampled, or marked.                                     |
| Context        | The frame that gives the observation meaning: bit space, coordinate space, time, phase, frequency, geometry, etc. |
| Axis           | A dimension along which observations can vary. Examples: value, position, time, phase, frequency, scale.          |
| Boundary       | A limit or threshold that separates one region/state from another.                                                |
| Interval       | The gap, distance, duration, or difference between two observations.                                              |
| Representation | The form chosen to express the observation: bit, point, coordinate, waveform, shape, spectrum.                    |
| Transformation | A translation from one representation/context into another.                                                       |
| Constraint     | A hidden or explicit assumption that reduces degrees of freedom.                                                  |
| Harmony        | A high-constraint relation where many properties are implied by structure rather than stated separately.          |

## First Ladder: From Dot To Structure

| Level | Concept | Minimal form | Context gives it meaning | Interpretation |
| --- | --- | --- | --- | --- |
| 0 | Dot | `.` | Observation frame | A single noticed distinction. |
| 1 | Binary dot | `0` or `1` | Bit vector | Presence/absence, off/on, false/true. |
| 2 | Phase dot | `0` or `pi` | Phase axis | A projection into two opposite phase states. |
| 3 | Coordinate dot | `(x)`, `(x,y)`, `(x,y,z)` | Spatial axis/plane/volume | A position in one, two, or three dimensions. |
| 4 | Time dot | `t0` | Time axis | A moment or sample instant. |
| 5 | Signal dot | `(t, s(t))` | Time-value plane | A value observed at a time. |
| 6 | Phase-time dot | `(t, phi(t))` | Time-phase plane | A phase observed at a time. |
| 7 | Complex dot | `z = x + iy` | Complex plane | A compressed two-axis point with phase and magnitude available. |

The dot is therefore not one concept. It is the seed of many concepts, depending on which axis or frame is active.

## Second Ladder: From Dot To Line

A line begins when there are two observations related by an interval.

| From | To | Line means | Example |
| --- | --- | --- | --- |
| Bit observation | Bit observation | Discrete gap or transition | `0 -> 1` |
| Time observation | Time observation | Duration | `t1 - t0` |
| Position observation | Position observation | Distance/displacement | `x1 - x0`, `p1 - p0` |
| Signal observation | Signal observation | Change over time | `s(t1) - s(t0)` |
| Phase observation | Phase observation | Phase advance | `phi(t1) - phi(t0)` |
| Boundary | Boundary | Interval/spectrum band | `[a,b]`, frequency band, value range |

So a line can be read as:

- an interval on one axis,
- a distance between two positions,
- a transition between states,
- a duration between moments,
- or a bounded region.

The same minimal form can carry different meaning because the context changes.

## Third Ladder: Split After The Line

Once two observations or two axes are present, the structure can branch.

| Branch | Inputs | Result | Meaning |
| --- | --- | --- | --- |
| Geometry | Two coordinates/axes | Shape | Position relations in a plane or volume. |
| Spectrum | Two boundaries | Range/band | Allowed or observed values between limits. |
| Signal | Time axis + value axis | Waveform | Value as a function of time. |
| Phase | Time axis + angle/phase axis | Phase trajectory | Position in a cycle as a function of time. |
| Complex form | Real axis + imaginary axis | Phasor/complex point | Magnitude and phase compressed into one object. |
| 3D extension | Three coordinates/axes | Volume/path/surface | Position with width, depth, and height. |

## Mapping Table

| Stage | Discrete observation | Continuous observation | Geometric view | Signal/time view | Hidden assumptions |
| --- | --- | --- | --- | --- | --- |
| Dot | `0`, `1`, sample, mark | Point value | Point on an axis or plane | `s(t0)`, `phi(t0)` | Context decides meaning. |
| Pair of dots | Two samples | Two points | Segment, displacement | Change between samples | An interval exists between observations. |
| Line | Step, transition, bit gap | Continuous interval | Distance, ray, boundary | Duration, slope, derivative candidate | Axis is selected. |
| Repetition | `010101...` | Periodic pattern | Repeated placement | Oscillation | Periodicity is assumed. |
| Phase mapping | `b[n] -> phi[n]` | `phi(t)` | Angle on cycle | Phase over time | Symbol-to-phase map is defined. |
| Unit phasor | `e^(i phi[n])` | `e^(i phi(t))` | Point on unit circle | Pure phase signal | Magnitude is fixed at 1. |
| Circle | Sampled points on circle | `z(t)=R e^(i theta(t))` | Equal scaling in x/y | Rotating phase with constant radius | `a=b=R`; no preferred direction. |
| Ellipse | Sampled points on ellipse | `x=a cos(theta), y=b sin(theta)` | Unequal axis scaling | Distorted or anisotropic cycle | Two independent scales exist. |
| Rectangle | Grid/bounded samples | Bounded plane region | Two axis-aligned intervals | Window over values/time | Corners/boundaries dominate over rotation. |
| Spectrum | Discrete bins | Continuous band | Interval between boundaries | Frequency/value range | Boundary pair defines the object. |
| Spiral | Accumulated samples | `R(t) e^(i theta(t))` | Radius changes with phase/time | Accumulation, drift, modulation | Radius is no longer constant. |
| 3D path | Ordered coordinate triples | Space curve | Motion through volume | Time-parametrized trajectory | A third spatial or state axis is active. |

## Key Translation Functions

| Translation | Form | What it does |
| --- | --- | --- |
| Bit to value | `b -> {0,1}` | Interprets a symbol as a state or amplitude. |
| Bit to phase | `b -> phi` | Maps a discrete symbol to a phase, such as `0 -> 0`, `1 -> pi`. |
| Phase to circle | `theta -> (R cos(theta), R sin(theta))` | Turns phase into position on a circle. |
| Circle to complex | `(x,y) -> z = x + iy` | Compresses two coordinates into one complex representation. |
| Complex to phase/magnitude | `z -> (|z|, arg(z))` | Extracts radius and angle from a complex point. |
| Time to signal | `t -> s(t)` | Observes a changing value through time. |
| Time to phase | `t -> phi(t)` | Observes phase evolution through time. |
| Phase accumulation | `phi(t) = integral omega(t) dt` | Builds phase from angular velocity over time. |
| Discrete accumulation | `phi[n] = sum delta_phi[k]` | Builds phase from sampled phase steps. |
| Boundary to spectrum | `(low, high) -> band` | Turns two limits into a continuous or discrete range. |

## Geometry: Circle, Ellipse, Rectangle

The circle and ellipse distinction is important.

An ellipse has two scale parameters:

```text
x = a cos(theta)
y = b sin(theta)
```

The ratio `a/b` expresses relative scaling between the axes. It is not the radius itself.

A circle appears when the two scales align:

```text
a = b = R
x^2 + y^2 = R^2
z = R e^(i theta)
```

So the circle is not merely a simpler drawing. It is an ellipse with a symmetry constraint.

The unit circle compresses further:

```text
R = 1
z = e^(i theta)
```

This hides multiple assumptions:

- radius is fixed,
- radius is one,
- x/y scaling is equal,
- x/y axes are phase-shifted by 90 degrees,
- the point remains on the circle,
- rotation does not prefer one direction.

This is where "harmony" can be used carefully: a harmonious representation is one where constraints create compression. Less has to be stated because more is implied by structure.

## Signal And Circle As Different Observations

A circle and a signal can describe the same cycle from different observations.

| View | Representation | What is observed |
| --- | --- | --- |
| Circle | `(x,y) = (R cos(theta), R sin(theta))` | Position in a 2D phase plane. |
| Cosine signal | `x(t) = R cos(theta(t))` | Projection of circular motion onto one axis over time. |
| Sine signal | `y(t) = R sin(theta(t))` | Projection onto the orthogonal axis over time. |
| Complex signal | `z(t)=R e^(i theta(t))` | Circle and phase evolution retained together. |

From this perspective:

- the circle is a spatial/phase-plane representation,
- the signal is a time-projection representation,
- the transformation is projection plus time parameterization,
- the reverse transformation requires enough information to reconstruct the missing dimension.

For example, `x(t)=cos(t)` alone is a projection. To recover the full circle without ambiguity, we need the complementary component `y(t)=sin(t)` or an equivalent phase/magnitude assumption.

## Discrete And Continuous Views

| Concept | Discrete | Continuous | Bridge |
| --- | --- | --- | --- |
| Observation | sample `n` | time `t` | sampling function |
| Value | `s[n]` | `s(t)` | interpolation/reconstruction |
| Phase | `phi[n]` | `phi(t)` | phase sampling |
| Frequency | phase step `delta_phi[n]` | angular velocity `omega(t)` | difference/integral |
| Pattern | finite or repeated sequence | periodic function | period and mapping |
| Spectrum | bins | frequency band | transform/resolution |
| Circle | sampled points | continuous curve | parametric traversal |

Discrete and continuous are not enemies. They are observation modes. A discrete sequence can sample a continuous process, and a continuous model can idealize a discrete pattern.

## Proposed Growth Order

This order may keep the map from drifting too quickly:

1. Dot as observation.
2. Dot in context: bit, coordinate, time, phase, signal sample.
3. Two dots as interval.
4. Line as distance, duration, transition, or boundary.
5. Two axes as plane.
6. Plane as geometry or signal surface.
7. Two coordinates as shape: circle, ellipse, rectangle.
8. Two boundaries as spectrum.
9. Time plus value as signal.
10. Time plus phase as phase evolution.
11. Complex number as compressed two-axis representation.
12. Circle as constrained ellipse.
13. Signal as projection of circular/phase motion.
14. Spiral as changing radius, accumulation, or modulation.
15. 3D as added coordinate, state, or observation dimension.

## Drift Warnings

These are the places where the table may confuse concepts unless the context is kept explicit.

| Drift | Correction |
| --- | --- |
| Treating a dot as always spatial | A dot is any observation; spatial position is only one context. |
| Treating a line as always geometry | A line may be interval, distance, duration, transition, or boundary. |
| Treating circle and signal as unrelated | A signal can be a time projection of circular phase motion. |
| Treating `a/b` as radius | `a/b` is relative axis scaling; `R` is absolute radius for a circle. |
| Treating phase as constant | Phase usually changes; constant radius is the circle constraint. |
| Treating complex numbers as "extra dimension" only | Complex form can compress two coordinates plus rotation/phase assumptions. |
| Treating simplification as loss only | Simplification may be compression through constraints. |
| Treating discrete/continuous as separate realities | They can be related through sampling, interpolation, projection, and transforms. |

## Open Questions For Review

1. Should "observation" be the root term, or should "distinction" be even more primitive?
2. Should boundaries be introduced before lines, since a line segment can be seen as two boundaries?
3. Should spectrum be modeled as a line/interval first, or as a transform view of a signal?
4. Should imaginary numbers be described as compression, rotation, orthogonality, or all three?
5. Is "harmony" best defined as equal scaling, stable constraint, resonance, or compression of degrees of freedom?
6. Where should probability enter: as uncertain observation, distribution over dots, or spectrum of possible values?
7. Is 3D simply another coordinate axis, or should it be framed as a new observational freedom?

## Compact Thesis

```text
dot
-> observation in context
-> two observations create interval
-> intervals become lines, boundaries, distances, durations
-> two axes create planes
-> planes branch into geometry, signals, phase spaces, spectra
-> constraints compress degrees of freedom
-> circle is constrained ellipse
-> signal is time projection of phase/geometry
-> complex form compresses two-axis phase geometry
-> spiral restores changing scale/accumulation
```

