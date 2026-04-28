# EP-488: Kill #64 — Uniqueness Conjecture FALSE (two independent counterexamples)
## April 7, 2026

## COUNTEREXAMPLE 1 (5.4 Pro — simpler)

A = {6, 8, 9, 20, 21}, n = 99, m = 147, M = 21

Layer a=20: B = {3, 2, 9}, active kernel {2,3}
  s=4, t=7, L(4)=1, L(7)=3, E = 99·3 - 294 = 3

Layer a=21: B = {2, 8, 3, 20}, active kernel {2,3}
  s=4, t=7, L(4)=1, L(7)=3, E = 99·3 - 294 = 3

Total excess = 6. First layer slack S_1 = 2328. Ratio = 388:1.

NOTE: M = 21. The computational check used M ≤ 20. Off by ONE.

## COUNTEREXAMPLE 2 (Gemini — larger, verified computationally)

A = {82, 123, 136, 153, 204, 205}, n = 1000, m = 1450, M = 205

Layer a=204: active kernel {2,3}, E = 100
Layer a=205: active kernel {2,3}, E = 100

Total excess = 200. First layer slack S_1 = 17800. Ratio = 89:1.

Uses parallel obstruction networks on carrier primes 17 and 41.

## WHY TWO BAD LAYERS CAN COEXIST

Two adjacent compact elements (like 20,21 or 204,205) can both have
active kernel {2,3} because:
- They use DIFFERENT elements for their 2-obstructions and 3-obstructions
- Adjacent integers share no prime factors (gcd(20,21)=1, gcd(204,205)=1)
- So their obstruction networks are completely independent
- Both can have s=4, t=7 at the same (n,m)

## WHAT SURVIVES

The first-layer theorem S_1 > E_j (for each individual bad child) is
STILL PROVED. The ratios are enormous (388:1, 89:1).

## THE NEW TARGET

Prove: Σ_{bad} E_j ≤ S_1 (first layer pays ALL bad children collectively)

This replaces uniqueness. The self-regulating property:
- More bad layers → more ancestor elements needed in A
- More ancestors → smaller a_1
- Smaller a_1 → larger S_1
- S_1 grows faster than Σ E_j

## KILL COUNT: 64
## PERCENTAGE: 82%
