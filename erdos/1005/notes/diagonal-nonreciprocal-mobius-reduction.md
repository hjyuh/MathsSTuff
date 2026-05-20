# EP1005 non-reciprocal diagonal Mobius reduction

Date: 2026-05-11

This note gives a more promising route for the remaining diagonal
non-reciprocal sector `r>h`: use Mobius inversion on the exact primitive
strip instead of row-by-row divisor discrepancy.

## Setup

Let

```tex
q=ha+r,\qquad r=h+1+c,\qquad c\ge1,\qquad r<a,
```

with

```tex
(a,r)=1,\qquad (a+1,c)=1.
```

At base order `n=q`, the non-reciprocal subcertificate is

```tex
C_0(a,h,r)=
\#\left\{(p,j):
1\le p\le a,\quad
\frac{cp}{a+1}<j<\frac{rp}{a},\quad
(p,j)=1
\right\}.
```

Before coprimality, the strip has exact size

```tex
R_1(a,h,r)=\frac{q+a-1}{2}.
```

This identity is proved in `notes/diagonal-nonreciprocal-agent.md`.

## Mobius inversion

For `d>=1`, let

```tex
R_d(a,h,r)=
\#\left\{(P,J):
1\le P\le \left\lfloor\frac ad\right\rfloor,\quad
\frac{cP}{a+1}<J<\frac{rP}{a}
\right\}.
```

Then

```tex
C_0(a,h,r)=\sum_{d=1}^{a}\mu(d)R_d(a,h,r).
```

The same strip width is

```tex
W=\frac ra-\frac c{a+1}=\frac{q+a}{a(a+1)}.
```

Putting `K_d=floor(a/d)`, the elementary floor bounds give

```tex
\frac W2K_d(K_d+1)-2K_d
\le R_d(a,h,r)\le
\frac W2K_d(K_d+1)+K_d.
```

This converts the primitive-strip problem into an explicit finite Mobius
sum plus a controlled tail.

## Finite-reduction template

For a chosen cutoff `D`, use

```tex
C_0\ge
\sum_{\substack{d\le D\\ \mu(d)=1}} L_d
-
\sum_{\substack{d\le D\\ \mu(d)=-1}} U_d
-
\sum_{d>D} U_d,
```

where

```tex
L_d=\frac W2K_d(K_d+1)-2K_d,\qquad
U_d=\frac W2K_d(K_d+1)+K_d.
```

The main term approaches

```tex
\frac{1}{\zeta(2)}R_1,
```

while the target is about `q/4`. Since

```tex
\frac{1}{\zeta(2)}\cdot\frac{q+a}{2}
>
\frac q4
```

with uniform margin, this should prove all large parameter ranges. The
remaining small range can then be certified by exact enumeration of `C_0`.

## Current evidence

Exact scans of the base strip through `q<=1000` found minimum surplus `4` at

```text
q=107, h=6, a=16, r=11.
```

A direct primitive/raw scan in moderate boxes found the primitive proportion
never close to the target threshold; the worst sampled ratio was about
`0.466`, still far above the ratio needed for `D(q)`.

The reusable exact checker is

```text
powershell -ExecutionPolicy Bypass -File scripts\diagonal_nonreciprocal_base_check.ps1 -QMax 1000 -MaxSurplus 5
```

with output

```text
RECORD q=131 h=4 a=28 r=19 count=41 target=36 surplus=5
RECORD q=107 h=6 a=16 r=11 count=34 target=30 surplus=4
checked=146008
bad=0
records=2
minSurplus=4
minRow=q=107 h=6 a=16 r=11 count=34 target=30 surplus=4
```

The exploratory truncated-Mobius certificate

```text
python scripts\diagonal_nonreciprocal_mobius_cert.py 1000 --cutoff-scale 12 --max-records 10
```

also certifies the whole range `q<=1000`:

```text
checked=146008
certified=146008
failures=0
worst=(4, 107, 6, 16, 11, 16, 34, 30)
```

With cutoff `8 sqrt(a)`, only three thin `h=1` cases near `q=1000` failed
the certificate, and they disappeared at cutoff `12 sqrt(a)`. This suggests
that a proof can use a variable cutoff to balance the Mobius tail.

## Remaining target

Implement the finite Mobius lower-bound checker above. If it forces
`a,h,r` into a bounded box and the exact base-strip certificate passes in
that box, then the base non-reciprocal diagonal case is closed. Slack
`n>q` will still need the expanding-cone analogue.
