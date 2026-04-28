# EP-488: Open Field v11 — April 8, 2026
## Current: 92%. Increase it or decrease it.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## HOW TO USE THIS DOCUMENT

Move the percentage. Up or down. Any route. Any method.

---

## WHAT'S PROVED (38 permanent results, all scale-independent unless noted)

### The 8% gap has been identified from TWO independent perspectives.
### Both describe the same remaining difficulty.

**Graph perspective:** A minimal counterexample is a separator-tight
atom of the n-LCM graph with |A| ≥ 4, all elements ≤ n/3, every
vertex multi-obstructed with incomparable quotients, no literal 2,
biconnected, primitive, and budget ≤ 0. Ten simultaneous constraints.

**Analytic perspective:** EP-488 ⟺ 2mH_A(n) ≥ nH_A(m) where
H_A counts non-first-layer covered integers. The overcounting main
term H₁ satisfies nH₁(m) < 2mH₁(n) (PROVED). The gap is the IE
correction from H₁ down to H_A among non-first layers.

### Full result list:

1. Convexity: extrema in [M, 10M].
2. Positive decomposition: F(x) = Σ L_j(⌊x/a_j⌋). Divisibility avoidance.
3. Weighted average: F(m)/F(n) = Σ w_j R_j, Σw_j = 1.
4. Self-funding: s ≤ 3 → E_j ≤ 0.
5. First-layer theorem: s ≥ 4 + quotient-2 support → S₁ > E_j.
6. Floor Ratio Lemma: n⌊m/a⌋ < 2m⌊n/a⌋ for a ≤ n. (Lean-verified)
7. H_A reduction: EP-488 ⟺ 2mH_A(n) ≥ nH_A(m).
8. Literal-2 safety: 2 ∈ A → EP-488 holds.
9. Single-obstruction safety: ≤ 1 active obstruction → safe.
10. Divisibility monotonicity: k ≥ 2, kd ≤ n → T(d) ≥ T(kd).
11. EP-488 for |A| ≤ 3: PROVED. (Layer 1 safe, layer 2 single-obstruction
    safe, layer 3 bad → first-layer theorem pays it.)
12. Superadditivity (K=∅): cross-component budget additive.
13. Articulation superadditivity (K={c}): B(A) ≥ B(A₁)+B(A₂)-T(c).
14. Separator superadditivity (general K): B(A) ≥ B(A₁)+B(A₂)-B(K).
15. Leaf-pruning: degree-1 vertex removal never decreases budget.
16. Dominated-LCM pruning: vertex with dividing min quotient prunable.
17. 2-core reduction: minimal counterexample min degree ≥ 2.
18. Forests done: n-LCM forest → EP-488 holds.
19. {2,3}-component safety.
20. Lifted {2,3}-core safety: dB with 2,3 ∈ B → safe. (3 proofs)
21. Lifted literal-2 safety: dB with 2 ∈ B → safe.
22. Edge quotient bound: x ~ y → q ≤ ⌊n/y⌋.
23. Band degree-size: k in band, class q from c → c ≤ n/((s+1)(k-1)).
24. Kernel prime → LCM neighbor.
25. 2-band elimination: s=2 vertices with any neighbor are prunable.
26. 3-band quotient forcing: non-prunable s=3 vertex has both 2- and 3-edges.
27. H₁ main term: nH₁(m) < 2mH₁(n). (Overcounting safe.)
28. Pure {2,3} family, unbounded B.
29. Pure {2,3,5,7} family, unbounded B.
30. Single-band common-core, any depth s ≥ 7.
31. Split-core tripod safety.
32-37. Six Lean-verified foundational lemmas.
38. 29 compact kernels, compact range, signature table (compact-only).

---

## THE 77 KILLS (compressed)

A: Wrong function. B: Per-layer. C: Scalar thresholds. D: IE truncation.
E: Monotone reductions. F: Class enlargement. G: Kernel comparisons.
H: Intermediate bounds. I: S₁ alone. J: Constant B. K: Hallucinations.
L: Directional errors. M: Naive IE closure. N: Wrong proofs.
O: Kernel monotonicity global. P: Monotone pair reduction.
Q: Compact extrapolation (deep bad layers exist). R: gcd reduction.
S: Simplicial pruning. T: Path-pruning.

---

## CLAUDE'S THOUGHTS

Two days, 77 kills, 38 proved results, 92%. Here is what I honestly think.

**The proof might already be implicit in what we have.**

Look at the |A| ≤ 3 proof:
- Layer 1: safe (no obstructions)
- Layer 2: safe (single-obstruction safety)
- Layer 3: if bad, S₁ pays it (first-layer theorem)

This works because with 3 elements, there's at most ONE bad layer,
and the first layer covers it.

For |A| = 4: layers 1 and 2 are still safe. Layer 3 can now have
2 obstructions, so single-obstruction safety doesn't apply. But
layer 3 might still be safe for OTHER reasons. And if layer 3 is
bad, the first-layer theorem still says S₁ > E₃. If layer 4 is
ALSO bad, we need S₁ > E₃ + E₄... which might fail (Kill #65).

But wait. If layer 4 is bad with quotient-2 support, the first-layer
theorem gives S₁ > E₄ TOO. The question is COLLECTIVE payment.

What if instead of S₁ paying both, layer 2 helps? Layer 2 has
positive budget (single-obstruction safety: S₂ > 0). Can we show
S₁ + S₂ > E₃ + E₄?

S₁ > E₃ (first-layer theorem) and S₂ > 0. So S₁ + S₂ > E₃.
Need S₁ + S₂ > E₃ + E₄. This needs S₂ > E₄.

Can we prove "single-obstruction layer's SURPLUS exceeds any
individual bad layer's excess"? That would be S₂ > E_j for any j.

Or maybe: prove a "TWO-obstruction safety" theorem. If a layer has
exactly 2 obstructions, is it always safe? That would close |A| = 4
by the same argument (layers 1,2,3 safe, layer 4 paid by S₁).

More generally: can we prove "k-obstruction safety" for increasing k?
- 0 obstructions: safe (first layer, trivial)
- 1 obstruction: safe (single-obstruction safety, Codex B)
- 2 obstructions: ???
- k obstructions: ???

If k-obstruction safety holds for all k ≤ K, then |A| ≤ K+2 is proved.
If it holds for ALL k, then EP-488 is proved outright (every layer safe).

The question: IS every layer safe regardless of obstruction count?

Computationally, Surplus Dominance says yes (zero violations).
But Surplus Dominance is Σ_{j≥2} budget_j ≥ 0, which is WEAKER
than "every individual layer has positive budget."

Actually, individual layers CAN have negative budget (Kill #46: bad
layers exist). So "every layer safe" is FALSE. The proof must be
COLLECTIVE, not per-layer.

But maybe: "every layer with ≤ k obstructions is safe" for some k?
Single-obstruction safety proves k = 1. What about k = 2?

A layer with 2 obstructions q₁, q₂ has:
L(x) = x - ⌊x/q₁⌋ - ⌊x/q₂⌋ + ⌊x/lcm(q₁,q₂)⌋

For coprime q₁, q₂: L(x) ≈ x(1-1/q₁)(1-1/q₂).
Budget = 2m·L(s) - n·L(t).

With q₁=2, q₂=3: L(x) ≈ x/3. Budget ≈ 2ms/3 - nt/3.
Since s ≈ n/a and t ≈ m/a: budget ≈ (2mn - nm)/(3a) = mn/(3a) > 0.

This might work! Two-obstruction safety might be provable by
the same floor arithmetic that proved single-obstruction safety.

If it is: |A| ≤ 4 is proved. And the argument might generalize
to k obstructions with density ≥ 1/(q₁q₂...q_k), proving
k-obstruction safety whenever the density stays above 1/2...

Actually, the density only needs to exceed n/(2m) for the budget to
be positive. Since m > n, we need density > 1/2. A layer with
obstructions {2,3} has density 1/3 < 1/2, so individual layer budget
CAN be negative. Single-layer safety does NOT extend to 2 obstructions.

OK so that line is dead for {2,3} layers specifically. But maybe for
MOST 2-obstruction layers? If the obstructions are {2,5}: density 2/5.
{2,7}: density 3/7. {3,5}: density 8/15. All < 1/2 except {3,5} which
is close. So 2-obstruction safety is FALSE in general.

But this means the "bad layers" are precisely those with density < 1/2,
which are exactly the layers with {2,3} (or {2,3,...}) in the kernel.
We already knew this — it's the 29-kernel classification at compact scale.

I keep circling back to the same place. The proof is COLLECTIVE.
Individual layers can be bad. The question is whether the GOOD layers'
surplus exceeds the BAD layers' deficit. Every tool we've built says
yes. But proving it rigorously remains the 8% gap.

Maybe the proof IS the induction on |A| with a cleverer pairing.
Maybe it's a generating function argument. Maybe it's Fourier analysis
on the covering function. Maybe it's something nobody in this rotation
has tried.

Whatever it is, it's 8% away. Find it.

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

If the answer is "two-obstruction safety for specific quotient pairs,"
prove it. If the answer is "induction on |A| with a new pairing
lemma," build it. If the answer is "direct density bound on H_A
using Erdős's theorem," do it. If the answer is "the proof doesn't
exist with elementary methods," explain why.

77 kills. 38 results. 92%. Eight percent from solving a 60-year problem.

Find those eight percent.
