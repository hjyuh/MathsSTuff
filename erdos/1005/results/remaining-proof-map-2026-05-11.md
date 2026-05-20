# EP1005 remaining proof map

Date: 2026-05-11

This file summarizes the current proof state after the latest diagonal and
unit-step reductions.

## Diagonal intervals

Goal:

```tex
\frac aq<\frac{a+1}{q-1}
\quad\Longrightarrow\quad
B_n(a,q)\ge D(n)
```

for `n>=92`, where

```tex
D(n)=\left\lfloor\frac n4\right\rfloor+d_{n\bmod4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4).
```

Closed or certified:

```text
h=2 reciprocal: closed by explicit formulas.
h=3 reciprocal: closed by explicit formulas; unique tie at n=99.
r=0: closed by injection and harmonic bound.
h>=4 reciprocal, n=q: certified by finite box.
h>=4 reciprocal, n>q: reduced to two-triangle lemma; finite boxes certified.
```

Remaining diagonal sector:

```text
non-reciprocal r>h.
```

Current exact reduction for `r>h`:

```tex
q=ha+r,\qquad c=r-h-1\ge1,
```

and the base strip

```tex
C_0(a,h,r)=
\#\left\{(p,j):
1\le p\le a,\quad
\frac{cp}{a+1}<j<\frac{rp}{a},\quad
(p,j)=1
\right\}
```

has raw size exactly

```tex
\frac{q+a-1}{2}.
```

The remaining proof-grade task is a primitive-point lower bound for this
two-sided rational strip, plus a denominator-slack estimate for `n>q`.
A truncated Mobius certificate with cutoff `12 sqrt(a)` verifies all
`q<=1000`, but `notes/diagonal-nonreciprocal-cone-obstruction.md` records
why the naive raw-tail and fixed 12-row growth routes are not scalable.

The most recent slack decomposition for `c>=2` is the staircase-band
certificate.  It partitions the cone by the lower-floor levels

```tex
U_s=\left\lfloor\frac{(s+1)(a+1)-1}{c}\right\rfloor+1
```

and uses full bands

```tex
U_{s-1}+1\le u\le U_s,\qquad
c+s+1\le j\le
\left\lfloor\frac{r(a+U_{s-1}+1)-1}{a}\right\rfloor.
```

The checker `scripts/diagonal_nonreciprocal_band_check.py` has no failures
through `q<=1000`, `s<=20`; the best margin is `8`.  The exact initial phase
before the first translated/base-style slab has no failures through `q<=700`.

The attempted reduced-residue dual bound for these same rectangles is not
strong enough.  The checker `scripts/diagonal_nonreciprocal_band_dual.py`
uses the better of the `j`-wise and `p`-wise discrepancy bounds; through
`q<=300`, `s<=20`, it has `exact_bad=0` but `dual_bad=117152`.  Therefore
the `c>=2` route still needs the Mobius rectangle certificate.  Cutoff
profiling shows the hard false negatives are tail-bound artifacts in thin
`h=1` families: cutoff `200` certifies `q<=300`, cutoff `300` certifies
`q<=500`, while cutoff `400` still fails for `q<=1000` near
`(h,a,r)=(1,501,499)`.

This raw-tail problem is now substantially fixed.  The band checker has a
new `--exact-tail` option that subtracts only the actual congruence classes
available in the rectangle for `d>T`, rather than the crude
`\lceil W/d\rceil\lceil H/d\rceil` tail.  With exact tail,
`--mobius-cutoff 1` certifies `q<=1000`, `s<=20`, and
`--mobius-cutoff 5` certifies `q<=500`, `s<=40`.  This turns the likely
`c>=2` theorem into a small-head Mobius bound plus an exact divisor-tail
union bound.

For the thin `c=1` large-slack branch, the first shifted-block gap is now
reduced by exact rational arithmetic.  The checker
`scripts/diagonal_nonreciprocal_c1_first_gap.py` evaluates

```tex
aM_h-T_h+(a+1)A_h-E_h\ge D(3h(a+1)+h+3)
```

and uses the positive four-step drift

```tex
\operatorname{margin}(h,a+4)-\operatorname{margin}(h,a)
=4(M_h+A_h)-3h.
```

Running

```text
python scripts\diagonal_nonreciprocal_c1_first_gap.py 300 --max-a-extra 1000
```

gives `bad=398`, `nonpositive_step=0`, and last bad `(h,a)=(44,47)`.
Thus the discrepancy first-gap bound holds outside the finite box
`h<=44`, `a<=47`; that box is handled by the exact shifted-block checker.
The note now also records an elementary summatory-totient estimate proving
the first-gap inequality for all `h>=165`, so only `h<=164` is genuinely
finite.

For later shifted-block increments, the new exact rational checker
`scripts/diagonal_nonreciprocal_c1_increment.py` uses the maximum of the
`j`-wise and dual `p`-wise reduced-residue lower bounds.  The run

```text
python scripts\diagonal_nonreciprocal_c1_increment.py 300 --k-max 100 --max-a-extra 1000
```

has `bad=0`, `nonpositive_step=0`, and best row
`(Fraction(3728434771, 76491415), 8, 12, 1)`.  The remaining work here is
to write the large-parameter proof showing the dual-bound certificate
covers all `h,k`, with only a finite rational box left to enumerate.

## Non-reduced unit-step obstruction

Setup:

```tex
\frac{gx-1}{gy+1}<\frac xy<\frac cd,\qquad
H=yc-xd.
```

Closed:

```text
H=1 edge: proved by primitive-triangle discrepancy plus finite check.
```

Remaining:

```text
H>=2.
```

Current exact reduction for the right block:

```tex
p=\frac{cE+xF}{H},\qquad
q=\frac{dE+yF}{H},
```

with

```tex
E,F\ge1,\qquad H\mid cE+xF,\qquad dE+yF\le nH.
```

The remaining proof-grade task is now sharpened further.  Every such interval
contains the real edge

```tex
\frac{gx-1}{gy+1}<\frac{gx}{gy-1}.
```

For `x=1` this is the closed `H=1` edge.  For `x>=2`,
`notes/unit-step-Hge2-edge-reduction.md` gives the exact row-count formula
and `scripts/unit_step_hge2_edge_check.py` verifies all edge orders through
`n<=300`, with minimum surplus `7`.

For minimal order, the branch now has two additional certificates:

```text
scripts/unit_step_hge2_periodic_check.py
scripts/unit_step_hge2_edge_mobius.py
```

The periodic checker verifies the `4X(X+1)` finite window for every
`X=gx-1<=40`, with no failures and the same minimum surplus `7`.  The
Mobius checker certifies minimal-order edges through `n<=1000` with cutoff
`512`.  These are still finite/proof-search certificates; the missing step is
a uniform large-`X` lower bound and a slack-in-`n` argument.

The previous 32-denominator-row growth candidate is false globally, although
it holds through `n<=1000`.  A sparse example
`(g,x,y)=(2,105,5251)` has only seven new fractions in the first 32 slack
rows.  Its minimal-order surplus is `756`, so the actual inequality remains
far from failure.  The remaining slack task is therefore to combine
minimal-order surplus with long-run denominator-row growth, not to prove a
fixed short-block lemma.

The single-numerator sparse phase is now isolated and checked through
`n_0<=1000` by `scripts/unit_step_hge2_sparse_buffer.py`, with no failures
and the same global minimum surplus `7`.

The periodic sparse-buffer checker
`scripts/unit_step_hge2_sparse_periodic_check.py` verifies the full
`4X(X+1)` finite window for `X<=40`, again with no failures and minimum
surplus `7`.  The missing proof step is to show the sparse-buffer surplus has
the same positive periodic drift used at minimal order.

After the sparse phase, `scripts/unit_step_hge2_t_band_check.py` groups rows
by numerator offset `p=gx+t`.  The exact completed-band checker has no
failures through `n<=500`, `t<=20`, with best margin `5`.  The simple
per-band discrepancy estimate is too weak, but the exact Mobius interval
formula over divisors of `gx+t` certifies the same bands through `n<=1000`,
`t<=20`, with no failures and the same best margin `5`.

The combined edge certificate
`scripts/unit_step_hge2_combined_certificate.py` verifies minimal order,
sparse rows, and completed Mobius offset bands together through `n<=1000`,
`t<=20`, with no failures and best margin `9`.

The periodic-window version
`scripts/unit_step_hge2_combined_periodic.py` verifies the combined
certificate through `X<=30` over four periods, with no failures and best
margin `7` at the minimal-order gate.

The offset-band drift checker finds no examples through `n<=500`, `t<=100`
where the completed-band minimum occurs after `t=20`; the best late margin is
`74`.  A drift lemma for `t>20` would make the finite `t<=20` certificates
structurally sufficient.

The refined drift target is a four-band increment lemma: every four
consecutive offset bands with `t>=21` should contribute at least the target
increase to the next four-band gate.  The checker verifies this through
`n<=700`, `t<=100`, with no failures and equality in the best case.
Tight checked cases have band lengths `(3,3,3,3)` or `(3,3,3,4)`, reducing
the hard local residue analysis to a small finite pattern family.
In the current widest scan, four-band equality occurs only for
`(g,x,y,t)=(2,169,178,46)`.
Naive reduced-residue discrepancy is too weak for this lemma; the needed
input is a direct local residue argument for the four moduli
`gx+t,...,gx+t+3` in the low-length cases.
The local equality pattern has all four short intervals starting at residue
`20` modulo their corresponding numerator moduli.

The equality uniqueness statement above is only true in the original
`n<=700` scan.  In the abstract variables `K=gx`, `A=gy-gx`, the exact
four-band inequality is

```tex
\sum_{i=0}^3
\#\{a_{t+i}\le s\le b_{t+i}:(K+t+i,K+A+s)=1\}
\ge D(K+A+b_{t+4})-D(K+A+b_t),
```

where

```tex
a_u=u+\lfloor(A-1)u/K\rfloor,\qquad
b_u=u+\lfloor((A+2)u+2K+A-1)/(K-1)\rfloor.
```

The new checker `scripts/unit_step_hge2_four_band_abstract.py` verifies this
exact local inequality in a larger low-length box:

```text
python scripts\unit_step_hge2_four_band_abstract.py 1200 --a-max 220 --t-max 180 --max-band-length 4 --max-total 3
checked=8236705
bad=0
best=(0, 338, 18, 46, 3, 3, (3, 3, 3, 3), (0, 0, 1, 2))
```

It finds later equality blocks, for example local modulus block
`894,895,896,897` starting at residue `90`, with count pattern `(1,2,0,0)`.
Thus the remaining local proof should prove the inequality itself and allow
a sparse equality family, not try to prove uniqueness of the first equality
case.

This target has been corrected again: the unbuffered four-band inequality is
false globally.  The valid abstract edge

```text
K=2270, A=488, t=28
```

has four-band count `2` and target `3`.  In original variables
`(g,x,y)=(2,1135,1379)`.  The cumulative edge certificate has surplus over
`1500`, so this is only a drift-lemma failure, not a conjecture threat.  The
remaining unit-step proof should now aim for a buffered drift theorem or a
monotonicity theorem restricted to the near-tight region where accumulated
surplus is small.

The buffered scanner `scripts/unit_step_hge2_four_band_buffer.py` measures
the exact cumulative surplus before each negative local block.  In the
counterexample window it reports

```text
negative=1
bad_buffer=0
worst_buffer=(1578, -1, 1579, 2270, 488, 28, 2, 3, 3)
```

so the only local deficit there is absorbed by a surplus of `1579` before
the block.  Broader low-length scans through the surrounding parameter
boxes found no unabsorbed deficits.

The negative-pattern classifier found only two local deficit patterns in the
verified high-`K` low-length box: `(0,1,0,1)` and `(0,2,0,0)`, both with
lengths `(3,3,3,3)`, target `3`, and local margin `-1`.  They have constant
residue starts and constant floor data across the block.  This suggests the
remaining local unit-step proof should isolate these CRT families and prove
that their occurrence implies a large accumulated buffer.

Later residue-realizability scans found additional negative count patterns,
so the two-pattern statement is only local to that box.  The stable
features are instead: length-three bands, target `3`, and constant floor
data across the four bands.  A wider scan finds local deficit `2` examples,
but sample negative realizations all have large pre-block surplus, from
`1579` upward.

The summary scanner collected 200 negative realizations from the first 59
pure CRT records.  The minimum pre-block buffer remained `1579`; the worst
local deficit was `-2`, with buffer `4287`.  The stable floor pattern is
`\alpha=(m,m,m,m,m)` and `\beta=(m+2,m+2,m+2,m+2,m+3)`.

## Final integration

Once the two remaining primitive-point theorems are proved:

1. every bad interval contains the real unit-step interval;
2. if that point is reduced, the global diagonal theorem applies;
3. if it is non-reduced, the `H=1` or `H>=2` unit-step theorem applies.

This would complete the lower bound. The upper bound is already supplied by
the residue-class constructions.
