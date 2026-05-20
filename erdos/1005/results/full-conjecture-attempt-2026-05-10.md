# EP1005 full conjecture attempt

Date: 2026-05-10

Goal: prove the exact conjecture

```tex
f(n)=\left\lfloor\frac n4\right\rfloor+d_{n\bmod 4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4),
```

for all `n >= 92`.

## What is now proved locally

### 1. Central half-cell classification

If a bad interval

```tex
\frac ab<\frac12<\frac cd
```

is extremal for large `n`, then it must have

```tex
c-a=1,\qquad b-d=1.
```

The proof is in `notes/central-half-cell-lemma.md`. It counts the two
determinant-one fans around `1/2`:

```tex
\frac{k}{2k+1}<\frac12<\frac{k+1}{2k+1}.
```

If the endpoint offsets from `1/2` are

```tex
A=b-2a,\qquad C=2c-d,
```

then

```tex
A+C=(b-d)+2(c-a).
```

If `(c-a,b-d)!=(1,1)`, this gives enough fractions around `1/2` to force

```tex
B_n(a/b,c/d)\ge n/3-O(1),
```

which is too large for an extremal pair.

The remaining unit diagonal intervals crossing `1/2` are exactly the two
central template classes, producing van Doorn's residue-class witnesses.

### 2. Diagonal rational-center asymptotics

For diagonal intervals

```tex
\frac aq<\frac{a+1}{q-1},
```

the exact parametrization in `notes/diagonal-rank-formula.md` gives:

```tex
B_n(a,q)=
\#\left\{(p,t):(p,t)=1,\ \frac{at}{q+a}<p<\frac{(a+1)t}{q+a},\
t-p\le n\right\}.
```

For fixed rational-center families

```tex
q=(h-1)a+\lambda,\qquad n=q+O(1),
```

one gets

```tex
B_n(a,q)=\left(\frac{C_{h,\lambda}}{h-1}+o(1)\right)n.
```

The central `1/2` families are the only fixed rational-center families with
leading constant `1/4`; the centers `1/3,1/4,1/5,...` are linearly above
`1/4`.

This explains why off-center ties such as

```tex
\frac{32}{99}<\frac{33}{98}
```

can exist at finite `n` but should not persist infinitely.

### 3. Fixed off-center rational cells

The note `notes/fixed-rational-fan-lemma.md` proves the fixed-cell fan
lower bound. If a bad interval contains a fixed reduced rational
`r/s != 1/2`, then determinant fans around `r/s` give a leading constant
strictly larger than `1/4`.

For the first off-center cell `1/3`, determinant-one and determinant-two fans
already give

```tex
B_n\ge \frac{5n}{18}-O(1),
```

which is above `n/4`.

## What remains unproved

The missing global step is now:

```text
If a bad interval is extremal, then either it crosses 1/2,
or the least-denominator rational in the interval has bounded denominator.
```

Fixed bounded-denominator cells are handled asymptotically by the fan lemma.
The remaining danger is a sequence of near-extremal intervals whose internal
smallest rational has denominator growing with `n`.

The data supports the chain

```text
near-minimal bad pair
=> numerator jump +1
=> high denominator
=> diagonal
=> central template, except finite off-center ties
```

but the only fully proof-grade global pieces are the central cell and fixed
rational cells.

## Why the previous line of attack stalls

For a fixed rational `r/s` inside a bad interval, determinant-one fans around
`r/s` give a lower bound

```tex
B_n\ge
1+\frac1s\left(n-\frac bA\right)_+
 +\frac1s\left(n-\frac dC\right)_+-O(1),
```

where

```tex
A=br-as,\qquad C=cs-dr.
```

This is enough for the `1/2` cell. For the `1/3` cell, the determinant-one
fans alone can give only `2n/9+O(1)` in the most asymmetric offset case,
below the required `n/4`. The missing surplus comes from higher determinant
fans. That is the next technical obstacle.

## Current best next lemma

Prove a full fixed-cell fan theorem:

> For every reduced rational `r/s != 1/2`, every bad interval contained in a
> fixed Stern-Brocot neighborhood of `r/s` and having `B_n <= n/4+O(1)` belongs
> to a finite list of templates. Each template has diagonal asymptotic constant
> strictly larger than `1/4`.

The `1/3` cell is the first real test case and is now handled at the
fixed-cell level. The next test is a moving cell whose center denominator
grows with `n`, especially the reduced unit-step obstruction.

## Reduced unit-step obstruction

Every bad interval contains the real unit-step point

```tex
\frac ab<\frac{a+1}{b-1}.
```

If this point is reduced, the problem reduces to the diagonal lower bound. If
it reduces to `x/y`, then

```tex
a=gx-1,\qquad b=gy+1,
```

and any actual bad endpoint above `x/y` has offsets around `x/y` satisfying

```tex
A=x+y,\qquad C\ge \min(x,y).
```

This creates a large two-sided fan around `x/y`. The main term is large
enough for the conjecture; the remaining issue is proving a uniform primitive
fan-count error term when `x,y,A,C` all grow with `n`.

## Computational support

Complete exact atlas through `n=500`:

```text
for 92 <= n <= 500, f(n) matches the conjectural formula;
for 100 <= n <= 500, the exact minimizer is unique and central;
only non-template exact minimizer for n >= 92 is n=99.
```

Representative direct checks and near-minimizer sampling up to `n=700` found
no counterexamples to the structural route.
