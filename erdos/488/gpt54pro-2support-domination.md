# EP-488: 5.4 Pro — 2-Support Singleton Domination (PROVED)
## April 7, 2026

## TWO NEW PROVED THEOREMS

### Theorem 1: Individual 2-support pays each bad child
For any bad layer a with 2-support b (quotient 2):
  T(b) > E_a
where T(b) = 2m⌊n/b⌋ - n⌊m/b⌋ (singleton surplus).

### Theorem 2: One 2-support pays ALL its assigned bad children
Fix b = 2d. Assign all bad children a_j with b/gcd(b,a_j) = 2.
Then: T(b) > Σ_{j→b} E_j

Proof uses: signature coefficient table c_s, band counting per
signature, and x = n/d ≥ 12 (from existence of bad child with h ≥ 3).

For x ≥ 25: 0.0461x² + 9.14x < x²/2 - 2x. ✓
For 12 ≤ x < 25: direct check, worst case 26d < 48d. ✓

## THE CRITICAL CONSEQUENCE

Partition ALL bad layers by designated 2-support.
Sum the theorem over all support batches:

  Σ_{b ∈ S₂} T(b) > Σ_bad E_j

THIS HOLDS FOR ANY PRIMITIVE SET. No common core needed.
No kernel comparison. No ancestor matching. Fully distributed.

## WHAT THIS IS AND ISN'T

T(b) is the SINGLETON surplus — the overcounting/Architecture 2 term.
T(b) ≥ S_b always (singleton counts more than layer counts).

So: Σ T(b) > Σ E_j at the SINGLETON level.

But EP-488 needs the ACTUAL surplus (after IE corrections) to be positive:
  2mF(n) - nF(m) = MAIN - IE_CORRECTION > 0

5.4 proved: the 2-support portion of MAIN already exceeds the bad excess.
Remaining gap: the IE correction doesn't eat ALL of this margin.

## WHY THIS NARROWS THE GAP ENORMOUSLY

Before 5.4: "Can we extract enough good budget from general primitive sets?"
After 5.4: "We HAVE enough good budget at the singleton level. Does the
IE correction preserve enough of it?"

The gap shifted from EXTRACTION to PRESERVATION.

And we know from Kill #68 that pair strands eat ~5/6 of MAIN for dense
prime sets. But 5.4 showed the 2-support T(b) values alone exceed bad
excess. So even after losing 5/6 of MAIN to IE correction, the
remaining 1/6 might still exceed the bad excess — because the bad
excess is a TINY fraction of MAIN.

## THE UPDATED GAP

Old gap: "Does global charging work for distributed-core sets?"
New gap: "Does the IE correction preserve enough of the 2-support
singleton margin to keep the actual surplus positive?"

This is MUCH narrower. It connects Architecture 1 (global charging)
and Architecture 2 (IE correction) — the answer lives at their intersection.

## KILL COUNT: 70
## PERCENTAGE: 87%

Major jump. 5.4 proved the extraction problem is SOLVED at singleton
level for fully general primitive sets. No common core needed. The
remaining gap is purely about IE correction preservation.
