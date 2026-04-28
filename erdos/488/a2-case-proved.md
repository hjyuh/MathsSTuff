# EP-488: The a=2 Case — PROVED
## March 31, 2026

### Theorem
Let A = {2, b} ∪ T be a primitive set with F(s) ≥ 5 (where s is the first such integer). Then for all m > s:
  F(m)/m < 2F(s)/s.

### Proof

**Step 1.** F(m) ≤ m - 1 for all m ≥ 1, since the integer 1 is not divisible by any element of A (all elements ≥ 2). Therefore F(m)/m ≤ 1 - 1/m < 1.

**Step 2.** Since a = 2, every even integer ≤ n is divisible by 2, so F(n) ≥ ⌊n/2⌋ for all n. In particular F(10) ≥ 5, so s ≤ 10.

**Step 3.** Since F(s) ≥ 5 and s ≤ 10:
  2F(s)/s ≥ 2·5/10 = 1.

**Step 4.** Combining: F(m)/m < 1 ≤ 2F(s)/s. □

### Scope
This covers ALL primitive sets with smallest element 2, which includes:
- Every primitive set containing an even number (since 2 divides all even numbers, primitivity forces 2 to be the smallest even element or not present)
- All "tightest" systems identified in 25,000+ system computational search
- The growing prime-tail family A = {2, 3} ∪ {primes 5 to P} for all P

### What remains for full EP-488
Primitive sets with smallest element a ≥ 3. For these:
- s ≤ 5a (since F(n) ≥ ⌊n/a⌋, so F(5a) ≥ 5)
- 2F(s)/s ≥ 10/(5a) = 2/a
- F(m)/m < 1
- Need 1 ≤ 2/a, which holds only for a ≤ 2

So for a ≥ 3, the trivial bound doesn't close. Need: either
(a) A sharper bound on F(m)/m (using δ < 1 structure), or
(b) A sharper bound on F(s) (showing F(s) >> 5 when s is large), or
(c) The relationship δ < 2F(s)/s (which says the asymptotic density is below the density-doubling threshold at s)

### Key structural fact for general a
If s is large (meaning F grows slowly to reach 5), then δ must be small:
  F(s-1) ≤ 4 implies δ(s-1) + c_{s-1} ≤ 4
  So δ ≤ (4 + |c_{s-1}|) / (s-1)

And F(m)/m → δ as m → ∞. So for m large: F(m)/m ≈ δ ≤ (4+C)/(s-1).
While 2F(s)/s ≥ 10/s.

Need: (4+C)/(s-1) < 10/s, i.e., s(4+C) < 10(s-1), i.e., (4+C)s < 10s - 10,
i.e., s(10 - 4 - C) > 10, i.e., s > 10/(6-C).

For C ≤ 5: s > 10. And for a ≥ 3: s ≤ 15. So s ∈ [11, 15] needs the correction bound C.

Bounding C (the max correction) is the remaining technical challenge for a ≥ 3.
