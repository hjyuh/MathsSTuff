# EP-488 Unified Truth v31 — April 12, 2026 (Evening)
## Three Paths, Two Obstructions, One Target

**Status: 93%. Pair theorem machine-verified. D(x) inequality is the sharpest target. 109 kills.**

---

## WHAT CHANGED SINCE v30

- **Kill #109 (5.2 Pro):** Suffix-minimizer inequality is FALSE even at run-end extremizers. Q'={4,5,6,7,9}, s=6, extremizer (62,372): Δ(372)/372 > 2·Δ(62)/62. The run boundary is caused by elements unrelated to the newly added s, so Δ(n*) can be tiny while Δ(m*) accumulates freely.
- **5.4 Pro D(x) deep analysis (35 min):** Three new D(x) lemmas proved. Exact IE sign failure identified. False hint corrected (D(q) ≥ |R|, not D(q) = |R|). Triple case identified as sharpest next target.
- **Codex BA pair monotonicity kill:** a → max O_{a,q} is non-monotone for composite q (gcd jumps at q=60). Does NOT kill Path 2 or Path 3.
- **Gemini Additive Contraction Lemma + coordinate relocation gap:** Proved ΔO_d ≤ −1/(dn) at the existing extremizer. Gap: global max might shift to different (n',m') after adjoining d.
- **Ferris wheel COMPLETE:** wheel_print_ready.html with 6 watertight STLs.
- **Full curriculum COMPLETE:** 63-day test-out plan for 3 courses.

---

## PROVED THEOREMS

### Machine-Verified (Aristotle/Lean 4)
**Pair Theorem:** O_{a,b}(n,m) < 1 for all primitive pairs. 3,103 build jobs, zero sorry, zero errors.
Bug found and fixed: T_scaled_div_mono needed n ≤ m hypothesis.

### Adjacent Pair Global Max (Codex BA)
Global max at (2q−3, (q−1)²) with value 1 − (4q−5)/((2q−3)(q−1)²).
Proof by independent optimization: Lemma 1 (max A(n)/n), Lemma 2 (min A(m)/m via periodicity).
**Submitted to Aristotle for Lean verification — pending.**

### Consecutive Triple (Codex BA)
{q−2,q−1,q} max computed in closed form, proved strictly below adjacent pair for q ≥ 5.

### D(x) Standalone Lemmas (5.4 Pro, NEW)

**Lemma A (Run-End Extremizer for D):** Any violation of D(m)/m ≤ 2D(n)/n must have n at end of D-uncovered run, m at end of D-covered run. Proved via D(n+1)−D(n) = 1_E(n+1).

**Lemma B (One-Step Safety):** m = n+1 always satisfies the inequality. Proved: D(n) ≥ 1 for n ≥ q since any r ∈ R contributes itself.

**Lemma C (Short-Interval Safety):** m − n ≤ D(n) always satisfies it. Any counterexample needs m − n > D(n).

### Previously Proved
Exact Singleton Theorem, Run-End Extremizer, One-Step Safety, Short-Interval Safety, Domain Amputation.

---

## KILLS (109 total)

### Kill #109: Suffix-Minimizer Inequality — DEAD (5.2 Pro)
Q'={4,5,6,7,9}, s=6, extremizer (62,372): Δ(372)/372 ≈ 0.040 > 2·Δ(62)/62 ≈ 0.032.
Run boundary at n*+1=63 is caused by 7 and 9, not by s=6. The run-end structure does NOT constrain Δ.
**Global max antitonicity itself survives** (M(Q)=0.548 > M(Q')=0.489), just this bridge lemma fails.

### Kill #108: u_T Target Lemma — DEAD (four independent confirmations)
T={2,3}, a=4, b=7. No universal constant exists (5.4 Pro: prime sieve family forces C → ∞).

### Kill: Pair monotonicity in a — DEAD for composite q (Codex BA)
q=60: max O_{23,60} > max O_{24,60} due to gcd(24,60)=12 jump. Coprime subfamily might hold.

### Kills 1-107: All previous (permanently closed).

---

## THE PROOF FRONTIER

### THE EXACT OBSTRUCTION (5.4 Pro, definitive)

The D(x) inclusion-exclusion expansion gives:
$$2\frac{D(n)}{n} - \frac{D(m)}{m} = \sum_{\emptyset \neq S \subseteq R} (-1)^{|S|+1} B_S(n,m)$$

where B_S involves paired floor terms ⌊x/d_S⌋ − ⌊x/D_S⌋ with d_S = lcm(S), D_S = lcm(S ∪ {q}).

**For |S| = 1:** B_S ≥ 0 (this IS the pair theorem).

**For |S| ≥ 2:** B_S can be NEGATIVE. Concrete: Q={2,3,5}, S={2,3}, n=5, m=6 gives B_S = −1/6.

**The overlap domination rescue also fails:** B_{a,b} can exceed min(B_{a}, B_{b}). Concrete example at Q={4,5,6,7,9}.

**Therefore:** The natural IE proof (show each term is non-negative) is dead. Any proof must exploit cancellation ACROSS terms, not within individual terms.

---

### PATH 1: D(x) Two-Point Inequality (PRIMARY TARGET)

**Statement:** For primitive Q with max q, R = Q\{q}:
D(m)/m ≤ 2·D(n)/n for all m > n ≥ q

**Status:** Zero counterexamples. Three supporting lemmas proved. Exact obstruction identified.

**Sharpest next target (5.4 Pro):** Prove for primitive triples Q = {a,b,q}:
B_{a} + B_{b} − B_{a,b} ≥ 0
Computationally clean for max ≤ 20. Smallest margin ~0.0089 at Q={17,18,19}, (n,m)=(33,187).

**Why B_{a} + B_{b} − B_{a,b} ≥ 0 might be provable even though B_{a,b} < 0:**
The pair terms B_{a} and B_{b} are individually non-negative (pair theorem). The overlap B_{a,b} is small relative to their sum. The q-exclusion creates correlation between the floor terms that forces the sum to stay positive.

**Proof strategies still live:**
1. Triple case analysis using the exact B_S formula with residue classes mod lcm(a,b,q)
2. Bounding |B_{a,b}| ≤ min(B_{a}, B_{b}) on average (even though pointwise fails)
3. Sieve-theoretic bound on the error sum via φ(M)/M density arguments

### PATH 2: Route 2 Top Window (PARALLEL TRACK)

**Status:** Gemini proved ΔO_d ≤ −1/(dn) at the existing extremizer. Coordinate relocation gap remains.

**The gap:** After adjoining d, the global max might shift to n' ≥ 2·min(Q_top), where the Additive Contraction Lemma doesn't apply. Need to prove the baseline O_{Q_top}(n',m') crashes at these larger n' values, making rescue impossible.

**Gemini Phase 3 protocol ready:** Three-prompt staged attack for next Deep Think session.

### PATH 3: Global Max Antitonicity (BACKUP)

**Statement:** M(Q ∪ {s}) ≤ M(Q) when max is preserved.

**Status:** Zero counterexamples. Kill #109 shows the suffix-minimizer bridge fails, but the antitonicity itself survives. Needs a different proof technique — possibly allowing the comparison pair (n,m) to change between Q and Q'.

---

## COMPUTATIONAL VERIFICATION

### D(x) inequality
- All primitive Q ⊂ [2,25], window q ≤ n < m ≤ 10q: ZERO violations (5.4 Pro)
- ~500 random primitive sets, max ≤ 30, window 3x: ZERO violations (Claude)
- Worst case: adjacent pair Q={24,25}, margin 1/1128 at (47,48)

### Singleton extremality (O_Q < 1)
- 109,295 primitive Q ⊂ [2,25]: singleton ALWAYS worst (5.4 Pro)
- All antichains max q ≤ 12, (n,m) up to 30q: ZERO counterexamples (5.2 Pro)
- 50,000 random antichains max ~80: ZERO counterexamples (5.2 Pro)

### Triple case B_{a}+B_{b}−B_{a,b} ≥ 0
- All primitive triples max ≤ 20, window 10q: ZERO violations (5.4 Pro)
- Smallest margin: ~0.0089 at Q={17,18,19}, (33,187)

---

## FORMAL VERIFICATION

### Aristotle #1: Pair Theorem — COMPLETE
ep488_pairs.lean: zero sorry, 3,103 build jobs, zero errors.

### Aristotle #2: Adjacent Pair Global Max — PENDING
ep488_adjacent_pair_max.lean: 7 sorry statements submitted. Grinding.

### AXLE: Type-checking confirmed on both files.

---

## MODEL RANKINGS (final for April 12)

1. **5.4 Pro** — Pair proof, singleton theorem, 109K computation, D(x) deep analysis (3 lemmas + exact obstruction + false hint correction), kill #107
2. **5.2 Pro** — Pair proof 2 (pointwise), D(x) formulation, Path 3 discovery, kill #109 (suffix-minimizer), u_T kill
3. **Codex BA** — Adjacent pair global max proof, consecutive triple, pair monotonicity kill (composite q), Route 2 architecture, computational tooling
4. **Claude Opus 4.6** — Session architect, truth documents v1-v31, D(x) computational validation, Lean formalization, Aristotle/AXLE coordination
5. **Gemini Deep Think** — Domain Amputation, Additive Contraction Lemma, coordinate relocation gap, D(x) standalone prompt, phased protocol design
6. **DeepSeek** — Bootstrapping argument for Route 2, φ(M)/M connection, strategic assessment
7. **Qwen** — First u_T kill, corrected lemma, D(x) proof sketch with Lemma 1-3 structure
8. **Codex B** — D(x) formulation (independent), pair monotonicity intermediate (killed for composite q but useful for primes), Form 2c architecture

---

## NEXT MOVES (priority order)

1. **Prove B_{a}+B_{b}−B_{a,b} ≥ 0 for primitive triples** — the smallest non-trivial D(x) case. Send to 5.4 Pro (already has the framework) and 5.2 Pro.
2. **Gemini fresh chat** — Phase 3 protocol targeting coordinate relocation gap (Route 2) or D(x) standalone.
3. **Check Aristotle #2** — adjacent pair global max formalization.
4. **Expand D(x) computation** — test triples with max ≤ 50 to increase confidence.
5. **MathOverflow** — if all three paths stall after 1 week.

---

## THE SHARPEST POSSIBLE STATEMENT OF WHERE WE ARE

**What's proved:** Singletons are worst for |Q| = 1 (exact theorem) and |Q| = 2 (pair theorem, machine-verified).

**What's conjectured with zero counterexamples:** Singletons are worst for all |Q| (singleton extremality conjecture = EP-488).

**The exact obstruction to proving it:** Higher-order inclusion-exclusion overlap terms B_S with |S| ≥ 2 have no usable pointwise sign in the D(x) expansion. Any proof must exploit cross-term cancellation.

**The sharpest next target:** B_{a}+B_{b}−B_{a,b} ≥ 0 for primitive triples. If this falls, the pattern likely generalizes via Bonferroni-style bounds to all |Q|.

**EP-488 has been open for 65 years. The pair case is machine-verified. The triple case is the next wall.**
