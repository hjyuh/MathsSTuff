# Blocker A: Corrected Status After Codex Review of DT Application

March 16, 2026

## What DT Gives (Real)
- The exponential sum setup h=(1,2), k=(0,c) IS valid for odd p ✓
- General AP modulus d allowed, no (d,q)=1 obstruction ✓  
- Power-saving cancellation for CONGRUENCE classes of (s_p(n), s_p(2n+c)) ✓

## What DT Does NOT Give (Codex Correction)
1. **Threshold ≠ congruence.** κ^{(c)}(n) < T is a union of EXACT VALUES of 2s_p(n) - s_p(2n+c), not residue classes mod (p-1). Congruence mod (p-1) loses the inequality.

2. **Error exponent deteriorates with p.** DT Corollary 2.10 has error exponent depending on m² where m = lcm(m₁,m₂). With m = p-1, this gives x^{1 - c₀/(p² · ...)} which is not uniform across primes p ≤ Y.

## What DT Probably Does Give (Narrower)
For **finitely many fixed small primes** p (say p = 3, 5, 7, ..., W), DT gives:
- Exponential sum estimates for s_p(n) and s_p(2n+c) in APs
- With FIXED p, the error exponent is a fixed positive constant
- Can derive large-deviation bounds for the carry deficit at each fixed prime

This handles the "small prime" part of the completion. But does NOT handle all primes up to Y uniformly.

## Revised Gap

The gap is now in two pieces:

**Piece 1 (small primes, p ≤ W):** DT machinery should work, one fixed prime at a time. The error exponent is fixed (depends on p but p is fixed). Need to extract a large-deviation / weighted bound for carry deficit, not a congruence count. This is "a plausible lemma to write from DT."

**Piece 2 (medium/large primes, W < p ≤ Y):** For these, a_p(X) = log_p(X) is moderate to small. The carry deficit is a large-deviation event on a short Markov chain. The uniform layer lemma already gives q_{n,p}(a) ≤ C_n·a·2^{-a}/p for p ≥ 4a. 

But the issue Codex identified earlier remains: converting these LOCAL single-prime bounds into a DENSITY statement in [X, 2X] requires the multi-prime lift, which in turn requires that the carry conditions at different primes are sufficiently independent INSIDE the truncated residue class.

## The Actual Architecture That Might Work

**For small primes p ≤ W (fixed, finitely many):**
- Use full depth a_p(X) for these primes
- The modulus contribution is ∏_{p≤W} p^{a_p} which for W fixed is roughly X^{π(W)}
- This is huge but we can use DT to handle the digit conditions for each fixed p
- Key: DT's short-interval exponential sums can control digit statistics in intervals of length N, even when N is much smaller than the prime power modulus

**For large primes W < p ≤ Y:**
- Use depth A (truncated) for these primes
- The modulus is ∏_{W<p≤Y} p^A ≤ exp(AY) which can be kept < X^{1/2-η} by choosing Y ≤ c·log(X)/A
- After the exact digit split, the high-digit carry chain runs on free digits (because for p > W, the interval length N = X/Q' >> p^{a_p-A} when W is chosen appropriately)

Wait — does N >> p^{a_p-A} hold for all W < p ≤ Y?

N = X / Q' where Q' = (∏_{p≤W} p^{a_p}) · (∏_{W<p≤Y} p^A).

For p > W: p^{a_p-A} = p^{log_p(X) - A + O(1)} ≈ X/p^A.

We need N >> X/p^A, i.e., Q' << p^A.

Q' = (∏_{p≤W} p^{a_p}) · (∏_{W<p≤Y} p^A).

For p in (W, Y]: Q' ≥ p^A (since p^A is one factor). So Q' ≥ p^A always, meaning N ≤ X/p^A. Equality when the other factors are 1, which they aren't.

So N << X/p^A, not N >> X/p^A. The digits are NOT free. Same obstruction as before.

**The fundamental issue persists:** Q' >> p^A for every p in the product, so inside a Q'-class, the p-digits above level A are constrained to a short interval, not free.

## Honest Assessment

DT narrows the gap but does not close it. The architecture needs:

1. A way to handle finitely many small primes using DT-style exponential sums (plausible)
2. A way to handle the remaining primes WITHOUT requiring digit freedom in the residue class

Option 2 might come from:
- Using DT's exponential sums directly for ALL primes (not just congruence counting), accepting the p-dependent error
- A different approach entirely for the multi-prime lift
- Cumberbatch's response (if his circle method extends to carries)

## Completeness Score: 7.5/10

Not 8/10 as claimed. DT is the right tool but the extraction is harder than GPT suggested. The proof is not complete — there is still genuine work required.

## STATUS: DT is the right machinery. Application to threshold events and uniformity in p are the remaining technical challenges. Not closed, but much closer than before.
