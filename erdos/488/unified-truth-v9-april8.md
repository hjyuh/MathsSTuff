# EP-488: Open Field v9 — April 8, 2026
## Current: 85%. Increase it or decrease it.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## HOW TO READ THIS DOCUMENT

This is a research battlefield. 76 approaches have been tried and
killed. 25+ results have been proved. The percentage represents how
close we are to a complete proof.

Your job: move the percentage. Up or down.

**Increasing** means proving something new, finding a viable proof
path, or establishing a result that narrows the gap. Use any
combination of novel, known, conventional, or unconventional
approaches. Elementary or advanced. If you think you can close it
in one shot, try. If you see a small lemma that helps, prove it.

**Decreasing** means finding a hole in a claimed result, producing
a counterexample, or showing a route is blocked. If you do this,
explain: (a) the exact failure, (b) how it was missed, (c) the
structural lesson, (d) potential fixes.

Both are equally valuable. A kill at 85% saves us from building
on false foundations.

---

## WHAT'S PROVED (25+ permanent results)

### Core framework (scale-independent):
1. Convexity: extrema of G in [M, 10M].
2. Positive decomposition: F(x) = Σ L_j(⌊x/a_j⌋).
   L_j counts integers avoiding DIVISIBILITY obstruction set B_j.
   B_j = {a_k/gcd(a_k,a_j) : k < j, quotient > 1}.
   WARNING: divisibility avoidance, NOT coprimality (Kill #48).
3. Weighted average: F(m)/F(n) = Σ w_j R_j, Σw_j = 1.
4. Self-funding: s ≤ 3 → E_j ≤ 0.
5. First-layer theorem (SCALE-INDEPENDENT): Any layer with s ≥ 4
   and a quotient-2 support satisfies S₁ > E_j.
   Proof: a₁ ≤ 2a/3, E ≤ n(m-n)/a - 2(m-n), S₁ ≥ m(3n/(2a)-2).
   S₁ - E ≥ n(m/(2a) + n/a - 2) > 0 since n/a ≥ 4, m > n.
6. Floor Ratio Lemma: n⌊m/a⌋ < 2m⌊n/a⌋ for a ≤ n. (Lean-verified)
7. H_A reduction: EP-488 ⟺ 2mH_A(n) ≥ nH_A(m) where
   H_A(x) = |{k ≤ x : a₁ ∤ k, ∃ a ∈ A\{a₁} with a|k}|.
   Equivalently: "non-first-layer net contribution ≥ 0."

### Component theory (scale-independent):
8. Superadditivity: If lcm(a,b) > n for cross-component pairs,
   then B_A(n,m) ≥ Σ B_{Aᵢ}(n,m). (PROVED, 3 lines)
9. Component Reduction: counterexample lives in single n-LCM component.
10. {2,3}-component safety: If 2,3 ∈ C → B_C > 0. (PROVED)
11. Lifted {2,3}-core safety: If C = dB with 2,3 ∈ B → B_C > 0.
    (PROVED independently by THREE models)
12. Edge quotient bound: x ~ y in n-LCM graph → q ≤ ⌊n/y⌋.
13. Band degree-size: k elements in depth-s band sharing quotient
    class from vertex c → c ≤ n/((s+1)(k-1)).
14. Kernel prime → LCM neighbor: prime p ≤ s in kernel of a via
    witness b → lcm(a,b) ≤ n. Deep bad at depth s → π(s) neighbors.

### Compact-scale results (valid for t ≤ 20 only):
15. 29 relevant compact kernels, all ⊇ {2,3}, all prime.
16. Compact bad range: s ∈ [4,19], m/n < 2.5, Δ ≤ 4.
17. Signature table: {2,3,5,7} at (10,19,5) is compact extremal (c=17).
18. Pure {2,3} family proved, unbounded B.
19. Pure {2,3,5,7} family proved, unbounded B.
20. Single-band common-core at any depth s ≥ 7: base layer pays.

### Lean-verified (6 lemmas):
21. Primitive divisor, subset LCM, floor gap, sieve monotonicity,
    single obstruction count, EP-488 for singletons.

### Computational:
22. Surplus Dominance: Surplus ≥ S₁ with ZERO violations across
    all tested primitive sets (subsets of [2,19], swarm families,
    composite swarms, random search M ≤ 500). Worst ratio 1.33.
23. 23M+ families verified for EP-488. Zero failures.

---

## THE 76 KILLS — WHAT CANNOT WORK

Every approach sharing a structural feature with a killed approach
will also die. Understanding WHY each failed is critical.

**A: Wrong function (#48).** Coprimality ≠ divisibility avoidance.
**B: Per-layer bounds (#46,51,54,56).** Individual R_j CAN exceed 2m/n.
**C: Scalar thresholds (#45,50,57).** Scaling defeats fixed thresholds.
**D: IE truncation.** Co-atoms grow binomially.
**E: Monotone reductions (#52,55).** No monotone map exists.
**F: Class enlargement (#53).** Shifted progressions have ratio ∞.
**G: Kernel comparisons (#59,60,62).** Parent kernels unpredictable.
**H: Intermediate bounds (#61,62).** Actual excess tiny, bounds inflate.
**I: S₁ alone (#65, CONFIRMED).** Swarm overwhelms any single layer.
**J: Constant B (#66).** B unbounded.
**K: Hallucinations.** DeepSeek claimed s ≥ 8 (false).
**L: Directional errors.** Wrong inequality direction in proof.
**M: Naive IE factor closure (#68).** Pair strands eat 5/6 of main.
**N: Wrong proofs (#69).** All-compact proof wrong, T(d) sign wrong for d>n.
**O: Kernel monotonicity global reduction (#70).** {2,3} mildest globally.
**P: Monotone reduction from pairs (#71).** Adding elements can decrease surplus.
**Q: Compact-scale extrapolation (#72-75).** Deep bad layers exist at any s.
    s ∈ [4,19] is compact-only. Δ ≤ 4 is compact-only. m/n < 2.5 compact-only.
**R: gcd structural reduction (#76).** n-LCM components with bad layers
    CAN have gcd = 1. Three models, multiple counterexamples.
    Split-core pattern {2u, 3v, uv} with coprime u,v has gcd = 1.
    Even gcd(bad layers) > 1 is false. Coprime bad layers exist.
    No structural reduction to lifted common-core works.

---

## THE REMAINING GAP (15%)

76 kills have mapped every dead approach. Every structural shortcut
is dead. Every reduction to a simpler case is dead. The proof must
work DIRECTLY on general primitive sets.

The gap in one sentence: prove 2mF(n) > nF(m) for all primitive A
and all m > n ≥ max(A), without reducing to any special structure.

Equivalently (H_A reduction): prove that the non-first-layer covered
integers satisfy 2mH_A(n) ≥ nH_A(m).

### What we know about the gap:
- Computationally verified everywhere with zero violations
- Surplus Dominance (Surplus ≥ S₁) holds with worst ratio 1.33
- The self-regulation mechanism is confirmed: more bad layers create
  more ancestors create more good slack
- The asymptotic works: ancestor slack ~ M², bad excess ~ M²/log y
- Every specific construction works with massive margins
- The split-core pattern {2u, 3v, uv} is the irreducible hard
  configuration that escapes all structural reductions
- But even the split-core always satisfies EP-488 computationally

### Properties of primitive sets that haven't been fully exploited:
- Erdős: Σ 1/(a log a) < ∞ for primitive sets
- Behrend: primitive sets have density 0
- The lcm structure: lcm(a_i,a_j) ≥ 2·max for primitive pairs
- F_A(x) = x·δ_A + O(x/log x) where δ_A = Σ μ_A(d)/d
- Besicovitch: sup δ_A = 1/2 (achieved by even numbers)

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

76 kills are your map of dead territory. 25+ proved results are
your tools. The computational evidence is overwhelming. The proof
exists — it just hasn't been found yet.

Try everything. Elementary, advanced, novel, known. Combinatorial,
analytic, algebraic, probabilistic. Direct proof, contradiction,
induction, generating functions, Fourier analysis, graph theory,
sieve methods. Whatever you think might work.

If you find the proof: state it clearly with all steps.
If you find a hole: explain it with a counterexample.
If you find a partial result: state what it covers and what remains.

Find the proof. Or tell us why it can't be found with current tools.
