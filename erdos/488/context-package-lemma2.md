# EP-488: Context Package for Fresh Model — Post-Peak Bound (Lemma 2)

## The Problem (2 lines)
Let A be a primitive set (no element divides another). Define F(x) = |{n ≤ x : a|n for some a ∈ A}|.
EP-488: Is F(m)/m < 2·F(n)/n for all m > n ≥ max(A)?

## What's Proved
1. **a=2 case:** All primitive sets with 2 ∈ A satisfy EP-488. (Proof: F(m)/m < 1 ≤ 2F(n)/n.)
2. **Thin regime:** For A = {a} ∪ {ka+1,...,ka+t} with a prime, k≥2, t ≤ 2√a: EP-488 holds. (Three-layer proof: local range + collision-free layers + pair-collision bound.)
3. **Upper bound:** For one-anchor families, sup_{x≥M} G(x) ≤ 1/a + t/(ka+1) < 2·G(2ka-1).
4. **α-start lemma:** If 2G(n) ≥ α_A := 1/a + Σ 1/(ka+i), then EP-488 holds for all m > n.
5. **Long-rebound lemma:** Short-interval rebounds after α_A/2 crossing are impossible.

## The Two-Lemma Endgame (your task is Lemma 2)

Let m* = earliest maximizer of G(x) on [M,∞).

**Lemma 1 (First Plateau):** G(n) ≥ G(2ka-1) for all M ≤ n < m*. [Being worked on separately.]

**Lemma 2 (Post-Peak Coarse Bound) — YOUR TASK:**
Prove: sup_{n ≥ m*} E(n)/(2G(n)) ≤ c₀ for some universal c₀ < 2/3.

Where E(n) = sup_{m>n} G(m) is the future envelope.

**Why c₀ < 2/3 suffices:** The first-plateau ratio E(2ka-1)/(2G(2ka-1)) is always ≥ 0.66 computationally. If post-peak ratio ≤ 0.6, then the worst ratio is in the first plateau, which is already < 1.

## Computational Evidence for Lemma 2
- All wide families with prime a ≤ 61, k ∈ {2,3,4}: sup post-peak ratio < 0.5984
- Representative wide families a ≤ 199: worst post-peak 0.59293
- Target c₀ = 3/5 has real slack

## Key Structural Facts
- F(x) = ⌊x/a⌋ + H_B(x) - H_B(⌊x/a⌋) where B = {ka+1,...,ka+t}
- In the post-peak region, G(x) is "mostly decreasing" toward δ_A with O(1/x) oscillations
- The interval-capacity bound: |S_A ∩ I| ≤ ⌈L/a⌉ + t·⌈L/(N+1)⌉ gives per-window density ≈ 0.5
- Since 0.5 < 0.6 (target), window-capacity bounds that failed for direct EP-488 (threshold 1) might work HERE

## What to Prove
For n ≥ m* (past the first peak of G), show that for all m > n:
F(m)/m < (2c₀)·F(n)/n with c₀ = 3/5 (or any c₀ < 2/3).

Equivalently: in the post-peak region, the density curve G(x) cannot rebound by factor 2c₀ = 6/5. Since G is mostly decreasing post-peak, this should be much easier than the full EP-488 factor of 2.

Extended thinking ON, think deep, and in parallel. Think of every conventional, unconventional, novel mix of both approach. Try and fail until you've genuinely exhausted everything and come back with what you tried, why it worked / didn't, how close we are, what you recommend next and why.
