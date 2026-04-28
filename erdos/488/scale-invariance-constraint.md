# EP-488: Scale-Invariance Constraint
## April 5, 2026

## KILL #45: Two-regime proof at S₁ = 1

Both Lemma A (S₁ < 1 → 2·min G > S₁) and Lemma B (S₁ ≥ 1 → δ > 1/2)
are FALSE. The scaling family A = 2{p ≤ y} slides across any fixed
S₁ threshold while preserving the ratio.

Mahmoud spotted the Lemma B kill. GPT-5.4 Pro confirmed and killed Lemma A.

## THE CONSTRAINT ON ANY VALID PROOF

GPT-5.4 Pro: "the next viable route has to be scale-invariant."

Scaling A → tA gives: G_{tA}(tx) = G_A(x), so ratio(tA) = ratio(A).
Any proof of ratio < 1 must use only scale-invariant quantities.

Scale-INVARIANT:
- ratio itself
- k (number of elements)
- max/min ratio
- δ/S₁
- S₂/S₁²
- the shape of G (up to rescaling x-axis)

Scale-VARIANT (cannot appear in the proof):
- S₁ alone
- δ alone
- max(A) alone
- any fixed threshold on S₁ or δ

## WHAT THIS RULES OUT

Any proof of the form "if [quantity] < c then [bound A], else [bound B]"
where [quantity] is not scale-invariant. This kills ALL threshold-based
approaches including:
- S₁ < 1 / S₁ ≥ 1
- δ < 1/2 / δ ≥ 1/2
- S₁ < ln 2 / S₁ ≥ ln 2
- Any other fixed cutoff on S₁ or δ

## PERCENTAGE: 91%
