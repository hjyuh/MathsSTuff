# Diagonal non-reciprocal `c=1` shifted-block draft

Date: 2026-05-12

This note isolates the `c=1` non-reciprocal diagonal branch.  It is a
proof skeleton, not a completed proof of Erdos Problem 1005.  The capped-core
range and the first large-slack gate are now essentially proof-ready after an
explicit finite check.  The remaining gap is an analytic all-`h`, all-`k`
proof for the later shifted-block increments; the current exact rational
certificate covers only the checked box.

## Setup

In the `c=1` branch write

```tex
r=h+2,\qquad A=a+1,\qquad q=ha+r=hA+2,
```

with

```tex
a>h+2,\qquad (a,h+2)=1,\qquad q\ge 92.
```

Let

```tex
D(n)=\left\lfloor {n\over4}\right\rfloor+\delta_{n\bmod4},
\qquad
(\delta_0,\delta_1,\delta_2,\delta_3)=(1,2,2,4).
```

For `n=q+\sigma`, the denominator-row cone count decomposes as

```tex
B_{q+\sigma}(a,q)=C_0(a,h)+G_\sigma(a,h),
```

where the base strip is

```tex
C_0=
\#\left\{(p,j):1\le p\le a,\quad
{p\over A}<j<{(h+2)p\over a},\quad (p,j)=1\right\},
```

and the slack cone is

```tex
G_\sigma=
\#\left\{(u,j):u\ge1,\quad
{a+u\over A}<j<{(h+2)(a+u)\over a},\quad
0\le hu+j-(h+2)\le\sigma,\quad (a+u,j)=1\right\}.
```

The target is

```tex
B_{q+\sigma}(a,q)\ge D(q+\sigma)
```

for every `\sigma\ge0` in this branch.

## Primitive interval lower bound

The elementary discrepancy input used throughout is:

```tex
\#\{x\in I:(x,m)=1\}\ge |I|{\phi(m)\over m}-\tau(m)
```

for any interval `I` of consecutive integers.  This follows by inclusion over
the divisors of `m`: each residue class count differs from its average by at
most one, and there are `\tau(m)` divisors.

With `H=h+2`, define

```tex
A_h=\sum_{j=2}^{H}{\phi(j)\over j},\qquad
E_h=\sum_{j=2}^{H}\tau(j),
```

and

```tex
M_h={1\over H}\sum_{j=1}^{H-1}{(H-j)\phi(j)\over j},
\qquad
T_h=\sum_{j=1}^{H-1}\tau(j).
```

Applying the interval bound row-by-row gives the base estimate

```tex
C_0(a,h)\ge aM_h-T_h.                         \tag{1}
```

The same bound gives, for the capped core rectangle

```tex
1\le u\le U,\qquad 2\le j\le H,
\qquad U=\min\left(a,\left\lfloor{\sigma\over h}\right\rfloor\right),
```

the slack lower bound

```tex
G_\sigma\ge U A_h-E_h.                         \tag{2}
```

This rectangle lies in the cone for `0\le\sigma<h(a+2)`.  The exact
capped-core finite reduction recorded in
`notes/diagonal-nonreciprocal-cone-obstruction.md` and checked by
`scripts/diagonal_nonreciprocal_c1_check.py` has no failures in the tested
finite reduction, with minimum combined margin `7` at

```tex
(q,h,a,\sigma)=(98,6,15,5).
```

Thus the current large-slack proof only has to begin at

```tex
\sigma\ge h(a+2)=hA+h.
```

## Shifted blocks

For `k\ge0`, set

```tex
Q_k=
\left\{(u,j):
kA+1\le u\le (k+1)A,\quad
k+2\le j\le (k+1)H
\right\}.
```

Every point of `Q_k` lies in the intrinsic slack cone.  The whole block is
available once

```tex
\Lambda_k=(k+1)hA+kH.                          \tag{3}
```

Indeed, the top-right corner has slack

```tex
h(k+1)A+(k+1)H-H=(k+1)hA+kH.
```

Between two consecutive gates, monotonicity reduces the proof to the right
endpoint.  Put

```tex
n_k=q+\Lambda_k-1=h(k+2)A+kH+1.
```

The first large-slack interval, after `Q_0` has appeared and before `Q_1`
appears, is certified by

```tex
C_0+\#Q_0^{\rm prim}\ge D(n_1)
=D(3hA+h+3).                                  \tag{4}
```

For every later step it is enough to prove

```tex
\#Q_k^{\rm prim}\ge D(n_{k+1})-D(n_k)
\qquad(k\ge1).                                \tag{5}
```

Here `#Q_k^{prim}` counts pairs in `Q_k` with `(a+u,j)=1`.

## First large-slack gate

The row-wise lower bound gives

```tex
C_0+\#Q_0^{\rm prim}
\ge aM_h-T_h+A A_h-E_h.
```

So the analytic first-gate inequality is

```tex
aM_h-T_h+A A_h-E_h\ge D(3hA+h+3).             \tag{6}
```

The exact rational checker

```text
python scripts/diagonal_nonreciprocal_c1_first_gap.py 300 --max-a-extra 1000
```

uses

```tex
\operatorname{margin}(h,a+4)-\operatorname{margin}(h,a)
=4(M_h+A_h)-3h.
```

In the rerun for this note:

```text
h_checked=300
bad=398
best=(Fraction(-283046653, 4849845), 20, 23)
nonpositive_step=0
last_bad=(44, 47, Fraction(-83805514698775, 10593329013498))
```

Thus the lower bound (6) fails only inside the explicit analytic box

```tex
h\le44,\qquad a\le47.                          \tag{7}
```

This box is not a proof failure.  It only means that the crude discrepancy
lower bound is too weak there.

For large `h`, (6) follows from elementary summatory estimates.  Let
`\kappa=6/\pi^2`.  Since

```tex
{\phi(n)\over n}=\sum_{d\mid n}{\mu(d)\over d},
```

we have

```tex
\sum_{n\le N}{\phi(n)\over n}
\ge \kappa N-\log N-2.                        \tag{8}
```

Also

```tex
\sum_{n\le N}\tau(n)\le N(1+\log N).
```

Consequently

```tex
A_h\ge \kappa H-\log H-3,\qquad
M_h\ge {\kappa(H-1)\over2}-\log H-2,
```

and

```tex
T_h+E_h\le2H(1+\log H),\qquad
M_h\le {H-1\over2},\qquad
D(N)\le {N\over4}+4.
```

Since `A\ge h+4`, the first-gate margin is bounded below by

```tex
(h+4)\left(
{\kappa(H-1)\over2}+\kappa H-2\log H-5-{3h\over4}
\right)
-{H-1\over2}-2H(1+\log H)-{h\over4}-{19\over4}.
```

This expression is positive for `h\ge165`.  The exact rational check covers
`h\le300`, so (6) is proved outside (7).  Inside (7), the largest possible
`q` is

```tex
q=h(a+1)+2\le44\cdot48+2=2114.
```

The exact shifted-block checker

```text
python scripts/diagonal_nonreciprocal_c1_shifted_reduction.py 10000 --k-max 20
```

directly checks the admissible cases in this finite box and reports

```text
rows_checked=569960
first_bad=0
first_best=(25, 98, 8, 11, 299, 103, 78)
```

Therefore the first large-slack gate is closed, with exact minimum margin
`25` in the checked admissible box.

## Later shifted-block increments

For `k\ge1`, the `j`-wise discrepancy lower bound for `Q_k` is

```tex
L_j(h,k,A)
=A\sum_{j=k+2}^{(k+1)H}{\phi(j)\over j}
-\sum_{j=k+2}^{(k+1)H}\tau(j).
```

The dual `p`-wise lower bound on the same block uses

```tex
(k+1)A\le p\le(k+2)A-1,\qquad
k+2\le j\le(k+1)H,
```

and is

```tex
L_p(h,k,A)
=
\bigl((k+1)H-(k+2)+1\bigr)
\sum_{p=(k+1)A}^{(k+2)A-1}{\phi(p)\over p}
-\sum_{p=(k+1)A}^{(k+2)A-1}\tau(p).
```

The exact rational increment checker certifies (5) whenever

```tex
\max(L_j(h,k,A),L_p(h,k,A))\ge D(n_{k+1})-D(n_k).
```

The rerun

```text
python scripts/diagonal_nonreciprocal_c1_increment.py 300 --k-max 100 --max-a-extra 1000
```

reports

```text
h_checked=300
k_checked=100
bad=0
best=(Fraction(3728434771, 76491415), 8, 12, 1)
nonpositive_step=0
```

For every checked `(h,k)`, the `j`-wise margin has positive four-step drift
in `A`,

```tex
\operatorname{margin}_j(h,k,A+4)-\operatorname{margin}_j(h,k,A)
=4\sum_{j=k+2}^{(k+1)H}{\phi(j)\over j}-h>0,
```

so the finite `A` scan proves all larger `A` for those checked `(h,k)`.
The worst certified row is `(h,A,k)=(8,12,1)`, with margin
`3728434771/76491415>48`.

## Current status and remaining gaps

The `c=1` branch is sharpened to the following gate proof.

1. The capped-core range

```tex
0\le\sigma<h(a+2)
```

is covered by the base estimate plus the capped rectangle, with exact finite
checking already recorded.

2. The first large-slack gate

```tex
h(a+2)\le\sigma<\Lambda_1
```

is closed.  The analytic discrepancy proof works outside
`h\le44, a\le47`, and the remaining finite box is directly checked by exact
primitive counts.

3. The later shifted-block induction is verified exactly, with rational
arithmetic, for

```tex
h\le300,\qquad 1\le k\le100,
```

and for all admissible `A=a+1` in those rows.

The remaining proof obligation is therefore:

```tex
\max(L_j(h,k,A),L_p(h,k,A))
\ge D(n_{k+1})-D(n_k)
```

for every admissible

```tex
h>300\quad\text{or}\quad k>100.
```

The existing summatory-totient estimate (8) should be strong enough to prove
this for large `h` and large `k`, because the main terms have size roughly
`A k h` while the target increment is only about `hA/4`.  However that
large-parameter inequality has not yet been written and checked.  Until it
is supplied, the `c=1` shifted-block branch should be described as
substantially reduced, not proof-ready.

## Faster increment checker

The original exact rational increment checker evaluates both the `j`-wise
and dual `p`-wise lower bounds for every `A`.  A faster equivalent bad-case
checker is now available:

```text
scripts/diagonal_nonreciprocal_c1_increment_fast.py
```

It computes the dual `p`-wise bound only when the `j`-wise margin is
negative.  This is enough for certification, because a nonnegative `j`-wise
margin already proves the row.  It also reports whether every `(h,k)` row is
closed by the positive four-step drift in `A`; the line
`unclosed_pairs=0` is the check that the scan proves all larger `A` in the
specified `(h,k)` box.

Verification against the old box:

```text
python scripts\diagonal_nonreciprocal_c1_increment_fast.py 300 --k-max 100 --max-a-extra 1000 --max-records 5
checked=78247
p_evaluated=1810
certified_by_j=78240
certified_by_p=7
bad=0
closed_pairs=30000
unclosed_pairs=0
p_pair_ranges
7: h=8 A=12 k_min=94 k_max=100
```

Two additional exact slices:

```text
python scripts\diagonal_nonreciprocal_c1_increment_fast.py 400 --h-min 301 --k-max 100 --max-a-extra 500
checked=26600
p_evaluated=0
certified_by_j=26600
bad=0
closed_pairs=10000
unclosed_pairs=0
```

```text
python scripts\diagonal_nonreciprocal_c1_increment_fast.py 300 --k-min 101 --k-max 160 --max-a-extra 500 --max-records 5
checked=47029
p_evaluated=1867
certified_by_j=46969
certified_by_p=60
bad=0
closed_pairs=18000
unclosed_pairs=0
p_pair_ranges
60: h=8 A=12 k_min=101 k_max=160
```

And a wider diagnostic with a smaller `A` window:

```text
python scripts\diagonal_nonreciprocal_c1_increment_fast.py 800 --h-min 401 --k-max 100 --max-a-extra 300
checked=106700
p_evaluated=0
bad=0
closed_pairs=40000
unclosed_pairs=0
```

```text
python scripts\diagonal_nonreciprocal_c1_increment_fast.py 300 --k-min 161 --k-max 260 --max-a-extra 300
checked=78569
p_evaluated=3817
certified_by_p=199
bad=0
closed_pairs=30000
unclosed_pairs=0
p_pair_ranges
100: h=8 A=12 k_min=161 k_max=260
99: h=9 A=13 k_min=162 k_max=260
```

The emerging pattern is useful: for large `h`, the `j`-wise bound alone
certifies the checked rows; for larger `k` at small `h`, the only displayed
dual-bound families are the minimal-width rows `(h,A)=(8,12)` and then
`(9,13)`.  This suggests the eventual all-`k` proof should split into a
general `j`-wise large-`h` estimate and a small-`h`, minimal-`A` dual
estimate.

## Commands rerun for this draft

```text
python scripts/diagonal_nonreciprocal_c1_first_gap.py 300 --max-a-extra 1000
python scripts/diagonal_nonreciprocal_c1_increment.py 300 --k-max 100 --max-a-extra 1000
python scripts/diagonal_nonreciprocal_c1_shifted_reduction.py 10000 --k-max 20
```
