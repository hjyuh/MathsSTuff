# EP885: Bremner Reconstruction and the K5 Analogue

Date: 2026-04-26.

This note records the working reconstruction of Bremner's `k = 4` construction
and what it suggests for the first open case `k = 5`.

## Incidence Translation

If `d = 2x_0`, then

```text
N = a(a+d)
```

is equivalent to

```text
N = x_i^2 - x_0^2
```

with factor pair

```text
a = x_i - x_0,    a+d = x_i + x_0.
```

Thus Bremner's half-differences `(x_0,y_0,z_0,t_0)` correspond to EP885
deltas

```text
2|x_0|, 2|y_0|, 2|z_0|, 2|t_0|.
```

A `K4,4` certificate is therefore a table

```text
(x_i,y_i,z_i,t_i),    i = 0,1,2,3,4,
```

such that for each column `i = 1,2,3,4`,

```text
x_i^2 - x_0^2
= y_i^2 - y_0^2
= z_i^2 - z_0^2
= t_i^2 - t_0^2
= N_i.
```

## Bremner's Construction, Dependency Graph

Bremner starts with the three-difference subsystem

```text
x_0^2 - y_0^2 = x_i^2 - y_i^2,
x_0^2 - z_0^2 = x_i^2 - z_i^2,
```

for `i = 1,2`.  This is parametrized by six variables

```text
b,c,d,q,r,s.
```

Those variables produce rational values

```text
(x_i,y_i,z_i),    i = 0,1,2.
```

Then set

```text
A = x_0^2 - z_0^2,
B = x_0^2 - y_0^2,
```

and use the full-2-torsion elliptic curve

```text
E_1: V^2 = U(U-A)(U-B).
```

The points with `U = x_i^2` lie in `2E_1(Q)`.  Adding such points gives new
`U`-coordinates that are again squares and therefore generates new columns.
Bremner chooses two such sums to obtain columns `i = 3,4`.  At this stage
there are four `N_i` sharing the first three half-differences `x_0,y_0,z_0`.

The fourth half-difference `t_0` is forced in stages:

1. Use

   ```text
   E_2: Y^2 = X(X+N_1)(X+N_2)
   ```

   to choose `t_0,t_1,t_2`.

2. Use two more elliptic curves, one tied to `N_3` and one tied to `N_4`, to
   choose `t_3,t_4`.

3. The remaining compatibility conditions factor into polynomial choices.
   Bremner selects the branch `f_34 = 0`, `f_41 = 0`.

4. The `f_41` equation is quadratic in one parameter.  Its square-discriminant
   condition is an elliptic quartic, which maps to a cubic curve.

5. Substitution reduces the remaining `f_34` condition to a genus-1 curve

   ```text
   E: Y^2 = X^3 + X^2 - 120X + 400.
   ```

This final curve has generator

```text
Q = (0,20)
```

and 2-torsion point

```text
T = (4,0).
```

Multiples of `Q` feed into Bremner's rational map and produce infinitely many
non-degenerate `K4,4`-type tables.  Only some of those tables have all `N_i`
positive, which is the version relevant for EP885.

## Local Exact Generator

The reconstruction is implemented in:

```text
scripts/bremner_map.py
```

Example:

```powershell
python .\erdos\885\scripts\bremner_map.py --n 3 --torsion
```

This uses `3Q + T` and reproduces Bremner's printed example:

```text
N_values = [26941381929, 94011840000, 455923353600, 728783193600]
deltas   = [83160, 451528, 910800, 1386000]
```

The output signs and row order can differ from the printed table, but the
factor differences are absolute values and the certificate verifies.

Likewise:

```powershell
python .\erdos\885\scripts\bremner_map.py --n 4
```

reproduces the `4Q` example:

```text
N_values = [
  3682673190625,
  94040161560576,
  292916434882500,
  1488767454720000
]
deltas = [1441440, 15615600, 27986400, 48620880]
```

Generated JSON snapshots:

```text
results/bremner-map-3Q-plus-T.json
results/bremner-map-4Q.json
results/bremner-map-5Q-plus-T.json
```

The `5Q+T` point also gives four positive `N_i`, but exact factorization shows
again that the common delta intersection has size exactly `4`.

## What the K5 Analogue Asks For

For `k = 5`, one would need five half-differences

```text
x_0,y_0,z_0,t_0,u_0
```

and five columns `N_1,...,N_5`, with

```text
x_i^2 - x_0^2
= y_i^2 - y_0^2
= z_i^2 - z_0^2
= t_i^2 - t_0^2
= u_i^2 - u_0^2
= N_i
```

for `i = 1,...,5`.

Using `x` as the reference row, this is

```text
5 * 4 = 20
```

quadratic equations, which matches Bremner's concluding warning.

The tempting strategy is:

1. Use Bremner's first elliptic curve mechanism to create many columns sharing
   three half-differences.

2. Add a fourth half-difference by a Bremner-style specialization.

3. Try to add a fifth half-difference by imposing one more simultaneous
   square-translate layer.

The problem is step 3.  In the `k = 4` case, the fourth row already requires a
careful branch choice and a rank-one genus-1 curve.  Adding `u_0` would require
another row satisfying all existing columns, and also a fifth column if one is
aiming at a full `K5,5`.  Naively this means intersecting several elliptic
conditions at once, which should usually jump to higher-genus or higher-rank
geometry rather than another friendly rank-one elliptic curve.

## Current Computational Interpretation

The first Bremner seed is rigid under cheap extension tests:

- exactly four common deltas for the four seed columns;
- no fifth column for the four seed deltas up to `10^12`;
- no nontrivial product lift through multiplier `5000`;
- no useful one-row swap through the tested range;
- no K4,4 in the tested integer quartic slice through `p = 500000`.

This suggests that `k = 5` is not likely to come from a local promotion of one
printed Bremner seed.  The next serious search should work on the rational
family itself:

1. Generate many positive Bremner-family K4,4 certificates from `nQ` and
   `nQ+T`.

2. For each positive certificate, factor the four `N_i` values and compute the
   exact common delta intersection.  This can detect accidental fifth deltas
   without enumerating up to `sqrt(N_i)`.

3. Look for a symbolic condition on the final curve point `(X,Y)` that makes an
   additional half-difference `u_0` possible.

4. If no accidental fifth deltas appear, formulate the fifth-row condition as a
   curve or surface over Bremner's final elliptic curve and estimate its genus
   or dimension.

The right next milestone is therefore not a broader brute-force scan; it is an
exact factorization-based Bremner-family scanner.

The exact factorization common-delta extractor is:

```text
scripts/common_deltas_factor.py
```

It has already confirmed that the printed examples from `3Q+T`, `4Q`, and the
newly generated `5Q+T` example each have exactly four common deltas.

The family scanner is:

```text
scripts/bremner_family_scan.py
```

It supports per-`N` factorization timeouts and an anchor-divisor bound, because
some Bremner-family examples factor quickly but have enormous divisor lattices.
The exact common-delta check enumerates only the smallest-divisor anchor and
tests candidate deltas against the remaining `N_i` by the square criterion.

Runs so far:

```text
runs/20260426_bremner_family_scan_n3_8_d60.json
runs/20260426_bremner_family_scan_n3_14_d90_t12_a5m.json
runs/20260426_bremner_family_scan_n7_10_d130_t12_a25m.json
runs/20260426_bremner_family_scan_n3_8_d90.json
```

The bounded scans checked `3Q+T`, `4Q`, `5Q+T`, `6Q`, and `7Q+T`, all with
exactly four common deltas.  An unbounded anchor run additionally checked
`8Q+T` exactly; it also has exactly four common deltas.  No Bremner-family
point checked so far has produced an accidental fifth common delta.
