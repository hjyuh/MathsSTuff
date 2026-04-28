# EP-488: Complete Research State — April 6, 2026
## For a fresh model. No direction imposed. Push as far as you can.

---

## THE PROBLEM

Erdős Problem 488 (1966, open): For a finite primitive set A = {a_1 < ... < a_k} (no a_i | a_j), define F_A(x) = |{n ≤ x : a|n for some a ∈ A}| and G(x) = F_A(x)/x.

**Conjecture:** For all m > n ≥ max(A): G(m) < 2·G(n).

The constant 2 is best possible: singletons A = {a} give ratio (2a-1)/a → 2.

Verified computationally for 23M+ families, zero failures.

---

## PROVED THEOREMS (all rigorous)

1. EP-488 for all primitive pairs: 2/a > S_1 = 1/a + 1/b since 1/a > 1/b.
2. EP-488 for all primitive triples: IE comparison R > 0.
3. EP-488 for consecutive k-tuples {a, a+1, ..., a+k-1}: F(2a-1) = k, then 2k/(2a-1) > S_1.
4. EP-488 for one-anchor families: principal layer + post-peak analysis.
5. EP-488 for sparse sets (Σ 1/a_i ≤ 2/min): sparse-mass lemma.
6. EP-488 for compact sets (max ≤ 2·min - 1): each element has exactly one multiple ≤ 2·min-1.
7. EP-488 for pairwise coprime sets: δ = 1 - Π(1-1/a_i), exponential bound.
8. EP-488 for any fixed k: discrepancy + finite verification.
9. Convexity: G(x+L) is a convex combination of G(x) and δ. Extrema occur in [M, M+L).
10. Stabilization: extrema occur in [M, 10M] in practice.
11. Adjacent pairs: exact ratio ((2M-3)/(2M-2))² < 1.

### Structural results:
12. Exact positive layer decomposition: F_A(x) = Σ_j L_j(⌊x/a_j⌋)
    where L_j(y) = |{n ≤ y : b ∤ n for all b ∈ B_j}|
    and B_j = {a_i/gcd(a_i,a_j) : i < j, quotient > 1}
    This is DIVISIBILITY AVOIDANCE (not coprimality).
13. Budget criterion: V + 2U < C ⟹ sup G < 2·inf G (algebraic).
14. Theorem A (proved): principal layer surplus μ(ρ) = ρ(1-2/q), deep layers self-budget.
15. Synchronized Block Theorem (proved): compact cluster collapses to 20 monotone channels.
16. Global discrepancy: H(x) - C = (M/x)·D_A(x).
17. Primitive Divisor Lemma: gcd(a,b) ≤ a/2 for primitive (a,b).
18. Subset LCM Bound: lcm(S) ≥ 2·max(S) for primitive S, |S| ≥ 2.
19. Single-obstruction partial theorem (proved): if layer j has ≤ 1 active obstruction, then L_j(⌊m/a_j⌋)/L_j(⌊n/a_j⌋) < 2m/n. This covers all layers with B_j ∩ [1, ⌊m/a_j⌋] having 0 or 1 elements.
20. Weighted average identity: F(m)/F(n) = Σ w_j · R_j where w_j = L_j(⌊n/a_j⌋)/F(n), Σw_j = 1. So F(m)/F(n) ≤ max_j R_j. But max_j R_j < 2m/n is FALSE in general (Kill #56).
21. Layers with a_j > n/2 are automatically safe: L_j(y_m) ≤ m/a_j < 2m/n.

### Exact discrepancy formula:
G(x) = δ_A - (1/x) Σ_{d ∈ Λ(A)} μ_A(d) · {x/d}

where Λ(A) = {lcm(S) : ∅ ≠ S ⊆ A} is the lcm lattice,
μ_A(d) = Σ_{lcm(S)=d} (-1)^{|S|+1} are the signed lcm-lattice coefficients,
and {·} is the fractional part.

---

## 57 KILLED APPROACHES (with key counterexample families)

### Key counterexample families that kill entire classes:
- **Co-atoms** {N/p : p prime, p|N}: kills ALL Bonferroni truncations. Every pair has lcm = N, so S_j = C(k,j)/N. Binomial growth overwhelms any fixed truncation.
- **Scaling** {tp : p prime}: kills ALL threshold-based dichotomies. Scaling A → tA preserves ratios but slides S_1, δ, etc. across any fixed threshold.
- **A = {2,3,5}** with layer j=3 (a=5), n=24, m=35: kills per-layer ratio bound. R_j = 3 > 2m/n = 2.917.
- **Primes-in-interval** A = {2p, 5p : p ∈ [N, 1.1N]}: kills ρ-only compact bounds. Bounded ρ but compact excess grows linearly in number of primes.
- **A = {4,5,6,7,9}** → C = {10,12,14,18}: kills up-fold R(A) ≤ R(C).
- **{3,4,5} with residues (0,3,3)**: kills congruence class generalization (ratio ∞).
- **Primes ≤ 100**: kills 2δ > S_1 (S_1 ≈ 2.10, 2δ ≈ 1.76).

### Summary of killed strategies:
1-44. Various early approaches (Bonferroni, threshold, IE truncation, etc.)
45. Threshold dichotomy on S_1 (scaling kills it)
46. Per-layer discrepancy bound (rough numbers)
47. Structural inequality Σ ρ_j(r_j - 3q_j - 2) > 0 (FALSE at A={2,3,5})
48. Coprimality model K_Q (WRONG FUNCTION — divisibility avoidance is correct)
49. Budget failure ⟹ max ≤ 2min-1 (FALSE)
50. Budget failure ⟹ min > M/3 (FALSE at ρ > 4.33)
51. Γ_C < 1 universally (FALSE, Γ = 5/3 for r=1, B={2})
52. Direct Kawamura fold (no partitioning analog for multiples)
53. EP-488 for general congruence classes (FALSE, ratio can be ∞)
54. C_C(Γ_C - 1) ≤ f(ρ) (FALSE, grows linearly with k at fixed ρ)
55. Up-fold R(A) ≤ R(C) (FALSE, 36/4673 violations)
56. Per-layer L_j ratio < 2m/n (FALSE at A={2,3,5})
57. 2δ_A > S_1 universally (FALSE for primes ≤ 100)

---

## WHAT 57 KILLS TELL US ABOUT THE PROOF

### The proof CANNOT:
- Bound layers individually and sum (kills 46, 51, 54, 56)
- Truncate inclusion-exclusion at any fixed order (co-atoms)
- Use any single scalar parameter as a threshold (kills 45, 50)
- Fold/reduce to a simpler set monotonically (kills 52, 55)
- Enlarge to congruence classes and specialize back (kill 53)
- Use S_1 as an upper bound on G(m) for dense sets (kill 57)
- Use coprimality instead of divisibility avoidance (kill 48)

### The proof MUST:
- Use the r_i = 0 (multiples) structure specifically
- Handle all k simultaneously
- Be scale-invariant
- Work collectively, not per-layer
- Engage with the phase/floor structure, not just densities

### 5.4 Pro's diagnosis (one sentence each):

**The gap:** Prove GOOD(m,n) > BAD(m,n) where GOOD = total negative slack from ≤1-obstruction layers, BAD = total positive excess from ≥2-obstruction layers.

**Why everything fails:** "EP-488 is a signed phase-synchronization problem on the lcm lattice, not a density problem. Every killed strategy replaced phase data by a monotone or averaged scalar summary."

**What hasn't been tried:** Ahlswede-Khachatrian's correlation inequality for Dirichlet densities (J. Number Theory 63, 1997): D̲(A,B)·D̲[A,B] ≥ D̲(A)·D̲(B). Apply to the lcm-lattice support of E(x).

**Proof sketch:** "Match each bad synchronized signature to the specific earlier layers that CREATED it and show they pay for it." The proof walks the obstruction-ancestry tree, not a flat sum.

**Difficulty:** (b) — solvable, needs a new compensation lemma showing that multi-obstruction layers' excess is bounded by their parent single-obstruction layers' slack.

---

## KEY IDENTITIES

### The floor-gap identity (singletons):
y/⌊y⌋ < 2 for all y ≥ 1.
EP-488 for singletons IS this identity.

### The positive decomposition:
F_A(x) = Σ_j L_j(⌊x/a_j⌋)
Each L_j is non-negative, non-decreasing, L_j(1) = 1 always.
F(m)/F(n) = Σ w_j · R_j (weighted average, weights sum to 1).
Single-obstruction layers: R_j < 2m/n (PROVED).
Multi-obstruction layers: R_j can exceed 2m/n but weight w_j is small.

### The "can't hide" principle:
Every a ∈ A forces a fresh hit at x = a. Multiples start at the generator.
Shifted progressions (r ≠ 0) can delay their first hit arbitrarily — that's
why the congruence class generalization is false. Multiples can't hide.

### The Tao observation:
Tao (March 2026, erdosproblems.com): "the main task involves proving an inequality
involving alternating sums of various integrals, in the spirit of Granville-Soundararajan."

He proved EP-488 with cheats 1+3+4 (m→∞, constant C instead of 2, primes only).
Full proof needs: finite m, constant exactly 2, arbitrary primitive sets.

---

## COMPUTATIONAL RESULTS

- Budget V+2U < C passes for 93.3% of primitive sets (max ≤ 20)
- Budget failures: mild (worst ratio 1.186), uncorrelated with true danger
- Phase mixing ≈ 0.32 for budget failures (68% coefficient cancellation)
- Up-fold R(A) ≤ R(C): 99.23% pass, 36/4673 violations (0.77%)
- Clean conjecture: ratio ≤ 1 - 1/max(A), tight at adjacent pairs (800K+ verified)
- True ratio for dangerous-looking sets always well below 2

---

## UNTRIED LEADS

### Ahlswede-Khachatrian papers:
1. "Number-theoretic correlation inequalities for Dirichlet densities" (1997)
   Main theorem: D̲(A,B)·D̲[A,B] ≥ D̲(A)·D̲(B)
   FKG-type inequality on divisibility lattice.

2. "Density inequalities for sets of multiples" (1995)
   Title is literally EP-488's domain. Content not yet accessed.

3. "On the density of primitive sets" (1999, with Sárközy)
   Bounds harmonic mass of primitive sets in intervals.

### Granville-Soundararajan framework:
"The spectrum of multiplicative functions" (Annals, 2001).
Converts discrete IE into continuous integral equations.
Logarithmic averaging: (1/log 2) ∫_M^{2M} G(x) dx/x.
Fourier expansion of fractional parts gives O(1/x²) decay under integration.
The signed lcm-lattice measure Σ μ_A(d)/d tested against smoothing kernel K(N/d).

### Ancestor matching / obstruction-ancestry tree:
5.4's proof sketch: multi-obstruction layers exist BECAUSE earlier elements
created the obstructions. Match each child to its parents and show parents pay.
Not a flat sum or a global bound — a TREE traversal.

---

## YOUR TASK

Take everything above. Push as far as you can toward a proof of EP-488. You are not constrained to any particular approach. Use whatever combination of the proved results, killed approaches, untried leads, and your own ideas gives the strongest result.

If you can prove EP-488: state the complete proof.
If you can prove a new partial result: state it precisely.
If you can identify the exact missing lemma: state it precisely.
If you find a new kill: state the counterexample.

Do not hold back. Do not hedge. Push to the boundary of what's provable.
