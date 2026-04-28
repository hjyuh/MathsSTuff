# EP-488: 5.2 Pro — Window Lemma (Thin Prime Window Charging)
## April 7, 2026

## THE KEY INSIGHT

You don't need the FULL ancestor web. You only need a THIN WINDOW
of ancestors near the prime threshold y where obstructions are minimal.

## THE WINDOW LEMMA (informal)

For primes p ∈ [y, y^{1+ε}] (tiny window near threshold):
- Obstruction set for 2p is {primes q : y ≤ q < p} — very thin
- Mertens product: Π(1-1/q) ≈ log y / log p ≥ 1/(1+ε)
- So L_{2p}(x) ≥ c_ε · x where c_ε > 1/2 for small ε
- Each ancestor 2p has slack S_{2p} ≥ (c_ε - 1/2) · mn/p
- Sum over window: Σ_{p∈P} 1/p ≈ log(1+ε) = O(1)
- Total window slack ≈ C_ε · M² (CONSTANT, independent of y)

Meanwhile: total bad excess ≈ M²/log y → 0.

So the thin window alone pays for the entire swarm.

## WHY THIS WORKS WHERE OTHER APPROACHES FAILED

1. NO kernel comparisons (Category G safe): only uses prime obstructions
   where the sieve IS multiplicative — no parent/child kernel comparison

2. NO intermediate bounds (Category H safe): directly computes L_{2p}
   using sieve density, no inflation

3. NO S_1 alone (Category I safe): uses MANY ancestors in the window,
   not just the first layer

4. NO full ancestor web needed: only the thin window near y, where
   inter-ancestor obstructions are provably thin

5. CORRECT L_j definition (Kill #48 safe): divisibility avoidance
   specializes to "avoid multiples of primes" when obstructions ARE primes

## TRANSFERABILITY

This isn't swarm-specific. The charging primitive is:

"In ANY primitive set with bad layers governed by prime threshold y,
extract the thin window [y, y^{1+ε}] of ancestor primes. These
ancestors have quasi-linear L (density ≥ c_ε), hence first-layer-like
slack. Their combined slack is O(M²), dominating the O(M²/log y) bad
excess."

This works for general primitive sets IF:
(a) bad layers require ancestors with prime quotients ≥ y
(b) the thin window contains enough primes (PNT: yes)
(c) the obstruction density in the window is bounded (Mertens: yes)

## WHAT REMAINS

1. Formalize the Window Lemma with explicit constants
   (Rosser-Schoenfeld style bounds for Mertens products)
2. Prove the "general extraction lemma": from any primitive set with
   bad layers, extract a thin ancestor window where this charging works
3. Handle edge cases where the ancestor window might not exist
   (e.g., if the set doesn't have enough prime-factored ancestors)
4. Verify for small M (computational, already done for M ≤ 20)

## CONSISTENCY WITH CODEX B'S CORRECTION

5.2's approach gives total window slack ≈ C_ε · M² (constant).
This is CONSISTENT with Codex B's correction (total slack ~ M², not M² log y).
The thin window captures the bulk of the useful slack in a constant-order sum.

## KILL COUNT: 69
## PERCENTAGE: 85%

Jump from 84%. The Window Lemma is the most technically precise and
transferable result of the round. It identifies the exact mechanism
(thin window of low-obstruction ancestors) and explains WHY it
survives all kills. The formalization path is clear.
