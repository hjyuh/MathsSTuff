# EP506 Research Starts

Date: 2026-04-26

## Statement / Status

EP506 asks for the minimum number of distinct circles determined by any
set of `n` points in `R^2`, not all on one circle. I interpret "circle
determined" as a circle containing at least three of the given points;
collinear triples do not determine a circle. The official page flags a
real ambiguity in the intended non-degeneracy condition: either "not all
on a line" or the stronger "no three collinear".

Current status: large `n` is solved, and the official status is
"decidable - resolved up to a finite check." Under Elliott's weaker
hypothesis, for `n > 393` the exact lower bound is

```tex
\binom{n-1}{2}+1-\left\lfloor\frac{n-1}{2}\right\rfloor.
```

The unresolved part is the finite range `n <= 393`, plus any separate
interpretation using the stronger no-three-collinear condition.

## Known Results And Partials

- Elliott (1967) claimed that if the points are not all on a circle or a
  line and `n > 393`, then at least `binom(n-1,2)` distinct circles are
  forced.
- Purdy and Smith point out that this count is slightly too high. Their
  correction is
  `1 + binom(n-1,2) - floor((n-1)/2)`, with the same `n > 393`
  threshold. The extremal construction is `n-1` points on one circle and
  one point off it, arranged so the off-circle point lies on as many
  two-point secants as possible, namely `floor((n-1)/2)`.
- Balintova and Balint (1994) reported the corrected lower bound, but
  apparently without enough explanation for later readers to recognize
  it as intentional.
- Segre's projected-cube example gives an `n = 8` obstruction to the
  stronger `binom(n-1,2)` lower bound, so the small cases are not just a
  cosmetic cleanup of Elliott's statement.
- Adjacent ordinary-circle results are strong but not directly the same
  problem: Lin, Makhul, Nassajian Mojarrad, Schicho, Swanepoel, and de
  Zeeuw prove the exact minimum number of ordinary circles for all
  sufficiently large `n`, with main term `n^2/4`; EP506's total-circle
  target has main term `n^2/2`.

## Latest Relevant Literature / Comments

- The EP506 page was last edited on 2026-02-01 and now incorporates the
  Purdy-Smith correction. Its forum thread records the 2026 comment that
  triggered the update.
- Purdy-Smith (arXiv 2009; DCG 2010/2011 listing) is the key post-Elliott
  source: it explains the subtractive term, uses circular inversion, and
  gives a lower bound for circles containing at most four points when no
  line or circle contains too many of the points.
- The ordinary-circle line of work is the main modern toolkit. Zhang
  improved earlier lower bounds; Lin et al. later got the asymptotic and
  sufficiently-large exact result, relying on Green-Tao ordinary-line
  structure plus inversion. Their structure theorem is useful scouting
  evidence: point sets with few ordinary circles are close to low-degree
  algebraic curves or double-circle configurations.
- I did not find a newer direct resolution of the `n <= 393` EP506
  finite check beyond the official ErdosProblems update.

## Natural First Attack Routes

- Reconstruct Elliott/Purdy-Smith carefully. The immediate deliverable is
  a clean proof ledger showing exactly where `n > 393` enters and which
  assumptions are used: weak "not all line/circle" versus "no three
  collinear".
- Use inversion at a chosen point. Circles through that point become
  lines in the inverted configuration, so Melchior/Kelly-Moser style
  line-counting can be reused. The delicate part is tracking collinear
  triples through the inversion, which is exactly where the
  `floor((n-1)/2)` correction appears.
- Split by a rich circle/line. If `n-1` points lie on a circle, the
  extremal construction is explicit. If no circle or line is very rich,
  Purdy-Smith's at-most-four-point-circle lower bounds and ordinary-circle
  structure may force a stronger count.
- Generate and classify small counterexamples: the one-off-circle family,
  Segre/projected cube, two concentric regular polygons, and double
  polygons from the ordinary-circle literature are the first families to
  compare.

## Computational / Formalization Hooks

- Exact circle counter: for rational/algebraic coordinates, enumerate
  non-collinear triples and normalize the circle equation
  `x^2 + y^2 + A x + B y + C = 0`; use the four-point determinant to
  merge triples lying on the same circle.
- Search templates: `(n-1)+1` circle/off-circle construction; projected
  cube under rational projections; two concentric regular polygons; and
  perturbations that remove accidental collinearities or concyclicity.
- Order-type databases can guide very small no-three-collinear searches
  (`n <= 10` or `11`), but order type alone is insufficient because
  concyclicity is metric. A stronger encoding needs in-circle predicates
  or polynomial equality constraints.
- Formalization target: start with the extremal construction and inversion
  facts, not the full Elliott proof. The official page currently lists no
  formalized statement.

## Risks / Unknowns

- The non-degeneracy ambiguity can change the answer. The corrected
  extremal construction uses collinear triples through the off-circle
  point, so it is not automatically admissible under "no three collinear".
- The finite check `n <= 393` is finite in principle, not obviously
  computationally small. It mixes incidence combinatorics with real
  algebraic realizability.
- The 1967 and 1994 papers need direct reading for exact definitions and
  hypotheses; secondary summaries agree on the correction but not every
  small technical convention.
- Ordinary-circle theorems are adjacent rather than decisive for total
  circles; their lower bound is too small by a factor of about two for
  EP506.

## Tractability Score

4/10 for a serious attempt over the next few days. Reproducing the
large-`n` proof and building a useful small-`n` search harness is quite
tractable; resolving the whole finite range or the no-three-collinear
variant is probably not.

## Three Concrete Next Steps

1. Obtain and read Elliott (1967) and Balintova-Balint (1994) directly;
   extract hypotheses, thresholds, and the exact finite remainder.
2. Implement an exact circle-counting script and benchmark the known
   constructions for `5 <= n <= 12`, including the projected cube.
3. Write a proof skeleton for the inversion route, isolating the lemma
   that produces the subtractive `floor((n-1)/2)` term and the cases left
   after a rich-circle split.

## Sources

- Official EP506 page:
  <https://www.erdosproblems.com/506>
- EP506 discussion thread:
  <https://www.erdosproblems.com/forum/thread/506>
- Elliott, "On the number of circles determined by n points":
  <https://doi.org/10.1007/BF02020972>
- Purdy and Smith, "Lines, Circles, Planes and Spheres":
  <https://arxiv.org/abs/0907.0724>
- Lin, Makhul, Nassajian Mojarrad, Schicho, Swanepoel, de Zeeuw,
  "On Sets Defining Few Ordinary Circles":
  <https://arxiv.org/abs/1607.06597>
- Published open-access version of the ordinary-circles paper:
  <https://link.springer.com/article/10.1007/s00454-017-9885-8>
- Zhang, "On the Number of Ordinary Circles Determined by n Points":
  <https://doi.org/10.1007/s00454-010-9286-8>
- Point Set Order Type Database overview:
  <https://publications.ist.tugraz.at/abstracts/ak-psotd-01/index.html>
