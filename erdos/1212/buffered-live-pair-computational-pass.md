# Buffered Live-Pair Computational Pass

Date: 2026-04-27

Script:

```text
scripts/buffered_live_pair_stats.py
```

Result files:

```text
results/buffered-live-pair-stats-N5000.json
results/buffered-live-pair-stats-N50000-theta040-045.json
```

## Statistic Split

The proposed successor definition already includes future clearance, so
`A = A+` if read literally. For computation, the script separates:

```text
raw successors:
  w composite, v < w <= v + H(v),
  gcd(w, product_{t=u}^{v} t) = 1

regenerative successors:
  raw successors with clr(v; w) >= H(w)
```

This makes the bottleneck visible.

## N = 5000

For `theta = 0.40`, the top slab `[4096,8192)` has:

```text
buffered pairs:       552
raw mean:             2.263
raw zero fraction:    0.194
regen mean:           0.049
regen zero fraction:  0.976
longest ray:          4 transitions
```

For `theta = 0.45`, the top slab `[4096,8192)` has:

```text
buffered pairs:       196
raw mean:             3.474
raw zero fraction:    0.163
regen mean:           0.031
regen zero fraction:  0.985
longest ray:          2 transitions
```

## N = 50000

For `theta = 0.40`, the top slab `[32768,65536)` has:

```text
buffered pairs:       23554
raw mean:             4.187
raw zero fraction:    0.054
regen mean:           0.073
regen zero fraction:  0.976
longest ray:          17 transitions
```

For `theta = 0.45`, the top slab `[32768,65536)` has:

```text
buffered pairs:       10364
raw mean:             7.115
raw zero fraction:    0.018
regen mean:           0.033
regen zero fraction:  0.989
longest ray:          5 transitions
```

## Interpretation

The raw live-pair graph is not the bottleneck. Raw successor means increase
with scale and with `theta`; zero-outdegree rates become small for larger
`theta`.

The future-clearance condition is the bottleneck. It requires the current
right coordinate `v` to have no prime divisor creating a multiple in the next
`H(w)` positions. In practice this forces `v` to be rough relative to `H`.
Most buffered pairs are therefore dead after imposing regeneration.

This weakens the "55%" optimism in the current formulation. The next useful
move is not simply larger `N`; it is to refine the state definition so that
rough right coordinates are selected explicitly, or to relax the buffer so it
tracks actual next obstruction distance instead of demanding a full fresh
`H(w)` clearance at every step.

## Next Experimental Variants

1. Condition source pairs by least prime factor of `v`, e.g. `P^-(v) > cH(v)`,
   and recompute regenerative means only inside that selected core.
2. Replace the full future buffer `clr(v; w) >= H(w)` by a variable buffer
   `B(v)` and test whether a smaller deterministic buffer still embeds an
   infinite path.
3. Search directly for rays among rough-right buffered pairs rather than all
   buffered pairs, since the all-pair average is dominated by instantly dead
   right coordinates.
4. Record explicit longest-ray certificates so individual survivor chains can
   be inspected for residue-pattern structure.
