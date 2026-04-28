# EP-488: Open Field v6 — April 7, 2026
## Current: 80%. Move this number. Up or down. Any route.

---

## WHO YOU ARE IN THIS PROCESS

You are entering a multi-model research effort on Erdős Problem 488.
We — human and AI models together — have accumulated 69 kills, 20+
structural results, 6 Lean-verified lemmas, and the deepest understanding
of this problem in its 60-year history.

We encourage you to push this ahead in your own novel way. Through
elementary or advanced routes, novel or known, conventional or
unconventional. The percentage is at 80%. Your job is to change it.

**Route 1 (increase):** Prove something new that survives all 69 kills.
**Route 2 (decrease):** Find a hole, produce a counterexample, show a
route is blocked. Come back with: (a) the exact failure, (b) how it
was missed, (c) the structural lesson, (d) potential fixes.

Both routes are equally valuable.

---

## THE PROBLEM (5 lines)

For a finite primitive set A (no a_i | a_j), define F_A(x) = |{n ≤ x :
a|n for some a ∈ A}| and G(x) = F_A(x)/x. Prove: G(m) < 2·G(n) for
all m > n ≥ max(A). Constant 2 is tight. Open since 1966.
Verified on 23M+ families. Zero failures.

---

## WHAT'S PROVED (permanent results — verified, no known issues)

### Core framework:
1. **Convexity:** extrema of G occur in [M, 10M].
2. **Positive decomposition:** F_A(x) = Σ_j L_j(⌊x/a_j⌋) where L_j
   counts integers avoiding divisibility obstruction set B_j.
   B_j = {a_k/gcd(a_k, a_j) : k < j, quotient > 1}.
   WARNING: DIVISIBILITY AVOIDANCE, not coprimality (Kill #48).
3. **Weighted average:** F(m)/F(n) = Σ w_j R_j, Σw_j = 1.

### Bad layer classification:
4. **Self-funding theorem:** Layers with s_j ≤ 3 always have E_j ≤ 0.
   (s=1: singleton; s=2: odd density; s=3: coprime-to-6 + case split.)
5. **29 relevant compact kernels:** At compact scale (quotients ≤ 20),
   only 29 kernels produce positive excess. All ⊇ {2,3}. All prime
   subsets of {2,3,5,7,11,13,17,19}. All satisfy L_K(s) = 1.
   NOTE: the FULL obstruction set can contain primes > 20 (e.g., 89).
   These are INERT at compact scale (t ≤ 20). The classification is
   about the RELEVANT kernel, not the full B_j.
6. **Prime-cover rigidity:** L_K(s) = 1 iff every prime ≤ s lies in K.
7. **Bad child range:** s ∈ [4, 19]. Self-funding kills s ≤ 3.
   Prime-cover kills s ≥ 20.
8. **Dangerous m/n range:** m/n ∈ (1, 2.5). If m ≥ 2.5n, every layer
   has E_j ≤ 0 (from Δ_j ≤ 4 and D = 2m-n > 4n).
9. **Prime Spike Lemma:** New survivors between s and t must be PRIME
   (product of two primes > s ≥ 4 exceeds 20 ≥ t). So Δ_j ≤ 4.

### Structural results:
10. **Quotient Transport:** q_{k,j} | 3·q_{k,i}. Proved rigorously.
11. **Box 1 (3-tax bound):** E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋).
12. **First-layer theorem:** S_1 > E_j for EACH individual bad child.
    S_1 ≥ 28a_j > 17a_j ≥ E_j. Uses: a_1 ≤ 2a_j/3, n ≥ 4a_j.
13. **Stock-flow identity:** S_1 - Σ E_j = D(s_1+B) - n(Δ_1 + Σ Δ_j).
    Exact. D = 2m-n > n.

### Floor Ratio / IE framework:
14. **Floor Ratio Lemma:** For m > n ≥ a ≥ 1: n·⌊m/a⌋ < 2m·⌊n/a⌋.
    This is EP-488 for singletons. Lean-verified.
15. **EP-488 for overcounting function:** F₁(m)·n < 2m·F₁(n) where
    F₁(x) = Σ ⌊x/a⌋. Proved by summing Floor Ratio Lemma.
16. **T(d) sign structure:** T(d) = 2m⌊n/d⌋ - n⌊m/d⌋.
    T(d) > 0 for d ≤ n. T(d) ≤ 0 for d > n. Sign flips at d = n.
    The Floor Ratio Lemma applies ONLY for d ≤ n.

### Kernel and family results:
17. **Kernel Monotonicity:** If K₁ ⊆ K₂ (both ⊇ {2,3}), both frozen
    (L_K(s) = 1), then E_{K₂} ≤ E_{K₁} at the same (s,t,n,m).
    The pure {2,3} kernel produces the LARGEST excess. {2,3} is worst case.
18. **EP-488 for unbounded-B pure {2,3}-kernel family:** PROVED.
    A = d{2, 3, p_1, ..., p_B} with primes p_i > 20. Arbitrary B.
    All bad layers forced to (4,7). Two base layers pay all bad excess.
19. **B is unbounded:** Explicit infinite families with arbitrary B.
20. **Six Lean-verified foundational lemmas** (Aristotle).

---

## THE 69 KILLS — CATEGORIZED WITH STRUCTURAL LESSONS

Understanding WHY each approach failed is critical. Every kill teaches
a structural lesson that constrains the proof space. Approaches that
share a structural feature with a killed approach will also die.

### A: Wrong function (Kill #48)
Used coprimality instead of divisibility avoidance.
**Lesson:** The DEFINITION of L_j matters. 99.9% failure with wrong one.

### B: Per-layer bounds (Kills #46, 51, 54, 56)
Individual layers CAN exceed 2m/n.
**Lesson:** Proof must be COLLECTIVE.

### C: Scalar thresholds (Kills #45, 50, 57)
Scaling A → tA defeats any fixed threshold.
**Lesson:** Proof must be SCALE-INVARIANT.

### D: IE truncation (early kills)
Co-atoms have binomially growing IE terms.
**Lesson:** Cannot truncate IE at fixed order.

### E: Monotone reductions (Kills #52, 55)
No monotone map to simpler sets exists.
**Lesson:** Must work on ORIGINAL set.

### F: Class enlargement (Kill #53)
Shifted progressions have ratio = ∞.
**Lesson:** Must use r = 0 structure.

### G: Kernel comparisons (Kills #59, 60, 62)
Parent kernels are UNPREDICTABLE. Child-redundant multiples of 3
create obstructions invisible to the child.
**Lesson:** Cannot compare parent/child kernel shapes.

### H: Intermediate bounds (Kills #61, 62)
Child excess is tiny (2-3) but bounds inflate to O(M).
Kill #62: Box 1 tax = 2092, actual excess = 2. Parent pays real cost
(2090) but not inflated cost (2092).
**Lesson:** No intermediate factoring — compare actual quantities.

### I: S_1 alone (Kill #65 — CONFIRMED)
The "Prime-Product Swarm" generates arbitrarily many bad layers whose
total excess overwhelms S_1.

CONSTRUCTION (rigorously verified):
- Fix huge M. Set n = 4M, m ≈ (113/20)M.
- Simultaneity band: I = (4M/5, 113M/140], length M/140.
  Every a ∈ I has ⌊n/a⌋ = 4, ⌊m/a⌋ = 7 simultaneously.
- Prime threshold y ≈ log M (> 20).
- Swarm S = {a ∈ I : gcd(a,6)=1, P⁻(a) ≥ y, a composite}.
- Ancestors: A_anc = {2p, 3p : p prime in [y, M/3]}.
- A = {M} ∪ A_anc ∪ S.
- Each a ∈ S gets relevant kernel exactly {2,3} (other quotients > 20).
- |S| ≈ cM/log log M (by Mertens product).
- Each E_a ≈ 0.7M. Total Σ E_j ≈ c'M²/log log M.
- S_1 ≈ M²/log M.
- Ratio S_1/Σ E_j → 0.

KEY: This construction explicitly satisfies the simultaneity constraint
(all bad elements in the narrow band at one fixed (n,m)) AND the
support constraint (each has explicit ancestors in A).

**Lesson:** A single good layer pays each individual bad child but NOT
all collectively. The proof MUST use ALL good layers.

### J: Constant B (Kill #66)
B is unbounded. But in specific unbounded family, S_1 still dominates.
**Lesson:** Many bad layers coexist, but self-regulation: more bad
→ more ancestors → more good slack.

### K: Hallucinated proofs (DeepSeek)
Claimed s ≥ 8 (false). Five sections of confident nonsense.
**Lesson:** Verify against established facts.

### L: Directional errors (Claude B)
Used s_1 ≥ 6 as s_1 = 6. Wrong direction.
**Lesson:** Check direction of every inequality.

### M: Naive IE factor closure (Kill #68)
For A = {primes ≤ 59}, n=495, m=545:
MAIN = 456,730, CORR = 230,395. Ratio = 1.982 < 2.
Pair strands (2,q) and (3,q) consume ~5/6 of main surplus asymptotically.
**Lesson:** Cannot bound IE correction by individual term magnitudes.
Must exploit cross-order cancellation or reorganize the alternating sum.

### N: Wrong proof of all-compact EP-488 (Kill #69)
Claimed lcm(a_i,a_j) > M²/4 > 10M for compact pairs.
Counterexample: A = {2d, 3d}, lcm = 6d = 2M ≪ 10M.
Primitivity gives lcm ≥ 2·max, which is only > M for compact pairs,
NOT > 10M.
**Lesson:** lcm ≥ 2·max is sharp. Compact sets DO have overlapping
multiples in [M, 10M].

### O: T(d) sign claim (Kill #69b)
Claimed T(d) > 0 for all d "by Floor Ratio Lemma."
False for d > n: T(d) = -n⌊m/d⌋ ≤ 0.
Example: A={2d,3d}, lcm=6d, n=4d. T(6d) = -4d < 0.
**Lesson:** Floor Ratio Lemma requires d ≤ n. IE correction terms
with d > n have NEGATIVE T(d). The IE decomposition has mixed signs,
not alternating-positive.

---

## THE ONE SURVIVING PROOF ARCHITECTURE: GLOBAL CHARGING

Every other approach is dead:
- Per-layer: killed (B)
- Ancestor matching: killed by kernel unpredictability (G) and intermediates (H)
- S_1 alone: killed by swarm (I)
- Constant B: killed (J)
- IE factor gap: killed by pair density (M)
- IE as shortcut: ratio → 1 (Claude A), same difficulty as EP-488

**What survives: Global Charging.**

EP-488 ⟺ Σ_good S_j > Σ_bad E_j ⟺ 2mF(n) > nF(m)

### Why it should work (the self-regulation mechanism):

Every bad layer with kernel K ⊇ {2,3} requires:
- A 2-ancestor in A (element giving quotient 2)
- A 3-ancestor in A (element giving quotient 3)
- For larger K: a p-ancestor for each prime p ∈ K

These ancestors are good layers with positive slack. The more bad layers
exist, the more ancestors are forced into A, generating more good slack.

### The asymptotic (confirmed with corrections):

In the swarm construction:
- Total ancestor slack ≈ M² · c · log p₁ (corrected for inter-ancestor
  obstructions via Mertens product Π(1-1/q))
- Total bad excess ≈ M² / log p₁
- Ratio ≈ (log p₁)² · c = (log log M)² · c → ∞

The correction matters: ancestors obstruct EACH OTHER (ancestor 2p has
obstructions from all earlier ancestors 2p'). But after correction,
the ratio still diverges. Self-regulation survives inter-ancestor effects.

### What's proved for specific families:

- Pure {2,3}-kernel family d{2,3,p₁,...,p_B}: EP-488 PROVED for all B.
  Two base layers pay everything.
- Kernel monotonicity: {2,3} produces LARGEST excess among all 29 kernels
  at same (s,t,n,m). So {2,3} is the worst case.

### The remaining gap:

The proof must show that for ANY primitive set (not just the pure family),
the global self-regulation holds: Σ_good S_j > Σ_bad E_j.

The specific challenge: in a general primitive set, the ancestor
structure may differ from the pure family. Ancestors can share
obstructions, and the allocation of slack to children is not clean.

---

## APPROACHES NOBODY HAS FULLY EXPLORED

1. **Direct proof of self-regulation.** Each bad layer forces ≥ 2
   ancestors. Each ancestor contributes slack. Show the aggregate
   ancestor slack exceeds aggregate bad excess without matching.
   The asymptotic says this works. Make it uniform.

2. **Induction on |A|.** Base case (singletons): proved (Lean-verified).
   Inductive step: adding an element to A either creates no new bad
   layers, or creates bad layers + ancestors whose net budget is positive.

3. **The Buchstab functional approach.** F(x) satisfies a Buchstab-type
   recurrence through the layer decomposition. Bad layers are discrete
   derivatives. Good layers are accumulated mass. Can you prove mass
   dominates derivatives globally?

4. **Reorganized IE with Euler products.** Architecture 2 fails as a
   termwise bound (Kill #68) but might work if the IE correction is
   reorganized by "prime skeletons" — grouping (p,q), (p,r), (p,q,r)
   terms that cancel internally.

5. **Density bounds on primitive sets.** Erdős proved Σ 1/(a log a) < ∞
   for primitive sets. This constrains how dense A can be at any scale.
   Can this density bound directly control F(m)/F(n)?

6. **Something entirely new.** 69 kills are your MAP, not your cage.
   Every killed approach shares a structural feature that caused its
   death. The proof lives in territory that avoids ALL of these features.

---

## COMPUTATIONAL EVIDENCE

- 23M+ families verified for EP-488 itself (zero failures)
- 10,240 primitive subsets of [2,20] verified for all structural claims
- Every infinite family tested satisfies the global budget
- The worst observed MAIN/CORR ratio is 1.98 (primes ≤ 59)
- The best observed S_1/Σ E_j ratio is 24,642:1 ({2,3,89,91,95})
- The global budget has NEVER failed

---

## YOUR TASK

Push the percentage. Up or down. Any route.

69 kills are your map. 20 proved results are your tools.
The global charging mechanism is real. The asymptotic works.
The gap is: make it uniform, or find a different path entirely.

Find the proof. Or show us why it can't be found with current tools.
