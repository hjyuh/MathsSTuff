# EP-488: Session Final Status — April 4, 2026

## PROVED THEOREMS (rigorous, in paper v6)

1. **One-anchor families** (any a prime, k ≥ 2, t < a): Principal-Layer + Post-Peak
2. **All primitive pairs**: 4-line proof (2G > 2/a > 1/a + 1/b > G)
3. **All primitive triples**: IE comparison R > 0 + discrepancy C < 4
4. **Sparse sets** (Σ1/a ≤ 2/min): sparse-mass lemma
5. **Coprime sets tail**: product-exponential (2δ > S₁ or δ > 1/2)
6. **Fixed k**: C ≤ 2^(k-1), finite verification per k
7. **Adjacent pairs exact formula**: ((2b-3)/(2b-2))² < 1

## SUPPORTING TOOLS (proved)
- Primitive Divisor Lemma (Lean-verified)
- Subset LCM Bound: lcm(S) ≥ 2·max(S)
- Fibered FKG: δ_B ≤ 0.3187 (ε = 0.0135)
- Quota-Capacity Identity: W - t = E - C
- Transfer Lemma: EP for k follows from EP for k-1 + compact strip
- Quotient-Core Recursion: δ_A = δ_{A'} + (1-δ_{Q_a})/a
- Complement Halving: ρ_A ≥ ρ_{A'}/2

## KILLED APPROACHES (38)
One-anchor (32): first-moment, global oscillation, sieve/NT, direct, envelope
Post-peak (1): C ≥ (1+δ)E
Generalization (5): singleton-extremal, 2δ>S₁ universal, δ>1/2 dense,
  Case A/B dichotomy, Bonferroni-2r fixed, C=O(k²)
Plus: FKG lower bound (wrong direction)

## COMPUTATIONAL VERIFICATION
- 23+ million families, zero EP-488 failures
- Worst ratio: 0.9824 at {196,197,198,199}
- C actual vs universal: 46.7 vs 2^20 for k=21 counterexample

## THE REMAINING GAP
Non-coprime dense primitive sets with |A| ≥ 5 where:
- 2δ < S₁ AND δ < 1/2 (both tail cases fail)
- C ≤ 2^(k-1) is too pessimistic (actual C << universal bound)

Key insight from Claude Code: actual C ≈ 47 even for k=21.
If provable C = O(k²) for non-coprime dense: EP-488 follows.
The Parseval obstruction (C ~ 2^{k/2}) uses COPRIME primes,
which are handled by the coprime tail proof. Non-coprime C might
genuinely be polynomial — but unproved.

## PERCENTAGE: 89%
Solid publishable result. Gap is genuine research-level.

## FILES IN C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\
### Paper versions
paper/ep488-paper-v6.tex (current)
paper/primitive-pairs-note.tex
paper/ep488-final-lemma.tex

### Proof documents
first-plateau-proved.md, postpeak-proved.md, postpeak-converged.md
primitive-pairs-proved.md, bonferroni4-breakthrough.md (then killed)
fibered-fkg-bound.md, tail-proof-status.md

### Analysis documents
generalization-analysis-april4.md, claude-code-analysis-summary.md
gpt54pro-generalization-r3.md, gpt54pro-postpeak-r2.md
gpt52-refined-packing-r2.md, discrepancy-obstruction.md
singleton-extremal-false.md, k4-proved-status.md
codex-dense-k4-k7-results.md, session3-final-status.md

### Computation results
postpeak_scan_p199_m100.json, postpeak_top10_push.json
singleton_extremal_scan_M17_50.json, primitive_pairs_b500_scan.json
dense_k4_k7_scan.json

### Scripts
scan_postpeak_bound.py, push_postpeak_top10.py
scan_singleton_extremal.py, scan_primitive_pairs.py
scan_dense_k4_k7.py, ep488_R_sign.py, ep488_k5_check.py

### Prompts
rotation-round2-all-postpeak.md, rotation-round3-corrected.md
rotation-round4-dense-k4.md, claude-code-prompt.md
claude-code-bonferroni4-prompt.md, gpt54pro-final-gap-prompt.md
gpt54pro-final-push.md
