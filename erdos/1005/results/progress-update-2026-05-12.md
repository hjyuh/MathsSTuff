# EP1005 progress update

Date: 2026-05-12

This update records the latest progress on the two remaining proof branches:
the non-reduced unit-step `H>=2` edge and the non-reciprocal diagonal slack
case.

## Unit-step `H>=2`

The four-band drift problem is now expressed in abstract variables

```tex
K=gx,\qquad G=gy,\qquad A=G-K.
```

The admissibility conditions are

```tex
A\ge2,\qquad (K,A)=g\ge2,\qquad K/g\ge2,\qquad (K-1,K+A+1)=1.
```

For `u>=21`, define

```tex
a_u=u+\left\lfloor\frac{(A-1)u}{K}\right\rfloor,\qquad
b_u=u+\left\lfloor\frac{(A+2)u+2K+A-1}{K-1}\right\rfloor.
```

The missing local drift lemma is exactly

```tex
\sum_{i=0}^3
\#\{a_{t+i}\le s\le b_{t+i}:(K+t+i,K+A+s)=1\}
\ge D(K+A+b_{t+4})-D(K+A+b_t).
```

The new checker

```text
scripts/unit_step_hge2_four_band_abstract.py
```

searches this exact local inequality directly.

Verification:

```text
python scripts\unit_step_hge2_four_band_abstract.py 800 --a-max 200 --t-max 160 --max-band-length 4 --max-records 5
checked=3632210
skipped_length=1872170
bad=0
best=(0, 338, 18, 46, 3, 3, (3, 3, 3, 3), (0, 0, 1, 2))
```

The earlier equality case `(K,A,t)=(338,18,46)` is not unique globally.
Later equality blocks occur, including a block with local moduli
`894,895,896,897` and starting residue `90`, with count pattern `(1,2,0,0)`.
Thus the right proof target is the inequality itself, not uniqueness of the
first equality case.

A tempting stronger surrogate is false: four length-three windows over
`p,p+1,p+2,p+3` need not have three primitive hits.  Example:
`p=1953`, residues `68,69,70` give only two primitive hits.  This is not a
counterexample to the real drift lemma because the corresponding realizable
gate target is only `1`.

Including length-five bands in the abstract search did not introduce new
equality:

```text
python scripts\unit_step_hge2_four_band_abstract.py 700 --a-max 180 --t-max 140 --max-band-length 5 --max-total 4
checked=3239749
skipped_length=450131
bad=0
best=(0, 338, 18, 46, 3, 3, (3, 3, 3, 3), (0, 0, 1, 2))
```

The unbuffered four-band drift lemma is false globally.  A valid edge tuple

```text
K=2270, A=488, t=28
```

has four band counts `(0,1,0,1)`, total `2`, while the gate target is `3`.
In original variables this is `(g,x,y)=(2,1135,1379)`.  The edge is still
far from threatening the conjecture: its minimal-order subcertificate has
surplus `1529`.  So the correct theorem must be a buffered drift statement:
negative four-band increments are allowed when the accumulated surplus is
already large.  The earlier four-band equality classification remains useful
only for the near-tight regime.

The new buffered scanner
`scripts/unit_step_hge2_four_band_buffer.py` confirms this in the
counterexample window:

```text
checked=5320
negative=1
bad_buffer=0
worst_buffer=(1578, -1, 1579, 2270, 488, 28, 2, 3, 3)
```

Here the local margin is `-1`, but the margin before the block is `1579`.
Two broader low-length scans, together checking over `21M` blocks, found no
unabsorbed deficits; the same counterexample remains the worst buffered row.

The new classifier `scripts/unit_step_hge2_negative_patterns.py` found only
two negative local patterns in the verified high-`K` low-length box:

```text
lengths=(3,3,3,3), target=3, margin=-1,
counts=(0,1,0,1) or (0,2,0,0).
```

Both have constant residue starts and constant floor data across the four
moduli.  This suggests the buffered proof can isolate a small CRT family of
negative blocks and prove those blocks only occur when the accumulated
surplus is already large.

The pure CRT search `scripts/unit_step_hge2_residue_bad.py` now distinguishes
bad residue blocks from actual negative edge drift.  The first pure bad
blocks, such as `(p,R)=(1308,644)`, are edge-realizable but harmless because
their actual target increments are `0` or `1`.  The first residue blocks
that create true local edge deficits are `(p,R)=(2298,494)` and
`(2532,440)`, both with local margin `-1` in their negative realizations.
The same script can list the first pure CRT obstruction templates with
`--stop-after-records`; they mostly use repeated small-divisor covers of the
two zero-count rows, but the edge floor data and exact `D`-increment filter
out several early pure obstructions.

A broader realizability run shows that the earlier two-pattern list is not
global.  Additional negative count patterns such as `(0,1,1,0)` and
`(0,0,1,1)` appear among the first pure CRT obstructions, and a wider run
finds local margin `-2` blocks such as `(p,R)=(6354,650)` with counts
`(0,1,0,0)`.  The common feature persists: displayed negative realizations
have `lengths=(3,3,3,3)`, target `3`, and constant floor data.  Sample
buffers before these blocks remain large, from `1579` up to more than
`4400` in the checked examples.

The summary scanner
`scripts/unit_step_hge2_negative_summary.py` collected the first 200
negative realizations from the first 59 pure CRT records.  The minimum
pre-block buffer is still `1579`; the worst local deficit seen is `-2`, with
buffer `4287`.  The count patterns vary, but every recorded floor pattern is
constant in `alpha` and has `beta=(m+2,m+2,m+2,m+2,m+3)`.  This gives a
concrete two-part theorem target: negative blocks have this constant-floor
length-three form with bounded deficit, and that form forces a large
pre-existing buffer.

## Diagonal non-reciprocal `c=1`

The first large-slack shifted-block gap now has an exact rational finite
reduction.  The analytic lower bound is

```tex
aM_h-T_h+(a+1)A_h-E_h\ge D(3h(a+1)+h+3).
```

The new checker

```text
scripts/diagonal_nonreciprocal_c1_first_gap.py
```

uses rational arithmetic and the positive four-step drift

```tex
\operatorname{margin}(h,a+4)-\operatorname{margin}(h,a)
=4(M_h+A_h)-3h.
```

Verification:

```text
python scripts\diagonal_nonreciprocal_c1_first_gap.py 300 --max-a-extra 1000
h_checked=300
bad=398
best=(Fraction(-283046653, 4849845), 20, 23)
nonpositive_step=0
last_bad=(44, 47, Fraction(-83805514698775, 10593329013498))
```

So the discrepancy first-gap bound holds outside the finite box
`h<=44`, `a<=47`.  The exact shifted-block checker covers that box and the
later block increments:

```text
python scripts\diagonal_nonreciprocal_c1_shifted_reduction.py 10000 --k-max 20
rows_checked=569960
first_bad=0
increment_bad=0
```

The note `notes/diagonal-nonreciprocal-cone-obstruction.md` now also records
an elementary summatory-totient estimate proving the first-gap inequality
for all `h>=165`; therefore only `h<=164` is finite for this analytic
subcase.

The later shifted-block increment has also been upgraded from the old
floating-point discrepancy check to an exact rational dual-bound checker:

```text
python scripts\diagonal_nonreciprocal_c1_increment.py 300 --k-max 100 --max-a-extra 1000
h_checked=300
k_checked=100
bad=0
best=(Fraction(3728434771, 76491415), 8, 12, 1)
nonpositive_step=0
```

The new checker uses the better of the original `j`-wise reduced-residue
bound and the dual `p`-wise bound over the numerator interval.  This removes
the float dependence and shows that the apparent large-`k` failures of the
`j`-wise lower bound are only a weakness of that one-sided estimate.

## Diagonal non-reciprocal `c>=2`

The same dual-discrepancy idea was tested on the general staircase bands by
the new checker

```text
scripts/diagonal_nonreciprocal_band_dual.py
```

It certifies each rectangle with the better of the `j`-wise and `p`-wise
reduced-residue lower bounds.  This is not strong enough for `c>=2`:

```text
python scripts\diagonal_nonreciprocal_band_dual.py 300 --s-max 20
checked=226506
exact_bad=0
dual_bad=117152
```

So the general branch still needs the Mobius rectangle certificate.  The
cutoff profile is now clearer: for `q<=300`, cutoff `200` is enough; for
`q<=500`, cutoff `300` is enough; for `q<=1000`, cutoff `400` still fails
in the thin `h=1`, `a~q/2` family, while cutoff `500` passes.  These are
tail-bound artifacts rather than true near-failures: for example
`(q,h,a,r,s)=(1000,1,501,499,20)` has a one-column band with exact count `3`
and cumulative exact margin `263`.

An exact scan of only `h=1`, through `q<=1000` and staircase gates
`s<=40`, found minimum base surplus `11` and minimum gate surplus `13`.
This suggests splitting off `h=1` as a direct buffer lemma, then proving the
Mobius rectangle gate for `h>=2`.

The Mobius tail has now been sharpened.  The old checker subtracted a raw
tail over every `d>T`; the new `--exact-tail` option subtracts only residue
classes that can actually occur in the rectangle.  This keeps the lower
bound adversarial in the unknown Mobius signs, but removes the artificial
one-column failures.

With exact tail:

```text
python scripts\diagonal_nonreciprocal_band_check.py 1000 --s-max 20 --mobius-cutoff 1 --exact-tail
checked=3024105
bad=0
mobius_bad=0
mobius_best=(2, 134, 1, 89, 45, 20, 54, 52)
```

For a deeper band range:

```text
python scripts\diagonal_nonreciprocal_band_check.py 500 --s-max 40 --mobius-cutoff 5 --exact-tail
checked=1370261
bad=0
mobius_bad=0
mobius_best=(1, 269, 1, 178, 91, 40, 103, 102)
```

So the general `c>=2` proof target is now much cleaner: a small-head Mobius
certificate plus an exact divisor-tail union bound.

The focused `h=1` exact-tail scanner
`scripts/diagonal_nonreciprocal_h1_tail_scan.py` reproduces the small-margin
family quickly.  With cutoff `5`, it certifies `q<=300`, `s<=40`, with best
lower margin `1` at `(q,a,r,c,s)=(269,178,91,89,40)`.  For deeper bands,
cutoff `10` certifies `q<=500`, `s<=80`, with `lower_bad=0`.  This suggests
the required Mobius head for `h=1` grows with staircase depth, not with `q`.

## Remaining gaps

The full conjecture is not yet proved.  The remaining proof-grade tasks are:

1. prove the unit-step `H>=2` four-band local drift lemma in the abstract
   `(K,A,t)` variables, plus the short interpolation between completed gates;
2. finish the diagonal non-reciprocal Mobius rectangle gate for `c>=2`,
   likely with a special treatment of the thin `h=1` tail-artifact family;
3. turn the `c=1` later shifted-block dual-bound evidence into a written
   large-parameter proof;
4. assemble the final lower-bound proof with the already completed upper
   constructions.
