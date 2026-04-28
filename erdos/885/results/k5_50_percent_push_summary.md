# EP885 k=5 push toward 50%

Date: 2026-04-26.

## Main correction

The simultaneous border surface is useful, but it does not bypass the
one-sided fifth-column obstruction for a fixed \(K_{4,4}\) seed.

For fixed rows \(N_1,\ldots,N_4\), any \(K_{5,5}\) extension containing that
seed must have a nontrivial rational \(X\) satisfying

\[
U_i^2=X^2+N_i,\qquad i=1,\ldots,4.
\]

So the true fixed-seed blocker is still this high-genus fifth-column curve.

## Work added

New files:

```text
notes/border-projection-caveat.md
scripts/elliptic_factor_export.py
scripts/fifth_column_param_search.py
results/elliptic_factors/
results/fifth_column_param/
```

## Elliptic-factor exports

For the quotient

\[
C:\quad y_i^2=t+N_i,\qquad i=1,\ldots,4,
\]

the Jacobian decomposes into elliptic factors attached to

\[
z^2=\prod_{i\in I}(t+N_i),\qquad |I|=3,4.
\]

Generated Sage scripts for:

```text
3Q+T
5Q+T
6Q
8Q+T
```

The scripts include:

- the cubic/quartic factor models;
- known old-column affine points on each factor;
- Sage commands for elliptic conversion, rank bounds, and torsion.

No local Sage/Magma executable is available in this environment, so these are
ready-to-run exports rather than completed rank computations.

## Direct rational fifth-column search

For fixed rows, parameterize the first conic by

\[
X=\frac{s^2-N_0t^2}{2st}.
\]

Then test the other three equations exactly.

Search bound:

```text
1 <= s,t <= 300
```

Seeds tested:

```text
3Q+T, 5Q+T, 6Q, 8Q+T
```

Result:

```text
no hits;
no two-row passes beyond the anchor row.
```

This is not evidence of nonexistence, but it says any fixed-seed fifth column
is not a tiny-height conic-parameter accident.

## Current assessment

Isolated \(k=5\) is not at 50% yet.

The honest status after this push:

```text
isolated K5,5: 30-35%
full EP885:    15-20%
```

To reach 50% for isolated \(k=5\), we need one of:

1. Sage/Magma shows extra rank or compatible new rational points on the
   elliptic factors for a Bremner seed.
2. A new \(K_{4,4}\) seed/family is constructed with a deliberately positive
   rank fifth-column quotient.
3. A direct \(K_{5,5}\) construction appears from the high-rank three-column
   or finite-field/rational-reconstruction route.

The next most valuable task is to run the generated Sage files in
`results/elliptic_factors/`.

## Update: modular CRT fifth-column search

Added `scripts/fifth_column_crt_search.py`, implementing the direct modular
\(X\)-search:

\[
T_p=\{x\in\mathbb F_p:x^2+N_i\text{ is square for all }i\}.
\]

It combines small \(T_p\)'s by CRT, rationally reconstructs \(X=a/b\), and
checks exactly whether all \(a^2+N_i b^2\) are squares.

First run:

```text
prime_bound = 200
height_bound = 1000
```

Seeds tested:

```text
3Q+T, 5Q+T, 6Q, 8Q+T
```

Result:

```text
no fifth-column hits up to height 1000.
```

This reinforces the conclusion that fixed Bremner seeds are not extending by
low-height accident.  It does not rule out high-height points.

## Update: forum K3,5 packet extension

Added `scripts/extra_shift_from_columns.py`.

For the forum packet

\[
z=\{330,870,2445,4155,10482\},
\qquad
N=\{756000,15971200,45130176\},
\]

we searched for additional positive shifts \(N'\) such that

\[
z_i^2+N'\in\square
\]

for all five \(z_i\).  The CRT-filtered exact search reached

```text
m <= 10^12
```

where \(N'=m^2-330^2\).  It found exactly the three known shifts and no new
one.

We also tested the guidepost and two primitive four-secant triples from the
Lean addendum to \(m\le10^8\); again no new shifts appeared.

This means the forum \(K_{3,5}\) packet is not an immediate \(K_{5,5}\) route.
