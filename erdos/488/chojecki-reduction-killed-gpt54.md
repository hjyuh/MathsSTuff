# EP-488: Chojecki Reduction Version DISPROVED for a ≥ 3
## March 31, 2026 — GPT-5.4

### The counterexample

For any a ≥ 3, define:
  b = 5a + 1
  T = {t ∈ Z : 5a+1 < t ≤ 10a+1, a ∤ t}
  A = {a, b} ∪ T

This is primitive (all elements of {b}∪T are in (5a, 10a+1], too close to divide each other).

s = 5a (first integer with F(s) ≥ 5, since only multiples of a contribute below 5a)
F(s) = 5, so 2F(s)/s = 2/a

m = 10a + 1:
F(10a+1) = 5a + 6 (all integers in [5a+1, 10a+1] counted by tail, plus 5 multiples of a)
F(m)/m = (5a+6)/(10a+1)

Check: (5a+6)/(10a+1) > 2/a iff 5a² - 14a - 2 > 0, which holds for all a ≥ 3. ✓

Concrete example (a=3):
  A = {3, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31}
  s = 15, F(15) = 5, 2F(s)/s = 2/3
  m = 31, F(31) = 21, F(m)/m = 21/31 ≈ 0.677 > 2/3

### What this kills
The claim "F(m)/m < 2F(s)/s for all m > s" where s is the first integer with F(s) ≥ 5.
This is the Chojecki reduction version used in the reduction chain.

### What this does NOT kill
The original EP-488: "F(m)/m < 2F(n)/n for all m > n ≥ max(A)".
In this family, s = 5a < 10a+1 = max(A), so the counterexample is outside the valid range.

### Implications
1. The a=2 proof (Theorem 1) is UNTOUCHED — uses original EP-488 statement
2. The reduction framework (Theorem 2) needs restating for original EP-488 range
3. The general-a case is HARDER than Chojecki reduction suggested
4. Cannot use "first s with F(s) ≥ 5" as the reference point for a ≥ 3
5. Must use n ≥ max(A) as stated in original problem

### Killed approaches: now 18
18. Chojecki reduction version for a ≥ 3 (GPT-5.4: tail-packing counterexample)
