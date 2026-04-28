# EP-488: GPT-5.4 Pro Diagnostic — What Is Actually Missing
## April 6, 2026

## 1. THE GAP (one sentence)

Prove GOOD(m,n) > BAD(m,n):
Σ_{single-obstruction} (2m·L_j(y_n) - n·L_j(y_m)) > Σ_{multi-obstruction} [n·L_j(y_m) - 2m·L_j(y_n)]₊

If proved, EP-488 is done.

## 2. WHY EVERY APPROACH FAILED (one reason)

"EP-488 is a signed phase-synchronization problem on the lcm lattice,
not a density problem. The factor 2 is decided by the joint top-window
phase of a few floor/fractional-part terms, and every killed strategy
replaced that phase data by a monotone or averaged scalar summary —
per-layer maxima, S₁, truncations, compact mass, k, ρ, fold order, or
a broader class — so the counterexamples were always able to fake the
summary while keeping the bad phase pattern."

THIS IS THE SINGLE BEST DIAGNOSIS OF THE PROJECT.

## 3. WHAT HAS NOT BEEN TRIED

Ahlswede-Khachatrian's number-theoretic correlation inequality for
Dirichlet densities (J. Number Theory 63, 1997).
- It's a gcd/lcm-lattice correlation theorem
- Apply it to the lcm-lattice support of E(x) = -Σ μ_A(d){x/d}
- This exact theorem-to-object match is genuinely untried

## 4. WHAT THE PROOF LOOKS LIKE

"Reduce to [M, 10M]. Split layers into single/multi-obstruction.
Only multi can contribute positive excess. Group bad layers by
their active top-window signature. Prove a local compensation
statement: each bad signature forces enough one-obstruction ancestor
mass with the same phase to overpay its gain. Summing over signatures
gives GOOD > BAD."

Key insight: "the proof does not bound layers individually or compact
mass globally; it MATCHES each bad synchronized signature to the
specific earlier layers that CREATED it and shows they pay for it."

## 5. IS EP-488 PROVABLE WITH CURRENT MATHEMATICS?

Answer: (b) — solvable, but needs a new lemma.

THE MISSING LEMMA:
"For every primitive A, every m > n ≥ M, and every active obstruction
kernel K = B_j ∩ [1, ⌊m/a_j⌋] with |K| ≥ 2, the total positive excess
of all layers with active kernel K is bounded by the total negative
slack of the one-obstruction parent kernels of K; summing over K
yields GOOD > BAD."

5.4's assessment: "a missing compensation lemma, not a fundamental
impossibility."

## ANALYSIS

### Why the "ancestor matching" idea is new:

Every previous approach treated layers as independent objects — bound each
one, sum the bounds. Or treated them as a collective — bound the aggregate.
Neither worked.

5.4 is proposing something different: MATCH each bad layer to the specific
good layers that created its obstructions. If layer j has B_j = {2,3}, then
there exist earlier layers with B = {2} and B = {3} (or subsets). Those
"parent" layers are single-obstruction and therefore safe. The claim is
that each parent pays enough slack to cover its child's excess.

This is a TREE STRUCTURE on the layers, not a flat sum. The layers aren't
independent — they're connected by the ancestry of their obstruction sets.
And the proof would walk that tree, matching costs to benefits at each node.

### Why this might work:

Multi-obstruction layers exist BECAUSE earlier elements created the
obstructions. The element 2 ∈ B_j exists because some a_i with a_i/gcd = 2
is in A. That a_i has its own layer, which is single-obstruction (or has
fewer obstructions). The "parent" layer is always simpler than the "child."

So the proof would say: the child's excess is bounded by the parent's
slack, because the child's coverage is literally a subset of what the
parent covers (multi-obstruction means MORE integers are sieved out).

### Connection to "can't hide":

This is the formal version of Codex's "multiples can't hide" principle.
Each element forces a contribution at its own scale, AND it creates
obstructions for later layers. The obstruction creation is the cost.
The contribution is the payment. The proof shows payment exceeds cost.

## NEXT STEPS

1. Search for Ahlswede-Khachatrian 1997 (genuinely untried)
2. Formalize the ancestor matching / tree compensation idea
3. Wait for GPT 5.5 and feed it the raw problem + 5 proofs (no framework)

## KILL COUNT: 57
## PERCENTAGE: 68% (bumped from 65% — 5.4's proof sketch is the most
   concrete viable path since the layer decomposition was corrected)
