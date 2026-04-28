# Threshold Transitions and Finite Exact-DAG Paths

Date: 2026-04-28

## Purpose

This note records the 5.4 refinement of the EP1212 live-pair program.

The main point is that, after fixing the middle coordinate `v`, the parent to
child incidence is not a general bipartite expansion problem. It is a nested
suffix, or threshold, relation. This sharpens the compatible-survival problem.

The note also records a rigorous finite result: the exact live-pair DAG has
directed paths of arbitrarily large finite length.

## Setup

Fix an increasing integer-valued buffer `H`. For a right-core middle coordinate
`v`, define

```text
U(v) = {
  u in [v-H(v), v) :
  u composite and clr(u;v) >= H(v)
}.
```

Define the child set

```text
W(v) = {
  w in (v, v+H(v)] :
  w composite,
  clr(v;w) >= H(w),
  P^-(w) > H(w)+1
}.
```

For `w in W(v)`, define the backward bad threshold

```text
beta_v(w)
  = max({t in [v-H(v), v] : gcd(t,w)>1} union {v-H(v)-1}).
```

## Lemma 1: Fixed-v Threshold Relation

For `u in U(v)` and `w in W(v)`,

```text
(u,v) -> (v,w)    iff    u > beta_v(w).
```

Proof. Since `u in U(v)` and `w <= v+H(v)`, the forward lane condition

```text
w-v <= clr(u;v)
```

is automatic. The target conditions are already included in `W(v)`.
Therefore the only remaining edge condition is

```text
gcd(w, product_{t=u}^v t) = 1.
```

The interval `[u,v]` is a suffix of `[v-H(v),v]`. Thus this gcd condition is
equivalent to saying that no bad point

```text
t in [v-H(v),v] with gcd(t,w)>1
```

lies in that suffix. This happens exactly when `u > beta_v(w)`.

Consequently, for fixed `v`, each child is available to a suffix of the
ordered parent set `U(v)`.

## Corollary 2: Future-Good Parents Are a Suffix

Let `G(v) subset W(v)` be any family of children. Then the set of parents
having at least one child in `G(v)` is

```text
{u in U(v) : u > min_{w in G(v)} beta_v(w)}.
```

In particular, if `W_infty(v)` denotes the children from which continuation is
possible, then the parent states over `v` that survive indefinitely form one
suffix of `U(v)`.

This replaces a Hall/min-cut view by a one-dimensional threshold view at each
middle coordinate.

## Lemma 3: Parent Interval Killing Bound

Assume

```text
H(x)=floor(x^theta),    1/3 < theta < 1/2.
```

Let `(u,v)` be `H`-buffered and right-core, and set

```text
I = [u,v],    g = |I| = v-u+1.
```

Then the number of children `w in W(v)` killed by the backward coprimality
condition

```text
gcd(w, product_{t=u}^v t) > 1
```

is at most

```text
sum_{t=u}^v omega_{>H(v)}(t) <= 2g
```

for all sufficiently large `v`, where `omega_{>H(v)}(t)` counts distinct prime
factors of `t` exceeding `H(v)`.

Proof. Distinct children in `W(v)` are pairwise coprime. Indeed, if a prime
`p` divided two distinct children `w_1,w_2`, then `p` would divide
`|w_1-w_2|`. But every prime factor of each child exceeds `H(v)`, while

```text
0 < |w_1-w_2| < H(v).
```

Now fix `t in I`. A child killed by `t` must share with `t` a prime
`p > H(v)`. For each such prime `p|t`, at most one child in `(v,v+H(v)]` is
divisible by `p`, because the window length is smaller than `p`. Hence `t`
kills at most `omega_{>H(v)}(t)` children.

Summing over `t in [u,v]` gives the first bound. For `theta>1/3`, no integer
`t asymp v` can have three distinct prime factors larger than `H(v)`, because
that would force `t > H(v)^3 > v` eventually. Hence each summand is at most
`2`.

## Corollary 4: Concrete Continuation Criterion

Let `G(v) subset W(v)` be a designated future-good child set. If

```text
|G(v)| > sum_{t=u}^v omega_{>H(v)}(t),
```

then `(u,v)` has a child in `G(v)`.

In particular, in the power-buffer semiprime range, the sufficient condition

```text
|G(v)| > 2(v-u+1)
```

guarantees continuation.

This is the quantity a proof must beat. Mean outdegree alone is not the right
survival statistic.

## Lemma 5: Rough Composite Blocks Give Exact-DAG Paths

Let

```text
a_0 < a_1 < ... < a_m
```

be composite integers such that

```text
P^-(a_i) > a_m-a_0      for all 0 <= i <= m.
```

Then for every `0 <= i <= m-2`,

```text
(a_i,a_{i+1}) -> (a_{i+1},a_{i+2})
```

is an edge in the exact live-pair DAG.

Proof. Fix `i`. If `p|a_i`, then

```text
p > a_m-a_0 >= a_{i+2}-a_i,
```

so no multiple of `p` lies in `[a_{i+1},a_{i+2}]`. Hence

```text
a_{i+2}-a_{i+1} <= clr(a_i;a_{i+1}).
```

Similarly, if `q|a_{i+2}`, then `q > a_{i+2}-a_i`, so no integer in
`[a_i,a_{i+1}]` is divisible by `q`. Therefore

```text
gcd(a_{i+2}, product_{t=a_i}^{a_{i+1}} t)=1.
```

These are exactly the edge conditions in the exact DAG.

## Theorem 6: Arbitrarily Long Finite Exact-DAG Paths

For every `ell >= 1`, the exact live-pair DAG contains a directed path of
length `ell`.

External input: use the Goldston--Graham--Pintz--Yildirim theorem on small gaps
between products of two primes, in the form that admissible tuples of linear
forms can be forced to contain arbitrarily many `E_2` values, with all prime
factors exceeding any fixed constant.

Proof. Choose `k` large enough for the external theorem with `ell+2` desired
`E_2` values. Set

```text
M = product_{p <= k} p,
L_j(n) = n + jM,        0 <= j < k.
```

This tuple is admissible: for primes `p <= k`, all shifts are congruent to
`0 mod p`, and for primes `p > k`, the `k` shifts cannot occupy all residue
classes.

Choose

```text
D > (k-1)M.
```

The external theorem gives infinitely many `n` for which at least `ell+2`
of the values `L_j(n)` are `E_2` numbers with every prime factor exceeding
`D`. Choose these values in increasing order:

```text
a_0 < a_1 < ... < a_{ell+1}.
```

Then

```text
a_{ell+1}-a_0 <= (k-1)M < D < P^-(a_r)
```

for every `r`. Lemma 5 gives

```text
(a_0,a_1) -> (a_1,a_2) -> ... -> (a_ell,a_{ell+1}).
```

Thus arbitrary finite exact-DAG paths exist.

## Consequence

The obstruction is not local finite pattern creation. The missing step is an
infinite survival theorem.

The threshold formulation suggests a sharper missing theorem:

> For infinitely many dyadic slabs, there are right-core middle coordinates
> `v` for which the future-good threshold
>
> ```text
> tau(v) = 1 + min_{w in W_infty(v)} beta_v(w)
> ```
>
> is finite and lies below at least one available parent in `U(v)`.

Equivalently, in a constructive version, one must produce enough future-good
children of `v` to beat the parent-interval killing count

```text
sum_{t=u}^v omega_{>H(v)}(t).
```

For `H=x^theta`, `1/3<theta<1/2`, the sufficient target is

```text
future-good children > 2(v-u+1).
```

## Relation to Current Technology

EP1212 remains open on the Erdos Problems page as of the 2026-04-28 check.

Known short-interval results do not close this threshold theorem:

```text
Benatar's pointwise short-interval Hildebrand--Tenenbaum theorem reaches
y >= x^(17/30+epsilon), which is above the viable H<x^(1/2) range.

Matomaki's almost-prime theorem works in almost all very short intervals, not
pointwise/adversarial intervals.

Jarviniemi's large-prime-gap estimates are exceptional-set estimates for
prime gaps, not de-sieved rough-semiprime survival.

Campbell's all-interval almost-prime result between consecutive squares is at
the square-root scale and does not include the roughness/adaptive coprimality
needed here.
```

So the current route requires a pointwise adaptive de-sieved rough-semiprime
theorem, or an alternative state space that avoids the fixed-buffer roughness
regime.

## Sources Checked

```text
Erdos Problems #1212:
https://www.erdosproblems.com/1212

Goldston--Graham--Pintz--Yildirim, Small gaps between products of two primes:
https://arxiv.org/abs/math/0609615

Benatar, A short-interval Hildebrand--Tenenbaum theorem:
https://arxiv.org/abs/2408.16576

Matomaki, Almost primes in almost all very short intervals:
https://arxiv.org/abs/2012.11565

Jarviniemi, On large differences between consecutive primes:
https://arxiv.org/abs/2212.10965

Campbell, Integers with at most 3 prime factors between consecutive squares:
https://arxiv.org/abs/2603.10356
```
