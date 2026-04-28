# EP-488 Model Rotation — Round 1 Prompts
## April 3, 2026

## Model 1: GPT-5.4 Pro Extended — TARGET: (RQ_q) Rowwise Bound

PROMPT:
---
Attached is a paper on Erdős Problem 488. Read the full paper. Sections 1-4 contain proved results — do NOT re-derive them.

Your specific target is Conjecture 5.5 (the Rowwise Quota Bound):

For every active q ≥ 2 in the pre-peak range, prove:
C_q(x) ≤ E_{q-1}(x)

where C_q counts row-q collisions with earlier rows, and E_{q-1} counts elements in the adjacent two-hit band J_{q-1}.

The exact collision structure (Section 5.3): for rows q > r with g = gcd(q,r), collisions occur in lattice sets with density 1/lcm(q,r). The collision condition is r > kq/(k+1). For k=2: only r > 2q/3.

Key facts you can use:
- The quota-capacity identity W(x) - t = E(x) - C(x) is PROVED (Theorem 5.1)
- Pre-peak windows have at most 5 active rows (Theorem 5.6, conditionally on m* < m6)
- The pair-sum bound Σ|S_{q,r}| ≤ E_{q-1} is FALSE (counterexample at (31,2,24,380,8))
- Hall/SDR is the WRONG abstraction (killed, Section 7.5)
- Componentwise charging FAILS ((29,2,26,360) has component with surplus -2)

(RQ_q) holds in every exact pre-peak wide window for prime a ≤ 61, k ∈ {2,3,4}. It fails outside pre-peak exactly where expected.

Think deep. Try every approach. Return what you proved, what you tried and why it failed, and what you recommend next.

Extended thinking ON.
---


## Model 2: GPT-5.2 Pro Extended — TARGET: Post-Peak Bound

PROMPT:
---
Attached is a paper on Erdős Problem 488. Read the full paper. Sections 1-4 contain proved results — do NOT re-derive them.

Your specific target is the Post-Peak Coarse Bound (Conjecture 5.8):

Prove: sup_{n ≥ m*} E(n)/(2G(n)) ≤ c₀ for some universal c₀ < 2/3,
where E(n) = sup_{m>n} G(m) is the future envelope.

Computational evidence: worst observed post-peak ratio is 0.5984. Target c₀ = 5/8 = 0.625.
Note: c₀ = 3/5 is NOT universal (counterexample (a,k,t)=(3,3,2) gives 0.6071).

Key insight from Section 7: window-capacity bounds that failed for EP-488 (threshold 1) may work HERE because the threshold is only 0.625. The per-window density ceiling is ≈ 0.5, which is below 0.625.

Also useful: in the post-peak region, G(x) is "mostly decreasing" with O(1/x) oscillations. Any 6/5-factor rebound forces local density d(n,m) ≥ G(n)(6/5 + n/(5L)) where L = m-n.

The α-start lemma (Theorem 3.3) already covers all starts where 2G(n) ≥ α_A. So the post-peak bound only needs to handle starts where G(n) < α_A/2 ≈ 0.2.

Think deep. Try every approach. Return what you proved, what you tried and why it failed, and what you recommend next.

Extended thinking ON.
---


## Model 3: Gemini 3.1 Pro — TARGET: Fresh Eyes, Find New Route

PROMPT:
---
Attached is a paper on Erdős Problem 488. Read the entire paper carefully, including the 31 killed approaches in Section 7.

I am NOT giving you a specific target. Instead, I want you to:

1. Read everything.
2. Identify what the paper is missing — structural insights, connections to other areas of math, proof techniques that weren't tried.
3. Either push one of the existing open targets (Section 8) as far as you can, OR propose a completely new proof route that avoids all 31 killed approaches.

The single most important meta-observation (Section 7.6): every killed approach is "primitivity-blind" — none uses the fact that A is an antichain in the divisibility order. But EP-488 is false for non-primitive sets. The proof MUST use primitivity.

Questions to consider:
- Is there an order-theoretic or lattice-theoretic approach using the antichain structure?
- Can Dilworth's theorem or Mirsky's theorem on posets contribute?
- Is there a connection to the Sunflower lemma or delta-systems?
- Can the problem be reformulated as an optimization problem on antichains?
- Is there an information-theoretic or entropic argument?

Think deep. Return what you tried, what worked/didn't, and your strongest recommendation for the next step.
---


## Model 4: Claude (Different Chat) — TARGET: Prove First Plateau Directly

PROMPT:
---
Attached is a paper on Erdős Problem 488. Read the full paper. Sections 1-4 contain proved results — do NOT re-derive them.

Your target: prove the First Plateau Lemma (Conjecture 5.7) by ANY route, not necessarily through (RQ_q) or the peak-location bound.

The First Plateau says: for wide one-anchor families (t > 2√a), G(n) ≥ β for all M ≤ n < m*, where β = G(2ka-1) and m* is the first peak of G.

What's already proved:
- Base strip: G(n) ≥ β on [2ka-1, 4ka-1] (Theorem 3.7)
- Quota-capacity identity: W(x) - t = E(x) - C(x) (Theorem 5.1)
- Window Lemma W(x) ≥ t propagates base strip if proved

What's been tried and killed for this specific lemma:
- Global W(x) ≥ W(0): false at a=331 (but true pre-peak)
- Hall/SDR: wrong abstraction
- Fsharp upper envelope: too coarse
- Peak-location via Fsharp: counterexample at (107,91)

Consider approaches that DON'T go through the Window Lemma:
- Direct induction on the pre-anchor dips G(ra-1)
- Discrepancy bounds for H_B(x) on short intervals
- A convexity or monotonicity argument on the "dip sequence" G(2ka-1), G(3ka-1), G(4ka-1), ...
- Layer-by-layer analysis of the multiplication table up to the peak

Think deep. Try every approach. Return what you proved, what you tried and why it failed, and what you recommend next.
---
