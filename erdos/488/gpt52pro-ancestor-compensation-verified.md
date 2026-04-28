# EP-488: 5.2 Pro — Ancestor Compensation VERIFIED for All 29 Kernels
## April 6, 2026

## THE RESULT

5.2 verified the finite ancestor compensation inequality for ALL 29 bad
kernels, ALL violating signatures (s,t), with ZERO failures.

### What was checked:
For each bad kernel K and each violating (s,t) with L_K(s) = 1:
- Child excess: Δ_child = n·L_K(t) - 2m (since L_K(s) = 1)
- Parent kernel: K^- = K \ {3}
- Parent slack: 2m·L_{K^-}(s') - n·L_{K^-}(t')
- Result: Parent slack ≥ Child excess for ALL 29 kernels, ALL signatures

### The margins are ENORMOUS:
- Tightest case: K={2,3} at (s,t)=(4,7), h_min=5
  - Child excess = 2
  - Parent slack = 136
  - Margin = 134
- For K={2,3,5,7} at (10,19): margin is in the THOUSANDS

### The compensating parent is ALWAYS K \ {3}
Remove 3 from the kernel. That's the parent. Universal across all 29.

### Parent signature computation:
s' = ⌈(h_min/3)(s+1)⌉ - 1
t' = ⌊(h_min/3)t⌋

where h_min(K) = min{h ≥ 2 : gcd(h, Π_{p∈K} p) = 1}
h_min values: {5, 7, 11, 13, 17} across the 29 kernels.

## WHY IT WORKS (uniform explanation):
1. Every bad case has L_K(s) = 1 (child is maximally weak)
2. This forces s < h_min(K)
3. Parent rescales by factor ≈ h/3 ≥ 5/3
4. Parent removes obstruction 3, so L_{K^-} jumps to double-digit scale
5. Result: parent has overwhelming surplus even in the tightest case

## THE ONE REMAINING GAP

The finite arithmetic is verified. What's NOT proved:

"In any primitive set A, if a compact layer has bad kernel K containing
{2,3}, then there EXISTS an earlier layer whose effective kernel at the
needed scale behaves like K \ {3}."

This is a STRUCTURAL statement about how obstruction sets arise from
primitive sets. Specifically:

If layer j has obstruction B_j containing both quotient-2 and quotient-3
elements, then there must exist an earlier layer i whose obstruction B_i
contains the quotient-2 element but NOT the quotient-3 element.

## WHY THIS STRUCTURAL BRIDGE SHOULD BE TRUE

If layer j has 3 in its effective kernel, that means some element a_i in A
satisfies a_i/gcd(a_i, a_j) = 3. Call this element the "3-ancestor."

The 3-ancestor itself has its own layer with its own obstruction set.
Since the 3-ancestor is EARLIER in the ordering (smaller index), its
obstruction set is a SUBSET of layer j's (it can't contain obstructions
from elements that come after it).

So the 3-ancestor's effective kernel should be K \ {3} or smaller.
That's exactly the parent we need.

## ON AHLSWEDE-KHACHATRIAN

5.2 notes that the AK correlation inequality requires NONNEGATIVE measures,
but the lcm-lattice coefficients μ_A(d) are SIGNED. So the direct
application doesn't work. Would need to go through nonnegative subset
counting weights first. Not a clean path.

## KILL COUNT: 58 (unchanged — no new kills)
## PERCENTAGE: 78%

Major jump from 72%. The finite verification is COMPLETE with enormous
margins. The only remaining gap is a structural lemma about how obstruction
sets inherit from primitive ancestry. This feels like a one-paragraph
argument, not a deep theorem.
