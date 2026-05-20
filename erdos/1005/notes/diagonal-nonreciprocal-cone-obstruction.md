# EP1005 non-reciprocal diagonal cone and growth obstruction

Date: 2026-05-11

This note records the denominator-row cone formula for the non-reciprocal
diagonal sector and a counterexample to the naive fixed 12-row growth lemma.

## Denominator-row formula

For a valid non-reciprocal diagonal tuple

```tex
q=ha+r,\qquad r=h+1+c,\qquad c\ge1,\qquad r<a,
```

with

```tex
(a,r)=1,\qquad (a+1,c)=1,
```

the exact positive-row cone count is

```tex
B_n(a,q)=
\sum_{m=1}^n b_m(a,q),
```

where

```tex
b_m(a,q)=
\#\left\{
p:
\left\lfloor\frac{am}{q}\right\rfloor+1
\le p\le
\left\lfloor\frac{(a+1)m-1}{q-1}\right\rfloor,\quad
(p,m)=1
\right\}.
```

Equivalently, these are exactly the reduced fractions `p/m` in

```tex
\frac aq<\frac pm<\frac{a+1}{q-1}.
```

The script

```text
python scripts\diagonal_nonreciprocal_cone_check.py 1000
```

checks the initial windows `q<=n<=q+11` through `q<=1000`:

```text
initial_checked=1752096
initial_failures=0
```

## False fixed 12-row growth lemma

The tempting lemma

```tex
\sum_{m=M}^{M+11} b_m(a,q)\ge3
```

for all `M>=q` is false.  Take

```tex
h=12,\qquad r=14,\qquad c=1,\qquad
a=30029,\qquad A=a+1=30030,\qquad q=ha+r=360362.
```

Then `(a,r)=1`, `(a+1,c)=1`, and `h+2=r<a`.  For `m=q+t`,
`0<=t<=11`, the row interval has exactly one possible numerator:

```tex
p=A.
```

Indeed,

```tex
\left\lfloor\frac{a(q+t)}q\right\rfloor+1=A,\qquad
\left\lfloor\frac{A(q+t)-1}{q-1}\right\rfloor=A.
```

But

```tex
(q+t,A)=(12A+2+t,A)=(t+2,A)>1
```

for all `0<=t<=11`, since `t+2` runs from `2` to `13` and `A` is
divisible by every prime in that range.  Hence

```tex
b_q+b_{q+1}+\cdots+b_{q+11}=0.
```

This obstruction persists in the infinite thin-strip family

```tex
h=H,\qquad r=H+2,\qquad a=A-1,\qquad q=HA+2,
```

whenever `A` is divisible by the primes needed to cover the desired initial
row interval.  More generally, for any fixed block length `L`, choose
`H>=L` and choose `A` divisible by every integer `2,3,...,L+1`.  For
`m=q+t`, `0<=t<L`, the row interval again has the single candidate `p=A`,
and

```tex
(m,A)=(t+2,A)>1.
```

Thus no proof should rely on a universal fixed-length growth block for the
slack.

## Replacement target

The counterexample does not threaten the conjecture: for the displayed tuple
the base surplus is already large,

```text
B_q(a,q)=127521, D(q)=90092, surplus=37429.
```

The remaining proof should combine:

1. a proof-grade base surplus lower bound, strong enough to absorb early
   thin-strip primitive gaps;
2. a long-block or density growth estimate whose length may depend on the
   thin-strip parameter `h` or on the small-prime covering range;
3. a large-`n` cone estimate, since the primitive area growth is quadratic
   and has average slope well above the target slope `1/4`.

## Exact slack coordinates

The cone can also be written in coordinates adapted to denominator slack.
For `n=q+sigma`, write

```tex
p=a+u,\qquad m=h(a+u)+j=q+(hu+j-r).
```

Then

```tex
B_{q+\sigma}(a,q)=C_0(a,h,r)+G_\sigma(a,h,r),
```

where `C_0` is the base strip and

```tex
G_\sigma=
\#\left\{(u,j):
u\ge1,\quad
\frac{c(a+u)}{a+1}<j<\frac{r(a+u)}a,\quad
0\le hu+j-r\le\sigma,\quad
(a+u,j)=1
\right\}.
```

Thus slack only needs to prove

```tex
G_\sigma\ge D(q+\sigma)-D(q)-S_0,
\qquad S_0=C_0-D(q).
```

The failed fixed-block lemma tried to prove growth without using `S_0`.
The counterexample shows that `S_0` must be part of the argument.

## Thin `c=1` core block

When `c=1`, `r=h+2`.  For

```tex
U=\min\left(a,\left\lfloor\frac{\sigma}{h}\right\rfloor\right),
```

the slack cone contains the full rectangle

```tex
1\le u\le U,\qquad 2\le j\le h+2.
```

Therefore

```tex
G_\sigma\ge
\sum_{u=1}^{U}\sum_{j=2}^{h+2}1_{(a+u,j)=1}.
```

For any interval of `U` consecutive integers,

```tex
\sum_{u=1}^{U}\sum_{j=2}^{h+2}1_{(a+u,j)=1}
\ge
U A_h-E_h,
```

with

```tex
A_h=\sum_{j=2}^{h+2}\frac{\phi(j)}j,\qquad
E_h=\sum_{j=2}^{h+2}\tau(j).
```

This gives a concrete proof target for the thin edge:

```tex
S_0+U\left(A_h-\frac h4\right)\ge E_h+\frac h4+3.
```

The cap in `U` is essential.  The uncapped rectangle fails at `u=a+2`,
`j=2`, where the lower cone inequality becomes equality.

The focused `c=1` analysis reduces this branch as follows.  Base order uses

```tex
C_0(a,h)\ge aM_h-T_h,\qquad
M_h={1\over h+2}\sum_{j=1}^{h+1}{(h+2-j)\phi(j)\over j},
\qquad
T_h=\sum_{j=1}^{h+1}\tau(j),
```

plus an exact finite box.  The capped core block then closes every slack
with

```tex
0\le\left\lfloor\frac{\sigma}{h}\right\rfloor\le a+1,
\qquad\text{equivalently}\qquad
0\le\sigma<h(a+2).
```

The only `c=1` range not handled by this method is the large-slack cone

```tex
\left\lfloor\frac{\sigma}{h}\right\rfloor\ge a+2.
```

In the finite reduction for the capped-core range, the minimum margin is `7`
at `h=6`, `a=15`, `q=98`, `w=0`.

For large slack, shifted full blocks give a second subcertificate.  For
`k>=0`, the rectangle

```tex
k(a+1)+1\le u\le (k+1)(a+1),\qquad
k+2\le j\le (k+1)(h+2)
```

lies in the `c=1` slack cone once

```tex
\sigma\ge h(k+1)(a+1)+(k+1)(h+2)-(h+2).
```

Exact shifted-block checking through `q<=5000`, `sigma<=5000`, restricted
to the large-slack range `sigma>=h(a+2)`, gives:

```text
base_checked=13101
base_bad=0
base_best=(10, 98, 6, 15, 36, 26)
shifted_bad=0
shifted_best=(25, 299, 201, 98, 8, 11, 103)
combined_bad=0
combined_best=(25, 299, 201, 98, 8, 11, 103)
```

So in the tested range, the capped-core certificate and the shifted-block
certificate together cover all `c=1` slack with margin at least `7` in the
small/core range and `25` in the large-shifted range.

The shifted-block proof can be organized as an induction over completed
blocks.  The first large-slack gap is the interval after block `0` has
appeared and before block `1` appears; its worst endpoint is

```tex
\sigma=2h(a+1)+h+1.
```

At that endpoint the certificate is `C_0+B_0`.  Every later step only needs
block `k>=1` to pay for the target increase until the next block appears.
The checker

```text
python scripts\diagonal_nonreciprocal_c1_shifted_reduction.py 10000 --k-max 20
```

verifies these two gates in the displayed box:

```text
rows_checked=569960
first_bad=0
first_best=(25, 98, 8, 11, 299, 103, 78)
increment_bad=0
increment_best=(43.67712411427581, 98, 8, 11, 68.67712411427581, 25)
```

Here `first_best` is the exact margin for the first large-slack gap, and
`increment_best` is the margin from the reduced-residue discrepancy lower
bound for a later shifted block over the exact target increase.

The later-increment check now has an exact rational version:

```text
python scripts\diagonal_nonreciprocal_c1_increment.py 300 --k-max 100 --max-a-extra 1000
```

It uses two lower bounds on the same shifted block.  The original `j`-wise
bound is

```tex
(a+1)\sum_{j=k+2}^{(k+1)(h+2)}\frac{\phi(j)}j
-
\sum_{j=k+2}^{(k+1)(h+2)}\tau(j).
```

For large `k`, this can be too crude because the `\tau(j)` losses accumulate
over many `j`.  The dual `p`-wise bound over

```tex
(k+1)(a+1)\le p\le(k+2)(a+1)-1
```

is

```tex
L_{h,k}\sum_p\frac{\phi(p)}p-\sum_p\tau(p),
\qquad
L_{h,k}=(k+1)(h+2)-(k+2)+1.
```

The checker certifies a row if either rational lower bound pays the exact
`D`-increment.  Output:

```text
h_checked=300
k_checked=100
bad=0
best=(Fraction(3728434771, 76491415), 8, 12, 1)
nonpositive_step=0
```

The worst certified row is again the small valid case `h=8`, `a=11`,
`k=1`, with margin about `48.74`.  This also explains why the old
floating-point checker saw a strong margin for `k<=20`: the only later
failure mode was an artifact of using just the `j`-wise discrepancy.

The crude first-gap discrepancy lower bound has the form

```tex
aM_h-T_h+(a+1)A_h-E_h-D(3h(a+1)+h+3).
```

In the range checked through `q<=20000`, this analytic lower bound can fail
only for

```tex
h\le44,\qquad a\le47.
```

The exact first-gap check above covers that finite box with positive margin.
This suggests a short final proof of the `c=1` large-slack case: prove
positivity of the coefficient

```tex
M_h+A_h-\frac{3h}{4}
```

with explicit summatory-totient estimates, reduce the remaining small
`(h,a)` box, and use the later shifted-block discrepancy increment for the
induction across all further blocks.

This finite reduction is now exact.  The script

```text
python scripts\diagonal_nonreciprocal_c1_first_gap.py 300 --max-a-extra 1000
```

checks the first-gap analytic inequality with rational arithmetic and uses

```tex
\operatorname{margin}(h,a+4)-\operatorname{margin}(h,a)
=4(M_h+A_h)-3h.
```

The four-step increment is positive for every checked `h`, so once four
consecutive `a` values pass for fixed `h`, every larger `a` passes.  The
output is

```text
h_checked=300
bad=398
best=(Fraction(-283046653, 4849845), 20, 23)
nonpositive_step=0
last_bad=(44, 47, Fraction(-83805514698775, 10593329013498))
```

Thus the discrepancy lower bound for the first large-slack gap is proved by
finite rational checking outside the explicit box `h<=44`, `a<=47`; the
remaining failures are exactly the small cases that must be handled by the
exact shifted-block checker.

One elementary analytic bound gives a clean proof for large `h`.  Let
`H=h+2` and `\kappa=6/\pi^2`.  From

```tex
\frac{\phi(n)}n=\sum_{d\mid n}\frac{\mu(d)}d
```

we have, for `N>=1`,

```tex
\sum_{n\le N}\frac{\phi(n)}n
\ge \kappa N-\log N-2.
```

Therefore

```tex
A_h\ge \kappa H-\log H-3,\qquad
M_h\ge \frac{\kappa(H-1)}2-\log H-2.
```

Also

```tex
T_h+E_h\le 2H(1+\log H),\qquad
M_h\le\frac{H-1}{2},\qquad
D(N)\le N/4+4.
```

Since `a+1>=h+4`, the first-gap margin is bounded below by

```tex
(h+4)\left(
\frac{\kappa(H-1)}2+\kappa H-2\log H-5-\frac{3h}{4}
\right)
-\frac{H-1}{2}-2H(1+\log H)-\frac h4-\frac{19}{4}.
```

This expression is positive for `h>=165`.  Hence only `h<=164` needs exact
rational checking for the discrepancy first-gap inequality; the script above
does that and shows all failures lie in `h<=44`, `a<=47`.

The exact `c=1` checker is

```text
python scripts\diagonal_nonreciprocal_c1_check.py 1000 --sigma-max 200
```

and currently gives

```text
base_checked=2003
base_bad=0
base_best=(10, 98, 6, 15, 36, 26)
slack_checked=400600
slack_bad=0
slack_best=(9, 99, 1, 98, 6, 15, 37)
core_best=(7, 103, 5, 98, 6, 15, 36)
combined_bad=0
combined_best=(7, 103, 5, 98, 6, 15, 36)
```

An additional exact scan reported by the focused `c=1` analysis checked
`q<=1000`, `sigma<=2000`, with `4,008,003` cases and no failures.  The best
slack surplus remained `9` at `(n,sigma,q,h,a)=(99,1,98,6,15)`.

Base order alone was also checked through `q<=5000`:

```text
base_checked=13101
base_bad=0
base_best=(10, 98, 6, 15, 36, 26)
```

## Long-rectangle primitive lemma

For general `c`, fixed short row averages can be defeated by CRT choices of
the `j` interval.  The replacement should be a two-dimensional rectangle
Mobius lemma.  If

```tex
R=[U_0+1,U_0+U]\times[J_0+1,J_0+J]
```

lies inside the slack cone, then

```tex
P_R(a)=\#\{(u,j)\in R:(a+u,j)=1\}
```

satisfies the finite lower bound

```tex
P_R(a)\ge
\sum_{d\le T}\mu(d)N_d(R)
-
\sum_{T<d\le J_0+J}
\left\lceil\frac Ud\right\rceil
\left\lceil\frac Jd\right\rceil,
```

where

```tex
N_d(R)=
\#\{u\in[U_0+1,U_0+U]:u\equiv -a\pmod d\}
\#\{j\in[J_0+1,J_0+J]:j\equiv0\pmod d\}.
```

The remaining analytic task is to place such rectangles inside the slack cone
with enough total primitive mass to overcome the target growth after the base
surplus is included.

## General `c` translated-base slabs

For `c>=2`, the `c=1` shifted rectangles can be too sparse before their
height becomes positive.  A better general slack subcertificate is a
translated copy of the whole base strip.

Let `(p,j_0)` run over the raw base strip

```tex
1\le p\le a,\qquad
\frac{cp}{a+1}<j_0<\frac{rp}{a}.
```

For every scale `s>=1`, put

```tex
a+u=s(a+1)+p,\qquad j=sc+j_0.
```

Then

```tex
\frac{c(a+u)}{a+1}<j<\frac{r(a+u)}a,
```

so these points lie in the slack cone.  The whole translated base strip is
available once

```tex
\sigma\ge s\{h(a+1)+c\}-1.
```

The exact initial phase before the first translated strip,

```tex
0\le\sigma<h(a+1)+c-1,
```

is checked by

```text
python scripts\diagonal_nonreciprocal_initial_phase.py 700
```

with output

```text
checked=32645089
bad=0
best=(5, 107, 0, 107, 6, 16, 11, 35)
```

The translated strips themselves were checked by

```text
python scripts\diagonal_nonreciprocal_translated_base.py 500 --s-max 20
```

The raw gate check reports failures before the first translated strip, as
expected, but the increment check has no failures:

```text
checked_increment=668420
increment_bad=0
increment_best=(5, 95, 6, 14, 11, 8, 30)
```

This suggests a global non-reciprocal slack strategy:

1. prove the initial phase by a base-plus-partial-cone estimate;
2. prove each translated base strip contributes at least the target increase
   over the next interval of length `h(a+1)+c`.

## General `c` staircase bands

A sharper general decomposition uses the exact lower-floor levels of the
slack cone.  Put `A=a+1`, and define

```tex
U_s=\left\lfloor\frac{(s+1)A-1}{c}\right\rfloor+1
\qquad(s\ge0).
```

For `s>=0`, set `U_{-1}=0` and

```tex
B_s=\left\{(u,j):
U_{s-1}+1\le u\le U_s,\quad
c+s+1\le j\le
\left\lfloor\frac{r(a+U_{s-1}+1)-1}{a}\right\rfloor
\right\}.
```

Every point of `B_s` lies in the intrinsic cone

```tex
\frac{c(a+u)}{a+1}<j<\frac{r(a+u)}a.
```

The whole band is available at slack

```tex
\theta_s=hU_s+
\left\lfloor\frac{r(a+U_{s-1}+1)-1}{a}\right\rfloor-r.
```

The exact band-gate checker

```text
python scripts\diagonal_nonreciprocal_band_check.py 1000 --s-max 20
```

gives

```text
checked=3024105
bad=0
best=(8, 102, 2, 37, 28, 0, 39, 31)
```

and the wider early-band check

```text
python scripts\diagonal_nonreciprocal_band_check.py 500 --s-max 40
```

gives

```text
checked=1370261
bad=0
best=(8, 102, 2, 37, 28, 0, 39, 31)
```

This is currently the most promising route for the whole `c>=2` slack
sector.  It replaces fixed row averages by disjoint rectangles whose lower
edge follows the exact staircase of the cone.

The same checker can certify bands by a finite Mobius rectangle lower bound.
For a band rectangle `R`, the exact primitive count is

```tex
\sum_d \mu(d)N_u(d)N_j(d),
```

where `N_u(d)` counts `u` in the band with `a+u==0 mod d`, and `N_j(d)`
counts multiples of `d` in the `j` interval.  Truncating at `T` and
subtracting the raw tail gives a proof-grade lower certificate.

With cutoff `T=500`,

```text
python scripts\diagonal_nonreciprocal_band_check.py 1000 --s-max 20 --mobius-cutoff 500
```

has no Mobius-certificate failures:

```text
checked=3024105
bad=0
best=(8, 102, 2, 37, 28, 0, 39, 31)
mobius_bad=0
mobius_best=(8, 102, 2, 37, 28, 0, 39, 31)
```

Cutoffs much smaller than this still fail because the raw tail bound is too
loose, not because the exact band count is close to failing.

The dual-discrepancy idea that works for `c=1` was tested on these
staircase rectangles by

```text
python scripts\diagonal_nonreciprocal_band_dual.py 300 --s-max 20
```

Here each band is lower-bounded by the better of

```tex
W\sum_{j=j_0}^{j_1}\frac{\phi(j)}j-\sum_{j=j_0}^{j_1}\tau(j)
```

and

```tex
H\sum_{p=p_0}^{p_1}\frac{\phi(p)}p-\sum_{p=p_0}^{p_1}\tau(p).
```

The exact counts still have no failures, but the dual discrepancy
certificate is much too weak:

```text
checked=226506
exact_bad=0
exact_best=(8, 102, 2, 37, 28, 0, 39, 31)
dual_bad=117152
```

The worst false negatives occur in thin `h=2` high-band cases.  Thus the
general `c>=2` proof should not be based on divisor-discrepancy over one
rectangle side alone; it needs the Mobius rectangle certificate or a sharper
family-specific argument.

The Mobius cutoff profile also identifies the tail obstruction.  For
`q<=300`, cutoff `200` certifies all gates, while cutoffs `50` and `100`
produce many false negatives.  For `q<=500`, cutoff `300` certifies all
gates, while cutoff `200` still fails.  For `q<=1000`, cutoff `400` fails
in the thin `h=1`, `a\approx q/2`, `r\approx a-2` family, while cutoff
`500` was previously enough.  These failures are tail-bound artifacts: in
the typical hard row

```tex
(q,h,a,r,s)=(1000,1,501,499,20),
```

the band is only

```tex
u=22,\qquad 518\le j\le520,
```

with exact band count `3`, and the cumulative exact margin is `263`.
The truncated Mobius lower bound is negative only because the raw tail
subtracts too much.

The tail issue is largely solved by replacing the raw tail with the exact
rectangle tail.  In `band_mobius_lower`, the old tail used

```tex
\sum_{d>T}\left\lceil\frac{W}{d}\right\rceil
\left\lceil\frac{H}{d}\right\rceil,
```

which ignores the congruence condition `a+u\equiv0\pmod d`.  The new
`--exact-tail` option instead subtracts

```tex
\sum_{d>T}
\#\{u:u\equiv-a\pmod d\}
\#\{j:j\equiv0\pmod d\},
```

still with adversarial signs for the unknown Mobius tail.  This is a valid
lower bound, but is much sharper in thin rectangles.

With this exact tail, the finite certificates become small-head Mobius
certificates:

```text
python scripts\diagonal_nonreciprocal_band_check.py 1000 --s-max 20 --mobius-cutoff 1 --exact-tail
checked=3024105
bad=0
mobius_bad=0
mobius_best=(2, 134, 1, 89, 45, 20, 54, 52)
```

For wider staircase depth,

```text
python scripts\diagonal_nonreciprocal_band_check.py 500 --s-max 40 --mobius-cutoff 5 --exact-tail
checked=1370261
bad=0
mobius_bad=0
mobius_best=(1, 269, 1, 178, 91, 40, 103, 102)
```

and cutoff `10` in the same box restores the exact best margin `8`.  Thus
the promising `c>=2` proof target is now a small-head Mobius inequality with
an exact divisor-tail union bound, rather than a large raw-tail cutoff.

In lemma form, for any rectangle

```tex
R=[u_0,u_1]\times[j_0,j_1],
\qquad P_R=\#\{(u,j)\in R:(a+u,j)=1\},
```

Mobius inversion and adversarial tail signs give, for every `T>=1`,

```tex
P_R\ge
\sum_{d\le T}\mu(d)
N_u(d)N_j(d)
-
\sum_{d>T}N_u(d)N_j(d),                 \tag{4}
```

where

```tex
N_u(d)=\#\{u_0\le u\le u_1:a+u\equiv0\pmod d\},
\qquad
N_j(d)=\#\{j_0\le j\le j_1:j\equiv0\pmod d\}.
```

The `T=1` case is especially simple:

```tex
P_R\ge |R|-\sum_{d\ge2}N_u(d)N_j(d).     \tag{5}
```

This is a union bound over possible common divisors, but unlike the old raw
tail it preserves the exact congruence positions of the rectangle.  The
checks above show that (5), accumulated over staircase bands, already
certifies `q<=1000`, `s<=20`, while adding only `d<=5` certifies the deeper
`q<=500`, `s<=40` box.

This points to a separate `h=1` treatment.  An exact scan restricted to
`h=1`, `q<=1000`, and staircase gates through `s<=40` gives

```text
rows=3228750
best_base=(11, (95, 62, 33, 31, 38, 27))
best_gate=(13, 94, 55, 39, 37, 0, 41, 28, (1, 2, 38, 39))
```

So the thin family that defeats the Mobius tail is not close to the target
inequality: the base strip already has surplus at least `11` in this range,
and the staircase gate surplus is at least `13`.  A plausible final split is:

1. prove the `h=1` non-reciprocal sector directly using base surplus plus
   elementary bounds for the small staircase bands;
2. apply the Mobius rectangle certificate only for `h>=2`, where the
   problematic one-column tail family disappears or is much less severe.

The focused `h=1` scanner is

```text
python scripts\diagonal_nonreciprocal_h1_tail_scan.py 300 --s-max 40 --mobius-cutoff 5
```

with output

```text
checked=258587
base_best=(11, 95, 62, 33, 31, 38)
exact_bad=0
exact_best=(13, 94, 55, 39, 37, 0, 41, (1, 2, 38, 39))
lower_bad=0
lower_best=(1, 269, 178, 91, 89, 40, 103, (82, 83, 130, 132))
```

For deeper `h=1` bands, cutoff `5` is not enough, but cutoff `10` certifies
the larger box:

```text
python scripts\diagonal_nonreciprocal_h1_tail_scan.py 500 --s-max 80 --mobius-cutoff 10
checked=1533411
exact_bad=0
lower_bad=0
lower_best=(11, 98, 65, 33, 31, 1, 41, (4, 5, 33, 35))
```

So the `h=1` exact-tail head appears to grow with staircase depth rather
than with `q`; this is consistent with the one-column/short-height geometry
of the worst bands.

## Proof-ready gate formulation

The current non-reciprocal slack branch can be organized as a gate theorem.
For every valid tuple

```tex
q=ha+r,\qquad r=h+1+c,\qquad r<a,\qquad (a,r)=1,\qquad (a+1,c)=1,
```

write

```tex
B_{q+\sigma}=C_0+G_\sigma,
```

where

```tex
C_0=
\#\{(p,j):1\le p\le a,\ cp/(a+1)<j<rp/a,\ (p,j)=1\}
```

and

```tex
G_\sigma=
\#\{(u,j):u\ge1,\ c(a+u)/(a+1)<j<r(a+u)/a,\ 
0\le hu+j-r\le\sigma,\ (a+u,j)=1\}.
```

For `c>=2`, put `A=a+1`, `U_{-1}=0`, and

```tex
U_s=\left\lceil\frac{(s+1)A}{c}\right\rceil
=\left\lfloor\frac{(s+1)A-1}{c}\right\rfloor+1.
```

The staircase rectangle

```tex
\mathcal B_s=
\{(u,j):
U_{s-1}+1\le u\le U_s,\quad
c+s+1\le j\le
\lfloor(r(a+U_{s-1}+1)-1)/a\rfloor\}
```

lies in the cone and is complete once

```tex
\Theta_s=hU_s+\lfloor(r(a+U_{s-1}+1)-1)/a\rfloor-r.
```

Let

```tex
P_s=\#\{(u,j)\in\mathcal B_s:(a+u,j)=1\}.
```

Thus a sufficient theorem for all `c>=2` slack is:

```tex
C_0+\sum_{s=0}^S P_s\ge D(q+\Theta_{S+1}-1)
\qquad(S\ge0),
```

after the initial phase `0<=sigma<Theta_0` is covered.  Monotonicity then
proves `B_{q+\sigma}\ge D(q+\sigma)` for every `sigma>=0`.

The exact rectangle count has the Mobius form

```tex
P_s=\sum_d\mu(d)N_u(d)N_j(d),
```

where `N_u(d)` counts `u` in the band with `a+u==0 mod d` and `N_j(d)`
counts multiples of `d` in the `j` interval.  A proof-grade lower bound is

```tex
P_s\ge
\sum_{d\le T}\mu(d)N_u(d)N_j(d)
-
\sum_{T<d\le j_{\max}}
\left\lceil\frac{W_s}{d}\right\rceil
\left\lceil\frac{H_s}{d}\right\rceil,
```

with `W_s` and `H_s` the rectangle width and height.  The remaining analytic
lemma is to choose `T` and show this lower bound pays the assigned
`D`-increment outside a finite box.

For `c=1`, the same gate structure uses the capped core

```tex
1\le u\le \min(a,\lfloor\sigma/h\rfloor),\qquad 2\le j\le h+2,
```

and, for large slack, the shifted blocks

```tex
\mathcal Q_k=
\{(u,j):k(a+1)+1\le u\le(k+1)(a+1),\quad
k+2\le j\le(k+1)(h+2)\}.
```

The first large-slack gap is handled by `C_0+Q_0`; every later gap follows
if

```tex
Q_k\ge D(q+\Lambda_{k+1}-1)-D(q+\Lambda_k-1)\qquad(k\ge1),
```

where

```tex
\Lambda_k=(k+1)h(a+1)+(k+1)(h+2)-(h+2).
```

The remaining `c=1` analytic inequality is the first-gap lower bound

```tex
aM_h-T_h+(a+1)A_h-E_h\ge D(3h(a+1)+h+3),
```

apart from the finite box already checked exactly.
