# Prime Distribution, Explained Carefully

A prime number is easy to define: an integer $n>1$ is prime if its only positive divisors are $1$ and $n$. Describing **where primes occur**, however, requires us to distinguish two different scales.

## Local irregularity and global regularity

Locally, the primes are unevenly spaced. Some occur in close pairs, such as $11,13$ and $41,43$, while prime-free intervals can be arbitrarily long. For example, for every $m\ge 2$, the $m-1$ consecutive integers

$$
(m+1)!+2,\ (m+1)!+3,\ldots,\ (m+1)!+m
$$

are all composite: the term $(m+1)!+k$ is divisible by $k$ for $2\le k\le m$.

Globally, this irregularity has a remarkably stable average. If

$$
\pi(x)=\#\{p\le x:p\text{ is prime}\},
$$

then the **Prime Number Theorem** states that

$$
\pi(x)\sim \frac{x}{\log x}.
$$

Equivalently, the proportion of integers up to $x$ that are prime is approximately $1/\log x$ when $x$ is large. It is common to say heuristically that an integer near $x$ has “probability” about $1/\log x$ of being prime. This is a statement about average density, not a claim that primality itself is random.

The [[Mathematical fundamentals#Zeta function|Riemann zeta function]] connects this average law with finer fluctuations. Through Euler's product,

$$
\zeta(s)=\prod_p\frac{1}{1-p^{-s}},\qquad \Re(s)>1,
$$

it encodes every prime. Explicit formulas in analytic number theory then express weighted prime-counting functions in terms of the zeros of $\zeta(s)$. Those zeros govern oscillations around the main smooth approximation; they are not a simple formula predicting the next prime.

## The sieve picture: periodic exclusions

There is also an elementary and exact way to understand how **candidate primes** are formed. A composite integer $n$ has a prime divisor not exceeding $\sqrt n$. Therefore,

$$
n\text{ is prime}
\quad\Longleftrightarrow\quad
p\nmid n\text{ for every prime }p\le \sqrt n.
$$

Each prime supplies a periodic divisibility test. For a fixed prime $p$, define

$$
b_p(n)=
\begin{cases}
0,&p\mid n,\\
1,&p\nmid n.
\end{cases}
$$

The sequence $b_p(1),b_p(2),\ldots$ has period $p$. For example, with $0$ marking a multiple,

$$
\begin{aligned}
p=2 &: 1,0,1,0,1,0,\ldots,\\
p=3 &: 1,1,0,1,1,0,\ldots.
\end{aligned}
$$

An integer survives sieving by the primes up to $y$ precisely when all the corresponding entries equal $1$. If

$$
P(y)=\prod_{p\le y}p
$$

is the associated **primorial**, then this combined pattern repeats exactly every $P(y)$ integers. The surviving residue classes are precisely those relatively prime to $P(y)$.

This makes the overlap between exclusions precise. Sieving by $2$ removes one half of all integers. Among all integers, sieving next by $3$ removes only one additional sixth: the other multiples of $3$ were already removed as even numbers. More generally, one full period contains

$$
\varphi(P(y))=P(y)\prod_{p\le y}\left(1-\frac1p\right)
$$

survivors, so their exact proportion is

$$
\prod_{p\le y}\left(1-\frac1p\right).
$$

Thus regular periodic filters combine into an increasingly intricate, but still deterministic, pattern. This explains why wheel sieves based on $2,3,5,7,\ldots$ efficiently eliminate composite numbers.

## Why a newly found prime is used from $p^2$

In the sieve of Eratosthenes, after the smaller primes have already been processed, the first **new composite** that must be crossed out using a prime $p$ is $p^2$. Indeed, every smaller multiple

$$
2p,3p,\ldots,(p-1)p
$$

has a factor smaller than $p$ and has therefore already been removed. The prime $p$ itself is retained. Starting at $p^2$ is an efficiency rule; it does not mean that divisibility by $p$ begins there.

To find all primes up to $N$, it is consequently enough to sieve using primes $p\le\sqrt N$. Any composite $n\le N$ must have at least one prime factor no larger than $\sqrt n\le\sqrt N$.

## Recursive exclusion waves

The nested structure can be written as an exact recursion. Put $p_0=1$ and begin with every integer $n\ge2$ marked as a possible prime:

$$
S_0(n)=1.
$$

Given the stage-$k-1$ survivor field, define the next prime to be its first survivor after the preceding prime:

$$
p_k=\min\{n>p_{k-1}:S_{k-1}(n)=1\}.
$$

This produces $p_1=2,p_2=3,p_3=5,\ldots$. Define the exclusion wave introduced by $p_k$ as

$$
W_k(n)=
\begin{cases}
0,&n\ge p_k^2\text{ and }p_k\mid n,\\
1,&\text{otherwise}.
\end{cases}
$$

After introducing the first $k$ prime waves, define the survivor field recursively by

$$
\boxed{S_k(n)=S_{k-1}(n)W_k(n)}.
$$

Equivalently,

$$
S_k(n)=\prod_{i=1}^{k}W_i(n).
$$

This equation gives a precise meaning to the statement that every new wave **contains the result of all previous waves**. The $k$th stage does not rebuild the distribution: it takes the complete survivor field $S_{k-1}$ and removes one new family of multiples. Consequently, the survivor sets

$$
\mathcal S_k=\{n\ge2:S_k(n)=1\}
$$

are nested:

$$
\mathcal S_0\supseteq\mathcal S_1\supseteq\mathcal S_2\supseteq\cdots.
$$

The genuinely new exclusions at stage $k$ are

$$
E_k(n)=S_{k-1}(n)\bigl(1-W_k(n)\bigr).
$$

Thus $E_k(n)=1$ exactly when $n$ survived every earlier wave but is removed by $p_k$. Such an $n$ has $p_k$ as its least prime factor. The first occurrence is $p_k^2$.

The newly discovered prime $p_{k+1}$ then supplies $W_{k+1}$, which produces $S_{k+1}$. Prime discovery and composite exclusion therefore form a recursive feedback process:

$$
S_k\longrightarrow p_{k+1}\longrightarrow W_{k+1}\longrightarrow S_{k+1}.
$$

The periodic nesting can be displayed separately using the untruncated divisibility masks $B_{p_i}$. Define

$$
C_k(n)=\prod_{i=1}^{k}B_{p_i}(n),
\qquad
P_k=\prod_{i=1}^{k}p_i.
$$

Then

$$
C_k(n)=C_{k-1}(n)B_{p_k}(n)
$$

and $C_k$ has period $P_k=P_{k-1}p_k$. Because $C_{k-1}$ has period $P_{k-1}$, one period of the new field begins with $p_k$ repeated copies of the entire preceding pattern; multiplication by $B_{p_k}$ then removes the positions divisible by the new prime. In this exact sense, the $p_k$-wave contains the $p_{k-1}$-wave, which contains the $p_{k-2}$-wave, and so on.

For any fixed $N$, this recursion stabilizes after all primes up to $\sqrt N$ have entered:

$$
S_k(n)=1
\quad\Longleftrightarrow\quad
n\text{ is prime},
\qquad 2\le n\le N,
$$

whenever $p_k\le\sqrt N<p_{k+1}$.

## Prime gaps as recursively refined survivor gaps

The gaps are not separate from the distribution; they are derived from its ordered survivors. At stage $k$, list the surviving candidates in increasing order:

$$
s_1^{(k)}<s_2^{(k)}<s_3^{(k)}<\cdots,
$$

and define the stage-$k$ gaps by

$$
g_j^{(k)}=s_{j+1}^{(k)}-s_j^{(k)}.
$$

Introducing $W_{k+1}$ deletes some members of this list. Whenever one survivor $s_j^{(k)}$ is deleted, its two neighboring gaps merge:

$$
g_{j-1}^{(k)}+g_j^{(k)}
=
\bigl(s_j^{(k)}-s_{j-1}^{(k)}\bigr)
+
\bigl(s_{j+1}^{(k)}-s_j^{(k)}\bigr)
=
s_{j+1}^{(k)}-s_{j-1}^{(k)}.
$$

Hence each new prime wave recursively transforms the previous gap pattern by deleting newly excluded candidates and joining the adjacent gaps. After the sieve has included every prime up to $\sqrt N$, the surviving candidates up to $N$ are the actual primes, and the stabilized values $g_j^{(k)}$ in that range are the actual prime gaps.

This gives a direct hierarchy:

$$
\text{previous survivor field}
\longrightarrow
\text{new prime wave}
\longrightarrow
\text{refined survivor field}
\longrightarrow
\text{refined gaps}.
$$

Statistical gap estimates summarize this recursively generated gap sequence; they do not define an independent phenomenon.

## What this does—and does not—explain

The sieve gives a concrete structural explanation for primality:

> primes are the integers greater than $1$ that survive all relevant periodic divisibility filters.

It also explains why local patterns appear nested: adding a prime $p$ refines the previous pattern into one with a period multiplied by $p$. Yet surviving a finite collection of filters does not guarantee primality. For example, $49$ survives the filters for $2$, $3$, and $5$, but is composite because $7\mid49$.

Most importantly, these divisibility filters **do determine the prime distribution exactly**. To recover every prime up to $N$, apply the filters for all primes $p\le\sqrt N$; the surviving integers greater than $1$ are precisely the primes. In this constructive sense, no additional principle is needed to explain where the primes come from.

What does not follow immediately from the elementary product of survivor proportions is a compact quantitative description of the resulting distribution. For example, the product alone does not prove

$$
\pi(x)\sim\frac{x}{\log x},
$$

give a sharp error term for this approximation, or describe the possible sizes of prime gaps. Such results ask us to summarize the cumulative effect of many exact filters without explicitly sieving every integer. Sieve theory studies that cumulative exclusion directly, while analytic number theory—including the zeta function—encodes and estimates the same arithmetic structure by different methods.

So the balanced conclusion is:

- Primes are deterministic, not intrinsically random.
- Their local occurrence is irregular and difficult to predict.
- Their large-scale density follows the precise asymptotic law $1/\log x$.
- Periodic divisibility filters completely determine the distribution; deeper theorems provide compressed estimates of its density, fluctuations, and gaps.
