# EP-488: Context Package for Fresh Model — First Plateau Lemma (Alternative Approach)

## The Problem (2 lines)
Let A be a primitive set (no element divides another). Define F(x) = |{n ≤ x : a|n for some a ∈ A}|.
EP-488: Is F(m)/m < 2·F(n)/n for all m > n ≥ max(A)?

## What's Proved
1. **a=2 case:** All primitive sets with 2 ∈ A satisfy EP-488.
2. **Thin regime:** For A = {a} ∪ {ka+1,...,ka+t} with a prime, k≥2, t ≤ 2√a: EP-488 holds.
3. **Upper bound:** sup_{x≥M} G(x) ≤ 1/a + t/(ka+1) < 2·G(2ka-1) where G(x) = F(x)/x.

## YOUR TASK: Prove the First Plateau Lemma

For A = {a} ∪ {ka+1,...,ka+t}, a prime, k ≥ 2, 1 ≤ t < a:

Let m* be the earliest maximizer of G(x) = F(x)/x on [M, ∞) where M = ka+t.

**Prove:** G(n) ≥ G(2ka-1) for all M ≤ n < m*.

Equivalently: the minimum of G on the "rising phase" [M, m*) occurs at n = 2ka-1.

## Why This Matters
Combined with the upper bound (already proved) and a separate post-peak bound (being worked on in parallel), this closes EP-488 for ALL one-anchor families, which are the known extremal class.

## Computational Evidence
3402 families tested (all t, prime a ≤ 101, k ∈ {2,3,4}, plus k up to 6). Zero exceptions.

## Key Values
At n = 2ka-1: F(2ka-1) = t + 2k - 1 (each block element contributes itself, anchor contributes 2k-1 multiples).
So G(2ka-1) = β := (t+2k-1)/(2ka-1).

## The Structure of G on [M, m*)

G(x) has a specific shape: it rises overall (new block multiples turning on) but dips at pre-anchor points x = ra-1 where ⌊x/a⌋ is about to increment.

The dips occur at x = 2ka-1, (2k+1)a-1, (2k+2)a-1, ...

At each dip x = ra-1:
- Anchor contributes r-1 multiples
- Block contributes the number of block-divisible integers up to ra-1

The claim is: later dips are shallower because more block multiples have accumulated.

## Approach Hint (one possible route, feel free to ignore)

Between consecutive anchor multiples, in the interval [(r-1)a, ra-1]:
- The anchor contributes 0 new multiples
- Each block element b ∈ B = {ka+1,...,ka+t} contributes at most 1 multiple (since b > a, so at most one multiple of b fits in an interval of length a)
- Element b contributes a multiple iff ∃j with (r-1)a ≤ jb ≤ ra-1

The fraction of block elements contributing in each anchor interval is approximately a/b ≈ 1/k.

For k=2: about half the block elements contribute per interval. This is exactly what's needed to keep G(ra-1) ≥ β.

The proof reduces to: in each anchor interval [(r-1)a, ra-1], at least (t+2k-1)/2 block elements have a multiple. This is an equidistribution statement about {(r-1)a/b} for b ∈ B.

## Important: Do NOT use these approaches (they've been killed)
- Sieve theory / inclusion-exclusion oscillation bounds
- Global sup/inf < 2 (FALSE in wide regime)
- U_x ≥ S_x/2 (FALSE asymptotically)
- Monotone compression (adding elements can increase ratio)

The proof should be ELEMENTARY and DIRECT, using the specific structure of one-anchor families.

Extended thinking ON, think deep, and in parallel. Think of every conventional, unconventional, novel mix of both approach. Try and fail until you've genuinely exhausted everything and come back with what you tried, why it worked / didn't, how close we are, what you recommend next and why.
