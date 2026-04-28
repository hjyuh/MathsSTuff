# EP1005 Structural Lemma Roadmap

Drafted: 2026-04-26

## Scope

This note proposes a proof ladder for the conjectural sharp lower bound in
EP1005. The goal is not to replace van Doorn's analytic lower bound directly,
but to isolate a sequence of partial structural lemmas that would force every
short bad pair into the same near-`1/2` families used for the known upper
bound.

Local source notes used here:

- `README.md`
- `research-starts.md`

## Conventions

Let `F_n` be the Farey sequence of order `n`, in increasing order. For reduced
fractions

```tex
\alpha=\frac{a}{b}<\beta=\frac{c}{d}
```

write

```tex
B_n(\alpha,\beta)=\#\left(F_n\cap(\alpha,\beta)\right)
```

for the number of Farey fractions strictly between them. If the two endpoints
occur at indices `k<l`, then the rank gap is

```tex
l-k = B_n(\alpha,\beta)+1.
```

Thus

```tex
f(n)=\min B_n(\alpha,\beta),
```

where the minimum is over bad pairs. This is the OEIS "fractions in between"
normalization and avoids the common off-by-one issue.

Since all Farey fractions lie in `[0,1]`, a bad ordered pair
`a/b<c/d` must have

```tex
c>a,\qquad d<b.
```

The opposite sign pattern `c<a,d>b` is impossible for positive increasing
fractions. Put

```tex
u=c-a\ge 1,\qquad v=b-d\ge 1.
```

Then

```tex
bc-ad = bu+av,\qquad
\beta-\alpha=\frac{bu+av}{bd}.
```

The conjectural extremizers have `b,d` very close to `n`, `u,v` very small,
and both endpoints within `O(1/n)` of `1/2`.

## Dependency Ladder

1. Exact rank-gap formula.
2. Local interval lower bounds.
3. Reduction to small-denominator intervals.
4. Classification of near-`1/2` extremizers.
5. Exclusion of off-center bad pairs.

Together these would prove that the only asymptotically shortest bad pairs are
the explicit near-`1/2` constructions. For the exact conjecture, the final
output should recover

```tex
f(n)=\left\lfloor\frac n4\right\rfloor+d_r,\qquad
d_0,d_1,d_2,d_3=1,2,2,4,
```

for `n=4m+r` and all sufficiently large `n` matching the known conjectural
threshold.

## Lemma 1. Exact Rank-Gap Formula

**Statement.** For reduced `alpha=a/b<beta=c/d` in `F_n`, define

```tex
A_M(\alpha,\beta)
  =\sum_{Q=1}^M
    \left(
      \left\lfloor\frac{cQ-1}{d}\right\rfloor
      -\left\lfloor\frac{aQ}{b}\right\rfloor
    \right).
```

Then

```tex
B_n(\alpha,\beta)
  =\sum_{e=1}^n \mu(e) A_{\lfloor n/e\rfloor}(\alpha,\beta).
```

Equivalently, `B_n` is the number of primitive lattice points `(Q,P)` with
`1<=Q<=n` in the open strip

```tex
\alpha Q<P<\beta Q.
```

A denominator-stratified version should also be recorded:

```tex
B_n^{[Y,Z]}(\alpha,\beta)
  =\#\left\{\frac PQ\in F_n\cap(\alpha,\beta):Y<Q\le Z\right\}.
```

The same Mobius formula with `Y/e<Q<=Z/e` gives exact counts on denominator
blocks.

**Dependencies.** None beyond the Farey definition and Mobius inversion.

**Likely proof tools.**

- Mobius inversion for the primitive-point condition.
- Floor-sum identities for rational endpoints.
- Dedekind-sum or reciprocity reductions for symbolic residue-class checks.
- Stern-Brocot interval decompositions when the endpoints have a fixed small
  rational between them.

**Computational evidence.** Strong and directly useful. This formula gives an
exact evaluator for candidate pairs without generating all of `F_n`. It should
be checked against the standard Farey recurrence and OEIS A386893 values for
small `n`. It can also produce minimizer tables grouped by `n mod 4`,
endpoint denominator deficits `n-b,n-d`, and increments `u=c-a`, `v=b-d`.

**Roadmap role.** This is the arithmetic engine for every later lemma. The
proof can be fully rigorous and probably formalizable.

## Lemma 2. Local Interval Lower Bounds

**Statement.** There should be a local lower-bound package with two levels.

First, a coarse forcing statement: for every fixed `A` and `eta>0`, there is a
constant `c_eta>0` such that any bad pair satisfying

```tex
B_n(a/b,c/d)\le \frac n4 + A
```

must have

```tex
\min(b,d)>(1-\eta)n
```

unless the interval `(a/b,c/d)` contains a reduced fraction with denominator
bounded in terms of `A` and `eta`.

Second, in the high-denominator case, write `c=a+u`, `d=b-v`. A sharp local
version should prove that if `b,d>(1-\eta)n` and no bounded-denominator
fraction lies in the open interval, then

```tex
B_n(a/b,c/d)
  \ge n\Phi\left(\frac ab,u,v,\frac bn,\frac dn\right)-O_A(1),
```

where the normalized function `Phi` has its minimum `1/4` only in the critical
configuration

```tex
\frac ab=\frac12+O(1/n),\qquad u=1,\qquad v=1,\qquad b,d=n-O(1).
```

A weaker but still valuable partial is enough for a first pass: prove a
strict margin

```tex
B_n(a/b,c/d)\ge \left(\frac14+c\right)n
```

whenever one of the following holds:

- `|a/b-1/2|>epsilon`,
- `u+v` is larger than a fixed threshold,
- one of `b,d` is at most `(1-epsilon)n`,
- the interval length is outside the critical `Theta(1/n)` window.

**Dependencies.** Lemma 1 for exact counts and the determinant identity
`bc-ad=bu+av`.

**Likely proof tools.**

- Primitive lattice-point counts in thin rational strips.
- Denominator block decomposition: split `Q<=n` into ranges where the strip
  contains zero, one, or several integer ordinates.
- Continued fractions to detect the intervals where local density can be
  unusually low.
- Dress-style discrepancy estimates only as a coarse fallback; the `n/4`
  target needs sharper interval-specific information.
- Elementary lower bounds from the width identity
  `(c/d)-(a/b)=(bu+av)/(bd)`.

**Computational evidence.** Helpful but not decisive. Exhaustive minimizer
data can identify the normalized variables where `Phi` is small and can
falsify proposed constants. It cannot by itself prove the analytic uniformity,
but it should guide which denominator blocks and continued-fraction cells need
separate inequalities.

**Roadmap role.** This lemma is the main constant-improvement step. It should
turn a possible counterexample to the `1/4` lower bound into a highly
structured interval rather than an arbitrary short interval.

## Lemma 3. Reduction to Small-Denominator Intervals

**Statement.** Fix an additive slack `A`. There should be a constant `Q(A)`
such that every bad pair with

```tex
B_n(a/b,c/d)\le \frac n4 + A
```

falls into one of the following cases.

1. The open interval `(a/b,c/d)` contains a reduced fraction `r/s` with
   `s<=Q(A)`.
2. The pair is already in the high-denominator critical strip from Lemma 2:
   `b,d=n-O_A(1)`, `u,v=O_A(1)`, and both endpoints are within `O_A(1/n)` of
   `1/2`.

In case 1, the interval can be localized further to a bounded Stern-Brocot
cell around `r/s`. Concretely, after fixing `r/s`, the quantities

```tex
bs-ar,\qquad cr-ds
```

should be bounded in terms of `A` for any genuinely short bad pair. Hence the
remaining possibilities are a finite set of small-denominator cells plus a
bounded set of endpoint offsets.

**Dependencies.** Lemma 2, plus the exact formula of Lemma 1 to measure each
cell.

**Likely proof tools.**

- Continued-fraction convergents and the nearest small-denominator rational
  to the interval.
- Stern-Brocot parents of the two endpoints.
- Local lower bounds showing that if no small-denominator rational is present,
  the primitive-point density is too high except in the central critical
  strip.
- Exact floor-sum counts for each fixed `r/s` and bounded offset pattern.

**Computational evidence.** Very strong for choosing `Q(A)` and discovering
the offset bounds. A search over primitive bad endpoint pairs can list the
small denominators `r/s` that actually occur in near-minimizers. Once a
candidate finite list is known, the exact formula in Lemma 1 can test the
result over large `n` and fit quasi-polynomial expressions in `n mod M`.

**Roadmap role.** This is the bridge from analytic estimates to finite
classification. It should reduce the global problem to finitely many rational
neighborhoods, with `1/2` singled out as the only plausible extremal center.

## Lemma 4. Classification of Near-`1/2` Extremizers

**Statement.** Let `n=4m+r`, `0<=r<4`. For every fixed slack `A`, every bad
pair in the central critical strip

```tex
\left|\frac ab-\frac12\right|,\,
\left|\frac cd-\frac12\right| \le \frac{A}{n},
\qquad
b,d=n-O_A(1),
\qquad
c-a,\ b-d=O_A(1)
```

and satisfying

```tex
B_n(a/b,c/d)\le \frac n4+A
```

belongs to a finite residue-class template list `E_r(A)`.

For the exact conjectural bound, the minimal templates should be precisely
van Doorn's upper-bound constructions, giving

```tex
B_n(a/b,c/d)=\left\lfloor\frac n4\right\rfloor+d_r,
\qquad
d_0,d_1,d_2,d_3=1,2,2,4.
```

The `r=0` template includes the known pair

```tex
\frac{2m-1}{4m}<\frac{2m}{4m-1},
```

for which the rank gap is `m+2` and the in-between count is `m+1`.
The templates for `r=1,2,3` should be copied from van Doorn's explicit
construction after the paper is audited locally.

**Dependencies.** Lemmas 1 and 3. Lemma 2 supplies the reason that only this
central strip remains.

**Likely proof tools.**

- Parametrize endpoints as

  ```tex
  b=n-s,\quad d=n-t,\quad
  a=\left\lfloor\frac b2\right\rfloor+\rho,\quad
  c=\left\lfloor\frac d2\right\rfloor+\sigma,
  ```

  with `s,t,rho,sigma` bounded.
- Use the bad-pair constraint `c>a`, `d<b` to cut the bounded parameter set.
- Evaluate `B_n` exactly by Lemma 1 for each bounded pattern.
- Convert each pattern into a quasi-polynomial in `m` and residue classes.
- Discard all patterns above the conjectural value and retain the upper-bound
  templates.

**Computational evidence.** This is the most computation-friendly part of the
roadmap. Existing notes report checks through `n<=5000`; a fresh exact-rank
search should recover the same residue classes, identify all ties, and produce
candidate quasi-polynomials. Once the template list is known, the proof is
finite and symbolic rather than heuristic.

**Roadmap role.** This lemma proves that the known examples are not accidents.
It should also provide the exact additive constants once the global exclusion
lemmas have forced all near-minimizers into the central strip.

## Lemma 5. Exclusion of Off-Center Bad Pairs

**Statement.** For every fixed `epsilon>0`, there should be a constant
`c_epsilon>0` such that every bad pair with midpoint outside the central
window

```tex
\left|\frac12\left(\frac ab+\frac cd\right)-\frac12\right|>\epsilon
```

satisfies

```tex
B_n(a/b,c/d)\ge \left(\frac14+c_epsilon\right)n-O_\epsilon(1).
```

For the exact conjecture, the needed finite version is sharper: after Lemma 3
reduces to bounded small-denominator cells, every cell centered at
`r/s != 1/2` should satisfy

```tex
B_n(a/b,c/d)\ge
\left\lfloor\frac n4\right\rfloor+d_{n\bmod 4}+1
```

for all sufficiently large `n`, apart from the already known small exceptional
values.

**Dependencies.** Lemmas 1, 2, and 3. Lemma 4 handles the only cell expected
to survive, namely `1/2`.

**Likely proof tools.**

- Exact floor-sum lower bounds on each fixed small-denominator cell.
- Monotonicity in endpoint offsets: moving away from `1/2` should either
  widen the interval or place it in denser denominator blocks.
- Symmetry under `x -> 1-x` to pair cells `r/s` and `(s-r)/s`.
- Finite residue-class verification for bounded cells, upgraded to proof by
  quasi-polynomial inequalities.
- Coarse local-density estimates to handle cells with denominator above the
  chosen finite cutoff.

**Computational evidence.** Strong for discovery and finite reduction. A
minimizer search should show a positive linear margin away from `1/2`, and
cell-by-cell exact counts should reveal the worst off-center cells. However,
the final exclusion still needs symbolic inequalities, because the relevant
claim is uniform in `n`.

**Roadmap role.** This closes the structural proof. Once off-center cells are
excluded and near-`1/2` cells are classified, the upper-bound constructions
become globally extremal.

## Suggested Work Products

1. Implement the exact `B_n` evaluator from Lemma 1 and compare it with direct
   Farey recurrence generation for `n<=200`.
2. Enumerate primitive bad endpoint pairs for `n<=1000`, recording
   `(n mod 4, B_n, b,d,u,v,a/b,c/d)`.
3. Fit the near-`1/2` minimizers to bounded templates in the variables
   `n-b`, `n-d`, `c-a`, `b-d`, and endpoint offsets from one half.
4. For each small rational `r/s` discovered by the search, use the exact
   formula to generate residue-class quasi-polynomials for the best possible
   bad pair in that cell.
5. Turn the quasi-polynomial comparisons into human-checkable inequalities,
   starting with all cells `s<=6` and then increasing the cutoff only if the
   data forces it.

## Main Risk

The hard step is Lemma 2: local density in intervals of length `Theta(1/n)` is
not governed well enough by global Farey discrepancy estimates. The roadmap is
therefore designed so that Lemma 2 only has to be sharp outside bounded
small-denominator cells; those cells can then be attacked exactly by Lemmas 3
through 5.
