# Erdős Problem 509 — Perfect Run Output
# March 20, 2026 — GPT 5.4 Pro

## THE BRIDGE LEMMA (Section 5.2)

For monic f of degree d, let E(f) = ⊔ E_j be the connected components.

**Component-capacity subadditivity conjecture:**
  Σ_j cap(E_j) ≤ cap(E(f)) = 1

If true, then:
- Each E_j is a continuum, so diam(E_j) ≤ 4·cap(E_j) [Pólya-type]
- Cover each E_j by one disk of radius diam(E_j)/2 ≤ 2·cap(E_j)
- Sum: τ(f) ≤ Σ_j 2·cap(E_j) ≤ 2 ✅

## WHY THE CONNECTED CASE WORKS
- cap(E(f)) = 1 for monic polynomials (Green function normalization)
- For continua: diam(K) ≤ 4·cap(K) [Barnard-Pearce-Solynin]
- Connected E is one continuum → one disk of radius 2 covers it
- SHARP: segments of length 4 are extremal

## WHY IT BREAKS FOR DISCONNECTED
- Capacity does NOT control sum of component sizes
- The failure is CAPACITY BUDGETING, not geometric spacing
- Need: Σ cap(E_j) ≤ 1 for polynomial lemniscate components

## STRONGER CONJECTURE (degree-weighted)
For E_j containing k_j zeros (Σ k_j = d):
  cap(E_j) ≤ k_j / d
This immediately gives Σ cap(E_j) ≤ 1.

Motivation: harmonic measure on ∂E(f) pulled back from |w|=1 under f
gives mass k_j/d to ∂E_j. Converting harmonic measure to capacity
bound is a standard potential theory move.

## COMPUTATIONAL EVIDENCE (degrees 2-4)
- No disconnected lemniscate found with τ > 1.38
- Worst case: "just barely disconnected" (near Cassini oval transition)
- More components → smaller τ (each component shrinks fast)
- Strongly supports τ ≤ 2 conjecture

## NEXT STEPS
1. Get Pommerenke 1959 + 1961 papers (Michigan Math J)
2. Prove or disprove: Σ cap(E_j) ≤ 1 for polynomial lemniscate components
3. If that's known in potential theory literature, problem is SOLVED
4. Literature search: capacity subadditivity for polynomial sublevel sets

## Connection distance: 4-5
## Estimated tractability: HIGH
## The bridge lemma might already be a known theorem in potential theory
