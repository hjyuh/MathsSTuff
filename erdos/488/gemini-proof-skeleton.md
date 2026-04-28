# EP-488: Proof Skeleton for the Actual-Slack Ancestor Lemma
## For Gemini — April 7, 2026 — Temperature 0.5

---

## YOUR TASK

Build a proof skeleton for the following lemma. Not a complete proof — a structured argument with clear steps, where each step is either proved or marked as "needs verification." I want to see the logical architecture, not every detail.

## THE LEMMA

For every finite primitive set A, every m > n with M ≤ n < m ≤ 10M (where M = max(A)), and every compact layer j (a_j ∈ (M/2, M]) whose layer contributes positive excess:

  n · L_j(⌊m/a_j⌋) - 2m · L_j(⌊n/a_j⌋) > 0

there exists a 3-ancestor layer i < j such that:

  2m · L_i(⌊n/a_i⌋) - n · L_i(⌊m/a_i⌋) ≥ n · L_j(⌊m/a_j⌋) - 2m · L_j(⌊n/a_j⌋)

(Parent actual slack ≥ child actual excess.)

## DEFINITIONS

- A is primitive: no element divides another.
- L_j(y) = |{u ≤ y : b ∤ u for all b ∈ B_j}| where B_j = {a_k/gcd(a_k, a_j) : k < j, quotient > 1}.
- "3-ancestor": element a_i ∈ A with a_i/gcd(a_i, a_j) = 3. This means a_i = 3g, a_j = hg where g = gcd(a_i, a_j) and gcd(h, 3) = 1.
- "Compact layer": a_j ∈ (M/2, M], so ⌊x/a_j⌋ ≤ 20 for x ≤ 10M.

## KNOWN FACTS TO USE

### Fact 1: Buchstab Identity
L_B(x) = L_{B\{p}}(x) - L_{B\{p}}(x/p)

Removing prime p from sieve set B: the count avoiding B equals the count avoiding B\{p}, minus that count evaluated at x/p.

### Fact 2: Quotient Transport Lemma (proved)
If a_i/gcd(a_i, a_j) = 3, then for any k < i:
  q_{k,j} | 3 · q_{k,i}
Child obstructions are bounded by 3× parent obstructions.

### Fact 3: Bad child properties (proved)
- The child's active kernel K always contains {2, 3}
- L_K(s) = 1 in every bad case (only integer 1 survives up to s)
- s < h_min(K) where h_min is the smallest integer ≥ 2 coprime to all primes in K
- L_K(t) ≤ 8 (bounded by the 29-kernel classification)
- The child excess = n · L_K(t) - 2m is small (since L_K(s) = 1)

### Fact 4: Parent scale
The parent a_i = 3g is smaller than the child a_j = hg (since h ≥ 5).
So the parent's floor values are larger:
  ⌊n/a_i⌋ ≈ (h/3) · s ≥ (5/3) · s
  ⌊m/a_i⌋ ≈ (h/3) · t ≥ (5/3) · t

### Fact 5: Computational verification
6,657 instances checked, zero failures. Tightest margin: parent slack 552 vs child excess 3. The lemma is true with enormous room to spare.

## THE PROOF SKELETON I WANT

Structure the proof as follows:

**Step 1: Establish the 3-ancestor exists.**
Why must there be an a_i ∈ A with a_i/gcd(a_i, a_j) = 3? Under what conditions on a_j does such an element exist in A? (Hint: if 3 is in the child's active kernel, something must have put it there.)

**Step 2: Bound the child's excess from above.**
The child has L_K(s) = 1 and L_K(t) ≤ 8. So child excess = n · L_K(t) - 2m ≤ 8n - 2m. Since m > n, this is at most 6n. Can you get a tighter bound using the specific bad signatures?

**Step 3: Bound the parent's slack from below.**
The parent evaluates at s' ≈ (h/3)(s+1) and t' ≈ (h/3)t with h ≥ 5.
So s' ≥ 7 and t' ≥ 11 (in the tightest case).
At these depths, L_{B_i}(s') is large (many integers survive a sieve with fewer/larger obstructions).
Use the Buchstab identity to relate L_{B_i} to L_{B_j}:
  Since B_j's obstructions come from B_i's via quotient transport (q_{k,j} | 3·q_{k,i}), the parent has RELATED but LESS HARMFUL obstructions at a DEEPER evaluation point.

**Step 4: Compare parent slack to child excess.**
Show that the parent's evaluation depth (s' ≥ 7 vs s ≤ 4) and reduced obstruction severity combine to give slack >> excess.

**Step 5: Handle all 29 bad kernels.**
Either give a uniform argument that works for all, or show the argument reduces to a finite check that's already been verified.

## ADDITIONAL GUIDANCE

The key insight to build on: the child is maximally weak (L_K(s) = 1, meaning only integer 1 survives). This happens because the child has many small prime obstructions ({2,3,...}) crammed into a short evaluation window (s ≤ 4). The parent, by contrast, evaluates deeper (s' ≥ 7) with one fewer small prime obstruction (no 3). Going deeper with fewer obstructions is a double advantage — each factor individually helps, and together they're overwhelming.

The Buchstab identity L_B(x) = L_{B\{3}}(x) - L_{B\{3}}(x/3) connects child and parent directly: the child's count equals the parent's count minus a correction term evaluated at x/3. If the correction term is small relative to the parent's count at the relevant scale, the parent dominates.

## OUTPUT FORMAT

For each step:
- State the claim precisely
- Give the proof or proof sketch
- If a step requires a sub-lemma you can't prove, state the sub-lemma precisely and mark it [NEEDS PROOF]
- If a step reduces to a finite computation, say so and mark it [FINITE CHECK]

The goal is a complete logical skeleton where every gap is precisely identified and either filled or flagged.
