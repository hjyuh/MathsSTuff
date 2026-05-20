# EP1005 non-reduced unit-step `H>=2` edge family

Date: 2026-05-11

This note records the sharper reduction of the non-reduced unit-step
obstruction to one explicit edge family.

## Minimal right endpoint

Let

```tex
\alpha=\frac{gx-1}{gy+1}<\frac xy,\qquad (x,y)=1,\quad g>1,
```

be the reduced unit-step setup.  Any bad endpoint to the right of `x/y` has

```tex
\beta=\frac cd,\qquad c\ge gx,\qquad d\le gy,\qquad \frac cd>\frac xy.
```

Writing `c=gx+u`, `d=gy-v`, with `u,v>=0`, gives

```tex
yc-xd=yu+xv>0.
```

If `v>=1`, then

```tex
\frac cd\ge \frac{gx}{gy-1}.
```

If `v=0`, then `u>=1`, and

```tex
\frac{gx+u}{gy}\ge \frac{gx+1}{gy}>\frac{gx}{gy-1},
```

because `g(y-x)>1`.  Therefore every non-reduced unit-step bad interval
contains

```tex
\frac{gx-1}{gy+1}<\frac{gx}{gy-1}.        \tag{1}
```

For `x=1`, this is the already closed `H=1` edge.  The remaining branch is
therefore the edge family (1) with `x>=2`.

## Exact count

The minimal Farey order for (1) is

```tex
n_0=gy+1.
```

For any `n>=n_0`, the edge interval has exact interior count

```tex
E_n(g,x,y)=
\sum_{p=1}^{\left\lfloor (gxn-1)/(gy-1)\right\rfloor}
\#\left\{q:
\left\lfloor\frac{(gy-1)p}{gx}\right\rfloor+1
\le q\le
\min\left(n,\left\lfloor\frac{(gy+1)p-1}{gx-1}\right\rfloor\right),
\ (p,q)=1
\right\}.                                  \tag{2}
```

This single row formula includes the central reduced fraction `x/y`.
At minimal order one can also use the lower subcertificate with `p<=gx`
obtained by splitting the interval at `x/y`; it is slightly weaker in some
small `y` ranges but agrees with the currently sharp checked examples.

The script

```text
python scripts\unit_step_hge2_edge_check.py 1000 --max-surplus 10
```

checks (2) for all admissible edge families with `92<=n_0<=1000`.  Output:

```text
checked=137602
bad=0
records=44
best=(7, 95, 34, 27, 2, 5, 47)
```

The same exact checker with `--scan-slack` checks every order between
`n_0` and the displayed limit.  Through `n<=300`, no slack order improves on
the minimal-order surplus:

```text
checked=929818
bad=0
records=0
best=(7, 95, 34, 27, 2, 5, 47)
```

So the sharp checked edge through these boxes is

```tex
\frac9{95}<\frac5{47}<\frac{10}{93},
```

with `E=34`, `D(95)=27`, and surplus `7`.

## Proof target

It remains to prove from (2), or from an equivalent primitive-lattice
triangle in determinant coordinates, that

```tex
E_n(g,x,y)>D(n)
```

for all

```tex
x\ge2,\qquad 0<x<y,\qquad (x,y)=1,\qquad g>1,
\qquad (gx-1,gy+1)=1,\qquad n\ge gy+1\ge92.
```

This would close the full non-reduced unit-step `H>=2` branch, because every
other bad endpoint to the right contains this edge interval.

## Periodicity at minimal order

For fixed

```tex
X=gx-1,\qquad P=X(X+1),
```

the minimal-order lower subcertificate is periodic-affine in `y`:

```tex
R_0(y+P)=R_0(y)+g\Phi(X),
```

where

```tex
\Phi(X)=\sum_{m=1}^X\phi(m).
```

Consequently, over `4P`,

```tex
\bigl(R_0(y+4P)-D(g(y+4P)+1)\bigr)
-
\bigl(R_0(y)-D(gy+1)\bigr)
=g(4\Phi(X)-X(X+1)).
```

The last quantity is positive for every admissible `X>=3`.  Thus for each
fixed `X` the minimal-order problem reduces to finitely many residue classes
`y mod 4X(X+1)`.  A direct residue-window check for `X<=25` found the same
minimum surplus `7` at `(g,x,y)=(2,5,47)`.

This does not yet close the branch.  The missing ingredient is a uniform
large-`X` bound over the finite residue window, plus a slack-in-`n` argument.
For example `(g,x,y)=(3,3,32)` has minimal-order surplus `8` at `n=97`, but
surplus `7` at `n=99`, so minimal order is not automatically worst.

The periodic-window checker is now

```text
python scripts\unit_step_hge2_periodic_check.py 40 --periods 4
```

It checks the `p<=gx` minimal-order subcertificate over the required
`4X(X+1)` window for every `X<=40`, with output:

```text
checked=92695
bad=0
best=(7, 9, 2, 5, 47, 95, 34, 27)
```

## Mobius subcertificate

For the minimal-order `p<=gx` strip, Mobius inversion gives

```tex
S_0(g,x,y)=\sum_{d\le gx}\mu(d)R_d(g,x,y),
```

where `R_d` is the raw count after dividing both coordinates by `d`.
The script

```text
python scripts\unit_step_hge2_edge_mobius.py 1000 --cutoff 512
```

certifies the same minimal-order range through `n<=1000`:

```text
checked=137602
exact_bad=0
exact_best=(7, 95, 2, 5, 47, 34, 27)
mobius_bad=0
mobius_best=(7, 95, 2, 5, 47, 34, 27)
```

Cutoff `256` is not enough through `n<=1000`; the failures are the expected
hard family `g=2`, `x` close to `y/2`, where the raw Mobius tail is too
coarse.  Thus the Mobius route is currently a finite certificate rather than
a clean asymptotic proof.

## Denominator slack

For fixed edge endpoints, the denominator-row count is

```tex
b_m(g,x,y)=
\#\left\{p:
\left\lfloor\frac{(gx-1)m}{gy+1}\right\rfloor+1
\le p\le
\left\lfloor\frac{gxm-1}{gy-1}\right\rfloor,\quad
(p,m)=1
\right\}.
```

Then

```tex
E_n(g,x,y)=\sum_{m\le n}b_m(g,x,y).
```

The slack-row checker is

```text
python scripts\unit_step_hge2_slack_rows.py 1000 --block 32 --need 8
```

Since `D(n+32)=D(n)+8`, this tested a candidate 32-row growth lemma.  Output:

```text
checked_surplus=44884050
surplus_bad=0
surplus_best=(7, 95, 34, 27, 2, 5, 47)
checked_growth=40614586
growth_bad=0
growth_best=(2, 223, 255, 10, 2, 3, 110, [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0])
```

Shorter fixed blocks are false in the checked range: 4-row growth fails by
`n<=300`, 8-row growth fails by `n<=500`, and 16-row growth fails by
`n<=700`.

The 32-row lemma is also false globally.  A targeted sparse-row example is

```tex
g=2,\qquad x=105,\qquad y=5251,\qquad n_0=10503.
```

For the 32 rows `m=n_0+1,...,n_0+32`, the row interval is the single
candidate `p=210` each time.  Only seven of those denominators are coprime
to `210`, so the block contributes `7<8=D(n_0+32)-D(n_0)`.  The theorem is
not threatened because the minimal-order surplus is large:

```text
E_{n0}=3385, D(n0)=2629, surplus=756,
E_{n0+32}-D(n0+32)=755.
```

Thus the slack proof cannot be a universal fixed-block growth lemma.  It
must use the minimal-order surplus as a buffer for sparse windows, then prove
long-run growth once row intervals widen.

The first sparse phase is explicit.  The candidate `p=gx` is present in row
`m` exactly when

```tex
m\ge gy,\qquad
m<\frac{gx(gy+1)}{gx-1}.
```

Thus after the minimal order `n_0=gy+1`, the single-numerator phase has
length at most

```tex
\left\lceil\frac{gx(gy+1)}{gx-1}\right\rceil-gy-2
\le
\frac{gy+gx}{gx-1}.
```

During this phase, the row contribution from this candidate is

```tex
1_{(gx,m)=1}.
```

This explains the sparse examples: if `gx` is highly composite, a short
window can have fewer primitive hits than the target slope `1/4`.  A viable
slack proof should therefore show that the minimal-order surplus dominates
the maximum possible early sparse-phase deficit, and then switch to a
long-run primitive-area or Mobius argument once additional numerator
candidates enter the rows.

The sparse-buffer checker is

```text
python scripts\unit_step_hge2_sparse_buffer.py 1000
```

and verifies the whole single-numerator phase through `n_0<=1000`:

```text
checked=137602
bad=0
best=(7, 95, 102, 95, 2, 5, 47, 34, 27)
```

The periodic sparse-buffer checker is

```text
python scripts\unit_step_hge2_sparse_periodic_check.py 40 --periods 4
```

and gives the finite-window certificate

```text
checked=92695
bad=0
best=(7, 8, 3, 3, 32, 97, 105, 99, 35)
```

This supports the same `4X(X+1)` finite-reduction pattern for the entire
single-numerator sparse phase, not only for minimal order.

The sparse-row counterexamples are systematic.  In the sparse phase, with
`K=gx` and `m=gy+s`,

```tex
\left\lfloor\frac{(K-1)m}{gy+1}\right\rfloor+1
=
K+\left\lfloor\frac{(K-1)(s-1)}{gy+1}\right\rfloor,
```

and

```tex
\left\lfloor\frac{Km-1}{gy-1}\right\rfloor
=
K+\left\lfloor\frac{K(s+1)-1}{gy-1}\right\rfloor.
```

For example, `g=2`, `x=105`, `y=3571` gives `K=210`, `n_0=7143`, and the
first 32 slack rows have only the candidate `p=210`.  They contribute exactly
seven primitive rows because the residues `4,5,...,35 mod 210` have only
seven numbers coprime to `210`.

## Numerator-offset bands

After the sparse phase, a better certificate groups by numerator offset

```tex
p=gx+t,\qquad m=gy+s.
```

Let `K=gx`, `B=gy+1`, and `D=gy-1`.  The offset `t>=0` is admissible for
exactly the rows

```tex
s_{\min}(t)\le s\le s_{\max}(t),
```

where

```tex
s_{\min}(t)=
\max\left(2,\left\lfloor\frac{Dt-K}{K}\right\rfloor+1\right),
```

and

```tex
s_{\max}(t)=
\left\lfloor\frac{gy+K+Bt-1}{K-1}\right\rfloor.
```

The contribution of the full `t`-band is therefore

```tex
\#\{s_{\min}(t)\le s\le s_{\max}(t):(K+t,gy+s)=1\}.
```

The exact checker

```text
python scripts\unit_step_hge2_t_band_check.py 500 --t-max 20
```

has no failures for the first 20 completed offset bands:

```text
checked=690879
exact_bad=0
exact_best=(5, 131, 3, 2, 31, 0, 41, 36)
```

Each `t`-band also has an exact finite Mobius formula:

```tex
\#\{s_{\min}\le s\le s_{\max}:(K+t,gy+s)=1\}
=
\sum_{d\mid K+t}\mu(d)
\#\{s_{\min}\le s\le s_{\max}:gy+s\equiv0\pmod d\}.
```

The Mobius-enabled checker

```text
python scripts\unit_step_hge2_t_band_check.py 1000 --t-max 20 --mobius
```

certifies the first 20 completed offset bands through `n<=1000`:

```text
checked=2889642
exact_bad=0
exact_best=(5, 131, 3, 2, 31, 0, 41, 36)
mobius_bad=0
mobius_best=(5, 131, 3, 2, 31, 0, 41, 36)
```

The simple reduced-residue discrepancy bound for each short band is too weak,
but the exact Mobius interval formula is proof-grade for finite reductions.

Empirically, the completed-band minimum occurs early.  The drift checker

```text
python scripts\unit_step_hge2_t_drift_check.py 500 --early-t 20 --t-max 100
```

reports

```text
checked=32899
late_min=0
best_all=(5, 0, 131, 3, 2, 31)
best_late=(74, 21, 141, 2, 24, 47)
```

So through this box, no edge has its completed-band minimum after `t=20`;
after that point the surplus is already much larger.  A useful proof target
is therefore a drift lemma showing that completed `t`-band surplus is
nondecreasing, or at least cannot drop below its first 20-band minimum, once
`t>20`.

Per-band drift is false: individual later offset bands can be empty.  But
grouped drift over four consecutive offset bands appears to be the right
statement.  The checker

```text
python scripts\unit_step_hge2_t_increment_check.py 700 --t-start 21 --t-max 100 --block 4
```

reports

```text
checked=5294000
bad=0
best=(0, 411, 2, 169, 178, 46, 3, 3)
```

Thus, in the checked range, every four completed offset bands after `t=20`
pay for the target increase to the next four-band gate.  This explains why
the completed-band minimum is always attained in the early `t<=20` range.

The tight four-band cases are highly structured.  The pattern classifier

```text
python scripts\unit_step_hge2_t_increment_patterns.py 700 --t-start 21 --t-max 120 --max-count 3
```

finds only the length patterns

```text
lengths=(3, 3, 3, 3)
lengths=(3, 3, 3, 4)
```

among blocks with total count at most `3`.  The observed low-count patterns
are

```text
(1,0,2,0), (0,0,1,2), (0,3,0,0), (0,0,3,0),
(0,1,2,0), (2,0,1,0), (0,2,0,1).
```

This suggests a route for the four-band drift proof: show that if the four
band lengths are outside this tiny family, then the block has surplus, and
handle the listed residue patterns directly.

The exact band length is

```tex
L_t=
\left\lfloor\frac{(gy+1)t+gy+gx-1}{gx-1}\right\rfloor
-
\left\lfloor\frac{(gy-1)t}{gx}\right\rfloor
+1.
```

The exact equality case for the four-band drift is rare in the tested range.

```text
python scripts\unit_step_hge2_t_increment_patterns.py 700 --t-start 21 --t-max 120 --max-count -1 --max-margin 0
```

finds only

```text
lengths=(3, 3, 3, 3), counts=(0, 0, 1, 2), target=3, margin=0
```

at `(g,x,y,t)=(2,169,178,46)`.  This suggests an even sharper local lemma:
the four-band increment is always nonnegative, with equality only in a small
residue pattern.

The local residue verifier

```text
python scripts\unit_step_hge2_four_band_local.py 700 --t-start 21 --t-max 120 --max-margin 0
```

finds exactly one local equality configuration:

```text
lengths=(3, 3, 3, 3)
counts=(0, 0, 1, 2)
starts=(20, 20, 20, 20)
target=3
margin=0
```

Here `starts` means the first denominator in each short interval, reduced
modulo its corresponding numerator modulus `gx+t+i`.

The naive reduced-residue discrepancy estimate does not prove this local
lemma.  Even for moderate band lengths, the `tau(gx+t)` losses swamp the
short intervals.  The exact proof target is therefore a residue lemma for the
four fixed moduli

```tex
gx+t,\quad gx+t+1,\quad gx+t+2,\quad gx+t+3
```

over their corresponding short `s` intervals.  The scans above show that the
only hard cases are the low-length patterns listed here; all wider patterns
have visible surplus in exact checks.

## Abstract four-band variables

The four-band drift lemma is cleaner after eliminating the original
`(g,x,y)` variables.  Put

```tex
K=gx,\qquad G=gy,\qquad A=G-K=g(y-x).
```

Then the edge admissibility conditions become

```tex
A\ge2,\qquad g=(K,A)\ge2,\qquad K/g\ge2,\qquad (K-1,K+A+1)=1.
```

For `u>=21`, the completed numerator-offset band has

```tex
a_u=u+\left\lfloor\frac{(A-1)u}{K}\right\rfloor,\qquad
b_u=u+\left\lfloor\frac{(A+2)u+2K+A-1}{K-1}\right\rfloor,
```

and contributes

```tex
C_u=\#\{a_u\le s\le b_u:(K+u,K+A+s)=1\}.
```

Thus the exact post-`t=20` drift target is the purely local inequality

```tex
C_t+C_{t+1}+C_{t+2}+C_{t+3}
\ge D(K+A+b_{t+4})-D(K+A+b_t).             \tag{3}
```

The proof-search script

```text
python scripts\unit_step_hge2_four_band_abstract.py 800 --a-max 200 --t-max 160 --max-band-length 4 --max-records 10
```

checks this exact inequality in the low-band-length range and reports

```text
checked=3632210
skipped_length=1872170
bad=0
best=(0, 338, 18, 46, 3, 3, (3, 3, 3, 3), (0, 0, 1, 2))
```

A wider low-length run

```text
python scripts\unit_step_hge2_four_band_abstract.py 1200 --a-max 220 --t-max 180 --max-band-length 4 --max-total 3 --max-records 30
```

also has no failures:

```text
checked=8236705
skipped_length=2634495
bad=0
best=(0, 338, 18, 46, 3, 3, (3, 3, 3, 3), (0, 0, 1, 2))
```

This corrected an overinterpretation of the earlier `n<=700` scan.  The
equality at `(K,A,t)=(338,18,46)` is not globally unique; later equality
blocks occur, for example at `(K,A,t)=(763,77,131)`, `(772,78,122)`,
`(792,80,102)`, and the same local residue block

```tex
K+t=894,\qquad K+A+a_t\equiv90\pmod{894}
```

with count pattern `(1,2,0,0)`.  The right theorem is therefore not
uniqueness of one equality case, but a local inequality (3), with equality
allowed in a sparse family of CRT-like residue blocks.

A tempting stronger surrogate is false: four length-three windows over
moduli `p,p+1,p+2,p+3` need not contain three primitive residues.  For
example `p=1953`, residues `68,69,70` give only two primitive hits.  This
does not contradict (3); in the realizable edge case
`(K,A,t)=(1932,68,21)` the target increment is only `1`.  Any proof of
(3) must therefore use the gate increment
`D(K+A+b_{t+4})-D(K+A+b_t)`, not just a uniform coprime-window lower bound.

Including length-five bands in the abstract search did not introduce new
equality in the tested box:

```text
python scripts\unit_step_hge2_four_band_abstract.py 700 --a-max 180 --t-max 140 --max-band-length 5 --max-total 4
checked=3239749
skipped_length=450131
bad=0
best=(0, 338, 18, 46, 3, 3, (3, 3, 3, 3), (0, 0, 1, 2))
```

The first low-total length-five cases have positive margin.  This supports a
case split in which the genuinely tight CRT analysis is confined to
length-three and length-four windows, while wider bands should be handled by
a coarser lower bound.

## Four-band drift counterexample

The unbuffered four-band drift lemma is false globally.  A valid edge tuple is

```tex
K=2270,\qquad A=488,\qquad t=28,
```

equivalently

```tex
g=2,\qquad x=1135,\qquad y=1379.
```

It satisfies

```tex
(K,A)=2,\qquad K/(K,A)=1135\ge2,\qquad (K-1,A+2)=1.
```

For the four bands `u=t,t+1,t+2,t+3`, the floor data are constant:

```tex
\alpha_u=\left\lfloor\frac{(A-1)u}{K}\right\rfloor=6,\qquad
\beta_u=\left\lfloor\frac{(A+2)u+2K+A-1}{K-1}\right\rfloor=8,
```

so each interval has residues

```tex
494,\quad 495,\quad 496
```

modulo the four consecutive moduli

```tex
2298,\quad 2299,\quad 2300,\quad 2301.
```

The primitive counts are

```text
0, 1, 0, 1
```

because the gcds are

```text
2298: (2,3,2)
2299: (19,11,1)
2300: (2,5,4)
2301: (13,3,1)
```

The four-band count is therefore `2`.  But

```tex
N_t=K+A+t+\beta_t=2794,\qquad
N_{t+4}=2799,
```

and since `D(2799)-D(2794)=3`, the unbuffered drift margin is `-1`.

This does not threaten the edge inequality.  The minimal-order
subcertificate for this edge has

```text
base=2222, D(2759)=693, surplus=1529.
```

At the surrounding completed-band gates the cumulative surplus is still over
`1500`.  Thus the correct post-sparse theorem cannot be pure four-band
monotonicity.  It must be a buffered drift statement:

```tex
\text{large accumulated surplus absorbs rare negative four-band increments.}
```

The revised task is to bound possible four-band deficits in terms of the
minimal/sparse/early-band surplus, or to prove monotonicity only in the
near-tight region where the accumulated surplus is small.  The previous
four-band equality scans remain useful for identifying the near-tight
region, but they are not a global theorem.

The counterexample is reproduced by

```text
python scripts\unit_step_hge2_four_band_abstract.py 2280 --k-min 2260 --a-min 480 --a-max 500 --t-start 21 --t-max 60 --max-band-length 4
checked=5320
bad=1
best=(-1, 2270, 488, 28, 2, 3, (3, 3, 3, 3), (0, 1, 0, 1))
```

The buffered version is checked by

```text
python scripts\unit_step_hge2_four_band_buffer.py 2280 --k-min 2260 --a-min 480 --a-max 500 --t-start 21 --t-max 60 --max-band-length 4
checked=5320
negative=1
bad_buffer=0
worst_local=(-1, 1578, 1579, 2270, 488, 28, 2, 3, 3)
worst_buffer=(1578, -1, 1579, 2270, 488, 28, 2, 3, 3)
```

Here `worst_local` records

```text
(local_margin, buffered_margin, before_margin, K, A, t, count, target, max_length).
```

So the local `-1` deficit is absorbed by pre-existing surplus `1579`.
Broader low-length buffered scans found no unabsorbed deficits:

```text
python scripts\unit_step_hge2_four_band_buffer.py 1600 --a-max 500 --t-start 21 --t-max 100 --max-band-length 4
checked=13656590
negative=0
bad_buffer=0

python scripts\unit_step_hge2_four_band_buffer.py 2500 --k-min 1600 --a-min 300 --a-max 700 --t-start 21 --t-max 100 --max-band-length 4
checked=8265600
negative=7
bad_buffer=0
worst_buffer=(1578, -1, 1579, 2270, 488, 28, 2, 3, 3)
```

The negative local patterns in this range are classified by

```text
python scripts\unit_step_hge2_negative_patterns.py 2500 --k-min 1600 --a-min 300 --a-max 700 --t-start 21 --t-max 100 --max-band-length 4 --buffer
checked=8265600
negative=7
patterns=2
worst_local=(-1, 1578, 1579, 2270, 488, 28, 2, 3, (3, 3, 3, 3), (0, 1, 0, 1), ...)
worst_buffer=(1578, -1, 1579, 2270, 488, 28, 2, 3, (3, 3, 3, 3), (0, 1, 0, 1))
```

The only observed negative patterns have

```text
lengths=(3,3,3,3), target=3, local margin=-1,
counts=(0,1,0,1) or counts=(0,2,0,0).
```

In every sample, the residue start is constant across the four moduli and
the floor data are constant across the block.  The two residue blocks seen
are:

```text
start=494, gcd rows
(2,3,2), (19,11,1), (2,5,4), (13,3,1)

start=440, gcd rows
(4,3,2), (1,1,17), (2,7,2), (5,3,13)
```

Thus the likely buffered proof can split negative blocks into a small CRT
family of constant-floor length-three patterns and then show these patterns
force large `K,A` and hence large accumulated surplus before the block.

The pure CRT obstruction can be separated from edge realizability using

```text
python scripts\unit_step_hge2_residue_bad.py 2600 --target3-mod --max-records 4 --realizable --t-max 120 --alpha-window 40
```

The first pure residue block is

```text
p=1308, R=644, counts=(0,1,0,0).
```

It is edge-realizable, but all displayed realizations have nonnegative local
drift because the actual target increment is `0` or `1`.  The next pure
block

```text
p=1944, R=944, counts=(0,2,0,0)
```

is similarly harmless in the displayed realizations.  The first residue
blocks that produce actual negative edge drift are

```text
p=2298, R=494, counts=(0,1,0,1),
p=2532, R=440, counts=(0,2,0,0).
```

Their realizations include the local `-1` blocks listed above.  This
explains why a proof cannot look only at pure four-modulus CRT obstructions:
the floor geometry and the exact `D`-increment filter out earlier residue
blocks.

The residue script can also list pure CRT obstructions quickly:

```text
python scripts\unit_step_hge2_residue_bad.py 10000 --target3-mod --max-records 25 --stop-after-records
```

The first records include repeated small-divisor templates such as

```text
(2,3,2), ..., (2,5,4), ...
```

for the two zero-count rows.  This supports treating the local obstruction
as a finite CRT covering problem.  However, several early pure CRT
obstructions are filtered out by the edge floor data and the exact target
increment, so the proof must keep the realizability and `D`-increment
conditions.

A broader residue-realizability run shows that the two-pattern list above is
not a global classification; it is only what appears in that verified
high-`K` box.  Running

```text
python scripts\unit_step_hge2_residue_bad.py 10000 --target3-mod --max-records 25 --stop-after-records --realizable --negative-realizations-only --t-max 160 --alpha-window 80
```

finds additional negative count patterns such as `(0,1,1,0)` and
`(0,0,1,1)`.  Extending to `50` pure CRT records also finds local margin
`-2`, for example

```text
p=6354, R=650, counts=(0,1,0,0).
```

The first displayed negative realizations include

```text
(K,A,t)=(6174,632,180), (6183,633,171), (6212,636,142),
```

all with target `3`, count `1`, and local margin `-2`.  The common
structural shape still persists:

```text
lengths=(3,3,3,3), target=3,
constant floor data across the four bands.
```

Sample cumulative buffers are large:

```text
(K,A,t)=(2270,488,28):  before_margin=1579
(2508,436,24):          before_margin=1721
(3220,414,158):         before_margin=2414
(3594,372,24):          before_margin=2442
(4406,154,24):          before_margin=2958
(4704,958,138):         before_margin=3394
(5036,626,148):         before_margin=3613
(6116,1250,118):        before_margin=4307
(6174,632,180):         before_margin=4413
(6183,633,171):         before_margin=4402
(6212,636,142):         before_margin=4366
```

Thus the emerging theorem is not a finite list of two CRT patterns.  It is a
structural statement: negative local blocks have the constant-floor
length-three form, and the arithmetic needed to force such a block appears
only after the edge has already accumulated a large surplus.

The current summary scanner is

```text
python scripts\unit_step_hge2_negative_summary.py 20000 --target3-mod --t-max 200 --alpha-window 120 --max-pure-records 100 --max-negative-records 200
```

with output

```text
pure_records=59
negative_records=200
min_buffer=(1579, -1, 2270, 488, 2, 28, 2, 3, ...)
worst_local=(4287, -2, 6300, 645, 15, 54, 1, 3, ...)
```

The count-pattern distribution in these 200 negative realizations is

```text
95: (0, 1, 0, 1)
30: (0, 0, 1, 1)
29: (0, 1, 1, 0)
27: (0, 2, 0, 0)
7:  (0, 0, 0, 2)
6:  (0, 1, 0, 0)
6:  (1, 1, 0, 0)
```

The floor patterns are even more rigid than the count patterns: every top
pattern has

```tex
\alpha_t=\alpha_{t+1}=\cdots=\alpha_{t+4}=m,
```

and

```tex
\beta_t=\beta_{t+1}=\beta_{t+2}=\beta_{t+3}=m+2,\qquad
\beta_{t+4}=m+3.
```

So a proof-grade buffered drift lemma can aim to prove:

1. if a local four-band block is negative, then it has this constant-floor
   length-three structure and local deficit at most a small absolute
   constant;
2. this structure forces parameters large enough that the cumulative
   base/early-band certificate before the block exceeds that deficit.

## Combined finite certificate

The current edge-slack pieces can be checked together:

1. exact minimal-order count;
2. exact sparse-phase rows;
3. exact Mobius interval sums for completed numerator-offset bands.

The combined checker is

```text
python scripts\unit_step_hge2_combined_certificate.py 1000 --t-max 20
```

with output

```text
checked=3027244
bad=0
best=(9, 99, 3, 4, 31, -1, 37, 28)
```

The `t=-1` marker in the best row is the sparse-phase gate.  Thus in the
checked range, the handoff from sparse rows to completed offset bands has
positive margin.  The remaining task is a global finite reduction: show the
minimal/sparse periodic drift and enough completed offset bands reduce all
large parameters to a finite window.

The combined periodic-window checker is

```text
python scripts\unit_step_hge2_combined_periodic.py 30 --periods 4 --t-max 20
```

and gives

```text
checked=38389
bad=0
best=(7, 9, 2, 5, 47, 95, -2, 34, 27)
```

Here `marker=-2` denotes the minimal-order gate.  In this window, the
combined certificate is never tighter than the already-known minimal-order
case.
