# EP-488: Formalize the 3-Tax / Upstream Credit Law
## For Codex xhigh — April 7, 2026

You just identified the key structural insight:

"Every bad compact child is paying a local 3-Buchstab tax, and the primitive
3-ancestor sits far enough upstream that its credit overfunds that tax."

You proposed two boxed inequalities. Prove them or find counterexamples.

---

## BOX 1

Claim: For a bad compact child j with kernel K ⊇ {2,3} and C = K \ {3}:

  E_j ≤ 2m · L_C(⌊s/3⌋) - n · L_C(⌊t/3⌋)

where s = ⌊n/a_j⌋, t = ⌊m/a_j⌋.

Your derivation: Buchstab gives L_K(x) = L_C(x) - L_C(⌊x/3⌋), so
  E_j = [n·L_C(t) - 2m·L_C(s)] - [n·L_C(⌊t/3⌋) - 2m·L_C(⌊s/3⌋)]

You claimed the first bracket is ≤ 0 because C is not a bad kernel.

Is this true? C = K \ {3} removes 3 from the kernel. Is C guaranteed
to NOT be one of the 29 bad kernels? (The 29 bad kernels all contain
{2,3}, so removing 3 means C doesn't contain {2,3}, so C is NOT bad.
This seems correct — verify.)

If the first bracket ≤ 0, then:
  E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋)

Prove this rigorously. State any additional conditions needed.

---

## BOX 2

Claim: For the 3-ancestor i with a_i = 3g, a_j = hg, h ≥ 5:

  2m · L_i(⌊n/a_i⌋) - n · L_i(⌊m/a_i⌋) ≥ 2m · L_C(⌊s/3⌋) - n · L_C(⌊t/3⌋)

The left side is the parent's actual slack. The right side is the child's
3-tax upper bound from Box 1.

The parent evaluates at scale ~(h/3)s while the tax lives at scale ~s/3.
Scale separation factor: ~h ≥ 5.

Questions:
- Is this provable from the scale separation alone?
- Does the parent's kernel matter at all, or is the scale factor sufficient?
- Can you bound L_i at scale (h/3)s from below in terms of L_C at scale s/3?
- Does the quotient transport lemma (q_{k,j} | 3·q_{k,i}) help here?

---

## WHAT WOULD CONSTITUTE A COMPLETE PROOF

If Box 1 and Box 2 are both proved, then for every bad compact child j:
  E_j ≤ [3-tax bound] ≤ [parent slack]

Summing over all bad children and using the fact that each parent is used
at most a bounded number of times (because the number of elements with
quotient 3 to a_j is bounded), the total GOOD exceeds total BAD.

Therefore F(m)/F(n) = Σ w_j R_j < 2m/n, and EP-488 follows.

---

## RULES
- Prove Box 1 and Box 2, or give explicit counterexamples.
- If you need a sub-lemma, state it precisely.
- If a step reduces to a finite check, say so.
- Do not re-derive the 3-tax insight. Build on it.
