# EP-488 CONTINUATION PROMPT — March 29, 2026 (FINAL)

## THE BREAKTHROUGH: Exact Positive-Sum Decomposition

F(n) = A_{Q_ℓ}(w) + A_{Min(Q_a∪{A})}(u) + A_{Min(Q_b∪{B})}(v)

where n = ℓw+t, u = Aw+u₀(t), v = Bw+v₀(t), A = ℓ/a, B = ℓ/b.

THREE non-negative counting functions. No subtraction. The -A_{Q_ℓ} was double-counted overlap that cancels exactly. Proved via quotient compression lemma: q_ℓ(t) = q_a(t)/gcd(q_a(t),A).

This eliminates the volatility from subtraction that made F≥5 hard.

## COMPLETE CHAIN (all verified)

1-12: Quotient-tail → periodicity → visible slab → F=2,3,4 elimination → sub-exceptional closure
13: Window-bound theorem (Mahmoud)
14-19: Hitting-time → delay condition → CRT obstruction (5.2)
20: Positive-sum decomposition (5.2 clean chat) — THE NEW RESULT

## THE REMAINING GAP

One lemma: prove the active drought bound.

For each primitive pair-tail system, visible-slab s with F(s) ≥ 5, every window (s, s+L] with L ≥ F(s):
  D(s+L) - D(s) ≥ δ_D L - (F(s) + α(s)L - 4)

where D counts deleted multiples in the exclusive decomposition.

Equivalently: prove no CRT alignment among active exclusive moduli can keep deletions sparse enough to violate the split inequality.

## STRUCTURAL MECHANISMS (verified)

1. Signed correlation is an exact identity (positive-sum decomposition)
2. Active/inactive scales: ratio peak only sees moduli r ≤ m; W+ uses inactive moduli
3. Deletion drought reformulation: delay failure = D below mean by linear amount
4. Half-scale reduction: violators need m ≥ s + F(s)
5. Weak charging: Δ_a + Δ_b ≥ 2Δ_ℓ always

## KILLED APPROACHES (8, each with counterexample)

Envelope (×5), two-route (14 primes), peak absorption (4,13,{15,17,19}), strong charging (67,71,...), universal peak/δ (2,3,T), per-residue W+ (11,15,{28,31}), W+<5 (5,11,{16,17,18}), 2^k bound (most Q)

## COMPUTATIONAL EVIDENCE

Zero failures in millions of checks. peak/δ ∈ [1.035, 1.373]. Margin 32-55%.
Signed correlation: 96.6% positive, c_ℓ > 0 in 100% of "both high" cases.

## MODELS CONSULTED

Claude Opus 4.6, GPT 5.2 Pro (×2), GPT 5.4 Pro (×3), Gemini 3.1 Pro, Gemini Deep Research, Claude Deep Research, Codex xhigh. Best results: 5.2 (hitting-time framework, positive-sum decomposition), 5.4 fresh (deletion drought)

## EXTERNAL

Forum post to Chojecki on erdosproblems.com — live, awaiting reply.

## FILES

- ep488_current_candidate_proof.md — full proof write-up
- subexceptional-48-54-charging.md — window-bound proof
- window-bound-general-theorem.md — general window theorem
- All in C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\
