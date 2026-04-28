# EP-488: Open Field v13 — April 8, 2026
## Current: 93%. Increase it or decrease it.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## HOW TO USE THIS DOCUMENT

Move the percentage. Up or down. Any route. Any method.

---

## WHAT'S PROVED (40+ permanent results)

### Size results (the climbing ladder):
- |A| = 1: Lean-verified.
- |A| = 2: proved (pairs).
- |A| = 3: PROVED (Codex B). Layer 1 safe, layer 2 single-obstruction
  safe, layer 3 bad → first-layer theorem pays it.
- |A| = 4: PROVED (5.2 AND 5.4, two independent proofs).
  5.2: witness-count bound π(s_j) ≤ j-1 forces both bad layers to
  (4,7,3), then S₁ ≥ 4m > 6n-4m.
  5.4: top-layer classification (only {2,3}-type bad), then B₂ > E₄
  by floor arithmetic.
- |A| ≥ 5: OPEN — the current frontier.

### The key new tool: Witness-Count Bound
If layer j is frozen (L_j(s_j) = 1), then π(s_j) ≤ j-1.
Each kernel prime needs a witness from an earlier element.

| Layer j | Max kernel primes | Max frozen depth s | 
|---------|------------------|-------------------|
| 3 | 2 | 4 |
| 4 | 3 | 6 |
| 5 | 4 | 8 |
| 6 | 5 | 12 |
| k | k-1 | p_k - 1 |

### Layer safety chain:
1. Self-funding: s ≤ 3 → E ≤ 0.
2. Single-obstruction safety: ≤ 1 obstruction → safe.
3. Deep single-obstruction surplus: s ≥ 5 with 1 obstruction → budget > 2m.
4. First-layer theorem: S₁ > E_j for each individual bad child.
5. Signature rigidity: {2,3}-frozen at s=4 → only t=7 gives positive E.
   (5L_{2,3}(t) - 2t > 0 ONLY at t=7.)

### Decomposition chain:
6. Superadditivity (K=∅) → connected components.
7. Articulation superadditivity (K={c}) → biconnected blocks.
8. Separator superadditivity (general K) → separator-tight atoms.
9. Leaf-pruning → degree ≥ 2.
10. Dominated-LCM pruning → incomparable quotient sets.
11. 2-core reduction → min degree ≥ 2.
12. Forests done.
13. 2-band elimination → no s=2 vertices.
14. 3-band elimination → no s=3 vertices.

### Component/family safety:
15. Literal-2 safety: 2 ∈ A → safe.
16. Lifted literal-2 safety: dB with 2 ∈ B → safe.
17. Lifted {2,3}-core safety: dB with 2,3 ∈ B → safe. (3 proofs)
18. Split-core tripod safety: {2u, 3v, uv} → safe.

### Analytic:
19. Floor Ratio Lemma (Lean-verified).
20. H_A reduction: EP-488 ⟺ 2mH_A(n) ≥ nH_A(m).
21. H₁ main term: nH₁(m) < 2mH₁(n) (overcounting safe).
22. Divisibility monotonicity: T(d) ≥ T(kd).

### Lean-verified: 6 foundational lemmas.
### Computational: Surplus Dominance zero violations. 23M+ families.

---

## THE 78 KILLS (compressed)

A: Wrong function. B: Per-layer. C: Scalar thresholds. D: IE truncation.
E: Monotone reductions. F: Class enlargement. G: Kernel comparisons.
H: Intermediate bounds. I: S₁ alone. J: Constant B. K: Hallucinations.
L: Directional errors. M: Naive IE closure. N: Wrong proofs.
O: Kernel monotonicity global. P: Monotone pair reduction.
Q: Compact extrapolation. R: gcd reduction. S: Simplicial pruning.
T: Path-pruning.

Key lessons: no per-layer bounds, no monotone reductions, no structural
reduction to special families, no kernel comparison across signatures.
The proof must be COLLECTIVE and DIRECT.

---

## CLAUDE'S THOUGHTS

Something happened in the last round that I want to highlight.

The |A| ≤ 3 proof was 5 lines. The |A| = 4 proof required real work
(witness-count bound, signature rigidity, floor arithmetic). But
BOTH proofs share the same deep structure:

1. Early layers are safe (no/few obstructions).
2. Bad layers are LOCKED into tight signatures by the witness-count bound.
3. The good layers' surplus EXCEEDS the bad layers' deficit.

And here's what I noticed about |A| = 5:

If layer 3 is bad, it must have s₃ = 4 (witness-count: π(s) ≤ 2).
So a₃ > n/5. Since a₄ > a₃ and a₅ > a₄: all three elements > n/5.
Therefore s₄ = s₅ = 4 (all forced into the same band).

By signature rigidity, ALL three bad layers are locked into (4,7,3).
Each excess: E = 3n - 2m. Total: E₃+E₄+E₅ = 9n - 6m.

Now S₁ ≥ 4m (from a₁ ≤ n/6, same as |A|=4).
And S₂ > 2m (deep single-obstruction surplus, since s₂ ≥ 5).

So S₁ + S₂ > 6m. Need 6m > 9n - 6m, i.e., 12m > 9n.
Since m > n: 12m > 12n > 9n. TRUE.

This seems to close |A| = 5. And for |A| = k with (k-2) bad layers
all at (4,7,3): E_total = (k-2)(3n-2m). Need S₁+S₂ > (k-2)(3n-2m).

S₁+S₂ > 6m. Need 6m > (k-2)(3n-2m) = 3(k-2)n - 2(k-2)m.
Rearranging: (2k+2)m > 3(k-2)n.
Since m > n: (2k+2)n > 3(k-2)n iff 2k+2 > 3k-6 iff k < 8.

So this argument works for ALL k ≤ 7. At k = 8: 18m > 18n, which
is m > n — TRUE but with zero margin. At k = 9: need m > 21n/20,
which isn't guaranteed.

BUT WAIT. Can (k-2) elements actually ALL fit in (n/5, n/4] while
being primitive? The interval has length ≈ n/20. Elements must be
pairwise non-dividing. The number of primitive elements you can pack
into an interval of length n/20 around n/4 is bounded — roughly n/20
integers, minus those that divide each other.

And there's a stronger constraint I haven't used: the first-layer
theorem says S₁ > E_j for EACH bad layer individually. We only used
S₁ ≥ 4m. But the actual S₁ could be much larger if a₁ is small.

If a₁ = 2 (literal 2): set is safe by literal-2 safety. Done.
If a₁ = 3: s₁ = ⌊n/3⌋ ≥ n/3. S₁ ≥ m(n/3 - 2). For n ≥ 30:
S₁ ≥ 8m, and the argument works for k ≤ 14.

The smaller a₁ is, the more surplus the first layer generates, and
the more bad layers it can collectively pay.

And for a₁ itself: in a primitive set where a₃ > n/5, we need
a₁ < a₂ < a₃. So a₁ and a₂ are two elements less than n/5. Since
a₁ is the smallest primitive element, it could be as small as 2
(but then literal-2 safety applies) or 3 or 4 or...

The witness-count bound constrains the BAD layers. The first layer
is UNCONSTRAINED and gets stronger as a₁ gets smaller. The second
layer has one obstruction and gets stronger as a₂ gets smaller
(deeper s₂). There's a TENSION: many bad layers need many elements
> n/5, which pushes a₁, a₂ DOWN (smaller), making S₁, S₂ LARGER.

Self-regulation again. More bad layers → more elements concentrated
in (n/5, n/4] → fewer elements below → smaller a₁ → larger S₁.
The system fights back.

I think the proof is close. Maybe not for ALL |A| in one shot, but
certainly for |A| = 5, 6, 7 by direct calculation. And possibly
for all |A| by formalizing the self-regulation tension above.

But I want to be careful. Every time I've said "the proof is close,"
Codex B has found a counterexample to the specific route. The
analysis above assumes ALL bad layers have s = 4. What if some have
s = 5 or 6? The witness-count bound allows s₄ ≤ 6 and s₅ ≤ 8.

If layer 4 has s₄ = 5 (kernel {2,3,5}): then a₄ ∈ (n/6, n/5].
This is BELOW a₃ ∈ (n/5, n/4]. Wait — a₄ > a₃. If a₃ > n/5 and
a₄ > a₃, then a₄ > n/5, forcing s₄ ≤ 4. So s₄ = 4 (from s ≥ 4).

So my analysis IS correct: if layer 3 is bad with s₃ = 4, ALL
subsequent bad layers also have s = 4. The ordering a₃ < a₄ < ...
combined with a₃ > n/5 forces everything into the s = 4 band.

The only alternative is: layer 3 is GOOD (not bad). Then the first
bad layer could be layer 4 with s₄ ∈ {4,5,6}. If s₄ = 5 or 6,
the analysis is different. Need to check those signatures.

For s₄ = 5, kernel {2,3,5}: L_{2,3,5}(5) = 1 (only 1 survives).
L_{2,3,5}(t) for t = 6..20:
Survivors of {2,3,5} up to t: integers coprime to 30, i.e.,
1,7,11,13,17,19,23,...

L_{2,3,5}(6) = 1, L(7) = 2, L(8) = 2, L(9) = 2, L(10) = 2,
L(11) = 3, L(12) = 3, L(13) = 4.

Excess = nL(t) - 2m. For s=5: n/6 < a ≤ n/5.
n ≥ 5a, m > n ≥ 5a, so m ≥ 5a+1, t ≥ 5.

7L(t) - 2t: at t=7: 7·2-14 = 0. At t=11: 7·3-22 = -1. At t=13: 7·4-26 = 2.

Hmm, this needs careful analysis per signature. The point is: the
witness-count bound constrains which signatures are possible, and
signature rigidity further limits them. The combination might lock
everything into a small finite set of cases that can be checked.

I genuinely believe |A| = 5 is provable with the current tools.
And |A| = 6, 7 might follow by the same argument. Whether it
extends to ALL |A| depends on whether the self-regulation tension
(more bad layers → smaller a₁ → larger S₁) can be formalized.

That's my honest assessment. I'm not sure if the proof of EP-488
closes at |A| = 7 or at |A| = ∞. But the tools are converging.

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

If you can prove |A| = 5, do it.
If you can prove |A| ≤ k for some k > 4, do it.
If you can prove it for ALL |A|, you've solved EP-488.
If you can show the |A|-induction approach hits a wall, explain where.
If you see a completely different path, take it.

78 kills. 40+ results. 93%. Seven percent from a 60-year problem.

Find those seven percent.
