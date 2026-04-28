# EP-488: THE SYNCHRONIZATION QUESTION
## April 5, 2026 — Claude's Question

## THE QUESTION

"Why can't all layers peak at the same x?"

In the decomposition H_A(x) = Σ T_j(x), each T_j peaks at specific
x values determined by periodicity of K_{Q_j} and spacing a_j.

For sup(Σ T_j) ≥ 2·inf(Σ T_j), we need layers to SYNCHRONIZE:
many peaking while others trough, simultaneously.

Primitivity (a_i ∤ a_j) might prevent this synchronization.

## WHY THIS IS DIFFERENT

- NOT about amplitude (kill #46 showed individual amplitudes can be large)
- NOT about phase cancellation (Fourier — hard to prove)
- ABOUT: the geometry of where peaks land on the x-axis

## THE MECHANISM

Layer j peaks when ⌊x/a_j⌋ hits a "good" residue for Q_j.
Peak locations: x ≈ a_j · y*_j for each j.

Synchronization requires: a_1·y*_1 ≈ a_2·y*_2 ≈ ... ≈ a_k·y*_k

If a_i | a_j: ⌊x/a_i⌋ = a_j/a_i · ⌊x/a_j⌋ (synchronized — peaks align)
Primitivity forbids a_i | a_j: sampling rates are "incommensurable"

## THE ANALOGY

Like irrational rotations on a torus:
- If angles are rationally related: orbits synchronize, peaks align
- If angles are "independent": orbits equidistribute, peaks spread out
- Primitivity forces the a_j to be "independent" in the divisibility sense

## WHAT TO TEST

1. For primitive sets where ratio is high (e.g. {9,22,23,25,26,28,29}):
   WHERE does each layer T_j peak? Do they align?
   
2. For adjacent pairs {M-1, M} (worst case): the two layers have
   a_1 = M-1, a_2 = M. Peaks at x ≈ (M-1)·y*_1 and x ≈ M·y*_2.
   gcd(M-1, M) = 1, so these are maximally incommensurable.
   Yet the ratio is 0.997. So SOME synchronization happens even here.
   How?

3. For non-primitive sets (hypothetical): if a_i | a_j were allowed,
   would ratio exceed 1? This would prove primitivity is the key.

## PROOF STRATEGY

If we can show: for primitive sets, at any x where SOME layers peak,
at least one layer is near its MEAN (not its trough), then:

sup(Σ T_j) ≤ (k-1)·max_single_peak + 1·mean ≈ Σ means + O(max oscillation)
inf(Σ T_j) ≥ 1·min_single_trough + (k-1)·mean ≈ Σ means - O(max oscillation)

And the ratio sup/inf ≈ 1 + O(oscillation/Σmeans) < 2 when oscillation < Σmeans.

The "at least one layer near mean" claim is the desynchronization lemma.
It follows if the peak locations are spread out (not all at the same x).

