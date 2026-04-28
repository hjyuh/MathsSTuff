# EP-488: GPT-5.4 Pro Post-Peak Analysis — Round 2
## April 3, 2026

## Kill #32: C ≥ (1+δ)E Post-Peak is FALSE
Counterexample: (a,k,t) = (7,2,6) at x=197 (post-peak, w=6).
All 11 nearest multiples are distinct. C=0, E=5.
Post-peak windows often have ZERO collisions.
The collision-surplus approach is dead for post-peak.

## The Corrected Post-Peak Identity
Raw W(x) includes anchor-row multiples (a|q). Need corrected version:
W♯(x) = t - Z(x) + E♯(x) - C♯(x)
where Z counts block elements with zero non-anchor hits in window.
Corrected deficit C♯+Z ≥ (1+δ)E♯ also FALSE at (7,2,6,450).

## THE KEY NEW INSIGHT: Periodic Deviation Reduction

F(qL+r) = qF(L) + F(r), so:
G(qL+r) = δ_A + D(r)/(qL+r)

where D(r) = F(r) - δ_A·r is a PERIODIC deviation function on [0, L).

Consequences:
1. Along each residue ray (fixed r), G is monotone:
   - D(r) > 0: G decreasing (SAFE — high G means small ratio)
   - D(r) < 0: G increasing toward δ_A (DANGEROUS — low G dip)
   - D(r) = 0: G constant at δ_A

2. The future envelope E(n) is EXACTLY computable from D:
   E(qL+r) = max(δ_A, max_{s>r} (δ_A + D(s)/(qL+s)), ...)

3. The ratio E(n)/(2G(n)) DECREASES with q along negative-D rays.
   So worst case is at FIRST occurrence after m*.

4. Conjecture 7.1 becomes: bound the periodic deviation envelope of D.

## Structural Diagnosis
Pre-peak: short contiguous row blocks, carrier-AP structure, finite state.
Post-peak: dispersed nearest-multiples, anchor contamination, periodic structure.
The regimes are QUALITATIVELY DIFFERENT. Pre-peak methods don't transfer.

## Recommendation
Abandon pointwise collision-surplus for post-peak.
The right framework is periodic deviation D(r) + averaged window bounds
over the long intervals forced by the long-rebound lemma.

## Status
- Route killed: C ≥ (1+δ)E (approach #32)
- New reduction: periodic deviation envelope
- Conjecture 7.1 NOT proved
