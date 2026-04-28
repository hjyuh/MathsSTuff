# EP-488: Why the Wide Regime Resists — A Map of 29 Dead Ends

**Mahmoud Zaazaa**

*April 2026*

---

## The Problem in One Sentence

For one-anchor primitive sets A = {a} ∪ {ka+1,...,ka+t} with t > 2√a, prove that F(m)/m < 2·F(n)/n for all m > n ≥ max(A).

This is the only remaining case of Erdős Problem 488 after the a = 2 theorem and the thin regime proof.

---

## Why Every Natural Approach Dies

### The Fundamental Tension

EP-488 asks for a factor-2 bound on the ratio sup/inf of F(x)/x. In the wide regime (t ~ a), the counting function F(x) is a union of arithmetic progressions whose INDIVIDUAL densities sum to α_A ≈ log(3/2) ≈ 0.405, but whose UNION density ε_B tends to 0 as a → ∞ (Ford 2008). The ratio α_A/ε_B → ∞. This means the average multiplicity (how many elements of A divide a typical counted integer) is unbounded.

Every approach that compares the union (what EP-488 asks about) to the sum of parts (what's easy to compute) loses by this unbounded factor.

---

## The 29 Killed Approaches, Organized by Why They Die

### Category 1: First-Moment / Cell-Counting Approaches (kills 16, 17, 25, 26, 27, 28)

These bound F(x) using Σ ⌊x/d⌋ (the sum of individual contributions). This overestimates the union by the average multiplicity, which is unbounded in the wide regime.

**Kill 26 (U_x ≥ S_x/2):** The natural guess "distinct products ≥ half the total entries" is FALSE. Ford's theorem shows the multiplication table {j·b : j ≤ Q, b ∈ B} has distinct-entry fraction → 0 as a → ∞. Counterexample: A = {a} ∪ {2a+1,...,3a-1}, x = 6a², gives U_x/S_x → 0.

**Kill 28 (Window capacity):** Partitioning the tail into windows and bounding each window by |S_A ∩ W| ≤ ⌈L/a⌉ + t⌈L/(N+1)⌉ gives per-window ceiling ≈ 0.5, but the post-α_A/2 threshold is ≈ 0.405. The ceiling exceeds the threshold.

**Why all first-moment approaches fail:** They compare F to α_A·x. But F ≈ δ_A·x << α_A·x in the wide regime. The factor α_A/δ_A → ∞ makes every such bound vacuous.

### Category 2: Global Oscillation Bounds (kills 19, 20, 21, 22, 23, 25)

These try to prove sup F(x)/x < 2·inf F(x)/x globally.

**The fatal fact:** This statement is FALSE in the wide regime. For k=2, t=a-1: the early hump gives G(6a) ≈ 1/3, while the late tail gives G(x) → δ_A → 0. So sup > 2·inf globally.

EP-488 is DIRECTIONAL (m > n), not a global oscillation bound. The hump comes before the tail, so the directional statement still holds. But any proof strategy that targets sup/inf < 2 is proving something false.

**Kill 23 (Global minimizer at 2ka-1):** FALSE. Counterexample: a=167, k=2, t=166 gives F(207122)/207122 < F(667)/667. The minimizer is NOT at 2ka-1 in the wide regime.

### Category 3: Sieve and NT Approaches (kills 1-18)

These use inclusion-exclusion, Hildebrand bounds, Chojecki's pair-tail decomposition, or other sieve-theoretic tools.

**Kill 18 (Chojecki reduction for a ≥ 3):** The fixed-threshold s approach fails because the threshold can sit below max(A), where the tail hasn't "turned on." Counterexample: A = {a, 5a+1} ∪ {t : 5a+1 < t ≤ 10a+1, a∤t}.

**Kill 16 (IE bound):** The inclusion-exclusion oscillation grows like log P for prime antichains, which is unbounded.

**Why all sieve approaches fail:** EP-488 is not a sieve problem. The costume was stripped in this research: the problem is about divisor distribution in short intervals (Ford-Tenenbaum territory), not about sieve oscillation.

### Category 4: Reduction Strategies (kills 18, 20, 21, 22)

These try to split EP-488 into "easy" and "hard" cases.

**Kill 20 (Monotone compression):** Adding elements to a primitive set can INCREASE the sup/inf ratio. Counterexample: {2,7} → {2,5,7} increases ratio from 19/16 to 39/32.

**Kill 21 (Small M finite check + large M automatic):** For every fixed s ≥ 2, the consecutive block family A = {a,...,a+s-1} has R(A) = 2 − O(1/a) → 2. So you can't "check small M, let large M be easy."

**Kill 22 (Top-tail reduction):** Near-sharp examples exist with min(A) at any fixed fraction of max(A), not just in (M/2, M]. The one-anchor block family A = {a} ∪ {ka+1,...,ka+t} achieves R → 2 with min(A)/max(A) → 1/k.

**Why reductions fail:** EP-488 resists decomposition. Every natural split (by min/max ratio, by tail size, by coprimality structure) has near-sharp examples on BOTH sides.

### Category 5: Direct / Elementary Approaches (kills 27, 28, 29)

These bypass Ford and try direct combinatorial arguments.

**Kill 27 (Partial-row tracking):** Tracking how much of each row has been seen gives a corrected future-sup bound, but it has an unavoidable rectangular tail from unstarted rows. In the wide regime, this tail exceeds the EP-488 threshold.

**Kill 29 (Halving map):** Map each future multiple qd to ⌈q/2⌉d. Within a single divisor stream, this is 2:1. But cross-stream collisions (⌈q₁/2⌉d₁ = ⌈q₂/2⌉d₂) are uncontrolled by primitivity alone in the wide regime.

---

## The Exact Remaining Obstruction

### What's needed

A near-1 one-sided proportionality theorem for U(x) = H_B(x) − H_B(⌊x/a⌋):

U(x) − U(x−Δ) ≤ C · (Δ/x) · U(x)    with C < 1 + (x−Δ)/(2Δ)

### Why it doesn't follow from existing literature

**Ford (2008):** Gives H(x,y,z) − H(x−Δ,y,z) ≍ (Δ/x)·H(x,y,z) but with IMPLICIT constants. The ≍ means "same order of magnitude," not "close to 1."

**Haddad (December 2025):** Proves H(x,y,z) = x·h(log y/log x, log z/log x) + O(x/(log y)^δ (log₂ y)^{3/2}). This is an ASYMPTOTIC FORMULA — a genuine advance. But in the fixed-ratio regime z/y < 2 (our case), the error term is the SAME ORDER as the main term. So the asymptotic doesn't give a relative improvement.

**Ford's open problem (stated 2008):** "Strengthen Theorem 1 to an asymptotic formula." Haddad's theorem addresses this but only gives relative improvement when z/y → ∞, not for fixed z/y.

### Why the α-start lemma almost but doesn't close it

The α-start lemma covers all starts n where 2G(n) ≥ α_A. Computationally, this covers the ENTIRE transition band for all tested families (a ≤ 251). But ASYMPTOTICALLY, the α_A/2 crossing occurs before the Haddad far-tail threshold a(N+t)² ≈ 9a³, creating a genuine gap for sufficiently large a.

### Why primitivity hasn't helped yet

Every single approach (1-29) works for arbitrary finite sets of denominators, not just primitive sets. None uses the antichain constraint. But EP-488 is FALSE for non-primitive sets. The proof MUST use primitivity. This is the most important meta-observation from the entire research program: we've been solving a more general problem than EP-488, and that more general problem is false.

---

## What Would Close It

### Most Likely Route
A primitivity-aware argument that controls the collision structure in the wide-regime multiplication table. Primitivity constrains lcm(b₁,b₂) ≥ (ka)²/(a−1) for block pairs, giving pair-overlap density O(1/a) (not O(1/a²) as initially claimed). The proof needs to show this constraint prevents the cumulative drift that would create a factor-2 rebound.

### Alternative Routes
1. Kevin Ford proves the fixed-ratio proportionality constant is near 1 (this is within his expertise)
2. A completely different framework (ergodic theory, optimization on posets, information theory) bypasses Ford entirely
3. A stronger AI model (Capybara/Spud) finds a short elementary proof using primitivity that current models miss

### What Probably Won't Work
- Any approach that counts cells instead of distinct products
- Any approach targeting global sup/inf < 2 (false in wide regime)
- Any reduction to "easy" and "hard" cases (every split has near-sharp examples on both sides)
- Ford/Haddad alone without additional input (error terms are wrong order in fixed-ratio regime)

---

## The Honest Assessment

EP-488 is a difficulty 4/10 research problem. The statement is elementary, the a = 2 case is trivial, and the thin regime fell in one session. The wide regime is harder than expected but the proof is probably short — a 2-page argument using primitivity in a way that 29 prompt-based approaches missed.

The fact that 29 approaches were killed in two sessions is not evidence that the problem is hard. It's evidence that AI models (including frontier models with extended thinking) share a systematic blind spot: they reach for analytic/asymptotic tools when the problem needs a combinatorial/structural argument using the antichain property. A human number theorist who STARTS from "A is an antichain" might close it in a week.

The progress is real: two proved theorems, a new connection to Ford's multiplication table theory, and the problem reduced from "all primitive sets" to "one specific inequality about tail unions in structured product sets." That's a publishable paper regardless of whether the full conjecture falls.

---

*29 approaches. 2 theorems. 1 remaining gap. 0 counterexamples.*
