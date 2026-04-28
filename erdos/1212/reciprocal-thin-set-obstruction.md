# Reciprocal Thin-Set Obstruction

Date: 2026-04-28

## Purpose

This note records the obstruction identified in the 5.2 pass:

```text
For H(x)=x^theta with 1/3 < theta < 1/2, core successors are rough semiprimes,
and choosing one large prime factor determines at most one candidate successor
inside the H-window.
```

Thus the missing theorem is not an ordinary short-interval almost-prime
theorem. It is a prime/almost-prime theorem on a sparse reciprocal set.

## Semiprime Rigidity

Let

```text
H(x)=floor(x^theta),    1/3 < theta < 1/2.
```

If `n ~ X`, `n` is composite, and

```text
P^-(n) > H(n),
```

then `n` has exactly two prime factors for all sufficiently large `X`.
Indeed, three prime factors would force

```text
n > X^(3theta) > X.
```

So the right-core and strong-core graphs in this range are rough-semiprime
graphs.

## Reciprocal Parameterization

Fix a core state `(u,v)` and write `H=H(v)`. If

```text
v < w <= v+H
```

and a prime `r > H` divides `w`, then there is at most one such `w` for this
`r`, because the window length is smaller than `r`.

Define

```text
t_r = (-v) mod r,      0 <= t_r < r,
w_r = v + t_r.
```

Then `r | w` and `v < w <= v+H` is equivalent to

```text
1 <= t_r <= H,    w = w_r.
```

In the semiprime core, `w_r` is a valid rough-semiprime candidate exactly when

```text
q_r = w_r / r = ceil(v/r)
```

is prime and both `r,q_r` exceed the core threshold. This is the sparse
reciprocal-prime condition.

## Diagnostic Script

Script:

```text
scripts/reciprocal_candidate_stats.py
```

It reports, by slab:

```text
tested_primes:
  primes r above the core threshold and below sqrt(v+H).

window_multiples:
  primes r whose first multiple after v lies in (v,v+H].

reciprocal_semiprimes:
  candidates where w_r/r is prime and the semiprime is still core.

backward_clean:
  reciprocal semiprimes also satisfying gcd(w, product_{t=u}^v t)=1.

forward_clear:
  candidates also satisfying clr(v;w)>=H(w).

valid_core_successors:
  candidates whose target pair is a core state.
```

## Million-Scale Results

For the ordinary `C=1` core at `N=1000000`:

```text
theta  slab              tested  multiples  semiprime  backward  valid  valid-zero
0.34   [262144,524288)   91.94   28.20      3.595      3.364     2.734  0.122
0.36   [262144,524288)   86.86   31.05      4.047      3.769     2.982  0.118
0.38   [262144,524288)   81.71   34.31      4.544      4.178     3.136  0.126
0.40   [262144,524288)   74.24   36.16      4.874      4.432     3.132  0.139
```

For the strong `C=2.1` core at `N=1000000`:

```text
theta  slab              tested  multiples  semiprime  backward  valid  valid-zero
0.34   [262144,524288)   75.31   17.13      2.264      2.264     2.264  0.084
0.36   [262144,524288)   66.66   17.51      2.370      2.370     2.370  0.077
0.38   [262144,524288)   55.18   16.61      2.288      2.288     2.287  0.084
0.40   [262144,524288)   42.12   14.49      2.023      2.023     2.023  0.118
```

The strong core behaves exactly as predicted: after a reciprocal semiprime is
found, the backward and forward filters essentially stop costing anything.

## Interpretation

The bottleneck has shifted to a cleaner but still hard object:

```text
Find enough primes r such that the reciprocal cofactor ceil(v/r) is prime,
and show that these local choices have compatible directed survival across
slabs.
```

This explains why the project does not close from existing short-interval
almost-prime results. Those theorems count almost primes in dense intervals.
Here the candidates form a thin reciprocal set of size roughly the number of
large primes whose first multiple after `v` lands in the window.

## Missing Theorem

A close-to-minimal theorem that would close the current route is:

> For some `1/3 < theta < 1/2` and some `C > 2`, the strong `C`-core
> reciprocal rough-semiprime transition graph has compatible dyadic slab
> survival.

Expanded, this means proving enough directed expansion for states `(u,v)` so
that the candidates

```text
w_r = v + ((-v) mod r),    r > C H(v),
q_r = w_r / r prime,
```

not only exist locally but also land in future-surviving core states.

This is the current analytic wall.
