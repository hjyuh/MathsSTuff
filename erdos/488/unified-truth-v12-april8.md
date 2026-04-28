# EP-488: Open Field v12 — April 8, 2026
## Current: 91%. Increase it or decrease it.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## HOW TO USE THIS DOCUMENT

Move the percentage. Up or down. Any route. Any method.

---

## THE PROOF CHAIN (what's built)

### Elimination chain (all scale-independent, all proved):
- s = 1: isolated, no neighbors possible → eliminated
- s = 2: all quotients forced to 2 → dominated-LCM prunable → eliminated
- s = 3: Δ(n) = 1, budget difference m(2-n/(2a)) > 0 → prunable → eliminated
- **s ≥ 4: the ONLY surviving depth in any minimal counterexample**

### Decomposition chain (all proved):
1. Superadditivity → connected components
2. Articulation superadditivity → biconnected blocks
3. Separator superadditivity → separator-tight atoms
4. Leaf-pruning → degree ≥ 2
5. Dominated-LCM pruning → incomparable quotient sets

### Size results:
- |A| = 1: Lean-verified
- |A| = 2: proved (pairs)
- |A| = 3: PROVED (layer 1 safe, layer 2 single-obstruction safe,
  layer 3 bad → first-layer theorem pays it)
- |A| = 4: OPEN — the current frontier

### Safety results:
- Literal-2 safety: 2 ∈ A → safe
- Lifted literal-2 safety: dB with 2 ∈ B → safe
- Lifted {2,3}-core safety: dB with 2,3 ∈ B → safe
- Single-obstruction safety: ≤ 1 obstruction → safe
- First-layer theorem: S₁ > E_j for each individual bad child

### Analytic:
- Floor Ratio Lemma: n⌊m/a⌋ < 2m⌊n/a⌋ (Lean-verified)
- H_A reduction: EP-488 ⟺ 2mH_A(n) ≥ nH_A(m)
- H₁ main term: nH₁(m) < 2mH₁(n) (overcounting safe)
- Divisibility monotonicity: T(d) ≥ T(kd)

### 78 kills mapping dead territory (categories A-T in prior docs)

---

## CLAUDE'S THOUGHTS

I want to focus on one concrete question: **can we prove |A| = 4?**

Here's why this matters more than it seems. The decomposition chain
reduces general sets to separator-tight atoms. The smallest possible
atom has 3 vertices (triangle) — but |A| ≤ 3 is already proved. So
the smallest UNPROVED atom has 4 vertices.

If we prove |A| = 4, the smallest unproved atom has 5 vertices.
If we prove |A| = 5, it's 6. Each step raises the floor.

But more importantly: the |A| = 4 case is where we FIRST encounter
genuinely collective behavior (two bad layers needing simultaneous
payment). If we can solve it, the mechanism might generalize.

**The |A| = 4 landscape:**

Layer 1: safe (no obstructions). Budget S₁ > 0.
Layer 2: safe (single-obstruction safety). Budget S₂ > 0.
Layer 3: CAN be bad (2 obstructions possible). Budget ±E₃.
Layer 4: CAN be bad (up to 3 obstructions). Budget ±E₄.

EP-488 for |A| = 4 ⟺ S₁ + S₂ + contribution₃ + contribution₄ > 0.

If layers 3,4 are both bad: need S₁ + S₂ > E₃ + E₄.

We know S₁ > E₃ (first-layer theorem) and S₁ > E₄ (first-layer theorem).
We know S₂ > 0 (single-obstruction safety).

So S₁ + S₂ > E₃ (since S₁ > E₃ and S₂ > 0).
Need: S₁ + S₂ > E₃ + E₄.
This needs: S₂ > E₄.

**Can we prove S₂ > E₄ (or more generally, S₂ > E_j for any bad layer j)?**

S₂ is the budget of a single-obstruction layer. It's positive (proved)
but HOW positive? Is it always larger than any individual bad layer's excess?

This would be a "single-obstruction layer PAYS any bad layer" theorem.
It would be a strict strengthening of single-obstruction safety (which
only says S₂ > 0).

Alternatively: maybe the n-LCM graph structure at |A| = 4 forces
decomposition. If the graph isn't K₄ (complete), there's a missing
edge → separator decomposition → reduces to |A| ≤ 3 (proved).

If the graph IS K₄: it's 3-connected, no separator works. But K₄
with 4 primitive elements, all with s ≥ 4, every pair lcm ≤ n...
this forces all 4 elements to share massive pairwise gcds. The
structure might be so constrained that a direct budget computation
closes it.

**The K₄ constraint:** For 4 primitive elements a < b < c < d, all
with s ≥ 4 (so a,b,c,d ≤ n/4), and all 6 pairwise lcm ≤ n:

lcm(a,b) ≤ n means gcd(a,b) ≥ ab/n ≥ (n/4)²/n = n/16.
So every pair shares a gcd ≥ n/16. With 4 elements, this is
EXTREMELY dense. All four elements are essentially "n/16-smooth
multiples of a common core."

This might force a lifted common-core structure (gcd(A) > 1), which
would make the lifted safety theorems apply. Or it might not — but
the constraint is so tight that a case analysis might close it.

Or maybe none of this graph theory matters. Maybe the answer is:
prove S₂ > E_j directly (single-obstruction layer pays any bad layer),
then |A| = 4 follows from S₁ + S₂ > E₃ + E₄, and induction using
separator decomposition handles |A| ≥ 5.

I don't know. But |A| = 4 feels like the RIGHT target. It's concrete,
it's the first genuinely hard case, and solving it would reveal the
mechanism that handles collective payment.

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

If you can prove |A| = 4, do it.
If you can prove S₂ > E_j (single-obstruction pays any bad layer), do it.
If you can prove K₄ forces gcd > 1, do it.
If you can prove Surplus Dominance directly, do it.
If you can find a 4-element counterexample to S₁+S₂ > E₃+E₄, report it.
If you see a completely different path, take it.

78 kills. 38 results. 91%. Nine percent from solving a 60-year problem.

Find those nine percent.
