# EP-488: Structural Bound on Quotient-Core Moduli
## Prompt for GPT-5.4 Pro Extended — April 5, 2026

---

## CONTEXT (read carefully)

EP-488 is 89% proved. The layer decomposition is exact and complete:

F_A(x) = Σ_{j=1}^k K_{Q_j}(⌊x/a_j⌋)

where K_Q(y) counts integers ≤ y coprime to all elements of Q, and Q_j is the quotient-core at peeling step j.

Each normalized layer T_j(x) = (M/x)·K_{Q_j}(⌊x/a_j⌋) decomposes as:

T_j(x) = c_j + ε_j(x),   where c_j = r_j·ρ_j = (M/a_j)·ρ_{Q_j}  (CONSTANT)

EP-488 ⟺ sup(Σ T_j) < 2·inf(Σ T_j) on [M, 10M].

GPT-5.2 Pro reformulated this as a COLLECTIVE OSCILLATION BUDGET:

  V + 2U < C

where V = Σ v_j (upward excursions), U = Σ u_j (downward excursions), C = Σ c_j.

Kill #46 showed the per-layer bound fails (rough numbers phenomenon). But the COLLECTIVE condition can still hold.

## THE KEY REDUCTION (Claude's analysis)

Using the periodicity of K_Q, the discrepancy satisfies:

|D_Q(y)| = |K_Q(y) - y·ρ_Q| ≤ φ(q)

where q = ∏_{p ∈ P_Q} p is the product of all primes dividing elements of Q.

Note: φ(q) = q·ρ_Q, so |D_Q(y)| ≤ q·ρ_Q.

Plugging into the excursion bounds:
  v_j ≤ q_j·ρ_j     (upward; floor term only reduces upward spikes)
  u_j ≤ q_j·ρ_j + ρ_j   (downward; floor term adds at most ρ_j)

The collective criterion V + 2U < C becomes:

  **Σ_j ρ_j·(3q_j + 2) < Σ_j r_j·ρ_j**

Or equivalently: **Σ_j ρ_j·(r_j - 3q_j - 2) > 0**

where r_j = M/a_j and q_j = product of primes appearing in Q_j.

## YOUR TASK

### Task 1: Characterize q_j

For a primitive set A = {a_1 < ... < a_k} with M = a_k, describe the peeling process that produces quotient-cores Q_1, ..., Q_k. Then:

(a) What is Q_j explicitly? How does it relate to A and a_j?

(b) What primes appear in Q_j? Specifically, let P_j = set of prime factors of elements of Q_j. Give bounds on q_j = ∏_{p ∈ P_j} p.

(c) Is q_j always ≤ M? Is q_j always ≤ a_j? What is the tightest bound?

### Task 2: Prove or disprove the structural inequality

For every primitive set A with max(A) = M:

**Is it true that Σ_j ρ_j·(r_j - 3q_j - 2) > 0?**

If true for all primitive sets, EP-488 follows. If false, find a counterexample and describe how close the inequality is to failing.

Specific sub-questions:
- For the principal layer (j=1, a_1 = min(A)): what is q_1? Is r_1 = M/a_1 always much larger than q_1?
- For "tail" layers (j near k, a_j near M): what is q_j? These layers have r_j ≈ 1, so q_j must be ≤ 0 (impossible) — how does the structure save us?
- Can the "bad" layers (r_j ≤ 3q_j + 2) ever outweigh the "good" layers?

### Task 3: If the naive bound fails, refine it

The bound |D_Q(y)| ≤ φ(q) = q·ρ_Q is worst-case over all y. But for specific y-values arising in the layer decomposition (y_j ∈ [r_j/10, r_j]), the discrepancy may be much smaller.

(a) Can you give a tighter bound on sup_{y ∈ [r/10, r]} |D_Q(y)| using the specific structure of the quotient cores that arise from primitive sets?

(b) Is there a "phase mixing" argument: the different layers' discrepancies D_j(y_j(x)) oscillate at different rates as x varies, so their SUM has smaller sup than Σ sup|D_j|?

## WHAT'S ALREADY PROVED (do not re-derive)

1. EP-488 for all pairs, triples, consecutive k-tuples, one-anchor families, sparse sets, compact sets
2. The layer decomposition F_A = Σ K_{Q_j}(⌊x/a_j⌋) — exact
3. The collective oscillation budget V + 2U < C ⟹ sup < 2·inf
4. |D_Q(y)| ≤ φ(q) for all y (periodicity of K_Q)
5. Complement FKG: ρ_Q ≥ 1/(|Q|+1)
6. 23M+ families tested computationally, zero EP-488 failures

## WHAT'S KILLED (do not attempt)

- Per-layer bound C^loc < r·ρ/3 (Kill #46: rough numbers dip)
- Any threshold on S₁ or δ (not scale-invariant)
- Monotonicity by min(A) (44K violations)
- Bonferroni-2r for any fixed r

## CONSTRAINTS ON YOUR PROOF

- Must be SCALE-INVARIANT (scaling A → tA preserves the ratio)
- Must handle ALL primitive sets, not just specific families
- Must be compatible with the exact layer decomposition (no approximations)
- If you find the naive bound insufficient, propose a REFINED bound and state clearly what structural property of primitive sets it uses

## FORMAT

Start with your answer to Task 1 (characterize q_j). Then Task 2 (structural inequality). Then Task 3 (refinements if needed). Be explicit about what is proved vs. conjectured. If you find a counterexample to the structural inequality, say so immediately — do NOT patch it silently.
