# EP1212 Closure Attempt (GPT-5.2, attempt 1)

Date: 2026-04-28

Verdict: **NOT CLOSED**.

Reason: the local notes correctly reduce EP1212 to existence of an infinite ray
in a right-core buffered live-pair digraph. What remains is an analytic
"slab-survival" theorem about rough semiprimes in power-short intervals with
two-window avoidance constraints. I do not see a way to deduce that theorem
from standard unconditional results without inserting an unproved short-interval
rough-semiprime statement (which this attempt avoids).

This document restates the reductions and then pushes a "deep-core semiprime"
route to the precise point where it breaks.

---

## 0. EP1212 Statement

Let `G` be the graph with vertex set

```
V := { (x,y) in N^2 : gcd(x,y)=1 }.
```

Edges join `(x,y)` to `(x+1,y)`, `(x-1,y)`, `(x,y+1)`, and `(x,y-1)` when the
target is still in `V`.

Question (EP1212): does there exist an infinite path `P` in `G` such that for
every `(x,y)` on `P`,

1. `min(x,y) > 1`, and
2. at least one of `x,y` is composite?

---

## 1. Exact Two-Window DAG Reduction (Sound)

This section is a condensed re-derivation of `exact-live-pair-dag.md`.

### 1.1 Clearance

For integers `u < v`, define

```
clr(u; v) := max { L >= 0 : gcd(u, prod_{t=v}^{v+L} t) = 1 }.
```

Thus `clr(u;v) >= L` iff no prime dividing `u` divides any integer in
`[v, v+L]`.

### 1.2 Exact Live-Pair DAG

Define the directed acyclic graph `D_exact` whose vertices are ordered pairs
`(u,v)` with `u<v` and `u,v` composite.

Put a directed edge

```
(u,v) -> (v,w)
```

iff

1. `u < v < w` and `u,v,w` are composite,
2. `w - v <= clr(u; v)`, and
3. `gcd(w, prod_{t=u}^{v} t) = 1`.

### 1.3 Infinite Rays Give EP1212 Paths

If

```
(a0,a1) -> (a1,a2) -> (a2,a3) -> ...
```

is an infinite ray in `D_exact`, then concatenating the rectangle paths

```
(ai, ai+1) -> (ai, ai+1+1) -> ... -> (ai, ai+2)
          -> (ai+1, ai+2)  (then horizontal step-by-step)
```

produces an infinite path in `G` with `min(x,y)>1` and at least one composite
coordinate at each step:

* Along the vertical segment the first coordinate is the fixed composite `ai`
   and condition (2) ensures `gcd(ai, y)=1` for all visited `y`.
* Along the horizontal segment the second coordinate is the fixed composite
  `ai+2` and condition (3) ensures `gcd(x, ai+2)=1` for all visited `x`.

Therefore:

> Proposition A: An infinite ray in `D_exact` implies a "yes" answer to EP1212.

---

## 2. Buffered Right-Core Reduction (Sound)

This section condenses `buffered-live-pair-bridge.md`.

Fix an increasing integer-valued `H(x) >= 1` with `H(x) -> infinity`.

Call a composite pair `(u,v)` with `u<v` **H-buffered** if

1. `v-u <= H(v)`, and
2. `clr(u; v) >= H(v)`.

Given an H-buffered pair `(u,v)`, define

```
Raw(u,v) := { w : v < w <= v+H(v), w composite, gcd(w, prod_{t=u}^{v} t)=1 }.
Reg(u,v) := { w in Raw(u,v) : clr(v; w) >= H(w) }.
```

Define the right-core condition

```
P^-(v) > H(v) + 1
```

where `P^-(v)` is the least prime divisor of `v`. This is necessary for
regeneration to be possible (otherwise some prime dividing `v` forces a multiple
in any block of length `H(w)+1`).

Exactly the same rectangle concatenation as in Section 1.3 shows:

> Proposition B: If for some increasing `H` there is an infinite ray in the
> regenerative digraph on H-buffered pairs (optionally restricted to right-core),
> then EP1212 holds.

So EP1212 is reduced to:

> Finish-Line Theorem: there exists `H(x)->infty` such that the H-buffered
> right-core regenerative digraph contains an infinite directed ray.

---

## 3. Deep-Core Route and the Exact Point It Fails

The current roadmap suggests a power buffer

```
H(x) := floor(x^theta),  with  1/3 < theta < 1/2,
```

and a stronger roughness cutoff

```
Y(x) := A H(x)  with A>3,
```

seeking a ray whose right coordinates are "deep-core":

```
P^-(n) > Y(n).
```

### 3.1 Lemma: Deep-Core Composites Near X Are Semiprimes

Let `X` be large and `n in [X,2X]` with `P^-(n) > Y(X)`.

If `n` had at least 3 prime factors, then

```
n >= (Y(X))^3  >>  X^(3 theta),
```

and since `theta>1/3`, we have `X^(3 theta) > X` for large `X`, contradicting
`n <= 2X`. Hence any such `n` must have exactly 2 prime factors (possibly equal).

So, in the intended regime, right-core vertices are essentially **rough
semiprimes**.

### 3.2 Why Deep-Core Looks Promising (Heuristic Only)

If `u` and candidate successors `w` have prime factors `>> H(v)`, then the
clearance and two-window avoidance constraints each reduce to avoiding (at most)
one multiple of each prime in a short interval of length `H`. This is the
intuition behind the observed supercritical "core-to-core mean outdegree" in the
finite experiments.

However, this is not a proof: it requires a quantitative short-interval theorem
that simultaneously handles:

* existence/density of rough semiprimes in intervals of length `X^theta`,
* residue-class avoidance against the whole block `[u,v]`, and
* the next-step clearance constraint depending on prime factors of `v`.

### 3.3 The Precise Missing Theorem

A statement strong enough to complete the Finish-Line Theorem (in the current
framework) would look like:

Missing Theorem (Right-Core Live-Pair Branching / Slab Survival):
Fix `1/3<theta<1/2` and set `H(x)=floor(x^theta)`. There exist `A>1`, `eps>0`
such that for all sufficiently large dyadic slabs `[X,2X)`, there is a nontrivial
collection of H-buffered right-core pairs `(u,v)` with `v in [X,2X)` whose
core-to-core regenerative successor process is uniformly supercritical and
non-concentrated across the slab, in a way that forces directed paths to survive
from slab to slab (hence an infinite ray by Koenig compactness).

Concretely, one needs a *rigorous* lower bound for core-to-core successors for a
positive fraction of right-core sources, plus a dependency/concentration control
strong enough to upgrade that to slab-crossing survival.

I do not know how to derive such a theorem unconditionally from standard results
without inserting an unproved short-interval distribution statement for rough
semiprimes (and their correlations with the two-window avoidance condition).

That is the exact point where this closure attempt stops.

---

## 4. What Is Rigorously Achieved Here

1. The reductions recorded in `exact-live-pair-dag.md` and
   `buffered-live-pair-bridge.md` are logically correct: an infinite ray in the
   exact DAG or in the buffered regenerative right-core digraph implies EP1212.
2. For `H(x)=x^theta` with `theta>1/3`, the right-core condition forces the
   relevant composites to be semiprimes, explaining why the analytic bottleneck
   is "rough semiprimes in short intervals" plus correlation control.

Nothing beyond (1)-(2) is proved here; in particular the Finish-Line Theorem
remains open in this attempt.
