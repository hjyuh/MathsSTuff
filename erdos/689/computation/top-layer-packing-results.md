# Top-layer packing experiment

Created: 2026-04-24

Scope: this note records a standard-library computational experiment for the
directed packing model left open in `../parity-top-layer.md`.

## Model

Fix `n`, let

```text
H_top(n) = {2^k q : n/2 < 2^k q <= n, q <= n/2 an odd prime},
```

and let `P` be a pool of candidate switched primes, usually one or more blocks
at or below `n/4`.

For distinct `p, r in P`, the directed choice

```text
p -> r   meaning   b_p == r (mod p)
```

repairs `r` and covers exactly the top targets `h in H_top(n)` with
`h == r (mod p)`, equivalently `h = r + j p`.

If every switched prime chooses one repair target and every switched prime must
receive repair indegree at least one, then on the selected switched set we get
a permutation / directed cycle cover.  This is the finite model used here.

For a fixed pool `P` the script reports:

- `reachable_targets`: the size of the union of all arc target sets
  `C(p, r)`;
- `max_arc_weight`: the maximum `|C(p, r)|` over ordered pairs `p != r`;
- `assignment raw upper`: the maximum total raw weight
  `sum_p |C(p, f(p))|` over permutations `f`; this is a rigorous upper bound
  for distinct target coverage in this simplified model on that fixed pool.

Searches tried:

- `pair-greedy`: greedy disjoint 2-cycles, mirroring the two-prime gadget;
- `assignment`: maximum raw-weight derangement via Hungarian;
- `assignment-local`: swap local search on top of `assignment`, optimizing
  distinct `H_top` coverage.

## Commands

All commands were run from repository root on 2026-04-24 with Python 3.13.1.

Smoke checks:

```powershell
python -m py_compile erdos\689\computation\top_layer_packing_experiment.py
python erdos\689\computation\top_layer_packing_experiment.py --help
python erdos\689\computation\top_layer_packing_experiment.py run --n 1000 --pool block:4
```

Main sweep:

```powershell
python erdos\689\computation\top_layer_packing_experiment.py sweep --ns 500,1000,2000,5000 --pools "block:4;block:5;block:6;blocks:4,5;blocks:4,5,6;le-n/4" --local-passes 6
```

Here:

- `block:4` means `(n/5, n/4]`;
- `block:5` means `(n/6, n/5]`;
- `block:6` means `(n/7, n/6]`;
- `blocks:4,5` and `blocks:4,5,6` are unions of those neighboring blocks.

## Structural summary near `(n/5,n/4]`

The next table is the main structural takeaway for the near-critical pools.

| n | pool | `|P|` | reachable / `|H_top|` | max arc | assignment raw upper |
|---:|---|---:|---:|---:|---:|
| 500 | `block:4` | 5 | 7 / 52 | 1 | 5 |
| 500 | `block:5` | 2 | 0 / 52 | 0 | 0 |
| 500 | `block:6` | 3 | 7 / 52 | 2 | 4 |
| 500 | `blocks:4,5` | 7 | 13 / 52 | 1 | 7 |
| 500 | `blocks:4,5,6` | 10 | 36 / 52 | 2 | 12 |
| 1000 | `block:4` | 7 | 17 / 94 | 1 | 7 |
| 1000 | `block:5` | 8 | 20 / 94 | 1 | 8 |
| 1000 | `block:6` | 4 | 9 / 94 | 1 | 4 |
| 1000 | `blocks:4,5` | 15 | 50 / 94 | 1 | 15 |
| 1000 | `blocks:4,5,6` | 19 | 72 / 94 | 2 | 24 |
| 2000 | `block:4` | 17 | 54 / 167 | 1 | 17 |
| 2000 | `block:5` | 11 | 25 / 167 | 1 | 11 |
| 2000 | `block:6` | 6 | 25 / 167 | 2 | 11 |
| 2000 | `blocks:4,5` | 28 | 93 / 167 | 1 | 28 |
| 2000 | `blocks:4,5,6` | 34 | 132 / 167 | 2 | 41 |
| 5000 | `block:4` | 36 | 128 / 366 | 1 | 36 |
| 5000 | `block:5` | 23 | 78 / 366 | 1 | 23 |
| 5000 | `block:6` | 18 | 129 / 366 | 2 | 31 |
| 5000 | `blocks:4,5` | 59 | 225 / 366 | 1 | 59 |
| 5000 | `blocks:4,5,6` | 77 | 304 / 366 | 2 | 96 |

Two patterns are stable in every tested row:

1. `block:4` and `blocks:4,5` never produce an arc covering more than one top
   target.  In this model they are effectively one-top-target-per-switched-prime
   reservoirs.
2. Adding `block:6` is the first place where weight-2 arcs appear, but even
   then the raw permutation upper bound stays far below `|H_top|`.

## Search results near `(n/5,n/4]`

Covered targets after each search:

| n | pool | pair-greedy | assignment | assignment-local |
|---:|---|---:|---:|---:|
| 500 | `block:4` | 4 | 5 | 5 |
| 500 | `block:5` | 0 | 0 | 0 |
| 500 | `block:6` | 3 | 4 | 4 |
| 500 | `blocks:4,5` | 6 | 6 | 7 |
| 500 | `blocks:4,5,6` | 11 | 9 | 12 |
| 1000 | `block:4` | 5 | 7 | 7 |
| 1000 | `block:5` | 7 | 6 | 8 |
| 1000 | `block:6` | 3 | 4 | 4 |
| 1000 | `blocks:4,5` | 13 | 13 | 15 |
| 1000 | `blocks:4,5,6` | 22 | 22 | 23 |
| 2000 | `block:4` | 13 | 14 | 17 |
| 2000 | `block:5` | 8 | 10 | 10 |
| 2000 | `block:6` | 9 | 11 | 11 |
| 2000 | `blocks:4,5` | 23 | 26 | 28 |
| 2000 | `blocks:4,5,6` | 37 | 37 | 41 |
| 5000 | `block:4` | 34 | 29 | 36 |
| 5000 | `block:5` | 20 | 21 | 23 |
| 5000 | `block:6` | 26 | 25 | 30 |
| 5000 | `blocks:4,5` | 56 | 52 | 59 |
| 5000 | `blocks:4,5,6` | 86 | 83 | 92 |

Observations:

- `assignment-local` is usually the best of the three searches on these medium
  pools, but only by a few targets.
- For `block:4` and `blocks:4,5`, local search hits the raw assignment upper
  exactly in every tested row.  So on those fixed pools the simplified model is
  solved optimally by the experiment, and the optimum is still tiny.
- For `blocks:4,5,6`, local search is also close to the upper bound:
  `12/12`, `23/24`, `41/41`, `92/96`.

This is stronger than a heuristic failure.  For example, at `n = 5000`,
`blocks:4,5,6` can reach `304` of the `366` top targets in union, but any
permutation of that pool has raw capacity at most `96`, and local search gets
to `92`.  The bottleneck is the one-residue-per-prime packing constraint, not
mere reachability.

## Comparison with the full `p <= n/4` pool

Allowing all odd primes up to `n/4` changes the picture completely.

| n | `|P|` | `|H_top|` | pair-greedy cover / selected primes | assignment-local cover |
|---:|---:|---:|---|---:|
| 500 | 29 | 52 | `52 / 22` | 52 |
| 1000 | 52 | 94 | `94 / 26` | 94 |
| 2000 | 94 | 167 | `167 / 36` | 167 |
| 5000 | 203 | 366 | `366 / 64` | 366 |

Further details:

- `reachable_targets = |H_top|` in every tested `le-n/4` row;
- `max_arc_weight` is already large: `26, 48, 83, 184`;
- the raw assignment upper is huge: `116, 232, 449, 1060`.

So the simplified top-layer-plus-repair problem is not hard once genuinely
small primes are admitted.  The difficult regime is exactly the near-critical
window around `(n/5,n/4]` and a few neighboring blocks below it.

## Interpretation

Current computational takeaway:

1. The first-capacity-open block `(n/5,n/4]` is still far too sparse in the
   directed packing model.  Up through `n = 5000`, every ordered arc inside
   `block:4` covers at most one `H_top` target, and the whole pool covers at
   most one top target per switched prime.
2. The immediate lower neighbor `(n/6,n/5]` does not qualitatively change the
   situation.  The union `blocks:4,5` still has `max_arc_weight = 1` in every
   tested row, so its full-pool optimum is just `|P|`.
3. Going down to `(n/7,n/6]` finally creates a few two-target arcs, but the
   best observed / bounded covers are still only about a quarter of `H_top` by
   `n = 5000`:

   ```text
   blocks:4,5,6 at n = 5000: best 92, raw upper 96, |H_top| = 366.
   ```

4. Once much smaller primes are allowed, the simplified model becomes easy:
   even the 2-cycle greedy search covers all of `H_top` for `p <= n/4`.

So the new obstruction suggested by these experiments is not just coarse
capacity.  In the near-critical medium blocks, the directed graph is too thin:
each residue choice `p -> r` produces too few top targets, and the permutation
constraint prevents the large reachability union from being packed efficiently.

This does **not** rule out the full parity-first program.  The experiment
ignores lower-layer obligations, prime powers, and any help from primes outside
the tested pool.  But it does say that a proof based only on `(n/5,n/4]` or on
the first two or three neighboring blocks below `n/4` is very unlikely to work
through this simple directed-packing mechanism alone.
