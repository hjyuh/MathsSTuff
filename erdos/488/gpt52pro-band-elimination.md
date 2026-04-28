# EP-488: 5.2 Pro — 2-Band Elimination + 3-Band Quotient Forcing (PROVED)
## April 8, 2026

## TWO NEW PROVED LEMMAS

### Lemma 36: 2-Band Elimination
Any vertex with s(a) = 2 (i.e., a ∈ (n/3, n/2]) that has ANY neighbor
in the n-LCM graph is dominated-LCM prunable.

Proof: every neighbor quotient must be exactly 2 (since q ≤ s = 2 and
q ≥ 2 by primitivity). So q₀ = 2 divides all quotients trivially.
Dominated-LCM pruning applies. ∎

CONSEQUENCE: No vertex in (n/3, n/2] survives in a minimal counterexample.
Combined with s=1 being isolated: all elements must satisfy a ≤ n/3 (s ≥ 3).

### Lemma 37: 3-Band Quotient Forcing
Any non-prunable vertex with s(a) = 3 (i.e., a ∈ (n/4, n/3]) must have
BOTH a quotient-2 neighbor AND a quotient-3 neighbor.

Proof: neighbor quotients are in {2,3} (since q ≤ s = 3, q ≥ 2).
If all quotients are 2: dominated-LCM prunable (min quotient 2 divides all).
If all quotients are 3: dominated-LCM prunable (min quotient 3 divides all).
Must have both. ∎

CONSEQUENCE: s=3 vertices are forced {2,3} bifurcation points — they
must participate in both a 2-edge and a 3-edge simultaneously.

## WHAT THIS MEANS FOR MINIMAL COUNTEREXAMPLE ATOMS

After all pruning, every vertex satisfies:
- s ≥ 3 (Lemma 36 eliminates s=2, isolation eliminates s=1)
- Equivalently: a ≤ n/3, so n ≥ 3M

If vertex has s = 3 (the "top band" of the atom):
- Must have both 2-edge and 3-edge (Lemma 37)
- This is a local {2,3} bifurcation point
- Exactly the structure that creates split-core / witness-star patterns

If vertex has s ≥ 4:
- Already covered by first-layer theorem (S₁ > E_j individually)
- But collective excess might overwhelm S₁ (Kill #65)

## COMBINED WITH |A| ≤ 3 PROVED (Codex B):

A minimal counterexample atom has:
- |A| ≥ 4
- All elements ≤ n/3
- s=3 vertices forced into {2,3} bifurcation
- No literal 2

This is an extremely constrained object.

## KILL COUNT: 77
## PERCENTAGE: 92%

Holding at 92% (consistent with Codex B's |A| ≤ 3 theorem).
Two new structural lemmas that tighten the atom constraints further.
