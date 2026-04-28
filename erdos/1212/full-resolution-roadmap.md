# EP1212 Full Resolution Roadmap

Date: 2026-04-27

## Current Position

The problem has been reduced to a directed live-pair problem.

There are now two clean graph objects:

```text
D_exact:
  scale-free exact two-window DAG.

D_H^core:
  H-buffered right-core subgraph, where P^-(v) > H(v)+1.
```

An infinite ray in either object gives an EP1212 path. The local computational
evidence says `D_H^core` is the right finite-type object to attack, but the
slab-flow pass shows that local branching is not yet compatible across
multiple dyadic boundaries.

The remaining work is not another finite search. A full resolution needs a
theorem that proves infinite survival in `D_H^core`.

## The Finish-Line Theorem

A proof of the following would solve EP1212:

> There exists an increasing integer-valued function `H(x) -> infinity` and an
> infinite sequence of composite integers
>
> ```text
> a_0 < a_1 < a_2 < ...
> ```
>
> such that every pair `(a_i, a_{i+1})` is `H`-buffered right-core and
> `a_{i+2}` is a right-core regenerative successor of `(a_i, a_{i+1})`.

Expanded, this means:

```text
a_i, a_{i+1}, a_{i+2} composite,
a_{i+1} - a_i <= H(a_{i+1}),
clr(a_i; a_{i+1}) >= H(a_{i+1}),
P^-(a_{i+1}) > H(a_{i+1}) + 1,
a_{i+2} - a_{i+1} <= H(a_{i+1}),
gcd(a_{i+2}, product_{t=a_i}^{a_{i+1}} t) = 1,
clr(a_{i+1}; a_{i+2}) >= H(a_{i+2}),
P^-(a_{i+2}) > H(a_{i+2}) + 1.
```

This is stronger than EP1212, but it is now concrete and numerically supported.

## Finite-Slab Version

The compactness/Konig version should be stated first.

For dyadic slabs

```text
S_k = [2^k, 2^{k+1}),
```

define the right-core buffered graph restricted to source right coordinates in
`S_k`. A sufficient theorem is:

> For all large `k`, there is a nonempty set `C_k` of right-core buffered
> pairs with right coordinate in `S_k` such that every pair in `C_k` has at
> least one core-to-core directed path reaching `C_{k+1}`.

Since each finite slab graph has finite branching, nested finite choices then
give an infinite ray.

In practice one may prove a stronger crossing statement:

```text
Every large slab contains a forward-surviving right-core component crossing
to the next slab.
```

## Analytic Inputs Needed

### 1. Right-Core Density

Show that right-core buffered states are not too sparse. A target form:

```text
# {H-buffered right-core pairs (u,v), v in [X,2X)}
  >= X * H(X) / (log X)^C
```

for some fixed `C`, or any lower bound that leaves enough states for branching.

The hard part is simultaneous roughness and clearance:

```text
P^-(v) > H(v)+1,
v-u <= H(v),
clr(u;v) >= H(v).
```

### 2. Conditional Successor Estimate

For a typical right-core buffered pair `(u,v)`, prove that the number of
right-core regenerative successors is supercritical:

```text
E( core-to-core successors | right-core source ) > 1 + epsilon
```

on large slabs, with enough uniformity to survive dependencies.

Empirically this statistic is positive, but it is no longer sufficient:

```text
theta=0.36, N=1e6, top complete slab:
core-to-core mean about 2.98,
core-to-core zero about 0.118.
```

The slab-flow pass found that crossing images can miss the next slab's own
forward-surviving subset. A proof needs directed expansion/min-cut control, not
only a successor mean.

### 3. Concentration / Dependency Control

Mean greater than one is not enough. Need to rule out the possibility that
all edges concentrate in a few isolated bursts.

A usable theorem could be:

```text
Among right-core sources in [X,2X), all but o(1) of the mass lies in
components with forward reach at least X + cX, or at least the next dyadic slab.
```

Alternatively, prove a second-moment or expansion estimate:

```text
sum outdegree  >>  #sources
and
edge collisions / local dependencies are controlled.
```

This is where a Gafni-Tao-style rough-number moment method would be relevant.

### 4. Exceptional Slab Control

Almost-all interval estimates are not sufficient by themselves. A path can
fall into exceptional windows. Need either:

```text
no exceptional slab can block all right-core branches,
```

or

```text
exceptional slabs are sparse and can be crossed by stored buffer.
```

The current `H=x^theta` model is attractive because the buffer is large enough
to absorb some local irregularity.

### 5. Finite Seed

Once the asymptotic theorem starts at `X_0`, computation can supply a verified
finite ray from a small state into the first guaranteed slab. The certificate
verifier already handles finite right-core rays.

## Most Likely Proof Shape

The most plausible full proof is:

1. Work with `H(x)=floor(x^theta)` for a small fixed `theta`, probably in
   `0.34 <= theta <= 0.38`.
2. Prove a lower-bound and second-moment estimate for right-core buffered
   pairs in `[X,2X)`.
3. Prove that a positive fraction of right-core pairs have at least two
   right-core regenerative successors in the next local window.
4. Use a finite-slab branching/percolation argument to produce an infinite ray.
5. Apply the buffered live-pair reduction to obtain the EP1212 path.

The polylog route remains possible, especially `H=(log x)^2`, but the strict
right-core condition makes higher log powers invisible at current scales.

A cleaner conditional route is the strong `C`-core variant with `C>2`.
For `H=x^theta`, this makes future clearance automatic once the fixed
coordinate has `P^- > C H`, and for `1/3 < theta < 1/2` the composite
coordinates are eventually rough semiprimes. This reduces the missing theorem
to rough-semiprime slab expansion in short intervals with one anchored
exclusion window.

The reciprocal-candidate pass sharpens this further. In the semiprime regime,
each prime factor `r > H` determines at most one successor in `(v,v+H]`,
namely the first multiple of `r` after `v`. The successor is core precisely
when the reciprocal cofactor `ceil(v/r)` is prime and exceeds the core
threshold. Thus the missing analytic input is not a dense short-interval
almost-prime theorem; it is a directed expansion theorem for sparse reciprocal
semiprime candidates.

The threshold-transition pass adds a combinatorial simplification: after
fixing the middle coordinate `v`, every child `w` is available to a suffix of
the parent set `U(v)`. Thus the compatible-survival problem is controlled by
one scalar threshold per `v`, not by a general Hall-type matching problem.
For `H=x^theta`, `1/3<theta<1/2`, a parent interval `[u,v]` kills at most

```text
sum_{t=u}^v omega_{>H(v)}(t) <= 2(v-u+1)
```

candidate children. A sufficient analytic theorem is therefore: produce more
than this many future-good rough-semiprime children at each surviving state.

## What Would Count As Full Resolution

Any one of these is enough:

```text
1. Prove an infinite ray in D_exact.
2. Prove an infinite ray in D_H^core for some H -> infinity.
3. Prove a finite-slab survival theorem for D_H^core plus a finite seed.
4. Prove the threshold continuation criterion uniformly, i.e. future-good
   children beat the parent-interval killing count.
5. Give an explicit infinite construction a_i satisfying the exact DAG edge
   conditions.
```

The third route is currently the most promising.

## What Is Still Missing

The missing item is a named analytic theorem:

> Right-core live-pair branching theorem.

Local computational evidence supports it, but slab-flow compatibility remains
unproved. We do not yet have:

```text
- a rigorous asymptotic count of right-core buffered states,
- a rigorous asymptotic count of core-to-core successors,
- a second-moment/concentration estimate,
- a slab-crossing survival argument.
```

Until those are proved, the project is at "strong reduction plus strong
finite evidence", not a solution.

## Updated Percentage

```text
exact graph reduction:             95%
buffered/right-core target:        85%
local computational evidence:      90%
compatible slab-flow evidence:     45%
analytic theorem in hand:          20%
full EP1212 solution:              45-50%
```

The percentage should not rise back past 55% until compatible slab-flow
survival is demonstrated computationally at increasing scales or proved by an
analytic directed expansion theorem.
