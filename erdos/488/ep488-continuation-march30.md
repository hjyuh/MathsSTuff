# EP-488 CONTINUATION PROMPT — March 30, 2026

## WHAT THIS IS

Continuation of a two-day research session on Erdős Problem 488: prove f_A(m)/m < 2f_A(n)/n for all primitive A and m > n ≥ max A. Reduces to pair-tail split inequality via Chojecki's Conjecture 4.8.

## THE COMPLETE PROVED CHAIN

**Theorems 1-20 (proved across March 29-30):**

1-6: Quotient-tail correction → positivity → periodicity → finite obstruction → off-slab closure → visible-slab reduction (V1,V2,V3)
7-8: F=2,3 harmless → F=4 exceptional family
9: Sub-exceptional (48k,54k,{64k,72k,81k}) closed via scaling law + 540-window
10-12: Window-bound theorem → half-scale reduction → weak charging
13-19: Hitting-time → delay condition → CRT obstruction → deletion drought
20: **POSITIVE-SUM DECOMPOSITION** (the key new result):
    F(n) = A_{Q_ℓ}(w) + A_{Min(Q_a∪{A})}(u) + A_{Min(Q_b∪{B})}(v)
    Three non-negative counting functions. Verified 1,805 systems.

**Bridge Lemma B′ (unconditional, proved March 30):**
    A_Q(y)/y ≤ δ_Q + sum_{q>y} 1/q + W+_{Q≤y}/y

## THE REMAINING GAP

The refined sufficient condition:

    sum_{q>y} 1/q + W+_{Q≤y}/y < a·α(s)

holds computationally across 2,648+ systems with 69%+ margins. NOT YET PROVED.

## KILLED APPROACHES (13 total)

Each with explicit counterexample:

1. Envelope H_j reductions (×5): never closes
2. Two-route via Prop 5.1: G = first 14 primes, n=198
3. Peak absorption: (4,13,{15,17,19})
4. Strong charging +1: (67,71,{73,75,76,78,79})
5. Universal peak/δ: (2,3,T) many primes
6. Per-residue W+: (11,15,{28,31}) at s=43
7. W+ < 5: (5,11,{16,17,18})
8. 2^k active bound: most Q
9. Trivial bound 1/a+1/b: (4,6,{9,10}) at s=41
10. Bridge B (A_Q(x)/x ≤ C*·δ_Q): Q={2,3} at x=1
11. Option I (W+_R ≤ y·sum(1/r)): R={19,20,21,22,23}, ratio 1.465
12. Option II (|Q_{≤y}| ≤ C): (6,8|{9,10,14,29}), |Q_{≤5}|=3; unbounded family
13. Cardinality |Q| < 2F(s)-δs: (14,36|{45,50,62,64}), |Q_a^ex|=5

## STRUCTURAL LEMMAS (proved, usable)

- Lemma A: gcd(t,a) ≤ a/2 by primitivity, so q_a(t) ≥ 2t/a
- Lemma B: active q ≤ y requires t ≤ (a/2)·y
- Corollary: tail sum bound via 1/q ≤ a/(2t)
- Bridge B′: A_Q(y)/y ≤ δ_Q + sum_{q>y} 1/q + W+_{Q≤y}/y

## EXTERNAL ENGAGEMENT

**Terence Tao (March 30, 07:29):**
- Worst-case ratio ~1.031 using primes between n^{1/3} and n^{1/2}
- "doesn't look like it gets close to 2"
- Pointed to Granville-Soundararajan paper
- "alternating sums of various integrals, which looks somewhat complicated"

**Chojecki (March 30, 14:45):**
- "computational search paired with Terence Tao remark... should result in something new, but I don't know if this would give full resolution (but maybe)"
- Has our PDF/tex/verification code

**G-S gap:** Their framework is for multiplicative functions. Our Q-free sieve is combinatorial (non-multiplicative when Q contains composites). Bridge lemma needed.

**Ruzsa 1982 ("Sifting by composite numbers"):** Handles composite moduli but gives asymptotic extremal bounds, not periodic oscillation control.

## WHAT THE NEXT SESSION SHOULD DO

1. **Monitor forum:** Check for new replies from Tao or Chojecki. If Tao engages further, his analytic perspective may spot the closing argument.

2. **Try a completely new approach to the refined condition.** All simple structural bounds have been killed. The proof must use something deeper about quotient-tail arithmetic — possibly:
   - The interaction between ALL THREE streams simultaneously (not just one-stream dominance)
   - The specific structure of Q = Min(Q_a ∪ {A}) where A = ℓ/a
   - Fourier/character-sum methods on the periodic correction
   - Adapting G-S Lipschitz estimates to periodic (rather than multiplicative) sieves

3. **Consider whether the problem splits into cases** by the size of |Q_{≤y}|. When |Q_{≤y}| = 0 (93.8% of systems), the condition is trivially satisfied. The hard cases are |Q_{≤y}| ≥ 1. Maybe prove a bound conditional on the structure of the active moduli.

4. **Formalize what we have.** Even without the final step, the reduction chain + positive-sum decomposition + 13 killed approaches is a substantial contribution. Consider writing a formal paper with the reduction chain and the computational evidence, flagging the refined sufficient condition as a conjecture.

## KEY FILES

- ep488_current_candidate_proof.md — full proof write-up (v3)
- ep488_chojecki.pdf/.tex — LaTeX document sent to Chojecki
- ep488_verification.py — computational verification code
- subexceptional-48-54-charging.md — window-bound proof
- window-bound-general-theorem.md — general window theorem
- bridge2-FROZEN.md, bridge1-pair-FROZEN.md — earlier approaches (frozen)
- All in C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\

## MODELS CONSULTED (10+)

Claude Opus 4.6 (orchestrator), GPT 5.2 Pro (×3, best results: positive-sum decomposition, structural lemmas A/B, killed Options I/II/Bridge B), GPT 5.4 Pro (×3, deletion drought, active/inactive), Gemini 3.1 Pro, Gemini Deep Research, Claude Deep Research (hallucinated "trivial bound closes" — FALSE), Codex xhigh

## PROBABILITY

EP-488 overall: **88%**. Down from 91% after three proof routes killed today. The refined sufficient condition holds with massive margins but the right formulation for proving it hasn't been found. Tao/Chojecki engagement is the strongest positive signal.

*Last updated: March 30, 2026, 5:00 PM CT*
