# The Cake Model of Continuous Decay

## Core Idea

Negative compound interest describes repeated proportional removal. Each removal is taken from the current remaining quantity, not from the original quantity. The result is a recursive process: every step acts on the output of the previous step.

## Recursive Removal

Let the initial quantity be

$$
C_0 = 1.
$$

Perform \(n\) steps. At each step, remove the fraction \(1/n\) of what currently remains. The remaining quantity is multiplied each time by

$$
1 - \frac{1}{n}.
$$

After \(k\) removals,

$$
C_k = \left(1-\frac{1}{n}\right)^k.
$$

After exactly \(n\) removals,

$$
C_n = \left(1-\frac{1}{n}\right)^n.
$$

The total removed quantity is therefore

$$
R_n = 1 - \left(1-\frac{1}{n}\right)^n.
$$

## Example: Four Removals

For \(n=4\), each step removes one quarter of the current remainder:

$$
1 \rightarrow \frac{3}{4} \rightarrow \left(\frac{3}{4}\right)^2
\rightarrow \left(\frac{3}{4}\right)^3
\rightarrow \left(\frac{3}{4}\right)^4.
$$

After four rounds,

$$
C_4 = \left(\frac{3}{4}\right)^4 = \frac{81}{256} \approx 0.3164.
$$

Thus the removed fraction is

$$
1 - 0.3164 = 0.6836,
$$

or about \(68.36\%\) of the original quantity.

## Continuous Limit

The limiting survival fraction is

$$
\lim_{n\to\infty}\left(1-\frac{1}{n}\right)^n = e^{-1}.
$$

Hence

$$
\lim_{n\to\infty} R_n = 1-e^{-1} \approx 0.63212.
$$

In the limit of many increasingly small proportional removals, approximately \(63.2\%\) is removed and approximately \(36.8\%\) remains.

## Contrast: Removal From the Original Quantity

If each step removes \(1/n\) of the original quantity, rather than \(1/n\) of the current remainder, then the process is not recursive:

$$
1 - n\frac{1}{n} = 0.
$$

After \(n\) such removals, the entire original quantity is removed.

## Course Note

The distinction is structural:

| Process | Rule | Result after \(n\) steps |
|---|---|---|
| Linear removal | Remove a fixed fraction of the original quantity | \(0\) remains |
| Recursive removal | Remove a fixed fraction of the current quantity | \(\left(1-\frac{1}{n}\right)^n\) remains |

Negative compound interest belongs to the second case. Its limiting form is governed by \(e^{-1}\), the natural residual scale of continuous proportional decay.
