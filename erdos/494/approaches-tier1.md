# Erdős Problem 494 — Tier 1: k_eq_2_card_pow_two
## March 12, 2026

---

## Target

```lean
@[category research solved, AMS 5]
theorem erdos_494.variants.k_eq_2_card_pow_two :
    ∀ card : ℕ, (∃ l : ℕ, card = 2 ^ l) → ¬Erdos494Unique 2 card := by
  sorry
```

### Plain English
For every cardinality that's a power of 2, there exist two DISTINCT finite subsets A ≠ B of ℂ with |A| = |B| = 2^l such that their 2-element sum multisets are equal. This is a COUNTEREXAMPLE construction — show Erdos494Unique 2 (2^l) is false.

### Recall: `Erdos494Unique k card`
```lean
def Erdos494Unique (k : ℕ) (card : ℕ) :=
  ∀ A B : Finset ℂ, A.card = card → B.card = card → sumMultiset A k = sumMultiset B k → A = B
```

So ¬Erdos494Unique 2 card means: ∃ A B : Finset ℂ, A.card = card ∧ B.card = card ∧ sumMultiset A 2 = sumMultiset B 2 ∧ A ≠ B.

---

## What's Already in the File (Existing Machinery)

The 494.lean file already contains PROVEN theorems with reusable infrastructure:

### `card_eq_2k` (PROVEN — Tao's A vs -A construction)
Shows ¬Erdos494Unique k (2*k) for k > 2 by constructing:
- A = witnessA k = {1, 2, 3, -6} ∪ D ∪ negImage(D) where D = {10, 11, ..., 10+k-3}
- B = negImage(A) = {-a | a ∈ A}
- Key engine: `sumMultiset_eq_negImage` — if A.card = 2k and A.sum = 0, then sumMultiset A k = sumMultiset (negImage A) k

### `k_eq_card` (PROVEN — rotation counterexample)
Shows ¬Erdos494Unique k k for k > 2 using counterexampleA/counterexampleB with Complex.I rotation.

### Available helpers:
- `negImage` — negate all elements of a Finset ℂ
- `negImage_card` — |negImage A| = |A|
- `sumMultiset_eq_negImage` — if |A| = 2k and sum(A) = 0, then sumMultiset A k = sumMultiset (negImage A) k
- `sum_negImage` — sum(negImage A) = -sum(A)
- All the disjointness/membership lemmas for witness sets

---

## The Mathematical Construction

### What Selfridge-Straus showed (the classical counterexample)

For k = 2 and card = 2^l, the counterexample uses roots of unity or similar symmetric constructions. The key insight: if A has the property that A = -A + c for some constant c (a "symmetric translate"), then sumMultiset A 2 can equal sumMultiset B 2 for a related B.

### Simplest approach: Reuse the A vs -A engine

The `sumMultiset_eq_negImage` lemma already gives us: if |A| = 2k and sum(A) = 0, then the k-element sum multiset of A equals that of -A.

For our target: k_eq_2_card_pow_two needs Erdos494Unique 2 (2^l) to be false, i.e., we need |A| = 2^l and the 2-element sums of A and -A to match.

Setting k = 2^(l-1) in the existing `card_eq_2k` gives: ¬Erdos494Unique (2^(l-1)) (2^l). But we need k = 2, not k = 2^(l-1).

**So `card_eq_2k` does NOT directly apply.** We need a different construction specifically for k = 2.

### The correct construction for k = 2

For 2-element sums (k=2), the classical counterexample for card = 2^l uses:
- Construct A ⊂ ℂ with |A| = 2^l and sum(A) = 0
- Let B = negImage(A)
- sumMultiset_eq_negImage gives sumMultiset A (2^(l-1)) = sumMultiset B (2^(l-1))

Wait — that's the wrong k again. We need sumMultiset A 2 = sumMultiset B 2.

**The right approach for k = 2:** The 2-element sum multiset of A is {a_i + a_j : i < j} (with multiplicity). For this to equal the 2-element sum multiset of -A = {-a_i - a_j : i < j}, we'd need the multiset of pairwise sums to be symmetric. But the sums of A are a_i + a_j while the sums of -A are -(a_i + a_j). These are generally different multisets unless all pairwise sums are 0, which is impossible for |A| > 1.

**So the A/-A engine DOESN'T WORK for k = 2 directly.**

### Alternative: Polynomial method / roots of unity

The classical Selfridge-Straus counterexample for k=2, card=2^l uses:
- Consider A = {a₁, ..., a_n} ⊂ ℂ
- The 2-element sum multiset determines the power sum symmetric functions S₁(A), S₂(A)
- For card = 2^l, one can construct A ≠ B with same S₁, S₂ using the fact that 2^l allows recursive "doubling" constructions
- Specifically: if {a,b} and {c,d} have a+b = c+d and a²+b² = c²+d², then a=c,b=d OR a=d,b=c. But for SETS of size 2^l, you can build non-isomorphic sets with matching power sums by a recursive halving/doubling.

### Most Lean-friendly approach: Explicit small cases + induction

**Base case l = 0:** card = 1. ¬Erdos494Unique 2 1 means ∃ A B with |A|=|B|=1 and same 2-element sums and A≠B. But 2-element sums of a singleton are empty (can't pick 2 elements from 1). So sumMultiset A 2 = sumMultiset B 2 = ∅ for any singletons A ≠ B. This is TRIVIAL — any two distinct singletons work.

**Base case l = 1:** card = 2. Need A ≠ B with |A|=|B|=2 and same 2-element sums. sumMultiset {a,b} 2 = {a+b}. So need a+b = c+d with {a,b} ≠ {c,d}. Example: A = {0,1}, B = {-1,2}. Sum = 1 for both. Done.

**Inductive step:** Given a counterexample pair (A,B) of size 2^l, construct a counterexample pair of size 2^(l+1). This can be done by "shifting": take A' = A ∪ (A + M) and B' = B ∪ (B + M) for M sufficiently large. The 2-element sums split into: sums within the first copy, sums within the second copy, and cross-sums. If M is large enough, these three groups are disjoint, and the within-group sums match by hypothesis.

This inductive construction is clean and Lean-friendly.

---

## Proof Strategy

### Approach 1: Trivial base case (l = 0 or l = 1) + induction

**For l = 0 (card = 1):**
Any two distinct singletons have the same (empty) 2-element sum multiset.
```lean
-- Witness: A = {0}, B = {1}
-- sumMultiset {0} 2 = ∅ = sumMultiset {1} 2 (can't choose 2 from 1)
-- {0} ≠ {1}
```

**For general l (card = 2^l):**
Actually, the l = 0 argument works for ALL card values where card < 2: if card = 1, any two distinct singletons give empty 2-element sum multisets. And if card = 2^0 = 1, that's exactly this case.

Wait — we need to be more careful. For card = 2^l with l ≥ 1, we need actual non-trivial counterexamples.

### Approach 2: Direct construction for all 2^l simultaneously

For ANY n = 2^l, construct:
- A = Finset.range n (i.e., {0, 1, ..., n-1} embedded in ℂ)
- B = insert n (Finset.range n \ {some element}) adjusted to have same 2-sums

This gets complicated. Better to use the shifting/induction approach.

### Approach 3: Let Codex figure out the construction

Given that this is mathematically subtle (the right construction isn't immediately obvious), the best move might be:
1. Give Codex the full file context with existing machinery
2. Point it at the sorry
3. Let it try multiple approaches including searching for small explicit counterexamples
4. If it stalls, get GPT to produce the specific construction first

---

## Key Observations for Codex

1. **l = 0 (card = 1) is trivial:** sumMultiset of a singleton with k=2 is empty. Any two distinct singletons work.

2. **l = 1 (card = 2) is easy:** {0, 1} and {-1, 2} both have 2-sum = {1}. Or simpler: {0, 3} and {1, 2} both have 2-sum = {3}.

3. **The theorem quantifies over ALL card that are powers of 2.** So you need a construction that works for every 2^l. An inductive approach or a parametric family is needed.

4. **The existing negImage/complement machinery may or may not help.** It's designed for the "A vs -A when sum = 0" pattern. For k = 2 specifically, this might not apply.

5. **Consider: for card ≤ 2, sumMultiset A 2 has ≤ 1 element.** For card = 1, it's empty. For card = 2, it's a singleton {a+b}. Matching a singleton is easy. So the hard cases start at l ≥ 2 (card ≥ 4).

6. **The powersetCard 2 of A is just all pairs.** sumMultiset A 2 = multiset of {a_i + a_j : {i,j} ⊆ A, i ≠ j}. This is a well-studied object (the "sumset of pairs").

## Recommended Codex Instructions

1. Read the full 494.lean file for existing machinery
2. Try the trivial cases first (l=0, l=1) to understand the API
3. For the general case, try a parametric family construction OR induction on l
4. Use xhigh compute, sub-agents if available
5. If stuck on the general construction after 15 minutes, focus on understanding what mathematical construction works and request a GPT roadmap

---

## Files Reference

| File | Location |
|------|----------|
| 494.lean | `!math/erdos/formal-conjectures/FormalConjectures/ErdosProblems/494.lean` |
| Existing proven theorems | k_eq_card, card_eq_2k, product — all in same file |
| card_eq_2k scratch engine | `!math/erdos/erdos-1026/.codex_card_eq_2k_scratch.lean` |

---

*Created: March 12, 2026*
*Pipeline: Claude → Codex (xhigh) → Axle*
