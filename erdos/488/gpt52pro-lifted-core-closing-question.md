# EP-488: 5.2 Pro — Lifted {2,3}-Core Safety (Independent Confirmation) + Closing Question
## April 8, 2026

## INDEPENDENT PROOF of Scaled {2,3}-Component Safety

5.2 proved the same theorem as Codex B independently:
If A = dB with 2,3 ∈ B, then B_A(n,m) ≥ ⌊m/d⌋ > 0.

Proof matches Codex B's structure:
F_A(x) = F_B(⌊x/d⌋), use 2/3 coverage of {2,3}, 2U(N)-N ≥ 1.
Explicit bound: B_A ≥ ⌊m/d⌋.

TWO INDEPENDENT MODELS, SAME THEOREM, SAME PROOF STRUCTURE.

## THE EXACT CLOSING QUESTION (stated by 5.2)

"Show: if a component has a bad layer but does NOT contain literal 2 or 3,
then gcd(C) > 1."

If proved → Theorem G (scaled {2,3}-core safety) closes EP-488.

## WHY THIS MIGHT BE TRUE

By Lemma D: a bad layer at depth s is adjacent to π(s) kernel witnesses.
None of these witnesses is literally 2 or 3 (by assumption).
So the 2-witness b satisfies b/gcd(b,a) = 2, meaning b = 2·gcd(b,a).
Since b ≠ 2: gcd(b,a) > 1, so b and a share a common factor > 1.
Similarly for the 3-witness.

The star of π(s) neighbors all share factors with the bad layer a.
If the component is connected, these shared factors propagate.
The question: does propagation force a GLOBAL common divisor?

## POTENTIAL APPROACH (5.2's suggestion)

Use Lemma D (deep star) + Lemma F (degree-size) to show that
having many kernel witnesses without literal 2,3 forces repeated
shared gcds along the star, hence a nontrivial global gcd.

Specifically: the 2-witness b has b = 2g where g = gcd(b,a) | a.
The 3-witness c has c = 3h where h = gcd(c,a) | a.
Since g | a and h | a: gcd(g,h) | a.
If gcd(g,h) > 1: there's a common factor shared by a, b, and c.
If this propagates through the component: global gcd > 1.

## KILL COUNT: 75
## PERCENTAGE: 88%

Up from 87%. Two independent confirmations of the lifted-core theorem.
The closing question is precisely stated. The proof of EP-488 reduces
to ONE graph-theoretic statement about n-LCM components.
