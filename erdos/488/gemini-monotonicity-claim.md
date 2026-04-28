# EP-488: Gemini — Architecture 2 Kill + Sieve Monotonicity Claim
## April 7, 2026

## CLAIM 1: Kill Architecture 2 (IE Correction Framework)

Gemini says: the alternating sum has binomially many terms.
C(k,2) positive terms at order 2, C(k,3) negative at order 3, etc.
Bounding individual T(d) magnitudes can't control the alternating sum
when the number of terms explodes. "Category D in disguise."

ASSESSMENT: Partially correct, partially wrong.
- CORRECT: naive "each term ≤ half" doesn't work for large k because
  the NUMBER of terms grows binomially. This is the co-atom problem.
- WRONG: Architecture 2 doesn't TRUNCATE IE (which is what Category D
  kills). It keeps the full alternating sum. The question is whether
  the full alternating sum is bounded by the main sum.
- The co-atom concern is real but there might be ways to handle it
  (e.g., the alternating sum might telescope for primitive sets).

VERDICT: Architecture 2 is WEAKENED but not definitively killed.
The naive approach fails. A more sophisticated approach might work.

## CLAIM 2: Swarm Topology Dichotomy

"Any swarm either collapses to Codex B's family (shared ancestors)
or generates independent ancestors dense enough to fund it."

ASSESSMENT: Structurally sound as intuition, not proved.
The "convex hull between shared and independent" is exactly the gap.
Mixed topologies (some sharing, some independent) aren't addressed.
This is a framework, not a theorem.

VERDICT: Valuable framing. Not a proof.

## CLAIM 3: Sieve Monotonicity — {2,3} is worst case

"Adding primes to K monotonically decreases excess AND increases slack.
Therefore {2,3} is the global minimum. Codex B proved {2,3}. QED."

ASSESSMENT: THIS NEEDS CAREFUL CHECKING.

The claim: adding prime p to K:
(a) removes p from eligible survivors → fewer spikes → less excess
(b) forces p-ancestor into A → more good layers → more slack

Concern with (a): adding 5 to K forces s ≥ 6 (prime-cover rigidity).
At s=6, the window (s,t] can extend to t=20. Primes in (6,20] are
{7, 11, 13, 17, 19} — FIVE potential spikes.
Compare K={2,3} at (4,7): primes in (4,7] are {5,7} — TWO spikes.

So adding 5 to K can INCREASE the number of spikes from 2 to 5!
The per-layer Δ_j is NOT monotone decreasing in |K|.

BUT: the EXCESS E_j = n·Δ_j - D depends on the specific (s,t) signature.
For K={2,3,5} at s=6: n > 6a_j. For K={2,3} at s=4: n > 4a_j.
The larger n might offset the larger Δ_j through the D = 2m-n term.

VERDICT: The monotonicity claim is PLAUSIBLE but NOT PROVED as stated.
The per-layer spike count is not monotone. The global budget might be
monotone due to the ancestor tax, but this needs rigorous verification.

If the monotonicity is TRUE, it closes the entire problem
(Codex B proved {2,3}, monotonicity extends to all 29 kernels).
If it's FALSE, we need to handle each kernel family separately.

## OVERALL ASSESSMENT

Gemini's most important contribution: the Sieve Monotonicity conjecture.
If proved, EP-488 is solved. If killed, we know to handle kernels
case-by-case.

PRIORITY: Verify or kill the monotonicity claim.

## KILL COUNT: 67 (Architecture 2 weakened but not killed — call it 67.5)
## PERCENTAGE: 82% (holding — monotonicity needs verification before bump)
