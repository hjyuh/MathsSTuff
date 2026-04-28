# EP-488 — Gemini Deep Think Prompt (April 13, 2026)

## THINKING BUDGET MANAGEMENT

You have a thinking limit. Phase your work:

**Phase 1 (light thinking):** Read the problem state and proved results below. Internalize, don't re-derive.

**Phase 2 (medium thinking):** Explore multiple strategies in parallel. Identify which ones gain traction and which hit walls early. Abandon dead ends fast.

**Phase 3 (deep thinking):** Pour remaining budget into the most promising 1-2 strategies. Push them as far as they go.

**Phase 4 (output):** Write your report. If you didn't finish, document what you tried, where each strategy broke, and what you learned.

---

## THE PROBLEM (EP-488)

For primitive Q (no element divides another), q = max(Q), prove:
$$O_Q(n,m) = 2\frac{A_Q(n)}{n} - \frac{A_Q(m)}{m} < 1 \quad \forall m > n \geq q$$

Equivalently, with D(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}, R = Q \ {q}:
$$\frac{D(m)}{m} \leq \frac{2D(n)}{n}$$

---

## WHAT IS PROVED (trust these, do not re-derive)

1. **|R| = 1 (pairs):** PROVED, machine-verified in Lean.
2. **|R| = 2 (triples):** PROVED, all sub-regimes closed.
3. **Top Window Theorem:** If Q has any element ≤ q/2, then O_Q < 1. Only Q ⊂ (q/2, q] matters.
4. **n < 2q:** PROVED for all |R|. Overlap graph is a matching → pair/triple per block.
5. **D-separator superadditivity:** Machine-verified. Counterexamples must live in a single connected component of the n-LCM graph on R.
6. **Components ≤ 2:** Handled by pair/triple theorems.
7. **Five specific atomic families closed:** {6c,8c,9c}, {8c,9c,12c}, {9c,12c,16c}, {12d,15d,20d}, {16d,18d,24d,27d} — all by compression + finite verification, zero violations in ~18M tuples.
8. **Top Window LCM Lemma:** For a, b ∈ (q/2, q) with a ∤ b: lcm(a,b) ≥ 2a > q. Machine-verified.
9. **2q ≤ n < 9q/4:** Only {6c,8c,9c}-type connected triples, which are closed.

---

## THE ONE REMAINING GAP

For Q ⊂ (q/2, q] with n ≥ 2q, and the n-LCM graph on R having a connected component C with |C| ≥ 3, prove:
$$\frac{D_C(m)}{m} \leq \frac{2D_C(n)}{n}$$

### Why this is the last wall:
- Odd-order IE terms (|S| = 3, 5, ...) with lcm(S) ∈ (n, m] are harmful
- No termwise IE domination available
- Leaf-pruning blocked (adjoining-monotonicity killed)
- Density domination has right direction but crude constants don't close
- Compression works per-family but needs a finiteness theorem for the family list

### Key structural constraints you can use:
- All elements of C are in (q/2, q] — ratio max/min < 2
- Pairwise lcm > q (proved, machine-verified)
- If n < Kq, only finitely many edge types: a, b < 2K
- All computational extremizers have n < 3q

---

## KILLED APPROACHES (do NOT use)

- **Kill #110:** "Adding elements to Q lowers max O_Q" is FALSE. Concrete counterexample.
- **Kill #109:** "Δ(m)/m ≤ 2Δ(n)/n at run-end extremizers" is FALSE. Concrete counterexample.
- **Kill #108:** u_T target lemma is FALSE.
- Do NOT use any form of "adding elements helps" or subset comparison via pointwise monotonicity.
- Do NOT claim "components ≤ 3 are handled by triple case" — |R|=3 is |Q|=4, NOT the proved triple case.

---

## PROMISING TARGETS (explore freely)

**Target A: Prove n < 3q at the extremizer.**
If true: only 5 edge types ({2:3}, {2:5}, {3:4}, {3:5}, {4:5}), template list finite, compression closes everything. Strong computational evidence — all observed extremizers have n < 3q.

**Target B: Template Finiteness Theorem.**
Show every connected top-window component belongs to one of finitely many scaled templates.

**Target C: Uniform density domination.**
Pair budget Σ B_r ≥ Ω(|C|/q) vs harmful terms ≤ o(|C|/q). Needs exact constants.

**Target D: Structural insight (your specialty).**
You previously found Domain Amputation and Additive Contraction — structural insights nobody else saw. Is there a structural argument here that bypasses IE and density entirely?

**Target E: n-range extension.**
Push the safe range beyond 9q/4 by classifying edge types at each threshold. Progressive narrowing.

---

## COMPUTATIONAL EVIDENCE

- 1,400 random top-window sets (q up to 500): zero violations
- 5 atomic families (~18M tuples): zero violations, worst margin 0.093
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- All extremizers observed have n < 3q
- Worst ratio across all tests: ≈ 0.973 (Q={55,56,57,59})

---

## YOUR REQUIRED OUTPUT

**You MUST include ALL of the following:**

1. **Percentage complete:** Your honest estimate of how close EP-488 is to fully proved. Justify the number — why that high, why not higher.

2. **Why we're not finished:** State precisely what mathematical gap remains and why existing tools don't close it.

3. **What you attempted:** Describe the strategies you explored. For EACH one: what the idea was, how far it got, and exactly where/why it broke. Be specific — name the exact inequality or step that fails.

4. **What you recommend:** Propose the most promising next step. Give evidence for why it should work — computational, structural, or analogical. Explain why you believe this over the alternatives.

5. **If you believe you've closed the gap:** Give an explicit proof. Check your constants numerically at the worst known case ({6c,8c,9c} at n ≈ 2q, {8c,9c,12c} at n ≈ 9q/4). Do not declare QED without verification.
