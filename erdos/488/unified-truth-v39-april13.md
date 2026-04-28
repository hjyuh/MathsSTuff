# EP-488 Unified Truth v39 — April 13, 2026 (Morning)
## Seven Theorems. Four Lean Proofs. Frontier: n ≥ 5q/2 Only.

**Status: 98%. Codex B extended safe range to n < 5q/2. Threshold is sharp. 110 kills.**

**YOUR TASK: Prove the D(x) inequality for connected components ≥ 3 in the top window with n ≥ 5q/2, or identify the exact obstruction.**

---

## COMPLETE PROOF CHAIN (all proved)

1. **Singletons:** max O_{q} < 1. Exact closed form.
2. **Pairs:** O_{a,q} < 1. Machine-verified (Aristotle, zero sorry).
3. **Top Window:** Any Q with element ≤ q/2 → O_Q < 1. Only Q ⊂ (q/2, q] competes.
4. **Triple case:** All sub-regimes closed (lcm>n, inert, active (2,3), active u≥3).
5. **n < 2q, all |R|:** Block decomposition — overlap graph is matching → pair/triple per block (Codex B).
6. **n < 5q/2, all |R| (NEW):** Edge types limited to {2:3} and {3:4} only. No path of length 2 fits in top window below 5q/2 (Codex B). All components ≤ 2 → pair/triple.
7. **D-separator superadditivity:** Counterexamples live in single connected components. Machine-verified (Gauss, zero sorry).
8. **Components ≤ 2, any n:** Pair/triple theorems apply.

### Machine-verified (Lean 4):
| # | Theorem | System |
|---|---------|--------|
| 1 | Pair theorem | Aristotle |
| 2 | Coprime core N·C(M) ≤ 2M·C(N) | Gauss |
| 3 | Top Window LCM (lcm ≥ q for a,b > q/2, a ∤ b) | Gauss |
| 4 | Separator superadditivity | Gauss |

---

## THE n < 5q/2 PROOF (Codex B, NEW)

### Edge classification below 5q/2:
For r ~ s in the n-LCM graph with r, s > q/2 and n < 5q/2:
- Write lcm(r,s) = L, r = L/a, s = L/b with a ≠ b coprime
- Since r, s > q/2 and L ≤ n < 5q/2: a, b < 5
- Coprime, distinct, ≥ 2: only {a,b} = {2,3} or {3,4}

### No connected triple below 5q/2:
Every possible path x-y-z through two edges:

| Triple type | Ratio max/min | Fits (q/2,q]? | Min n for edges |
|-------------|---------------|---------------|-----------------|
| {4c,6c,9c} (two 2:3) | 9/4 > 2 | ❌ | — |
| {2c,3c,4c} (2:3 + 3:4) | 4/2 = 2 | ❌ | — |
| {6c,8c,9c} (2:3 + 3:4) | 9/6 < 2 | ✅ | n ≥ 24c > 8q/3 > 5q/2 |
| {8c,9c,12c} (2:3 + 3:4) | 12/8 < 2 | ✅ | n ≥ 36c > 3q > 5q/2 |
| {9c,12c,16c} (two 3:4) | 16/9 < 2 | ✅ | n ≥ 48c > 3q > 5q/2 |

Every triple that fits the top window needs n > 5q/2. QED.

### Sharp threshold:
R = {12d, 15d, 20d}, q ≈ 24d. Connected triangle at n = 60d ≈ 5q/2.

### Correction to v38:
gcd(r,s) > q/4 is FALSE. Counterexample: q=23, r=12, s=15, gcd=3 < 23/4. Correct bound: gcd > q²/(4n).

---

## THE REMAINING FRONTIER

### What's proved by n-range:

| Range | Components | Status |
|-------|-----------|--------|
| q ≤ n < 3q/2 | All isolated | ✅ |
| 3q/2 ≤ n < 2q | Matching only | ✅ |
| 2q ≤ n < 5q/2 | No paths of length 2 | ✅ |
| n ≥ 5q/2, components ≤ 2 | Pair/triple | ✅ |
| **n ≥ 5q/2, component ≥ 3** | **Connected triples+** | **❌ OPEN** |

### The first genuine connected atom:
R = {12d, 15d, 20d} ⊂ (q/2, q] with q ≈ 24d, n = 60d.
- lcm(12d,15d) = 60d = n ✓
- lcm(15d,20d) = 60d = n ✓  
- lcm(12d,20d) = 60d = n ✓
- Connected triangle in the n-LCM graph

### The exact obstruction (Codex BA):
Odd-order IE terms |S| = 3, 5, ... with lcm(S) ∈ (n, m] contribute with positive sign but B_S ≤ 0. Example: R = {64,80,96}, q = 101, lcm = 960 ∈ (n, m], contributes −1/960.

---

## KILLED APPROACHES (do NOT use)

**Kill #110:** Operator monotonicity under adjoining. Q={5,6,8,9,11,13,14}, Q'=Q∪{21}. max O increased.

**Kill #109:** Suffix-minimizer Δ inequality at run-end extremizers.

**Kill #108:** u_T target lemma.

**Do NOT argue "adding elements helps."** Do NOT compare Q to subsets via pointwise monotonicity. Both are dead.

---

## LIVE PROOF STRATEGIES

### Strategy A: Graph-theoretic classification + finite verification
Classify all possible connected R-graphs with |C| ≥ 3 in (q/2, q]. Edge types are {2:3}, {3:4}, and potentially {2:5}, {3:5}, {4:5} for larger n. The set of coprime ratio pairs is finite. For each graph type, verify the D(x) inequality computationally for small q, then prove density domination for large q.

### Strategy B: Direct density domination for connected components
For a connected component C with |C| = k ≥ 3:
- Pair terms contribute Σ B_r ≥ k/(2q) (k positive terms)
- Harmful odd-order terms: at most 2^k terms, each O(1/m)
- For n ≥ 5q/2 and m in the relevant range, pair budget grows linearly in k while harmful terms are bounded
- Needs exact constants

### Strategy C: Separator + leaf pruning under top-window hypothesis
5.4 Pro's separator theorem gives: leaf r attached to s yields Δ_R ≥ Δ_{R\{r}} + Δ_{r,s} − Δ_{s}. Pruning needs Δ_{r,s} ≥ Δ_{s}. This is adjoining-monotonicity — killed IN GENERAL, but perhaps provable in the top window where r, s > q/2 forces structural constraints.

### Strategy D: Codex B's block decomposition extended
For n ≥ 5q/2, classify edge types (now includes {2:5} etc.), find all possible connected subgraphs, show that for each the D(x) inequality holds by reducing to coprime core + finite check.

---

## COMPUTATIONAL EVIDENCE

- 1,400 random top-window sets (q up to 500): zero violations
- Worst case: Q = {55,56,57,59}, ratio ≈ 0.973 (2.7% margin)
- All primitive Q ⊂ [2,25]: singleton always extremal (109,295 sets)
- 4.8M+ computational tuples: zero violations in any regime

---

## MODEL PERFORMANCE NOTES

- **5.4 Pro:** Best grinder. Proved separator superadditivity. Use for rigorous proof attempts.
- **Codex B:** Best precision. Proved n < 5q/2, corrected gcd bound. Use for structural analysis.
- **Codex BA:** Best computation. Scanner suite, odd-overlap obstruction. Use for verification.
- **Qwen:** Good structure, overclaims constants. Verify all "QED" independently.
- **5.2 Pro:** Stuck on kill #109 loop. May need fresh-chat reset.
- **DeepSeek:** Good strategy. lcm > q proof. Responsible about retracting overclaims.
- **Gauss:** Three Lean proofs in first session. Submit structural lemmas for verification.

---

## WHAT I NEED FROM YOU

1. **Attack the n ≥ 5q/2 connected-component case.** The first atom is {12d, 15d, 20d}.
2. **Do NOT use killed approaches.** No operator monotonicity. No pointwise Δ comparison. No "adding elements helps."
3. **The top-window constraint is your main tool.** All elements > q/2 forces edge types to have bounded coprime ratios. Use this.
4. **The separator superadditivity is your reduction tool.** Only connected components matter. Prove it per-component.
5. **Check your constants.** If your bound gives margin = 0 at the worst case, that's not a proof.
6. **The {12d,15d,20d} family is the acid test.** If your argument works for this family, it likely generalizes. If it fails here, find out why.

---

## KILLS (110)
#110: Operator monotonicity under adjoining.
#109: Suffix-minimizer Δ at run-end extremizers.
#108: u_T target lemma.
1-107: All previous.

## STATUS: 98%

Seven theorems proved across two days. Four machine-verified in Lean. The frontier is a single graph-theoretic atom: connected components of size ≥ 3 in the top window with n ≥ 5q/2. The threshold 5q/2 is sharp (Codex B). The first genuine atom is {12d, 15d, 20d}.

**EP-488: October 5, 1960 → April 13, 2026. One atom remains.**
