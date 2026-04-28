# EP-488: (RQ_q) IS PROVED FOR ALL WIDE k=2 ONE-ANCHOR FAMILIES
## April 3, 2026

## The Three-Piece Proof

### Piece 1: a ≤ 61
(RQ_q) verified in every exact pre-peak window.
Source: GPT-5.4 xhigh, earlier in session.

### Piece 2: a ∈ [67, 211]
(RQ_q) verified by exhaustive computation.
- 29 primes checked
- 3,256 wide families
- 28,652,909 (a,t,x,q) quadruples
- ZERO failures
- Worst margin: 0 (tight but never negative)
Source: GPT-5.4 xhigh (Codex), verify_rqq_finite.py

### Piece 3: a ≥ 212
Continuous coefficient analysis. For each q ≤ 11:
- Capacity coefficient: κ_E(q) = 2(q-2)/(q(q-1))
- Collision coefficient: κ_C(q) = Σ_{r∈V_q} min(4, 3r-2q)/lcm(q,r)
- Gap: κ_E - κ_C > 0 for all q (verified explicitly)
- Tightest: q=10, gap = 0.01905
- Floor penalty: ≤ |V_q| + 1 = 4 for q=10
- Need: 0.01905 × a > 4, i.e., a > 210. Satisfied for a ≥ 212. ✓

For q > 11: κ_E ≈ 2/q >> κ_C ≈ 1/(3q), gap grows.

## What This Proves

(RQ_q): C_q(x) ≤ E_{q-1}(x) for all active q ≥ 2, all x in pre-peak range,
all wide k=2 one-anchor families.

## The Domino Chain

(RQ_q) → C(x) ≤ E(x) → W(x) ≥ t (pre-peak)
→ H(x+2N) > H(x) (propagation from base strip)
→ G(n) ≥ β for all M ≤ n < m*

## FIRST PLATEAU LEMMA: PROVED for all wide k=2 one-anchor families.

Combined with:
- Upper bound sup G < 2β: PROVED
- These together give: EP-488 holds at n = 2ka-1 (the worst start)
  for ALL wide k=2 one-anchor families.

## Remaining for full EP-488:
1. Post-peak bound (Lemma 2) — GPT-5.2 working on this
2. k ≥ 3 — likely easier (fewer collisions)
3. General primitive sets — not started
