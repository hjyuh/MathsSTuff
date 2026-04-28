# EP-488 Model Rotation — Round 3 Prompts (Generalization)
## April 3, 2026

EP-488 IS PROVED FOR ALL ONE-ANCHOR FAMILIES.
All models now target the ONLY remaining piece: proving general primitive
sets are not worse than one-anchor families.

---

## Claude (other chat) — Monotone reduction

PROMPT:
---
You proved EP-488 for all one-anchor families (First Plateau + Post-Peak). The paper is v4 (attached). The ONLY remaining piece for full EP-488 is:

Conjecture (Singleton-Extremal): Among all primitive sets with max(A) = M, the worst EP-488 ratio sup_{m>n} G(m)/(2G(n)) is achieved by a one-anchor family.

Verified computationally for max(A) ≤ 16.

Your task: prove the singleton-extremal conjecture, or find a reduction from general primitive sets to one-anchor families.

Possible approaches:
1. MONOTONE SPLITTING: Take a primitive set A with two "anchors" (two small elements). Show that replacing A with a one-anchor family A' that has the same max doesn't decrease the worst ratio. This would reduce to the proved case.

2. DENSITY DOMINANCE: Show that for any primitive set A, there exists a one-anchor family A' with F_{A'}(x) ≥ F_A(x) for all large x AND inf G_{A'} ≤ inf G_A. This would make A' the harder case.

3. LICHTMAN'S APPROACH: Lichtman proved the Erdős primitive set conjecture using L-divisibility chains. His machinery might provide the reduction — the key insight was that "greedy" constructions (maximizing density) have a specific structure.

4. DIRECT: Prove EP-488 for ALL primitive sets directly, without reducing to one-anchor. The discrepancy approach (|F(x) - δ_A x| ≤ C) works for any primitive set — you just need C to be controlled.

Think deep. The one-anchor case took two sessions. This might be easier (it's a structural reduction, not a new proof) or harder (general primitive sets have less structure to exploit).
---


## GPT-5.4 Pro Extended — Structural analysis of general primitive sets

PROMPT:
---
EP-488 is proved for all one-anchor families (attached paper v4). The remaining piece: prove general primitive sets aren't worse.

A primitive set A = {a₁, a₂, ..., a_k} where no element divides another. Define F_A(x) = |{n ≤ x : ∃a ∈ A, a|n}|.

Your structural analysis skills identified the carrier/AP structure and the periodic deviation reduction. Apply the same structural thinking to the generalization.

Key questions:
1. For a multi-anchor set like {6, 10, 15}, what does the density G(x) look like? Does it have the same peak-then-decay structure as one-anchor families?

2. The discrepancy bound |F(x) - δ_A x| ≤ C works for ANY primitive set. What is C as a function of |A| and max(A)? If C is polynomial, the post-peak argument transfers immediately.

3. What about the first plateau? For one-anchor families, G ≥ β on [M, m*) because the Principal-Layer Lemma injects t fresh elements per layer. For general sets, is there an analogous injection argument?

4. Can you find a counterexample to the singleton-extremal conjecture for max(A) > 16? If you can, the reduction approach is dead and we need a direct proof.

Extended thinking ON.
---


## GPT-5.2 Pro Extended — Discrepancy bound for general primitive sets

PROMPT:
---
EP-488 is proved for one-anchor families (paper v4 attached). The post-peak proof uses: |F(x) - δ_A x| ≤ C ⟹ no 5/4-rebound for n > 9C/δ_A.

This argument works for ANY primitive set if we can bound C.

Your task: prove a discrepancy bound C for general primitive sets A.

For a primitive set A with |A| = k elements:
F(x) = Σ_{∅≠S⊆A} (-1)^{|S|+1} ⌊x/lcm(S)⌋

The error h(x) = F(x) - δ_A x = -Σ c_d {x/d} where the sum is over the inclusion-exclusion lattice.

Bound |h(x)| ≤ C where C depends on |A| and max(A).

The naive bound C ≤ 2^|A| is exponential. Can you do better for PRIMITIVE sets (antichain in divisibility lattice)?

Key structural fact for primitive sets: if S ⊆ A with |S| ≥ 2, then lcm(S) > max(A) (because no element divides another, so lcm grows). This means higher-order IE terms have large denominators and contribute little to the error.

Target: C = O(|A|²) or better. If achieved, the post-peak argument (analytic tail + finite verification) extends to all primitive sets.

Also: your fibered FKG bound works for ANY set of moduli, not just consecutive ones. What does it give for general primitive B?

Extended thinking ON.
---


## GPT-5.4 xhigh (Codex) — Computational verification of singleton-extremal

PROMPT:
---
EP-488 is proved for one-anchor families. The remaining question: are one-anchor families the worst case among ALL primitive sets?

Conjecture (Singleton-Extremal): For fixed max(A) = M, the worst EP-488 ratio is achieved by a one-anchor family.

Currently verified for M ≤ 16. Extend this.

For each M from 17 to 50:
1. Enumerate ALL primitive sets A with max(A) = M and |A| ≤ 6
2. For each, compute sup_{m>n≥M} G(m)/(2G(n)) up to horizon 1000M
3. Compare against the worst one-anchor family with the same max
4. Report any primitive set that BEATS the worst one-anchor family

Also: for M ≤ 30, enumerate primitive sets with |A| ≤ 8 (more elements might create worse ratios through density concentration).

Write a Python script, run it, report results. The key output: does ANY multi-element primitive set beat the one-anchor worst case?
---
