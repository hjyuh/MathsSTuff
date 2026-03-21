# GPT 5.2 — Push the Low-Frequency Sum. This Is the Last Bridge.

You offered to write the low-frequency sum decomposition by CRT profiles. Do it now.

---

## Where we are

You proved:
- hat(1_{A_p})(k) = S₁(k)·S₂(k) with |S₁| ≤ n+1, |S₂| ≤ min(H, p/(2r*))
- CRT factorization: hat(1_{A_d})(k) = ∏_p hat(1_{A_p})(k mod p²)
- Discrepancy identity: |N_{G_d}(X) - (|G_d|/d)X| ≤ (1/d)Σ_{k≠0} |hat(1_{G_d})(k)| · min(X, d/|k|)

The blocker: for d >> X, the low-frequency terms (small |k|) have min(X, d/|k|) = X, so we need:

Σ_{|k| ≤ d/X} |hat(1_{G_d})(k)| ≤ ε · |G_d|

Since G_d is the COMPLEMENT of A_d in ℤ/dℤ:
hat(1_{G_d})(k) = -hat(1_{A_d})(k) for k ≠ 0.

So we need: Σ_{|k| ≤ d/X} |hat(1_{A_d})(k)| ≤ ε · |G_d| = ε · d · ∏(1-g(p)).

## The CRT profile decomposition

Each k mod d corresponds to a tuple (k_p)_{p∈P} where k_p = k mod p² ∈ {0,...,p²-1}.

hat(1_{A_d})(k) = ∏_p hat(1_{A_p})(k_p)

For k_p = 0: hat(1_{A_p})(0) = |A_p| = (n+1)H ≈ (n+1)p/2.
For k_p ≠ 0: |hat(1_{A_p})(k_p)| ≤ (n+1)·min(H, p/(2r*_p)) where r*_p = min(k_p mod p, p - k_p mod p).

The SAVING comes when k_p ≠ 0 for at least one p, because then that factor is ≤ (n+1)p/(2r*_p) instead of (n+1)H ≈ (n+1)p/2.

If k_p ≡ 0 mod p (but k_p ≠ 0 mod p²): then S₂ = H (no saving from S₂), but S₁ may give some saving.
If k_p not ≡ 0 mod p: then |S₂| ≤ p/(2r*_p), giving saving ≥ r*_p/H ≈ 2r*_p/p.

## Your task

1. **Decompose** Σ_{|k|≤d/X} |hat(1_{A_d})(k)| by CRT profiles. Each k ↔ (k_p)_p. Group by which primes have k_p = 0, k_p ≡ 0 mod p (but ≠ 0 mod p²), or k_p not ≡ 0 mod p.

2. **Bound each group.** The "worst" profile is k_p = 0 for all p (but that's just k=0, excluded). The next worst is k_p = 0 for all but one p. Then all but two, etc.

3. **Count profiles.** For |k| ≤ d/X: the number of k with a given profile depends on the structure. For example, k_p = 0 for p ∈ S means d/∏_{p∈S}p² | k, so k is a multiple of d/∏_{p∈S}p² = ∏_{p∉S}p². The number of such k in [1, d/X] is ≤ (d/X) / ∏_{p∉S}p² = ∏_{p∈S}p² / X.

4. **Determine:** does the total Σ |hat(1_{A_d})(k)| over |k| ≤ d/X give the needed bound ε·|G_d|? Or is there an irreducible obstruction?

5. If the full sum doesn't converge: **identify the exact profiles** that cause trouble, and whether a modified approach (truncating the prime set, weighting differently, or using a different discrepancy inequality) can handle them.

This is the computation that determines whether the proof closes for general n. Please execute it completely.
