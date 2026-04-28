# EP-488: Codex B — Kill #71 + Exact Gap Isolation
## April 7, 2026

## KILL #71: Monotone Reduction from Pairs is FALSE

Adding generators can DECREASE the non-first-layer surplus R_A.

Counterexample:
A = {4, 7, 9, 10, 11}, n=76, m=109: R_A = 2450
B = {4, 6, 7, 9, 10, 11}, n=76, m=109: R_B = 2440

Adding element 6 increases H at both scales but increases H(m) MORE,
reducing the surplus. The functional X → 2m|X∩[1,n]| - n|X∩[1,m]|
is NOT monotone under set enlargement.

So "pairs are worst, adding generators only helps" is DEAD.

## THE EXACT REMAINING THEOREM (cleanest statement yet)

Define H_A(x) = |{n ≤ x : a₁ ∤ n, ∃ a ∈ A\{a₁} with a|n}|.

Then F_A(x) = ⌊x/a₁⌋ + H_A(x).

EP-488 ⟺ S₁ + [2mH_A(n) - nH_A(m)] > 0.

Since S₁ > 0 (Lean-verified), EP-488 follows from:

  2mH_A(n) - nH_A(m) ≥ 0  (SURPLUS DOMINANCE)

Equivalently: "the union of later multiples, after deleting first-layer
multiples, still satisfies the 2-inequality."

## COMPUTATIONAL VERIFICATION

- All primitive subsets of [2,19]: zero violations
- Random search M ≤ 500: zero violations  
- Worst case: A={2,19}, (n,m)=(56,57), surplus = 2
- Near-extremals are pair-shaped (but NOT by monotone reduction)

## WHAT THIS CHANGES

The gap is now ONE clean analytic statement about H_A.
No layers, no kernels, no ancestors, no matching.
Just: "the non-first-layer covered set satisfies 2mH(n) ≥ nH(m)."

This is a statement about primitive sets and their covering functions.
It might be provable by methods from analytic number theory (Erdős
density bounds, Behrend structure theorem) without any of our
layer-based machinery.

## KILL COUNT: 71
## PERCENTAGE: 87%

Up 1%. Kill #71 closes a tempting false route. The gap is now the
cleanest and most precise it has ever been: prove surplus dominance
for H_A, or equivalently non-first-layer positivity.
