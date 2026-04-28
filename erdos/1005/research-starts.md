# EP1005 Research Starts

Researched: 2026-04-26

## Statement and Status

Let `a_1/b_1, a_2/b_2, ...` be the Farey fractions of order `n >= 4`, in increasing order. Define `f(n)` as the largest integer such that every pair with `1 <= k < l <= k + f(n)` is similarly ordered:

```tex
(a_k-a_l)(b_k-b_l) >= 0.
```

Equivalently, `f(n)` is one less than the smallest Farey-index gap between two fractions whose numerator and denominator move in opposite directions. The problem is to estimate `f(n)`, especially whether `f(n) = (c + o(1)) n` for some constant `c > 0`.

Status: open. The current best bounds are due to Wouter van Doorn:

```tex
\left(\frac{1}{12}-o(1)\right)n <= f(n) <= \frac{1}{4}n + O(1).
```

van Doorn conjectures the upper bound is sharp, more precisely that for all `n >= 92`,

```tex
f(n) = floor(n/4) + d,
```

where `d = 1, 2, 2, 4` according as `n = 0, 1, 2, 3 (mod 4)`.

## Known Results and Partials

- Mayer introduced the phenomenon in 1942. van Doorn's summary separates two steps: Mayer first proved `f(n) >= 3` for `n >= 5`, then improved this to `f(n) -> infinity`.
- Erdos proved the first linear lower bound, with the proof giving `f(n) > n/400`.
- Zaharescu studied the Mayer-Erdos phenomenon for chains of consecutive Farey fractions and generalized the setup to arbitrary linear forms; van Doorn reports a constant `1/480` in that generalized setting.
- Meng and Zaharescu later gave a multivariable generalization for linear forms in more variables.
- Dress's exact discrepancy result for Farey sequences is relevant background for interval rank estimates, though the present problem needs sharper local information at intervals of length about `1/n`.
- van Doorn's 2025 paper improves the original problem to `(1/12-o(1))n <= f(n)` and constructs bad pairs with gap `< n/4 + 5`, sharpened to the residue-class bound above.
- OEIS A386893 records this sequence as "minimal number of Farey fractions in between two fractions that are not similarly ordered"; this equals `f(n)` under the off-by-one convention. The b-file currently lists values for `n=4..100`, and the OEIS formula/comment records van Doorn's lower bound and exact conjecture.

## Latest Literature and Comments

The latest substantive item I found is van Doorn's arXiv preprint, submitted 2025-08-28 as v1. I did not find a later improvement or follow-up paper in current web search. J-GLOBAL mirrors the same preprint metadata, and OEIS A386893 was added by van Doorn in September 2025 and now tracks the conjectural exact formula.

Important details from van Doorn:

- The upper-bound examples are explicit and centered near `1/2`. For example, when `n=4m`, the pair `(2m-1)/(4m)` and `2m/(4m-1)` gives a non-similarly-ordered pair at distance `m+2`, hence `f(n) <= m+1`.
- The conjecture was computationally checked for all `n <= 5000`; the only `4 <= n < 92` exceptions to the residue-class upper-bound equality are
  `7, 9, 11, 15, 19, 23, 25, 27, 31, 35, 39, 49, 51, 63, 91`.
- The lower-bound proof is really a local-density statement: if two Farey fractions of order `n` differ by `x/n`, then either the interval contains a fraction with denominator `< 6/x`, or their index gap is at least roughly `nx/12`.
- Near the right half of the sequence, van Doorn notes a stronger local lower bound `l-k > (1/8-o(1))n` for bad pairs with left endpoint at least `1/2-o(1)`.

## Natural First Attack Routes

1. Classify short bad pairs rather than improve global density blindly. A bad ordered pair `a/b < c/d` has either `c > a, d < b` or `c < a, d > b`. The conjectural minimizers seem to be sparse, structured pairs near `1/2`, so try to prove that any bad pair with index gap `< n/4 + O(1)` must lie in a short list of continued-fraction/Farey-neighbor configurations.

2. Sharpen the local-density dichotomy. van Doorn loses a factor through the threshold for small denominators in an interval and the split of adjacent denominators into small/large classes. Optimizing that argument, or replacing it with a sharper rank-counting estimate in intervals of length `x/n`, is the most direct route from `1/12` toward `1/4`.

3. Use exact rank formulas for candidate intervals. For a candidate bad pair `a/b < c/d`, the index gap is the number of reduced fractions with denominator `<= n` in `(a/b, c/d)`, plus one. Mobius-inversion floor sums or Stern-Brocot interval decompositions may turn the conjecture into a finite family of inequalities.

4. Exploit the explicit upper-bound neighborhoods. The constructions around `1/2` are arithmetic progressions in Farey neighbors. Proving they are extremal may reduce to showing every other bad pair contains a denser subinterval or a smaller-denominator obstruction.

## Computational and Formalization Hooks

- Baseline verifier: generate `F_n` by the standard recurrence
  `k = floor((n+b)/d)`, `(a,b,c,d) <- (c,d,kc-a,kd-b)`, then check pairs only up to `floor(n/4)+4` using the conjectural upper bound. This is enough for regression tests and small-data exploration.
- Better search: enumerate primitive bad endpoint pairs, compute their Farey rank gap by
  `sum_{q <= n} #{p : gcd(p,q)=1, a/b < p/q < c/d}`, and minimize. This avoids scanning every local window and directly exposes endpoint structure.
- OEIS A386893 values for `n=4..100` are immediate test fixtures; my quick local check reproduced the `n=88..100` pattern and the exceptional `n=91`.
- Formalization target: the upper-bound construction is low-risk to formalize from the consecutive-Farey criterion `bc-ad=1`, `max(b,d) <= n < b+d`. The analytic lower bound is harder, but the finite rank-gap reformulation and exact residue-class constructions are realistic Lean targets.

## Risks and Unknowns

- The gap between `1/12` and conjectural `1/4` is still large; a few days may produce a useful lemma or computation, not a full proof.
- The 2025 result is recent and appears to be an arXiv v1 preprint, so proofs and constants should be independently checked before building on them.
- The exact conjecture may require controlling all exceptional low-denominator intervals, not just the obvious `1/2` family.
- Be careful with conventions: OEIS counts fractions in between a bad pair, which equals `f(n)`; the raw index distance is `f(n)+1`.
- Older Mayer/Erdos papers are short but partly behind journal/archive interfaces; van Doorn's introduction is currently the clearest source trail.

## Tractability Score

5/10 for a serious few-day attempt. The problem has a clean formulation, a recent short proof to audit, strong computational evidence, and explicit conjectural extremizers. The main downside is that closing a factor-three lower-bound gap likely needs a genuinely sharper structural argument.

## Three Concrete Next Steps

1. Reproduce van Doorn's Theorem 1 and Theorem 2 proofs in local notes, marking every inequality where the constant `1/12` is lost.
2. Build a rank-gap search for primitive bad endpoint pairs and collect all minimizers for `n <= 1000`, grouped by residue class and continued-fraction pattern.
3. Try to prove a classification lemma for bad pairs with index gap `<= n/4 + O(1)`, starting with the case where the interval contains no denominator `< 6/x`.

## Sources

- Official problem page: https://www.erdosproblems.com/1005
- Wouter van Doorn, "Improved bounds for the Mayer-Erdos phenomenon on similarly ordered Farey fractions", arXiv:2509.00121: https://arxiv.org/abs/2509.00121
- J-GLOBAL metadata for van Doorn's preprint: https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502215989278030
- OEIS A386893: https://oeis.org/A386893
- Alexandru Zaharescu, "The Mayer-Erdos phenomenon", Indagationes Mathematicae 17 (2006), 147-156: https://www.sciencedirect.com/science/article/pii/S0019357706800121
- Xianchang Meng and Alexandru Zaharescu, "A multivariable Mayer-Erdos phenomenon", Journal of the Korean Mathematical Society 51 (2014), 1029-1044: https://experts.illinois.edu/en/publications/a-multivariable-mayer-erdos-phenomenon
- A. E. Mayer, "On neighbours of higher degree in Farey series", Quarterly Journal of Mathematics 13 (1942), 185-192: https://academic.oup.com/qjmath/article-abstract/os-13/1/185/1520904
- Francois Dress, "Discrepance des suites de Farey", Journal de theorie des nombres de Bordeaux 11 (1999), 345-367: https://eudml.org/doc/225810
