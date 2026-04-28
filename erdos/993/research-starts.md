# EP993 research starts

Researched: 2026-04-26

## Statement / Status

Erdos Problem #993 asks whether the independent-set sequence of every
tree or forest is unimodal: for `i_k(T)` equal to the number of independent
vertex sets of size `k`, must

```tex
i_0(T) \leq i_1(T) \leq \cdots \leq i_m(T) \geq i_{m+1}(T) \geq \cdots
```

hold for some mode `m`? The [official ErdosProblems page](https://www.erdosproblems.com/993)
still lists the problem as open/falsifiable, with no formalized statement. The
general-graph analogue is false: Alavi, Malde, Schwenk, and Erdos showed that
general graphs can realize arbitrary inequality patterns. The matching/edge
independence sequence is unimodal for every graph by Schwenk, but that result
does not transfer to vertex independent sets.

Important scouting point: the forest case is not a trivial corollary of the
tree case, because the independence polynomial of a forest is a product of the
component polynomials, and convolution does not preserve ordinary unimodality
in general.

## Known Results And Partials

- Computation gives strong evidence and no counterexample. Basit-Galvin cite
  Radcliffe's verification through 25 vertices, including the stronger ordered
  log-concavity property for all trees up to that size. The current public
  forum/repository trail reports exhaustive unimodality verification through
  `n <= 29`: 8,691,747,673 unlabeled trees total, including 5,469,566,585 trees
  at `n = 29`, with zero failures. Treat this as reproducible but not yet
  peer-reviewed.
- General tails are controlled. Levit-Mandrescu proved that for
  Konig-Egervary graphs, hence for trees and forests, the final one-third of
  the independent-set sequence is weakly decreasing. Basit-Galvin generalize
  this: for an `n`-vertex graph with independence number `alpha`, the sequence
  is decreasing from `ceil(alpha(n-1)/(alpha+n))` onward. They also prove an
  initial increasing interval for trees through roughly `(n-alpha+1)/4`.
- Random trees look easier than worst-case trees. Basit-Galvin show that for a
  uniformly random labelled tree, asymptotically almost surely the initial
  approximately 49.5% of the nonzero sequence is increasing and the terminal
  approximately 38.8% is decreasing.
- Several special classes are settled. Levit-Mandrescu prove unimodality for
  well-covered spiders and reductions for some well-covered trees. Li-Li-Yang-
  Zhang give a symmetric-function method proving log-concavity for all spiders.
  Grace Li proves unimodality for the two Kadrawi-Levit non-log-concave
  infinite tree families `T_{3,m,n}` and `T^*_{3,m,n}`.
- The stronger log-concavity route is dead. Kadrawi-Levit found tree
  independence polynomials that are not log-concave starting at order 26 and
  constructed infinite non-log-concave families. Galvin later constructed
  non-log-concave trees with failures near the top degree; Bautista-Ramos
  constructed trees with arbitrarily many log-concavity breaks. Ramos-Sun used
  PatternBoost to find tens of thousands of additional log-concavity
  counterexamples on 27 to 101 vertices, but report that all found examples are
  still unimodal.

## Latest Relevant Literature / Comments

- [Erdos Problem #993](https://www.erdosproblems.com/993) and its
  [discussion thread](https://www.erdosproblems.com/forum/thread/993): official
  status plus Jan-Mar-Apr 2026 comments. The comments are explicitly
  unverified by the site.
- [BrettRey/erdos-problem-993](https://github.com/BrettRey/erdos-problem-993):
  public code/results claiming exhaustive `n <= 29`, an `n = 28` log-concavity
  near-miss audit, and a draft structural route using
  `I(T_e;x) = I(T;x) + x I(T/e;x)`.
- Basit and Galvin, [On the independent set sequence of a tree](https://arxiv.org/abs/2006.12562)
  (2020/2021): best general published scouting reference for tails, random
  trees, and computational history.
- Kadrawi and Levit, [The independence polynomial of trees is not always
  log-concave starting from order 26](https://arxiv.org/abs/2305.01784) (2023):
  kills log-concavity as a global proof strategy.
- Galvin, [Trees with non log-concave independent set sequences](https://arxiv.org/abs/2502.10654)
  (v2 Jan. 2026): asymptotic non-log-concavity family resolving a
  Kadrawi-Levit conjecture.
- Ramos and Sun, [An AI enhanced approach to the tree unimodality
  conjecture](https://arxiv.org/abs/2510.18826) (Oct. 2025): ML-guided search
  for log-concavity counterexamples, no unimodality counterexample found.
- Bautista-Ramos, [Multiple breaks of log-concavity in the independence
  polynomials of trees](https://arxiv.org/abs/2511.00334) (Nov. 2025):
  arbitrary many log-concavity breaks.
- Grace M. X. Li, [Unimodality of independence polynomials of two family of
  trees](https://arxiv.org/abs/2603.03025) (Mar. 2026): proves unimodality for
  the two main known non-log-concave tree families.
- Li, Li, Yang, Zhang, [A symmetric function approach to log-concavity of
  independence polynomials](https://arxiv.org/abs/2501.04245) (2025): proves
  all spiders have log-concave independence polynomials.
- Levit and Mandrescu, [On Unimodality of Independence Polynomials of some
  Well-Covered Trees](https://arxiv.org/abs/math/0211036) (2002): useful older
  reductions and well-covered spider results.

## Natural First Attack Routes

1. Close the central gap left by known increasing/decreasing intervals. The
   Basit-Galvin extension-count setup gives clean identities for ratios
   `i_{k+1}/i_k`; global monotone ratios are false, but a weaker "no valley"
   inequality in the middle could still be viable.
2. Study minimal counterexamples under tree operations. The subdivision-
   contraction identity `I(T_e;x) = I(T;x) + x I(T/e;x)` suggests an induction
   route if one can prove a robust mode-shift bound under contraction or
   subdivision. The public draft claims this is close but still conditional.
3. Mine the non-log-concave families. Known bad-for-log-concavity examples
   fail near the high-degree end yet remain unimodal. A structural explanation
   of why their ratio dips do not create valleys may give a lemma for broad
   "multi-arm" tree classes.
4. Keep the forest version separate. If the tree case is approached by a
   property not closed under products, a forest counterexample could still
   lurk in component convolutions. Search products of near-miss tree
   polynomials, not just connected trees.

## Computational / Formalization Hooks

- Rooted-tree DP is straightforward and exact. For each rooted vertex `v`, keep
  two polynomials: `A_v` for independent sets in the subtree not using `v`, and
  `B_v` for those using `v`. Then
  `B_v = x * product A_u` and `A_v = product (A_u + B_u)` over children `u`.
  This supports exhaustive verification, targeted family search, and proof
  experiments.
- Unimodality can be checked by finite differences: the sign pattern of
  `i_{k+1}-i_k` should have at most one change from nonnegative to nonpositive.
  Near-miss metrics should track ratio minima around the first possible valley,
  not just log-concavity failures.
- Reproducibility target: run the BrettRey unit tests and small exhaustive
  enumerations locally, then audit result JSON/hashes for the `n = 28,29`
  claims. The repo already includes DP code, nauty/generation hooks, targeted
  search, and a small amount of Lean.
- Formalization target: start with the rooted DP recurrence and the
  subdivision-contraction identity. These are small enough for Lean/Mathlib or
  Sage-to-Lean proof sketches before attempting global unimodality.

## Risks / Unknowns

- The strongest `n <= 29` computation is currently a public artifact and forum
  comment, not a refereed result. It is valuable but should be independently
  reproduced before being used as evidence in a writeup.
- Log-concavity, ordered log-concavity, and real-rootedness are not viable
  global targets for all trees. Any proof must tolerate local ratio reversals.
- Random-tree behavior may be irrelevant to adversarial trees; all known
  difficult examples are structured, high-degree, multi-arm constructions.
- The forest formulation may require a separate closure argument or direct
  product search.
- Exhaustive search is now expensive: moving beyond `n = 29` is a serious
  compute project unless guided by near-miss/family heuristics.

## Tractability Score

4/10 for a serious attempt over the next few days. A full proof is unlikely on
that timescale, but there are concrete partial-progress targets: reproduce and
audit computations, isolate a structural lemma around subdivision/contraction,
or explain unimodality in the known non-log-concave families.

## Three Concrete Next Steps

1. Reproduce the public computation at small scale: run the repo tests, verify
   the DP recurrence independently, and exhaustively check through at least
   `n <= 20` locally before trusting the `n = 28,29` artifacts.
2. Build a near-miss atlas for known families: Kadrawi-Levit, Galvin,
   Bautista-Ramos, Ramos-Sun samples if available, and multi-arm stars. Record
   mode location, ratio sequence, log-concavity break indices, and smallest
   unimodality margin.
3. Pick one proof lemma and attack it in isolation: either prove a usable
   edge-contraction/subdivision mode-shift bound, or derive a weaker
   Basit-Galvin-style extension-count inequality that rules out a second sign
   change in the central interval.
