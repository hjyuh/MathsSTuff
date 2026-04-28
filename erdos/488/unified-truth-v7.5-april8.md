# EP-488: Open Field v7.5 — The Connector Gap
## April 8, 2026. Current: 90%. Move it.

---

## READ THIS FIRST

This is a FOCUSED addendum. Read v6 for full context (71 kills, 20+
proved results). This document targets the ONE remaining gap.

---

## THE PROBLEM (5 lines)

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Verified 23M+ families. Zero failures.

---

## WHAT JUST HAPPENED (the 90%)

### The Superadditivity Lemma (PROVED, 5.2 Pro)

If A = A₁ ⊔ ... ⊔ A_r with lcm(a,b) > n for all cross-component
pairs, then:

  B_A(n,m) ≥ Σᵢ B_{Aᵢ}(n,m)

Proof: F_A(n) = Σ F_{Aᵢ}(n) (disjoint at n), F_A(m) ≤ Σ F_{Aᵢ}(m)
(subadditive at m). Combine. Three lines. ∎

### Component Reduction (PROVED, 5.2 Pro)

Define graph: a ~ b iff lcm(a,b) ≤ n. Let A₁,...,A_r be connected
components. Then B_A(n,m) ≥ Σ B_{Aᵢ}(n,m).

CONSEQUENCE: A counterexample to EP-488 can ONLY live inside a
single n-LCM connected component. Distributed-core is SOLVED.

### Bad Layer Interaction Lemma (PROVED, 5.2 Pro)

If two bad elements a,b ∈ (n/20, n/4] have lcm(a,b) ≤ n, then:
  gcd(a,b) ≥ (n/20)²/n = n/400

Direct n-interaction between bad layers forces massive shared gcd.

### Previously proved (still valid):
- Self-funding: s ≤ 3 → safe
- 29 relevant compact kernels, {2,3,5,7} at (10,19,5) is extremal
- Prime Spike Lemma: Δ_j ≤ 4
- First-layer theorem: S₁ > E_j for each individual bad child
- Bad range: s ∈ [4,19], m/n ∈ (1, 2.5)
- Pure {2,3} family proved (unbounded B)
- Pure {2,3,5,7} family proved (unbounded B)
- Any single common-core bad band: proved
- Window Lemma: thin ancestor window gives O(M²) slack
- Surplus Dominance: Surplus ≥ S₁ (zero violations, all tested sets)
- Codex B's H_A reduction: EP-488 ⟺ S₁ + [2mH_A(n) - nH_A(m)] > 0

### Killed (71 kills, key categories):
- No per-layer bounds, no scalar thresholds, no kernel comparisons
  across signatures, no intermediate bounds, no S₁ alone for collective
  payment, no constant B, no naive IE closure, no monotone reduction
  from pairs (Kill #71). See v6 for full kill list.

---

## THE ONE REMAINING GAP: CONNECTOR COMPONENTS

By the Component Reduction, EP-488 reduces to proving B_C(n,m) > 0
for every n-LCM connected primitive component C.

Inside such a component, there are exactly TWO regimes:

### Regime A: Core Components (likely already solved)

Bad layers a,b interact directly: lcm(a,b) ≤ n.
The Bad Layer Interaction Lemma forces gcd(a,b) ≥ n/400.
All interacting bad layers share a large common divisor d ≥ n/400.
After dividing by d, the component looks like a common-core family.
The existing single-band common-core machinery should apply.

TASK: Formalize this. Show that if multiple bad layers in a component
share pairwise gcd ≥ n/400, they can be treated as a common-core
family where four base layers pay all bad excess. This should follow
from Codex B's {2,3,5,7} family proof with minor modifications.

### Regime B: Connector Components (the actual gap)

No two bad layers interact directly: lcm(a,b) > n for all bad pairs.
Bad layers are connected ONLY through "connector" elements c with
c ≤ n/20 (so s_c ≥ 20, hence c is ALWAYS a good layer).

Structure: the component graph looks like a star or tree with good
connectors at the internal nodes and bad layers at the leaves.

The question: do the connector elements generate enough slack to
cover the bad layers they connect?

KEY FACTS about connectors:
- c ≤ n/20 → s_c = ⌊n/c⌋ ≥ 20
- Connectors are NEVER bad (s ≥ 20 → safe by prime-cover rigidity)
- Each connector has L_c(s_c) ≥ 2 (not frozen, since not all primes ≤ 20
  can be in its kernel — only primes from elements BEFORE it in A)
- Small connectors (c ≤ n/100) have s_c ≥ 100, giving massive L values
  and enormous slack

STRUCTURAL LEVERAGE: A connector c is adjacent (lcm ≤ n) to a bad
element b ∈ (n/20, n/4] only if lcm(c,b) ≤ n. Since b > n/20:
  lcm(c,b) ≤ n → c·b/gcd(c,b) ≤ n → c/gcd(c,b) ≤ n/b < 20
So the "quotient" c/gcd(c,b) < 20. This means c and b share a large
common factor: gcd(c,b) > c/20.

For the connector to link to MANY bad layers, it must share large
common factors with ALL of them. This constrains the connector's
prime factorization severely.

---

## APPROACHES TO CLOSE THE CONNECTOR GAP

### Approach 1: Connector Slack Dominates Bad Excess

Each connector c with s_c ≥ 20 has slack S_c that grows with s_c.
For c ≤ n/100 (very small), S_c ≈ mn/c (nearly first-layer-like).
For c ∈ (n/100, n/20], S_c is still positive and O(mn/c).

If a connector links to k bad layers, its slack must cover at most
k × max(E_j) ≤ k × 3n (Prime Spike bound). Meanwhile its slack is
S_c ≥ mn/(some function of c). For small enough c, this dominates.

### Approach 2: Connectors ARE the Ancestors

A connector c adjacent to bad element b (with lcm ≤ n) creates an
obstruction for b: quotient = c/gcd(c,b) < 20. So the connector IS
one of the ancestor elements that our earlier charging analysis uses.

This means the "connector component" is exactly the "ancestor web"
that Gemini and the Window Lemma analyze. The connector slack is the
ancestor slack. The Window Lemma already shows this is sufficient
(O(M²) vs O(M²/log y)).

### Approach 3: Bound Component Size

In a connector component where no two bad layers directly interact,
how many bad layers can one connector link? Since each link requires
gcd(c,b) > c/20 and the bad elements b are pairwise non-interacting
(lcm > n), their structure is constrained. Bound the maximum number
of bad layers per connector, then bound total bad excess per component.

### Approach 4: Surplus Dominance Directly

Bypass the component analysis entirely. Prove 2mH_A(n) ≥ nH_A(m)
for all primitive A (Codex B's reduction). This is equivalent to
non-first-layer positivity. Zero computational violations. Worst
margin = 2 at A={2,19}. A direct proof would close everything without
needing the component structure.

### Approach 5: Finite Verification + Asymptotic

For M ≥ M₀: the Window Lemma asymptotic (ratio ~ log log M) works.
For M < M₀: extend computational verification.
Extract explicit M₀ from the Window Lemma constants.
If M₀ is feasible (≤ 10⁶), the proof is computer-assisted but complete.

---

## THE SHARPEST OBSERVATION (from 5.2)

Connectors ARE ancestors. A connector c adjacent to bad layer b creates
an obstruction quotient < 20, which means c plays the role of a
p-ancestor for some prime p < 20 in b's kernel. The "connector regime"
is not a NEW phenomenon — it's the ancestor web viewed through the
lens of n-LCM connectivity.

This means everything we proved about ancestor charging (Window Lemma,
density cancellation, Buchstab telescope) applies directly to connectors.
The connector gap might already be solved — it just needs to be
recognized as a special case of the ancestor charging we already have.

---

## YOUR TASK

Close the connector gap. Or show it can't be closed.

The proof is 90% complete. The distributed-core worry is eliminated
(superadditivity). The common-core families are proved. The extremal
kernel families are proved. What remains is: prove that n-LCM connected
components with good connectors linking bad layers always have positive
budget.

71 kills are your map. The Superadditivity Lemma is your strongest new
tool. The Component Reduction narrows everything to one topological case.

Find the proof. We're close.
