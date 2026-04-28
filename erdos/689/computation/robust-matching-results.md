# Robust Prime-Difference Finite Probe

Created: 2026-04-25

This note records a finite computational probe for the "robust prime-difference"
route in the parity-first model for Erdos Problem 689.

The goal here is modest: for manageable `n`, fix a small switched set
`S subset {7,11,13,...}`, choose residues `b_s (mod s)` by random/greedy trials,
compute the exact post-switch residual demand, isolate the main `2^k d q`
family, identify robust cleanup primes `P > n/5`, build pair edges
`x,y in A_S(n)` with `y - x = 2P`, and test the finite pair-and-singleton
inequality. None of the negative outcomes below should be read as an
asymptotic impossibility statement.

## Finite model

Start from the parity-first baseline

```text
a_2 = 1 mod 2,
a_p = 0 mod p for odd primes p <= n.
```

After switching a fixed finite odd-prime set `S` to nonzero residues `b_s mod s`,
the exact residual demand is

```text
r_S(m) = max(0, 2 - C0(m) + L_S(m) - H_S(m)),
```

where

- `C0(m) = 1_{m odd} + omega_odd(m)`,
- `L_S(m) = #{s in S : s | m}`,
- `H_S(m) = #{s in S : m == b_s (mod s)}`.

For the matching experiment I used the exact positive-residual subset inside the
main family

```text
A_S(n) = { 2^k d q <= n :
           k >= 1,
           d is S-smooth,
           q is an odd prime outside S,
           H_S(2^k d q) = 0 }.
```

On this family one has `2 - C0 + L_S = 1`, so `A_S(n)` is an exact
one-token subfamily, not just a heuristic sample. I also record the full exact
token count `sum_{m <= n} r_S(m)` to show how much finite mass still lies
outside the main family.

Define robust primes by

```text
R_S(n) = { P prime : P > n/5, H_S(P) >= 1, H_S(2P) >= 2, H_S(4P) >= 2 }.
```

Only `P <= n/2` can serve as pair labels, since the pair edges are

```text
(x, y, P) with x, y in A_S(n), y - x = 2P.
```

I built the 3-uniform labelled edge set from those triples and then ran a
greedy matching: repeatedly choose an edge through the current lowest-degree
target, with tie-breaks by the other endpoint's degree and then the label
degree. This is a heuristic matching only.

The finite pair-and-singleton check is

```text
|A_S(n)| <= |R_S(n)| + |M|,
```

because a matched label covers two main targets, while every unused robust
label can still be spent on one singleton target. I report the slack

```text
main slack = |R_S(n)| + |M| - |A_S(n)|.
```

For honesty I also record the stronger diagnostic

```text
exact slack = |R_S(n)| + |M| - sum_{m <= n} r_S(m),
```

which is not the intended asymptotic theorem, but measures how far the finite
instance is from closing even before exceptional cleanup.

## Commands

All commands were run from repository root on 2026-04-25 with Python 3.13.

```powershell
python -m py_compile erdos\689\computation\robust_matching_experiment.py
python erdos\689\computation\robust_matching_experiment.py suite --ns 1000,2000,4000 --sieves "7,11,13,17,19" --reference-n 4000 --trials 16 --passes 3 --sample-edges 6
python erdos\689\computation\robust_matching_experiment.py suite --ns 1000,2000,4000 --sieves "7,11,13,17,19,23,29,31,37,41,43,47" --reference-n 4000 --trials 16 --passes 3 --sample-edges 6
```

The residue search optimizes `|R_S(n)| + |M|` first, then penalizes a larger
main family.

## Best searched residue choices

For the two tested sets, the best assignments found at reference scale
`n = 4000` were:

- `S5 = {7,11,13,17,19}` with
  `b = {7:6, 11:6, 13:8, 17:6, 19:10}`.
- `S12 = {7,11,13,17,19,23,29,31,37,41,43,47}` with
  `b = {7:5, 11:1, 13:10, 17:2, 19:9, 23:20, 29:2, 31:10, 37:15, 41:35, 43:16, 47:17}`.

These are only best-found outputs of a finite greedy search, not proven
optimal residue choices.

## Results

### Core counts

| switched set | n | exact tokens | main targets `|A_S(n)|` | robust `|R_S(n)|` | pair labels `<= n/2` | greedy pairs `|M|` | capacity `|R_S|+|M|` | main slack |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `S5` | 1000 | 337 | 165 | 0 | 0 | 0 | 0 | -165 |
| `S5` | 2000 | 577 | 332 | 1 | 0 | 0 | 1 | -331 |
| `S5` | 4000 | 1003 | 648 | 1 | 1 | 1 | 2 | -646 |
| `S12` | 1000 | 378 | 127 | 2 | 0 | 0 | 2 | -125 |
| `S12` | 2000 | 658 | 259 | 10 | 2 | 1 | 11 | -248 |
| `S12` | 4000 | 1159 | 523 | 13 | 10 | 10 | 23 | -500 |

The stronger exact-token slack is also very negative throughout:

- `S5`: `-337`, `-576`, `-1001` at `n = 1000, 2000, 4000`.
- `S12`: `-376`, `-647`, `-1136` at `n = 1000, 2000, 4000`.

### Main-family share and pair graph diagnostics

| switched set | n | main / exact token share | pairable main targets | isolated main targets | labels with at least one pair edge | pair edges |
|---|---:|---:|---:|---:|---:|---:|
| `S5` | 4000 | 0.646 | 66 | 582 | 1 | 33 |
| `S12` | 4000 | 0.451 | 424 | 99 | 10 | 435 |

The larger set `S12` is the more interesting finite probe:

- the pair graph is not empty at all;
- `424 / 523` main targets are incident to at least one pair edge;
- all `10` mid-range robust labels have pair edges;
- the greedy matching finds `10` disjoint labelled pairs, i.e. it saturates the
  available pair-label supply.

So in this finite regime the first bottleneck is not "no pair edges exist";
it is that the number of robust labels is tiny compared with the size of the
main residual family.

### Sample greedy pairs for `S12`, `n = 4000`

The first few labelled pairs found by the greedy matcher were:

```text
(6, 1844; P = 919)
(24, 3578; P = 1777)
(48, 2174; P = 1063)
(84, 2582; P = 1249)
(106, 2352; P = 1123)
(130, 3612; P = 1741)
```

These confirm that the intended `y - x = 2P` structure does appear in quantity
once `S` is large enough, but not nearly in the volume required to close the
main-family count.

## Interpretation

Finite takeaway only:

1. Small fixed `S` is nowhere near enough in these tests. With
   `S = {7,11,13,17,19}`, the best found residue choice produced at most one
   robust prime above `n/5`, and the pair graph was empty below `n = 4000`.

2. A noticeably larger fixed set can create a nontrivial robust/pair structure.
   For the 12-prime set `S12`, the best found assignment at `n = 4000`
   produced `13` robust labels and a reasonably dense pair graph on the main
   family, with a greedy matching of size `10`.

3. Even in that better case, the pair-and-singleton inequality is not close.
   At `n = 4000` the available capacity is only
   `|R_S| + |M| = 13 + 10 = 23`, versus `523` main targets. The slack is
   `-500`.

4. The full exact residual count is still much larger than the main family at
   these scales. For `S12` and `n = 4000`, the main family accounts for only
   about `45%` of the exact residual tokens, so these finite runs are still far
   from an asymptotic regime in which the main-family theorem would dominate.

So the finite evidence here is negative but narrowly so: it does not suggest a
matching obstruction once many robust labels exist; it suggests that, for the
tested small fixed sets, the dominant difficulty is producing enough robust
labels in the first place. I would not promote this to an asymptotic claim
without much larger `S`, better residue optimization, or actual analytic input
for the robust-density question.
