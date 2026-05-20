# EP-488 v57 Full-Solution Attempt

Date: 2026-05-18

Status: partial progress, not a proof and not a counterexample.

## Goal

Solve EP-488, or produce an exact counterexample, or close both remaining reduced
top-window branches:

- A2: high-defect cyclic components.
- A4: unicyclic host-margin/event-point components.

This attempt does not close either branch. It preserves the current strongest
checks as a rerunnable verifier in `ep488_v57_checks.py`.

## Commands

Run from this directory:

```powershell
python .\ep488_v57_checks.py
```

The verifier completed successfully on 2026-05-18.

## A2 high-defect certificates checked

The finite-certificate theorem says that for fixed `(q,C,n)`,

```text
D_C(m;q)/m <= delta + E/m,
B = 2D_C(n;q)/n,
eta = B - delta.
```

When `eta > 0`, only `n < m <= floor(E/eta)` must be checked.

### theta13

```text
q = 451
n = 1350
C = {240,243,256,270,288,300,320,324,360,384,405,432,450}
epsilon = 2
D_C(n) = 37
B = 37/675
delta = 35/1353
delta/B = 7875/16687
E = 78
cutoff = 2694
best = 37/1351 at m = 1351, D_C(m) = 37
best/B = 675/1351
failures = 0
```

theta13 remains harmless for the EP bound, while still killing unconditional
A2'/stripped-pseudoforest claims.

### Kimi obstruction

```text
q = 427
n = 1280
C = {216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405}
epsilon = 2
D_C(n) = 47
B = 47/640
delta = 783343/23058000
delta/B = 6266744/13546575
E = 106
cutoff = 2685
best = 1/27 at m = 1296, D_C(m) = 48
best/B = 640/1269
failures = 0
```

The Kimi obstruction remains harmless for the EP bound, while still refuting
broad triple-stripping.

### v56 strongest high-defect near-miss

```text
q = 71440
n = 213189
C = {35760,36207,36269,38144,38296,40230,42912,43640,44700,
     46678,47680,48276,53640,57216,60345,63116,64368,67050,68055}
epsilon = 2
D_C(n) = 61
B = 122/213189
delta = 247527163896052833247853914829/818631113780204727506401615314480
delta/B = 17590022847945202489092242749493227/33290998627061658918593665689455520
E = 1934
cutoff = 7165749
best = 1033/3411504 at m = 3411504, D_C(m) = 1033
best/B = 73408079/138734496
failures = 0
```

This remains the strongest checked high-defect near-miss, with best ratio about
0.529126 of the EP bound.

## A4 host-margin check

The verifier also checks induced connected unicyclic top-window hosts for
`q <= 45`, host size `<= 8`, at generated event points.

Result:

```text
ok = True
checked = 348
worst margin = 498
example worst host = (12,15,20), cycle LCM = 60
```

This is evidence only. It is not a proof of the A4 event-point host-margin
inequality.

## Dead routes avoided

- Broad triple-stripping.
- Unconditional stripped-pseudoforest A2'.
- v52 run-count equality.
- Hunter density bridge `D(m)/m <= W_T`.
- Undefined `x_1/x_3` degree-count formulations.

## Exact missing lemmas

### Missing A2 lemma

Uniform High-Defect Safety:

For every reduced top-window connected component `(q,C,n)` with
`epsilon_n(C,q) >= 2`,

```text
D_C(m;q)/m <= 2D_C(n;q)/n
```

for every `m > n`.

The current finite-certificate theorem proves this for fixed checked templates
when `eta = 2D_C(n;q)/n - delta > 0` and the finite window is exhausted. What is
missing is a structural or analytic proof that every high-defect component has
positive margin and no event-point violation, or a complete motif
classification reducing all high-defect components to certified templates.

### Missing A4 lemma

Unicyclic Host-Margin Event-Point Lemma:

For every reduced top-window connected unicyclic host `U` and every relevant
event point `m`,

```text
2m H_U#(n) - n H_U#(m) >= n c_m(L_cyc).
```

The current bounded search found no counterexample, but the full proof still
needs a formal event-point reduction and an all-host argument.

## Closure state

- A2: not closed.
- A4: not closed.
- Original `F_Q` statement: not closed.

The defensible percentage remains the v53/v55 anchor: about 87%, provisional.
The v57 checks increase confidence in the finite-certificate route but do not
justify claiming a higher solved percentage without a new theorem.
