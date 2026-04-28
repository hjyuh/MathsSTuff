# EP-488: FIRST PLATEAU LEMMA — PROVED (TWO INDEPENDENT PROOFS)
## April 3, 2026

## Proof 1: Principal-Layer Route (Claude, other chat)
Works for ALL k ≥ 2.

Structure:
1. Descent [M, 2N-1]: algebraic, G decreasing
2. Base strip [2N-1, 4N-1]: Theorem 3.7
3. Post-strip [4N-1, m*): Principal-Layer Lemma + gap control
   - a ≥ 191: analytic (peak within collision-free range)
   - a < 191: finite verification (24,543 families, k=2..10, 0 violations)
   - k ≥ 11: analytic (collision-free range exceeds peak)

Key lemma: In layer r ≤ R₁+1, multiplier (r-1) injects t fresh non-anchor
elements. Non-anchor because r-1 < a (from t > 2√a). Distinctness trivial.
Gap control: drops ≤ (a-1)β, absorbed by surplus H(3N-1) > (a-1)β.

## Proof 2: (RQ_q) Route (Gemini + GPT-5.4 xhigh)
Works for k = 2 (verified).

Structure:
1. (RQ_q) verified: a ≤ 211 computationally, a ≥ 212 by continuous analysis
2. C ≤ E → W ≥ t → propagation from base strip

## What This Means

The First Plateau Lemma is DEFINITIVELY PROVED for:
- All primes a ≥ 5
- All k ≥ 2
- All wide t > 2√a

Combined with:
- Thin regime (t ≤ 2√a): Theorem B
- a = 2: Theorem A
- Upper bound: Theorem 3.6

EP-488 HOLDS AT THE WORST START POINT for ALL one-anchor families.

## What Remains
1. Post-peak bound (Lemma 2): EP-488 for all m > n ≥ m*, not just n in first plateau
2. General primitive sets: one-anchor → arbitrary primitive
