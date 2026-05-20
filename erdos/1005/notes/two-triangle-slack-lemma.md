# EP1005 two-triangle slack lemma target

Date: 2026-05-11

This note isolates a simpler primitive-count lemma that would close
reciprocal diagonal slack for all `w>=1`.

## Setup

Recall

```tex
T(X,Y)=
\#\{(p,j):1\le p\le X,\ 1\le j\le Y,\ (p,j)=1,\ (Y+1)p>Xj\}.
```

For a reciprocal diagonal interval

```tex
q=ha+r,\qquad 1\le r\le h,\qquad n=q+\sigma,
```

write

```tex
\sigma=wh+t,\qquad 0\le t<h.
```

If `w>=1`, put

```tex
X=a+w.
```

Then the positive reciprocal rows contain the full primitive triangle
`T(X,r-1)`, and the negative reciprocal rows contain the full primitive
triangle `T(X,h-r)`. Therefore

```tex
B_n(a,q)\ge 1+T(X,r-1)+T(X,h-r).
```

Also

```tex
n=ha+r+wh+t=hX+r+t,\qquad 1\le r\le h,\quad 0\le t<h.
```

Thus it is enough to prove the independent lemma

```tex
1+T(X,r-1)+T(X,h-r)
\ge
\left\lfloor\frac{hX+r+t}{4}\right\rfloor
+d_{(hX+r+t)\bmod4}
```

for all admissible `h>=4`, `1<=r<=h`, `0<=t<h`, and `X=a+w`.

## Discrepancy bounds

Let

```tex
\Phi(X)=\sum_{m\le X}\phi(m),\qquad
\Tau(X)=\sum_{m\le X}\tau(m),
```

and

```tex
H(Y)=\sum_{j=1}^{Y}\frac{\phi(j)}j\left(1-\frac{j}{Y+1}\right).
```

The same reduced-residue discrepancy lemma used in the `H=1` proof gives

```tex
T(X,Y)\ge \frac{Y+1}{X}\Phi(X)-\Tau(X),
```

and

```tex
T(X,Y)\ge XH(Y)-\Tau(Y).
```

Consequently

```tex
1+T(X,r-1)+T(X,h-r)
\ge
1+\frac{h+1}{X}\Phi(X)-2\Tau(X)
```

and

```tex
1+T(X,r-1)+T(X,h-r)
\ge
1+X(H(r-1)+H(h-r))-\Tau(r-1)-\Tau(h-r).
```

The second bound, together with

```tex
H(r-1)+H(h-r)-h/4\ge h/100,
```

proves the lemma when `X` is large compared with `log h`. The first bound
proves it when `h` is large compared with the divisor error in `X`, except
for a few small `X` values where the leading coefficient is exactly tight.

A sharper exact check gives

```tex
H(r-1)+H(h-r)-h/4\ge h/24
```

for all checked `h>=4`, `1<=r<=h`, with the minimum at `h=4`. If this
inequality is promoted to a proof, the horizontal criterion becomes much
stronger:

```tex
\frac{Xh}{24}\ge \Tau(r-1)+\Tau(h-r)+\frac h2+3.
```

Together with the vertical bound, this should reduce the lemma to a finite
set of small `X`.

## Exact evidence

The checker

```text
python scripts\two_triangle_slack_check.py --max-x 500 --max-h 500
```

uses the admissibility conditions coming from reciprocal diagonal slack:

```tex
X\ge r+2,\qquad h(X-1)+r\ge92.
```

It verifies the two-triangle inequality in that box:

```text
checked=41537711
bad=0
best=(0, 4, 24, 4, -1, 29, 29)
```

Thus no counterexample appears through `X,h<=500`; the worst checked rows
are exact ties in the two-triangle lower bound, not failures.

The finite region forced by the vertical and horizontal analytic criteria is
larger. The compiled checker

```text
powershell -ExecutionPolicy Bypass -File scripts\two_triangle_slack_check.ps1 -XMax 168 -HMax 7800
```

verifies that whole box:

```text
checked=107351897
bad=0
minSurplus=0
minRow=h=4 X=24 r=4 lower=29 target=29 surplus=0
```

## Remaining work

The remaining proof-writing task is to justify rigorously that the vertical
and horizontal criteria reduce all cases to `X<=168`, `h<=7800`. The exact
box itself is now certified. Once this reduction is written cleanly, it closes
every reciprocal diagonal slack case with `w>=1`; the case `w=0` is exactly
the already-certified base-order reciprocal diagonal theorem.

## Proof-grade finite reduction plan

The exact box check above should be paired with the following purely finite
arithmetic verifications.

First, verify for all `X>=13` up to a cutoff `X_0` that

```tex
\frac{\Phi(X)}X-\frac{X+1}{4}\ge \frac X{50}.
```

For `X>X_0`, use the explicit summatory-totient lower bound already quoted in
`notes/unit-step-H1-proof-agent2.md` to continue the inequality. This gives
the vertical criterion

```tex
\frac{hX}{50}\ge 2\Tau(X)+\frac h4+4.
```

Second, verify for all `h` up to a cutoff `h_0` that

```tex
H(r-1)+H(h-r)-h/4\ge h/24
\qquad(1\le r\le h).
```

For larger `h`, this follows from the same fixed-cell fan estimates with
strict surplus; alternatively it can be made a finite certificate because the
left side is minimized at the edge `r=1` in all checked ranges. This gives the
horizontal criterion

```tex
\frac{Xh}{24}\ge \Tau(r-1)+\Tau(h-r)+\frac h2+3.
```

Finally, a deterministic arithmetic check verifies that for every

```tex
X\ge169\quad\text{or}\quad h\ge7801
```

at least one of the vertical or horizontal criteria holds. In the local
calculation this check used exact divisor sums up to `100000` and found that
the simultaneous failure region has

```tex
13\le X\le168,\qquad h\le7799.
```

Thus the compiled exact check with `XMax=168`, `HMax=7800` covers every
remaining case.

The arithmetic gate is checked by

```text
python scripts\two_triangle_reduction_check.py --limit 10000
```

with output

```text
bad_phi=0
bad_h=0
outside_fail=0
```

This verifies the required finite inequalities up to the cutoff used by the
box reduction. The continuation beyond the cutoff uses the same explicit
summatory-totient estimate cited in the `H=1` proof note.

## Large-parameter split

The vertical bound gives

```tex
1+T(X,r-1)+T(X,h-r)
\ge
1+\frac{h+1}{X}\Phi(X)-2\Tau(X).
```

Using

```tex
\frac{\Phi(X)}X-\frac{X+1}{4}\ge\frac X{50},
```

this exceeds the worst possible target

```tex
\max_{0\le t<h}D(hX+r+t)
\le \frac{hX}{4}+\frac h2+4
```

whenever

```tex
\frac{hX}{50}\ge 2\Tau(X)+\frac h4+4.
```

Thus, for every `X>=13`, all sufficiently large `h` are handled explicitly.
For fixed small `X`, the same two-triangle count has positive linear slope in
`h`; direct scans for `3<=X<=12` through `h<=2000` found positive surplus in
every admissible case, with minima:

```text
X=3:  surplus 12
X=4:  surplus 4
X=5:  surplus 8
X=6:  surplus 1
X=7:  surplus 6
X=8:  surplus 3
X=9:  surplus 4
X=10: surplus 0
X=11: surplus 3
X=12: surplus 0
```

The remaining proof-grade task is to replace these scans by periodic formulas
in `h` for the finite set `3<=X<=12`, and to run the exact finite check for
the remaining bounded region with `X>=13`.
