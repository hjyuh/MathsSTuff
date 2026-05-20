# EP-488 v79 A2 Smooth Motif Frontier q10000

Status: A2 structural and computational progress. This does not solve A2,
A4, or EP-488.

## Purpose

v78 made the full-component A2 census exact through `q <= 1500`. v79 extracts
the structural reason those motifs live in a small arithmetic universe, then
uses that structure to push a normalized scale-1 motif frontier through
`q <= 10000`.

## Four-Ratio Lemma

Let

```text
q/2 < a < b < q,
n < 3q,
lcm(a,b) <= n.
```

Write `a = ug`, `b = vg`, where `g = gcd(a,b)` and `gcd(u,v)=1`.
Since `a > q/2`, we have

```text
g > q/(2u).
```

Since `lcm(a,b)=uvg < 3q`, we have

```text
g < 3q/(uv).
```

Combining gives `v < 6`. Also `b/a < 2`, so `v < 2u`. With
`2 <= u < v`, `gcd(u,v)=1`, this leaves exactly:

```text
(u,v) in {(2,3), (3,4), (3,5), (4,5)}.
```

Thus every top-window collision edge has ratio in:

```text
2:3, 3:4, 3:5, 4:5.
```

## 5-Smooth Normalization Lemma

If a connected top-window lcm component has at least one edge, then after
dividing all vertices by their gcd, every normalized vertex is 5-smooth.

Reason: along every edge, the ratio of the two endpoints uses only primes
`2,3,5`. Therefore every prime `p > 5` has the same p-adic valuation at every
vertex in the connected component. The component gcd removes those common
outside-prime factors.

This gives a proof-ready structural reduction:

```text
connected top-window component
  -> four-ratio graph
  -> normalized 5-smooth lattice
```

This part is rigorous and does not rely on sampling.

## New Scripts

The normalized frontier generator:

```text
ep488_v79_a2_smooth_motif_frontier.py
```

It scans integer `q_norm <= q_max`, keeps only 5-smooth vertices in
`(q/2,q)`, checks collision event heights in `[ceil(5q/2),3q)`, and records
components with `epsilon >= 2`.

The representative certificate checker:

```text
ep488_v79_a2_smooth_representative_certs.py
```

It applies the grouped inclusion-exclusion finite-window certificate to one
representative row of every generated normalized motif.

## q1500 Calibration

Command:

```powershell
python .\ep488_v79_a2_smooth_motif_frontier.py --q-max 1500 --json-out ep488_v79_a2_smooth_motif_frontier_q1500.json
```

Comparison with v78 exact full-component q1500:

```text
v78 exact motifs = 14
v79 smooth motifs = 14
motif sets equal = True
q sets equal = True
q_with_rows = 363
bad_edge_type_rows = 0
```

So the scale-1 smooth generator exactly recovers the v78 normalized motif set
through `q <= 1500`.

## q10000 Smooth Frontier

Command:

```powershell
python .\ep488_v79_a2_smooth_motif_frontier.py --q-max 10000 --json-out ep488_v79_a2_smooth_motif_frontier_q10000.json
```

Result:

```text
q_max = 10000
smooth_vertex_count = 175
event_row_count = 14719
unique_normalized_motifs = 120
bad_edge_type_rows = 0
q_with_rows = 7815
elapsed_seconds = 309.83
```

Size distribution:

```text
size 14: 2
size 16: 3
size 17: 2
size 18: 1
size 19: 4
size 20: 4
size 21: 9
size 22: 6
size 23: 6
size 24: 12
size 25: 9
size 26: 22
size 27: 10
size 28: 9
size 29: 13
size 30: 8
```

Epsilon-value set distribution among the 120 motifs:

```text
epsilon values {2}:       90 motifs
epsilon values {2,3}:     16 motifs
epsilon values {3}:        9 motifs
epsilon values {2,3,4}:    2 motifs
epsilon values {2,4}:      2 motifs
epsilon values {4}:        1 motif
```

This is the first frontier where the high-defect full-component model is not
only `epsilon=2`; genuine larger high-defect layers appear.

## Representative Certificates

Command:

```powershell
python .\ep488_v79_a2_smooth_representative_certs.py --input-json ep488_v79_a2_smooth_motif_frontier_q10000.json --max-cutoff 10000000 --json-out ep488_v79_a2_smooth_motif_representative_certs_q10000.json
```

Result:

```text
motifs = 120
status_counts = {'certified': 120}
elapsed_seconds = 3.63
```

No representative motif has `eta <= 0`, a large cutoff, or an EP finite-window
failure.

Strongest representative ratios:

```text
q=1921, n=5760, size=17, epsilon={2}, best/B=765/1504
q=481,  n=1440, size=14, epsilon={2}, best/B=1600/3159
q=961,  n=2880, size=16, epsilon={2}, best/B=50/99
q=1334, n=4000, size=21, epsilon={2}, best/B=7625/15104
q=427,  n=1280, size=16, epsilon={2}, best/B=640/1269
```

All remain far below the EP threshold.

## Exact Unrestricted Spot Checks

The smooth frontier is not automatically the unrestricted full-component
census, because a smooth component might be attached to a non-smooth top-window
vertex. Three exact unrestricted checks were run.

### First new q-range after 1500

Command:

```powershell
python .\ep488_v78_a2_full_component_exact_census.py --q-ranges 1501-1535 --max-cert-size 24 --max-cutoff 10000000 --json-out ep488_v79_a2_exact_check_1501_1535.json
python .\ep488_v77_a2_full_component_q1000_motifs.py --input ep488_v79_a2_exact_check_1501_1535.json --json-out ep488_v79_a2_exact_check_1501_1535_motifs.json
```

Result:

```text
components checked = 1501469
high_defect = 1890
status_counts = {'certified': 1890}
unique normalized motifs = 1
```

The exact unrestricted motif is:

```text
{768,800,810,864,900,960,972,1000,1024,1080,
 1125,1152,1200,1215,1280,1296,1350,1440,1458,1500}
size = 20
epsilon = 2
best/B = 8057/15840
```

This exactly matches the first new smooth-frontier motif.

### First mixed epsilon 2/3 motif

Command:

```powershell
python .\ep488_v78_a2_full_component_exact_census.py --q-ranges 2251 --max-cert-size 24 --max-cutoff 10000000 --json-out ep488_v79_a2_exact_check_q2251.json
python .\ep488_v77_a2_full_component_q1000_motifs.py --input ep488_v79_a2_exact_check_q2251.json --json-out ep488_v79_a2_exact_check_q2251_motifs.json
```

Result:

```text
components checked = 93277
high_defect = 273
status_counts = {'certified': 273}
unique normalized motifs = 1
epsilon values = {2,3}
best/B = 96760/190269
```

### First epsilon up to 4 motif

Command:

```powershell
python .\ep488_v78_a2_full_component_exact_census.py --q-ranges 3751 --max-cert-size 30 --max-cutoff 10000000 --json-out ep488_v79_a2_exact_check_q3751.json
python .\ep488_v77_a2_full_component_q1000_motifs.py --input ep488_v79_a2_exact_check_q3751.json --json-out ep488_v79_a2_exact_check_q3751_motifs.json
```

Result:

```text
components checked = 264138
high_defect = 453
status_counts = {'certified': 453}
unique normalized motifs = 1
epsilon values = {2,3,4}
best/B = 55451/109350
```

The exact unrestricted checks support that the smooth-frontier generator is
seeing real A2 full-component motifs beyond q1500, not merely artifacts of
discarding non-smooth vertices.

## Interpretation

v79 changes the A2 picture in two useful ways.

First, the four-ratio and 5-smooth normalization lemmas are actual structural
lemmas, not numerical evidence. They should be promoted into the A2 proof
framework.

Second, the full-component high-defect family is definitely not a finite small
table. By q10000 the scale-1 smooth frontier already contains 120 normalized
motifs, with sizes up to 30 and epsilon up to 4. The right target is therefore
an infinite 5-smooth/four-ratio theorem, not a finite motif classification.

## Remaining Missing Lemma

The A2 missing lemma should now be stated as:

```text
Uniform 5-smooth high-defect safety.

Let C be a reduced top-window connected component with epsilon_n(C,q) >= 2.
After gcd-normalization, C lies in the 5-smooth four-ratio graph. Prove that
every such normalized component admits a grouped inclusion-exclusion density
gap

    eta = 2D_C(n;q)/n - delta(C,q) > 0

with a finite event-window certificate that is uniform over all scales,
all admissible q,n, and all induced/full-component realizations.
```

The current failure point is the uniform analytic part. v79 proves the
normalization lemma and gives a much larger certified representative frontier,
but it does not prove `eta > 0` for every 5-smooth high-defect component.

## Closure State

```text
A2: not closed.
    New rigorous structural reduction: four-ratio + 5-smooth normalization.
    q10000 scale-1 smooth representatives: 120/120 certified.
    Exact unrestricted spot checks beyond q1500: certified.
    Uniform all-q/all-induced high-defect safety remains open.

A4: not closed.
    Pure-cycle motifs through length 18 remain certified, but no all-length
    theorem yet.

EP-488: not solved.
```
