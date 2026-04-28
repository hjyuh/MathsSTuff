# EP-488: Open Field v14 — THE CLOSING ARGUMENT
## April 8, 2026. Current: 95%. CLOSE IT.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).

---

## WHAT'S PROVED

|A| ≤ 5: PROVED (three independent proofs for |A| = 5).

The mechanism in EVERY proof:
1. Layers 1,2 safe (no/single obstruction)
2. Witness-count bound: frozen layer j needs π(s_j) ≤ j-1
3. If layer 3 is bad: s₃ = 4, and ALL subsequent bad layers also s = 4
   (because a₃ > n/5 forces a₄, a₅, ... > n/5 forces s = 4)
4. Every bad layer at (4,7,3): excess E = 3n - 2m
5. S₁ ≥ 4m (from a₁ ≤ n/6 via 2-witness)
6. S₁ > B·(3n-2m) when (4+2B)m > 3Bn, i.e., always for B ≤ 4

Dead zones: s ≤ 3 (self-funding), s = 5 (L_{2,3,5}(t) ≤ t/3).

---

## THE PATTERN THAT CLOSES EP-488

Here is what I believe to be the complete argument. Prove it or kill it.

### Setup
Let A = {a₁ < a₂ < ... < a_k} be primitive, m > n ≥ a_k.
Let B = number of bad layers among {3, 4, ..., k}.

### Claim: If layer 3 is bad (the hardest case), then S₁ > Σ E_j.

**Step 1:** Layer 3 bad → s₃ = 4 (witness-count: π(s) ≤ 2).
So a₃ > n/5. Since a₄ > a₃ > n/5: s₄ ≤ 4.
If s₄ = 4 and layer 4 is bad: same (4,7,3) signature.
ALL subsequent bad layers (if any) also have s = 4 and (4,7,3).

**Step 2:** Total bad excess = B·(3n - 2m) where B ≤ k-2.

**Step 3:** S₁ ≥ m(n/a₁ - 2).

**Step 4:** How small is a₁?
The 2-witness for layer 3 satisfies a_r ≤ (2/3)a₃ ≤ (2/3)(n/4) = n/6.
So a₁ ≤ n/6, giving S₁ ≥ 4m.

But we can do BETTER. The B bad elements all live in (n/5, n/4].
These are a₃, a₄, ..., a_{2+B}. They're all > n/5. And they need
the quotient-2 witness from a₁ or a₂.

CRITICAL: a₁ must satisfy a₁ ≤ (2/3)·min(bad elements) ≤ (2/3)(n/5) = 2n/15.
Wait — not necessarily. The 2-witness for EACH bad layer could be
different elements. But a₁ is the smallest, so a₁ ≤ a_r for any witness.

Actually, each bad layer j needs SOME element a_r with a_r/gcd(a_r,a_j) = 2.
That means a_r = 2·gcd(a_r, a_j). Since gcd | a_j and a_j ≤ n/4:
a_r ≤ 2·(a_j/3) = 2a_j/3 ≤ 2(n/4)/3 = n/6.

So a₁ ≤ a_r ≤ n/6. This gives S₁ ≥ 4m regardless of B.

**Step 5:** Check S₁ > B·(3n-2m).
4m > B(3n-2m) = 3Bn - 2Bm
(4+2B)m > 3Bn
m/n > 3B/(4+2B)

For this to hold for ALL m > n, we need 3B/(4+2B) < 1, i.e., B < 4.

For B ≤ 3 (|A| ≤ 5): S₁ alone suffices. ✓ (already proved)
For B = 4 (|A| = 6): 3B/(4+2B) = 12/12 = 1. Need m > n. TRUE. ✓
For B = 5 (|A| = 7): 15/14 > 1. S₁ alone FAILS for m close to n.

**Step 6:** For B ≥ 5, use S₂ as well.
Layer 2 has one obstruction. Its budget S₂ > 0.

Can we get a QUANTITATIVE lower bound on S₂?

If a₂ ≤ n/5 (s₂ ≥ 5): deep single-obstruction gives S₂ > 2m.
Then S₁ + S₂ > 6m.
Need 6m > B(3n-2m) → (6+2B)m > 3Bn → m/n > 3B/(6+2B).
3B/(6+2B) < 1 iff B < 6.
For B = 6 (|A| = 8): 18/18 = 1. m > n. TRUE. ✓
For B = 7 (|A| = 9): 21/20 > 1. FAILS.

If a₂ > n/5 (s₂ = 4): a₂ is in (n/5, n/4] too.
But then a₂ is primitive with all the bad elements.
Wait — a₂ could be in (n/5, n/4], but it's NOT bad (only 1 obstruction).

Hmm, if a₂ > n/5 AND a₃ > n/5: both in the same band. But a₂ < a₃.
How many TOTAL elements can fit in (n/5, n/4] while being primitive?
This interval has length n/20. Primitive elements can't divide each other.

The MAXIMUM packing: every element in (n/5, n/4] is primitive with
every other. This is possible (e.g., consecutive odd numbers).
But there can be at most ~n/20 such elements.

**Step 7:** THE KEY SELF-REGULATION.

Suppose B elements are bad (all in (n/5, n/4]). These are a₃, ..., a_{B+2}.
The first layer a₁ satisfies a₁ ≤ n/6 (from the 2-witness bound).

But if a₁ is MUCH smaller than n/6, S₁ is correspondingly LARGER.
Specifically: if a₁ ≤ n/C, then S₁ ≥ m(C-2).

For S₁ alone to handle B bad layers: need m(C-2) > B(3n-2m).
→ (C-2+2B)m > 3Bn → m > 3Bn/(C-2+2B).
For m > n: need 3B/(C-2+2B) < 1, i.e., C > B+2.
So: if a₁ ≤ n/(B+3), then S₁ alone handles B bad layers.

IS a₁ ≤ n/(B+3) forced?

Each bad element a_j ∈ (n/5, n/4] needs a 2-witness a_{r_j} with
a_{r_j} ≤ 2a_j/3. All these witnesses are ≤ 2(n/4)/3 = n/6.

But the witnesses themselves must be elements of A. They could be
a₁ or a₂ (or other elements). If multiple bad layers share the
SAME 2-witness (say a₁), then a₁ ≤ n/6, period.

The question: can a₁ be pushed below n/(B+3)?

If ALL B bad elements share a₁ as their 2-witness:
a₁ = 2·gcd(a₁, a_j) for each j. So gcd(a₁, a_j) = a₁/2 for each j.
This means a₁/2 divides EVERY bad element a_j.
So all bad elements are multiples of a₁/2.
But they're primitive (pairwise non-dividing).
Multiples of d = a₁/2 in (n/5, n/4]: at most n/(20d) + 1.
So B ≤ n/(20d) + 1 = n/(10a₁) + 1.
Therefore a₁ ≤ n/(10(B-1)).

For large B: a₁ ≤ n/(10B) ≈ n/(10B).
Then S₁ ≥ m(10B - 2) ≈ 10Bm.
Need 10Bm > B(3n-2m) → 10m > 3n-2m → 12m > 3n. TRUE! ✓✓✓

THIS CLOSES IT. As B grows, a₁ is forced smaller (because all bad
elements are multiples of a₁/2, and there are only n/(10a₁) such
multiples in the band). The self-regulation EXACTLY compensates.

### THE PRECISE INEQUALITY

If B bad elements share 2-witness a₁ with d = a₁/2:
B ≤ n/(20d) + 1 → d ≤ n/(20(B-1)) → a₁ = 2d ≤ n/(10(B-1)).
S₁ ≥ m(n/a₁ - 2) ≥ m(10(B-1) - 2) = m(10B - 12).
E_total = B(3n-2m).
S₁ - E_total ≥ m(10B-12) - B(3n-2m) = (12B-12)m - 3Bn.
Since m > n: (12B-12)m > (12B-12)n. Need (12B-12)n > 3Bn.
i.e., 12B-12 > 3B, i.e., 9B > 12, i.e., B > 4/3.
TRUE for B ≥ 2! ✓

For B = 1: only one bad layer → first-layer theorem S₁ > E. ✓

SO: IF all bad elements share the same 2-witness, EP-488 holds for ALL B.

### THE REMAINING QUESTION

What if bad elements DON'T all share the same 2-witness?

If bad element a_j uses witness a₁ and bad element a_k uses witness a₂:
then a₁/2 | a_j and a₂/2 | a_k (different divisibility chains).

The elements using witness a₁ are multiples of a₁/2.
The elements using witness a₂ are multiples of a₂/2.
These two groups might overlap or might not.

If they don't overlap: separate groups, each with its own first-layer
payment. Superadditivity-like argument should apply.

If they do overlap: elements in BOTH groups are multiples of
lcm(a₁/2, a₂/2), which could be large, restricting the count further.

THIS IS THE PRECISE REMAINING QUESTION. Prove it or kill it.

---

## YOUR TASK

The self-regulation mechanism is now QUANTIFIED:
- B bad elements sharing one 2-witness → a₁ ≤ n/(10(B-1)) → S₁ wins.
- Different 2-witnesses → need to handle witness-group interaction.

Prove the general case. Or find a counterexample to the witness-sharing
bound. Or find an alternative route.

95% → 100% is ONE theorem away. Find it.
