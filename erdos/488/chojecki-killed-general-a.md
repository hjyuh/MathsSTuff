# EP-488: Chojecki Reduction Version KILLED for a ≥ 3
## March 31, 2026 — GPT-5.4

### Counterexample (Approach #18)

For a ≥ 3, define:
  b = 5a + 1
  T = {t ∈ Z : 5a+1 < t ≤ 10a+1, a ∤ t}
  A = {a, b} ∪ T

This is primitive. s = 5a, F(s) = 5, 2F(s)/s = 2/a.
At m = 10a+1: F(m) = 5a+6, F(m)/m = (5a+6)/(10a+1) > 2/a for a ≥ 3.

Concrete: a=3, A={3,16,17,19,20,22,23,25,26,28,29,31}, s=15, F(15)=5, m=31, F(31)=21.
F(31)/31 = 21/31 ≈ 0.677 > 2/3 = 2F(15)/15.

### What this kills
The claim F(m)/m < 2F(s)/s for all m > s (Chojecki reduction version) is FALSE for a ≥ 3.

### What survives
- EP-488 itself (n ≥ max(A)) — because s = 5a < max(A) = 10a+1 in this family
- The a=2 proof — uses actual EP-488 statement, not Chojecki s
- The reduction chain — but ONLY when applied in the n ≥ max(A) regime

### Key lesson
The Chojecki s can be much smaller than max(A). When s < max(A), the tail elements
haven't "appeared" yet at s, so 2F(s)/s = 2/a is artificially small. The real EP-488
requires n ≥ max(A), where ALL elements are active.

### Impact on paper
The paper's Theorem B (reduction framework) needs correction: the reduction to
sieve oscillation only applies in the n ≥ max(A) regime, not the Chojecki s regime.
The a=2 proof (Theorem A) is unaffected.

### Killed approaches: now 18 total
18. Chojecki reduction for general a (GPT-5.4: s < max(A) counterexample family)
