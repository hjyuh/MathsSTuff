# EP1005 progress update

Date: 2026-05-11

Goal: prove the full exact conjecture

```tex
f(n)=\left\lfloor\frac n4\right\rfloor+d_{n\bmod 4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4),
```

for all `n>=92`.

## New proof-grade partials

### Uniform determinant fan bound

The note `notes/uniform-fan-count-agent.md` replaces the previous
fixed-offset fan estimate with an exact uniform floor bound. If

```tex
\frac ab<\frac rs<\frac cd,\qquad
A=br-as,\qquad C=cs-dr,
```

then

```tex
B_n(a/b,c/d)\ge
1+
\sum_{1\le h<A}\phi(h)
\left\lfloor\frac{n(A-h)}{Ash}\right\rfloor
+
\sum_{1\le h<C}\phi(h)
\left\lfloor\frac{n(C-h)}{Csh}\right\rfloor.
```

There is no hidden `O_{A,C,s}(1)` term. In particular, the `1/3` cell has
the uniform lower bound

```tex
B_n(a/b,c/d)\ge 5n/18-1.
```

This removes the earlier asymptotic-only gap for fixed rational cells.

### Diagonal strips `h=2` and `h=3`

The note `notes/diagonal-h2-h3-agent.md` proves the diagonal lower bound in
the tight reciprocal strips:

```text
h=2, r=1,2: proved globally by closed formulas.
h=3, r=1: proved for n>=92 with strict surplus.
h=3, r=2: impossible for reduced diagonal endpoints.
h=3, r=3: proved for n>=92; unique exact tie at n=99, 32/99<33/98.
```

This accounts for the central families and the only off-center exact
minimizer seen in the atlas for `n>=92`.

### Non-reduced unit-step edge `H=1`

The note `notes/unit-step-edge-H1-reduction.md` reduces the sharp non-reduced
unit-step edge case to a two-parameter primitive-triangle count. The special
interval is

```tex
\frac{g-1}{gB+1}<\frac1B<\frac g{gB-1},
```

and at minimal order `n_0=gB+1` its exact count is

```tex
E(g,B)
=2+
\#\left\{(p,h):
1\le p\le g-1,\ 1\le h\le B,\ (p,h)=1,\ 
(B+1)p>(g-1)h
\right\}.
```

The note `notes/unit-step-H1-proof-agent2.md` proves this edge case. It uses
a reduced-residue interval discrepancy lemma and weak explicit
totient/divisor estimates to reduce possible exceptions to
`X<=538`, `Y<=527`, then checks a slightly larger rectangle exactly.

The exact scanner `scripts/edge_h1_scan.py` now reproduces this check. For
example:

```text
python scripts\edge_h1_scan.py 10000 --max-surplus 3
```

returns only the two minimum-surplus cases `(n,g,B)=(111,11,10)` and
`(127,7,18)`.

### Diagonal non-reciprocal edge `r=0`

The note `notes/diagonal-remaining-agent2.md` proves the valid diagonal
`r=0` case for all `n>=92`. Reducedness forces `a=1`, `h` even, and the
explicit injection in that note gives

```tex
B_n(1,h)\ge \frac{7(n+1)}{24}\ge D(n).
```

### Reciprocal diagonal base order

The note `notes/diagonal-reciprocal-base-reduction.md` gives a finite-box
proof for the remaining reciprocal diagonal base case `n=q`, `h>=4`.
It combines vertical and horizontal reduced-residue discrepancy estimates for
the primitive triangle `T(X,Y)`. If both estimates fail, then it forces

```tex
h<1300,\qquad a<1100.
```

The finite box is checked by `scripts/diagonal_reciprocal_base_check.ps1`:

```text
checked=182192127
bad=0
minSurplus=1
minRows=h=5 a=18 r=5 q=95 lower=28 target=27 surplus=1
```

Denominator slack `n>q` is still separate.

The note `notes/diagonal-reciprocal-slack-growth.md` records the exact slack
decomposition `n-q=wh+t`. Each full block of `h` slack adds a width-`w`
vertical strip to every reciprocal fan row, with coefficient

```tex
\sum_{j<r}\phi(j)/j+\sum_{k<h+1-r}\phi(k)/k,
```

which is enough to beat the `D(n)` growth once `w` is large. This reduces the
remaining reciprocal slack proof to bounded `w=O(log h)` and then an exact
finite certificate.

The compiled slack checker

```text
powershell -ExecutionPolicy Bypass -File scripts\diagonal_reciprocal_slack_check.ps1 -NMax 1000 -MaxSurplus 1
```

checked `4,849,486` reciprocal slack certificates through `n<=1000`, with no
failures and only three surplus-`1` records.

The note `notes/two-triangle-slack-lemma.md` isolates a sharper route for
all reciprocal slack with `w>=1`: the certificate contains

```tex
1+T(a+w,r-1)+T(a+w,h-r).
```

With the admissibility conditions `X=a+w>=r+2` and `h(X-1)+r>=92`, the exact
checker

```text
python scripts\two_triangle_slack_check.py --max-x 500 --max-h 500
```

found no failures in `41,537,711` checked triples; the minimum surplus was
`0`.

The larger finite box forced by the current analytic criteria was also
checked:

```text
powershell -ExecutionPolicy Bypass -File scripts\two_triangle_slack_check.ps1 -XMax 168 -HMax 7800
checked=107351897
bad=0
minSurplus=0
minRow=h=4 X=24 r=4 lower=29 target=29 surplus=0
```

The arithmetic gate for the box reduction is checked by
`scripts/two_triangle_reduction_check.py`:

```text
bad_phi=0
bad_h=0
outside_fail=0
```

So reciprocal diagonal slack is closed modulo writing the cited explicit
totient estimate into the final proof text. The computational certificates
for the finite reductions are in place.

## Remaining blockers

The full conjecture is not solved. The open proof obligations are:

1. A global diagonal lower bound for all reduced diagonal intervals outside
   the proved reciprocal cases, the proved `h=2` and `h=3` rows, and the
   proved `r=0` edge; the remaining diagonal sector is non-reciprocal `r>h`.
2. A proof of the non-reduced unit-step obstruction, including the `H=1`
   primitive-triangle inequality and the `H>=2` determinant-triangle case.
3. A final integration lemma showing every bad interval either contains a
   reduced diagonal subinterval or falls into the proved non-reduced
   unit-step obstruction.

The current state is strong partial progress, not a publishable full
solution.

## Latest non-reciprocal diagonal reduction

The note `notes/diagonal-nonreciprocal-strip-reduction.md` maps the
non-reciprocal diagonal sector `r>h` into the Stern-Brocot cell
`1/(h+1)<x<1/h`, using coordinates

```tex
x=\frac p{hp+j}.
```

At base order it gives the primitive-strip lower bound

```tex
B_q(a,q)\ge
\frac{q+a}{a(a+1)}\Phi(a)-\Tau(a).
```

The exact scanner found only one non-reciprocal row with surplus at most `5`
through `n<=220`, namely `(n,h,a,r)=(107,6,16,11)`.

The independent note `notes/diagonal-nonreciprocal-agent.md` confirms the
same obstruction and adds the exact raw lattice identity for the base strip:

```tex
\sum_{p=1}^{a}
\left(
\left\lfloor\frac{rp-1}{a}\right\rfloor
-\left\lfloor\frac{(r-h-1)p}{a+1}\right\rfloor
\right)
=\frac{q+a-1}{2}.
```

So the remaining difficulty is purely primitive-point loss in this strip; the
raw area is already far above the target scale.

The note `notes/diagonal-nonreciprocal-mobius-reduction.md` gives a Mobius
inversion route for the base strip. The compiled exact checker
`scripts/diagonal_nonreciprocal_base_check.ps1` verifies the base strip
through `q<=1000`:

```text
checked=146008
bad=0
records=2
minSurplus=4
minRow=q=107 h=6 a=16 r=11 count=34 target=30 surplus=4
```

The exploratory truncated-Mobius certificate with cutoff `12 sqrt(a)` also
certifies every non-reciprocal base row through `q<=1000`.

## Latest unit-step `H>=2` reduction

The note `notes/unit-step-Hge2-reduction.md` records determinant coordinates
for the remaining non-reduced unit-step case after `H=1` is closed. For the
right block

```tex
\frac xy<\frac pq<\frac cd,\qquad H=yc-xd\ge2,
```

the exact coordinates are

```tex
p=\frac{cE+xF}{H},\qquad q=\frac{dE+yF}{H},
```

with

```tex
E,F\ge1,\qquad H\mid cE+xF,\qquad dE+yF\le nH.
```

Thus `H>=2` is reduced to a primitive congruence-point count in a triangle,
plus the large left fan from `(gx-1)/(gy+1)` to `x/y`.

The near-target scanner

```text
python scripts\unit_step_hge2_scan.py 300 --max-surplus 7
```

found only three `H>=2` records within surplus `7` for `92<=n<=300`, with no
failures and minimum surplus `7`.

The branch has since been reduced to the real edge family

```tex
\frac{gx-1}{gy+1}<\frac{gx}{gy-1}.
```

The exact edge checker

```text
python scripts\unit_step_hge2_edge_check.py 300 --max-surplus 10
```

finds the same minimum surplus `7` at

```tex
n=95,\qquad \frac9{95}<\frac5{47}<\frac{10}{93}.
```

With `--scan-slack`, the checker verifies every edge order through `n<=300`
and finds no smaller slack case.

The minimal-order periodic reduction now has a dedicated checker:

```text
python scripts\unit_step_hge2_periodic_check.py 40 --periods 4
checked=92695
bad=0
best=(7, 9, 2, 5, 47, 95, 34, 27)
```

The minimal-order Mobius subcertificate also certifies the range through
`n<=1000` with cutoff `512`:

```text
python scripts\unit_step_hge2_edge_mobius.py 1000 --cutoff 512
checked=137602
exact_bad=0
mobius_bad=0
mobius_best=(7, 95, 2, 5, 47, 34, 27)
```

For edge slack in `n`, the denominator row formula is now checked by

```text
python scripts\unit_step_hge2_slack_rows.py 1000 --block 32 --need 8
```

with no surplus failures and no 32-row growth failures:

```text
surplus_bad=0
surplus_best=(7, 95, 34, 27, 2, 5, 47)
growth_bad=0
growth_best=(2, 223, 255, 10, 2, 3, 110, [...])
```

The analogous 4-, 8-, and 16-row growth lemmas are false in the checked
ranges.  However, the 32-row growth statement is false globally: for
`g=2`, `x=105`, `y=5251`, the first 32 slack rows all have the single
candidate numerator `210`, and only seven denominators are coprime to it.
The minimal-order surplus is `756`, so the actual surplus remains large.
The slack proof therefore needs a buffer-plus-long-run-growth argument, not a
fixed-block lemma.

The first sparse phase has an exact description: the single candidate
`p=gx` is present for

```tex
gy\le m<\frac{gx(gy+1)}{gx-1},
```

and contributes only when `(gx,m)=1`.  The next slack target is to prove that
the minimal-order surplus covers the worst possible deficit in this phase,
then use a long-run primitive-area/Mobius estimate once more numerator
candidates enter each row.

The sparse-buffer checker verifies the whole single-numerator phase through
`n_0<=1000`:

```text
python scripts\unit_step_hge2_sparse_buffer.py 1000
checked=137602
bad=0
best=(7, 95, 102, 95, 2, 5, 47, 34, 27)
```

The periodic sparse-buffer window also checks cleanly:

```text
python scripts\unit_step_hge2_sparse_periodic_check.py 40 --periods 4
checked=92695
bad=0
best=(7, 8, 3, 3, 32, 97, 105, 99, 35)
```

For the post-sparse edge rows, grouping by numerator offset
`p=gx+t`, `m=gy+s` gives explicit bands in `s`.  The checker

```text
python scripts\unit_step_hge2_t_band_check.py 500 --t-max 20
```

has no exact completed-band failures:

```text
checked=690879
exact_bad=0
exact_best=(5, 131, 3, 2, 31, 0, 41, 36)
```

With exact Mobius interval sums enabled, the first 20 completed offset bands
are certified through `n<=1000`:

```text
python scripts\unit_step_hge2_t_band_check.py 1000 --t-max 20 --mobius
checked=2889642
exact_bad=0
mobius_bad=0
mobius_best=(5, 131, 3, 2, 31, 0, 41, 36)
```

The completed-band drift checker suggests only early offset bands can be
tight:

```text
python scripts\unit_step_hge2_t_drift_check.py 500 --early-t 20 --t-max 100
checked=32899
late_min=0
best_all=(5, 0, 131, 3, 2, 31)
best_late=(74, 21, 141, 2, 24, 47)
```

The stronger grouped-increment check uses four consecutive offset bands:

```text
python scripts\unit_step_hge2_t_increment_check.py 700 --t-start 21 --t-max 100 --block 4
checked=5294000
bad=0
best=(0, 411, 2, 169, 178, 46, 3, 3)
```

So the likely drift lemma is not per-band monotonicity, but four-band
monotonicity after `t=20`.

The tight four-band patterns are narrow: in the scan through `n<=700`,
`t<=120`, every block with total count at most `3` has lengths
`(3,3,3,3)` or `(3,3,3,4)`.  The observed count patterns are a short finite
list, now recorded in `notes/unit-step-Hge2-edge-reduction.md`.

The exact equality case for the four-band increment is unique in that scan:
`(g,x,y,t)=(2,169,178,46)`, with lengths `(3,3,3,3)`, counts `(0,0,1,2)`,
and target increment `3`.

The local residue verifier identifies the equality configuration more
sharply: all four short intervals start at residue `20` modulo their
respective numerator moduli.

The pieces also pass as a single combined certificate:

```text
python scripts\unit_step_hge2_combined_certificate.py 1000 --t-max 20
checked=3027244
bad=0
best=(9, 99, 3, 4, 31, -1, 37, 28)
```

This checks exact minimal order, exact sparse rows, and Mobius-certified
completed offset bands together.

The same combined certificate was checked on periodic windows:

```text
python scripts\unit_step_hge2_combined_periodic.py 30 --periods 4 --t-max 20
checked=38389
bad=0
best=(7, 9, 2, 5, 47, 95, -2, 34, 27)
```

Here `marker=-2` is the minimal-order gate, so the post-sparse gates are not
the tight cases in this window.

## Cone-growth obstruction found

The denominator-row cone formula for non-reciprocal diagonal intervals is
recorded in `notes/diagonal-nonreciprocal-cone-obstruction.md`.  It gives

```tex
B_n(a,q)=\sum_{m=1}^n
\#\left\{
p:
\left\lfloor\frac{am}{q}\right\rfloor+1
\le p\le
\left\lfloor\frac{(a+1)m-1}{q-1}\right\rfloor,\quad
(p,m)=1
\right\}.
```

The initial windows `q<=n<=q+11` are certified through `q<=1000`, but the
natural fixed 12-row growth lemma is false.  The thin-strip family

```tex
h=12,\quad r=14,\quad a=30029,\quad q=360362
```

has zero primitive rows for `m=q,...,q+11`.  Its base surplus is still large,
so the conjecture is not threatened, but the remaining proof needs a
base-surplus-plus-long-growth argument rather than fixed 12-row growth.

For the important `c=1` thin strip (`r=h+2`), the slack cone now has a
two-piece certificate:

```text
small/intermediate slack: capped core rectangle, floor(sigma/h) <= a+1
large slack: shifted full blocks, sigma >= h(a+2)
```

The shifted block `k` is

```tex
k(a+1)+1\le u\le (k+1)(a+1),\qquad
k+2\le j\le (k+1)(h+2).
```

The combined checker

```text
python scripts\diagonal_nonreciprocal_c1_check.py 1000 --sigma-max 200
```

reports no combined-certificate failures:

```text
combined_bad=0
combined_best=(7, 103, 5, 98, 6, 15, 36)
```

For the large-slack shifted-block range alone,

```text
python scripts\diagonal_nonreciprocal_c1_check.py 5000 --sigma-max 5000 --shifted-only --large-slack-only
```

also reports no failures, with best margin `25`.

The shifted-block induction gates are checked by

```text
python scripts\diagonal_nonreciprocal_c1_shifted_reduction.py 10000 --k-max 20
```

with no failures.  The exact first-gap margin is `25`, and the later-block
discrepancy increment margin is about `43.68` in the checked box.

The first-gap analytic discrepancy bound was also probed through `q<=20000`;
its only failures are within `h<=44`, `a<=47`, which are covered by the
exact first-gap gate.  This makes the remaining `c=1` writeup look like a
finite-reduction proof rather than an open search.

For general `c>=2`, there is now a stronger candidate than the sparse shifted
rectangles: translated copies of the full base strip.  The map

```tex
(p,j_0)\mapsto (a+u,j)=(s(a+1)+p,\ sc+j_0)
```

takes the raw base strip into the slack cone at scale `s`, available once
`sigma>=s(h(a+1)+c)-1`.  The exact initial phase before the first such strip
is verified through `q<=700`:

```text
python scripts\diagonal_nonreciprocal_initial_phase.py 700
checked=32645089
bad=0
best=(5, 107, 0, 107, 6, 16, 11, 35)
```

The translated strip increment check through `q<=500`, `s<=20` has no
increment failures:

```text
checked_increment=668420
increment_bad=0
increment_best=(5, 95, 6, 14, 11, 8, 30)
```

An even cleaner general `c>=2` decomposition is the staircase band
certificate.  With

```tex
U_s=\left\lfloor\frac{(s+1)(a+1)-1}{c}\right\rfloor+1,
```

the band

```tex
U_{s-1}+1\le u\le U_s,\qquad
c+s+1\le j\le
\left\lfloor\frac{r(a+U_{s-1}+1)-1}{a}\right\rfloor
```

lies inside the intrinsic cone.  The checker

```text
python scripts\diagonal_nonreciprocal_band_check.py 1000 --s-max 20
```

has no failures:

```text
checked=3024105
bad=0
best=(8, 102, 2, 37, 28, 0, 39, 31)
```

With the finite Mobius rectangle certificate enabled,

```text
python scripts\diagonal_nonreciprocal_band_check.py 1000 --s-max 20 --mobius-cutoff 500
```

also has no Mobius lower-bound failures:

```text
mobius_bad=0
mobius_best=(8, 102, 2, 37, 28, 0, 39, 31)
```
