# The Cake Model of Continuous Decay

## The cake rule

Imagine one cake whose initial size is normalized to $1$. We observe it over one unit of time and divide that time into $n$ equal rounds.

At every round, remove the fraction $1/n$ of the cake **currently on the table**. The rule always acts on what survived the preceding rounds:

$$
\text{next remainder}
=
\text{current remainder}
-\frac1n(\text{current remainder}).
$$

Equivalently,

$$
\text{next remainder}
=
\left(1-\frac1n\right)
\text{current remainder}.
$$

The cake is therefore not divided in advance into $n$ equal pieces of the original whole. Every new removal is a smaller piece because it is measured from the cake that remains at that moment. This recursive rule is the entire model.

## The discrete recursion

Let $C_{n,k}$ denote the fraction of cake remaining after $k$ of the $n$ rounds. Initially,

$$
C_{n,0}=1.
$$

The rule gives the recursion

$$
\boxed{
C_{n,k+1}
=
\left(1-\frac1n\right)C_{n,k}.}
$$

Applying it repeatedly yields

$$
C_{n,k}
=
\left(1-\frac1n\right)^k.
$$

After all $n$ rounds, the surviving fraction is

$$
C_{n,n}
=
\left(1-\frac1n\right)^n,
$$

and the fraction removed is

$$
R_n
=
1-C_{n,n}
=
1-\left(1-\frac1n\right)^n.
$$

## Example: four rounds

Take $n=4$. At each round, remove one quarter of the cake then present. The cake evolves as

$$
1
\longrightarrow
\frac34
\longrightarrow
\left(\frac34\right)^2
\longrightarrow
\left(\frac34\right)^3
\longrightarrow
\left(\frac34\right)^4.
$$

The successive amounts removed are

$$
\frac14,
\qquad
\frac14\left(\frac34\right),
\qquad
\frac14\left(\frac34\right)^2,
\qquad
\frac14\left(\frac34\right)^3.
$$

Each piece is one quarter of the remainder at that stage, so the pieces become progressively smaller.

After four rounds,

$$
C_{4,4}
=
\left(\frac34\right)^4
=
\frac{81}{256}
\approx0.3164.
$$

The removed fraction is therefore

$$
R_4
=
1-\frac{81}{256}
=
\frac{175}{256}
\approx0.6836.
$$

About $31.64\%$ of the cake remains and $68.36\%$ has been removed.

## Putting time into the model

Each round lasts

$$
\Delta t=\frac1n.
$$

After $k$ rounds, the elapsed time is

$$
t_k=\frac{k}{n}.
$$

Since $k=nt_k$, the remaining fraction can be written as

$$
C_n(t_k)
=
\left(1-\frac1n\right)^{nt_k}.
$$

This notation reveals the continuous question: what happens at a fixed time $t$ when the rounds become increasingly short and increasingly numerous?

## From the recursion to a differential equation

The change during one round is

$$
C_{n,k+1}-C_{n,k}
=
-\frac1nC_{n,k}.
$$

Divide by the duration $\Delta t=1/n$:

$$
\frac{C_{n,k+1}-C_{n,k}}{1/n}
=
-C_{n,k}.
$$

The left-hand side is the discrete rate of change. As $n\to\infty$, the time step tends to zero, and the recursion approaches

$$
\boxed{
\frac{dC}{dt}=-C(t),
\qquad C(0)=1.}
$$

The rate of removal is proportional to the amount of cake currently remaining. The solution is

$$
\boxed{C(t)=e^{-t}.}
$$

The constant $e$ appears because exponential decay is the continuous process whose instantaneous rate is always proportional to its current state.

## The one-unit-time limit

At $t=1$,

$$
C(1)=e^{-1}.
$$

Equivalently,

$$
\lim_{n\to\infty}
\left(1-\frac1n\right)^n
=
e^{-1}
\approx0.36788.
$$

Thus, after one unit of continuous proportional decay,

$$
\boxed{
\begin{aligned}
\text{fraction remaining}
&=e^{-1}\approx36.8\%,\\
\text{fraction removed}
&=1-e^{-1}\approx63.2\%.
\end{aligned}}
$$

The four-round example removes about $68.36\%$. Increasing the number of rounds while decreasing the fraction removed per round moves the result toward $63.2\%$.

## The general decay rate

Suppose the cake is removed at proportional rate $\lambda>0$. For $n>\lambda$, divide time into $n$ rounds and multiply the remainder at each round by

$$
1-\frac{\lambda}{n}.
$$

At time $t=k/n$,

$$
C_{n,\lambda}(t)
=
\left(1-\frac{\lambda}{n}\right)^{nt}.
$$

For fixed $\lambda$ and $t$, letting $n\to\infty$ gives

$$
\boxed{
C_\lambda(t)=e^{-\lambda t}.}
$$

It satisfies

$$
\frac{dC_\lambda}{dt}
=
-\lambda C_\lambda(t).
$$

The parameter $\lambda$ controls the rate, while the recursive structure remains unchanged.

## What the metaphor captures

The cake model makes four structural features visible:

1. **State dependence:** every removal is determined by the current remainder.
2. **Recursion:** each state becomes the input to the next step.
3. **Proportionality:** a smaller remainder produces a smaller subsequent removal.
4. **Continuous limit:** increasingly fine recursive steps converge to exponential decay.

The complete progression is

$$
\boxed{
\text{current cake}
\longrightarrow
\text{proportional removal}
\longrightarrow
\text{new current cake}
\longrightarrow
\cdots
\longrightarrow
e^{-\lambda t}.}
$$

Throughout the model, the cake means the amount currently present. That single state-dependent rule generates the full exponential decay law.
