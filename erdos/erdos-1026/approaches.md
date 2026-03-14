# Erdős Problem 1026 — Proof Approaches
## Brainstorming Document

**Goal:** Independently prove that for k² distinct positive reals summing to 1,
some monotone subsequence has sum ≥ 1/k.

---

## Approach 1: The Blowup Reduction (Most Elementary)

### Core idea
Turn the *weighted* problem into the *unweighted* Erdős-Szekeres theorem by
replacing each element with many copies, then take a limit.

### Step-by-step sketch

**Step 1 — Discretize.**
Given x₁, ..., x_{k²} with Σxᵢ = 1, pick a large integer N.
Replace each xᵢ with a block of Bᵢ = ⌊N²xᵢ²⌋ copies of values near xᵢ.
Within each block, arrange the values so no monotone subsequence exceeds
length ⌈Nxᵢ⌉. (This is possible by Erdős-Szekeres: Bᵢ ≈ N²xᵢ² elements
with no monotone run longer than Nxᵢ means we need Bᵢ ≤ (Nxᵢ)², which holds.)

**Step 2 — Apply classical Erdős-Szekeres.**
The total blown-up sequence has length Σ Bᵢ ≈ N² Σ xᵢ² elements.
By Erdős-Szekeres, it contains a monotone subsequence of length at least
√(Σ Bᵢ) ≈ N√(Σ xᵢ²).

**Step 3 — Translate back.**
A monotone subsequence of the blown-up sequence hits each block at most
⌈Nxᵢ⌉ times. Each hit "costs" ≈ xᵢ from the original sum. So the original
sum picked up by this subsequence is:
    S ≈ (length of subsequence) × (average xᵢ per hit)
More precisely, S satisfies NS + O(1) ≥ the blown-up monotone length.

**Step 4 — Take N → ∞.**
    (NS)² ≥ N² Σ xᵢ²  ⟹  S² ≥ Σ xᵢ²

**Step 5 — Apply Cauchy-Schwarz.**
    Σ xᵢ² ≥ (Σ xᵢ)² / k² = 1/k²
    ⟹  S ≥ 1/k.  ∎

### Formalization difficulty: MEDIUM-HARD
The limit argument (N → ∞) is the painful part in Lean. You need to
formalize "for all ε > 0, for sufficiently large N, ..." which requires
working with filters/tendsto in Mathlib. This is doable but tedious.

### Key lemmas needed
- Erdős-Szekeres theorem (might need to state ourselves or find in Mathlib)
- Cauchy-Schwarz for finite sums (Mathlib has this)
- Floor/ceiling arithmetic
- Basic limit machinery

---

## Approach 2: Weighted Seidenberg (Avoids Limits Entirely)

### Core idea
Adapt the Seidenberg (1959) proof of Erdős-Szekeres to work with sums
instead of lengths. Assign each element a "weighted increasing score"
and "weighted decreasing score," then use a packing argument.

### Step-by-step sketch

**Step 1 — Define weighted scores.**
For each element xᵢ in the sequence:
- Sᵢ = maximum sum of an increasing subsequence ending at xᵢ
- Tᵢ = maximum sum of a decreasing subsequence ending at xᵢ

Note: Sᵢ ≥ xᵢ and Tᵢ ≥ xᵢ (the singleton subsequence).

**Step 2 — Establish the key inequality.**
Claim: Sᵢ + Tᵢ - xᵢ is a "weight" associated with xᵢ, and these
weights don't overlap too much.

More precisely: the rectangles [Sᵢ - xᵢ, Sᵢ] × [Tᵢ - xᵢ, Tᵢ]
are pairwise disjoint.

**Why disjoint?** If i < j:
- If xᵢ < xⱼ (values increasing): then Sⱼ ≥ Sᵢ + xⱼ, so the
  S-intervals don't overlap.
- If xᵢ > xⱼ (values decreasing): then Tⱼ ≥ Tᵢ + xⱼ... wait,
  this needs to be Tᵢ ≥ Tⱼ + xᵢ or similar. Need to check direction.

**Step 3 — Area argument.**
All rectangles fit inside [0, max S] × [0, max T].
Each rectangle has area xᵢ². (Width xᵢ, height xᵢ.)
Total area: Σ xᵢ² ≤ (max S)(max T).

**Step 4 — Apply AM-GM or direct bound.**
    (max S)(max T) ≥ Σ xᵢ² ≥ 1/k²  (by Cauchy-Schwarz)
    ⟹  max(S, T) ≥ √(Σ xᵢ²) ≥ 1/k.

Actually, even simpler: max(S, T) ≥ √(max(S) · max(T)) ≥ √(Σ xᵢ²) ≥ 1/k.

### Formalization difficulty: MEDIUM
No limits! Purely combinatorial/algebraic. The disjointness of rectangles
is the key lemma. In Lean, this becomes a proof about Finsets and intervals.

### Key lemmas needed
- Rectangle disjointness (main technical lemma)
- Σ xᵢ² ≥ 1/k² (Cauchy-Schwarz for Finset sums)
- AM-GM or √(ab) ≤ max(a,b)

### Why this might be better for Lean
No limits, no ε-δ, no filters. Pure algebra + combinatorics. This is
exactly the kind of argument Lean/Mathlib handles well.

---

## Approach 3: Variance + Pigeonhole (Most Direct)

### Core idea
Forget Erdős-Szekeres entirely. Use the pigeonhole principle directly
on a partition of the sequence into monotone subsequences.

### Step-by-step sketch

**Step 1 — Partition into monotone subsequences.**
By Dilworth's theorem, any sequence of k² elements can be partitioned
into at most k increasing subsequences, OR at most k decreasing
subsequences. (Because the longest decreasing subsequence has length
at most k, or vice versa.)

Wait — this isn't quite right. We need Erdős-Szekeres to guarantee
that either there's an increasing subsequence of length k+1 or a
decreasing one of length k+1. From k² + 1 elements. We have k²
elements, so we get length k.

Actually: by Dilworth's theorem, if no increasing subsequence has
length > k, then the sequence can be partitioned into ≤ k decreasing
subsequences. Similarly the other direction.

**Step 2 — Pigeonhole on sums.**
If the sequence is partitioned into ≤ k monotone subsequences, and
their sums total 1, then by pigeonhole at least one has sum ≥ 1/k.

**Step 3 — Wait, does this work?**
Let's check. We need to partition into monotone subsequences of the
SAME type (all increasing or all decreasing). Dilworth gives us:
- Either longest increasing ≥ k+1 (done, but we need sum ≥ 1/k too...
  length alone doesn't give us sum), OR
- Partition into ≤ k decreasing subsequences.

In the second case, pigeonhole gives a decreasing subsequence with
sum ≥ 1/k. ✓

In the first case, we have an increasing subsequence of length ≥ k+1
but we don't know its sum...

### Problem with this approach
Length ≥ k+1 doesn't guarantee sum ≥ 1/k. The k+1 elements could all
be tiny (e.g., the k+1 smallest values). So the first case DOESN'T
immediately give us what we want.

### Can we fix it?
Maybe. If the longest increasing subsequence has length ≥ k+1, can we
argue its sum is ≥ 1/k? Not directly. But maybe we can choose WHICH
increasing subsequence to take (not the longest, but the heaviest).

This seems to circle back to the Seidenberg approach — we need to
reason about sums, not just lengths.

### Verdict: DOESN'T WORK as stated. Needs Seidenberg-type fix.

---

## Approach 4: Dual Optimization (Clean but Abstract)

### Core idea
Frame as an optimization problem. Among all monotone subsequences,
let S* = max sum. We want S* ≥ 1/k. Suppose for contradiction S* < 1/k,
then derive a contradiction.

### Sketch
Assume every increasing subsequence has sum < 1/k and every decreasing
subsequence has sum < 1/k.

Define Sᵢ = max sum of increasing subsequence ending at xᵢ.
Then Sᵢ < 1/k for all i.

Define Tᵢ = max sum of decreasing subsequence ending at xᵢ.
Then Tᵢ < 1/k for all i.

Now use the rectangle-packing from Approach 2:
    Σ xᵢ² ≤ max(S) · max(T) < (1/k)(1/k) = 1/k²

But Cauchy-Schwarz gives Σ xᵢ² ≥ 1/k². Contradiction. ∎

### This is just Approach 2 repackaged as contradiction!
Same proof, different framing. Might be cleaner in Lean because
the contradiction structure is explicit.

### Formalization difficulty: MEDIUM (same as Approach 2)

---

## Approach Comparison

| Approach | Difficulty | Limits needed? | Key insight | Lean friendliness |
|----------|-----------|---------------|-------------|-------------------|
| 1. Blowup | Medium-Hard | YES | Reduce to classical E-S | Medium (limits painful) |
| 2. Seidenberg | Medium | No | Rectangle packing | HIGH (pure algebra) |
| 3. Pigeonhole | Broken | No | Doesn't work alone | N/A |
| 4. Contradiction | Medium | No | Same as 2, cleaner frame | HIGH |

---

## Recommended Order of Attack

### Round 1: Prove the Cauchy-Schwarz bound (standalone lemma)
This is needed by ALL approaches. Formalize:
    For k² positive reals summing to 1, Σ xᵢ² ≥ 1/k².
This is a direct consequence of Cauchy-Schwarz (or QM-AM).
Test with Axle. Get it compiling. This builds confidence.

### Round 2: Prove rectangle disjointness (the hard lemma)
Define Sᵢ, Tᵢ. Prove the rectangles [Sᵢ - xᵢ, Sᵢ] × [Tᵢ - xᵢ, Tᵢ]
are pairwise disjoint. This is the core technical content.

### Round 3: Assemble the contradiction proof (Approach 4)
Put it all together:
- Assume max(S) < 1/k and max(T) < 1/k
- Rectangle packing gives Σ xᵢ² < 1/k²
- Cauchy-Schwarz gives Σ xᵢ² ≥ 1/k²
- Contradiction.

### Round 4: Verify with Axle, compare with Aristotle's proof

---

## Open Questions for Next Session

1. **Rectangle disjointness:** The exact argument for why
   [Sᵢ - xᵢ, Sᵢ] × [Tᵢ - xᵢ, Tᵢ] are disjoint needs to be
   worked out carefully. The case split is:
   - If i < j and xᵢ < xⱼ: need Sⱼ ≥ Sᵢ + xⱼ (so S-intervals separate)
   - If i < j and xᵢ > xⱼ: need Tᵢ ≥ Tⱼ + xᵢ? Or Tⱼ ≥ Tᵢ + xⱼ?
   Direction matters. Work this out on paper.

2. **Do we need distinct values?** The problem says "distinct positive reals."
   Where does distinctness enter? In classical E-S, distinctness ensures the
   sequence is totally ordered. Here, distinctness might only be needed to
   ensure the xᵢ define a sequence (not a multiset). Check if the proof
   works without distinctness.

3. **What does Aristotle's proof actually look like?** We're going blind
   first, but after our attempt, we should pull the Lean file from
   github.com/plby/lean-proofs and compare structure.

4. **Can we formalize the Seidenberg scores?** In Lean, Sᵢ would be
   defined as a supremum over a finite set of sums. Need to check what
   Mathlib provides for "max over Finset."

---

*Created: March 8, 2026*
*Session: Brainstorming — no Axle/Aristotle calls*
