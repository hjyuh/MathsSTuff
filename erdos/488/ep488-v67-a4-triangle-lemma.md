# EP-488 v67 A4 Triangle Lemma

Date: 2026-05-18

Status: rigorous A4 subcase theorem. This does not solve A4 or EP-488.

## Theorem

Let `Z` be a pure-cycle host with normalized cycle `{12,15,20}`. Equivalently,
for some integer `s >= 1`,

```text
Z = {12s, 15s, 20s}.
```

Assume the reduced top-window triangle hypotheses:

```text
20s < q < 24s,
q does not divide 60s,
60s <= n < 3q,
m > n.
```

Then the A4 pure-cycle inequality holds:

```text
N_Z(m)/m <= 2H_Z#(n)/n,
```

where

```text
H_Z#(x) = c_x(12s;q) + c_x(15s;q) + c_x(20s;q) - 3c_x(60s;q),
N_Z(x)  = H_Z#(x) + c_x(60s;q).
```

In particular, every A4 pure-cycle realization of the normalized triangle
`{12,15,20}` is harmless.

## Proof

The top-window conditions force

```text
floor(n/(12s)) = 5,
floor(n/(15s)) = 4,
floor(n/(20s)) = 3,
floor(n/(60s)) = 1.
```

Also `q does not divide 60s`, and `20s < q < 24s`.

First note that

```text
lcm(60s,q) >= 180s.
```

Indeed, if `q/gcd(60s,q) = 2`, then `q/2` is a divisor of `60s` strictly
between `10s` and `12s`; this is impossible, with the endpoint `12s`
corresponding to the excluded value `q = 24s`. Hence
`q/gcd(60s,q) >= 3`.

Since `n < 3q < 72s`, no q-excluded correction occurs in the `60s` term at
height `n`.

Now the only possible q-excluded correction among the three positive vertex
terms is the `15s` term. More explicitly:

- a correction in the `20s` term would require
  `q/gcd(20s,q) <= 3`, which forces `q >= 30s`;
- a correction in the `12s` term would require
  `q/gcd(12s,q) <= 5`, which forces `q >= 24s`;
- a correction in the `15s` term can occur only in the case
  `q = 45s/2`, with `s` even.

The divisor check behind these three bullets is the same each time: if
`q = h gcd(ds,q)` with `gcd(ds,q) | ds`, then the constraint `q > 20s`
forces that divisor to be a large divisor of `ds`. The only possible divisor
quotients are then `1` or `2`, except for endpoint cases that give
`q = 24s`; the only value still lying in `(20s,24s)` is
`q = 45s/2` from the `15s` term.

Therefore

```text
H_Z#(n) >= 8.
```

Because `n < 3q < 72s`, this gives

```text
2H_Z#(n)/n > 16/(72s) = 2/(9s).
```

It remains to bound `N_Z(m)`. For every `m`, put `k = floor(m/s)`. Since
`m >= sk`,

```text
c_m(12s;q) <= floor(k/12),
c_m(15s;q) <= floor(k/15),
c_m(20s;q) <= floor(k/20).
```

For the negative cycle-lcm term,

```text
-2c_m(60s;q)
 = -2floor(m/(60s)) + 2floor(m/lcm(60s,q))
 <= -2floor(k/60) + 2floor(k/180),
```

using `lcm(60s,q) >= 180s`.

Thus

```text
N_Z(m)
 <= floor(k/12) + floor(k/15) + floor(k/20)
    - 2floor(k/60) + 2floor(k/180).
```

Since `m > n >= 60s`, we have `k >= 60`. The following finite floor inequality
holds for every `k >= 60`:

```text
floor(k/12) + floor(k/15) + floor(k/20)
- 2floor(k/60) + 2floor(k/180)
<= 41k/228.
```

It is enough to check `60 <= k < 240`, because increasing `k` by `180` raises
the left side by `32`, while `41(k+180)/228 - 41k/228 = 615/19 > 32`.
The finite table has maximum exactly

```text
k = 228,
left side = 41,
left side / k = 41/228.
```

Therefore

```text
N_Z(m)/m <= 41/(228s).
```

Finally,

```text
41/228 < 2/9,
```

so

```text
N_Z(m)/m <= 41/(228s) < 2/(9s) < 2H_Z#(n)/n.
```

This proves the triangle A4 lemma.

## Sharpness Signal

The v66 family

```text
q = 24s - 1,
n = 72s - 4,
m = 108s
```

still gives the observed strongest ratio to the A4 bound:

```text
(N_Z(m)/m) / (2H_Z#(n)/n)
= 19/27 - 19/(486s).
```

The proof above is intentionally coarser than this sharp family. It is strong
enough to close the entire normalized triangle subcase.

## Exact Verification Harness

Script:

```powershell
python .\ep488_v67_a4_triangle_exact.py --max-s 80 --keep-top 40 --exact-top 80 --json-out ep488_v67_a4_triangle_exact_s80.json
```

Result:

```text
max_s = 80
total_cases = 4153680
H_n_counts = {'9': 4141380, '8': 12300}
eta_nonpositive = 0
exact_checked = 235
failures = 0
max_cutoff = 9570
```

The strongest exact row in the finite-certificate check was:

```text
s = 80
q = 1919
n = 5756
m = 8640
best/B = 27341/38880 ~= 0.7032150206
```

The finite floor table used in the proof was also checked:

```text
range = 60..239
best = 41/228 at k = 228
bad_count = 0
41/228 < 2/9
```

## Closure State

```text
A2: not closed
A4: triangle pure-cycle subcase closed; longer pure cycles remain open
EP-488: not solved
```
