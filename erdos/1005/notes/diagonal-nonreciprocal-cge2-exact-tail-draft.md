# Diagonal non-reciprocal c>=2 exact-tail draft

Date: 2026-05-12

This note attacks the remaining non-reciprocal diagonal slack case

```tex
q=ha+r,\qquad r=h+1+c,\qquad c\ge2,\qquad r<a,
\qquad (a,r)=1,\qquad (a+1,c)=1.
```

It is deliberately proof-oriented but not a completed proof.  The useful
certificate is the staircase-band gate from
`notes/diagonal-nonreciprocal-cone-obstruction.md`, with the exact divisor
tail from `scripts/diagonal_nonreciprocal_band_check.py --exact-tail`.

Write `A=a+1`.  For `s>=0`, put

```tex
U_s=\left\lceil{(s+1)A\over c}\right\rceil,\qquad U_{-1}=0,
```

and define the staircase rectangle

```tex
R_s=[u_0,u_1]\times[j_0,j_1]
```

by

```tex
u_0=U_{s-1}+1,\qquad u_1=U_s,\qquad
j_0=c+s+1,\qquad
j_1=\left\lfloor {r(a+u_0)-1\over a}\right\rfloor .
```

Let

```tex
P_s=\#\{(u,j)\in R_s:(a+u,j)=1\}.
```

The gate target is

```tex
C_0+\sum_{t=0}^S P_t\ge D(q+\Theta_{S+1}-1),
\qquad
\Theta_s=hU_s+j_1(s)-r,
```

after the initial phase `0<=sigma<Theta_0` is covered.

## Geometry of one staircase rectangle

Let

```tex
P_0=a+u_0,\qquad P_1=a+u_1,\qquad W=u_1-u_0+1,\qquad H=j_1-j_0+1.
```

Every point of `R_s` lies in the intrinsic cone

```tex
{c(a+u)\over A}<j<{r(a+u)\over a}.
```

Consequently the whole rectangle has the ratio enclosure

```tex
{a\over r}< {P_0\over j_1}\le {a+u\over j}
\le {P_1\over j_0}< {A\over c}.              \tag{1}
```

The width of this enclosing rational interval is explicit:

```tex
\Delta={A\over c}-{a\over r}
={Ar-ac\over cr}
={(h+1)A+c\over cr}.                         \tag{2}
```

This is the first useful structural saving.  In the thin `h=1` artifact
family, where `c` is comparable to `A`, the possible quotient ratios in the
tail lie in an interval of length `O(1/c)`, even though the raw tail bound
sees all divisors `d<=j_1`.

The exact height is

```tex
H=h+1-s+
\left\lfloor {r u_0-1\over a}\right\rfloor . \tag{3}
```

Thus `H>=h+1` for the initial band `s=0`; for `h=1` and `c` comparable to
`A`, (3) gives the observed short rectangles of height `2,3,4,...`.

## Exact-tail Mobius certificate

For a rectangle `R=[u_0,u_1]\times[j_0,j_1]`, define

```tex
N_u(d)=\#\{u_0\le u\le u_1:a+u\equiv0\pmod d\},
\qquad
N_j(d)=\#\{j_0\le j\le j_1:j\equiv0\pmod d\}.
```

Mobius inversion gives

```tex
P_R=\sum_{d\ge1}\mu(d)N_u(d)N_j(d).
```

For any cutoff `T>=1`,

```tex
P_R\ge
\sum_{d\le T}\mu(d)N_u(d)N_j(d)
-E_T(R),                                      \tag{4}
```

where the exact adversarial tail is

```tex
E_T(R)=\sum_{d>T}N_u(d)N_j(d).                \tag{5}
```

This is the `--exact-tail` lower bound in the band checker.  It is a union
bound over possible large common divisors, but it keeps the exact residue
condition in the `u` coordinate.

## Divisor-quotient transform for the tail

The following identity is the strongest analytic handle found so far.

**Lemma 1 (tail quotient identity).**  Let

```tex
P=[P_0,P_1]=[a+u_0,a+u_1],\qquad J=[j_0,j_1].
```

For `T>=1`,

```tex
E_T(R)=
\sum_{1\le e\le P_1/(T+1)}
\sum_{1\le y\le j_1/(T+1)}
M_T(e,y),                                    \tag{6}
```

where

```tex
M_T(e,y)=
\#\left\{d\in{\bf Z}:
d>T,\ P_0\le ed\le P_1,\ j_0\le yd\le j_1
\right\}.
```

Equivalently,

```tex
M_T(e,y)=
\max\left(0,
\left\lfloor\min\left({P_1\over e},{j_1\over y}\right)\right\rfloor
-\left\lceil\max\left({P_0\over e},{j_0\over y},T+1\right)\right\rceil
+1
\right).                                    \tag{7}
```

Proof.  A summand in (5) is exactly a triple `(d,u,j)` with `d>T`,
`d|(a+u)`, and `d|j`.  Put `a+u=ed` and `j=yd`.  This is reversible, and
(7) is just the interval of admissible `d`.  Each common divisor is counted
once, as required by the union tail (5).  QED.

The staircase cone immediately restricts the quotient pair.

**Lemma 2 (ratio-window tail bound).**  For a staircase rectangle `R_s`,
`M_T(e,y)=0` unless

```tex
{a\over r}< {e\over y}< {A\over c}.          \tag{8}
```

Therefore, with

```tex
Y_T=\left\lfloor {j_1\over T+1}\right\rfloor,\qquad
K(y)=\#\left\{e\in{\bf Z}: {ay\over r}<e<{Ay\over c}\right\},
```

we have the computable upper bound

```tex
E_T(R_s)\le
\sum_{1\le y\le Y_T}
\sum_{\substack{e\in{\bf Z}\\ ay/r<e<Ay/c}}
M_T(e,y),                                   \tag{9}
```

with `M_T(e,y)` given by (7), and the softer closed bound

```tex
E_T(R_s)\le
\sum_{1\le y\le Y_T}K(y)\left(1+{H\over y}\right).  \tag{10}
```

Since

```tex
K(y)\le 1+y\Delta,\qquad
\Delta={(h+1)A+c\over cr},
```

(10) implies

```tex
E_T(R_s)\le
Y_T+{\Delta Y_T(Y_T+1)\over2}
+H\sum_{y\le Y_T}{1\over y}
+H\Delta Y_T.                              \tag{11}
```

Proof.  If `M_T(e,y)>0`, then for some `d>T` the point `(ed,yd)` lies in
`P\times J`.  By (1), `e/y=(ed)/(yd)` lies in `(a/r,A/c)`.  For fixed
`e,y`, the admissible `d` values with `yd in [j_0,j_1]` form an interval of
length at most `H/y`, proving `M_T(e,y)<=1+H/y`.  The estimate for `K(y)`
uses the interval length (2).  QED.

Remarks.

1.  Bound (9), not the softer (11), is the right finite-reduction object:
    it is an exact floor expression over only the small quotient variables
    `(e,y)`, and it is independent of Mobius signs.
2.  Bound (11) is useful for a large-parameter proof because its dependence
    on the tail cutoff is through `Y_T=j_1/(T+1)`, while its dependence on
    the staircase arithmetic is through the narrow width `Delta`.
3.  The old raw tail corresponds morally to replacing `K(y)` by all
    `e<=P_1/(T+1)`, losing the cone ratio window.

## The h=1 split

When `h=1`, `r=c+2`, and

```tex
\Delta_1={2A+c\over c(c+2)}.                \tag{12}
```

The exact height formula becomes

```tex
H=2-s+\left\lfloor{(c+2)u_0-1\over a}\right\rfloor. \tag{13}
```

This explains the scanner behavior.  In the hard family
`c` comparable to `A`, the width `W` is one or two columns and `H` is small;
the raw tail is terrible, but (12) forces only very few quotient numerators
`e` for each `y`.

The focused scanner reports:

```text
python scripts\diagonal_nonreciprocal_h1_tail_scan.py 300 --s-max 40 --mobius-cutoff 5
checked=258587
exact_bad=0
lower_bad=0
lower_best=(1, 269, 178, 91, 89, 40, 103, (82, 83, 130, 132))
```

and

```text
python scripts\diagonal_nonreciprocal_h1_tail_scan.py 500 --s-max 80 --mobius-cutoff 10
checked=1533411
exact_bad=0
lower_bad=0
lower_best=(11, 98, 65, 33, 31, 1, 41, (4, 5, 33, 35))
```

I also re-ran the narrower `q<=300` deeper scans while preparing this note:

```text
python scripts\diagonal_nonreciprocal_h1_tail_scan.py 300 --s-max 80 --mobius-cutoff 10
checked=510867
exact_bad=0
lower_bad=0
lower_best=(11, 98, 65, 33, 31, 1, 41, (4, 5, 33, 35))

python scripts\diagonal_nonreciprocal_h1_tail_scan.py 300 --s-max 120 --mobius-cutoff 15
checked=763147
exact_bad=0
lower_bad=0
lower_best=(11, 98, 65, 33, 31, 1, 41, (4, 5, 33, 35))
```

So the required head cutoff in the `h=1` branch appears to scale with the
staircase depth, roughly `T=s/8` in these boxes, not with `q`.

**Candidate h=1 lemma.**  There is an absolute constant `K` such that the
gate inequality for `h=1`, `c>=2`, is certified by (4) on each completed
staircase band with cutoff

```tex
T_S=\max(1,\lceil S/K\rceil)
```

through gate depth `S`, plus the already observed base surplus.  The current
data support `K=8` in the tested ranges.

How to prove it.

1.  Use (9) with `h=1` and `T=T_S`.  For `s` comparable to `c`, (12) and
    `Y_T=O(c/T+s/T)` make the quotient sum bounded by an absolute multiple
    of `H`.
2.  For `s<c/4`, the depth is still in the early phase where the base
    surplus and the first few exact bands should cover a finite rational
    reduction.  This is the part not yet written as a theorem.
3.  For `c` small compared with `A`, the bands are wide.  The area term from
    the Mobius head should dominate the quotient-tail bound; this needs a
    separate "wide h=1" inequality.

Remaining h=1 gap: no global analytic inequality has yet been proved that
turns (9) or (11) into the cumulative gate inequality for every `a,c,S`.
The computational evidence says the reduction should be low-dimensional:
after quotienting by `(e,y)`, the hard thin bands have only a bounded number
of possible quotient ratios.

## The h>=2 split

For `h>=2`, the exact-tail certificate is much stronger.  The band checker
passes with cutoff `T=1` in the tested boxes:

```text
python scripts\diagonal_nonreciprocal_band_check.py 1000 --s-max 20 --h-min 2 --mobius-cutoff 1 --exact-tail
checked=1370355
bad=0
mobius_bad=0
mobius_best=(3, 104, 4, 23, 12, 1, 44, 41)

python scripts\diagonal_nonreciprocal_band_check.py 500 --s-max 40 --h-min 2 --mobius-cutoff 1 --exact-tail
checked=594090
bad=0
mobius_bad=0
mobius_best=(3, 104, 4, 23, 12, 1, 44, 41)

python scripts\diagonal_nonreciprocal_band_check.py 300 --s-max 80 --h-min 2 --mobius-cutoff 1 --exact-tail
checked=362799
bad=0
mobius_bad=0
mobius_best=(3, 104, 4, 23, 12, 1, 44, 41)
```

Thus the right `h>=2` target is simpler:

```tex
C_0+\sum_{s=0}^S
\left(|R_s|-\sum_{d\ge2}N_u^{(s)}(d)N_j^{(s)}(d)\right)
\ge D(q+\Theta_{S+1}-1).                    \tag{14}
```

Equivalently, prove the gate with the exact nonprimitive union tail
`E_1(R_s)`.

Using Lemma 2 with `T=1`, a proof can replace each `E_1(R_s)` by the
finite quotient expression

```tex
\overline E_1(R_s)=
\sum_{1\le y\le\lfloor j_1/2\rfloor}
\sum_{\substack{e\in{\bf Z}\\ ay/r<e<Ay/c}}
M_1(e,y).                                  \tag{15}
```

This expression is still exact enough for finite checking, but its summation
range is governed by the cone-ratio width `Delta`, not by the long numerator
interval.

**Candidate h>=2 lemma.**  For every valid non-reciprocal tuple with
`h>=2` and `c>=2`, and every `S>=0`, inequality (14) holds.  A proof should
use (15) for the tail and split only by the elementary size of `Delta`:

```tex
\Delta={(h+1)A+c\over cr}.
```

Suggested analytic split.

1.  If `c` is small, then `W_s` is large and the head term `|R_s|` is large.
    The harmonic tail bound (11) should be dominated after summing bands.
2.  If `c` is large, then `Delta` is small and `K(y)` is usually `0` or `1`
    for the quotient variables; (15) should be a short floor-sum reduction.
3.  The minimum checked lower margin for `h>=2` is `3`, at
    `(q,h,a,r,s,total,target)=(104,4,23,12,1,44,41)`, so the finite box is
    tighter than the `h=1` base-buffer scan but not near a true failure.

Remaining h>=2 gap: inequality (14) has not been proved from (15).  The
needed finite reduction should be exact rational/floor arithmetic and should
not use floating estimates for Mobius sums.

## Quotient-tail checker

The quotient transform has now been made executable in

```text
scripts/diagonal_nonreciprocal_tail_quotient_check.py
```

It computes the exact adversarial tail both ways:

```tex
\sum_{d>T}N_u(d)N_j(d)
```

and the quotient sum (6)-(7), using the ratio-window restriction (8).  It
then asserts equality row by row.

Verification runs:

```text
python scripts\diagonal_nonreciprocal_tail_quotient_check.py 300 --s-max 40 --cutoff 1
checked=442226
mismatches=0
worst_tail=(2990, 2969, 3, 297, 2, 146, 5, 2, 40)

python scripts\diagonal_nonreciprocal_tail_quotient_check.py 300 --s-max 80 --h-min 1 --h-max 1 --cutoff 10
checked=510867
mismatches=0
worst_tail=(502, 486, 2, 297, 1, 292, 5, 3, 76)

python scripts\diagonal_nonreciprocal_tail_quotient_check.py 220 --s-max 80 --h-min 2 --cutoff 1
checked=167346
mismatches=0
worst_tail=(4331, 4314, 3, 217, 2, 106, 5, 2, 80)

python scripts\diagonal_nonreciprocal_tail_quotient_check.py 500 --s-max 20 --h-min 2 --cutoff 1
checked=304290
mismatches=0
worst_tail=(2554, 2516, 2, 497, 2, 246, 5, 2, 20)
```

Here `worst_tail` records

```text
(tail, quotient_pairs, max_multiplicity, q, h, a, r, c, s).
```

The equality check matters because future proof reductions can work with the
smaller quotient pair set without changing the certificate.

## Computational reduction still needed

Then add two proof-reduction scans.

1.  `h>=2`, `T=1`: accumulate the lower bound (14), but record the quotient
    parameters `(y,e)` that realize the worst tails.  This should identify a
    small finite box in `(h,c,s)` or prove monotone drift outside it.
2.  `h=1`, `T=ceil(S/8)`: accumulate gates through depth `S`, using the same
    quotient tail.  The output should separate the thin case
    `c comparable to A` from the wide case `c small compared with A`.

The key advantage is that all quantities in (7), (9), and (15) are floors of
rational functions in `a,h,c,s,e,y`.  No unproved cancellation in `mu` is
being used in the tail.

## Current conclusion

The full diagonal non-reciprocal `c>=2` proof is not complete.

The strongest proved general lemma here is the exact-tail quotient identity
and ratio-window bound, Lemmas 1 and 2.  They explain why the exact-tail
certificate succeeds where the raw tail fails: a large common divisor
`d>T` forces the reduced quotient pair `(e,y)=((a+u)/d,j/d)` into the
short interval

```tex
{a\over r}< {e\over y}< {a+1\over c}.
```

For `h>=2`, computations now support the very clean `T=1` gate theorem.
For `h=1`, computations support a separate theorem with head cutoff growing
with staircase depth, approximately `T=ceil(S/8)`.  The remaining work is to
turn these quotient-tail bounds into a cumulative gate inequality outside an
explicit finite box.
