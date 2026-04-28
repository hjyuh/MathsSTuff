# EP885 sprint 4: Bremner paper acquired

Date: 2026-04-26.

## Summary

The Bremner paper is now available locally:

```text
erdos/885/On a problem of Erdos related to common factor differences_ -- Bremner, Andrew ... .pdf
```

Bibliographic target:

```text
Andrew Bremner, "On a problem of Erdos related to common factor differences",
International Journal of Number Theory 15.5 (2019), 1059-1068,
DOI 10.1142/S1793042119500581.
```

The paper gives explicit K4,4 examples.  In Bremner's notation the listed
common values `(x_0,y_0,z_0,t_0)` are half-differences, so the EP885 incidence
deltas are twice those numbers.

The rational construction has also been reconstructed locally in:

```text
scripts/bremner_map.py
```

See:

```text
bremner-reconstruction-and-k5-analogue.md
```

The script reproduces the printed `3Q+T` and `4Q` examples from Bremner's
rank-one elliptic curve

```text
Y^2 = X^3 + X^2 - 120X + 400.
```

I also added:

```text
scripts/common_deltas_factor.py
scripts/bremner_family_scan.py
```

These compute exact common delta intersections from factorizations of the
`N_i` values and scan Bremner's rank-one family.  This is the right tool
because direct enumeration to `sqrt(N_i)` becomes impossible once the generated
values have dozens of digits.

## Verified K4,4 certificates

### Bremner example 1

```text
N_values = [26128575, 291722431, 561117375, 713526975]
deltas   = [126, 16110, 33390, 75390]
```

Certificate:

```text
results/bremner-example-1-k44-certificate.json
```

### Bremner example 2

```text
N_values = [26941381929, 94011840000, 455923353600, 728783193600]
deltas   = [83160, 451528, 910800, 1386000]
```

Certificate:

```text
results/bremner-example-2-k44-certificate.json
```

### Bremner example 3

```text
N_values = [
  3682673190625,
  94040161560576,
  292916434882500,
  1488767454720000
]
deltas = [1441440, 15615600, 27986400, 48620880]
```

Certificate:

```text
results/bremner-example-3-k44-certificate.json
```

Exact common-delta factor checks:

```text
results/bremner-example-2-common-deltas-factor.json
results/bremner-example-3-common-deltas-factor.json
results/bremner-map-5Q-plus-T-common-deltas-factor.json
```

All currently checked Bremner-family positive examples have exactly four
common deltas, not five.

The first family scan is:

```text
runs/20260426_bremner_family_scan_n3_8_d60.json
```

It checked `3Q+T`, `4Q`, `5Q+T`, and `6Q`; no candidate with five common deltas
appeared.

## Extension checks on example 1

### Exact shared-delta check

Run:

```text
runs/20260426_bremner1_verify_complete
```

Result:

```text
common_delta_count = 4
strict_extension_status = impossible_retaining_all_seed_columns
```

So this K4,4 cannot become a K5,4 by adding a fifth common delta while keeping
all four original columns.

### Fixed-row extension

Run:

```text
runs/20260426_bremner1_fixedrows_1e12
```

Rows:

```text
[126, 16110, 33390, 75390]
```

Result:

```text
x_bound = 1000000000000
column_count = 4
witness_count = 0
```

Keeping the four Bremner deltas fixed gives no fifth column up to `10^12`.

### Product lift

Run:

```text
runs/20260426_bremner1_productlift_m5000
```

Result:

```text
m_max = 5000
lift_count = 770
nontrivial_lift_count = 0
trivial_square_scale_count = 770
```

Only trivial square scalings appear.

### Quartic parameter scan

Run:

```text
runs/20260426_bremner1_quartic_p500k.json
```

Result:

```text
p_max = 500000
total_hit_count = 192
k44_candidate_count = 0
```

This scan is only a thin integer slice of the elliptic setup, but it did not
find a new K4,4 candidate.

### Row-swap search

Run:

```text
runs/20260426_bremner1_rowswap_1e10
```

Result:

```text
x_bound = 10000000000
rowset_count = 500
witness_count = 0
best rowsets have only column_count = 2
```

Seed-derived one-row swaps do not produce serious near misses.

### Restricted delta mine

Run:

```text
runs/20260426_bremner1_restrictedmine_1e10
```

Result:

```text
x_bound = 10000000000
delta_universe_count = 9
triple_count = 11
rowset_count = 0
witness_count = 0
```

## Bremner-family scan

The exact family generator and scanner are:

```text
scripts/bremner_map.py
scripts/common_deltas_factor.py
scripts/bremner_family_scan.py
```

The common-delta checker now uses anchor enumeration: factor all four `N_i`,
pick the one with the smallest divisor count, enumerate only its deltas, and
test candidates against the other columns by the square criterion
`delta^2 + 4N = square`.

Runs:

```text
runs/20260426_bremner_family_scan_n3_14_d90_t12_a5m.json
runs/20260426_bremner_family_scan_n7_10_d130_t12_a25m.json
runs/20260426_bremner_family_scan_n3_8_d90.json
```

Results:

```text
checked exactly: 3Q+T, 4Q, 5Q+T, 6Q, 7Q+T, 8Q+T
candidate_count = 0
common_delta_count = 4 for every checked point
```

The `8Q+T` check had 89-digit `N_i` values and still found exactly the four
constructed deltas.  Some larger entries were generated but skipped by digit or
anchor-divisor bounds.

## Interpretation

Bremner gives the missing K4,4 seed data, but the first verified seed is rigid
under all cheap extension tests:

- no fifth shared delta for the four Bremner columns;
- no fifth column for the four Bremner rows up to `10^12`;
- no nontrivial product lift through multiplier `5000`;
- no K4,4 in the tested quartic integer slice through `p = 500000`;
- no useful one-row swap or restricted seed-derived delta mine.
- no accidental fifth common delta in the checked Bremner-family points through
  `8Q+T`.

The next serious EP885 push should not be "extend this exact seed by brute
force."  It should either formalize Bremner's elliptic construction and search
inside its parameter space, or derive the five-difference analogue and look for
structure in the resulting 20 quadratic equations.
