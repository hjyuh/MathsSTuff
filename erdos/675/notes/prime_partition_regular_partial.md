# EP675 lane G: regular and random dense prime partitions

Problem page: https://www.erdosproblems.com/675

## 1. Goal of this lane

EP675 asks, among other things, whether a dense partition of the primes

```text
Primes = P sqcup Q
```

can give a translation-property set

```text
A = S(P) = {m >= 1 : every prime divisor of m lies in P}.
```

The earlier reduction in `prime_partition.md` showed that, for a fixed prefix
`[1,n]`, the nonmember side can be frozen by taking

```text
M_n = product_{q in Q, q <= n} q.
```

Then it is enough to find `s` such that

```text
M_n s + a in S(P)       for every a in S(P) cap [1,n].
```

This note records three levels of partial theorem:

1. finite forbidden prime sets;
2. a deterministic "linear forms recurrence" criterion;
3. a genuinely useful random dense partition theorem.

The third item is the strongest output of this lane.

## 2. Finite forbidden primes

This is the clean baseline.

### Proposition 2.1

If `Q` is finite and `P` is its complement in the primes, then

```text
S(P) = {m : no prime from Q divides m}
```

has the translation property.

### Proof

Let

```text
M = product_{q in Q} q.
```

For every `a` and every `q in Q`,

```text
a + M == a mod q.
```

Therefore `q | a` if and only if `q | a+M`. Hence `a in S(P)` if and only if
`a+M in S(P)`. The same single shift works for every prefix.

This is not dense in the sense of the problem, but it is the exact finite
model behind the CRT-freezing argument.

## 3. Deterministic finite-pattern criterion

For a general partition, define

```text
F_n = S(P) cap [1,n],
M_n = product_{q in Q, q <= n} q.
```

### Lemma 3.1

If there is an integer `s >= 1` such that

```text
M_n s + a in S(P)       for every a in F_n,
```

then

```text
t_n = M_n s
```

is a translation witness for `S(P)` on `[1,n]`.

### Proof

For `a in F_n`, the conclusion is exactly the hypothesis.

If `1 <= b <= n` and `b notin S(P)`, then some `q in Q` divides `b`. Since
`q <= b <= n`, one has `q | M_n`, and therefore

```text
b + M_n s == b == 0 mod q.
```

Thus `b+M_n s notin S(P)`.

This proves the lemma.

### Deterministic regularity hypothesis

The lemma shows that a sufficient condition is:

> For every `n`, the finite tuple of forms
>
> ```text
> L_a(s) = M_n s + a,       a in F_n,
> ```
>
> simultaneously takes values in `S(P)`.

Equivalently, a dense prime partition is good if the multiplicative semigroup
`S(P)` is recurrent along every finite admissible one-variable linear pattern
that arises from this construction.

This is a useful interface, but by itself it is not a proof. For arbitrary
dense partitions it remains a hard global distribution assertion.

## 4. Standard sieve input: almost-prime linear tuples

The random theorem below uses the following standard consequence of Brun's
combinatorial sieve.

### Lemma 4.1: almost-prime tuple lemma

Let

```text
L_1(s), ..., L_m(s)
```

be integer affine-linear forms with positive leading coefficients. Let `R` be
a finite set of primes that we are allowed to ignore. Suppose that outside
`R` the tuple has no local obstruction: for every prime `ell notin R`, there
is a residue class `s mod ell` for which

```text
ell does not divide L_1(s) ... L_m(s).
```

Then there is a constant `C_m` and infinitely many integers `s` for which the
product

```text
L_1(s) ... L_m(s)
```

has at most `C_m` prime factors outside `R`, counted without multiplicity.

Moreover, the same remains true after imposing finitely many additional
avoidance conditions

```text
ell does not divide L_1(s) ... L_m(s)
```

at any prescribed finite set of primes `ell notin R`.

### Proof status

This is a standard Brun/linear-sieve theorem for admissible tuples of linear
forms. A public write-up should cite a precise source, for example
Halberstam--Richert or Greaves. The proof idea is simple:

1. choose a residue class satisfying the finitely many local conditions;
2. sieve the sequence `prod_i L_i(s)` for primes below `X^(1/u)`;
3. for `u` large enough relative to `m`, the lower-bound sieve leaves many
   values;
4. any surviving product is `O(X^m)` and has no prime factor below
   `X^(1/u)`, so it has at most `m u + O(1)` prime factors.

The exact value of `C_m` is irrelevant for EP675.

## 5. Random dense prime partitions

Now choose a random prime partition as follows. Fix `alpha in (0,1)`. For
each prime `p`, independently put

```text
p in P with probability alpha,
p in Q with probability 1-alpha.
```

### Theorem 5.1

Assuming Lemma 4.1, the random set

```text
A = S(P)
```

has the translation property almost surely.

Moreover, almost surely both `P` and `Q` are dense prime sets:

```text
pi_P(x) ~ alpha pi(x),
pi_Q(x) ~ (1-alpha) pi(x).
```

Thus, in the probabilistic/existential sense, the dense prime partition
question in EP675 has a positive answer.

### Proof

The density assertion follows from the strong law of large numbers applied to
the sequence of primes, together with the prime number theorem.

It remains to prove the translation property.

Fix `n`. Condition on the random choices for all primes `<= n`. Then `F_n`,
`Q cap [1,n]`, and

```text
M_n = product_{q in Q, q <= n} q
```

are fixed.

For each `a in F_n`, define

```text
L_a(s) = M_n s + a.
```

Let `R` be the finite set of primes `<= n`. We apply Lemma 4.1 outside `R`.
The tuple has no local obstruction outside `R`. Indeed, if `ell > n`, then
`ell` does not divide `M_n`, and the bad residue classes are

```text
s == -a M_n^{-1} mod ell,       a in F_n.
```

There are at most `|F_n| <= n < ell` such classes, so they do not cover all
residues modulo `ell`.

Therefore Lemma 4.1 gives infinitely many candidates `s` for which

```text
prod_{a in F_n} L_a(s)
```

has at most `C_n` prime factors outside `R`.

We need a little independence. Construct candidates recursively. After choosing
finitely many candidates, add all outside-`R` prime factors that have appeared
so far to the finite avoidance set in Lemma 4.1. The "moreover" part of the
lemma gives another candidate. Thus we obtain an infinite sequence

```text
s_1, s_2, ...
```

such that the sets of outside-`R` prime factors of

```text
prod_{a in F_n} L_a(s_j)
```

are pairwise disjoint, and each has size at most `C_n`.

For a candidate `s_j` to work, it is enough that every outside-`R` prime
factor of every `L_a(s_j)` lies in `P`. The conditional probability of this
event is at least

```text
alpha^(C_n).
```

For different `j`, these events are independent because the involved outside
prime sets are disjoint. Hence the probability that none of the candidates
works is at most

```text
prod_{j=1}^infinity (1 - alpha^(C_n)) = 0.
```

Thus, conditional on the choices of primes `<= n`, almost surely there exists
some `s` such that

```text
M_n s + a in S(P)       for every a in F_n.
```

By Lemma 3.1, `t_n = M_n s` is a translation witness on `[1,n]`.

There are only countably many `n`, and for each fixed `n` only finitely many
possible initial assignments of primes `<= n`. Taking a countable intersection
of probability-one events proves that almost surely a witness exists for every
`n`.

This completes the proof.

## 6. Why this is stronger than a heuristic

The random theorem does not require a prime `k`-tuple conjecture. The values

```text
M_n s + a
```

are not required to be prime. They only need all of their prime factors to lie
in the random set `P`.

Brun's sieve supplies infinitely many candidates for which the total number of
prime factors that must land in `P` is bounded by a constant depending only on
the prefix. Randomness then supplies the desired prime labels with fixed
positive probability, and the disjoint-prime construction gives independence.

This is the reason the random partition case looks substantially easier than
the adversarial dense partition case.

## 7. Deterministic regular partitions

The proof above suggests the right deterministic replacement for randomness.

### Definition 7.1: almost-prime capture property

Say that a prime set `P` has the almost-prime capture property if for every
finite admissible tuple of affine-linear forms

```text
L_1(s), ..., L_m(s)
```

and every finite set of locally allowed primes `R`, there exists an `s` such
that every prime factor outside `R` of

```text
L_1(s) ... L_m(s)
```

belongs to `P`.

### Proposition 7.2

If a prime partition `P sqcup Q` has the almost-prime capture property, then
`S(P)` has the translation property.

### Proof

Apply the property to the forms

```text
L_a(s) = M_n s + a,       a in S(P) cap [1,n],
```

with `R` equal to the primes `<= n`. The same argument as in Lemma 3.1 gives
a translation witness.

This proposition is mostly an interface, not a final theorem. However, the
random theorem proves that Bernoulli prime sets satisfy this kind of property
almost surely for the countable collection of tuples needed in EP675.

## 8. What this does and does not solve

### Solved under random regularity

If the EP675 prime-partition question is interpreted existentially:

> Does there exist a dense partition `P sqcup Q` for which `S(P)` has the
> translation property?

then Theorem 5.1 gives a strong positive answer, modulo citing Lemma 4.1
cleanly.

Indeed, a Bernoulli random partition almost surely has both sides of positive
prime density and almost surely gives the translation property.

### Not solved for adversarial dense partitions

If the intended question is universal:

> Does every dense partition `P sqcup Q` give `S(P)` the translation property?

then this lane does not solve it. Density alone does not force the
almost-prime capture property. An adversarial partition could try to capture
all prime factors of every almost-prime tuple value in `Q`, or arrange long
blocks/residue biases that defeat the recurrence condition.

The CRT audit still says there is no finite local obstruction, but the global
distribution problem remains.

## 9. Impact on full EP675 percentage

This is a meaningful gain.

Before this lane, the dense prime partition part was only reduced to a vague
finite-pattern recurrence problem. The random theorem gives a plausible full
solution of that subquestion in the strongest natural regular model, and it
likely gives an existential dense partition example.

Updated estimate:

```text
Prime partition subquestion, existential/random interpretation: 70-85%
Prime partition subquestion, universal adversarial interpretation: 20-30%
Full EP675 package: 30-40%
```

The remaining citation gate is the standard almost-prime tuple lemma. This is
not a new number-theory conjecture, but the exact statement should be cited
carefully before public posting.

The sums-of-two-squares existence question remains the main hard part of full
EP675.

## 10. Citation targets

For a public version, the only non-elementary citation needed in this lane is
Lemma 4.1. Search/citation targets:

- H. Halberstam and H.-E. Richert, *Sieve Methods*.
- G. Greaves, weighted/linear sieve treatments of almost-prime values.
- Diamond--Halberstam--Richert style higher-dimensional sieve statements.
- Papers on "almost-prime k-tuples" or "admissible tuples of linear forms"
  state explicit constants `C_m`, but this argument only needs existence of
  some finite `C_m`.

The exact numerical almost-prime bound is irrelevant; any bound depending only
on the number of forms is enough.
