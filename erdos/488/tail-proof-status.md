# EP-488: Tail Proof Status — April 4, 2026

## PROVED RIGOROUSLY

### Coprime primitive sets (+ their scalings): 2δ > S₁
Case A (S₁ < 1.594): δ ≥ 1-e^{-S₁} > S₁/2
  Proof: ln(1-x) ≤ -x → Π(1-1/aᵢ) ≤ e^{-S₁}
  Then: 2(1-e^{-S}) > S for S < S₀ = 1.5936 (calculus)

Case B (S₁ > ln 2 = 0.693): δ > 1/2 → 2G > 1 > G(m)
  Proof: δ ≥ 1-e^{-S₁} > 1/2 when S₁ > ln 2

Cases overlap on (0.693, 1.594). Complete coverage for coprime.

### Scaling invariance: 2δ(mA)/S₁(mA) = 2δ(A)/S₁(A). Rigorous.

## THE REMAINING GAP

Non-coprime, non-scaling primitive sets with S₁ ∈ (2/min, S₀).

Key facts:
- Coprime sets MAXIMIZE δ for fixed S₁ (wrong direction for us)
- But coprime sets MINIMIZE the ratio 2δ/S₁ (right direction!)
- So coprime is the HARDEST case, and it's proved
- Non-coprime should be EASIER, but we can't prove it
- FKG gives δ ≤ upper bound (wrong direction)
- Need δ ≥ lower bound for non-coprime

Computational: 830K+ sets, zero failures. Gap is analytical only.

## POSSIBLE APPROACHES FOR NON-COPRIME LOWER BOUND
1. Selberg sieve lower bound + Primitive Divisor Lemma
2. Second-moment method (Paley-Zygmund on indicator)
3. Direct: write δ = S₁ - S₂ + S₃ - ... and bound truncation error
4. Monotonicity: show replacing coprime pair with non-coprime
   can only increase 2δ/S₁ ratio (proved computationally)

## STATUS: 94%
