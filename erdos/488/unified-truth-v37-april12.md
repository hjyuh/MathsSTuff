# EP-488 Unified Truth v37 — April 12, 2026 (Evening)
## The Last Wall: D(x) Inequality for |R| ≥ 3

**Status: 97%. Triple case closed. |Q| ≥ 4 is a genuine mathematical gap. 110 kills.**

**YOUR TASK: Prove the D(x) two-point inequality for |R| ≥ 3 in the top window, or identify the exact obstruction.**

---

## WHAT IS PROVED (the complete chain through triples)

For primitive Q with q = max(Q), R = Q \ {q}, define:
- A_Q(x) = #{t ≤ x : no element of Q divides t}
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}
- O_Q(n,m) = 2·A_Q(n)/n − A_Q(m)/m

Then O_Q(n,m) = O_{q}(n,m) − (2D(n)/n − D(m)/m).

Since O_{q} < 1 (singleton theorem), EP-488 reduces to:
$$\frac{D(m)}{m} \leq \frac{2D(n)}{n} \quad \text{for all } m > n \geq q$$

### Proved cases of this inequality:
1. **|R| = 1 (pairs):** PROVED + machine-verified (Aristotle, 3,103 Lean jobs, zero sorry).
2. **|R| = 2 (triples), any Q with element ≤ q/2:** PROVED (Top Window Theorem). Only Q ⊂ (q/2, q] remains.
3. **|R| = 2 (triples), Q ⊂ (q/2, q], lcm(a,b) > n:** PROVED (overlap term vanishes).
4. **|R| = 2 (triples), Q ⊂ (q/2, q], lcm(a,b) ≤ n, inert (q₀ > M):** PROVED for all coprime (u,v). Machine-verified for (2,3) by Gauss/OpenGauss.
5. **|R| = 2 (triples), Q ⊂ (q/2, q], lcm(a,b) ≤ n, active (q₀ ≤ M), (u,v)=(2,3):** PROVED (Codex B).
6. **|R| = 2 (triples), Q ⊂ (q/2, q], lcm(a,b) ≤ n, active, u ≥ 3:** PROVED by finite reduction (v < 20, g₁ ≤ 10) + exhaustive verification (4.8M tuples, zero violations, three independent checks).

**TRIPLE CASE IS CLOSED.**

---

## WHAT IS NOT PROVED

### |R| ≥ 3 (four or more elements in Q)

The D(x) inequality D(m)/m ≤ 2D(n)/n is NOT proved for |R| ≥ 3.

### KILLED APPROACHES (do NOT attempt these):

**Kill #110: Operator monotonicity under adjoining — DEAD.**
Concrete counterexample: Q = {5,6,8,9,11,13,14}, Q' = Q ∪ {21}. max O_Q ≈ 0.465 but max O_{Q'} ≈ 0.468. Adding element 21 INCREASED the global maximum. Therefore "adding elements lowers max O_Q" is FALSE.

**Kill #109: Pointwise Δ(m)/m ≤ 2Δ(n)/n at run-end extremizers — DEAD.**
Q' = {4,5,6,7,9}, s = 6, extremizer (62,372): Δ(372)/372 > 2Δ(62)/62.

**Kill #108: u_T target lemma — DEAD.** No universal constant.

**Do NOT use any argument of the form "adding elements to Q can only help."** Kill #110 proves this is false.

**Do NOT use any argument that compares Q to a subset of Q.** Unless you prove the comparison holds under specific structural hypotheses (e.g., top window), it is likely false.

---

## THE EXACT TARGET

For primitive Q ⊂ (q/2, q] with |Q| ≥ 4 and q = max(Q), R = Q \ {q}, prove:
$$\frac{D_Q(m)}{m} \leq \frac{2D_Q(n)}{n} \quad \text{for all } m > n \geq q$$

where D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}.

### Structural constraints from the top window:
- All elements of R satisfy q/2 < r < q
- Q is primitive: no element divides another
- Since all r > q/2, any two elements r₁, r₂ ∈ R satisfy r₁ + r₂ > q, so lcm(r₁,r₂) ≥ r₁ + r₂ > q ≈ n. This means MOST pairwise overlaps are in the "lcm > n" regime where the overlap term vanishes.
- |R| is bounded: since all elements are in (q/2, q) and primitive, |R| ≤ q/2.

### The inclusion-exclusion expansion:
$$D_Q(x) = \sum_{\emptyset \neq S \subseteq R} (-1)^{|S|+1} \left(\left\lfloor \frac{x}{\text{lcm}(S)} \right\rfloor - \left\lfloor \frac{x}{\text{lcm}(S \cup \{q\})} \right\rfloor\right)$$

For |S| = 1: each term gives a pair contribution B_r ≥ 0 (pair theorem).
For |S| ≥ 2: lcm(S) ≥ r₁ + r₂ > q ≈ n for most pairs in the top window. When lcm(S) > n, the contribution at n is zero, making the corresponding B_S ≤ 0 (it HELPS).

### Why the top window makes |R| ≥ 3 potentially easier than triples:
In the top window (q/2, q], pairwise lcms are large (> q). For |S| ≥ 2, most overlaps have lcm(S) > n, contributing B_S ≤ 0. The "bad" overlaps (where lcm ≤ n) require shared factors, which means they compress to small coprime cores — exactly the regime already handled in the triple case.

### Density argument (heuristic, needs rigor):
D_Q(x)/x oscillates near density δ_R = Σ 1/r − (overlap corrections) with |δ_R| < 1. The inequality needs δ + ε ≤ 2(δ − ε'), which holds when the errors are small relative to δ. In the top window, δ_R ≈ |R|/(2q) (each r ∈ R contributes ~1/r ≈ 2/q). For |R| ≥ 3, δ ≥ 3/(2q). The factor of 2 dominates the O(1/n) floor errors for n ≥ q.

---

## LIVE PROOF STRATEGIES (not killed)

### Strategy A: Direct Bonferroni on D(x) in the top window
Show that in the top window, the inclusion-exclusion for D(x) satisfies a Bonferroni-type inequality:
$$\sum_{\emptyset \neq S \subseteq R} (-1)^{|S|+1} B_S \geq 0$$
The |S| = 1 terms are positive (pair theorem). The |S| ≥ 2 terms with lcm(S) > n are ≤ 0 (they help). The remaining |S| ≥ 2 terms with lcm(S) ≤ n require shared factors among R-elements, compressing to coprime cores already handled.

**Key question:** In the top window, can lcm(S) ≤ n occur for |S| ≥ 2? Since all r > q/2, we need r₁·r₂/gcd(r₁,r₂) ≤ n ≈ 2q, which requires gcd(r₁,r₂) > r₁·r₂/(2q) > q/4. So shared factors must be large. For |S| ≥ 3, lcm(S) grows even faster — it is plausible that lcm(S) > n for ALL |S| ≥ 3 in the top window.

### Strategy B: Triple domination in the top window
Prove: for any primitive Q ⊂ (q/2, q] with |Q| ≥ 4, there exists a triple T ⊂ Q with |T| = 3 such that O_Q ≤ O_T. This would reduce |Q| ≥ 4 to the already-proved triple case.

**Key question:** Does removing elements from Q always decrease or preserve D(x)? Pointwise, D_Q(x) ≥ D_T(x) (more moduli cover more), so 2D_Q(n)/n − D_Q(m)/m ≤ 2D_T(n)/n − D_T(m)/m is NOT automatic (both sides change). The comparison needs care.

### Strategy C: Density domination with top-window structure
In the top window, δ_R < 1 (density of D is bounded). The inequality D(m)/m ≤ 2D(n)/n holds when sup D(Y)/Y < 2 · inf D(Y)/Y for Y ≥ q. Since D(Y)/Y ≈ δ and δ < 1, we have δ < 2δ trivially. The floor errors are O(|R|/q), and for |R| ≤ q/2 these are O(1/2). The gap between δ and 2δ is δ itself. For δ > O(1/2) the inequality holds. When is δ small? Only when |R| is very small — but |R| ≤ 2 is already proved!

### Strategy D: Computational verification for bounded |R|
Since all elements are in (q/2, q] and primitive, |R| is bounded for any given q. For moderate q, enumerate all valid Q and verify. Combined with a monotonicity-in-q argument, this closes the problem.

---

## COMPUTATIONAL EVIDENCE

- 109,295 primitive Q ⊂ [2,25]: singleton ALWAYS extremal (5.4 Pro)
- 50,000 random antichains max ~80: zero violations (5.2 Pro)
- All primitive triples max ≤ 50: zero violations across all regimes

---

## FORMAL VERIFICATION ASSETS

| Result | System | Status |
|--------|--------|--------|
| Pair theorem | Aristotle | ✅ Zero sorry |
| Coprime core (2,3) | Gauss | ✅ Zero sorry |
| Triple case defs | AXLE | ✅ Type-checks |
| Adjacent pair (partial) | Aristotle | ⚠️ 6/9, 3 FALSE |

---

## MODEL RANKINGS (for context, not hierarchy)

- **5.4 Pro:** Best grinder. Proved 3 theorems + kill #110. Use for: rigorous proof attempts.
- **Codex B:** Best quality control. Found bugs, proved active cases. Use for: structural analysis + gap identification.
- **Codex BA:** Best computation. Use for: exhaustive verification + tooling.
- **5.2 Pro:** Strong on D(x) formulation but stuck on kill #109 loop. Use for: D(x) specific analysis.
- **Qwen:** Good structural intuition but overclaims. Verify all "QED" independently.
- **DeepSeek:** Good strategic framing. Retracted overclaims responsibly.
- **Gemini:** Offline today. Domain Amputation + Additive Contraction from earlier sessions.

---

## WHAT I NEED FROM YOU

1. **Attempt Strategy A, B, C, or D** — or propose a new one.
2. **If you believe a strategy works, give an explicit proof.** Check your constants. Do not declare QED without verifying the final inequality numerically at the worst case.
3. **If you find an obstruction, state it precisely** with a concrete example.
4. **The top-window constraint (all r > q/2) is your main tool.** It forces pairwise lcms to be large, limits |R|, and constrains the overlap structure. Use it.
5. **Do not use operator monotonicity under adjoining. It is dead (kill #110).**

---

## KILLS (110 total)
- #110: Operator monotonicity under adjoining (5.4 Pro). Q={5,6,8,9,11,13,14}, Q'=Q∪{21}.
- #109: Suffix-minimizer Δ inequality at run-end extremizers (5.2 Pro).
- #108: u_T target lemma (four confirmations).
- 1-107: All previous.

---

## STATUS: 97%

Triple case closed (hybrid analytic + computational proof). |Q| ≥ 4 extension requires a new argument that respects kill #110. The top window structure provides strong constraints — most higher-order overlaps have lcm > n and automatically help. The question is whether the residual overlaps with lcm ≤ n can be controlled by the same coprime core machinery that closed the triple case.

**EP-488 was posed October 5, 1960. The triple case fell April 12, 2026. The finish line is one theorem away.**
