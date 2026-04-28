# EP-488 — Gemini Deep Think Prompt v2 (April 14, 2026)

## THINKING BUDGET MANAGEMENT

Phase your work carefully:

**Phase 1 (light):** Read the audit results on your previous attempt. Understand exactly what was verified, what was a gap, and what was false. Do NOT defend Step 5b — it is dead.

**Phase 2 (medium):** Explore multiple repair strategies in parallel. Test each against the known counterexample ({2,3} at m=4 where D(m)/m = 3/4 > 2/3 = W_T). Any strategy that fails this test is dead on arrival.

**Phase 3 (deep):** Push the most promising strategies as far as they go.

**Phase 4 (output):** Write your report with full discipline (see required format below).

**CRITICAL RULE: Before declaring ANY inequality, check it numerically on at least 3 specific cases, including the worst known ones. Your previous Step 5b was killed by a 4-number counterexample. Do not let that happen again.**

---

## AUDIT RESULTS ON YOUR PREVIOUS ATTEMPT

Two independent auditors (Codex B and 5.4 Pro) reviewed your Null-Space Forest argument:

| Step | Your claim | Verdict | Detail |
|------|-----------|---------|--------|
| 1 | n < 3q at extremizer | **GAP** | "0.83" factor asserted, not derived |
| 2 | Only 4 edge types | **VERIFIED** | ✅ Clean |
| 3 | Null-space → forests | **GAP** | Linear algebra correct, graph conclusion not established |
| 4 | Forest → IE truncation | **VERIFIED** | ✅ Conditional on forestness |
| 5 | Floor-Fractional Lemma | **VERIFIED** | ✅ Algebra correct |
| 5b | D(m)/m ≤ W_T (Hunter) | **FALSE** | {2,3} at m=4: D(m)/m = 3/4 > 2/3 = W_T |

### What survived:
- Steps 2, 4, 5 are real building blocks. Use them.
- The null-space observation (one fundamental cycle = {12,15,20}) is likely correct but needs the graph-theoretic link proved.

### What is dead:
- **Step 5b is KILLED (Kill #111).** Density weights ≠ floor counts. You cannot bound D(m)/m by the asymptotic density tree weight W_T. Floor counts can exceed asymptotic density for finite m. The {2,3} counterexample at m=4 is definitive.

### The core problem with your assembly:
Your n-side bound (Floor-Fractional Lemma) gives: 2D(n)/n ≥ W_T (density weight).
Your m-side bound claimed: D(m)/m ≤ W_T.
But D(m)/m can exceed W_T for finite m. The bridge between n and m is broken.

---

## THE CURRENT STATE (trust this, don't re-derive)

### Proved:
1. Singletons, pairs (machine-verified), top window theorem
2. Full triple case (|R|=2), all sub-regimes
3. n < 2q for all |R| (block decomposition)
4. Separator superadditivity (machine-verified)
5. Components ≤ 2 for any n
6. Five atomic families: {6c,8c,9c}, {8c,9c,12c}, {9c,12c,16c}, {12d,15d,20d}, {16d,18d,24d,27d}

### The gap:
Connected components of size ≥ 3 in the top window (Q ⊂ (q/2, q]) with n ≥ 2q.

### Key asymmetry:
The n-side has good tools (IE truncation in forests, floor lemma). The m-side resists bounding. Your previous attempt died exactly at the m-side.

---

## KILLED APPROACHES (111 total)

**Kill #111 (YOUR Step 5b):** D(m)/m ≤ W_T is FALSE. Do NOT use density weights as upper bounds on floor counts.
**Kill #110:** Operator monotonicity under adjoining. Adding elements can increase max O_Q.
**Kill #109:** Suffix-minimizer Δ at run-end extremizers. FALSE.
**Kill #108:** u_T target lemma. FALSE.

**The lesson from Kill #111:** Any m-side bound must use EXACT floor-count inequalities, not density approximations. Check every claimed inequality against {2,3} at m=4 before using it.

---

## YOUR TARGETS (explore freely, but check everything)

### Target A: Prove n < 3q at the extremizer
Your Step 1 was in the right direction but the "0.83" was not derived. Can you make it rigorous? If proved, only 4 edge types exist and compression closes everything.

### Target B: Repair the m-side bound
Replace W_T with an exact floor-count bound. For each edge (u,v) in the spanning tree, the finite Hunter bound uses ⌊m/u⌋/m and ⌊m/lcm(u,v)⌋/m, NOT 1/u and 1/lcm(u,v). Can you prove D(m)/m ≤ (exact finite tree weight) and then show 2D(n)/n ≥ (that same weight)?

### Target C: Close Step 3's gap
Prove that a cycle in the n-LCM graph on R ⊂ (q/2, q] with n < 3q must realize the {12,15,20} triangle. The linear algebra says the nullity is 1, but the graph-theoretic conclusion needs a proof that accounts for scaling and lcm constraints.

### Target D: Bypass the forest route entirely
Find a uniform argument that doesn't need forestness. Maybe the Floor-Fractional Lemma can be applied edge-by-edge across ANY graph structure (not just trees) with a different assembly.

### Target E: Something completely new
Your previous structural insights (Domain Amputation, Additive Contraction, null-space analysis) came from thinking differently. What does the operator look like from a perspective nobody has tried?

---

## YOUR REQUIRED OUTPUT

**You MUST include ALL of the following:**

1. **Percentage complete:** Honest estimate with justification.
2. **Why we're not finished:** The precise gap, stated as a missing theorem.
3. **What you attempted:** Every strategy you explored. For EACH: the idea, how far it got, the exact step where it broke. **For every inequality you claim, state whether you checked it numerically and on which cases.**
4. **What you recommend:** Most promising next step with evidence.
5. **If you believe you've closed the gap:** Explicit proof. **Mandatory numerical checks** at:
   - {2,3} at m=4 (the Step 5b killer)
   - {6c,8c,9c} at n ≈ 2q
   - {8c,9c,12c} at n ≈ 9q/4
   - A large random top-window set with q ≈ 100
   If ANY check fails, your proof is wrong. State that clearly instead of declaring QED.

**The project has killed 111 false claims. Be the proof that survives, or be the 112th kill. Either outcome is valuable.**
