# EP-488: Open Field v5 — April 7, 2026
## Current: 78%. Move this number. Up or down. Any route.

---

## WHO YOU ARE IN THIS PROCESS

You are entering a multi-model research effort on Erdős Problem 488.
We — human and AI models together — have accumulated 66 kills, 12+
proved theorems, 6 Lean-verified lemmas, and the deepest structural
understanding of this problem in its 60-year history.

We encourage you to push this ahead in your own novel way. Through
elementary or advanced routes, novel or known, conventional or
unconventional. The percentage is at 78%. Your job is to change it.

**Route 1 (increase):** Prove something new. Find a viable proof path
that survives all 66 kills. Establish a structural result that narrows
the remaining gap. Build on what's proved.

**Route 2 (decrease):** Find a hole in a claimed result. Produce a
counterexample. Show that a proposed route is fundamentally blocked.
If you take this route, come back with: (a) the exact failure,
(b) how we missed it, (c) what structural lesson it teaches, and
(d) potential fixes or new directions suggested by the failure.

Both routes are equally valuable. A kill at 78% saves us from building
on a false foundation. A proof at 78% closes a 60-year-old problem.

---

## THE PROBLEM (5 lines)

For a finite primitive set A (no a_i | a_j), define F_A(x) = |{n ≤ x :
a|n for some a ∈ A}| and G(x) = F_A(x)/x. Prove: G(m) < 2·G(n) for
all m > n ≥ max(A). Constant 2 is tight. Open since 1966.

---

## WHAT'S PROVED (permanent results, no known issues)

1. **Convexity:** extrema of G occur in [M, 10M].
2. **Positive decomposition:** F_A(x) = Σ_j L_j(⌊x/a_j⌋) where L_j
   counts integers avoiding divisibility obstruction set B_j.
   B_j = {a_k/gcd(a_k, a_j) : k < j, quotient > 1}.
   WARNING: this is DIVISIBILITY AVOIDANCE, not coprimality. Using
   coprimality is Kill #48 — the single most important correction of
   the project.
3. **Weighted average:** F(m)/F(n) = Σ w_j R_j, Σw_j = 1, w_j = L_j(s_j)/F(n).
4. **Self-funding theorem:** Layers with s_j ≤ 3 always have E_j ≤ 0.
   Proof: case analysis on density of survivors (s=1: singleton EP-488;
   s=2: odd-number density; s=3: coprime-to-6 density + case split on m/n).
5. **29-kernel classification:** Only 29 compact kernels can be bad.
   All contain {2,3}. All are subsets of {2,3,5,7,11,13,17,19}. All have
   L_K(s) = 1. Exhaustive check of 10,239 antichain kernels.
6. **Prime-cover rigidity:** L_K(s) = 1 iff every prime ≤ s lies in K.
7. **Bad child range:** s ∈ [4, 19]. Self-funding kills s ≤ 3.
   Prime-cover kills s ≥ 20 (would need prime 23 in kernel, impossible).
8. **Dangerous m/n range:** m/n ∈ (1, 2.5). If m ≥ 2.5n, every layer
   has E_j ≤ 0 because Δ_j ≤ 4 and D = 2m-n > 4n forces E_j = nΔ_j - D < 0.
9. **Prime Spike Lemma:** New survivors between s and t must be PRIME
   (product of two primes > s ≥ 4 exceeds 20 ≥ t). So Δ_j ≤ 4.
10. **Quotient Transport:** q_{k,j} | 3·q_{k,i}. Proved rigorously.
11. **Box 1 (3-tax bound):** E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋)
    where C = K\{3}. Proved via Buchstab + C not being a bad kernel.
12. **First-layer theorem:** S_1 > E_j for EACH individual bad child.
    S_1 ≥ 28a_j > 17a_j ≥ E_j. Uses: a_1 ≤ 2a_j/3 (primitivity),
    n ≥ 4a_j (s ≥ 4), no obstructions for first layer.
13. **Stock-flow identity:** S_1 - Σ E_j = D(s_1+B) - n(Δ_1 + Σ Δ_j).
    Exact algebra. D = 2m-n > n. No approximation.
14. **Six Lean-verified foundational lemmas** (Aristotle):
    Primitive divisor, subset LCM, floor gap, sieve monotonicity,
    single obstruction count, EP-488 for singletons.

---

## THE 66 KILLS — IN DEPTH

Each kill teaches a structural lesson. Understanding WHY each approach
failed is as important as knowing THAT it failed.

### CATEGORY A: Wrong function (Kill #48)
**What:** Used coprimality (K_Q counting integers coprime to quotient set)
instead of divisibility avoidance (L_j counting integers not divisible by
any element of B_j).
**Why it failed:** 99.9% failure rate. The two functions are different
because divisibility is not the same as coprimality when quotients share
factors.
**Structural lesson:** The DEFINITION matters more than the technique.
Every result built on the wrong function was garbage. This is the most
important kill because it was invisible — the wrong function gave
plausible-looking results until computational verification caught it.
**Any approach must use divisibility avoidance L_j, not coprimality.**

### CATEGORY B: Per-layer bounds (Kills #46, 51, 54, 56)
**What:** Bound each layer's ratio R_j < 2m/n individually, then the
weighted average is automatically safe.
**Why it failed:** Individual layers CAN exceed 2m/n. Example: A={2,3,5},
layer a=5, n=24, m=35 gives R_j = 3 > 2.917 = 2m/n.
**Structural lesson:** Bad layers have small weights (w_j = 1/F(n)), so
R_j > 2m/n doesn't break the weighted average. But you can't PROVE this
by bounding R_j — you must use the COLLECTIVE structure.
**Any approach must be collective, not per-layer.**

### CATEGORY C: Scalar thresholds (Kills #45, 50, 57)
**What:** Find a parameter (S₁, ρ, δ, k) that separates safe from dangerous.
**Why it failed:** Scaling A → tA preserves ratios but moves any scalar
across any fixed threshold. No absolute scalar can distinguish safe from
dangerous.
**Structural lesson:** EP-488 is SCALE-INVARIANT. The proof must be too.
**Any approach must work at all scales simultaneously.**

### CATEGORY D: Inclusion-exclusion truncation (early kills)
**What:** Truncate the Möbius/IE expansion at some fixed order j.
**Why it failed:** Co-atom sets {N/p : p prime | N} have IE terms
S_j = C(k,j)/N that grow binomially. Any fixed truncation is overwhelmed.
**Structural lesson:** The IE coefficients have no fixed sign pattern.
**Any approach must handle the full IE, not a truncation.**

### CATEGORY E: Monotone reductions (Kills #52, 55)
**What:** Map A to a simpler set C where EP-488 is easier.
**Why it failed:** No monotone map exists. Up-fold can INCREASE the ratio
(36/4673 violations). Kawamura fold has no partitioning analog.
**Structural lesson:** The map changes which integers are covered in
non-monotone ways.
**Any approach must work on the ORIGINAL set.**

### CATEGORY F: Class enlargement (Kill #53)
**What:** Prove EP-488 for shifted progressions (r ≠ 0), specialize to
multiples (r = 0).
**Why it failed:** Shifted progressions can have ratio = ∞. Multiples are
special because r = 0 pins all phases at zero.
**Structural lesson:** The r = 0 structure is ESSENTIAL.
**Any approach must use the multiples structure specifically.**

### CATEGORY G: Kernel comparisons (Kills #59, 60, 62)
**What:** Compare parent and child kernels — show parent kernel equals
K\{3}, or is dominated by it in sieve strength, or is primitive-incompatible
with dangerous configurations.
**Why it failed:**
- Kill #59: A={8,9,12}, parent kernel {8} ≠ K\{3}={2}.
- Kill #60: A={2,9,15,25}, parent kernel {2,3}, MORE obstructed than K\{3}.
- Kill #62: A={2,5,9,33,39,69,161,307}, parent gets extra obstructions 11,13
  from elements that are "child-redundant" (invisible to child because 3
  already handles their multiples).
**Structural lesson:** Parent kernels are UNPREDICTABLE. Elements creating
obstructions for the parent can be invisible to the child (child-redundant
multiples of 3). The quotient transport (q_{k,j} | 3·q_{k,i}) constrains
INDIVIDUAL obstruction pairs but NOT the full parent kernel.
**Any approach must avoid comparing parent and child kernel shapes.**

### CATEGORY H: Intermediate bounds (Kills #61, 62)
**What:** Factor the comparison S_i ≥ E_j through an intermediate inequality
(discrete inequality 2t[L_i(s')-1] ≥ (s+1)[L_i(t')+L_j(t)], or the 3-tax
route Box 1 + Box 2).
**Why it failed:** The child excess is TINY (typically 2-3) but intermediate
bounds inflate it to O(M). The parent can trivially pay the real cost but
can't pay the inflated cost.
- Kill #61: A={2,9,15,25}, discrete inequality gives 28 ≥ 35 (false), but
  actual compensation is 554 vs 22.
- Kill #62: A={2,5,9,33,39,69,161,307}, Box 1 tax = 2092 but actual E_j = 2.
  Parent slack = 2090 < 2092 = tax, but 2090 >> 2 = actual excess.
**Structural lesson:** Any intermediate bound between E_j and S_i loses
information. The actual excess is so small that even a 2× intermediate
bound can flip the inequality.
**Any approach must compare actual quantities directly, or use the global
budget without intermediate factoring.**

### CATEGORY I: S_1 alone (Kill #65)
**What:** Show S_1 (first layer's slack alone) exceeds Σ E_j.
**Why it failed:** The "Prime-Product Swarm" construction produces
arbitrarily many bad layers:
- Choose prime threshold p_1 ≈ log M.
- Ancestors: {2p : p prime in [p_1, M/3]} ∪ {3q : q prime in [p_1, M/3]}.
- Swarm: {a ∈ (M/2, M] : gcd(a,6)=1, all prime factors ≥ p_1}.
- Each swarm element gets kernel {2,3} from its ancestors.
- B ≈ M/(2e^γ log p_1) swarm elements.
- Total excess ≈ 0.7M · B ∝ M²/log log M.
- S_1 ≈ M²/p_1 ∝ M²/log M.
- Since p_1 >> log p_1: S_1 << Σ E_j asymptotically.
**Structural lesson:** A single good layer can pay every individual bad
child (First-layer theorem: S_1 > E_j for each j), but NOT all of them
simultaneously when B is large. The bad mass grows as B·E_j while S_1
grows more slowly than B.
**Any approach must use ALL good layers collectively, not just S_1.**

### CATEGORY J: Constant B (Kill #66)
**What:** Bound the number of simultaneous bad layers by a constant.
**Why it failed:** Explicit infinite family with arbitrary B:
A = {2d, 3d, dp_1, ..., dp_B} where p_1 < ... < p_B are primes with
14p_B ≤ 15p_1 - 4. All dp_i have kernel ⊇ {2,3} and (s,t) = (4,7).
B is unbounded.
**Structural lesson:** Many bad layers can coexist because adjacent or
nearby compact elements with independent obstruction networks can all
have the same (s,t) = (4,7) signature simultaneously.
**But:** In Codex B's family, S_1 STILL dominates Σ E_j (proved:
S_1/Σ E_j → 980). The self-regulating property works: more bad layers
→ more ancestors → smaller a_1 → larger S_1.

### CATEGORY K: Hallucinated proofs (DeepSeek)
**What:** Claimed to prove uniqueness by asserting s ≥ 8 (false — first
bad signature is (s,t) = (4,7)).
**Structural lesson:** Always verify claims against established facts.
s ≥ 8 contradicts the 29-kernel classification. The "proof" was five
sections of confident nonsense. Trust computations, not confidence.

### CATEGORY L: Directional errors (Claude B)
**What:** "Proved" S_1 ≥ Σ E_j by using s_1 ≥ 6 as if it were s_1 = 6
to bound t_1 ≤ 70. But s_1 can be arbitrarily large, so t_1 is unbounded.
**Structural lesson:** Using a LOWER bound where you need an UPPER bound
(or vice versa) can make a false proof look correct. Always check the
DIRECTION of every inequality in a proof chain.

---

## THE CENTRAL MYSTERY (what 66 kills reveal)

Every mechanism that tries to explain WHY compensation works has been
killed. But the compensation ITSELF has never failed across 6,659+
instances and multiple infinite families.

Four independent models converge on the same structural explanation:

**"Bad compact children are frozen at n (L_K(s)=1). They unfreeze with
a few prime spikes between n and m. The good layers (ancestors + first
layer + others) have already banked massive accumulated mass at n. The
coefficient structure (D = 2m-n > n) makes banked mass worth more than
new flow. So the good budget overwhelms the bad excess."**

In mathematical language:
  Total budget = 2mF(n) - nF(m) = Σ_good S_j - Σ_bad E_j

The proved facts constrain both sides:
- Each E_j = n·Δ_j - D where Δ_j ≤ 4 (prime spike lemma)
- Bad layers only exist when m/n < 2.5
- Good layers include ALL ancestors and the first layer
- Each bad layer CREATES ancestors that become good layers (self-regulation)

---

## WHAT'S ALIVE: THE GLOBAL BUDGET

The only unproved statement:

  Σ_{good j} S_j > Σ_{bad j} E_j

where S_j = 2m·L_j(s_j) - n·L_j(t_j) for good layers and
E_j = n·L_j(t_j) - 2m·L_j(s_j) for bad layers.

Equivalently: 2mF(n) > nF(m), i.e., F(m)/F(n) < 2m/n.

Evidence:
- 23M+ families verified, zero violations
- 6,659+ ancestor instances verified, zero failures
- Every infinite family tested satisfies it
- The self-regulating property: more bad layers create more good layers
- Asymptotic analysis: good slack grows as M² log log M, bad excess
  grows as M²/log log M, ratio (log log M)² → ∞

---

## YOUR TASK

Push the percentage. Up or down. Any route.

You have 14 proved theorems, 66 kills, 6 Lean-verified lemmas, and the
complete constraint map. Every approach in Categories A-L is dead.

Some directions nobody has fully explored:

1. **Global charging without matching.** Don't match bad layers to
   specific good layers. Show the AGGREGATE good slack dominates
   AGGREGATE bad excess using properties of F(n) and F(m) directly.

2. **The self-regulation theorem.** Each bad layer with kernel ⊇ {2,3}
   forces at least a 2-ancestor and a 3-ancestor into A. Each ancestor
   is a good layer with positive slack. Prove: the ancestors' combined
   slack exceeds their children's combined excess.

3. **Sieve theory on F directly.** F_A(x) = |{n ≤ x : ∃ a ∈ A, a|n}|
   = x·δ_A - E(x) where δ_A = Σ μ_A(d)/d. Can you bound E(x)
   pointwise using properties of primitive sets?

4. **The Buchstab functional.** L_K(x) = L_{K\{p}}(x) - L_{K\{p}}(x/p).
   The child is a discrete derivative. The good layers are accumulated
   mass. Can you prove accumulated mass dominates the derivative globally?

5. **Induction on |A|.** Base case (singletons, pairs) proved. Inductive
   step: adding an element to A either doesn't create a new bad layer,
   or creates a new bad layer + ancestors whose net contribution is positive.

6. **Something entirely different** that we haven't thought of.

Remember: 66 kills are your MAP, not your cage. They tell you where NOT
to go. The proof lives in the territory none of them touch.

Find it.
