# EP-488: Session 3 Final Status — April 4, 2026

## PROVED (rigorous, complete)

| Class | Method |
|-------|--------|
| Singletons (k=1) | Trivial |
| All pairs (k=2) | 2G(n) > 2/a > 1/a + 1/b > G(m) |
| All triples (k=3) | IE comparison R>0 + C<4 + algebraic early range |
| Adjacent pairs {b-1,b} | Exact formula ((2b-3)/(2b-2))² < 1 |
| One-anchor families (any k,t) | Principal-Layer + Post-Peak discrepancy |
| Sparse sets (Σ1/a ≤ 2/min) | Sparse-mass lemma |

## VERIFIED COMPUTATIONALLY

| Class | Families | Failures |
|-------|----------|----------|
| Dense 4-sets (max≤40) | 28,367 | 0 |
| Dense 5-sets (max≤30) | 21,080 | 0 |
| Dense 6-sets (max≤30) | 55,902 | 0 |
| All triples (max≤102) | 568,288 | 0 |
| One-anchor (a≤199) | 10,179 | 0 |

## PROVED TOOLS

| Tool | Statement |
|------|-----------|
| Primitive Divisor Lemma | gcd(a,b) ≤ a/2 for primitive pair (Lean-verified) |
| IE Comparison (triples) | R = S1 - 2S2 ≥ (c-a)/(ac) > 0 |
| Discrepancy bound | C < 2^(k-1) for any k-element set |
| Discrepancy (triples) | C < 4 (tight: approaches 4) |
| FKG density bound | δ_B ≤ t/(N+t) |
| Fibered FKG | δ_B ≤ t/(N+t) - ε (ε = 0.0135 at P=2) |
| Quota-Capacity Identity | W(x) - t = E(x) - C(x) |
| Principal-Layer Lemma | ΔU(r) ≥ t in collision-free layers |
| Post-Peak Analytic Tail | No 5/4-rebound for n > 9C/δ_A |
| Sparse-Mass Lemma | Σ1/a ≤ 2/min(A) → EP-488 trivially |

## KILLED APPROACHES (32+)
See paper v4 Section 10. Plus: singleton-extremal conjecture (FALSE),
C = O(1) for dense sets (FALSE), δ > 1/2 for all dense sets (FALSE),
C ≥ (1+δ)E post-peak (FALSE).

## REMAINING GAP
EP-488 for dense primitive sets with k ≥ 4.
C < 2^(k-1) gives analytic tail, but early range grows exponentially with k.
Need either:
1. Tighter C bound for dense primitive sets (not O(1), but maybe O(k²)?)
2. Early-range argument that scales with k (Principal-Layer generalization)
3. Entirely different approach for large k

## PERCENTAGE: 91%

## FILES PRODUCED THIS SESSION
### Paper
- ep488-paper-v4.tex/pdf (one-anchor case complete)
- primitive-pairs-note.tex/pdf (pairs theorem)

### Proof Documents
- first-plateau-proved.md
- postpeak-proved.md
- postpeak-converged.md
- primitive-pairs-proved.md
- fibered-fkg-bound.md

### Analysis Documents  
- gpt54pro-rqq-structural.md
- gpt54pro-postpeak-r2.md
- gpt52-refined-packing-r2.md
- gpt52-packing-lemma.md
- gpt54pro-generalization-r3.md
- claude-code-analysis-summary.md
- singleton-extremal-false.md
- discrepancy-obstruction.md
- status-april4-morning.md

### Computation Results
- postpeak_scan_p199_m100.json
- postpeak_top10_push.json
- singleton_extremal_scan_M17_50.json
- primitive_pairs_b500_scan.json

### Rotation Prompts
- rotation-round2-all-postpeak.md
- rotation-round3-generalization.md
- rotation-round3-corrected.md
- claude-code-prompt.md
