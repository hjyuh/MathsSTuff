# EP-488 Round 3 Prompts — CORRECTED (Self-Contained)
## April 4, 2026

Each prompt includes ALL context. No separate updates needed.
Attach v4 .tex to each.

---

## PROMPT FOR: Claude (new chat)

EP-488 (Erdős Problem 488) asks: for every primitive set A, is F(m)/m < 2F(n)/n for all m > n ≥ max(A)?

We PROVED this for all one-anchor families A = {a} ∪ {ka+1,...,ka+t} with a prime. The proof has two parts:
1. First Plateau (Theorem F): G(n) ≥ β on [M, m*) via the Principal-Layer Lemma
2. Post-Peak (Theorem G): no 5/4-rebound past m*, via discrepancy bound |F(x) - δ_A x| ≤ C forcing n < 9C/δ_A, plus finite verification

The full paper is attached (v4).

We then tried to reduce general primitive sets to one-anchor families. THIS FAILED. Computational verification shows {M-1, M} gives ratio ((2M-3)/(2M-2))² ≈ 0.98 for large M, while the best one-anchor family with same max gives only ≈ 0.81. One-anchor families are NOT the worst case. 75,463 counterexamples found across max(A) = 17..50.

EP-488 still HOLDS for all these counterexamples (0.98 < 1). We just can't prove it by reduction.

YOUR TASK: Prove EP-488 DIRECTLY for all primitive sets.

The discrepancy approach works for ANY primitive set A:
- F(x) = δ_A x + h(x) with |h(x)| ≤ C
- If G(m) ≥ (5/4)G(n), algebra gives n < 9C/δ_A
- Below n₀ = 9C/δ_A: finite verification

The key question: what is C for a general primitive set A with |A| = k elements?
- Naive IE: C ≤ 2^k (exponential, useless)
- For primitive sets: higher-order IE terms have lcm > max(A), so they're small
- Target: C = O(k) or O(k²)

If C is polynomial in k, the post-peak argument extends to all primitive sets. The first plateau might not even be needed — if you can show G never drops too far below δ_A for ANY primitive set, the discrepancy bound alone closes EP-488.

Think deep. Return what you proved, what failed, what you recommend.

---

## PROMPT FOR: GPT-5.4 Pro Extended

EP-488 is PROVED for all one-anchor families (paper v4 attached). We tried to reduce general primitive sets to one-anchor — it FAILED.

The singleton-extremal conjecture is FALSE: {M-1, M} gives ratio ((2M-3)/(2M-2))² ≈ 0.98, while the best one-anchor with same max gives ≈ 0.81. 75,463 counterexamples found. EP-488 still holds for all of them.

New target: prove EP-488 DIRECTLY for all primitive sets.

Your periodic deviation reduction G(qL+r) = δ_A + D(r)/(qL+r) works for ANY primitive set, not just one-anchor. The discrepancy bound |F(x) - δ_A x| ≤ C also works for any A.

For a primitive set A with |A| = k: what is C? The naive IE bound gives C ≤ 2^k (exponential). But for PRIMITIVE sets (antichain), higher-order IE terms have lcm > max(A)², so they contribute little. Can you prove C = O(k) or C = O(k²)?

If C is polynomial in k: no 5/4-rebound for n > 9C/δ_A, and finite verification covers the rest. EP-488 would follow for all primitive sets of bounded size, and a compactness argument might close the general case.

Also: the hard cases are SPARSE sets like {M-1, M}, not dense one-anchor families. What structural property of sparse primitive sets prevents the ratio from reaching 1? For {M-1, M}: the maximizer is always n = 2M-3, m = (M-1)², and the ratio is ((2M-3)/(2M-2))² < 1. Can you prove this for all primitive pairs?

Extended thinking ON.

---

## PROMPT FOR: GPT-5.2 Pro Extended

EP-488 is PROVED for all one-anchor families (paper v4 attached). We tried to reduce general primitive sets to one-anchor — it FAILED.

The singleton-extremal conjecture is FALSE. {M-1, M} beats every one-anchor family. The reduction approach is dead.

New target: prove EP-488 DIRECTLY for all primitive sets using the discrepancy method.

Your discrepancy/FKG machinery is model-independent — it works for any set of moduli. Apply it now to GENERAL primitive sets.

Concrete task: For a primitive set A = {a₁,...,a_k} (no divisibility), bound the discrepancy C = sup_x |F(x) - δ_A x|.

Key structural fact: A is an antichain in divisibility. So for any S ⊆ A with |S| ≥ 2: lcm(S) ≥ a₁·a₂/gcd(a₁,a₂) > max(A) (since neither divides the other). This means second-order IE terms have denominators > max(A), contributing O(k²/max(A)) to the density. Higher terms are even smaller.

So: C ≤ k + k(k-1)/(2·max(A)) + negligible ≈ k for large max(A).

Prove this rigorously. Then: no 5/4-rebound for n > 9k/δ_A. Since δ_A ≥ 1/max(A): n₀ ≤ 9k·max(A). For fixed k this is O(max(A)).

The remaining question: can we handle ALL k simultaneously, or does the proof only work for bounded |A|?

Also: apply your fibered FKG to {M-1, M} and verify it gives δ < 2/M (the IE-exact density). This is a sanity check.

Extended thinking ON.

---

## PROMPT FOR: GPT-5.4 xhigh (Codex)

You already proved the singleton-extremal conjecture is false. Next task:

Prove EP-488 holds for ALL primitive PAIRS {a, b} with a < b and a∤b.

Write a script that:
1. For each pair {a, b} with b ≤ 500 and a < b and a∤b:
   - Compute sup_{m>n≥b} G(m)/(2G(n)) up to horizon 10000b
   - Record the worst ratio

2. Report:
   - Overall worst ratio across all pairs
   - Whether it's always < 1 (EP-488 holds)
   - Whether the worst pair is always {b-1, b}
   - Whether the worst ratio matches ((2b-3)/(2b-2))² exactly

3. For the pair {b-1, b}: verify algebraically that n = 2b-3 and m = (b-1)² always gives the maximum, and that the ratio is ((2b-3)/(2b-2))² < 1.

This would give us "EP-488 for all primitive pairs" as a proved theorem.
