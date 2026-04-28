# EP-488: |A| ≤ 5 PROVED — Two Independent Proofs (Again)
## April 8, 2026

## TWO INDEPENDENT PROOFS OF |A| = 5

### Proof 1 (Codex B): Four new lemmas + exhaustive case analysis
- Lemma 1: Single-obstruction budget > 3n-2m (for s ≥ 4)
- Lemma 2: Bad s=4 → (4,7,3) signature rigidity
- Lemma 3: s=5 is NEVER bad (L_{2,3,5}(t) ≤ t/3)
- Lemma 4: s=6 bad excess < 4a
- Cases: layer 3 bad → all at (4,7,3), S₁+S₂ > E_total;
         layer 4 bad at s=6 → S₁ ≥ 7m > excess;
         single bad layer → first-layer theorem

### Proof 2 (5.4): Top-layer classification + |A|=4 reuse
- Top-layer classification: all 256 obstruction subsets of {2,...,10}
  with size ≤ 4 checked. Only {2,3}∪R with R ⊆ {4,6,8,9,10} bad.
  All equivalent to {2,3} on [1,10]. Signature always (4,7,1,3).
- Case 1 (layer 3 bad): all bad layers at (4,7,3), S₁ ≥ 4m,
  total excess ≤ 9n-6m, 10m-9n > 0 since m > n. ✓
- Case 2b (layer 3 good, layer 5 bad): B₂ > E₅ by the |A|=4
  floor lemma (same signature). Layer 4 paid by S₁ if bad. ✓
- Case 3 (only layer 5 bad): first-layer theorem. ✓

5.4 also CORRECTED my Claude's thoughts error: from a₃ > n/5 you
CANNOT conclude s₂ ≥ 5 (since a₂ < a₃, not a₂ > a₃). The right
fix is the B₂ > E_top mechanism, not the deep single-obstruction surplus.

## THE SIZE LADDER

| |A| | Status | Key mechanism |
|-----|--------|----------------|
| 1 | ✅ | Lean |
| 2 | ✅ | Pairs |
| 3 | ✅ | Single-obstruction + first-layer |
| 4 | ✅ | Witness-count + signature rigidity (2 proofs) |
| 5 | ✅ | Top-layer classification + case analysis (2 proofs) |
| ≥ 6 | ❓ | Open |

## KEY STRUCTURAL INSIGHTS FOR |A| = 6+

1. s=5 is NEVER bad (Codex B's Lemma 3). Dead zone confirmed.
2. Bad layers at s=4 are always (4,7,3) with E = 3n-2m.
3. If layer 3 is bad: ALL subsequent bad layers also at (4,7,3).
4. The B₂ > E_top mechanism works whenever the top layer has (4,7,3).
5. The witness-count bound constrains deeper bad signatures.

## PERCENTAGE: 95%

Two independent proofs. The pattern continues: every |A| we attempt
falls to the witness-count + signature rigidity + case analysis approach.
