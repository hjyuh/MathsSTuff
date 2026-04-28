# EP-488: Finite Verification of (RQ_q) for a ∈ [13, 210]
## Context Package for GPT-5.4 xhigh (Codex)

## The Problem
Erdős Problem 488: For primitive set A (no element divides another), is F(m)/m < 2F(n)/n for all m > n ≥ max(A)?

We've reduced EP-488 for one-anchor families A = {a} ∪ {2a+1,...,2a+t} (a prime, k=2) to proving a single rowwise inequality in the "pre-peak" range.

## What You Need to Verify

### The Quota-Capacity Identity (PROVED)
For a window I_x = (x, x+4a], define:
- R_q(x) = qB ∩ I_x where B = {2a+1,...,2a+t}
- W(x) = |⋃_q R_q(x)| (window count)
- E_q(x) = |B ∩ (x/q, (x+4a)/(q+1)]| (two-hit band at level q)
- C_q(x) = |R_q(x) ∩ ⋃_{r<q} R_r(x)| (row-q collisions with earlier rows)

EXACT identity: W(x) - t = E(x) - C(x) where E = Σ E_q, C = Σ C_q.

### The Rowwise Quota Bound (RQ_q) — TARGET
For every active q ≥ 2 in the pre-peak range:
C_q(x) ≤ E_{q-1}(x)

If true for all x in pre-peak range: C ≤ E → W ≥ t → First Plateau Lemma → EP-488.

### What's Already Verified
- (RQ_q) holds for all wide families with prime a ≤ 61, k ∈ {2,3,4} (exact pre-peak scan)
- For a ≥ 211: a continuous coefficient analysis proves it analytically (the gap κ_E - κ_C scales as ~0.019a, absorbing floor effects)

### What's Missing
Finite verification for primes a ∈ {67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211} — roughly 29 primes.

For each such prime a, and each wide t (meaning t > 2√a), verify:
C_q(x) ≤ E_{q-1}(x) for ALL active q ≥ 2 and ALL x with 0 ≤ x ≤ m* - 4a,
where m* is the earliest maximizer of G(x) = F(x)/x on [2a+t, ∞).

### How to Compute

For each (a, t) with a prime, k=2, t > 2√a (wide regime):

1. Compute F(x) = floor(x/a) + |{n ≤ x : ∃b ∈ B, b|n}| for x from M to some large bound
2. Find m* = argmax G(x) on [M, large bound]
3. For each x from 0 to m* - 4a:
   a. For each active q (where qB ∩ I_x is nonempty):
      - Compute R_q(x) = {qb : b ∈ B, x < qb ≤ x+4a}
      - Compute C_q(x) = |R_q(x) ∩ ⋃_{r<q} R_r(x)|
      - Compute E_{q-1}(x) = |B ∩ (x/(q-1), (x+4a)/q]|
      - Check C_q(x) ≤ E_{q-1}(x)
4. Report any failure

### Optimization
You don't need to check every x. The collision counts change only at multiples of elements of B (where R_q gains/loses elements). So you can enumerate the "event points" and check at each one.

Also: m* is typically ≤ 15a for k=2 wide families. So the pre-peak range is at most ~15a integers.

### Expected Output
For each prime a in [67, 211]:
- Number of wide t values checked
- Total (a, t, x, q) quadruples verified
- Any failures found
- Worst margin (smallest E_{q-1} - C_q)

Write a Python script, run it, report results.

Extended thinking ON. Write efficient code and verify all cases.
