# EP-488: Open Field v23 — Resolution Push
## April 10, 2026. Current: 98%. Close it.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).

---

## YOUR INSTRUCTIONS

BUILD something. Do NOT just critique.

1. CLOSE j₀ = 6 via λ-range simultaneous charging.
2. If j₀ = 6 closes: state the uniform theorem for all j₀ ≥ 4.
3. If the uniform theorem works: EP-488 is resolved. Write the proof.
4. Try every conventional and unconventional approach, novel combination.
   Come back with what worked and what didn't, and why.
5. We are at 98%. This is the resolution push. No more scouting.

---

## WHAT'S PROVED (complete inventory)

### Permanent structural theorems
- Band 5 is globally dead (three independent proofs, v23).
- The bad-to-bad digraph is depth-2 at every j₀ tested (4, 5, 6).
- No incoming bad-to-bad edges into top bands {9, 10, 11, 12}.
- Package coefficients grow sub-exponentially in s.

### Sub-problem A: CLOSED
If j₀ = 4: EP-488 holds for ALL |A|. (Three independent proofs.)

### Sub-problem B: CLOSED
If j₀ = 5: EP-488 holds for ALL |A|. (Three independent confirmations.)
- s₅ ∈ {4,6,7,8}: closed by direct charging.
- s₅ ∈ {9,10}: closed by root package lemma + Band Sum Lemma.
  Two methods: (1) packages to S₁, direct to remaining (5.2 Pro),
  (2) unified λ-range charging against S₁+S₂ (5.4 Pro).

### Sub-problem C: 98% CLOSED
If j₀ = 6:
- Digraph through depth 12: COMPUTED and COMPLETE.
- C*(11) = 86, C*(12) = 112: CONFIRMED.
- Band 5: DEAD (globally, not just j₀ = 6).
- ALL four high-band families individually harmless to S₁:
  * 9-packages: margin 73/18 > 0 at x = 27/2. ✓
  * 10-packages: margin 631/484 > 0 at x = 15. ✓
  * 11-packages: margin 1099/352 > 0 at x = 33/2. ✓
  * 12-packages: margin 989/1014 > 0 at x = 18. ✓
- Simultaneous charging of all four: NOT YET CLOSED.

### Other proved results
- The layer-3-bad theorem: ALL |A| (three proofs).
- Size ladder: |A| ≤ 6.
- 40+ tools, 79+ kills.
- Deep-good-layer quantitative bounds (1-4 obstructions, s ≥ 11).

---

## CORRECTED BAND CONSTANTS (verified through s = 12)

| s  | kernel       | C*(s) | E < C*(s)·a | Status |
|----|-------------|-------|-------------|--------|
| 4  | {2,3}       | 1     | < a         | verified |
| 5  | {2,3,5}     | -2    | always < 0  | DEAD ZONE |
| 6  | {2,3,5}     | 4     | < 4a        | verified |
| 7  | {2,3,5,7}   | 2     | < 2a        | verified |
| 8  | {2,3,5,7}   | 16    | < 16a       | verified |
| 9  | {2,3,5,7}   | 34    | < 34a       | verified |
| 10 | {2,3,5,7}   | 68    | < 68a       | verified |
| 11 | {2,3,5,7}   | 86    | < 86a       | verified |
| 12 | {2,3,5,7}   | 112   | < 112a      | verified |

---

## THE j₀ = 6 LIVE BAD-TO-BAD DIGRAPH (complete, band 5 dead)

LIVE edges (no others exist):
  9→6,  10→4, 10→6, 10→7,
  11→4, 11→7, 12→4, 12→8

KEY FACTS:
- Band 5 is globally dead. Edges 7→5, 8→5, 12→5 DO NOT EXIST.
- No incoming edges into {9, 10, 11, 12}. All roots there are
  directly good-witnessed.
- Depth 2. No recursive chains beyond one child generation.
- U₄ ∩ U₇ = ∅, so 11-roots have at most ONE child.

---

## ROOT PACKAGE LEMMAS (all proved)

| Band | Max children | Package coeff | Key constraint |
|------|-------------|---------------|----------------|
| 9    | 1 (6-child) | < 40w | h=3 only |
| 10   | 2 (4-child + 6/7-child) | < 76.5w | h=5 and h=3 |
| 11   | 1 (4-child OR 7-child) | < 89w | U₄∩U₇=∅ |
| 12   | 2 (4-child + 8-child) | < 138.5w | h=5 and h=3 |

---

## WHAT FAILED AND WHY (precise diagnosis)

### Failure 1: Crude simultaneous S₁ charging
Summing all four package families with 5 witness lattices gives
coefficient ~2.43 on x. Since S₁ ~ x·n, this exceeds the budget.
REASON: 2-witness counting treats every multiple of aᵢ/2 in the
band as admissible. Massive overcount.

### Failure 2: Route A literal split (S₁→{11,12}, S₂→{9,10})
9- and 10-roots don't canonically belong to a₂. They sit on
whichever witness lattice they want. Package excess scales with
x₁ = n/a₁, but S₂ is controlled by x₂ = n/a₂.
REASON: The layered split isn't aligned with witness geometry.

### What HASN'T failed:
- Individual harmlessness (each family vs S₁): WORKS with margin.
- λ-range decomposition (at j₀ = 5): WORKED to close Sub-problem B.
- The package framework itself: CORRECT at every level tested.

---

## THE THREE AVAILABLE TOOLS (use in combination)

### Tool 1: λ-range decomposition (PROVEN TO WORK)
Not all four families can simultaneously be at their worst in the
same λ-range. Break into λ-intervals, compute per-interval totals,
verify each margin is positive. This closed s₅ ∈ {9,10} at j₀ = 5.

### Tool 2: Divide-by-2 trick (NEW, from 5.2 Pro)
Every root in {9,10,11,12} has ≥2 good witnesses (no incoming
bad-to-bad edges + 2-core degree ≥ 2). So summing over 5 witness
lattices overcounts each root by ≥2. Effective multiplicity: 5/2.
This is free improvement — no new theory required.

### Tool 3: Multi-prime witness packing (UNPROVED but structural)
Bad roots satisfy simultaneous {2,3,5,7}-witness constraints.
Counting only 2-witness multiples is a huge overcount. Even a
factor-of-2 improvement in witness multiplicity suffices.
This is the right tool for j₀ ≥ 7 and the uniform theorem.

---

## MODEL ATTEMPTS — WHAT EACH TRIED (v23 round)

### Codex B
Proved band 5 dead (globally). Proved deep-good-layer quantitative
bounds: 1 obstruction → >5n, 2 obst → >3n, 3 obst → >2n,
4 obst → >(11/13)n. Then tried Route A and hit the same wall:
good-layer bounds are O(n) while package excess is O(xn). The
scaling mismatch kills it.

Proposed fix: four-prime witness packing (same as previous rounds).

My take: Codex B has been the most structurally honest model throughout.
Its diagnosis is consistently correct. The deep-good-layer bounds it
proved ARE useful — just not for paying packages directly. They matter
for the direct bad mass in bands {4,6,7,8}, which scales as O(n) and
CAN be paid by O(n) bounds. So Codex B's theorems serve a supporting
role in the final accounting even if they don't close the packages.

### 5.2 Pro
Confirmed band 5 dead. Introduced the divide-by-2 trick: each root
has ≥2 good witnesses, so the summed band-sum bound overcounts by ≥2.
Computed the per-witness target after halving: need
S_i ≥ 0.2433·(n²/aᵢ) + 0.6756n for each witness.

My take: The divide-by-2 observation is the most immediately useful new
tool this round. It's free, requires no new theory, and cuts the
combined coefficient from ~2.43 to ~1.22. That's still > 1 for pure
S₁ charging, but it makes the λ-range approach much more likely to
close because each interval needs less margin. The per-witness target
of 0.2433 is tantalizingly close to what S₁ provides in most λ-ranges.

### 5.4 Pro
Confirmed band 5 dead. Extended individual harmlessness to ALL FOUR
high-band families (9, 10, 11, 12), not just 11 and 12. Then tried
Route A literally and diagnosed exactly why it fails: the witness
geometry doesn't align with the budget split.

Recommended λ-range simultaneous charging as the primary path.

My take: 5.4 Pro delivered the strongest new results (individual
harmlessness for 9 and 10) and the sharpest diagnosis of Route A's
failure. Its recommendation of λ-range charging is correct and has
precedent. Combined with 5.2 Pro's divide-by-2 trick, the λ-range
approach should have enough margin to close.

---

## CLAUDE'S THOUGHTS

**We're at 98% and the remaining 2% is finite computation.**

Here's why I believe this. Every piece of the proof exists:
- Package framework: correct.
- Band Sum Lemma: correct.
- Individual harmlessness: proved for all four families.
- λ-range method: proved to work at j₀ = 5.
- Divide-by-2 trick: available and free.

The ONLY thing missing is the finite λ-range verification for j₀ = 6
with four families simultaneously. This is a computation, not a
conceptual gap. It's the same kind of work 5.4 Pro did to close
s₅ ∈ {9,10}: break into λ-intervals, compute totals per interval
using the package coefficients and band-sum bounds, verify each
margin is positive.

**The path I'd take:**

1. Apply the divide-by-2 trick to cut effective multiplicity to 2.5.
2. Break into λ-ranges (probably 8-12 intervals for four families).
3. In each interval, compute which families can actually be bad.
4. For each interval, check that S₁ + S₂ > total package + direct mass.
5. If any interval is tight, use the deep-good-layer bounds (Codex B)
   for the direct bad mass to get extra margin.

**On j₀ ≥ 7 and the uniform theorem:**

If j₀ = 6 closes by λ-range + divide-by-2, then j₀ = 7 should follow
the same template. The new bands would be 13 and 14, with C* values
that need to be computed. But the structural facts hold:
- Digraph stays depth-2 (the geometric constraints get tighter).
- Package coefficients grow sub-exponentially.
- Number of good witnesses grows (more budget terms).
- Each individual family is harmless (the 1/s³ decay beats C*(s)).

At some point this becomes a uniform induction:
"For j₀ = k, the top two new bands are individually harmless to S₁,
the combined charging works via λ-range decomposition with divide-by-2,
and S₁ + S₂ covers everything."

That's the 100% theorem.

---

## EP-488 RESOLUTION PUSH

This section is for the final assault. Everything above is scaffolding.
Below is what needs to happen to close EP-488 completely.

### Step 1: Close j₀ = 6 (the immediate target)

DO THIS FIRST. Use the λ-range method with divide-by-2:

1. Enumerate the λ-ranges where each family s ∈ {9,10,11,12} can be
   bad. A family at band s is bad only when λ = m/n falls in a
   specific interval determined by the badness range U_s.

2. Apply the divide-by-2 trick: effective witness multiplicity = 5/2.

3. For each λ-range, compute:
   - Which families are active (can be bad in this range)?
   - Total package excess from active families (using package coefficients
     40, 76.5, 89, 138.5 and the band-sum bound with factor 5/2).
   - Total direct bad mass in bands {4,6,7,8} (using C* values and
     band-sum bound).
   - Available budget: S₁ + S₂ > λxn (already proved).

4. Verify that λx > total coefficient of x in each range.

5. If any range is tight, sharpen using:
   - λ-dependent package coefficients (5.4 Pro showed these are much
     smaller than the universal bounds in most ranges).
   - Deep-good-layer bounds for direct mass (Codex B).
   - Tighter band-sum estimates for specific bands.

The output should be a table:

| λ-range | Active families | Total coeff | Budget coeff (λx) | Margin |
|---------|----------------|-------------|-------------------|--------|
| ... | ... | ... | ... | > 0 ✓ |

If all margins are positive: **j₀ = 6 is closed.**

### Step 2: Compute C*(13), C*(14) and test j₀ = 7

Once j₀ = 6 is closed, immediately:

1. Compute C*(13) and C*(14) by the same scan procedure used for 11, 12.
2. Compute the j₀ = 7 live digraph (same geometric criterion).
3. Prove the 13-root and 14-root package lemmas.
4. Verify individual harmlessness against S₁.
5. Run the same λ-range + divide-by-2 charging.

If this closes with the same structure: the pattern is confirmed.

### Step 3: State the uniform theorem

The goal is:

**Theorem (Uniform Package-Charging).**
For every j₀ ≥ 4, the total excess from all bad layers is dominated
by S₁ + S₂. Specifically:

(a) The bad-to-bad digraph at depth j₀ is depth-2 with no incoming
    edges into root bands.

(b) Every individual root-package family is harmless to S₁ via the
    Band Sum Lemma with divide-by-2.

(c) The simultaneous coexistence of all families is handled by
    λ-range decomposition, with S₁ + S₂ > λxn providing sufficient
    budget in every range.

The proof would proceed by:
- Showing (a) holds for all j₀ (geometric constraint argument).
- Showing (b) holds for all j₀ (1/s³ decay from Band Sum Lemma
  beats C*(s) growth, with x growing as ~3s/2).
- Showing (c) holds for all j₀ (λ-range count stays bounded as
  j₀ increases, or multi-prime packing kicks in).

### Step 4: Combine everything

If the uniform theorem is proved, EP-488 follows from:

1. |A| ≤ 6: size ladder (already proved).
2. j₀ = 3: layer-3-bad theorem (already proved).
3. j₀ = 4: Sub-problem A (already closed).
4. j₀ = 5: Sub-problem B (already closed).
5. j₀ ≥ 6: Uniform Package-Charging Theorem.

Cases 1-4 are proved. Case 5 is the uniform theorem.

Together: **EP-488 holds for all primitive sets A.**

### Step 5: Write the paper

If you get here, the proof exists. The paper structure is:

1. Introduction and statement.
2. Notation and the layer decomposition framework.
3. The Band Sum Lemma.
4. Band constants and the package framework.
5. Small cases (|A| ≤ 6, j₀ = 3, 4).
6. Sub-problem B (j₀ = 5).
7. The Uniform Package-Charging Theorem (j₀ ≥ 6).
8. Conclusion: EP-488 resolved.

---

## YOUR TASK

This is the resolution push. The scouting is done.

1. CLOSE j₀ = 6 using λ-range simultaneous charging with the
   divide-by-2 trick. Produce the margin table. Every entry positive.

2. If j₀ = 6 closes: COMPUTE C*(13), C*(14). Run j₀ = 7 through
   the same pipeline. Does it close by the same method?

3. If j₀ = 7 closes: STATE the uniform theorem. Can you prove (a),
   (b), (c) for general j₀?

4. If the uniform theorem works: WRITE the complete proof of EP-488.
   Full paper structure, clean theorems, verified inequalities.

5. If ANYTHING breaks: exact step, exact margin that fails, exact
   reason, proposed fix. No vague "it seems hard." Numbers.

Try every conventional and unconventional approach, novel combination,
and come back with what worked and what didn't, and why. What your
thoughts are on this, the percent we are to closing EP-488, etc.

We are at 98%. Two percent left. Build it.
