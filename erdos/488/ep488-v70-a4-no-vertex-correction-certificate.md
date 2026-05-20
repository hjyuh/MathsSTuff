# EP-488 v70 A4 No-Vertex-Correction Certificate

Date: 2026-05-18

Status: rigorous A4 subcase progress. This does not solve A4 or EP-488.

## Purpose

v67 closed the normalized triangle `{12,15,20}` by hand. v69 closed the first
non-triangle motif `{8,9,10,12,15}`. v70 generalizes that method into an
automatic fixed-motif certificate.

The certificate applies to any normalized pure-cycle motif for which:

1. no q-excluded correction can occur in a positive vertex term throughout the
   top-window realization interval;
2. the raw lower bound for `2H_Z#(n)/n` beats a q-independent upper envelope
   for `N_Z(m)/m`.

## Certificate

Let the ordered normalized cycle be

```text
P = (p_1,...,p_r),
```

with edge lcms

```text
e_i = lcm(p_i,p_{i+1}).
```

For the realization `sP`, the top-window interval is

```text
lower < q/s < upper,
lower = max(max_i p_i, max_i e_i / 3),
upper = 2 min_i p_i.
```

The no-positive-correction test is finite. If a q-excluded correction occurred
in the vertex `ps`, then, with

```text
h = q/gcd(ps,q),
r = ps/gcd(ps,q),
```

we would have

```text
q/s = hp/r,
lower < hp/r < upper,
p h < 3 upper.
```

So it is enough to check the finite set of pairs `(p,h)` and verify that the
open interval

```text
hp/upper < r < hp/lower
```

contains no integer `r`.

When this holds, the `n`-side has the raw lower bound

```text
H_Z#(n) >= min_y [sum_i floor(y/p_i) - sum_i floor(y/e_i)],
```

where

```text
max_i e_i <= y <= ceil(3 upper) - 1.
```

For the `m`-side, put `k = floor(m/s)`. Since each edge is q-excluded,

```text
lcm(e_i s,q) >= 2e_i s.
```

Therefore

```text
N_Z(m) <= A(k),
```

where

```text
A(k) =
  sum_i floor(k/p_i)
 -sum_i floor(k/e_i)
 +sum_i floor(k/(2e_i))
 +floor(k/L_P),
```

and `L_P = lcm(p_1,...,p_r)`.

The script checks one period of `A(k)` beginning at `k = max_i e_i`. If

```text
A(k)/k < lower bound for 2H_Z#(n)/n
```

through that period, the fixed normalized motif is proved for every scale and
every admissible `q,n,m`.

## Script

```powershell
python .\ep488_v70_a4_no_vertex_correction_bounds.py --max-length 12 --period-cap 4000000 --json-out ep488_v70_a4_no_vertex_correction_bounds_len12_cap4m.json
```

The script also produced smaller successful runs:

```text
ep488_v70_a4_no_vertex_correction_bounds_len6.json
ep488_v70_a4_no_vertex_correction_bounds_len8.json
ep488_v70_a4_no_vertex_correction_bounds_len10.json
```

## Results

Through normalized length 10:

```text
status_counts = {'vertex_correction_possible': 1, 'proved': 12}
```

The only unproved motif in that run is the triangle `{12,15,20}`, which is
already closed by v67. Therefore:

```text
A4 pure cycles through normalized length 10 are closed.
```

Through normalized length 12:

```text
status_counts = {'vertex_correction_possible': 7, 'proved': 21}
```

Again one of the seven is the triangle, already closed by v67. Thus:

```text
22 of 28 normalized motifs through length 12 are closed.
```

The six remaining length `<= 12` motifs are precisely the vertex-correction
cases:

```text
len 11:
{240,243,256,270,288,320,324,360,384,405,432}

len 12:
{720,729,768,810,864,960,972,1080,1152,1215,1280,1296}
{960,972,1024,1080,1152,1215,1280,1296,1440,1536,1620,1728}
{1152,1200,1215,1280,1296,1350,1600,1620,1728,1800,1920,2025}
{1152,1200,1215,1280,1350,1440,1600,1620,1800,1920,2025,2160}
{1200,1215,1280,1296,1350,1440,1600,1620,1800,1920,2025,2160}
```

The period-only large cases from the first length-12 run were all resolved by
the `period_cap=4000000` run.

## Examples Closed Automatically

The first non-triangle motif:

```text
{8,9,10,12,15}
B0 = 5/8
slope = 149/360
period = 720
```

The two length-6 motifs:

```text
{24,27,30,36,40,45}
B0 = 17/72
slope = 343/2160
period = 2160

{32,36,40,45,48,60}
B0 = 3/16
slope = 59/480
period = 2880
```

Representative length-8 motif:

```text
{135,144,150,160,180,200,225,240}
B0 = 26/405
slope = 43/1080
period = 43200
```

## What Remains

For pure-cycle A4, the next local target is now exact handling of the six
remaining vertex-correction motifs through length 12. The v70 certificate
already identifies the obstruction type: positive q-excluded vertex terms can
occur, so the raw `H_Z#(n)` lower bound must be replaced by a correction-aware
finite state analysis.

This still does not close A4 globally, because normalized motifs continue
beyond length 12.

## Closure State

```text
A2: not closed
A4: pure cycles through length 10 closed; 22/28 motifs through length 12
    closed; global pure-cycle theorem still open
EP-488: not solved
```
