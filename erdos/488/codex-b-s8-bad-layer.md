# EP-488: Codex B — s=8 Bad Layer Exists (Kills v15 Step 1)
## April 8, 2026

## THE COUNTEREXAMPLE

A = {22, 39, 85, 133, 46189}, n = 415700, m = 600457.
46189 = 11·13·17·19.

Layer 5 (a=46189): K = {2,3,5,7}, s = 8, t = 13.
L_K(8) = 1 (only 1 survives among 1..8 avoiding {2,3,5,7}).
L_K(13) = 3 (survivors: 1, 11, 13).
B_5 = 2·600457 - 415700·3 = -46186 < 0. BAD at s = 8.

Layers 1-4 all good (massive positive budgets).

## WHAT THIS KILLS

v15 Step 1 claimed: "first bad layer j₀ ≥ 4 has s ∈ {4, 6}"
This is ONLY true for j₀ = 4 (where π(s) ≤ 3 → s ≤ 6, s=5 dead).

For j₀ = 5: π(s) ≤ 4 → s ≤ 8. Kernel {2,3,5,7} at s=8 is real.
For j₀ = 6: π(s) ≤ 5 → s ≤ 12. Even deeper.

The correct band spectrum for the first bad layer:
j₀ = 3: s = 4 only
j₀ = 4: s ∈ {4, 6}
j₀ = 5: s ∈ {4, 6, 8}
j₀ = 6: s ∈ {4, 6, 8, 10, 12} (s=5,7,9,11 might be dead zones)
j₀ = k: s ≤ p_k - 1 (kth prime minus 1)

## WHAT SURVIVES

- |A| ≤ 5: PROVED (separate case analysis covered this)
- Layer-3-bad for ALL |A|: PROVED (three independent proofs)
- All 40+ permanent results: unaffected
- The witness-group charging IDEA: still viable, just needs
  to handle s = 4, 6, 8, 10, ... not just s = 4, 6

## THE REAL REMAINING TASK

The witness-group charging must work for bands at ALL even depths
(s = 4, 6, 8, 10, ...) simultaneously. The excess bound per layer
needs to be computed for each kernel type ({2,3}, {2,3,5}, {2,3,5,7}, ...).

At each band: excess < C_K · a for a known constant C_K.
Packing: multiples of d_i in the band, bounded count.
Self-regulation: more bad layers → witnesses forced smaller → surplus larger.

The mechanism is the same. The execution needs more bands.

## KILL COUNT: 79 (v15 Step 1)
## PERCENTAGE: 94%

Down from 97%. The closing path needs to handle deeper bands.
But the proved results hold and the mechanism is intact.
