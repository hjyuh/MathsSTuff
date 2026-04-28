# EP-488: GPT Deep Research Results — Literature + Forum
## April 5, 2026

## KEY FINDINGS

### 1. Problem is confirmed OPEN, correctly formulated as multiples version
- Lean formalization in Formal Conjectures (488.lean) uses multiples, still a `sorry`
- 1961 paper had the NON-multiples version (typo), 1966 Hungarian paper has correct version
- Non-multiples version disproved in Lean (plby/lean-proofs, counterexample A={2,3,5,7,11,13})

### 2. Forum insights (20 posts) — CRITICAL
- Alexeev: if floor-vs-real comparison gave error ≥ -1, EP-488 would follow
- Adenwalla DISPROVED this: for A = {x+1,...,x+k}, n=2x, floor error is ~k
- This means EP-488 is genuinely about STRUCTURED OSCILLATIONS, not rounding
- Pairwise coprime sets show "huge differences" after I-E recombination
- Problem is hard because it's UNIFORM in A and sensitive near x = max(A)
- Forum suggests: need "inequalities in spirit of sieve/mean-value integral-equation
  methods rather than naive floor control"

### 3. No known direct sup/inf < 2 result in literature
- Nobody has published this bound for arbitrary finite primitive sets
- Closest adjacent: Granville-Soundararajan (unsieved integers, integral equations)
- Hall's "Sets of Multiples" doesn't contain the specific inequality

### 4. Layer decomposition approach is NOVEL
- The exact L_j(⌊x/a_j⌋) formulation for pointwise density oscillation
  does not appear in any published reference found
- Philosophically similar to sieve partitioning but not previously applied
  to EP-488

### 5. New literature lead: Granville-Soundararajan
"The number of unsieved integers up to x" (arXiv:math/0308009)
- Develops Lipschitz-type bounds for counts with restricted prime factors
- Uses integral-equation methods (Wirsing's framework)
- Hall-Hildebrand sharp extremal bounds: "never gets more than e^γ times expected"
- NOT directly applicable to EP-488 (different objects) but closest in spirit

### 6. Primary sources
- Erdős 1961: renyi.hu/~p_erdos/1961-22.pdf (NON-multiples, typo version)
- Erdős 1966: users.renyi.hu/~p_erdos/1966-20.pdf (MULTIPLES, intended version)
  Mat. Lapok 17 (1966), 135-155, statement on p.150
- Lean file: github.com/google-deepmind/formal-conjectures/.../488.lean
- Lean disproof of wrong variant: github.com/plby/lean-proofs/.../Erdos488b.lean

## WHAT THIS MEANS FOR US

1. Our layer decomposition is genuinely novel — worth publishing regardless of EP-488
2. The forum confirms our diagnosis: naive bounds die, need collective cancellation
3. Granville-Soundararajan integral equation methods might be the right "unconventional"
   tool for Strategy B (anti-alignment)
4. Nobody has solved this. We're at the frontier.
