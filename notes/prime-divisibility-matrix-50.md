# Prime Divisibility Matrix, 1–50

This note develops a sieve-like observation table for the numbers from 1 to 50. Its purpose is not merely to identify prime numbers, but to make visible **how divisibility provides evidence for excluding composite candidates**.

The same idea is developed at three levels:

1. **Intuitive language** — what the idea means in ordinary terms.
2. **Functional language** — how the procedure operates.
3. **Mathematical language** — how the observation is represented formally.

We begin with the idea of primality itself. Only after that do we introduce the matrix as a formal way to record the divisibility evidence.

## 1. Prime Definition

### Intuitive language

A prime number is a number that cannot be built by multiplying two smaller positive integers.

Put differently, a prime has no proper divisor other than `1`.

There is one important convention to state explicitly: **in standard mathematics, 1 is not prime**. In the observation system developed in this note, however, `1` is retained as a special surviving starting value. This should be understood as a convention of the observation system, not as the standard mathematical classification of 1 as a prime.

### Functional language

To determine whether a candidate `n` is prime, we test whether any smaller number divides it exactly:
- If a proper divisor is found, the candidate is excluded as prime.
- If no proper divisor is found, the candidate survives the divisibility tests and is prime.

In practice, it is sufficient to test prime divisors up to $\sqrt n$. In this note we will later record a broader set of divisibility relationships so that the structure can be observed directly. We assume no prior knowledge from the reader.

### Mathematical language

A prime is a number $n$ that cannot be divided by a number $d$ with no remainder.

So, for an integer $n>1$, $n$ is prime if and only if there is no integer $d$ satisfying

$$
1<d<n
$$

such that $d$ divides $n$ exactly, in other words

$$
d\mid n.
$$

Equivalently,

$$
n \bmod d \neq 0
$$

for every proper divisor candidate $d$ with $1<d<n$.

These divisibility statements will later be turned into a structured representation.

---

## 2. First Example

Consider the candidate `5`. The smaller possible divisors are `2`, `3`, and `4`.

- $5\bmod 2\neq 0$
- $5\bmod 3\neq 0$
- $5\bmod 4\neq 0$

No proper divisor is found. Therefore `5` survives the test and is prime.

By contrast, consider `6`:

- $6\bmod 2=0$
- $6\bmod 3=0$

The first successful divisibility test is already enough to exclude `6` as prime.

This example already shows the two key ideas: some candidates survive, and others are excluded because a divisor has been found.

---

## 3. Relation to the Sieve of Eratosthenes

The construction resembles the Sieve of Eratosthenes. In the classical sieve, once a prime is identified, its multiples are crossed out. The process progressively removes composite candidates.

Here we introduce the matrix representation. Instead of simply crossing out a composite number, we record the crossing-out pattern itself.

For a given prime, its column shows a repeating divisibility rhythm:

```text
2 → 0101010101...
3 → 001001001...
5 → 0000100001...
```

These patterns mark the multiples of the prime:

```text
2 marks every second number
3 marks every third number
5 marks every fifth number
```

So the matrix does more than list surviving primes. It shows the repeating exclusion patterns produced by each prime, and from those patterns the surviving candidates can be read.

---

## 4. Matrix Construction

We are now ready to turn the number prime-evaluation idea into a visible structure. Each row will represent one candidate number. Each column will represent a possible divisor. A cell then records whether that divisor excludes that candidate.

Before writing this formally, it helps to see a small version of the matrix first. The rows highlighted below are not prime, so they show visible exclusion evidence.

| n\d                              | 1              | 2              | 3              | 4                               | 5              | 6                               | 7              | 8                               | 9                               | 10                              |
| -------------------------------- | -------------- | -------------- | -------------- | ------------------------------- | -------------- | ------------------------------- | -------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `1`                              | **1**          |                |                |                                 |                |                                 |                |                                 |                                 |                                 |
| `2`                              | 0              | **1**          |                |                                 |                |                                 |                |                                 |                                 |                                 |
| `3`                              | 0              | 0              | **1**          |                                 |                |                                 |                |                                 |                                 |                                 |
| <mark><strong>4</strong></mark>  | <mark>0</mark> | <mark>1</mark> | <mark>0</mark> | <mark><strong>0</strong></mark> |                |                                 |                |                                 |                                 |                                 |
| `5`                              | 0              | 0              | 0              | 0                               | **1**          |                                 |                |                                 |                                 |                                 |
| <mark><strong>6</strong></mark>  | <mark>0</mark> | <mark>1</mark> | <mark>1</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark><strong>0</strong></mark> |                |                                 |                                 |                                 |
| `7`                              | 0              | 0              | 0              | 0                               | 0              | 0                               | **1**          |                                 |                                 |                                 |
| <mark><strong>8</strong></mark>  | <mark>0</mark> | <mark>1</mark> | <mark>0</mark> | <mark>1</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark><strong>0</strong></mark> |                                 |                                 |
| <mark><strong>9</strong></mark>  | <mark>0</mark> | <mark>0</mark> | <mark>1</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark><strong>0</strong></mark> |                                 |
| <mark><strong>10</strong></mark> | <mark>0</mark> | <mark>1</mark> | <mark>0</mark> | <mark>0</mark>                  | <mark>1</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark>0</mark>                  | <mark><strong>0</strong></mark> |
### From the visible matrix to a formal rule

We can now describe what each cell means more precisely. Let $n$ denote the candidate number represented by a row, and let $d$ denote the possible divisor represented by a column. For example, the `1` in row `6`, column `2` tells us that **2 divides 6 exactly**. The `1` in row `6`, column `3` tells us that **3 divides 6 exactly**.

We can represent this divisibility result with a function called $D(n,d)$. Here, $D(n,d)$ simply means:

> **the result of testing whether $d$ divides $n$.**

We define it as follows:

$$
D(n,d)=
\begin{cases}
1, & d\mid n,\\
0, & d\nmid n.
\end{cases}
$$

So the meaning is straightforward:

- $D(n,d)=1$ means **$d$ divides $n$ exactly**.
- $D(n,d)=0$ means **$d$ does not divide $n$ exactly**.

### Connecting divisibility to remainders

There is another way to say that one number divides another exactly. If $d$ divides $n$, then dividing $n$ by $d$ leaves **no remainder**. The mathematical operation that gives us the remainder is called $\bmod$.

Thus:

$$
n \bmod d
$$

means:

> **the remainder left when $n$ is divided by $d$.**

For example:

$$
6 \bmod 2 = 0
$$

because 6 divided by 2 leaves no remainder. Likewise:

$$
7 \bmod 2 = 1
$$

because 7 divided by 2 leaves a remainder of 1. Therefore, a divisor test can be written mathematically as:

$$
D(n,d)=1 \quad \text{when} \quad n\bmod d=0.
$$

In more compact mathematical notation, we can write:

$$
D(n,d)=1 \Longleftrightarrow n\bmod d=0.
$$

The symbol `⇔` means **“if and only if.”** In this context, it tells us that the two statements describe exactly the same condition:

> $D(n,d)=1$ **if and only if** $n\bmod d=0$.


So the three language levels are now connected:
- Intuitive language: $d$ divides $n$ exactly.
- Functional language: test whether dividing $n$ by $d$ leaves a remainder.
- Mathematical language: $n\bmod d=0$.

### Why the matrix is triangular

Only proper divisors can exclude a candidate as prime. A proper divisor of $n$ is a divisor that is smaller than $n$ itself. Therefore, once we reach a column where

$$
d>n
$$

that column cannot provide exclusion evidence for row `n`. Those cells are therefore left empty. The matrix naturally takes on a triangular form:

```text
        divisors d →
        1  2  3  4  5  6  ...
candidate n
       ↓
       1  *
       2  *  *
       3  *  *  *
       4  *  *  *  *
       ...
```

The stars here simply represent cells that belong to the triangular region. In the actual matrix, the cells to the right of the diagonal are left empty.

## 5. The row as an evidence vector

At this point, each row can be viewed as more than a collection of independent cells. The row is a vector of observations about one candidate number. For example, row 10 contains divisibility evidence such as:

```text
     1  2  3  4  5  6  7  8  9
...
10:  0  1  0  0  1  0  0  0  0  ...
```

The `1` in column 2 tells us that 2 divides 10. The `1` in column 5 tells us that 5 divides 10. Taken together, these values form an **evidence vector** describing how the candidate relates to the possible divisors. The vector therefore contains more information than the final answer alone.
The final question is then:

> **How do we turn this vector of evidence into a single result?**

For primality, the answer is straightforward: if any proper-divisor position contains a `1`, the candidate is excluded. If none does, the candidate survives. The diagonal can therefore be understood as a **row-level readout**. It is not another divisibility observation. Instead, it **encodes the result** of evaluating the row as a whole.

The diagonal indicates given a number `n`, if that number is a prime `1` or not `0`. 

```text
     1  2  3  4  5  6  7  8  9 10 11 12
     1  1  1  0  1  0  1  0  0  0  1  0 ...
```

The matrix thus holds the results as well as the evidence vector. The diagonal tells us simply **the primality result for `n`** given the row's evidence vector. The “survival” is the process that produces that result.

| n\d                              | 1              | 2              | 3              | 4                               | 5              | 6                               | 7              | 8                               | 9                               | 10                              |
| -------------------------------- | -------------- | -------------- | -------------- | ------------------------------- | -------------- | ------------------------------- | -------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `1`                              | **1**          |                |                |                                 |                |                                 |                |                                 |                                 |                                 |
| `2`                              | 0              | **1**          |                |                                 |                |                                 |                |                                 |                                 |                                 |
| `3`                              | 0              | 0              | **1**          |                                 |                |                                 |                |                                 |                                 |                                 |
| <mark><strong>4</strong></mark>  | <mark>0</mark> | <mark>1</mark> | <mark>0</mark> | <mark><strong>0</strong></mark> |                |                                 |                |                                 |                                 |                                 |
| `5`                              | 0              | 0              | 0              | 0                               | **1**          |                                 |                |                                 |                                 |                                 |
| <mark><strong>6</strong></mark>  | <mark>0</mark> | <mark>1</mark> | <mark>1</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark><strong>0</strong></mark> |                |                                 |                                 |                                 |
| `7`                              | 0              | 0              | 0              | 0                               | 0              | 0                               | **1**          |                                 |                                 |                                 |
| <mark><strong>8</strong></mark>  | <mark>0</mark> | <mark>1</mark> | <mark>0</mark> | <mark>1</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark><strong>0</strong></mark> |                                 |                                 |
| <mark><strong>9</strong></mark>  | <mark>0</mark> | <mark>0</mark> | <mark>1</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark><strong>0</strong></mark> |                                 |
| <mark><strong>10</strong></mark> | <mark>0</mark> | <mark>1</mark> | <mark>0</mark> | <mark>0</mark>                  | <mark>1</mark> | <mark>0</mark>                  | <mark>0</mark> | <mark>0</mark>                  | <mark>0</mark>                  | <mark><strong>0</strong></mark> |
Conceptually:

```text
row of divisibility evidence
            ↓
     evaluate the row
            ↓
       prime or composite
            ↓
     encode the result
            ↓
       diagonal value
```

Thus:

```text
diagonal = 1  → candidate survives
diagonal = 0  → candidate is excluded
```

The diagonal is therefore a compact encoding of the meaning extracted from the row.

### Examples

For example, row 10 contains divisibility evidence at columns 2 and 5:

```text
10 → [0, 1, 0, 0, 1, 0, 0, 0, 0, ...]
```

Because the row contains evidence of proper divisibility, its result is composite:

```text
row 10
   ↓
proper divisor found
   ↓
composite
   ↓
diagonal = 0
```

Conversely, row 7 contains no evidence of a proper divisor:

```text
7 → [0, 0, 0, 0, 0, 0, ...]
```

so its row-level result is prime:

```text
row 7
   ↓
no proper divisor found
   ↓
prime
   ↓
diagonal = 1
```

The matrix therefore contains **both the evidence and the result**.

The off-diagonal cells preserve the divisibility evidence produced by the underlying rules. The diagonal provides a compact encoding of the result obtained from that evidence.

In this sense, a row can be viewed as an evidence vector together with a row-level readout:

```text
        evidence vector
              │
              ▼
      [0 1 0 0 1 0 ...]
              │
              ▼
        row evaluation
              │
              ▼
      prime / composite
              │
              ▼
        encoded as 1 / 0
              │
              ▼
           diagonal
```

The matrix thus does not merely give us the set of primes. It preserves some of the structure that **produces** that set: the divisibility relationships are represented in the rows and columns, while the diagonal encodes the resulting prime/composite classification.

### From rules to encoded results

This distinction becomes particularly interesting when we step back from the matrix. The matrix is generated by a set of rules:
- numbers are candidates;
- columns represent possible divisors;
- divisibility determines whether a cell receives `1` or `0`;
- proper divisibility provides evidence of compositeness;
- the row is evaluated according to those rules;
- the resulting classification is encoded in the diagonal.

The important point is that the **rules generate the observations**. The prime/composite label is therefore not the whole mathematical object. It is the result of applying a rule system to a candidate. We can express this conceptually as:

```text
candidate
    ↓
rule system
    ↓
divisibility observations
    ↓
evidence vector
    ↓
row evaluation
    ↓
encoded result
```

This gives us two different things to observe:

1. **the result** — prime or composite;
2. **the rule-derived structure that produced the result**.

Traditional presentations of prime numbers tend to emphasize the first. We list the primes, study their distribution, density, gaps, irregularities, correlations, and deviations from expected patterns. The matrix makes the second visible.

Instead of asking only:

> **Which numbers are prime, and what patterns do their results exhibit?**

we can also ask:

> **What pattern of rule-derived evidence causes a number to survive as prime or be excluded as composite?**

That shift in perspective is important.

> **What appears irregular in the prime sequence is the superposition of regular exclusion patterns generated by divisibility.**

## 6. The matrix as an encoding system

The matrix can therefore be viewed as an encoding of the relationships generated by the divisibility rules. A column does not merely contain arbitrary `0`s and `1`s. Its pattern is generated by a rule.

For example, column 2 encodes:

```text
"n is divisible by 2"
```

Its `1`s occur at:

```text
2, 4, 6, 8, 10, 12, ...
```

Column 3 encodes:

```text
"n is divisible by 3"
```

Its `1`s occur at:

```text
3, 6, 9, 12, 15, ...
```


The matrix is therefore not simply storing answers; it is **encoding the consequences of a collection of rules**. Each row represents the behaviour of one candidate under those rules, while each column represents the pattern produced by a particular rule. The diagonal provides a compact encoding of the resulting prime/composite classification.


```text
                 RULES
                   ↓
        ┌─────────────────────┐
        │     divisibility    │
        │     relationships   │
        └─────────────────────┘
                   ↓
                MATRIX
          ┌─────────────────┐
          │    evidence     │
          │    vectors      │
          └─────────────────┘
                   ↓
              ROW READOUT
                   ↓
             encoded result
            prime / composite
```

The matrix therefore preserves something that is easily lost when we look only at the final prime sequence: **the individual regular patterns that contribute to the result**. What appears irregular in the output can be decomposed into the regular exclusion patterns encoded by the columns. This connects to a more general idea in computing and information processing:

> **A representation can encode the consequences of a set of rules without explicitly storing the rules themselves.**

The rules generate the structure; the representation preserves that structure so that it can be observed, combined, and interpreted. We can therefore define **compositional irregularity** as the apparent irregularity of the prime sequence arising from the interaction of multiple regular exclusion patterns. The primes are not irregular because their underlying components are irregular, but because **regular components compose into a pattern whose structure is difficult to recognize once their contributions are combined**.

```text
regular      regular      regular
  ↓             ↓            ↓
2-pattern     3-pattern    5-pattern
      \          |          /
       \         |         /
        └── composition ──┘
                 ↓
        apparently irregular
             prime pattern
```

In this sense:

> **Prime irregularity is representational: it appears when the underlying rule contributions are collapsed into a single binary sequence.**

This connects directly to the broader representation/LLM argument: **apparent irregularity can arise when information about generating structure is compressed or collapsed into a less expressive representation.**

## 7. Reading the encoded structure

Once the matrix is understood as an encoding of rule-derived evidence, we can stop treating its cells as isolated divisibility tests and begin reading the structures formed by them. 

There are three natural directions:
- The rows tell us how individual candidates behave under the divisibility rules.
- The columns tell us how individual rules act across the candidate range.
- The diagonal tells us which candidates survive the complete row evaluation.

```text
             MATRIX
          /     |      \
         ↓      ↓       ↓
      rows   columns  diagonal
       ↓       ↓        ↓
    candidates rules   results
```

This gives us three complementary views of the same system:

> **The row describes a candidate. The column describes a rule. The diagonal describes the resulting classification.**

The important point is that these are not three independent datasets. They are different projections of the same underlying rule system.

### Reading a row

A row can be read as an explanation of why a particular candidate survives or is excluded.

Consider `10`:

```text
10 → [0, 1, 0, 0, 1, 0, 0, 0, 0]
```

The vector contains two proper-divisor witnesses:

```text
2 | 10
5 | 10
```

The candidate is therefore excluded.

Now consider `11`:

```text
11 → [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

No proper divisor appears in the row. The candidate survives.

The distinction can therefore be expressed as:
- **composite**: evidence vector contains a proper-divisor witness
- **prime**: evidence vector contains no proper-divisor witness

The row is consequently more informative than the final classification alone. If we were given only:

```text
10 → composite
11 → prime
```

we would know the results, but not the evidence represented by the matrix. The matrix preserves that additional information.

#### Multiple witnesses

A composite candidate may have more than one witness. For example:

```text
12 → [0, 1, 1, 1, 0, 1, 0, ...]
```

Here `12` is divisible by:

```text
2, 3, 4, 6
```

Any one of these is sufficient to establish that `12` is composite. The remaining `1`s nevertheless preserve additional structure. This distinction is useful:

> **A witness is sufficient for classification; the complete evidence vector is useful for structural observation.**

That is one of the reasons to retain the full matrix even though a more efficient primality test would inspect far fewer cells.

### Reading a column

The column provides the complementary perspective.

Instead of asking:

> Which divisors apply to this candidate?

we ask:

> Which candidates are affected by this divisor?

Consider column `2`:

```text
n:  1 2 3 4 5 6 7 8 9 10 11 12 ...
    0 1 0 1 0 1 0 1 0  1  0  1 ...
```

The `1`s occur at the multiples of `2`:

```text
2, 4, 6, 8, 10, 12, ...
```

Column `3` produces:

```text
0 0 1 0 0 1 0 0 1 0 0 1 ...
```

and therefore marks:

```text
3, 6, 9, 12, 15, ...
```

Column `5` marks:

```text
5, 10, 15, 20, 25, ...
```

The important observation is that these columns are not arbitrary binary sequences.

Each one is generated by a simple rule:

```text
column d
    ↓
mark every multiple of d
```

Thus a column can be viewed as the **spatial expression of a rule** across the candidate range.

## 8. Structural observations from the matrix

The preceding sections established that the prime/composite sequence is a compressed readout of a richer divisibility structure. We can now ask what additional structure becomes visible when the matrix itself, rather than only its diagonal, is treated as the object of observation.

Several properties become important.

The prime columns are periodic. Their contributions are not all independent. A newly discovered prime does not immediately contribute new exclusion information. The set of relevant prime rules changes with the observation horizon. Most importantly, the output of the matrix participates in generating the rules by which later outputs are determined.

These properties reveal that the matrix is not merely a static table of divisibility relationships. It is a recursively generated exclusion system.

### 8.1 Prime columns as periodic binary signals

For a prime $p$, define its divisibility signal by

$$
D_p(n)=
\begin{cases}
1, & p\mid n,\\
0, & p\nmid n.
\end{cases}
$$

For $p=2$,

```text
0 1 0 1 0 1 0 1 ...
```

For $p=3$,

```text
0 0 1 0 0 1 0 0 1 ...
```

and for $p=5$,

```text
0 0 0 0 1 0 0 0 0 1 ...
```

Each signal has period $p$:

$$
D_p(n+p)=D_p(n).
$$

A prime column can therefore be regarded as a periodic binary signal distributed across the number line.

The matrix is consequently built from regular periodic components even though its final prime readout is not itself periodic.

### 8.2 Prime columns as fundamental generators

Composite divisor columns do not introduce fundamentally new evidence for primality. If a composite divisor $d$ divides $n$, then at least one prime factor of $d$ also divides $n$.

Therefore,

$$
d\mid n \quad\Longrightarrow\quad p\mid n
$$

for some prime $p\mid d$.

A composite column can therefore provide additional factorization information, but it is not required to determine whether a candidate is composite. The fundamental exclusion generators are the prime columns. This allows the matrix to be reduced conceptually from

```text
all divisor rules
```

to

```text
prime-generated divisor rules.
```

### 8.3 The activation point $p^2$

Although the divisibility signal of prime $p$ is periodic from the beginning, the prime does not become necessary as an exclusion rule immediately.

Consider the multiples

$$
2p,3p,\ldots,(p-1)p.
$$

For any multiplier $k<p$, $k$ contains a prime factor smaller than $p$. Consequently, the candidate $kp$ has already been excluded by a smaller prime rule.

The first composite multiple of $p$ whose smallest prime divisor is $p$ itself is therefore

$$
p^2.
$$

For example,

$$
5\times2=10,\qquad 5\times3=15,\qquad 5\times4=20
$$

have already been excluded by 2 or 3.

But

$$
5^2=25
$$

requires the prime rule 5.

Thus $p$ and $p^2$ play different roles:

```text
p   → discovery of the prime generator
p²  → first indispensable use of that generator
```

We will call $p^2$ the activation point of the prime rule.

### 8.4 The square-root activation frontier

The $p^2$ activation property determines which prime generators can be relevant at a finite observation horizon $x$.

A prime $p$ can have reached its activation point only when

$$
p^2\leq x.
$$

Equivalently,

$$
p\leq\sqrt{x}.
$$

Thus all candidates up to $x$ can be classified using the prime rules

$$
A(x)=\{p\in\mathbb P:p\leq\sqrt{x}\}.
$$

The familiar square-root bound is therefore more than a computational optimization in this representation.

It defines a moving boundary between prime rules that can already contribute indispensable exclusion information and prime rules whose activation points lie beyond the current observation horizon.

We can call this the square-root activation frontier.

An additional geometric property appears if both axes are expressed logarithmically.

Let

$$
u=\log x
$$

and

$$
v=\log p.
$$

The activation relation

$$
p^2=x
$$

then becomes

$$
2v=u,
$$

or

$$
v=\frac12u.
$$

Thus the curved square-root frontier in ordinary coordinates becomes a straight half-scale boundary in logarithmic coordinates.

No interpretation beyond the matrix is required at this stage. It is simply an intrinsic geometric property of the prime-exclusion construction.

### 8.5 Diagonal-to-column feedback

The matrix contains an important recursive relationship between its output and its future rules.

A candidate $n$ is evaluated against the prime exclusion rules already available.

If one of those rules excludes $n$, the diagonal records

$$
P(n)=0.
$$

If none excludes it, the candidate survives and the diagonal records

$$
P(n)=1.
$$

When that surviving candidate is greater than 1, it is a new prime.

The important point is that this result does not remain only a result.

The newly discovered prime becomes a new fundamental divisor column.

Thus:

```text
existing prime generators
          ↓
evaluate candidate n
          ↓
candidate survives
          ↓
diagonal(n) = 1
          ↓
n becomes new prime p
          ↓
new periodic p-rule
          ↓
activation at p²
          ↓
future candidates are evaluated
against the enlarged rule system
```

The diagonal therefore participates in generating the future columns of the matrix.

This creates a feedback relation:

```text
RULES
  ↓
RESULT
  ↓
NEW RULE
  ↓
FUTURE RESULT
```

The prime system can consequently be described as recursively self-generating.

A prime is recognized by observing the exclusion structure generated by previous primes. Once recognized, it becomes part of that exclusion structure for future candidates.

The same object therefore has two roles:

```text
prime as result
      ↓
prime as generator
```

### 8.6 Two forms of depth

The matrix also reveals two different notions that should not be conflated.

An individual number has a factorization depth. A standard measure is

$$
\Omega(n),
$$

the number of prime factors of $n$, counted with multiplicity.

For example,

$$
12=2^2\times3
$$

gives

$$
\Omega(12)=3.
$$

The complete system has a different form of depth.

At observation horizon $x$, the number of prime exclusion generators whose activation points can already have been reached is

$$
H(x)=\pi(\sqrt{x}).
$$

This quantity describes the active rule depth of the exclusion system rather than the internal factor composition of a single candidate.

Thus:

```text
Ω(n)       → candidate composition
π(√x)      → active exclusion depth
```

They represent two different coordinates of the same matrix.

### 8.7 From periodic bits to harmonic phase

The periodic prime columns can also be represented harmonically.

For prime $p$,

$$
D_p(n)=1_{\{p\mid n\}}
$$

has the exact representation

$$
D_p(n)=\frac{1}{p}\sum_{k=0}^{p-1} e^{2\pi i kn/p}.
$$

This is not an approximation of the divisibility signal.

It reproduces the binary sequence exactly.

When $p\mid n$, all phase terms align and the sum equals $p$:

$$
D_p(n)=1.
$$

When $p\nmid n$, the phase terms are distributed around the unit circle and cancel:

$$
D_p(n)=0.
$$

For $p=3$, the same expression can be written entirely with a cosine:

$$
D_3(n)=\frac13\left(1+2\cos\frac{2\pi n}{3}\right).
$$

The periodic binary exclusion vector can therefore be observed in two equivalent representations:

```text
binary representation
        ↕
harmonic phase representation
```

The column that appeared as a repeating sequence of 0s and 1s can equally be regarded as the result of periodic phase alignment and cancellation.

This provides an exact mathematical meaning for describing the prime exclusion vectors as periodic signals or waves.

### 8.8 The combined prime-exclusion operator

The individual prime signals can now be recombined.

For $n>1$, define

$$
P(n)=\prod_{\substack{p\leq\sqrt n\\p\in\mathbb P}}\left(1-D_p(n)\right).
$$

If some active prime divides $n$, one factor becomes zero and therefore

$$
P(n)=0.
$$

If no active prime divides $n$, every factor remains one and

$$
P(n)=1.
$$

Thus the prime readout can be represented as

```text
periodic prime signals
          ↓
active primes p ≤ √n
          ↓
product of their complements
          ↓
survival / exclusion
          ↓
prime bit
```

The familiar prime sequence is therefore the final binary projection of a dynamically bounded composition of prime-generated periodic signals.

The matrix reveals both the signals and the mechanism by which their combined action produces that projection.

## 9. Foundational endpoint

The purpose of this note is basic: to reconstruct the prime distribution from the divisibility relationships that generate it, and to identify which structural properties become visible when those relationships are retained rather than collapsed immediately into the final prime sequence.

Starting from the divisibility matrix, we observed the following progression:

$$
\boxed{
\text{periodic exclusion}
\rightarrow
\text{recursive prime generation}
\rightarrow
p^2\text{ activation}
\rightarrow
\sqrt{x}\text{ frontier}
\rightarrow
\text{half-scale geometry}
\rightarrow
\text{harmonic representation}
}
$$

Each step follows from a different property of the same underlying system.

### Periodic exclusion

Every prime $p$ generates a periodic divisibility signal across the number line.

$$
D_p(n+p)=D_p(n).
$$

The prime distribution therefore arises from the interaction of regular periodic exclusion structures.

### Recursive prime generation

The system is not supplied with the complete prime set in advance.

Previously discovered primes generate the exclusion structure against which later candidates are evaluated.

A surviving candidate becomes a new prime, and that prime subsequently becomes a new exclusion generator.

Thus:

```text
existing prime rules
        ↓
evaluate candidate
        ↓
candidate survives
        ↓
new prime
        ↓
new prime rule
        ↓
future evaluation
```

The result of the system therefore participates in generating the future structure of the system.

### $p^2$ activation

A newly discovered prime $p$ has a periodic divisibility pattern immediately, but it does not provide indispensable new exclusion information until

$$
p^2.
$$

Before $p^2$, every composite multiple of $p$ has already been excluded by a smaller prime.

The point $p^2$ therefore marks the first candidate for which the prime $p$ becomes necessary as the smallest exclusion witness.

### The $\sqrt{x}$ frontier

For a finite observation horizon $x$, a prime rule can have reached its activation point only when

$$
p^2\leq x.
$$

Equivalently,

$$
p\leq\sqrt{x}.
$$

The square-root relation therefore defines the moving boundary of the prime rules required to classify the system up to $x$.

It is not only a computational shortcut. Within this representation it is a structural frontier.

### Half-scale geometry

When the candidate scale and prime scale are represented logarithmically,

$$
u=\log x,\qquad v=\log p,
$$

the activation relation

$$
p^2=x
$$

becomes

$$
v=\frac12u.
$$

The square-root frontier therefore becomes a linear half-scale boundary in logarithmic coordinates.

This factor $1/2$ arises directly from the geometry of prime-rule activation.

No further interpretation of that factor is made in this note.

### Harmonic representation

Finally, the periodic binary exclusion signals admit an exact harmonic representation.

For prime $p$,

$$
D_p(n)=\frac{1}{p}\sum_{k=0}^{p-1} e^{2\pi i kn/p}.
$$

The binary exclusion vector can therefore be represented equivalently as a finite system of periodic phases.

Its binary values arise from phase alignment and cancellation.

Thus the same prime rule may be observed in two representations:

```text
periodic binary exclusion
          ↕
periodic harmonic phase
```

The harmonic representation does not introduce a different prime-generating mechanism. It provides a different mathematical language for observing the same periodic structure.

---

### What has been established

The matrix reveals that the prime sequence is not being generated as an isolated irregular sequence. It is the surviving readout of a recursively expanding collection of periodic exclusion rules.

Those rules have:

- precise periodic structure;
    
- a recursive mechanism of generation;
    
- activation thresholds at $p^2$;
    
- a moving active boundary at $\sqrt{x}$;
    
- a half-scale form under logarithmic coordinates;
    
- and an exact harmonic representation.
    

The foundational object developed in this note can therefore be summarized as:

```text
prime-generated periodic rules
            ↓
recursive exclusion system
            ↓
dynamically bounded active rule set
            ↓
combined divisibility evidence
            ↓
surviving candidates
            ↓
prime sequence
```

The prime sequence is the visible result.

The exclusion system is the generative structure beneath it.

The purpose of this note has been to make that structure explicit.

Any later comparison with analytic representations of the prime distribution should begin from this object rather than from the prime sequence alone.
