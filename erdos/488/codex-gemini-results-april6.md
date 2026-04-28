# EP-488: Codex A (Terminal) — Gap Geometry + Literature
## April 7, 2026

## KEY INSIGHT (converges with Codex B)

"Bad compact layers are exactly initial-gap phenomena, and 3-ancestry
forces evaluation beyond that gap by enough to create uniform
overcompensation."

Codex A calls it "forced dephasing" and "gap geometry."
Codex B calls it "3-tax / upstream credit law."

THEY'RE THE SAME THING:
- The child's badness = L_K(s) = 1 = initial survivor desert
- The parent's evaluation = past the desert = forced by h/3 ≥ 5/3 scale
- The compensation = geometric (scale separation), not order-theoretic (kernel)

## CODEX A's FOUR PROPOSED PATHS (ranked)

### Path 1: Gap-geometry route (BEST — short human proof possible)
- Define gap invariant for sieve set B
- Prove parent points s', t' lie past the initial gap
- Show 2t·L_i(s') - (s+1)·L_i(t') ≥ 18 (or whatever beats child excess ≤ 17)
- Uses existing facts, avoids every killed reduction

### Path 2: Hybrid finite + analytic tail (FASTEST rigorous finish)
- 29 kernels + quotient transport → finite dangerous region
- Tail lemma: for h > H₀, parent slack grows linearly in h, child stays O(1)
- Exhaust h ≤ H₀ by exact computation
- "This is the architecture I would bet on if the goal is finish the paper"

### Path 3: Buchstab/renewal route (HARDER but clean)
- L_B(x) = L_{B\{3}}(x) - L_{B\{3}}(⌊x/3⌋)
- Prove direct inequality for D_L(u,v) = 2v·L(u) - u·L(v) under
  "remove 3, dilate by ≥ 5/3"
- This is exactly Codex B's Box 1 + Box 2

### Path 4: Global charging (FALLBACK)
- Throws away the rigid 3-ancestry structure
- Ranked below others

## CODEX A's NOVEL COMBINATION

Combine: 29-kernel classification + quotient transport + Jacobsthal gap
machinery + finite verification of small h signatures.

"Replaces 'parent kernel dominates child kernel' by 'parent evaluation
outruns the child's initial forbidden desert.'"

## LITERATURE RECOMMENDATIONS

1. Richard Hall, "Sets of Multiples" (Cambridge) — Ch 3 Oscillation, Ch 5
   Divisor Density. CLOSEST big-picture source.
2. Hall-Tenenbaum, "The Set of Multiples of a Short Interval" — closest
   in spirit to finite-cutoff counting.
3. Montgomery-Vaughan, "On the distribution of reduced residues" (Annals 1986)
   — best deep source for local gap/moment control of reduced residues.
4. Aryan, "Distribution of k-tuples of reduced residues" (Mathematika)
   — modern extension if right invariant is gap structure.
5. Friedlander-Iwaniec, Opera de Cribro — standard Buchstab reference.

## ASSESSMENT

Codex A independently reached the same structural conclusion as Codex B:
the phenomenon is GEOMETRIC (scale/gap based), not ORDER-THEORETIC
(kernel comparison based). Two independent models, same conclusion.

Path 2 (hybrid finite + tail) is probably the fastest to a complete proof.
Path 3 (Buchstab/renewal) is what Codex B already formalized as Box 1 + Box 2.
Path 1 (gap geometry) might give the shortest proof but needs new definitions.

The convergence of Codex A and B on the same core insight — "initial gap
phenomenon + forced dephasing" — is the strongest evidence that this is
the RIGHT explanation, not just another mechanism that will get killed.
