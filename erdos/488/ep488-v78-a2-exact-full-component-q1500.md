# EP-488 v78 A2 Exact Full-Component q1500 Census

Status: partial progress. This is not a proof of A2, A4, or EP-488.

## Purpose

v77 extended the A2 full top-window component census to `q <= 1500`, but it
still inherited the v58 sampling caveat: for `q > 100`, only sampled `n` values
were tested. v78 removes that caveat for the full-component model through
`q <= 1500` by scanning every integer

```text
n in [ceil(5q/2), 3q).
```

This is still not an arbitrary induced-subset census.

## New Script

The exact scanner is:

```text
ep488_v78_a2_full_component_exact_census.py
```

It incrementally maintains the q-excluded lcm graph and triple-fiber counts for
each fixed `q`. Every high-defect row is checked back against the existing v54
`analyze` harness before certification.

Smoke check:

```powershell
python -m py_compile .\ep488_v78_a2_full_component_exact_census.py
python .\ep488_v78_a2_full_component_exact_census.py --q-ranges 427-431 --max-cert-size 24 --max-cutoff 10000000 --json-out ep488_v78_a2_exact_smoke_427_431.json
```

The Kimi range smoke test found 35 exact high-defect rows, all certified.

## Exact q500 Check

Command:

```powershell
python .\ep488_v78_a2_full_component_exact_census.py --q-min 10 --q-max 500 --max-cert-size 24 --max-cutoff 10000000 --json-out ep488_v78_a2_full_component_exact_q500.json
```

Result:

```text
q_count = 491
components checked = 770554
high_defect = 1385
status_counts = {'certified': 1385}
elapsed_seconds = 7.50
```

No hidden high-defect q-ranges appeared below 500. The exact high-defect q-ranges
through 500 are:

```text
(427,431), (451,479), (481,485)
```

## Exact q1500 Check

Command:

```powershell
python .\ep488_v78_a2_full_component_exact_census.py --q-min 10 --q-max 1500 --max-cert-size 24 --max-cutoff 10000000 --json-out ep488_v78_a2_full_component_exact_q1500.json
```

Result:

```text
q_count = 1491
components checked = 20892065
high_defect = 28026
status_counts = {'certified': 28026}
elapsed_seconds = 286.66
```

Every exact high-defect full-component row through `q <= 1500` is certified by
the grouped inclusion-exclusion finite-window theorem. There are no
`eta <= 0`, large-cutoff, or failure rows.

Exact high-defect q-ranges:

```text
(427,431), (451,479), (481,485), (751,767), (854,863),
(901,959), (961,971), (1126,1151), (1216,1279),
(1281,1295), (1334,1349), (1351,1439), (1441,1457)
```

These are exactly the q-ranges seen in the sampled v77 q1500 census. Thus the
v77 sampling did not miss an entire high-defect full-component q-range through
`q <= 1500`.

## Normalization

Command:

```powershell
python .\ep488_v77_a2_full_component_q1000_motifs.py --input ep488_v78_a2_full_component_exact_q1500.json --json-out ep488_v78_a2_full_component_exact_q1500_motifs.json
```

Result:

```text
high_defect rows = 28026
unique normalized full-component motifs = 14
bad edge-type rows = 0
status_counts = {'certified': 28026}
```

Size distribution:

```text
size 14: 2 motifs
size 16: 3 motifs
size 18: 1 motif
size 19: 2 motifs
size 20: 1 motif
size 21: 5 motifs
```

Every normalized edge type is still in:

```text
2:3, 3:4, 3:5, 4:5
```

Every exact q1500 full-component high-defect row has:

```text
epsilon = 2
```

## Comparison To v77

v77 sampled q1500:

```text
components checked = 924545
high_defect = 1412
unique normalized motifs = 14
status_counts = {'certified': 1412}
```

v78 exact q1500:

```text
components checked = 20892065
high_defect = 28026
unique normalized motifs = 14
status_counts = {'certified': 28026}
```

The exact pass increases row coverage by about `19.85x`, but it does not add new
normalized motifs through `q <= 1500`.

## Strongest Full-Component Near-Miss

The strongest exact q1500 full-component row remains the v77 q479 motif:

```text
q = 479
n = 1436
C = {240,243,256,270,288,300,320,324,360,384,400,405,432,450}
size = 14
epsilon = 2
D_C(n) = 39
B = 39/718
best = 41/1458 at m = 1458
best/B = 14719/28431
```

This is harmless; it is still well below the EP bound.

## Required Regression Checks

The v57 finite-certificate checks were rerun.

theta13:

```text
q = 451
n = 1350
epsilon = 2
D_C(n) = 37
B = 37/675
best = 37/1351 at m = 1351
best/B = 675/1351
failures = 0
```

Kimi obstruction:

```text
q = 427
n = 1280
epsilon = 2
D_C(n) = 47
B = 47/640
best = 1/27 at m = 1296
best/B = 640/1269
failures = 0
```

v56 strongest known high-defect near-miss:

```text
q = 71440
n = 213189
epsilon = 2
D_C(n) = 61
B = 122/213189
best = 1033/3411504 at m = 3411504
best/B = 73408079/138734496
failures = 0
```

All three regressions remain certified harmless.

## Interpretation

v78 strengthens the A2 evidence in a specific way:

```text
Full top-window connected components through q <= 1500 are now exact in n,
not sampled, and every epsilon >= 2 row found is finite-certified.
```

The structural picture did not simplify to a tiny finite list. The same 14
motifs persist through q1500, and larger motifs already appear by size 21.
The data still points toward an infinite-family or automaton-style proof rather
than a hand list of sporadic motifs.

## Missing Lemma

The A2 missing lemma is now sharper:

```text
Exact A2 full-component-to-uniform lemma.

For every reduced top-window connected component C with epsilon_n(C,q) >= 2,
possibly after deleting isolated safe extensions, the normalized lcm graph lies
in the four-ratio graph {2:3, 3:4, 3:5, 4:5} and admits a uniform grouped
inclusion-exclusion certificate:

    eta(C,q,n) = 2D_C(n;q)/n - delta(C,q) > 0

with a finite event-window bound sufficient to prove

    D_C(m;q)/m <= 2D_C(n;q)/n

for every m > n.
```

The current failure point is the jump from exact finite evidence and known
induced examples to an all-q, all-induced-component theorem. v78 proves no such
uniform lemma.

## Closure State

```text
A2: not closed.
    Exact full-component q<=1500 branch: all high-defect rows certified.
    Arbitrary induced high-defect components and the infinite motif mechanism
    remain open.

A4: not closed.
    Pure-cycle motifs through length 18 are certified, but the global
    unicyclic host-margin theorem still needs an all-length structural proof.

EP-488: not solved.
```
