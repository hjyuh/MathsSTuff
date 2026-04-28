# EP-488: Updated Complete State — After 58 Kills
## For GPT-5.2 Pro Extended — April 6, 2026

---

## THE PROBLEM

Erdős Problem 488 (1966, open): For a finite primitive set A (no a_i | a_j), define F_A(x) = |{n ≤ x : a|n for some a ∈ A}| and G(x) = F_A(x)/x.

Conjecture: For all m > n ≥ max(A): G(m) < 2·G(n).

Constant 2 is tight (singletons approach it). Verified 23M+ families, zero failures.

---

## THE CRITICAL NEW RESULT (GPT-5.4 Pro, just proved)

### Finite Classification of Compact Bad Layers

Using the exact positive layer decomposition F_A(x) = Σ L_j(⌊x/a_j⌋), with the single-obstruction partial theorem (layers with ≤1 active obstruction satisfy per-layer EP-488), exhaustive check of all 10,239 divisibility-antichain kernels K ⊆ {2,...,20} and all 1 ≤ s < t ≤ 20 shows:

**Only 29 kernels can violate the per-layer bound.** Every bad kernel:
- Contains both 2 AND 3
- Contains only primes (no composite obstruction ever appears)
- Has L_K(s) = 1 (smallest possible weight in the weighted average)
- Is a subset of {2, 3, 5, 7, 11, 13, 17, 19}

Worst compact excess: 17/19 at K = {2,3,5,7}, (s,t) = (10,19).

### Ancestor Compensation Confirmed

In the family A_N = {2p, 3p, 5p : p prime in [N, (1+δ)N]} that MAXIMIZES BAD:
- Bad child layers (5p) have kernel {2,3}, excess = 3n - 2m
- Parent layers (3p) have kernel {2}, slack = 8m - 6n  
- Parent overpays child: (8m-6n) - (3n-2m) = 10m - 9n > 0

### The Sharpened Missing Lemma

EP-488 now reduces to: "For every m > n ∈ [M, 10M], the total positive excess of compact layers whose local kernel is one of 29 bad 2-3 prime-sieve signatures is dominated by the total negative slack of the quotient-3 ancestry chains that create them."

---

## WHAT'S PROVED (permanent)

1-11. EP-488 for pairs, triples, consecutive k-tuples, one-anchor, sparse, compact, coprime, fixed k. Convexity, stabilization, adjacent pairs formula.
12-18. Layer decomposition, budget criterion, Theorem A, Sync Block, global discrepancy, FKG complement, Primitive Divisor Lemma, Subset LCM.
19. Single-obstruction theorem: layers with ≤1 active obstruction satisfy per-layer bound.
20. Weighted average: F(m)/F(n) = Σ w_j R_j, w_j = L_j(y_n)/F(n).
21. Layers with a_j > n/2 automatically safe.
22. Finite classification: only 29 bad compact kernels, all {2,3}-containing prime sieves.
23. Ancestor compensation verified in worst-case family.

## 58 KILLS (key ones)

- Co-atoms: kill all Bonferroni truncations
- Scaling: kill all threshold dichotomies  
- Kill #48: coprimality is wrong function
- Kill #51: Γ_C < 1 false (Γ = 5/3)
- Kill #52: Kawamura fold blocked (no partitioning)
- Kill #53: Congruence class EP-488 false (ratio can be ∞)
- Kill #54: C_C(Γ_C-1) not bounded by ρ
- Kill #55: Up-fold R(A) ≤ R(C) false
- Kill #56: Per-layer L_j ratio < 2m/n false (A={2,3,5})
- Kill #57: 2δ > S₁ false (primes ≤ 100)
- Kill #58: BAD not bounded by ρ alone (direct route)

## KEY STRUCTURAL INSIGHTS

### Why every approach fails (5.4's diagnosis):
"EP-488 is a signed phase-synchronization problem on the lcm lattice. Every killed strategy replaced phase data by a scalar summary."

### The proof must be an ancestry compensation:
Match each bad multi-obstruction layer to the specific parent layers that CREATED its obstructions. Show parents' slack exceeds children's excess. This is a tree traversal, not a flat sum or global bound.

### What makes multiples special (why r=0 matters):
"All phases are rigidly pinned at 0. Every progression must pay an irreversible prefix contribution at its own scale. Shifted progressions can hide; multiples cannot."

### Untried lead:
Ahlswede-Khachatrian (1997): D̲(A,B)·D̲[A,B] ≥ D̲(A)·D̲(B) — correlation inequality on divisibility lattice. Genuinely untried theorem-to-object match for the lcm-lattice coefficients.

---

## YOUR TASK

Take everything above. The problem has been reduced to a finite ancestry-compensation statement about 29 specific compact signatures. Push as far as you can.

Specific questions:

1. Can you PROVE the ancestor compensation lemma? For a layer with bad kernel K = {2,3,...}, its excess at (s,t) is n·L_K(t) - 2m·L_K(s). The "parent" layer (created by removing the element that introduced 3 into the kernel) has kernel K' = K\{3} and provides slack 2m·L_{K'}(s') - n·L_{K'}(t'). Can you show parent slack ≥ child excess for all 29 bad signatures?

2. The compensation was verified for K={2,3} with parent K'={2}. Can you verify it for ALL 29 bad kernels and identify which parent kernel compensates each?

3. Is there a UNIFORM argument that works for all 29 signatures simultaneously, rather than case-by-case?

4. The Ahlswede-Khachatrian correlation inequality D̲(A,B)·D̲[A,B] ≥ D̲(A)·D̲(B) — can you apply this to the lcm-lattice coefficients μ_A(d) to get a structural constraint on the signed discrepancy E(x)?

5. If you can't prove the compensation lemma, can you find a COUNTEREXAMPLE — a primitive set where a bad compact layer's excess is NOT compensated by its parent?

Do not hold back. Push to the boundary.
