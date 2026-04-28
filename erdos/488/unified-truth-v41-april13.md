# EP-488 Unified Truth v41 — April 13, 2026
## Eight Theorems. Four Lean Proofs. Four Atoms Closed. Classification Is the Last Wall.

**Status: 98.5%. Four specific atomic families closed by compression (5.4 Pro). The remaining gap is the general classification/finiteness theorem for connected top-window components.**

---

## YOUR REQUIRED OUTPUT FORMAT

**You MUST include ALL of the following in your response:**

1. **Percentage complete:** Give your honest estimate of how close EP-488 is to fully proved. Justify the number.
2. **Why we're not finished:** State precisely what mathematical gap remains and why existing tools don't close it.
3. **What you attempted:** Describe at least 3 proof strategies you tried in depth. For each: what the idea was, how far it got, and exactly where/why it broke.
4. **What you recommend:** Propose the most promising next step with evidence for why it should work.
5. **If you believe you've closed the gap:** Give an explicit proof. Check your constants at the worst case. Do not declare QED without numerical verification.

---

## COMPLETE PROOF CHAIN (all proved)

1. **Singletons:** max O_{q} < 1. Exact closed form.
2. **Pairs:** Machine-verified (Aristotle, zero sorry).
3. **Top Window:** Any Q with element ≤ q/2 → O_Q < 1. Only Q ⊂ (q/2, q] competes.
4. **Triple case (|R|=2):** All sub-regimes closed (lcm>n, inert, active (2,3), active u≥3).
5. **n < 2q, all |R|:** Block decomposition — components ≤ 2 → pair/triple (Codex B).
6. **2q ≤ n < 9q/4, |R| ≥ 3:** Only {6c,8c,9c}-type connected triples → PROVED by compression (Codex B).
7. **D-separator superadditivity:** Counterexamples live in single connected components. Machine-verified (Gauss).
8. **Components ≤ 2, any n:** Pair/triple theorems apply.
9. **Four specific atomic families closed (5.4 Pro, compression + finite verification):**
   - {6c, 8c, 9c}: 0 violations in full compressed box
   - {8c, 9c, 12c}: 0 violations / 2.2M tuples / worst margin 0.15
   - {9c, 12c, 16c}: 0 violations / 1.2M tuples / worst margin 0.148
   - {16d, 18d, 24d, 27d}: 0 violations / 10M tuples / worst margin 0.102
   - {12d, 15d, 20d}: 0 violations / worst margin 0.093

### Machine-verified (Lean 4):
| # | Theorem | System |
|---|---------|--------|
| 1 | Pair theorem | Aristotle |
| 2 | Coprime core (2,3) | Gauss |
| 3 | Top Window LCM | Gauss |
| 4 | Separator superadditivity | Gauss |

---

## THE REMAINING GAP

### What is NOT proved:
The D(x) inequality D(m)/m ≤ 2D(n)/n for GENERAL connected components of size ≥ 3 in the top window with n ≥ 2q.

### What IS proved:
Five specific families closed by compression + finite verification. But we need EITHER:
- (a) A proof that finitely many families exist + verification of each, OR
- (b) A uniform argument covering all families at once

### Why this is hard:
- Odd-order IE terms (|S| = 3, 5, ...) with lcm(S) ∈ (n, m] hurt the inequality
- No termwise IE domination (each term lacks a usable sign)
- Leaf-pruning via separator is blocked (adjoining-monotonicity killed)
- Density domination has correct direction but constants don't close with crude bounds

### The compression method (what WORKS, family by family):
Factor out gcd c from R = cB. D_Q(x) = D̃(⌊x/c⌋). Top window forces q/c ∈ bounded interval. This makes M bounded, turning each family into a finite box. Exhaustive check closes it.

### What's needed to make this a general proof:
**The Template Finiteness Theorem:** Every connected top-window component with n ≥ 2q belongs to one of finitely many scaled templates {c · b₁, c · b₂, ..., c · bₖ} where the bᵢ come from a finite enumerable list.

If this is proved, then compression + finite verification closes EVERY family, and EP-488 is done.

---

## THE STRUCTURAL CONSTRAINTS ON TEMPLATES

### Edge classification in the top window:
For r ~ s with r, s ∈ (q/2, q] and lcm(r,s) ≤ n:
- Write r = L/a, s = L/b with a, b coprime, a ≠ b, a,b ≥ 2
- Since r, s > q/2 and L ≤ n: a, b < 2n/q
- For n/q bounded (e.g., n ≤ Kq), finitely many (a,b) types

### Connected component structure:
- All elements in (q/2, q] → ratio max/min < 2
- Each element r = c · bᵢ where c = gcd(R) and bᵢ are coprime-ish
- The bᵢ must all lie in a ratio-2 window
- Connected graph on the bᵢ via the lcm condition

### Key question: Is n/q bounded at the extremizer?
If the worst-case (n,m) for D(x) always has n = O(q), then:
- Edge types (a,b) are bounded
- Component size is bounded
- Template list is finite
This would close EP-488.

### Evidence that n/q is bounded:
- Singleton extremizer: n = 2q−1 (ratio ≈ 2)
- Pair extremizer: n = 2q−3 (ratio ≈ 2)
- All computational worst cases: n < 3q
- Run-end extremizer lemma: violations need n at end of uncovered run, which limits how far n can be from q

---

## FIVE METHODS TRIED AND THEIR STATUS

### Method 1: Direct IE termwise domination — FAILS
Each B_S term lacks a usable sign for |S| ≥ 2. Odd-order terms with lcm ∈ (n,m] are harmful. No budget allocation works termwise.

### Method 2: Separator + leaf pruning — PARTIALLY BLOCKED
Separator superadditivity reduces to components (PROVED). But leaf pruning needs Δ_{r,s} ≥ Δ_{s}, which is adjoining-monotonicity (KILLED #110).

### Method 3: Compression + finite verification — WORKS FAMILY BY FAMILY
Reduces each scaled family to a finite box. Successfully closed 5 families (~18M tuples total). But needs finiteness of the family list to become a general proof.

### Method 4: Density domination — DIRECTION RIGHT, CONSTANTS FAIL
Pair terms give O(|R|/q) budget. Harmful terms give O(1/m) each. For large q the budget wins, but crude bounds don't close for small q or specific phase alignments.

### Method 5: n-range extension (Codex B) — PROVED PARTIAL RANGES
n < 2q: components ≤ 2, proved. n < 9q/4: components ≤ 3, {6c,8c,9c} proved. Extends the safe range but doesn't close all n.

---

## KILLED APPROACHES (do NOT use)

**Kill #110:** Operator monotonicity under adjoining. DEAD.
**Kill #109:** Suffix-minimizer Δ at run-end extremizers. DEAD.
**Kill #108:** u_T target lemma. DEAD.
**Do NOT argue "adding elements helps."**
**Do NOT argue "components ≤ 3 are handled by triple case."** |R|=3 is |Q|=4, NOT the proved triple case.

---

## COMPUTATIONAL EVIDENCE

- 1,400 random top-window sets (q up to 500): zero violations
- 5 specific families: ~18M tuples, zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst case across all tests: ratio ≈ 0.973 (Q={55,56,57,59})

---

## WHAT I NEED FROM YOU

1. **Try to prove the Template Finiteness Theorem.** If every connected top-window component belongs to a finite list, compression closes EP-488.
2. **OR try to prove a uniform density argument.** If pair budget always dominates harmful terms regardless of family, EP-488 closes without classification.
3. **OR try to prove n/q is bounded at the extremizer.** If the worst-case n satisfies n ≤ Kq for some absolute K, then finitely many edge types exist and the template list is finite.
4. **The {6c,8c,9c} and {8c,9c,12c} families are your acid tests.** Any argument must work for these. Check constants there first.
5. **Do NOT use killed approaches.**

---

## KILLS (110)
#110: Operator monotonicity under adjoining.
#109: Suffix-minimizer Δ at run-end extremizers.
#108: u_T target lemma.
1-107: All previous.

---

## STATUS: 98.5%

Eight theorems proved. Four machine-verified in Lean. Five atomic families closed by compression. The gap is the classification/finiteness theorem for connected top-window components. The compression method works per-family; the question is whether the family list is finite and enumerable.

**EP-488: October 5, 1960 → April 13, 2026. The last wall: prove the template list is finite.**
