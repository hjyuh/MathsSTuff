# EP-488 v76 A2 Known High-Defect Motifs

Date: 2026-05-18

Status: A2 structural progress. This does not solve A2 or EP-488.

## Purpose

A4 has a successful normalized-ratio workflow. v76 applies the same viewpoint
to the known A2 high-defect evidence: normalize each connected `B_n` component
by `gcd(C)`, but keep the realization parameters

```text
q/s, n/s
```

as exact rationals. This matters because the v56/v59 theta core is a scaled
theta13 `C`, but its `q` is not the same scale multiple of the theta13 `q`.

## Script

```powershell
python .\ep488_v76_a2_known_high_defect_motifs.py
```

Output:

```text
ep488_v76_a2_known_high_defect_motifs.json
```

## Input Sources

The script collects connected components from:

```text
v57 templates: theta13, Kimi, v56 near-miss
v58 q<=500 full-component high-defect census
v59 theta-plus-isolate searches
v60 isolated-extension data through the v59 core
```

It then computes normalized `C`, normalized edge types, cyclomatic number,
`tau`, `epsilon`, and exact finite-certificate status for every connected
high-defect component.

## Results

```text
connected rows inspected = 168
high-defect rows = 168
unique normalized high-defect motifs = 4
status_counts = {'certified': 168}
bad edge-type rows = 0
```

Every connected high-defect component currently in the ledger uses only the
top-window edge-ratio alphabet:

```text
2:3, 3:4, 3:5, 4:5.
```

## Four Normalized Motifs

### 1. theta13 core

```text
C =
{240,243,256,270,288,300,320,324,360,384,405,432,450}
size = 13
occurrences = 5
cyclomatic = 2
tau = 0
epsilon = 2
edge types = 5*(2:3), 5*(3:4), 2*(3:5), 2*(4:5)
```

Realization range seen:

```text
q/s = 451 .. 71440/149
n/s = 1350 .. 213189/149
```

Strongest certified row:

```text
source = template:v56_near_miss
q = 71440
n = 213189
scale = 149
q/s = 71440/149
n/s = 213189/149
B = 74/213189
delta/B = 7105518307/14178553920
best/B = 923819/1786212
```

This is the connected cyclic core behind the v56/v59 isolate examples.

### 2. theta-plus-400 full-component motif

```text
C =
{240,243,256,270,288,300,320,324,360,384,400,405,432,450}
size = 14
occurrences = 145
cyclomatic = 3
tau = 1
epsilon = 2
edge types = 5*(2:3), 6*(3:4), 3*(3:5), 2*(4:5)
```

Realization range seen:

```text
q/s = 451 .. 479
n/s = 1350 .. 1436
```

Strongest certified row:

```text
source = v58_full_component:153
q = 479
n = 1436
B = 39/718
delta/B = 50365187/100877400
best/B = 14719/28431
```

### 3. shifted theta-plus-480 full-component motif

```text
C =
{243,256,270,288,300,320,324,360,384,400,405,432,450,480}
size = 14
occurrences = 8
cyclomatic = 3
tau = 1
epsilon = 2
edge types = 5*(2:3), 6*(3:4), 3*(3:5), 2*(4:5)
```

Realization range seen:

```text
q/s = 481 .. 485
n/s = 1441 .. 1454
```

Strongest certified row:

```text
source = v58_full_component:161
q = 485
n = 1454
B = 39/727
delta/B = 118420303/245138400
best/B = 14540/28431
```

### 4. Kimi obstruction motif

```text
C =
{216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405}
size = 16
occurrences = 10
cyclomatic = 4
tau = 2
epsilon = 2
edge types = 5*(2:3), 7*(3:4), 4*(3:5), 3*(4:5)
```

Realization range seen:

```text
q/s = 427 .. 431
n/s = 1280 .. 1292
```

Strongest certified row:

```text
source = v58_full_component:8
q = 431
n = 1292
B = 47/646
delta/B = 153237337/328163400
best/B = 646/1269
```

## Interpretation

The current ledger's connected A2 high-defect evidence is much smaller after
normalization than it looks in raw `(q,C,n)` form:

```text
168 connected high-defect rows collapse to 4 normalized motifs.
```

This suggests a realistic A2 route parallel to A4:

```text
classify feasible connected epsilon>=2 motifs in the four-ratio graph,
then prove a correction-aware fixed-motif density certificate for each.
```

The key new caution is that A2 motifs must keep exact rational realization
parameters `q/s` and `n/s`. Integer dilation alone is not enough: the v56/v59
theta core has normalized `C = theta13`, but

```text
q/s = 71440/149,
n/s = 213189/149.
```

## What Remains

This does not prove Uniform High-Defect Safety. The missing A2 theorem is now
sharper:

```text
Every feasible connected reduced top-window component with epsilon >= 2 is
either one of the known normalized motifs, a safe extension covered by v60, or
belongs to a classified finite/infinite motif family that admits a fixed-motif
density certificate.
```

The next concrete step is to enumerate connected high-defect induced motifs
directly in the normalized four-ratio graph, rather than by raw q-scanning.

## Closure State

```text
A2: not closed, but known connected high-defect evidence normalized to four
    finite-certified motifs
A4: all normalized pure-cycle motifs through length 18 closed; global A4 open
EP-488: not solved
```
