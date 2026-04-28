# EP-488: Chojecki Reduction Version KILLED for a ≥ 3
## March 31, 2026 — GPT-5.4

### The counterexample

For any a ≥ 3, define:
  b = 5a + 1
  T = {t ∈ Z : 5a+1 < t ≤ 10a+1, a ∤ t}
  A = {a, b} ∪ T

This is primitive (all elements of {b} ∪ T are in (5a, 10a+1], so no two divide each other, and none is divisible by a).

Key computation:
  s = 5a (first integer with F(s) ≥ 5, since only multiples of a contribute before tail activates)
  F(s) = 5
  2F(s)/s = 10/(5a) = 2/a

  m = 10a+1
  F(m) = 5 + (5a+1) = 5a + 6 (every integer in [5a+1, 10a+1] is covered by the tail)
  F(m)/m = (5a+6)/(10a+1) > 2/a for a ≥ 3

Check: 5a² - 14a - 2 > 0 for a ≥ 3. ✓

Concrete example: a=3, A = {3, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31}.
s=15, F(15)=5, m=31, F(31)=21. F(31)/31 = 21/31 ≈ 0.677 > 2/3 = 2F(15)/15.

### What this kills
The statement "F(m)/m < 2F(s)/s for all m > s" where s = first integer with F(s) ≥ 5.
This is the Chojecki reduction version. It is FALSE for a ≥ 3.

### What survives
- Original EP-488: "F(m)/m < 2F(n)/n for all m > n ≥ max(A)" — UNAFFECTED
  (In the counterexample, s = 5a < max(A) = 10a+1, so s is outside the valid range)
- The a=2 proof — UNAFFECTED (doesn't use Chojecki s)
- Bridge Lemma, kernel identity, anti-conspiracy — VALID (apply at n ≥ max(A))

### The lesson
The Chojecki s is the wrong reference point for a ≥ 3 because:
- s can occur BEFORE max(A), when only multiples of a have been counted
- After s, tail elements "turn on" and flood an interval, spiking F(m)/m
- The original EP-488 avoids this by requiring n ≥ max(A)

### Approach #18 (KILLED)
"Prove F(m)/m < 2F(s)/s for Chojecki s with a ≥ 3" — DISPROVED by explicit counterexample family.
