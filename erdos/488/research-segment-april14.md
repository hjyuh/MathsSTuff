# EP-488 Research Segment — April 14, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- A_Q(x) = #{t ≤ x : no element of Q divides t}
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

Prove: D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

This is Erdős Problem 488 (1960), open for 65 years. We have reduced it to one remaining case.

## What is SOLVED (treat as black boxes)

- |R| = 1 and |R| = 2: fully proved, machine-verified in Lean
- Top Window Theorem: only Q ⊂ (q/2, q] can be extremal
- n < 2q: proved for all |R| (overlap graph is a matching)
- D-separator superadditivity: counterexamples live in single connected components of the n-LCM graph (machine-verified)
- Components of size ≤ 2: handled by pair/triple theorems
- Five specific atomic families closed by compression + finite verification: {6c,8c,9c}, {8c,9c,12c}, {9c,12c,16c}, {12d,15d,20d}, {16d,18d,24d,27d}

## The OPEN case

Connected components C of size |C| ≥ 3 in the top window (all elements in (q/2, q]) with n ≥ 2q. Prove D_C(m)/m ≤ 2·D_C(n)/n.

## Key tools you may use

**m-side (SOLVED):** For any spanning tree T of the n-LCM graph, Hunter's inequality with q-exclusion gives:
$$\frac{D_C(m)}{m} \leq H_T^{(q)}(m) = \frac{1}{m}\sum_{a \in C}\left(\lfloor m/a \rfloor - \lfloor m/\text{lcm}(a,q) \rfloor\right) - \frac{1}{m}\sum_{e \in T}\left(\lfloor m/L_e \rfloor - \lfloor m/\text{lcm}(L_e,q) \rfloor\right)$$
This is exact, finite, floor-based. Verified.

**Floor-Fractional Lemma (VERIFIED):** For y ≥ 1, k ≥ 2: 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y.

**Edge-Domination (VERIFIED):** For g_k(y) = (⌊ky⌋ − ⌊y⌋)/y with k ≥ 2: 2·inf_{y≥1} g_k(y) ≥ sup_{z≥1} g_k(z).

**Top Window LCM (VERIFIED):** For a, b ∈ (q/2, q) with a ∤ b: lcm(a,b) ≥ 2a > q. Sharper: lcm(a,b) ≥ 3q/2.

**Under n < 3q:** Only 4 edge types exist: {2:3}, {3:4}, {3:5}, {4:5}.

## DEAD approaches (111 kills — do NOT use)

- "Adding elements to Q lowers max O_Q" — FALSE (concrete counterexample)
- "D(m)/m ≤ W_T" where W_T is asymptotic density — FALSE ({2,3} at m=4: 3/4 > 2/3)
- "Pointwise Δ(m)/m ≤ 2Δ(n)/n at run-end extremizers" — FALSE
- "The n-LCM graph is a forest under n < 3q" — FALSE (hexagon: C={24,27,30,36,40,45}, q=47, n=135 has cycles)
- "Template finiteness" — likely FALSE (multiplicative group {3/2, 4/3, 5/3, 5/4} is dense, infinitely many templates possible)
- "Components of size 3 are handled by the triple case" — WRONG (|R|=3 means |Q|=4, not the proved triple case)

## The deep structure of what remains

**The n-side is the wall.** The m-side has an exact upper bound (q-excluded Hunter). But the n-side needs a LOWER bound on D(n)/n.

In forests (cycle-free graphs), the inclusion-exclusion for D(n) truncates at pairs because all |S| ≥ 3 have some non-adjacent pair with lcm > n. So D(n) = H_T(n) exactly, and the edge-domination theorem gives 2H_T(n)/n ≥ H_T(m)/m. **Forests are solved.**

But graphs can have CYCLES (hexagon counterexample). In graphs with cycles, higher-order IE terms survive at n. These odd-order terms (|S| = 3, 5, ...) with lcm(S) ≤ n SUBTRACT from D(n), making D(n) < H_T(n). This breaks the chain.

## The research question

**Do cycle IE corrections preserve the factor-of-2 inequality?**

A cycle correction subtracts δ_S(x) = ⌊x/lcm(S)⌋ − ⌊x/lcm(S∪{q})⌋ from the IE sum. It subtracts at BOTH n and m. The key observation:

The m-side Hunter bound H_T^(q)(m) does NOT include cycle corrections (it's a tree bound). But D(n) on the n-side DOES include them (it's the exact count). So cycle corrections subtract from the n-side but are already absent from the m-side bound.

However: we multiply the n-side by 2. So a cycle correction of size ε at n costs us 2ε on the left side, while being absent (cost 0) on the right side. The question is whether the "base margin" (from the forest case) is large enough to absorb 2ε for all possible cycle corrections.

**Equivalently:** Is the forest case the HARDEST case? Do cycles make the inequality EASIER or HARDER?

**Intuition for why cycles might help:** Each cycle corresponds to elements sharing many common factors. More shared factors → more overlap → the elements are "less independent." Less independence means the coverage D(x) is closer to what a smaller set would give. Since the inequality is easier for smaller sets (pairs and triples are proved), more overlap should help.

**Intuition for why cycles might hurt:** At n, cycle corrections subtract coverage. At m (which is larger), the same correction subtracts proportionally less (⌊m/L⌋/m ≈ ⌊n/L⌋/n for large L, but the subtracted amount at n hits harder because we're dividing by smaller n).

## Your task

1. Investigate whether cycle corrections preserve the D(x) inequality. Try to prove or disprove: for a connected component C with cycles in the n-LCM graph, does 2D(n)/n ≥ H_T^(q)(m)/m still hold?

2. If you can prove it, give the explicit argument with numerical verification at: C={24,27,30,36,40,45}, q=47, n=135 (the hexagon — the hardest known non-forest case).

3. If you can't, identify the EXACT obstruction. What makes the cycle case resist?

4. Explore alternative approaches: Can you bypass the forest/non-forest distinction entirely? Is there a direct proof that 2D(n)/n ≥ D(m)/m using the q-excluded Hunter bound on BOTH sides?

5. Consider: what if instead of a spanning TREE, we use the full graph in Hunter's inequality? The q-excluded Hunter bound with all edges (not just a tree) gives a TIGHTER upper bound on D(m)/m. Does this tighter bound make the comparison with 2D(n)/n easier?

## Required output

- Your honest assessment of the problem's difficulty (percentage complete, 0-100)
- At least 2 strategies you attempted, with exact failure points
- Your strongest result (theorem, counterexample, or structural insight)
- Your recommendation for the most promising next step
- If you prove or disprove anything, verify numerically on the hexagon example

## Computational evidence

- 18M+ tuples across 5 families: zero violations
- 1,400 random top-window sets (q up to 500): zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst observed ratio D(m)/m ÷ (2D(n)/n) ≈ 0.973
