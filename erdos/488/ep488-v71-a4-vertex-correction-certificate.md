# EP-488 v71 A4 Vertex-Correction Certificate

Date: 2026-05-18

Status: rigorous A4 fixed-motif progress. This does not solve A4 or EP-488.

## Purpose

v70 proved 21 of the 28 normalized pure-cycle motifs through length 12. The
six remaining non-triangle motifs failed only because positive q-excluded
vertex corrections could occur. v71 adds those corrections to the finite
fixed-motif certificate.

## Certificate

Let

```text
P = (p_1,...,p_r)
```

be an ordered normalized pure-cycle motif, with edge lcms

```text
e_i = lcm(p_i,p_{i+1})
```

and let the realization be `sP`. The admissible top-window interval is

```text
lower < q/s < upper,
lower = max(max_i p_i, max_i e_i / 3),
upper = 2 min_i p_i.
```

For a positive vertex correction at `p s`, write

```text
h = q/gcd(ps,q),
r = ps/gcd(ps,q).
```

Then

```text
q/s = hp/r.
```

So every possible positive correction belongs to a finite rational state
`alpha = q/s`. For a fixed `y = floor(n/s)`, v71 lower-bounds the host count by

```text
H_Z#(n) >= raw_H(y) - max_alpha loss_alpha(y),
```

where

```text
raw_H(y) = sum_i floor(y/p_i) - sum_i floor(y/e_i),
loss_alpha(y) = sum_{corrections with q/s=alpha} floor(y/(p_i h_i)).
```

This gives a scale-free lower bound

```text
B0 = min_y 2(raw_H(y) - max_alpha loss_alpha(y))/(y+1),
```

over the finite range

```text
max_i e_i <= y <= ceil(3 upper) - 1.
```

For the `m` side, put `k = floor(m/s)`. Since each cycle edge is q-excluded,

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

The script checks one period of `A(k)` starting at `k = max_i e_i`. If

```text
A(k)/k <= B0
```

on that period and the period slope is at most `B0`, the motif is proved for
every scale and every admissible `q,n,m`.

## Script

```powershell
python .\ep488_v71_a4_vertex_correction_bounds.py --max-length 12 --period-cap 4000000 --json-out ep488_v71_a4_vertex_correction_bounds_len12.json
```

Result:

```text
status_counts = {'proved': 28}
```

Length distribution closed:

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
```

Thus:

```text
All normalized pure-cycle motifs through length 12 are closed by fixed-motif
A4 certificates.
```

## Former v70 Holdouts

The six non-triangle v70 holdouts are now certified:

```text
len 11:
{240,243,256,270,288,320,324,360,384,405,432}
  B0 = 2/45
  slope = 3119/103680
  correction state: q/s = 450

len 12:
{720,729,768,810,864,960,972,1080,1152,1215,1280,1296}
  B0 = 17/1080
  slope = 6643/622080
  correction state: q/s = 1350

{960,972,1024,1080,1152,1215,1280,1296,1440,1536,1620,1728}
  B0 = 7/576
  slope = 10253/1244160
  correction states: q/s = 1800, 3645/2

{1152,1200,1215,1280,1296,1350,1600,1620,1728,1800,1920,2025}
  B0 = 37/3456
  slope = 901/129600
  correction state: q/s = 2250

{1152,1200,1215,1280,1350,1440,1600,1620,1800,1920,2025,2160}
  B0 = 1/96
  slope = 881/129600
  correction state: q/s = 2250

{1200,1215,1280,1296,1350,1440,1600,1620,1800,1920,2025,2160}
  B0 = 1/100
  slope = 3479/518400
  correction state: q/s = 2250
```

The triangle is also certified by this general method:

```text
{12,15,20}
B0 = 2/9
slope = 23/120
correction state: q/s = 45/2
```

The sharper v67 triangle lemma remains useful because it identifies the
`19/27` asymptotic extremal family.

## Margins

The smallest gap between `B0` and the period slope among the 28 motifs is:

```text
B0 - slope = 3683/1555200
```

for the length-10 motif

```text
{1620,1728,1800,1920,2025,2160,2400,2700,2880,3200}.
```

The largest period checked was:

```text
3110400
```

for several length-12 motifs.

## Verification

The checker compiles:

```powershell
python -m py_compile .\ep488_v71_a4_vertex_correction_bounds.py
```

The certificate output is:

```text
ep488_v71_a4_vertex_correction_bounds_len12.json
```

## Closure State

```text
A2: not closed
A4: pure-cycle fixed motifs through normalized length 12 closed; global
    pure-cycle theorem still open
EP-488: not solved
```
