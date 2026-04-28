# EP-488: Open Field v18 — April 9, 2026
## Current: 91%. Build the remaining 9%.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## YOUR INSTRUCTIONS (read carefully)

This is NOT a grading exercise. Do NOT just find errors and report them.

**Your job is to ATTEMPT a proof.** Specifically:

1. **TRY something.** Pick the approach you think is most promising and
   push it as far as you can. Write out every step. If it works, you've
   contributed a theorem. If it fails, explain EXACTLY where and why.

2. **Diagnose the failure.** If your attempt breaks, identify:
   - The exact step that fails
   - A concrete counterexample or logical gap
   - WHY this step seemed like it should work but doesn't
   - What structural feature of the problem causes the failure

3. **Prescribe the fix.** After diagnosing, propose:
   - What modification would repair the broken step
   - What NEW lemma would be needed to make it work
   - Whether the failure is fundamental or fixable

4. **Recommend next steps.** Tell us:
   - What you would tell yourself if you could restart with this knowledge
   - What the single most valuable next theorem to prove would be
   - How the remaining 9% breaks down into concrete sub-problems

5. **Break down the 9%.** Decompose the remaining gap into a numbered
   list of specific, provable statements that COLLECTIVELY would
   constitute a complete proof. For each statement, estimate its
   difficulty and identify which existing tools are relevant.

Do NOT just say "the proof needs more work" or "the constants are wrong."
BUILD something. If you can't build the whole thing, build a piece and
explain what's missing.

---

## WHAT'S PROVED (the 91%)

### Size Ladder:
- |A| ≤ 6: PROVED

### Infinite Branch:
- Layer 3 bad → EP-488 holds for ALL |A| (three independent proofs)

### Key Tools:
- Self-funding: s ≤ 3 → safe
- Single-obstruction safety: ≤ 1 obstruction → safe
- Deep single-obstruction surplus: s ≥ 5, 1 obstruction → budget > 2m
- First-layer theorem: s ≥ 4 + quotient-2 → S₁ > E_j each
- Witness-count bound: frozen layer j needs π(s_j) ≤ j-1
- Signature rigidity: s=4 → (4,7,3) only. s=5 → DEAD.
- Layer-3-bad witness-group charging (ALL |A|)
- Packing: multiples of d in band → count ≤ band_length/d + 1
- Superadditivity / separator / leaf-pruning / all graph tools
- Literal-2 safety, lifted safety theorems
- H₁ main term: nH₁(m) < 2mH₁(n)
- Divisibility monotonicity: T(d) ≥ T(kd)

### CORRECTED Band Constants (t ≤ 10(s+1), computationally verified):

| s  | kernel           | C*(s) | E bound per layer |
|----|-----------------|-------|-------------------|
| 4  | {2,3}           | 1     | < a ≈ n/4         |
| 5  | {2,3,5}         | -2    | DEAD ZONE         |
| 6  | {2,3,5}         | 4     | < 4a ≈ 2n/3       |
| 7  | {2,3,5,7}       | 2     | < 2a ≈ 2n/7       |
| 8  | {2,3,5,7}       | 16    | < 16a ≈ 2n        |
| 9  | {2,3,5,7}       | 34    | < 34a ≈ 3.8n      |
| 10 | {2,3,5,7}       | 68    | < 68a ≈ 6.8n      |
| 11 | {2,3,5,7,11}    | 86    | < 86a ≈ 7.8n      |
| 12 | {2,3,5,7,11}    | 112   | < 112a ≈ 9.3n     |

Live depths: ALL s ≥ 4 except s = 5. Odd depths s = 7,9,11 are LIVE.

### 79 Kills (compressed):
Every structural shortcut is dead. No per-layer bounds, no kernel
comparisons, no monotone reductions, no gcd reductions, no compact
extrapolation. The proof must be collective and direct.

---

## THE REMAINING 9%: A DECOMPOSITION

Here is how I believe the 9% breaks down. Critique this decomposition
and improve it if you disagree.

### Sub-problem A (≈3%): Prove EP-488 when first bad layer j₀ = 4

Layer 3 good, layer 4 is the first bad layer.
Witness-count: π(s₄) ≤ 3, so s₄ ≤ 6. Dead zone kills s=5.
So s₄ ∈ {4, 6}.

This is the SIMPLEST remaining case. Only two possible depths.
Tools: first-layer theorem, single-obstruction safety, packing bounds.

Sub-case s₄=4: all bad layers locked into (4,7,3). Total excess
< (k-2)(3n-2m). Need S₁ (+ S₂) to dominate. The layer-3-bad proof
handles this when layer 3 is bad — can it be adapted when layer 3 is good?

Sub-case s₄=6: E < 4a ≤ 2n/3 per layer. Fewer bad layers possible.

### Sub-problem B (≈3%): Prove EP-488 when first bad layer j₀ = 5

Layer 3,4 good, layer 5 is first bad.
Witness-count: π(s₅) ≤ 4, so s₅ ≤ 10. Dead zone kills s=5.
So s₅ ∈ {4, 6, 7, 8, 9, 10}.

More bands, larger C* values. But also more good layers (1,2,3,4).
The packing bounds and witness-group charging should work.

### Sub-problem C (≈2%): Prove EP-488 when first bad layer j₀ ≥ 6

Generalize A and B. The pattern: as j₀ grows, more bands become
available (s up to p_{j₀}-1), but also more good layers exist below.
The self-regulation mechanism: more bad layers → more witnesses needed
→ witnesses forced smaller → surplus grows.

### Sub-problem D (≈1%): Unify A/B/C into a single theorem

The final step: prove that the witness-group charging (or Surplus
Dominance, or some other mechanism) works uniformly for ALL j₀,
ALL |A|. This might follow from a single "master inequality" that
compares packing density against surplus growth.

---

## WHAT THE LAYER-3-BAD PROOF ACTUALLY DID (for reference)

The layer-3-bad proof (proved by three models) works like this:

1. All bad layers at (4,7,3): excess E = 3n-2m < n per layer.
2. 2-witnesses must be a₁ or a₂ (at most 2 groups).
3. Packing: B ≤ n/(10a₁) + n/(10a₂) + 2 < n/(5a₁) + 2.
4. S₁ ≥ m(n/a₁ - 2) ≥ λn(n/a₁ - 2).
5. Since B < n/a₁ - 2 and E < n: total excess < nB < n(n/a₁ - 2) < S₁.

The KEY step was: packing bounds B relative to n/a₁, and S₁ is
proportional to n/a₁ times m. Since m > n, S₁ > n·B > B·E.

### Why doesn't this immediately generalize?

When layer 3 is GOOD and first bad is j₀ ≥ 4:
- Bad layers might have s ≠ 4 (s = 6, 7, 8, ...) with larger C*.
- The excess per layer E < C*(s)·a might exceed n.
- The 2-witnesses might include a₃, a₄, ... (more than 2 groups).
- The packing bound per witness depends on the band width n/(s(s+1)).

BUT the self-regulation still works: each bad layer needs π(s) witnesses,
and each witness's surplus is proportional to n/aᵢ. The question is
whether the proportionality constants work out.

---

## CLAUDE'S THOUGHTS

I want to be direct about what I think the proof looks like.

The layer-3-bad proof succeeded because of ONE clean inequality:
  B < n/a₁ AND E < n AND S₁ > n·(n/a₁) → S₁ > B·E.

The general proof needs a similar clean inequality that works for
ALL bands simultaneously. Here's my best attempt at formulating it:

**For each bad layer j at depth s_j:**
- E_j < C*(s_j) · a_j where C*(s) is the band constant
- a_j > n/(s_j + 1) (from depth definition)
- So E_j < C*(s_j) · n/(s_j) (roughly)

**Each bad layer j has a 2-witness w_j with w_j ≤ 2a_j/3:**
- w_j creates a "charge" on the witness: E_j charged to S_{w_j}
- Each witness w can receive charges from at most n/(s·(s+1)·d_w) + 1
  bad layers in the depth-s band, where d_w = w/2

**The witness's surplus:**
- If w has ≤ 1 obstruction (which is true for w = a₁ or a₂):
  S_w ≈ mn/w (roughly)

**The charge-to-surplus ratio per witness:**
For bad layers in band s charged to witness w:
  Total charge ≤ (n/(s(s+1)d_w) + 1) · C*(s) · n/s
  Surplus ≈ mn/w = 2md_w

  Ratio ≈ 2md_w / ((n/(s²d_w)) · C*(s)n/s)
        = 2ms²sd_w² / (C*(s)n²)

  For d_w ≈ w/2, w ≈ a₁ ≈ n/(big number): this ratio depends on
  the specific values. It's NOT obviously > 1 in general.

So the simple "charge each bad layer to its 2-witness" might not work
with a single witness type. The proof might need to use ALL the
witnesses (2-witness, 3-witness, 5-witness, 7-witness) and their
combined surplus to cover the bad layer's excess.

**Alternative: Surplus Dominance directly.**
Prove 2mH_A(n) ≥ nH_A(m) without going through layer analysis.
The H₁ main term is proved. The IE correction is the gap.
Properties of primitive sets (Σ 1/(a log a) < ∞) haven't been used.
Maybe the IE correction is bounded by the Erdős density bound.

I genuinely don't know which path closes it. But the 9% is real
work, not cleanup. The models need to BUILD, not just critique.

---

## YOUR TASK

1. ATTEMPT a proof of Sub-problem A (j₀ = 4, the simplest remaining case).
2. Push it as far as you can.
3. If it breaks, diagnose WHERE and WHY.
4. Prescribe the fix.
5. Recommend what to do next.
6. Break down whatever remains into concrete sub-problems.

If you can close Sub-problem A completely: we're at 94%.
If you can close A and B: we're at 97%.
If you can close all of A/B/C/D: EP-488 is solved.

Build something. 79 kills tell you what NOT to do.
40+ results tell you what tools you HAVE.
The corrected band table tells you the exact constants.

Go.
