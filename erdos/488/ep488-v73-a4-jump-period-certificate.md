# EP-488 v73 A4 Jump-Period Certificate

Date: 2026-05-18

Status: rigorous finite normalized-motif A4 progress. This does not solve A4
or EP-488 globally.

## Purpose

v71 proved all normalized pure-cycle motifs through length 12 using a
correction-aware period certificate. Length 13 initially stalled only because
the checker scanned every integer in periods up to about `15.5M`.

v73 replaces the full-period scan by a jump-point scan.

## Jump-Point Lemma

For a fixed normalized motif, v71 gives a scale-free lower bound `B0` for the
right side:

```text
2H_Z#(n)/n >= B0/s.
```

The `m`-side envelope has the form

```text
A(k) =
  sum_i floor(k/p_i)
 -sum_i floor(k/e_i)
 +sum_i floor(k/(2e_i))
 +floor(k/L_P),
```

where `k = floor(m/s)`, `e_i = lcm(p_i,p_{i+1})`, and
`L_P = lcm(p_1,...,p_r)`.

It is enough to prove

```text
A(k)/k <= B0
```

for `k >= max_i e_i`.

Let

```text
M(k) = B0 k - A(k).
```

Between floor jumps, `M(k)` increases. At a negative edge jump, `M(k)` also
increases. Therefore a new minimum can occur only at:

```text
k = max_i e_i,
```

or at a point where the positive floor jumps outnumber the negative floor
jumps. Thus one period can be checked by testing only positive-net jump
points, not every integer.

If the period slope of `A(k)` is at most `B0`, the checked period controls all
later periods.

## Script

```powershell
python .\ep488_v73_a4_jump_period_certificate.py --max-length 13 --json-out ep488_v73_a4_jump_period_certificate_len13.json

python .\ep488_v73_a4_jump_period_certificate.py --max-length 14 --json-out ep488_v73_a4_jump_period_certificate_len14.json

python .\ep488_v73_a4_jump_period_certificate.py --max-length 15 --json-out ep488_v73_a4_jump_period_certificate_len15.json

python .\ep488_v73_a4_jump_period_certificate.py --min-length 16 --max-length 16 --json-out ep488_v73_a4_jump_period_certificate_len16_only.json
```

## Results

The current v63 normalized motif file through length 16 contains:

```text
239 motifs total
```

Length distribution:

```text
3: 1
5: 1
6: 2
7: 2
8: 3
9: 3
10: 1
11: 3
12: 12
13: 23
14: 33
15: 51
16: 104
```

All are certified by v73:

```text
status_counts = {'proved': 239}
```

Run frontiers:

```text
length <= 13: status_counts = {'proved': 51}
length <= 14: status_counts = {'proved': 84}
length <= 15: status_counts = {'proved': 135}
length = 16:  status_counts = {'proved': 104}
```

## Extremal Certificate Stats

Largest period checked:

```text
746496000
```

for the length-16 motif

```text
{3456,3600,3645,3840,3888,4050,4096,4500,
 4608,4800,4860,5120,5184,6075,6144,6750}.
```

Only jump points were checked for that motif:

```text
jump_points_checked = 1794816
```

Smallest gap between `B0` and the period slope:

```text
B0 - slope = 11543/37324800
```

for the length-14 motif

```text
{14400,14580,15360,15552,16200,17280,18225,
 19200,19440,21600,23040,24300,25600,25920}.
```

Correction-state distribution among the 239 motifs:

```text
0 states: 150 motifs
1 state:   73 motifs
2 states:  16 motifs
```

No motif through length 16 has more than two positive vertex-correction states
under the v71 state model.

## What This Closes

This closes the finite normalized pure-cycle census currently represented by

```text
ep488_v63_a4_normalized_cycle_motifs_len16.json
```

as fixed-motif A4 theorems, not merely canonical-realization checks.

It does not close A4 globally, because v63 already showed that normalized
motifs continue appearing as the allowed cycle length grows. The remaining A4
problem is now to prove that the v71/v73 correction-aware certificate works
for every feasible cycle in the infinite ratio graph, or to reduce that graph
to a finite theorem.

## Verification

The checker compiles:

```powershell
python -m py_compile .\ep488_v73_a4_jump_period_certificate.py
```

## Closure State

```text
A2: not closed
A4: all normalized pure-cycle motifs through length 16 closed by fixed-motif
    certificates; global pure-cycle theorem still open
EP-488: not solved
```
