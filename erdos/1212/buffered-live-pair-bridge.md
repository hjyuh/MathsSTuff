# Buffered Live-Pair Bridge for EP1212

Date: 2026-04-27

## Purpose

This note records the current best reduction target for EP1212:

> It is enough to prove an infinite ray in a directed graph of buffered
> composite live pairs.

This is not a proof of EP1212. It isolates the remaining analytic problem as
a branching/survival theorem for sifted short intervals.

## Definitions

For composite integers `u < v`, define the forward clearance

```text
clr(u; v) = max { L >= 0 : gcd(u, product_{t=v}^{v+L} t) = 1 }.
```

Equivalently, if `P(u)` is the set of prime divisors of `u`, then

```text
clr(u; v) = min_{p in P(u)} (ceil(v / p) p) - v - 1,
```

with negative value when `gcd(u, v) > 1`.

Fix any increasing integer-valued buffer function `H(x) >= 1`. The first
experiments use

```text
H(x) = floor(x^theta),    0 < theta < 1/2.
```

but the reduction itself does not require this specific form.

A pair `(u, v)` is `H`-buffered if

```text
u, v are composite,
u < v,
v - u <= H(v),
clr(u; v) >= H(v).
```

Given an `H`-buffered pair `(u, v)`, define the raw successor set

```text
Raw(u, v) = {
  w : v < w <= v + H(v),
      w composite,
      gcd(w, product_{t=u}^{v} t) = 1
}.
```

Define the regenerative successor set

```text
Reg(u, v) = {
  w in Raw(u, v) : clr(v; w) >= H(w)
}.
```

Then `w in Reg(u, v)` implies `(v, w)` is again `H`-buffered. This is the
computationally useful split. In the stricter formulation where the successor
set already includes `clr(v; w) >= H(w)`, the two counts `A` and `A+` are
identical.

A buffered pair is `right-core` if

```text
P^-(v) > H(v) + 1,
```

where `P^-(v)` is the least prime divisor of `v`. This is a hard necessary
condition for full `H`-regeneration from `(u, v)`: if `p | v` and
`p <= H(w)+1`, then every block of `H(w)+1` consecutive integers contains a
multiple of `p`, so `clr(v; w) >= H(w)` is impossible.

## Reduction Proposition

Assume that for some increasing buffer `H` there is an infinite sequence of
composite integers

```text
a_0 < a_1 < a_2 < ...
```

such that every pair `(a_i, a_{i+1})` is `H`-buffered and

```text
a_{i+2} in Reg(a_i, a_{i+1})
```

for every `i >= 0`. Then EP1212 has a valid infinite path.

## Proof

For each transition

```text
(a_i, a_{i+1}) -> (a_{i+1}, a_{i+2}),
```

insert the lattice path

```text
(a_i, a_{i+1})
  -> (a_i, a_{i+1}+1)
  -> ...
  -> (a_i, a_{i+2})
  -> (a_i+1, a_{i+2})
  -> ...
  -> (a_{i+1}, a_{i+2}).
```

The vertical segment is valid because `(a_i, a_{i+1})` is buffered:

```text
a_{i+2} - a_{i+1} <= H(a_{i+1})
```

and

```text
clr(a_i; a_{i+1}) >= H(a_{i+1}),
```

so `gcd(a_i, t) = 1` for every `t` from `a_{i+1}` through `a_{i+2}`.

The horizontal segment is valid because `a_{i+2} in Raw(a_i, a_{i+1})`, hence

```text
gcd(a_{i+2}, product_{t=a_i}^{a_{i+1}} t) = 1.
```

Thus every vertex on the horizontal segment is also visible.

Every vertex has both coordinates greater than `1`. On the vertical segment,
the fixed coordinate `a_i` is composite. On the horizontal segment, the fixed
coordinate `a_{i+2}` is composite. Therefore every vertex also satisfies the
EP1212 composite-coordinate condition.

Concatenating these finite paths over all `i` gives an infinite path in the
EP1212 graph.

The same proof applies if the ray is required to stay inside the right-core
subgraph, i.e. every state `(a_i, a_{i+1})` has `P^-(a_{i+1}) > H(a_{i+1})+1`.
The right-core condition is not needed for the embedding; it is the natural
same-type branching condition for full-buffer regeneration.

## Strong C-Core Variant

There is a stricter core that removes one nuisance from the transition count.
Fix `C > 2`, and call `(u, v)` a strong `C`-core state if it is `H`-buffered
and

```text
P^-(u), P^-(v) > C H(v).
```

For `H(x)=floor(x^theta)` with `theta < 1`, if `v < w <= v + H(v)` and `v` is
strong `C`-core, then

```text
clr(v; w) >= H(w)
```

for all sufficiently large `v`. Indeed, if `p | v`, then the first multiple of
`p` after `v` is at least `v + C H(v)`, while

```text
w + H(w) <= v + H(v) + H(v + H(v)) < v + C H(v)
```

eventually because `C > 2` and `H(v + H(v)) / H(v) -> 1`.

Thus, inside the strong core, the regenerative condition is eventually
automatic. The successor problem reduces to finding composite rough successors
`w` in the short interval `(v, v + H(v)]` satisfying the anchored exclusion
condition

```text
gcd(w, product_{t=u}^{v} t) = 1.
```

For `1/3 < theta < 1/2`, strong-core composite coordinates near `X` are
rough semiprimes: three prime factors would force `n > X^{3theta}`, which
exceeds `X` for large `X`.

## Remaining Theorem

It remains to prove a buffered branching theorem. A useful finite-scale form is:

> For some `theta < 1/2`, the directed graph of `H`-buffered pairs and
> regenerative transitions contains forward-surviving components across
> arbitrarily large dyadic slabs.

Computational evidence should therefore track survival, not only local
existence. The relevant finite statistics are:

```text
P(Raw(u, v) = empty),
P(Reg(u, v) = empty),
E |Raw(u, v)|,
E |Reg(u, v)|,
longest surviving directed ray inside the finite cap.
```

The next analytic target is to estimate the typical regenerative count for
`h = v - u <= H(v)`:

```text
|Reg(u, v)| roughly
  H / log H
  times a singular-series penalty for avoiding [u, v]
  times the probability of future clearance.
```

The decisive question is whether the singular-series penalty is usually only
polylogarithmically small, rather than exponentially small.
