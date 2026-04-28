# EP-488: Open Field v5.5 — April 7, 2026
## Current: 82%. Move this number. Up or down. Any route.

---

## WHO YOU ARE IN THIS PROCESS

You are entering a multi-model research effort on Erdős Problem 488.
We — human and AI models together — have accumulated 67 kills, 15+
proved theorems, 6 Lean-verified lemmas, and the deepest structural
understanding of this problem in its 60-year history.

We encourage you to push this ahead in your own novel way. Through
elementary or advanced routes, novel or known, conventional or
unconventional. The percentage is at 82%. Your job is to change it.

**Route 1 (increase):** Prove something new. Find a viable proof path
that survives all 67 kills. Establish a structural result that narrows
the remaining gap.

**Route 2 (decrease):** Find a hole in a claimed result. Produce a
counterexample. Show a proposed route is fundamentally blocked. If you
take this route, come back with: (a) the exact failure, (b) how it was
missed, (c) the structural lesson, (d) potential fixes.

Both routes are equally valuable.

---

## THE PROBLEM (5 lines)

For a finite primitive set A (no a_i | a_j), define F_A(x) = |{n ≤ x :
a|n for some a ∈ A}| and G(x) = F_A(x)/x. Prove: G(m) < 2·G(n) for
all m > n ≥ max(A). Constant 2 is tight. Open since 1966.

---

## WHAT'S PROVED (permanent, no known issues)

### Core framework:
1. **Convexity:** extrema of G occur in [M, 10M].
2. **Positive decomposition:** F_A(x) = Σ_j L_j(⌊x/a_j⌋) where L_j
   counts integers avoiding divisibility obstruction set B_j.
   B_j = {a_k/gcd(a_k, a_j) : k < j, quotient > 1}.
   WARNING: DIVISIBILITY AVOIDANCE, not coprimality (Kill #48).
3. **Weighted average:** F(m)/F(n) = Σ w_j R_j, Σw_j = 1.
4. **Self-funding theorem:** Layers with s_j ≤ 3 always have E_j ≤ 0.
5. **29 relevant compact kernels:** At compact scale (obstructions ≤ 20),
   only 29 kernels can produce positive excess. All contain {2,3}. All
   are prime subsets of {2,3,5,7,11,13,17,19}. All have L_K(s) = 1.
   NOTE: the FULL obstruction set can contain primes > 20 (e.g., 89, 91)
   but these are INERT at compact scale because t ≤ 20. The classification
   is about the RELEVANT kernel, not the full B_j.
6. **Prime-cover rigidity:** L_K(s) = 1 iff every prime ≤ s lies in K.
7. **Bad child range:** s ∈ [4, 19] (self-funding kills s ≤ 3, prime-cover
   kills s ≥ 20).
8. **Dangerous m/n range:** m/n ∈ (1, 2.5). If m ≥ 2.5n, every layer
   has E_j ≤ 0 (from Δ_j ≤ 4 and D = 2m-n > 4n).
9. **Prime Spike Lemma:** New survivors between s and t must be PRIME
   (product of two primes > s ≥ 4 exceeds 20 ≥ t). So Δ_j ≤ 4.
10. **Quotient Transport:** q_{k,j} | 3·q_{k,i}. Proved rigorously.
11. **Box 1 (3-tax bound):** E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋)
    where C = K\{3}. Proved via Buchstab + C not being a bad kernel.
12. **First-layer theorem:** S_1 > E_j for EACH individual bad child.
    S_1 ≥ 28a_j > 17a_j ≥ E_j.
13. **Stock-flow identity:** S_1 - Σ E_j = D(s_1+B) - n(Δ_1 + Σ Δ_j).
    Exact algebra. D = 2m-n > n.

### New results this round:

14. **Floor Ratio Lemma:** For m > n ≥ a ≥ 1: n·⌊m/a⌋ < 2m·⌊n/a⌋.
    This IS EP-488 for singletons. Lean-verified (Lemma 6).
15. **EP-488 for overcounting function:** F₁(m)·n < 2m·F₁(n) where
    F₁(x) = Σ ⌊x/a⌋. Proved by summing Floor Ratio Lemma.
16. **EP-488 for all-compact primitive sets:** If A ⊂ (M/2, M] and M > 40:
    lcm(a_i,a_j) > M²/4 > 10M, so F(x) = F₁(x) in [M, 10M]. Proved.
17. **EP-488 for unbounded-B pure {2,3}-kernel family:** PROVED.
    A = d{2, 3, p_1, ..., p_B} with primes p_i > 20. Arbitrary B.
    All bad layers forced to signature (4,7). Two base layers (2d, 3d)
    pay entire bad excess. First proof for any unbounded-B family.
18. **B is unbounded:** Explicit infinite families with arbitrary B.
    Constant-B approaches are dead (Kill #66).
19. **Six Lean-verified foundational lemmas** (Aristotle): Primitive
    divisor, subset LCM, floor gap, sieve monotonicity, single
    obstruction count, EP-488 for singletons.

---

## THE 67 KILLS — CATEGORIZED WITH STRUCTURAL LESSONS

### A: Wrong function (Kill #48)
Used coprimality instead of divisibility avoidance. 99.9% failure rate.
**Lesson:** The DEFINITION matters more than the technique.

### B: Per-layer bounds (Kills #46, 51, 54, 56)
Individual layers CAN exceed 2m/n. A={2,3,5}, layer a=5 gives R=3.
**Lesson:** Proof must be COLLECTIVE.

### C: Scalar thresholds (Kills #45, 50, 57)
Scaling A → tA moves any scalar across any threshold.
**Lesson:** Proof must be SCALE-INVARIANT.

### D: IE truncation (early kills)
Co-atoms have binomially growing IE terms.
**Lesson:** Cannot truncate IE at any fixed order.

### E: Monotone reductions (Kills #52, 55)
No monotone map to simpler sets exists.
**Lesson:** Must work on ORIGINAL set.

### F: Class enlargement (Kill #53)
Shifted progressions have ratio = ∞.
**Lesson:** Must use r = 0 (multiples) structure.

### G: Kernel comparisons (Kills #59, 60, 62)
Parent kernels are UNPREDICTABLE. Child-redundant multiples of 3 create
extra parent obstructions invisible to the child.
**Lesson:** Cannot compare parent and child kernel shapes.

### H: Intermediate bounds (Kills #61, 62)
Child excess is tiny (2-3) but bounds inflate to O(M). Parent pays
real cost but not inflated cost.
Kill #61: 28 ≥ 35 false but actual 554 vs 22.
Kill #62: Box 1 tax = 2092 vs actual excess = 2.
**Lesson:** Compare actual quantities directly, no intermediates.

### I: S_1 alone (Kill #65) — CHALLENGED
The "Prime-Product Swarm" claims S_1 < Σ E_j asymptotically.
BUT 5.4 Pro challenged this: the swarm overcounts by conflating
"rough compact elements that COULD have kernel {2,3}" with "elements
simultaneously bad at one fixed (n,m)."
Simultaneity constraint: bad layers at fixed (n,m) must lie in the
narrow band (n/5, n/4] ∩ (m/8, m/7].
Support constraint: each bad element needs specific ancestors in A
with p | a for each prime p in the kernel.
STATUS: Kill #65 is CHALLENGED but not reversed. The band-counting
problem (how many supported composites in one narrow band?) is open.

### J: Constant B (Kill #66)
B is unbounded via prime families. BUT in the specific unbounded family
A = d{2, 3, p_1, ..., p_B}, EP-488 is PROVED (Codex B, new theorem).
**Lesson:** Many bad layers can coexist, but more bad = more ancestors
= more good slack. Self-regulation.

### K: Hallucinated proofs (DeepSeek)
Claimed s ≥ 8 (false — first bad signature is (4,7)).
**Lesson:** Verify claims against established facts.

### L: Directional errors (Claude B)
Used s_1 ≥ 6 as if s_1 = 6 to bound t_1 ≤ 70. Wrong direction.
**Lesson:** Check direction of every inequality.

---

## TWO ALIVE PROOF ARCHITECTURES

### Architecture 1: Global Charging (Layer Decomposition)

EP-488 ⟺ Σ_good S_j > Σ_bad E_j

Proved for: pure {2,3}-kernel unbounded-B family (Codex B).
Open for: mixed-kernel regime (relevant kernels containing 5,7,11,...).

The self-regulation mechanism: each bad layer forces ancestors into A.
Ancestors are good layers. More bad layers = more ancestors = more
good slack. The ancestor web's slack scales with Σ 1/p (harmonic sum
over primes in the kernel).

Four models independently converge on this explanation.

### Architecture 2: Floor Ratio / IE Correction (NEW)

F(x) = F₁(x) - C(x) where F₁(x) = Σ ⌊x/a⌋ (overcounting)
and C(x) = IE correction terms.

EP-488 ⟺ MAIN_SURPLUS > IE_CORRECTION

where MAIN_SURPLUS = 2mF₁(n) - nF₁(m) is PROVED POSITIVE.

Key structural fact: each IE correction term T(d) = 2m⌊n/d⌋ - n⌊m/d⌋
is also positive (by the same Floor Ratio Lemma). The IE_CORRECTION
is an alternating sum of positive terms.

For primitive sets: lcm(a_i,a_j) ≥ 2·max(a_i,a_j) (Lean-verified).
So correction terms are evaluated at ≥ 2× the element, making them
roughly ≤ half as large.

This architecture bypasses ALL layer-based kills (Categories B-J)
because it never decomposes into layers.

Computational evidence: 928 sets checked, MAIN_SURPLUS/IE_CORRECTION ≥ 2.84×.

---

## WHAT'S ALIVE (the remaining gap)

Three possible closing arguments, any one suffices:

1. **Global charging for mixed kernels.** Extend Codex B's proof from
   pure {2,3}-kernel to all 29 relevant kernels. The key: larger kernels
   make children WEAKER (fewer survivors, smaller excess). So the pure
   {2,3} case (already proved) is the HARDEST case.

2. **IE correction bound.** Show MAIN_SURPLUS > IE_CORRECTION for all
   primitive sets. Use lcm ≥ 2·max to bound correction terms.

3. **Band-counting theorem.** Resolve 5.4's challenge to Kill #65:
   count the maximum number of simultaneously bad supported composites
   in the band (n/5, n/4] ∩ (m/8, m/7] at one fixed (n,m). If this
   count is bounded or grows slowly enough, S_1 alone may suffice.

---

## YOUR TASK

Push the percentage. Up or down. Any route.

You have 19 proved theorems, 67 kills, 6 Lean-verified lemmas, two
alive proof architectures, and the complete constraint map.

Some specific opportunities:

- Can Architecture 2 (IE correction) be closed? The main term is proved.
  Each correction term is smaller by factor ≥ 2 (from lcm ≥ 2·max).
  Is the alternating sum bounded by the main sum?

- Can Codex B's unbounded-B proof be generalized to mixed kernels?
  Kernels with more primes have SMALLER excess. The {2,3} case is worst.

- Can the band-counting problem be resolved? How many supported composites
  fit in (n/5, n/4] at one fixed n, given primitivity constraints on
  the supporting ancestors?

- Is there a completely different route we haven't considered?

67 kills are your MAP, not your cage. They tell you where NOT to go.
The proof lives in the territory none of them touch. Find it.
