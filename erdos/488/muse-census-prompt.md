# EP-488 Muse Task — (c, τ_n) Realizability Census (April 15, 2026)

*Attach unified-truth-v45-april15.md alongside this prompt.*

---

## CONTEXT

You are part of a multi-model rotation attacking Erdős Problem 488. Read v45 for full state. The headline result from this session is the **exact cycle penalty formula**:

$$\varepsilon_n = c - \tau_n$$

where c is the cyclomatic number of the q-excluded n-LCM graph and τ_n counts triple-collision points. This transforms the closure problem: if every realizable component has τ_n ≥ (c−1)/2, then the existing CML target (c+1)/n closes everything.

**Someone reported (unverified) that for q ≤ 50, the only realizable (c, τ_n) pairs are (0,0), (1,0), (1,1), (2,1).** If true, the entire remaining problem reduces to ONE CML target: M_T ≥ 2/n. This claim must be verified or refuted with explicit computation.

### Rotation Roster
- **GPT 5.4 Pro (×2)** — Extended thinking. Solved an Erdős problem autonomously.
- **GPT 5.2 Pro** — Extended thinking. Strong structural intuition.
- **Codex B** — Error-finding, auditing.
- **Muse Spark Contemplating (you)** — 16 parallel agents. Highest HLE score.
- **Gemini Deep Think** — (When active.) 192k thinking limit.
- **Gauss/Aristotle** — Lean 4 formal verification.

### Orchestrator (Claude Opus 4.6) has:
- Filesystem MCP (reads/writes project directory)
- Gauss MCP (submit Lean proofs, poll results)
- Aristotle MCP (submit Lean proofs, poll results)
- Web search

If you need something formalized, written to disk, computed on a different platform, or looked up — say so explicitly.

---

## YOUR TASKS (priority order)

### Task 1: (c, τ_n) Realizability Census (HIGHEST PRIORITY)

Write a program (Python preferred) that:

1. For each q from 5 to 120:
   - Enumerate all primitive subsets C ⊂ (q/2, q] with |C| ≥ 3
   - For each such C, compute n = max{lcm(a,b) : a,b ∈ C, a≠b, lcm(a,b) < 3q} (or try all n in [2q, 3q))
   - Build the q-excluded n-LCM graph: vertices = C, edges = {(a,b) : lcm(a,b) ≤ n, q ∤ lcm(a,b)}
   - Find connected components
   - For each connected component with |V| ≥ 3:
     - Compute c = |E| − |V| + 1
     - Compute collision fibers S_ℓ = {a ∈ C : a | ℓ} for each ℓ ≤ n with q ∤ ℓ and |S_ℓ| ≥ 2
     - Count τ_n = #{ℓ : |S_ℓ| = 3}
     - Record (q, C, n, c, τ_n, ε_n = c − τ_n)

2. Output a summary table of all distinct (c, τ_n) pairs found, with example witnesses.

3. Specifically flag:
   - Any (c, τ_n) pair with τ_n < (c−1)/2 (these would need stronger CML or cycle absorption)
   - Any c ≥ 3 component
   - Any triangle-free component with c ≥ 2 (τ_n = 0, c ≥ 2)

**The key question:** Does τ_n ≥ (c−1)/2 always hold? If yes for q ≤ 120, this is very strong evidence that CML with target max(2(c−τ_n)/n) closes EP-488.

### Task 2: m-side Penalty Computation

On the same census, for each component found in Task 1:

1. Find the minimizing m > n (the m that maximizes D_C(m)/m, or at least check m up to 10q)
2. Build the m-LCM graph (edges where lcm(a,b) ≤ m)
3. Compute ε_m = H_T^(q)(m) − D_C(m) (using any spanning tree — it should be tree-independent if m < 3q, but may not be if m ≥ 3q)
4. Check: is ε_m/m ≥ 2ε_n/n? (cycle absorption condition)
5. Record (q, C, n, m, ε_n, ε_m, RHS_of_star = 2ε_n/n − ε_m/m)

**The key question:** Is the RHS of (★) always ≤ 0? If yes, forests are the hardest case and EP-488 closes.

### Task 3: Unicyclic CML (if time permits)

For the unicyclic τ_n = 0 case (c=1, ε_n=1):

1. For each such component found in Task 1, compute M_T(n,m) = 2H_T(n)/n − H_T(m)/m for the minimizing m
2. Check: is M_T ≥ 2/n always?
3. Record the worst-case margin M_T − 2/n and the witness

---

## INSTRUCTIONS

1. **Try every conditional and unconditional approach — at least 2 of each.** The enumeration IS one approach. Try at least one theoretical approach too (e.g., prove τ_n ≥ (c−1)/2 from structural constraints).

2. **Check against the kill list.** 113 dead approaches — don't reinvent them.

3. **Be concrete.** Code, data, explicit examples. No hand-waving.

4. **Flag errors in v45** prominently if found.

5. **State proved vs conjectured** precisely.

6. **Give Lean-ready statements** where possible.

7. **Come back with a detailed report:**
   - What you tried and why
   - What worked / what didn't (with WHY)
   - Recommendations with confidence 1-10
   - Percentage complete estimate with justification
   - Proposed closing path

8. **End with this checklist:**

```
## CHECKLIST
- [ ] Attempted ≥2 conditional approaches (list them)
- [ ] Attempted ≥2 unconditional approaches (list them)
- [ ] Checked all approaches against kill list
- [ ] Flagged any errors found in v45
- [ ] Clearly separated proved results from conjectures
- [ ] Provided Lean-ready statements where applicable
- [ ] Gave detailed report (tried/worked/failed/recommendations)
- [ ] Rated each recommendation 1-10 with evidence
- [ ] Gave percentage complete estimate with justification
- [ ] Proposed concrete closing path
```

---

## WHAT NOT TO DO

- Do NOT try D(m)/m ≤ W_T (kill #111)
- Do NOT assume the n-LCM graph is a forest (hexagon counterexample)
- Do NOT try BadBlock descent (kill #112)
- Do NOT try unrestricted f_supermodular (kill #113)
- Do NOT try full-graph Hunter as m-side bound (FALSE)
- Do NOT try direct Edge-Domination on q-excluded terms (terms ≠ g_k)
- Do NOT submit a pure audit without attempting computation/proofs
