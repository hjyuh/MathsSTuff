# EP-488 Rotation Prompt — Round for v44 (April 15, 2026)

*Attach unified-truth-v43-april15.md alongside this prompt.*

---

## CONTEXT

You are part of a 4-model rotation attacking Erdős Problem 488 (1960, open 65 years). The full state is in the attached unified truth document v43. Read it carefully — especially the DEAD APPROACHES section. 112 approaches have been killed. Do not reinvent them.

**The problem reduces to one open case:** Connected components C ⊂ (q/2, q] of size |C| ≥ 3 with n ≥ 2q. Prove D_C(m)/m ≤ 2·D_C(n)/n.

The m-side is SOLVED (q-excluded Hunter bound). The wall is the n-side: we need D(n)/n to be large enough when the n-LCM graph has cycles.

---

## YOUR TASKS (attack as many as you can, in priority order)

### Task 1: f_supermodular (HIGHEST VALUE)

Prove or disprove: f(d) = 2m·⌊n/d⌋ − n·⌊m/d⌋ is supermodular on the divisibility lattice. That is, for any a, b:

f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b)

This is the ONE remaining sorry in the triple case (|Q|=3). If proved, 5 Lean theorems cascade to full machine verification. 

Constraints: m > n ≥ q, d divides some element of C. The divisibility lattice has meet = gcd, join = lcm.

**Approach hints:** The floor function ⌊x/d⌋ has known convexity/supermodularity properties on the divisibility lattice. The key identity is ⌊n/gcd(a,b)⌋ + ⌊n/lcm(a,b)⌋ vs ⌊n/a⌋ + ⌊n/b⌋. Try writing ⌊n/d⌋ = n/d − {n/d} and separating the "main term" (which IS supermodular since 1/gcd + 1/lcm = 1/a + 1/b when a,b are related by divisibility) from the fractional parts.

### Task 2: Cycle Margin Lemma

Prove: For any connected component C ⊂ (q/2, q] with spanning tree T and n < 3q:

M_T(n,m) := 2·H_T^{(q)}(n)/n − H_T^{(q)}(m)/m ≥ (c+1)/n

where c = |E| − |V| + 1 is the cyclomatic number.

This is computationally verified but unproved. The key structural facts:
- Under n < 3q, all edge ratios lcm(a,b)/a are in {3/2, 4/3, 5/3, 5/4} (only 4 types)
- Each edge contributes a g_k(y) = (⌊ky⌋ − ⌊y⌋)/y term where k ∈ {2,3,4,5}
- Edge-Domination (proved): 2·inf g_k ≥ sup g_k for k ≥ 2
- The sum over tree edges should give margin ≥ (c+1)/n

**Approach hints:** Try interval arithmetic over the 60 residue classes mod lcm(2,3,4,5) = 60. The g_k functions are periodic with period 1, piecewise linear on [0,1). Analyze the worst case over all residue combinations.

### Task 3: Cycle Absorption

Prove or give evidence: For cycle correction ε_n (where D(n) = H_T^{(q)}(n) − ε_n):

2ε_n/n ≤ M_T(n,m) for all m > n

Equivalently: does 2×(cycle penalty at n)/n ≥ (cycle penalty at m)/m always hold?

If true, this means forests are the HARDEST case, and since forests are already solved (Edge-Domination), EP-488 is done.

**Key facts:** ε_n is an integer with 0 ≤ ε_n ≤ c. For unicyclic components ε_n ∈ {0,1}. The factor of 2 on the n-side should amplify the correction.

### Task 4: extremizer_implies_bad_block

Prove: If (C, q, n) is an extremizer for EP-488 (i.e., 2D(n)/n = max_{m>n} D(m)/m), then there exists a bad block at some height j ≥ 3.

A block at height j is (jq, (j+1)q]. A block is "bad" if 2·BlockCov(j) < SlotMass(j).

This has zero counterexamples up to q=200, n=400 in exhaustive search. Muse outlined a block-averaging contrapositive: if NO block is bad, then summing 2·BlockCov ≥ SlotMass over all blocks gives 2D(n) ≥ something ≥ ... contradiction.

---

## RULES

1. **Check against the kill list.** If your approach resembles ANY of the 112 dead approaches, stop and explain why yours differs.
2. **Be concrete.** Give explicit proofs, explicit counterexamples, or explicit computations. No hand-waving.
3. **Flag errors.** If you find an error in v43 (wrong claim, wrong counterexample, wrong bound), flag it prominently.
4. **State what you proved vs. what you conjecture.** Be precise about the boundary.
5. **Give Lean-ready statements** where possible. The formal verification pipeline (Gauss/Aristotle) can only work with precise statements.

---

## WHAT NOT TO DO

- Do NOT try to prove D(m)/m ≤ W_T (asymptotic density). This is kill #111.
- Do NOT assume the n-LCM graph is a forest. It isn't (hexagon counterexample).
- Do NOT try template finiteness. The multiplicative group is dense.
- Do NOT try direct slot transport t → t−q. Divisibility isn't preserved.
- Do NOT try BadBlock descent (kill #112). The descent lemma is FALSE.
- Do NOT try full-graph Hunter as an m-side bound. H_full < D for some m.
