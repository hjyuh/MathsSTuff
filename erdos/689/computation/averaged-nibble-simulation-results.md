# Averaged-Nibble Finite Simulation

Created: 2026-04-25

This note records a finite, deliberately modest probe of the "averaged nibble"
idea for Erdos Problem 689.

The point is not to produce arithmetic evidence for robust-prime density. The
point is narrower: once one has a finite labelled graph

```text
x in A1, y in A2, P in R, y - x = 2P,
```

with `A1` the `v_2 = 1` targets, `A2` the `v_2 >= 2` targets, and `R` a set of
odd labels in `(n/5, n/2]`, does a simple greedy/nibble-style packing use
almost all active labels when label degrees are already high and the target
sides have slack?

To test that, the new script `averaged_nibble_simulation.py` looks at two kinds
of finite input:

1. frozen "actual" graphs coming from the existing robust-matching finite model;
2. random layered synthetic sets with the same edge rule `y - x = 2P`.

The synthetic rows report saturation against **active labels** only, meaning
labels with at least one edge. The active-label ratio is listed separately.

## Model and heuristics

For each instance the script builds the labelled graph with edges
`(x, y, P)` satisfying `y - x = 2P`.

It then runs two heuristics:

- `greedy`: repeatedly protect the currently smallest available label degree;
- `nibble`: random parallel proposals by labels, discard collisions, then use
  the same greedy cleanup on the leftover graph.

This is still only a finite heuristic experiment. A positive result here says
the packing step looks combinatorially easy on the tested graphs; it does **not**
say the arithmetic input needed to create those graphs is available
asymptotically.

## Commands

Run from repository root:

```powershell
python -m py_compile erdos\689\computation\averaged_nibble_simulation.py
python erdos\689\computation\averaged_nibble_simulation.py suite
```

Observed suite runtime on 2026-04-25: about `24` seconds.

## Actual finite graphs

The first actual row is the residue choice already used in
`robust-matching-results.md`. The second freezes one 14-prime residue choice
found once by an `8`-trial finite search in `robust_matching_experiment.py`,
then only evaluates the resulting graph here; the new script does not rerun
that search.

| case | `|A1|` | `|A2|` | active labels | edges | label degree min / med / mean / max | target slack `(A1/R, A2/R)` | greedy saturation | nibble saturation |
|---|---:|---:|---:|---:|---|---|---:|---:|
| `s12_n4000` | 275 | 248 | 10 | 190 | `4 / 20 / 19.0 / 31` | `27.5, 24.8` | `10/10` | `10/10` |
| `s14_n8000` | 539 | 484 | 15 | 573 | `1 / 39 / 38.2 / 68` | `35.9, 32.3` | `15/15` | `15/15` |

So on the two finite graphs extracted from the robust-hypergraph machinery, the
matching step itself is not showing a bottleneck: both heuristics saturate
every active label.

## Synthetic layered graphs

These are random subsets of the parity layers with the same arithmetic edge
rule `y - x = 2P`. They are not arithmetic models of primes; they are only
combinatorial stress tests for the labelled packing step.

| synthetic case | trials | requested labels | mean active ratio | mean label degree | mean label-degree minimum | target slack `(A1/R, A2/R)` | greedy mean sat | greedy worst sat | nibble mean sat | nibble worst sat |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| `comparable_4000` | 80 | 10 | `0.979` | `21.33` | `4.16` | `27.5, 24.8` | `0.9988` | `0.9000` | `0.9978` | `0.9000` |
| `favorable_40` | 80 | 40 | `1.000` | `47.14` | `29.28` | `13.75, 13.75` | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `favorable_60` | 80 | 60 | `1.000` | `65.74` | `41.36` | `10.83, 10.83` | `1.0000` | `1.0000` | `1.0000` | `1.0000` |

The `comparable_4000` row is the closest synthetic analogue of the actual
`s12_n4000` side sizes. Even there, once a label is active, saturation is
essentially perfect on average. In the deliberately favorable high-degree
regimes, both heuristics saturate every active label in every trial.

## Reading the bottleneck

Finite takeaway only:

1. Once the graph already has many available edges per label and plenty of room
   on both target sides, the labelled matching step looks easy. In these tests
   a very simple greedy matcher already saturates essentially all active labels,
   and the nibble-style routine behaves the same way.

2. The actual finite graphs extracted from the current robust route are
   consistent with that reading: for the tested residue choices, all active
   labels are matched.

3. So these finite experiments do **not** point to a combinatorial obstruction
   in the matching/nibble stage itself. The visible difficulty remains earlier:
   producing enough robust labels, and producing them with the right degree
   profile, from genuine arithmetic data.

4. None of this should be promoted to asymptotic arithmetic evidence. The
   script freezes small finite graphs, and the synthetic cases are only
   geometry-preserving random models of the edge rule.

That is the intended use of this file: a bounded claim that the labelled
packing step looks plausible once the degree/slack hypotheses are already
granted, not a claim that those hypotheses have been proved in the real
problem.
