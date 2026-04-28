# EP-488: Synthesis — Collective Oscillation Budget + Sieve Analysis
## April 5, 2026 — Combines GPT-5.2 Pro + Claude

---

## THE CLEAN PICTURE (after Kill #46)

### What died:
Per-layer bound C^loc_Q(r) < r·ρ_Q/3 is FALSE (rough numbers dip).

### What 5.2 gave us:
The COLLECTIVE oscillation budget:

  **V + 2U < C**

where V = Σ v_j (total upward excursion), U = Σ u_j (total downward),
C = Σ c_j = Σ r_j·ρ_j (total mean). This allows individual layers to
misbehave wildly, as long as the misbehaving layers don't carry much weight.

### What Claude's literature search found:
1. Montgomery-Vaughan and Gorodetsky give L² bounds — useful context but
   not directly applicable (we need L∞/pointwise bounds).
2. K_Q(y) is computed by EXACT inclusion-exclusion, not sieve approximation.
   So the right tool is PERIODICITY of K_Q, not sieve theory.
3. The pointwise discrepancy bound is |D_Q(y)| ≤ φ(q) = q·ρ_Q where
   q = product of sifting primes. The relative discrepancy |D_Q(y)|/(y·ρ_Q)
   ≤ q/y → 0 as y → ∞.

---

## THE UNIFIED APPROACH

### Step 1: Layer decomposition (proved)
T_j(x) = c_j + ε_j(x), c_j = r_j·ρ_j constant.

### Step 2: Bound excursions (from periodicity)
For layer j with sifting-prime product q_j:
  v_j ≤ q_j·ρ_j           (upward, since floor term only reduces)
  u_j ≤ q_j·ρ_j + ρ_j     (downward, floor term adds ≤ ρ_j)

### Step 3: Collective criterion
V + 2U < C becomes:
  Σ q_j·ρ_j + 2·Σ(q_j·ρ_j + ρ_j) < Σ r_j·ρ_j
  3·Σ q_j·ρ_j + 2·Σ ρ_j < Σ r_j·ρ_j
  Σ ρ_j·(3q_j + 2) < Σ r_j·ρ_j

Since r_j = M/a_j, this is:

  **Σ ρ_j · (3q_j + 2) < Σ (M/a_j) · ρ_j**

Or equivalently:

  **Σ ρ_j · (M/a_j - 3q_j - 2) > 0**

### Step 4: When does this hold?
It holds whenever r_j > 3q_j + 2 for enough layers (weighted by ρ_j).

The principal layer (j=1, a_1 = min(A)) has r_1 = M/min(A), which is
the largest. If q_1 is moderate (say q_1 ≤ M^{1/2}), then r_1 > 3q_1
for M/min(A) > 3M^{1/2}, i.e., min(A) < M^{1/2}/3.

For compact sets (all elements near M), r_j ≈ 1 for all j, so this
approach doesn't apply — but compact sets are already proved (Thm 6).

---

## THE THREE PROOF STRATEGIES (from 5.2, now with concrete bounds)

### Strategy A: Dominant Stable Mass — MOST PROMISING

Split layers:
- Good (G): layers with r_j > 3q_j + 2  
- Bad (B): layers with r_j ≤ 3q_j + 2

For Good layers: e_j/c_j ≤ (q_j + 1)/r_j < 1/3, so 3·Σ_G e_j < C_G.

For Bad layers: T_j ∈ [0, r_j], total amplitude ≤ Σ_B r_j.

Need: Σ_B r_j < C_G - 3·Σ_G e_j ≈ (2/3)·C_G.

**KEY QUESTION:** Can Σ_B r_j ever exceed (2/3)·C_G for a primitive set?

If we can show that primitive sets always have enough "spread" that the
good layers dominate, this closes the proof.

### Strategy B: Anti-Alignment — MOST POWERFUL

The ε_j(x) functions have different periodicities in x-space:
- Layer j oscillates with period q_j·a_j/M in x (roughly).
- Different layers have different q_j, giving different frequencies.
- If the q_j are "sufficiently independent," the sup of the sum is
  much smaller than the sum of sups.

This is a large-sieve type argument. The bound would be:

  sup |Σ ε_j(x)| ≤ C · √(Σ e_j²)  (Cauchy-type)

instead of Σ e_j (triangle inequality). Much better for many layers
with comparable e_j.

**THIS NEEDS:** The different layers' oscillation patterns to be
genuinely phase-mixed. Requires understanding the joint structure of
the q_j's across peeling steps.

### Strategy C: Endpoint Control — MOST TARGETED

Since M/x ∈ [1/10, 1] on [M, 10M], the worst dips are at x ≈ M.

Key observation: at x = M, y_j(M) = ⌊M/a_j⌋ = r_j (integer part).
The "rough numbers dip" (K_Q(r) = 1 for prime cores) happens HERE.

But at x = 2M: y_j = ⌊2M/a_j⌋ ≈ 2r_j, and K_Q(2r) is typically
much larger (the dip is localized). Meanwhile M/x = 1/2, so T_j(2M)
is comparable to T_j(M) for well-behaved layers but MUCH better for
the "dipping" layers.

**STRATEGY:** Show inf H(x) is NOT achieved at x = M (where the dips
are worst) but at x > M (where dipping layers have recovered).

This is consistent with the computational finding that the worst ratio
is always < 1 - 1/M, achieved by adjacent pairs at the LEFT endpoint.

---

## IMMEDIATE NEXT STEPS

### 1. Codex verification (highest priority)
Compute for ALL tested primitive sets:
  - q_j for each peeling step
  - The ratio Σ ρ_j·q_j / Σ r_j·ρ_j
  - Whether Strategy A's condition holds

### 2. GPT-5.4 Pro (structural)
Bound q_j in terms of M, a_j, k for primitive sets.
Specifically: is q_j ≤ a_j always? (This would make r_j/q_j = M/a_j²·q_j ...
need to think about this.)

### 3. GPT-5.2 Pro (Fourier)
Formalize Strategy B: treat Σ ε_j(x) as a multi-frequency signal and
bound its sup using the structure of the quotient-core periods.

### 4. Claude (computation)
Run the Codex layer verification prompt (codex-layer-prompt.md is ready).
Also: verify the excursion bounds v_j, u_j empirically against the
theoretical predictions.

---

## RISK ASSESSMENT

### Strategy A risks:
- May fail for "adversarial" primitive sets where all layers have
  r_j ≈ q_j (elements are "smooth" relative to their size).
- Scale-invariance: scaling A → tA changes r_j but also changes q_j
  (the quotient cores change). Need to verify the ratio r_j/q_j is
  scale-invariant.

### Strategy B risks:
- Fourier independence of layers is not guaranteed — the Q_j's are
  correlated (they all come from the same primitive set).
- May need genuine algebraic independence conditions.

### Strategy C risks:
- Requires understanding WHERE inf H(x) is achieved — this may vary
  across primitive sets with no clean universal bound.

### THE MOST PROMISING PATH:
Strategy A for non-compact sets + existing Theorem 6 for compact sets,
with Strategy C as a backup for "near-compact" sets.

---

## FILE LOCATIONS
- 5.2's full response: gpt52-collective-oscillation-budget.md
- Claude's literature analysis: claude-sieve-layer-analysis.md
- Layer framework: layer-decomposition-framework.md
- Kill #46: kill46-local-discrepancy.md
- Scale invariance: scale-invariance-constraint.md
