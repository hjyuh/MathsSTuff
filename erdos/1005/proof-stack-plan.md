# EP1005 Proof Stack Plan

Date: 2026-04-26

Goal: build partial results that can stack toward the conjectural exact
asymptotic, and ideally the exact eventual formula, for the Mayer-Erdos
phenomenon in Farey fractions.

## Target

Let `F_n = a_1/b_1 < ... < a_N/b_N` be the Farey sequence of order `n`.
Two fractions are similarly ordered when

```tex
(a_k-a_l)(b_k-b_l) >= 0.
```

Let `f(n)` be the largest integer such that every pair with
`1 <= k < l <= k+f(n)` is similarly ordered. Equivalently, `f(n)+1` is the
least index distance between a non-similarly-ordered pair.

Current published/scouted bounds:

```tex
(1/12-o(1))n <= f(n) <= n/4 + O(1).
```

Conjectural sharp form reported in the scouting pass:

```tex
f(n)=floor(n/4)+d(n)
```

eventually, with residue-class correction `d(n)`.

## Stacking Principle

Every result we prove or compute should land in one of four layers:

1. **Exact identities**: no asymptotics, no heuristics.
2. **Certified finite data**: reproducible computations with checkable output.
3. **Structural reductions**: lemmas that reduce the conjecture to restricted
   endpoint families or intervals.
4. **Sharp lower bound**: a proof that every bad pair has index gap at least
   the conjectural value, except for finitely many checked cases.

The full solution should look like:

```text
explicit bad pairs give upper bound
+ rank-gap identity for arbitrary bad pairs
+ structural reduction to near-extremal endpoint families
+ lower bound for each family
+ finite verification below threshold
= exact/eventual formula
```

## Layer 1: Exact Identities

### Lemma A: Bad-pair convention

For `a/b < c/d`, the pair is bad iff `a<c` and `b>d`, or `a>c` and
`b<d`. Since the fractions are ordered by value, the near-`1/2`
extremizers have `a<c` and `b>d`.

Use: removes ambiguity from similarly ordered pairs and sets the endpoint
orientation used in searches.

### Lemma B: Rank-gap formula

For reduced fractions `a/b < c/d`, the Farey index gap in `F_n` equals

```tex
1 + # { p/q : 1 <= q <= n, gcd(p,q)=1, a/b < p/q < c/d }.
```

Equivalently, for each denominator `q`,

```tex
floor((cq-1)/d) - floor(aq/b)
```

counts candidate numerators before imposing coprimality. Apply Mobius
inversion to impose `gcd(p,q)=1`.

Use: turns the problem into lower bounds for reduced rationals in short
intervals.

### Lemma C: Neighbor interval formula

If `bc-ad=1`, then `a/b` and `c/d` are consecutive in `F_n` exactly when
`max(b,d) <= n < b+d`. More generally, their interval can be decomposed by
Stern-Brocot descendants with denominator bound `n`.

Use: explicit upper-bound pairs and near-extremal family classification.

## Layer 2: Certified Finite Data

### Data target 1: reproduce `f(n)` for `4 <= n <= 100`

Use OEIS A386893 as a fixture. This validates conventions, off-by-one choices,
and the basic generator.

### Data target 2: minimizer atlas up to `n <= 5000`

For each `n`, store every bad pair achieving the minimum index gap:

```text
n, n mod 4, f(n), endpoint fractions, denominator pair,
bc-ad, continued fractions, interval length, centered distance from 1/2
```

Use: discover whether all extremizers come from a small residue-class family.

### Data target 3: near-minimizers

Store bad pairs with index gap within `+5` or `+10` of the minimum.

Use: near-minimizers often reveal what a stability lemma must rule out.

## Layer 3: Structural Reductions

### Reduction R1: local density dichotomy

For a bad pair `a/b < c/d`, put interval length

```tex
c/d - a/b = x/n.
```

Prove that if the interval is not of the explicit near-`1/2` form, then it
contains enough reduced fractions of denominator `<= n` to force rank gap
`> n/4 + O(1)`.

This is the main route for improving van Doorn's `1/12`.

### Reduction R2: small denominator obstruction

If the interval contains a fraction with very small denominator, use Farey
spacing to force many surrounding fractions or classify the few exceptions.

Deliverable partial result: prove a strong bound in the case where the interval
contains a denominator `< C/x`, experimenting with constants `C=4,5,6`.

### Reduction R3: off-center exclusion

Prove that a bad pair far from `1/2` cannot be extremal. The expected reason is
that denominator/numerator monotonicity creates extra reduced fractions in the
interval.

Deliverable partial result: prove an `> n/4` lower bound for intervals wholly
inside `[0,1/2-epsilon]` or `[1/2+epsilon,1]`, then shrink `epsilon`.

### Reduction R4: near-`1/2` classification

For bad pairs with index gap `<= n/4+O(1)` and endpoints near `1/2`, prove the
denominators and numerators must satisfy one of a small number of linear
patterns, matching the upper-bound constructions.

Deliverable partial result: classify under added hypotheses such as
`bc-ad=1`, or `b+d` in a specified range.

## Layer 4: Sharp Lower Bound

The final lower bound should split all bad pairs into:

1. explicit near-`1/2` families, where exact rank gaps match the conjecture;
2. small-denominator intervals, handled by R2;
3. off-center intervals, handled by R3;
4. remaining generic intervals, handled by an improved local-density lemma.

Finite exceptions below the analytic threshold should be discharged by a
certificate file, not by an informal script output.

## Immediate Work Packages

The six active subagents map to the proof stack:

- `proof-ledger-vandoorn.md`: audit existing proof and constant losses.
- `scripts/farey_rank_gap.py` plus `computational-plan.md`: basic verifier and
  scaling plan.
- `minimizer-atlas-plan.md`: data schema and pattern-mining agenda.
- `upper-bound-constructions.md`: exact explicit bad pairs by residue class.
- `structural-lemma-roadmap.md`: lemma ladder toward the lower bound.
- `formalization-and-certificates.md`: Lean and finite-certificate plan.

## First Sprint Definition Of Done

The first sprint is successful if it produces all of:

1. a convention-tested script that reproduces OEIS values through `n=100`;
2. a verified table of conjectural upper-bound pairs by `n mod 4`;
3. a ledger showing the precise losses in the `1/12` lower bound;
4. a ranked list of candidate lemmas, with the easiest one stated in proof-ready
   form;
5. a finite certificate format for `n <= N` computations.

## Best First Partial Result To Prove

Prove the explicit upper-bound construction rigorously and formalization-ready:
for each residue class of `n mod 4`, exhibit a bad pair in `F_n` whose index
gap is the conjectural minimum plus one.

This does not solve the hard direction, but it locks down the sharp target and
prevents all later work from drifting on conventions.

## Best First Hard Lemma

A good first nontrivial lower-bound lemma is:

> If `a/b < c/d` is a bad pair in `F_n`, has index gap `<= n/4 + O(1)`, and
> `bc-ad=1`, then the pair lies in one of the explicit near-`1/2`
> residue-class families, up to finitely many small exceptions.

Why this is useful: computations can test it, Stern-Brocot theory applies
directly, and it is a plausible bridge from exact identities to the full
classification.

