# EP-488 Round 4 Prompts — Dense k≥4 Generalization
## April 4, 2026

Each prompt is self-contained. Attach v5 .tex to each.

---

## PROMPT FOR: Claude Code

Read C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\claude-code-prompt.md for background, then read C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\session3-final-status.md for current status.

EP-488 is proved for |A| ≤ 3, one-anchor families, and sparse sets. The remaining gap is dense primitive sets with |A| ≥ 4.

You already proved the IE comparison R = S1 - 2S2 > 0 for triples. Now extend it.

TASK 1: Check whether R = S1 - 2S2 > 0 for ALL primitive quadruples {a,b,c,d}. The Primitive Divisor Lemma gives 1/lcm(x,y) ≤ 1/(2·max(x,y)) for each pair. There are 6 pairs in a quadruple. Compute 2S2 using these bounds and check if S1 - 2S2 > 0 always.

If R > 0 for quadruples: EP-488 for k=4 follows by the same discrepancy tail (C < 8) + early range verification. Prove it.

If R ≤ 0 for some quadruple: find the counterexample. Then try the DIRECT approach: for that specific quadruple, does 2G(n) > G(m) still hold? The sparse-mass lemma might cover it, or a direct density argument.

TASK 2: For what k does R = S1 - 2S2 become negative? You found k=10 (first 10 primes). But those are SPARSE — the sparse-mass lemma handles them. Check: among DENSE primitive sets (Σ1/a > 2/min(A)), does R ever go negative for k=4? k=5? k=6?

TASK 3: If R > 0 for all dense sets up to some k₀, and sparse sets are handled by the sparse-mass lemma, then EP-488 holds for all |A| ≤ k₀. Find the largest such k₀.

---

## PROMPT FOR: GPT-5.4 Pro Extended

EP-488 is proved for |A| ≤ 3, one-anchor families, and sparse sets (paper v5 attached). The remaining gap is dense primitive sets with |A| ≥ 4.

You found the quotient-core recursion and the sparse-mass lemma. Now push toward the full result.

The IE comparison R = S1 - 2S2 works for triples but fails at k=10 (first 10 primes). However, the failure is in the SPARSE regime — those sets are already handled.

KEY QUESTION: In the DENSE regime (Σ1/a > 2/min(A)), is R = S1 - 2S2 always positive? Dense primitive sets have many elements clustered near min(A). The Primitive Divisor Lemma gives lcm(a,b) ≥ 2·max(a,b). For clustered elements near some value M, the pairwise lcms are ≥ 2M, so S2 ≈ k²/(4M). Meanwhile S1 ≈ k/M. So R ≈ k/M - k²/(2M) = k(1-k/2)/M. This goes negative at k ≥ 2, which seems wrong...

But wait: the bound 1/lcm ≤ 1/(2·max) is tight only when gcd = max/2 exactly. For random primitive pairs, lcm is much larger. Can you get a tighter average bound on S2 that keeps R > 0 for larger k?

Alternatively: your quotient-core recursion peels off min(A) and reduces to a smaller set. Can you show that EP-488 for A follows from EP-488 for A' = A\{min(A)} plus a bounded correction? If the recursion preserves EP-488 with only O(1) deterioration, induction on k works.

Extended thinking ON.

---

## PROMPT FOR: GPT-5.2 Pro Extended

EP-488 is proved for |A| ≤ 3, one-anchor families, and sparse sets (paper v5 attached).

You proved the Parseval obstruction: C can be 2^(k/2) for k large primes. But those are SPARSE — handled by the sparse-mass lemma.

NEW QUESTION: Prove C = O(k²) specifically for DENSE primitive sets (Σ1/a > 2/min(A)).

The intuition: dense sets have heavy overlap. The IE fractional parts interfere destructively, keeping the deviation small. Empirical data: C < 3 for every dense set tested (hundreds of thousands).

Your Parseval proof used k pairwise coprime primes. Dense primitive sets CANNOT be pairwise coprime (they'd be sparse). The shared prime factors create cancellation in the Fourier coefficients that kills the 2^(k/2) growth.

Specifically: for the Parseval argument, you needed |ĝ(r_S)| ≥ 1/(8π) for EVERY subset S. This works because the moduli are coprime, so every subset gives an independent frequency. For dense sets with shared factors, many subsets map to the SAME frequency (because lcm(S) can equal lcm(S') for different S, S'). The Fourier coefficients ADD with alternating signs, canceling.

Can you prove that for dense primitive sets, the Fourier coefficient cancellation forces C = O(k²) or even O(k)?

Also: your fibered FKG bound improved δ_B by ε = 0.0135 for one-anchor families. Can you compute the fibered FKG bound for a dense quadruple like {3,4,5,7}? If the fibered bound gives δ close to the true density, it might provide a tighter density ceiling that helps the direct argument.

Extended thinking ON.

---

## PROMPT FOR: GPT-5.4 xhigh (Codex)

EP-488 is proved for |A| ≤ 3, one-anchor, and sparse sets.

TASK 1: Extend the IE comparison to k=4.
For every primitive quadruple {a,b,c,d} with d ≤ 100 and Σ1/a > 2/a (dense):
- Compute R = S1 - 2S2 where S2 = Σ 1/lcm(a_i,a_j) over all 6 pairs
- Report whether R > 0 always
- If R ≤ 0 for any quadruple: report which one

TASK 2: For the same quadruples, compute the discrepancy C = max_x |F(x) - δ_A x| up to x = 10000·max(A).
- Report max C across all dense quadruples
- Is C always < 8? Always < 4?

TASK 3: For k=5,6,7: same tests but with max ≤ 50.
- At what k does R first go negative for a DENSE set?
- How does max C grow with k for dense sets?

TASK 4: Directly verify EP-488 for all dense quadruples with max ≤ 100.
- Compute sup G(m)/(2G(n)) for each
- Report worst ratio and whether it's always < 1

Write Python, run everything, report results.
