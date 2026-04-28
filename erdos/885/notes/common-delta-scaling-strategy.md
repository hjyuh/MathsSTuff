# EP885 subtask C: common-delta scaling strategy

Date: 2026-04-26.

## Objective

The current exact checker in `scripts/common_deltas_factor.py` factors each
`N_i`, expands all divisors of each `N_i`, forms each `D(N_i)`, and intersects
the resulting sets.  This is exact, but it scales with the divisor counts of
the `N_i` themselves.  Bremner-family examples quickly reach the point where
the factorization may still be possible but full divisor expansion is the wrong
unit of work.

This note records a better exact strategy: generate candidates from one
pair-difference `Delta = N_j - N_i`, use modular/local filters before expensive
square tests, and only then verify candidates against all `N_i`.

## Basic equivalences

Use

```text
D(N) = {d >= 0 : N = a(a+d) for some integer a >= 1}.
```

For a proposed `d`, set `s = 2a + d`.  Then

```text
d in D(N)
<=> s^2 - d^2 = 4N
<=> d^2 + 4N is a square s^2, with s == d mod 2.
```

So a candidate delta is cheap to verify without factoring `N`:

```text
for every N_i:
    s_i^2 = d^2 + 4N_i must be a square
    s_i == d mod 2
    a_i = (s_i - d) / 2 must be positive
```

This is the final certificate check for any candidate produced by the faster
methods below.

## Difference-first exact enumeration

Let `N_i < N_j` and suppose `d` is common to both.  Write

```text
N_i = a_i(a_i+d)
N_j = a_j(a_j+d)
```

Since `a(a+d)` is increasing for `a >= 0`, we have `a_j > a_i`.  Therefore

```text
Delta = N_j - N_i
      = (a_j - a_i)(a_j + a_i + d).
```

Let

```text
u = a_j - a_i
v = a_j + a_i + d
s_i = 2a_i + d = v - u.
```

Then every common delta for the pair comes from a divisor pair `u*v = Delta`:

```text
s_i = Delta/u - u
d^2 = s_i^2 - 4N_i.
```

Algorithm for an exact common-delta intersection:

1. Choose one ordered pair `N_i < N_j`.
2. Factor `Delta = N_j - N_i`.
3. Enumerate divisors `u | Delta` with `u <= sqrt(Delta)`.
4. Set `s = Delta/u - u`.
5. If `s^2 - 4N_i` is a positive square `d^2` and `s == d mod 2`, keep `d`.
6. Verify each kept `d` against every `N_k` using `d^2 + 4N_k` square tests.

This is exact because

```text
intersection_k D(N_k) subset D(N_i) intersection D(N_j),
```

and the divisor-pair construction enumerates the right-hand side exactly.

The immediate win is that no `D(N_k)` set is materialized.  Only the selected
pair's candidate deltas are materialized.

## Bremner-specific factorization source

For a Bremner `K4,4` table, the generator has half-difference rows

```text
h_{0,r}, h_{1,r}, h_{2,r}, h_{3,r}, h_{4,r}      r = 1..4
```

with

```text
N_i = h_{i,r}^2 - h_{0,r}^2
```

for each of the four existing rows `r`.  Hence for any pair `i,j`,

```text
N_j - N_i = h_{j,r}^2 - h_{i,r}^2
          = (h_{j,r} - h_{i,r})(h_{j,r} + h_{i,r}).
```

This gives four natural factorizations of the same `Delta`.  For huge
Bremner-family examples, do not start by factoring the full `N_i`, and do not
start by factoring the full `Delta` as an opaque integer.  Instead:

1. Re-run `scripts/bremner_map.py` for the family point and keep the integer
   half-difference table.
2. For each pair `i,j` and each row `r`, collect
   `abs(h_{j,r} - h_{i,r})` and `abs(h_{j,r} + h_{i,r})`.
3. Factor these smaller structured factors.
4. Refine the combined factorization by taking gcds between the four displayed
   splits of `Delta`.
5. Choose the `Delta` with the smallest completed divisor count or the easiest
   completed factorization.

The known Bremner rows also give a correctness sentinel: the four printed
deltas must appear in the pair-candidate stream before the final all-`N`
verification.

## Scaling when `Delta` has too many divisors

The pair-difference method still has a divisor-lattice step.  If
`tau(Delta)` is large, add necessary filters before exact square-root tests.

### Size filter

The condition `d^2 = s^2 - 4N_i > 0` implies

```text
s = Delta/u - u > 2*sqrt(N_i).
```

Equivalently,

```text
u < sqrt(N_j) - sqrt(N_i).
```

Use the exact integer inequality

```text
(Delta/u - u)^2 > 4N_i
```

while enumerating divisors.  This can remove large divisor pairs before any
modular or square test.

### Anchor-square residue filter

Fix the anchor pair `N_i < N_j`.  For a modulus `m`, precompute

```text
R_m = {
    s mod m :
    s^2 - 4N_i is a square mod m, and
    s^2 + 4(N_k - N_i) is a square mod m for every k
}.
```

For a divisor pair `u*v = Delta`, the anchor value is `s = v - u`.  If

```text
s mod m not in R_m,
```

then the divisor cannot produce a common delta.

Good moduli are products of small prime powers, especially powers of `2` and
odd primes for which the allowed square-residue set is small.  This filter is
strictly necessary, so it preserves exactness.

### Direct delta residue filter

Independently, for a modulus `m` define

```text
A_m = {
    d mod m : d^2 + 4N_k is a square mod m for every k
}.
```

Once `d^2 = s^2 - 4N_i` is a square modulo `m`, only square roots whose residue
lies in `A_m` can survive.  In implementation this can be combined with the
anchor-square filter by storing square-root residue classes modulo `m`.

### Divisor generation with residue pruning

If full divisor enumeration is too large, do not build the divisor list first.
Use a recursive or meet-in-the-middle divisor generator over the prime powers
of `Delta`:

```text
Delta = product p_l^e_l.
```

Track both `u mod M` and the complementary factor `v = Delta/u mod M`.  A leaf
only matters if `v - u mod M` lies in `R_M`.  For primes not dividing `M`, the
residue contribution is periodic in the exponent.  For primes dividing `M`,
track the valuation separately.  This lets the modular filter act on exponent
vectors before the corresponding large integer divisor is constructed.

A practical meet-in-the-middle version:

1. Split the prime powers of `Delta` into two groups.
2. Enumerate partial products with `(residue mod M, log-size, exact value)`.
3. Join only residue pairs that can make `v-u` land in `R_M`.
4. Apply the size filter and integer square test only to joined survivors.

This is still an exact enumeration of divisors of the chosen `Delta`; it just
does not materialize the whole divisor set.

## Necessary filters for an extra common delta

The following conditions are useful for ruling out candidates before expensive
work.  They are only necessary conditions, so any survivor still needs the
final square verification.

### Pair-difference divisibility

For every pair `N_i < N_j`, an extra common delta `d` gives

```text
s_i = sqrt(d^2 + 4N_i)
s_j = sqrt(d^2 + 4N_j)
u_ij = (s_j - s_i)/2
v_ij = (s_j + s_i)/2
u_ij * v_ij = N_j - N_i.
```

Thus the extra delta determines a divisor of every pair difference.  Enumerate
from the easiest pair, but verify this divisibility for all pairs as a cheap
sanity check.

### Parity and 2-adic restrictions

If any `N_i` is odd, then `d` must be even.  If any `N_i == 2 mod 4`, then
`d` must be odd.  These two requirements are incompatible.

For even `d` and odd `N_i`:

```text
d == 0 mod 4  => N_i == 1 mod 4
d == 2 mod 4  => N_i == 3 mod 4
```

So a mix of odd `N_i == 1 mod 4` and odd `N_i == 3 mod 4` rules out every even
common delta.  Higher powers of `2` should be handled by the general modular
square-residue test:

```text
d^2 + 4N_i must be a square mod 2^e.
```

### Prime divisors of `d`

If an odd prime `p` divides `d`, then

```text
N_i = a_i(a_i+d) == a_i^2 mod p
```

for every `i`.  Therefore every `N_i` must be a quadratic residue or `0`
modulo `p`.  Equivalently, if some `N_i` is a quadratic nonresidue modulo `p`,
then no common delta is divisible by `p`.

Also, if `p | d` and `p | N_i`, then both factors `a_i` and `a_i+d` are
divisible by `p`, so `p^2 | N_i`.  Hence any prime with `v_p(N_i) = 1` for
some `i` cannot divide a common delta.

For prime powers, use the local condition

```text
d^2 + 4N_i is a square mod p^e for every i.
```

This subsumes the Legendre-symbol test and is easy to include in `A_m`.

### Known-delta exclusion

For Bremner-family promotion, the four construction deltas are already known.
An "extra" delta must satisfy the same filters and also be outside that set.
The exact pair-difference pipeline should report both:

```text
pair_common_deltas
all_N_common_deltas
extra_common_deltas = all_N_common_deltas - bremner_seed_deltas
```

This prevents confusing a pair-only accidental delta with a genuine fifth
common delta.

## Local scale check from existing runs

A quick check against the existing JSON data shows why the pair-difference
method is the right next implementation target.

```text
family point | max N digits | old per-N delta counts       | best tau(Delta) | pair candidates
-------------|--------------|------------------------------|-----------------|----------------
3Q+T         | 12           | 96, 700, 1296, 1080          | 192             | 5
5Q+T         | 35           | 352800, 38880, 486000, 933120| 10368           | 5
6Q           | 47           | 589680, 2449440, 2338875,
             |              | 3564000                      | 124416          | 5
```

In each case, the final all-`N` verification leaves exactly the four Bremner
deltas.  The fifth pair candidate, when present, fails at least one of the
other `N_k`.

The important point is not that `tau(Delta)` is always tiny.  It is that the
candidate stream after the square and residue filters is tiny, and it is
generated from one selected pair rather than from four full `D(N_i)` sets.

## Recommended next helper

If this becomes code, make it a separate helper rather than changing the
current checker in place.  Suggested name:

```text
scripts/common_deltas_pairdiff_<unique_suffix>.py
```

Inputs:

```text
--json          Bremner-map JSON with N_values, and ideally half_difference_table
--pair          optional pair index; otherwise auto-select cheapest Delta
--modulus       optional product of small prime powers for residue pruning
--known-deltas  optional comma-separated seed deltas to classify extras
```

Outputs:

```text
selected_pair
Delta_factorization
Delta_divisor_count
residue_modulus
residue_allowed_count
pair_candidate_count
all_N_common_deltas
extra_common_deltas
verification_records
```

Exact negative claims should require a complete factorization of the selected
`Delta`, or an explicit proof that every unexpanded cofactor branch is killed
by the residue filters.  Positive claims only require the final integer square
verification for the reported delta.
