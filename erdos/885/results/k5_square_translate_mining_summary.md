# EP885 k=5 square-translate mining sprint

Date: 2026-04-26.

## New tools

Added:

```text
scripts/square_translate_biclique_mine.py
scripts/pair_column_extend_mine.py
scripts/extend_mined_candidates.py
scripts/sage_compatibility_runner.py
```

Both work in the normalization

\[
z^2+N=y^2.
\]

A \(K_{r,s}\) packet in this graph gives an EP885 packet with differences

\[
d_j=2z_j,
\]

because

\[
d_j^2+4N_i=4y_{ij}^2.
\]

Also updated:

```text
scripts/fifth_column_crt_search.py
scripts/elliptic_factor_export.py
scripts/magma_compatibility_export.py
```

It now accepts custom row sets via `--n-values` and `--deltas`, not only
Bremner-family seeds.  The elliptic/Sage and compatibility/Magma exporters now
also accept custom \(K_{4,4}\) seeds.

## Calibration and search results

### Small direct biclique mining

Runs:

```text
z <= 1500, N <= 2,000,000, target K5,5
z <= 3000, N <= 5,000,000, target K4,5
```

Result:

```text
no K5,5;
no K4,5.
```

The best overlaps in these small boxes were only row-pairs with five or more
common columns.

### Pair-extension mining

The pair-extension miner first finds dense row-pairs, then tests whether a
selected common column subset has more supporting rows.

Runs:

```text
z <= 3000, N <= 5,000,000, target K3,5: no hit
z <= 3000, N <= 5,000,000, target K5,4: no hit

z <= 8000, N <= 20,000,000, target K3,5: no hit
z <= 8000, N <= 20,000,000, target K5,4: no hit
```

The \(K_{5,4}\)-oriented run did rediscover the forum guidepost triple

\[
N=(79200,227205,1258560),
\qquad
z=(18,234,346,514),
\]

equivalently

\[
d=(36,468,692,1028).
\]

This verifies that the miner is aligned with the known comment data.

### Large calibration run

Run:

```text
z <= 11000, N <= 50,000,000, target K3,5
row_limit = 15000
```

Result:

```text
found exactly the known forum K3,5 packet:
N = (756000, 15971200, 45130176)
z = (330, 870, 2445, 4155, 10482)
d = (660, 1740, 4890, 8310, 20964)
```

Run:

```text
z <= 11000, N <= 50,000,000, target K5,4
row_limit = 15000
```

Result:

```text
no K5,4.
```

The best subsets had four rows and four columns.  The top two verified
\(K_{4,4}\) packets were:

```text
N = (493920, 9774765, 19511685, 46687680)
z = (126, 854, 2898, 10278)
d = (252, 1708, 5796, 20556)
```

and

```text
N = (274833, 1225728, 3368448, 30159360)
z = (216, 1116, 1656, 4724)
d = (432, 2232, 3312, 9448)
```

The exact verification JSON files are:

```text
results/square_translate_mine/seed_k44_z126_854_2898_10278.json
results/square_translate_mine/seed_k44_z216_1116_1656_4724.json
```

## Extension tests on the new K4,4 packets

For each of the two new \(K_{4,4}\) packets:

1. searched for an extra shift \(N'\) for the fixed four \(z\)-columns up to
   \(m\le10^{12}\), where \(N'=m^2-z_0^2\);
2. searched for an extra rational column \(X\) for the fixed four rows using
   CRT rational reconstruction to height \(20000\).

Results:

```text
no new fifth shift up to m <= 10^12;
no new fifth column up to rational height 20000.
```

Only the original four shifts/columns were recovered.

Result files:

```text
results/square_translate_mine/extra_shift_seed_z126_854_2898_10278_m1e12.json
results/square_translate_mine/extra_shift_seed_z216_1116_1656_4724_m1e12.json
results/square_translate_mine/fifth_column_seed_z126_854_2898_10278_h20000.json
results/square_translate_mine/fifth_column_seed_z216_1116_1656_4724_h20000.json
```

## Automated candidate-extension pass

Added `scripts/extend_mined_candidates.py`, which extracts \(K_{3,5}\),
\(K_{4,4}\), and \(K_{5,4}\)-shaped candidates from mining output and runs the
appropriate low-height extension tests automatically.

Run:

```text
results/square_translate_mine/extend_candidates_quick_top10.json
```

Inputs:

```text
pair_extend_z11000_n50m_k35_full15000.json
pair_extend_z11000_n50m_k54_full15000.json
```

Extracted candidates:

```text
2 x K4,4
1 x K3,5
```

Result:

```text
no positive extension in the quick bounds.
```

For the \(K_{3,5}\), the extra-shift scan recovered only the three known
shifts.  For each \(K_{4,4}\), the extra-shift and fifth-column scans recovered
only the old data.

## New Sage/Magma exports

Generated elliptic-factor Sage scripts and genus-2 compatibility Magma scripts
for the two mined \(K_{4,4}\) seeds:

```text
results/elliptic_factors/mined_z126_854_2898_10278.sage
results/elliptic_factors/mined_z216_1116_1656_4724.sage
results/magma_compatibility/mined_z126_854_2898_10278_compatibility.magma
results/magma_compatibility/mined_z216_1116_1656_4724_compatibility.magma
```

Native Sage/Magma is not installed in this environment.  Docker Desktop is
available, and the `sagemath/sagemath:latest` container was pulled successfully:

```text
SageMath version 10.8, Release Date: 2025-12-18
```

The two Sage elliptic-factor scripts were run through Docker.  Output files:

```text
results/elliptic_factors/mined_z126_854_2898_10278.sage.out
results/elliptic_factors/mined_z216_1116_1656_4724.sage.out
```

Rank-bound summary:

```text
mined_z126_854_2898_10278:
  E123   rank bounds (4,6), known generated rank <= 4
  E124   rank bounds (3,5), known generated rank <= 3
  E134   rank bounds (6,6), known generated rank <= 4
  E234   rank bounds (4,4), known generated rank <= 4
  E1234  rank bounds (4,4), known generated rank <= 3

mined_z216_1116_1656_4724:
  E123   rank bounds (4,4), known generated rank <= 4
  E124   rank bounds (4,4), known generated rank <= 4
  E134   rank bounds (3,5), known generated rank <= 3
  E234   rank bounds (4,4), known generated rank <= 3
  E1234  rank bounds (3,5), known generated rank <= 4
```

This is mixed evidence.  The elliptic factors have substantial rank, so these
seeds are not rank-cold.  However, the visible old columns already account for
much of the proven lower rank, and the earlier bounded fifth-column searches
did not find new square \(t\)-values.

Magma is still not available locally; the Magma scripts are ready to run
elsewhere.  A Sage translation of the genus-2 compatibility workflow was added:

```text
scripts/sage_compatibility_runner.py
```

It computes the genus-2 curves

\[
D_m: Z^2=\prod_{i\ne m}(W^2+N_i-N_m),
\]

uses the elliptic splitting

\[
\operatorname{Jac}(D_m)\sim E_{I_m}\times E_{1234}
\]

to get rank bounds, and performs bounded rational \(W\)-searches for points
that lift back to \(C\) with square \(t\).

Integer search output:

```text
results/elliptic_factors/mined_z126_854_2898_10278_compatibility_sage_int20000.json
results/elliptic_factors/mined_z216_1116_1656_4724_compatibility_sage_int20000.json
```

Rational search output with \(|\operatorname{num}(W)|\le 20000\) and
\(\operatorname{den}(W)\le20\):

```text
results/elliptic_factors/mined_z126_854_2898_10278_compatibility_sage_num20000_den20.json
results/elliptic_factors/mined_z216_1116_1656_4724_compatibility_sage_num20000_den20.json
```

Result:

```text
For both mined K4,4 seeds, every D_m search found exactly the eight old
signed points and no new lift to C.  In particular, no new square-t point
appeared in the denominator <= 20 search.
```

The Jacobian rank bounds via the elliptic splitting are high:

```text
mined_z126: D_m rank bounds [8,8], [10,10], [7,9], [8,10]
mined_z216: D_m rank bounds [7,9], [6,10], [7,9], [7,9]
```

So ordinary genus-2 Chabauty is not available for these \(D_m\)'s.  Magma is
therefore not needed for this exploratory layer, but it may still be useful for
more serious Mordell-Weil sieve / elliptic Chabauty work.

The key information still needed from Magma or a deeper Sage implementation is:

```text
whether the high-rank D_m curves can be sieved enough to prove that no further
rational points lift to C with square t;
or, more optimistically, whether an elliptic-cover / Mordell-Weil sieve search
finds such a point.
```

## Assessment

This sprint improved the computational base:

- we now have an independent square-translate miner;
- it rediscovers the known forum \(K_{3,5}\) at the expected scale;
- it produced fresh verified \(K_{4,4}\) seeds;
- those fresh seeds do not extend by low-height accident in either direction.

But it did **not** produce a \(K_{4,5}\), \(K_{5,4}\), or \(K_{5,5}\).

Current honest estimate:

```text
isolated K5,5: 35-40%
full EP885:    15-20%
```

To cross 50% for the isolated \(k=5\) case, we still need one of:

1. a verified \(K_{4,5}\) or \(K_{5,4}\) packet from search;
2. Sage/Magma rank evidence that one of these \(K_{4,4}\) seeds has a
   positive-rank fifth-column quotient;
3. a constructive parameter family that deliberately builds \(K_{4,5}\) or
   \(K_{5,4}\), instead of hoping for accidental extension.
