# EP-488 CONTINUATION PROMPT — April 5, 2026 (FINAL)
# Paste this at the start of a new Claude chat to resume

## WHERE WE ARE: 89%

EP-488 is 89% proved. The layer decomposition framework is exact and complete.
ONE analytical bound remains — but the precise formulation is still being refined.

## THE LAYER DECOMPOSITION (GPT-5.4 Pro — exact, proved)

F_A(x) = Σ_{j=1}^k K_{Q_j}(⌊x/a_j⌋)

where K_Q(y) = y - F_Q(y) counts integers ≤ y coprime to all elements of Q,
and Q_j is the quotient-core at the j-th peeling step.

Properties: EXACT, POSITIVE, SCALE-INVARIANT, LOCAL (only needs [M, 10M]).

Each layer T_j(x) = (M/x)·K_{Q_j}(⌊x/a_j⌋) oscillates around r_j·ρ_{Q_j}
where r_j = M/a_j and ρ_{Q_j} = 1 - δ_{Q_j}.

EP-488 ⟺ sup(Σ T_j) < 2·inf(Σ T_j) on [M, 10M].

## THE CURRENT OPEN QUESTION

The naive per-layer bound "C^loc_Q(r) < r·ρ_Q/3" is FALSE (Kill #46).
Counterexample: Q = {primes ≤ 30}, r=30. K_Q(30) = 1 but ρ_Q·30 ≈ 4.74.
Individual layers CAN have sup/inf > 2 (the "rough numbers" phenomenon).

BUT: EP-488 still holds for ALL tested sets (23M+ families, zero failures).
The SUM Σ T_j has ratio < 2 even when individual layers don't.

THE REAL QUESTION: What condition on the COLLECTIVE behavior of layers ensures
sup(Σ T_j) < 2·inf(Σ T_j) even when individual layers violate factor-2?

GPT-5.2 Pro suggested: reformulate using ratio bounds |D(y)|/(ρy) instead
of absolute bounds, or target only the positive correction at maximizing residues.

## WHAT'S PROVED (permanent — 19 theorems)

1. EP-488 for ALL consecutive k-tuples (3-line proof: F(2a-1)=k, G≤k/a, 2k/(2a-1)>k/a)
2. EP-488 for ALL primitive pairs (4-line proof)
3. EP-488 for ALL primitive triples (IE comparison R > 0)
4. EP-488 for ALL one-anchor families (Principal-Layer + Post-Peak)
5. EP-488 for ALL sparse sets (Σ1/a ≤ 2/min)
6. EP-488 for ALL compact sets (max ≤ 2min-1)
7. EP-488 coprime tail (product-exponential: 2δ>S₁ or δ>1/2)
8. EP-488 for any fixed k (discrepancy + finite verification)
9. Convexity framework: G(x+L) convex combination → first-period reduction
10. Layer decomposition: F_A = Σ K_{Q_j}(⌊x/a_j⌋) — exact
11. Adjacent pairs exact formula: ((2M-3)/(2M-2))²
12. Consecutive k-tuples formula: (2a-1)/(2(a+k-1))
13. Complement FKG: ρ_Q ≥ Π(1-1/q) ≥ 1/(|Q|+1) [Mahmoud's contribution]
14. Scaling lemma: C_{tB} ≤ C_B+1, δ_{tB} = δ_B/t
15. Primitive Divisor Lemma (Lean-verified): gcd(a,b) ≤ a/2
16. Subset LCM Bound: lcm(S) ≥ 2·max(S)
17. Every concrete primitive set has finite EP certificate
18. 2G(M) > S₁ for all tested sets (627K, zero failures)
19. Extrema stabilize by 10·max(A)

## 46 KILLED APPROACHES

Key kills (each with explicit counterexample):
- Bonferroni-2r for any fixed r (co-atom construction)
- 2δ > S₁ universal (first 21 primes: 2×0.874 < 1.757)
- δ > 1/2 for dense (scaling {2p : p≤73})
- Case A/B dichotomy (scaling gives both failing)
- Any S₁ or δ THRESHOLD (not scale-invariant — scaling slides across)
- Monotonicity by min (44K violations, {4,6,7} beats {4,5,6})
- Element addition decreases ratio (38% violation rate)
- #{S: lcm(S)≤M} ≤ k(k+1)/2 (coprime+one → 2^{k-1})
- Σ|c_d| = O(k²) (exact worst case 2^{k-1})
- C^loc_Q(r) < r·ρ/3 (rough numbers: K_Q(r)=1 for prime cores)

CRITICAL CONSTRAINT: Proof MUST be scale-invariant. No threshold on S₁ or δ works.

## CLEAN CONJECTURE (verified, unproved)

ratio(A) := max G/(2 min G) ≤ 1 - 1/max(A)

800K+ sets, zero violations. Tight at adjacent pairs {M-1, M}.

## LITERATURE LEADS (from Gemini)

1. Montgomery & Vaughan (1986). "On the distribution of reduced residues."
   Annals of Mathematics 123(2), 311-333. Tight variance bounds for coprime counts.
2. Friedlander & Iwaniec. Opera de Cribro. Fundamental Lemma of Sieve Theory.
3. Hall & Tenenbaum. Divisors (1988). Ch.5: density of sets of multiples.
4. Iwaniec (1978). Jacobsthal bound j(Q) ≤ c·(log Q)².
5. Gasharov-Peeva-Welker. LCM lattice shellability.

## MODELS IN ROTATION

1. GPT-5.4 Pro Extended — structural proofs, all major kills, layer decomposition
2. Claude Code — computation, consecutive k-tuples proof
3. Codex xhigh — ratio analysis, formula discovery, verification
4. GPT-5.2 Pro Extended — analytic bounds (killed local discrepancy lemma, offered reformulation)
5. Gemini — literature search ONLY (found Montgomery-Vaughan, Hall-Tenenbaum)

## KEY FILES

Paper: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\paper\ep488-paper-v6.1.tex
Layer framework: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\layer-decomposition-framework.md
Scale invariance: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\scale-invariance-constraint.md
Clean conjecture: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\clean-conjecture.md
Kill #46: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\kill46-local-discrepancy.md
Gemini findings: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\gemini-jacobsthal-findings.md
All prompts: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\

## NEXT STEPS

1. Send GPT-5.2 Pro the reformulation request (it offered to reformulate the
   discrepancy bound into one that's true AND sufficient for the layer sum)
2. Deploy Codex on layer verification (codex-layer-prompt.md ready)
3. Send GPT-5.4 Pro the collective-layer question: when do individual layer
   violations get rescued by the sum?
4. Consider: the "rough numbers" dip (K_Q(r) = 1 for prime cores) happens
   at x = M where T_j = 1. But at x = 2M: T_j ≈ ρ·r/2, much larger.
   The SUM might have its inf at x > M where individual layers have recovered.

## COMPUTATIONAL VERIFICATION

23M+ families direct EP-488: zero failures
800K+ ratio ≤ 1-1/M: zero violations  
627K 2G(M) > S₁: zero failures
C_local/k < 2: zero violations (50K sets)
Worst ratio: 0.997 at {50, 51}
