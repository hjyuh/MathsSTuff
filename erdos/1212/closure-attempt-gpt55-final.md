# EP1212 Closure Attempt (GPT-5.5 final)

Date: 2026-04-28

Verdict: **NOT CLOSED**.

I do not have a valid proof of EP1212. The exact live-pair DAG reduction and the
buffered right-core reduction are sound, but the remaining step is still a
uniform slab-survival theorem for compatible rough composites. In the power
buffer range that has the best numerical evidence, this is specifically a
rough-semiprime slab-survival theorem with moving two-window avoidance
constraints.

This pass tried to bypass that theorem through local/periodic corridors and
through bounded-gap rough composite constructions. Those attempts did not yield
a proof. The useful output is a sharper set of exact-ray roughness lemmas and a
more precise finish-line theorem: a compatible right-core slab min-cut theorem,
not a local mean-outdegree estimate.

---

## 1. Reductions retained from the local artifacts

I use the notation from:

- `exact-live-pair-dag.md`
- `buffered-live-pair-bridge.md`
- `right-core-survival-pass.md`
- `full-resolution-roadmap.md`
- `closure-attempt-gpt52.md`
- `closure-attempt-gpt54.md`
- `scripts/buffered_live_pair_stats.py`

The following are accepted as sound.

### Exact DAG reduction

Let `D_exact` have composite vertices `(u,v)` with `u<v`, and an edge

```text
(u,v) -> (v,w)
```

iff `u,v,w` are composite, `u<v<w`,

```text
w-v <= clr(u;v),
gcd(w, product_{t=u}^{v} t) = 1.
```

An infinite directed ray in `D_exact` gives an EP1212 path by concatenating the
two-window rectangle paths. Conversely, any monotone all-composite two-window
zig-zag gives such a ray.

### Buffered right-core reduction

For an increasing buffer `H`, an infinite ray in the regenerative
`H`-buffered graph, in particular in the right-core subgraph

```text
P^-(v) > H(v)+1,
```

also gives an EP1212 path. This is a sufficient route, not an equivalence with
all possible EP1212 paths.

---

## 2. Lemmas proved in this pass

### Lemma 2.1: exact rays force local roughness

Let

```text
(a_0,a_1) -> (a_1,a_2) -> (a_2,a_3) -> ...
```

be an infinite ray in `D_exact`, and put

```text
h_i = a_{i+1}-a_i.
```

Then for every `i>=2`,

```text
P^-(a_i) > max(h_{i-2}+1, h_{i+1}+1).
```

#### Proof

Let `p` be any prime divisor of `a_i`.

From the incoming edge

```text
(a_{i-2},a_{i-1}) -> (a_{i-1},a_i),
```

we have

```text
gcd(a_i, product_{t=a_{i-2}}^{a_{i-1}} t) = 1.
```

Thus `[a_{i-2},a_{i-1}]` contains no multiple of `p`. This interval has
`h_{i-2}+1` consecutive integers. If `p <= h_{i-2}+1`, every such interval
contains a multiple of `p`, contradiction. Hence `p>h_{i-2}+1`.

From the outgoing edge

```text
(a_i,a_{i+1}) -> (a_{i+1},a_{i+2}),
```

we also have

```text
gcd(a_i, product_{t=a_{i+1}}^{a_{i+2}} t) = 1.
```

The interval `[a_{i+1},a_{i+2}]` has `h_{i+1}+1` consecutive integers, so the
same argument gives `p>h_{i+1}+1`. Taking the least prime divisor of `a_i`
proves the claim. `QED`

This is only a necessary condition. It explains why any exact-ray proof must
control rough composites at the scale of the adjacent gaps.

### Lemma 2.2: a sufficient automatic-visibility roughness criterion

Let `a_0<a_1<a_2<...` be composite integers and set `h_i=a_{i+1}-a_i`.
Assume that for every relevant `j`,

```text
P^-(a_j) > max(h_{j-2}+h_{j-1}, h_j+h_{j+1}),
```

with missing initial indices ignored. Then

```text
(a_i,a_{i+1}) -> (a_{i+1},a_{i+2})
```

is an edge of `D_exact` for every `i` for which the displayed inequalities are
available. Hence the tail of the sequence gives an EP1212 path.

#### Proof

Fix `i`. For the vertical part, let `p|a_i` and let
`t in [a_{i+1},a_{i+2}]`. Then

```text
0 < t-a_i <= h_i+h_{i+1} < p.
```

So `p` cannot divide both `a_i` and `t`. This proves

```text
clr(a_i;a_{i+1}) >= h_{i+1}.
```

For the horizontal part, let `p|a_{i+2}` and
`s in [a_i,a_{i+1}]`. Then

```text
0 < a_{i+2}-s <= h_i+h_{i+1} < p,
```

so `p` cannot divide both `a_{i+2}` and `s`. Thus

```text
gcd(a_{i+2}, product_{s=a_i}^{a_{i+1}} s) = 1.
```

The exact DAG edge condition follows. `QED`

This lemma gives a clean possible bypass: find an infinite bounded-gap or
slow-gap sequence of composites whose least prime factors dominate the local
two-step spans. The next lemma shows why the most naive bounded-gap version
cannot work.

### Lemma 2.3: the constant-gap automatic route is blocked

Fix `B>=1`. There is no infinite increasing sequence `a_i` such that

```text
a_{i+1}-a_i <= B
```

for all `i` and

```text
P^-(a_i) > 2B
```

for all `i`.

#### Proof

Let

```text
Q = product_{p prime, p <= 2B} p.
```

If `P^-(n)>2B`, then `gcd(n,Q)=1`.

For every integer `m`, every number in the interval

```text
[mQ+2, mQ+2B]
```

has a prime divisor at most `2B`: if `n=mQ+r` with `2<=r<=2B`, then any prime
divisor of `r` divides both `Q` and `n`. Hence no number in that interval is
coprime to `Q`.

The last possible `Q`-coprime residue before this blocked interval is at most
`mQ+1`, and the first possible one after it is at least `mQ+2B+1`. Crossing the
blocked interval therefore requires a jump of at least `2B`, which is larger
than `B`. An unbounded increasing sequence with gaps at most `B` must cross
such blocked intervals for arbitrarily large `m`, contradiction. `QED`

This does not rule out all bounded-gap exact rays, because exact visibility can
use residue alignment with prime factors between `B` and `2B`. It does rule out
the simple sufficient construction from Lemma 2.2 with a fixed gap bound.

### Lemma 2.4: power-buffer right-core states are semiprimes

Fix

```text
H(x)=floor(x^theta),    1/3 < theta < 1/2.
```

For all sufficiently large `X`, if `n in [X,2X]` is composite and

```text
P^-(n) > H(X),
```

then `n=pq` with primes `p,q>H(X)`, allowing `p=q`.

#### Proof

If `n` had at least three prime factors counted with multiplicity, then

```text
n >= H(X)^3.
```

Since `3theta>1`, we have `H(X)^3>2X` for all sufficiently large `X`, contrary
to `n<=2X`. Since `n` is composite, it has exactly two prime factors. `QED`

This is the key correction from `closure-attempt-gpt54.md`: no extra
deep-core cutoff is needed in the power-buffer range. The right-core graph is
already a rough-semiprime graph.

### Lemma 2.5: CRT divisibility becomes exact-value forcing

In the setting of Lemma 2.4, if `p,q>H(X)` are primes and `pq|n`, then for all
sufficiently large `X`,

```text
n=pq.
```

#### Proof

Write `n=pqr`. If `r>1`, then every prime factor of `r` is also greater than
`H(X)`, so `r>H(X)`. Then

```text
n >= H(X)^3 > 2X,
```

contradiction. Hence `r=1`. `QED`

Thus a CRT/block construction that tries to force a right-core successor by
forcing divisibility by two large primes has not created a flexible composite
condition; it has specified the exact semiprime value. This is why the
semiprime-location theorem cannot be bypassed by the usual block method inside
the current right-core power-buffer framework.

---

## 3. Why the local computational statistics are not a proof

The script `scripts/buffered_live_pair_stats.py` correctly measures finite
statistics such as:

```text
right_core_pairs
core_to_core_mean
core_to_core_zero
longest_core_ray_certificate
```

The positive right-core data in `right-core-survival-pass.md` are meaningful
evidence. They do not prove survival, for two reasons.

First, a finite longest ray inside a cap is not compatible data across caps.
A new longer ray at a larger cap can start from a different finite component.

Second, mean outdegree greater than one is not enough. A layered directed graph
can have large average outdegree on every finite layer while all edges from the
reachable frontier concentrate into a small dead set. The missing theorem must
therefore be a compatible slab-survival or min-cut theorem, not merely a local
successor-count theorem.

---

## 4. Exact theorem that would close EP1212

Here is the clean deterministic finish line.

Fix an increasing integer-valued buffer `H`. Let `D_H^core` be the directed
right-core `H`-buffered regenerative graph from `buffered-live-pair-bridge.md`.
For `k>=1`, let

```text
S_k = { (u,v) in D_H^core : 2^k <= v < 2^{k+1} }.
```

### Compatible slab-survival theorem

There exist `H`, an integer `k_0`, and nonempty finite sets

```text
C_k subset S_k,    k>=k_0,
```

such that for every `k>=k_0` and every state `s in C_k`, there is a finite
directed path in `D_H^core` from `s` to at least one state in `C_{k+1}`.

### Why this closes EP1212

Choose any `s_0 in C_{k_0}`. By the theorem, choose a directed path from
`s_0` to some `s_1 in C_{k_0+1}`. Repeat from `s_1`, and so on. Concatenating
these finite directed paths gives an infinite directed ray in `D_H^core`.
The buffered live-pair bridge then embeds that ray as an infinite EP1212 path.

No finite seed from small coordinates is needed, because EP1212 asks only for
existence of an infinite path.

### Analytic version that should be proved

The theorem above is deterministic. The analytic theorem needed to produce the
sets `C_k` should be a robust min-cut statement in the power-buffer right-core
graph.

A concrete sufficient target is:

> For some `theta in (1/3,1/2)` and `H(x)=floor(x^theta)`, every sufficiently
> large dyadic slab contains a nonempty family `C_k` of right-core buffered
> rough-semiprime states such that every vertex cut separating any `s in C_k`
> from `S_{k+1}` inside the directed core graph has positive size, and the set
> of reachable endpoints in `S_{k+1}` contains the next family `C_{k+1}`.

Equivalently, one needs to prove compatible slab-to-slab survival for the
rough-semiprime successor process, with enough expansion or second-moment
control that the mass cannot collapse into finitely many dead branches.

---

## 5. Minimal remaining analytic obstacle

For `H(x)=floor(x^theta)`, `1/3<theta<1/2`, write a right-core source at scale
`X` as

```text
u=p_1p_2,    v=r_1r_2,
```

with all prime factors `>H(X)`. A core-to-core successor must be a semiprime

```text
w=ab,    v < w <= v+H(v),
```

with `a,b>H(w)` and with the two moving avoidance constraints:

```text
[u,v] contains no multiple of a or b,
[w,w+H(w)] contains no multiple of r_1 or r_2.
```

Thus the missing estimate is not a bare count of semiprimes in
`(v,v+H(v)]`. It is a lower-tail and dependency theorem for the weighted counts

```text
N(u,v) =
  # { w=ab in (v,v+H(v)] :
        a,b>H(w),
        [u,v] avoids multiples of a,b,
        [w,w+H(w)] avoids multiples of r_1,r_2 }.
```

The theorem must hold uniformly enough over every large dyadic slab to imply
slab min-cuts or expansion for reachable frontiers. In practical terms, the
missing package is:

```text
1. lower bounds for total rough-semiprime successor edges from large compatible
   families of right-core states;
2. second-moment or collision bounds for shared successors and overlapping
   avoidance windows;
3. lower-tail control ruling out a whole slab where every compatible frontier
   dies;
4. compatibility of the surviving endpoint distribution with the next slab.
```

This is strictly stronger than:

```text
E(core-to-core outdegree | right-core source) > 1,
```

and stronger than an almost-all short-interval semiprime theorem. It is exactly
the moving-constraint rough-semiprime slab-survival/min-cut problem identified
by the previous attempts and sharpened here.

---

## 6. Final assessment

The current proof stack is:

```text
exact DAG reduction:                         proved locally
buffered/right-core bridge:                  proved locally
power-buffer semiprime rigidity:             proved
CRT exact-value obstruction:                 proved
constant-gap automatic roughness obstruction: proved in this pass
compatible slab-survival theorem:            not proved
EP1212:                                      not closed
```

The strongest current route remains:

1. Work with `H(x)=floor(x^theta)` for some `theta in (1/3,1/2)`.
2. Prove the compatible right-core rough-semiprime slab-survival/min-cut theorem.
3. Use the buffered bridge to obtain an infinite EP1212 path.

Until item 2 is proved, the present pass does not close EP1212.

## Verdict

**NOT CLOSED.**
