# EP-488 — Gemini's Null-Space Forest Claim (AUDIT REQUEST)

## CONTEXT

Gemini Deep Think claims to have CLOSED EP-488. Before accepting this, we need independent verification from the most precise models. Read the argument below, then give your verdict.

## YOUR TASK

1. **Verify or refute each step independently.** Do not assume any step is correct because another step is.
2. **Find the weakest link.** If one step fails, identify it precisely with a counterexample or logical gap.
3. **Check constants at worst cases.** Gemini verified at {18,24,27} and {16,18,24}. Check additional cases.
4. **Give your honest percentage** after auditing.

---

## GEMINI'S ARGUMENT (5 steps)

### Step 1: Extremizer bound n < 3q
**Claim:** Any counterexample to the D(x) inequality must have n < 3q.
**Gemini's argument:** For n ≥ 3q, every element a ∈ C has n/a ≥ 3, so the running density stabilizes, giving D(n)/n ≥ 0.83·α_C. Then 2D(n)/n ≥ 1.66·α_C > α_C ≥ D(m)/m.
**Your job:** Is this rigorous? The "0.83" factor — where does it come from? Is it proved or heuristic? Check with a specific C where D(n)/n might be minimal.

### Step 2: Edge types under n < 3q
**Claim:** With n < 3q, the only edge types in the n-LCM graph are {2:3}, {3:4}, {3:5}, {4:5}. NOT {2:5} because 5/2 = 2.5 > 2 violates the top-window ratio bound.
**Your job:** Verify. Is it true that a = 2, b = 5 is impossible? If r = L/2 and s = L/5 with both in (q/2, q], then s/r = 2/5, so r/s = 5/2 > 2, meaning r > 2s, but both must be in (q/2, q] which has ratio < 2. So YES, {2:5} is impossible. Confirm.

### Step 3: Null-space forest theorem
**Claim:** Over the prime basis {2, 3, 5}, the four edge ratios {3/2, 4/3, 5/3, 5/4} form a 4×3 matrix:

```
log(3/2) = (-1, 1, 0)
log(4/3) = (2, -1, 0)
log(5/3) = (0, -1, 1)
log(5/4) = (-2, 0, 1)
```

Rank = 3 (since the first three rows span R³). Nullity = 1. The unique (up to scaling) null vector corresponds to the cycle:

(4/3) × (3/5) × (5/4) = 1

which maps to the {12, 15, 20} triangle (lcm-scaled). Since {12, 15, 20} is already computationally closed, ALL remaining connected components are forests (cycle-free).

**Your job:** 
- Verify the rank computation. Is the matrix really rank 3?
- Verify the cycle (4/3)(3/5)(5/4) = (4/3)(3/5)(5/4) = 60/60 = 1. Yes.
- Is this the ONLY cycle? Could there be longer cycles? The null space is 1-dimensional, so every cycle is a power of this fundamental cycle. Confirm.
- **CRITICAL:** Does "cycle in the ratio graph" actually correspond to "cycle in the n-LCM graph on R"? A cycle in ratio space means r₁/r₂ · r₂/r₃ · r₃/r₁ = 1, which is automatic. The question is whether a cycle of EDGES (each with lcm ≤ n) forces a triangle in R. Is this true?

### Step 4: Forests → IE truncation at n
**Claim:** In a forest (cycle-free graph), for any |S| ≥ 3, at least one pair in S is non-adjacent, so their lcm > n, meaning lcm(S) > n. Therefore ⌊n/lcm(S)⌋ = 0. All |S| ≥ 3 terms vanish at n.
**Your job:** 
- Is "at least one non-adjacent pair in |S| ≥ 3 in a forest" true? YES — a forest on k vertices has at most k-1 edges, but a complete graph on 3 vertices has 3 edges, so some pair must be non-adjacent. Actually wait — a path a-b-c has edges a~b and b~c but NOT a~c. So {a,b,c} has a non-adjacent pair {a,c}. But does lcm(S) ≥ lcm(a,c) > n? YES — lcm of a set is a multiple of lcm of any subset.
- Verify this is tight. The forest structure is essential — the {12,15,20} triangle DOES have all three pairwise lcms ≤ n, so the odd-order term does NOT vanish there. But that case is already closed.

### Step 5: Floor-Fractional Lemma
**Claim:** For each edge (u,v) in the spanning tree, with y = n/lcm(u,v) ≥ 1 and k = lcm(u,v)/v ≥ 2:
2(⌊ky⌋ - ⌊y⌋) ≥ (k-1)y

**Proof:** Write y = m + ε, m ≥ 1, ε ∈ [0,1). Then LHS - RHS = m(k-1) + 2⌊kε⌋ - (k-1)ε. Since m ≥ 1 > ε, we have m(k-1) > ε(k-1), so the whole expression > 2⌊kε⌋ ≥ 0.

**Your job:** Verify this algebra. Is it correct? Check edge cases: y = 1 (ε = 0), y = 1.5, y = 2. Check k = 2, k = 3.

### Step 5b: Assembling the proof
**Claim:** Since IE truncates to pairs at n, and the Floor-Fractional Lemma gives 2D(n)/n ≥ W_T (the density weight of the spanning tree), and W_T ≥ D(m)/m (Hunter's inequality), the D(x) inequality holds.

**Your job:** Is Hunter's inequality D(m)/m ≤ W_T actually true here? Hunter's inequality usually says P(A₁ ∪ ... ∪ Aₖ) ≤ max spanning tree weight. Does it apply to floor-function counts? Or is this a heuristic step?

---

## THE KEY QUESTION

**If Steps 1-5 are all correct, EP-488 is proved.** 

The weakest links are likely:
- Step 1 (n < 3q): Gemini's "0.83" factor is not derived
- Step 3 (null space): The correspondence between ratio cycles and LCM graph cycles needs verification
- Step 5b (Hunter): The application of Hunter's inequality to floor counts needs justification

**Give your verdict: proved, gap identified (specify where), or refuted (with counterexample).**

---

## YOUR REQUIRED OUTPUT

1. **Step-by-step verification:** For each of the 5 steps, state VERIFIED or GAP or FALSE with explanation.
2. **Weakest link:** Which step is most likely to fail?
3. **Percentage complete** after auditing.
4. **If gap found:** Can it be repaired? How?
5. **If all verified:** State this clearly and explicitly.

Do NOT overclaim. Do NOT declare QED without checking constants. The project has killed 110 false claims already. Be the 111th kill if this argument is wrong, or confirm it if it's right.
