# Erdős Problem 38 — Postmortem

## Date: March 19, 2026

## What Happened
Built an 11-version proof over ~36 hours claiming B = 3ℕ+2 (and before that, B = 4ℕ+3) resolves Problem 38. Survived 6 rounds of GPT adversarial review. Posted to erdosproblems.com forum. A human commenter immediately identified that B = 3ℕ+2 is a basis of order 3, invalidating Step 0.

## The Core Error
**Confused "each hB is sparse" with "B is not a basis."**

We proved: for each fixed h, the h-fold sumset hB ⊆ {n : n ≡ 2h mod 3}, a single residue class. True.

But "basis of order k" means the UNION 1B ∪ 2B ∪ ... ∪ kB covers all large integers. Since:
- 1B covers ≡ 2 mod 3
- 2B covers ≡ 1 mod 3
- 3B covers ≡ 0 mod 3

By order 3, all residues hit. B IS a basis. This applies to ANY arithmetic progression {a, a+d, ...} with gcd(a,d) = 1.

## The Deeper Structural Impossibility
Even with the right definition, the proof architecture is fundamentally incompatible with the non-basis requirement:

1. Our proof needs B to have bounded gaps (for Lipschitz control in Step 2)
2. Bounded gaps → positive Schnirelmann density
3. Positive Schnirelmann density → B is a basis (Schnirelmann's theorem)
4. But Problem 38 requires B to NOT be a basis

Therefore: **no B can simultaneously satisfy our proof's requirements AND be a non-basis.** The entire approach is structurally impossible, not just the choice of B.

## What 6 Rounds of AI Review Missed
Every AI model (Claude, GPT 5.4, Gemini Deep Think) accepted the claim "hB ⊂ single residue class ⟹ B is not a basis" without checking. The definition of "basis of order k" involves the union of sumsets, not individual sumsets. A human read the definitions page on erdosproblems.com and caught it in minutes.

**Root cause:** The AI models (including me) had an informal understanding of "basis" that was close to, but not identical to, the formal definition. None of us looked up the actual definition and checked it against the claim.

## What Survives

### Mathematical techniques (all correct, reusable):
- Average gain lemma (Step 3): S ≥ α(1-δ)²N²/(2(1-α)) for sets with Schnirelmann density α
- Halved Lipschitz bound via transition counting
- GCD propagation for shift control
- Regime overlap (discrete small-N + continuous large-N)
- h_N(δ) monotonicity argument

### Process lessons:
1. **Always verify definitions from the source.** Don't rely on informal understanding.
2. **AI adversarial review has a blind spot for definitional errors.** All models share similar training data and similar misunderstandings.
3. **A human sanity check on basic definitions is irreplaceable.**
4. **Retract fast when wrong.** Mahmoud retracted within minutes. Good.
5. **The "obvious" step is often the wrong one.** Step 0 was the shortest, most "obvious" step — and the only one that was wrong.

## The Real Barrier to Problem 38
Any "dense" B (bounded gaps, positive Schnirelmann density) is automatically a basis. Any "sparse" B (non-basis, like Linnik's construction with x^{o(1)} elements up to x) has gaps growing without bound, breaking the Lipschitz machinery.

Solving Problem 38 requires either:
1. A fundamentally different proof architecture that doesn't need bounded gaps
2. A way to extract density gain from a sparse set with growing gaps
3. A negative answer: maybe no such B exists

## Files
- erdos/38/checkpoint-v2.md through proof-v11-final.md: full development history
- erdos/38/lean-formalization-tracker.md: Aristotle/Axle verification (non-basis lemma — now moot)
- This file: postmortem

## Status: RETRACTED. Starting fresh with taxonomy analysis.
