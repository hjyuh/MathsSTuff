# EP-488: |A| ≤ 5 PROVED — THREE Independent Proofs
## April 8, 2026

## THREE INDEPENDENT PROOFS

### Proof 1 (Codex B): Four lemmas + exhaustive cases
Key: Lemma 3 (s=5 never bad), Lemma 4 (s=6 excess < 4a)
Cases split by first bad layer location.

### Proof 2 (5.4): Top-layer classification + |A|=4 reuse  
Key: All 256 obstruction subsets checked. B₂ > E_top reused from |A|=4.
Corrected Claude's s₂ ≥ 5 error.

### Proof 3 (5.2): Explicit periodicity bounds + worst-case summing
Key: max_{t≥6}(7L₃₀(t)-2t) = 4 gives E < 4a for s=6.
Layer 5 at s≥6 killed by t₅ ≤ 10.
Total worst excess < 11n/12. S₁ ≥ 4m > 37n/12. Done.

## THE SIZE LADDER (rock solid)

| |A| | Status | Proofs |
|-----|--------|--------|
| 1   | ✅ | Lean |
| 2   | ✅ | Pairs |
| 3   | ✅ | Codex B |
| 4   | ✅ | 5.2, 5.4 |
| 5   | ✅ | Codex B, 5.4, 5.2 |
| ≥ 6 | ❓ | Open |

## ACCUMULATED TOOLS FOR |A| = 6+

Dead zones (layers that are NEVER bad):
- s ≤ 3: self-funding
- s = 5: L_{2,3,5}(t) ≤ t/3 (Codex B Lemma 3)

Signature rigidity:
- s = 4 bad: ONLY (4,7,3), E = 3n-2m < n/4
- s = 6 bad: E < 4a ≤ 2n/3

Key bounds:
- S₁ ≥ 4m whenever any bad layer exists
- S₂ > 0 always (single-obstruction safety)
- S₂ > 2m when s₂ ≥ 5 (deep single-obstruction surplus)
- B₂ > E_top whenever top layer has (4,7,3)
- Witness-count: π(s_j) ≤ j-1

## PERCENTAGE: 95%

Three independent proofs. The tools accumulate with each |A|.
The pattern is clear and the next step (|A| = 6) is well-posed.
