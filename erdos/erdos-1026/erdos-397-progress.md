# Erdős 397 — Progress Log
## Updated: March 10, 2026

### Problem
Are there only finitely many solutions to ∏ C(2mᵢ, mᵢ) = ∏ C(2nⱼ, nⱼ) with mᵢ, nⱼ distinct?
Answer: NO (disproved). Infinite family of counterexamples exists.

### Status: PIECE 1 VERIFIED, PIECE 2 IN PROGRESS

---

### Piece 1: The Algebraic Identity ✅ VERIFIED BY AXLE
centralBinom(a) * centralBinom(2a+2) * centralBinom(8a²+8a+1) = 
centralBinom(a+1) * centralBinom(2a) * centralBinom(8a²+8a+2)

- Aristotle project: fc98a78c (PROVED)
- Axle verification: CLEAN (0 errors, 7 seconds, only unused var warning)
- Proof strategy: expand centralBinom to factorials, cast to ℚ, field_simp + ring

### Piece 2: The Structural Argument ⏳ IN PROGRESS
"Given the identity, prove the solution set is infinite"
- Needs: construct pairs (M(a), N(a)), show disjoint, show products equal, show injective
- Aristotle project: eb8dc4e7 (SUBMITTED, waiting)
- Previous attempt (00fdf6b5): FAILED — centralBinom API issues with Finset products

### Piece 3: Not needed separately
The infinity argument is part of Piece 2 (the map a ↦ (M(a), N(a)) is injective → infinite)

---

### Timeline
- March 9 night: First full attempt → Aristotle errored
- March 10 morning (vanished response): Decomposed into sorry-driven pieces
  - Verified identity computationally for a=2 (both sides = 141,247,882,363,789,870,668,737,496,158,400)
  - Submitted Job 1 (structural) and Job 2 (identity) in parallel
  - Job 1 failed (centralBinom API), Job 2 succeeded
- March 10 evening: Verified identity with Axle ✅, resubmitted structural piece

### Next Steps
- Check eb8dc4e7 when ready
- If structural piece succeeds → combine with identity proof → verify full theorem with Axle
- If structural piece fails → isolate the Finset product calculation as another sub-lemma
- Final target: complete proof of erdos_397 matching the Formal Conjectures statement
