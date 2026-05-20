# Non-reduced unit-step `H>=2`: buffered four-band drift draft

Date: 2026-05-12

This note attacks the remaining non-reduced unit-step edge family from
`unit-step-Hge2-edge-reduction.md`.  It does not solve the branch.  The aim
is to turn the observed negative four-band drift blocks into analytic proof
obligations that are small enough to attack by hand or by a finite CRT
certificate.

## Setup

Use the abstract variables

```tex
K=gx,\qquad G=gy,\qquad A=G-K=g(y-x).
```

The edge hypotheses become

```tex
A\ge2,\qquad h=(K,A)\ge2,\qquad K/h\ge2,\qquad (K-1,A+2)=1.
```

For numerator offset `u`, put

```tex
\alpha_u=\left\lfloor { (A-1)u\over K}\right\rfloor,\qquad
\beta_u=\left\lfloor { (A+2)u+2K+A-1\over K-1}\right\rfloor.
```

The completed `u`-band is

```tex
C_u=
\#\{j:\alpha_u\le j\le\beta_u,\ (K+u,A+j)=1\}.       \tag{1}
```

This is just the `s`-interval formula with `s=u+j`, since

```tex
(K+u,K+A+s)=(K+u,K+A+u+j)=(K+u,A+j).
```

Let

```tex
b_u=u+\beta_u,\qquad
D(n)=\left\lfloor {n\over4}\right\rfloor+\delta_{n\bmod4},
\quad
(\delta_0,\delta_1,\delta_2,\delta_3)=(1,2,2,4).
```

The local four-band margin at `t` is

```tex
\Lambda_t=
\sum_{i=0}^3 C_{t+i}
-
\bigl(D(G+b_{t+4})-D(G+b_t)\bigr).                  \tag{2}
```

The unbuffered lemma `\Lambda_t\ge0` is false.  The first checked
counterexample in the targeted box is

```tex
K=2270,\qquad A=488,\qquad t=28,
```

where `\Lambda_t=-1`.  The cumulative margin before the block is nevertheless
`1579`.

Define that cumulative buffer by

```tex
M_t=S_0+\sum_{u=0}^{t-1}C_u-D(G+b_t),                \tag{3}
```

where `S_0` is the exact minimal-order lower subcertificate from the
`p\le K` strip.  A sufficient post-early-band theorem is:

```tex
M_t+\Lambda_t\ge0\qquad(t\ge21).                     \tag{4}
```

The proof target is therefore not local monotonicity, but buffered drift.

## Proved reduction: constant-floor length-three blocks

The first and most common negative blocks found by the scanners have a
rigid floor shape:

```tex
\alpha_t=\alpha_{t+1}=\cdots=\alpha_{t+4}=m,
```

and

```tex
\beta_t=\beta_{t+1}=\beta_{t+2}=\beta_{t+3}=m+2,\qquad
\beta_{t+4}=m+3.                                    \tag{5}
```

In this case set

```tex
p=K+t,\qquad r=A+m.
```

Then each of the four completed bands has the same three residue candidates,
but modulo four consecutive moduli:

```tex
C_{t+i}
=\#\{0\le j\le2:\ (p+i,r+j)=1\},\qquad 0\le i\le3. \tag{6}
```

Also

```tex
G+b_t=p+r+2,\qquad G+b_{t+4}=p+r+7.
```

Thus (2) becomes the purely local residue inequality

```tex
B(p,r)\ge T(p,r),                                   \tag{7}
```

where

```tex
B(p,r)=\sum_{i=0}^3\sum_{j=0}^2 1_{(p+i,r+j)=1},
```

and

```tex
T(p,r)=D(p+r+7)-D(p+r+2)
=
\begin{cases}
3,&p+r\equiv0\pmod4,\\
-1,&p+r\equiv1\pmod4,\\
2,&p+r\equiv2\pmod4,\\
1,&p+r\equiv3\pmod4.
\end{cases}                                      \tag{8}
```

This proves two useful facts.

1. Any constant-floor length-three local deficit has absolute size at most
   `3`, because `0\le B(p,r)` and `T(p,r)\le3`.
2. The residue class `p+r\equiv1 mod 4` is automatically harmless because
   the gate target is negative.
3. The hard residue class is `p+r\equiv0 mod 4`, where the four length-three
   windows must produce at least three primitive cells.

The floor pattern (5) is equivalent to the following integer inequalities:

```tex
mK\le(A-1)t,\qquad
(A-1)(t+4)\le(m+1)K-1,                              \tag{9}
```

```tex
(m+2)(K-1)\le(A+2)t+2K+A-1,
```

```tex
(A+2)(t+3)+2K+A-1\le(m+3)(K-1)-1,
```

```tex
(m+3)(K-1)\le(A+2)(t+4)+2K+A-1,
```

```tex
(A+2)(t+4)+2K+A-1\le(m+4)(K-1)-1.                  \tag{10}
```

From (9), a necessary condition is

```tex
4m<t.                                               \tag{11}
```

Indeed, (9) gives
`mK(t+4)/t <= (A-1)(t+4) < (m+1)K`, hence
`m/t < (m+1)/(t+4)` and therefore `4m<t`.  This agrees with every negative
realization seen by the scanners and is a useful first pruning inequality.

## CRT form of the local obstruction

For a target-three block, negativity means `B(p,r)\le2`, so at least ten of
the twelve cells

```tex
(i,j)\in\{0,1,2,3\}\times\{0,1,2\}
```

are nonprimitive.  For each nonprimitive cell choose a prime

```tex
\ell_{ij}\mid(p+i,r+j).
```

Equivalently,

```tex
p\equiv-i\pmod{\ell_{ij}},\qquad
r\equiv-j\pmod{\ell_{ij}}.                          \tag{12}
```

Thus every negative constant-floor block lies in one of finitely many CRT
templates obtained by assigning primes to at least ten cells, subject to the
compatibility condition

```tex
i\equiv i'\pmod\ell,\qquad j\equiv j'\pmod\ell
```

whenever the same prime `\ell` is assigned to two cells.  Because
`0\le i\le3` and `0\le j\le2`, all repeated-prime interactions are confined
to `\ell=2` and `\ell=3`, except for identical row/column positions.

This is a genuine finite covering problem: prove that every compatible CRT
template either

```tex
B(p,r)\ge T(p,r),
```

or else forces `p` into a large lower range where the buffer estimate below
dominates the possible deficit.

The current pure residue scan gives the first target-three obstructions

```text
p=1308, r=644, B=1, counts=(0,1,0,0),
p=1944, r=944, B=2, counts=(0,2,0,0),
p=2298, r=494, B=2, counts=(0,1,0,1),
p=2532, r=440, B=2, counts=(0,2,0,0).
```

The first two have no negative realizations in the checked floor window.
The first negative edge-realizable block is `p=2298,r=494`.

## Wider near-constant floor signatures

A broader negative-floor summary shows that the clean length-three statement
above is not the whole story.  The script

```text
python scripts\unit_step_hge2_negative_floor_summary.py 9000 --target3-mod --t-max 240 --alpha-window 180 --max-pure-records 120 --max-negative-records 400
```

finds `260` negative realizations.  All have

```text
target=3, p+r == 0 mod 4.
```

The dominant signature is still

```text
lengths=(3,3,3,3),
alpha_rel=(0,0,0,0,0),
beta_rel=(0,0,0,0,1),
```

with minimum pre-block buffer `1579`.  But negative blocks also occur with

```text
lengths=(3,3,3,4),
alpha_rel=(0,0,0,0,0),
beta_rel=(0,0,0,1,1),
```

and

```text
lengths=(3,3,3,4),
alpha_rel=(0,0,0,0,1),
beta_rel=(0,0,0,1,1),
```

and, later in the scan,

```text
lengths=(3,3,4,3),
alpha_rel=(0,0,0,1,1),
beta_rel=(0,0,1,1,1).
```

These wider signatures still have count `2`, target `3`, and a large
buffer; the smallest buffer among them in the run is `2319`.  Therefore the
right local lemma is not "all negative blocks are constant length three".
It should say that every negative block has a near-constant floor signature
from a finite list, with the exact local CRT problem attached to that
signature.

## Buffer lemma needed

The cleanest route now appears to be the following pair of lemmas.

**Lemma A: negative block structure.**  
If `\Lambda_t<0` for an admissible edge and `t\ge21`, then the block has one
of finitely many near-constant floor signatures, beginning with (5) and the
three wider signatures listed above.  In each signature the exact local
obstruction is a finite CRT problem over four consecutive moduli with
three- or four-point residue windows.  The observed local deficit is at most
`2`.

Status: proved only after assuming a given signature.  The missing part is
to prove that all other floor patterns have nonnegative local drift, or to
produce the finite complete signature list.  The scripts have checked this
in low-length windows, but there is no analytic proof yet.

**Lemma B: buffer before any local obstruction.**  
If an admissible edge realizes one of the negative CRT signatures, then

```tex
M_t\ge3.                                             \tag{13}
```

Together with Lemma A, this proves buffered drift at every negative block.
For all nonnegative blocks, (4) is automatic.

The data are much stronger than (13).  In the current targeted runs, the
smallest buffer before a negative block is

```text
M_t=1579
```

at `(K,A,t)=(2270,488,28)`.

The likely proof of Lemma B is:

1. Use the CRT templates plus the relevant floor inequalities to force a
   lower bound `p\ge p_0` for every negative realizable block.
2. Since `p=K+t` and `4m<t`, turn this into a lower bound for `K` in the
   negative range.
3. Prove a linear lower bound for the base/early-band certificate,

```tex
M_t\ge cK-Ct-C_0,                                    \tag{14}
```

with `cK-Ct-C_0\ge3` throughout the negative CRT range.

The hard analytic piece is (14).  The minimal strip has raw area of order
`K+A`, and the target `D(G+b_t)` has slope `1/4`, so a positive linear
surplus is plausible.  However, a proof needs a primitive-lattice lower
bound strong enough for the hard family `g=2`, `x` near `y/2`; the existing
Mobius certificate is still finite/computational rather than uniform.

## Concrete proof path

The strongest path suggested by the scripts is:

1. Prove the exact band formula (1) and use it as the only counting object.
2. Prove a large-band drift lemma: if one of the four bands has length at
   least `5`, then `\Lambda_t\ge0`, possibly after a short residue split.
3. Prove that every negative length-three/length-four block reduces to a
   finite list of near-constant floor CRT problems, with target `3` and
   `p+r\equiv0 mod 4`.
4. Produce a finite CRT certificate for all `p<p_0`, with realizability
   constraints (9)-(10) and exact target (8) included.
5. Prove the buffer lower bound (14) for `p\ge p_0`.

This would close the post-early-band drift without claiming false local
monotonicity.  The remaining gap is substantial: steps 2, 4, and 5 still
need proof-grade arguments.

## Commands checked while drafting

```text
python erdos/1005/scripts/unit_step_hge2_residue_bad.py 3000 --target3-mod --max-records 8 --stop-after-records --realizable --negative-realizations-only --t-max 120 --alpha-window 80 --buffer-realizations
```

This reproduced the first pure residue obstructions and showed the first
negative realizations at `p=2298,r=494`, all with large buffer.

```text
python erdos/1005/scripts/unit_step_hge2_four_band_buffer.py 2600 --k-min 2200 --a-min 300 --a-max 700 --t-start 21 --t-max 80 --max-band-length 4
```

Output summary:

```text
checked=2763720
negative=7
bad_buffer=0
worst_local=(-1, 1578, 1579, 2270, 488, 28, 2, 3, 3)
worst_buffer=(1578, -1, 1579, 2270, 488, 28, 2, 3, 3)
```
