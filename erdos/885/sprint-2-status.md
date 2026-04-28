# EP885 sprint 2 status

Date: 2026-04-26.

Goal for the sprint: move EP885 from broad scouting into a reproducible attack
surface for the first open case, `k = 5`.

## What changed

New or updated working files:

- `known-constructions.md`: normalized notes on the known `k = 2,3,4` chain,
  including verified small seeds and the parsed Jimenez-Urroz DVI example.
- `seed-extension-plan.md`: algorithmic plan for fixed-row extension, row swaps,
  product lifts, Bremner-seed intake, and restricted delta mining.
- `algebraic-lifting-notes.md`: product/scaling identities, elliptic lift
  directions, local-obstruction tests, and falsifiable algebraic tests.
- `literature-risk-pass.md`: adversarial literature pass; no post-2019 `k = 5`
  or all-`k` solution found.
- `scripts/seed_extend.py`: reproducible seed-extension runner with output
  safety.

The new runner currently supports:

- `verify-seed`
- `fixed-rows`
- `row-swap`

Every run refuses to reuse an existing output directory and writes `run.json`,
`summary.json`, and `complete.json`.

## Verified seeds

The forum seed is

```text
N = [79200, 227205, 1258560]
D = [36, 468, 692, 1028]
```

It verifies as a `K_{4,3}`.  Complete intersection:

```text
D(79200) cap D(227205) cap D(1258560)
  = [36, 468, 692, 1028].
```

Therefore no `K_{5,5}` witness can retain all three forum columns unchanged.

The two Guiduli seeds from Erdos--Rosenfeld also verify:

```text
N = [6925500, 37901500, 108448956]
D = [420, 3780, 14940, 76860]
```

```text
N = [2778300, 862552800, 5400442044]
D = [420, 3780, 61695, 154332]
```

## Exact runs completed

### Forum fixed rows

Rows:

```text
[36, 468, 692, 1028]
```

Runs:

```text
runs/20260426_131000_seedext_forum_rows_X1e7
runs/20260426_132000_seedext_forum_rows_X1e8
runs/20260426_134000_seedext_forum_rows_X1e12
```

Result:

```text
column_count = 3
top_extra_deltas = []
witness_count = 0
```

This held unchanged through `X = 10^12`.

### Forum one-row swaps

Runs:

```text
runs/20260426_133000_seedext_forum_rowswap_X1e7_D5e3
runs/20260426_135000_seedext_forum_rowswap_X1e8_D5e3
```

Parameters:

```text
replacement_delta_max = 5000
max_rowsets = 200
```

Result:

```text
witness_count = 0
best rowsets have column_count = 2
```

The best replacements were `1134` and `2443`, usually replacing one of
`36, 468, 692`; they keep two of the seed columns but do not create a serious
near miss.

### Guiduli fixed rows

Runs:

```text
runs/20260426_140000_seedext_guiduli1_rows_X1e12
runs/20260426_141000_seedext_guiduli2_rows_X1e12
```

Result for both Guiduli seeds:

```text
column_count = 3
top_extra_deltas = []
witness_count = 0
```

So the public `K_{4,3}` examples look rigid under strict fixed-row extension,
at least through the current exact bound.

## Interpretation

The easy route is mostly dead:

```text
known K_{4,3} seed -> append one column or one delta nearby
```

The three available `K_{4,3}` seeds do not extend in the naive fixed-row sense,
and bounded one-row mutation around the forum seed does not produce a `K_{4,4}`
or `K_{5,4}` near miss.

The plausible routes left are:

1. Extract Bremner's actual `K_{4,4}` construction/data and test whether it has
   hidden fifth-row/fifth-column structure.
2. Use the elliptic three-row machinery to generate new `K_{4,4}` seeds, then
   test them for fifth rows/columns.
3. Implement the product-lift and divisor-grid tests from
   `algebraic-lifting-notes.md`; these are the best chance of turning existing
   seeds into genuinely new incidence geometry.
4. Add restricted delta mining around the seed-derived delta universe; this is
   broader than row swaps but still much smaller than blind `K_{5,5}` search.

## Current percent estimate

For EP885 as a full all-`k` problem: still low, roughly `10-15%`.

For the first open case `k = 5`: today moved us into roughly `20-25%`
position.  We have:

- verified the known small seeds;
- a reproducible seed-extension runner;
- negative exact evidence for the obvious public-seed extensions;
- a literature risk pass;
- a concrete list of next algebraic/computational tests.

The largest blocker is still Bremner 2019.  The metadata says it proves `k = 4`,
but without the paper's construction or explicit seed data we cannot run the
most natural `K_{4,4} -> K_{5,5}` extension tests.

## Next concrete tasks

1. Obtain Bremner 2019 or enough of its construction to produce one verified
   `K_{4,4}` certificate.
2. Add `product-lift` mode to `scripts/seed_extend.py`.
3. Add `restricted-delta-mine` mode to search a seed-derived delta universe.
4. Add a matrix-invariant script for the divisor-grid/low-rank tests.
5. If no Bremner paper appears, reconstruct `K_{4,4}` independently from the
   elliptic setup, starting with the four three-row subsets of the forum seed.
