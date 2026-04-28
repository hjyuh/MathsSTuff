# Smooth border and Hensel-lift summary

Date: 2026-04-26.

Scripts:

```text
scripts/border_surface_modp.py
scripts/border_hensel_lift.py
```

## Smooth finite-field border points

For each mod-\(p\) border point, the scanner now constructs the full Jacobian
of the equations

\[
U_i^2-X^2-N_i=0,\qquad
V_j^2-M-x_j^2=0,\qquad
W^2-M-X^2=0.
\]

The variables are

\[
X,M,U_1,\ldots,U_4,V_1,\ldots,V_4,W.
\]

Smooth means Jacobian rank \(9\), the number of equations.

High-yield Bremner seeds through primes \(p\le151\):

```text
5Q+T     smooth_primes=16/33 nontrivial= 1226 smooth_nontrivial= 1214 best=p83:760
6Q       smooth_primes=20/33 nontrivial= 2064 smooth_nontrivial= 2020 best=p109:632
8Q+T     smooth_primes=21/33 nontrivial= 1380 smooth_nontrivial= 1378 best=p53:312
```

Interpretation: the modular border points are overwhelmingly smooth in the
best cases.  They are Hensel-usable local points, not singular artifacts.

## First Hensel lift

Seed:

```text
5Q+T
p=83
X=1
M=3
precision exponent=8
```

Output:

```text
results/border_hensel_5QplusT_p83_X1_M3_e8.json
```

The lift modulus is

\[
83^8=2252292232139041.
\]

All lifted square-root checks are zero modulo \(83^8\).

## What this proves and does not prove

This proves the simultaneous border surface has explicit smooth \(p\)-adic
local points at the tested seeds.  It does not prove rational points.

The next step is rational reconstruction or a structured symbolic projection
from one of these local points.  The best practical target is:

```text
5Q+T, p=83, X=1, M=3
```

because it has many smooth nontrivial residues and a successful Hensel lift.
