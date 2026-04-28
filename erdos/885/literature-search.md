# EP885 literature search

Date: 2026-04-26. Accents are omitted in body text for plain-text portability.

## Problem

For an integer `n >= 1`,

`D(n) = {|a - b| : ab = n}`.

EP885 asks whether, for every `k >= 1`, there are integers

`N_1 < ... < N_k`

such that

`|D(N_1) cap ... cap D(N_k)| >= k`.

The current Erdos Problems page states that the problem is open, records the
known cases `k = 2, 3, 4`, and says there are no solutions or partial solutions
claimed in the incorporated comments. The discussion thread has a 2026 partial
computational/formalization note, but explicitly no claimed solution of EP885.

Primary EP885 links:

- T. F. Bloom, [Erdos Problem #885](https://www.erdosproblems.com/885), accessed 2026-04-26.
- [EP885 discussion thread](https://www.erdosproblems.com/forum/thread/885), accessed 2026-04-26.
- [EP885 LaTeX source](https://www.erdosproblems.com/latex/885), accessed 2026-04-26.

## Source map

Direct EP885 line:

- Paul Erdos and Moshe Rosenfeld, "The factor-difference set of integers",
  Acta Arithmetica 79.4 (1997), 353-359.
  Official metadata/full article links: [EuDML](https://eudml.org/doc/206983),
  [DOI](https://doi.org/10.4064/aa-79-4-353-359).
- Jorge Jimenez-Urroz, "A Note on a Conjecture of Erdos and Rosenfeld",
  Journal of Number Theory 78.1 (1999), 140-143.
  Links: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022314X99924071),
  [DOI](https://doi.org/10.1006/jnth.1999.2407),
  author page with DVI link
  ([papers page](https://web.mat.upc.edu/jorge.urroz/papers.htm),
  [DVI](https://web.mat.upc.edu/jorge.urroz/erdosros.dvi)).
- Andrew Bremner, "On a problem of Erdos related to common factor differences",
  International Journal of Number Theory 15.5 (2019), 1059-1068.
  Links: [ASU Pure metadata/abstract](https://asu.elsevierpure.com/en/publications/on-a-problem-of-erd%C3%B6s-related-to-common-factor-differences/),
  [DOI](https://doi.org/10.1142/S1793042119500581),
  [ResearchGate preview](https://www.researchgate.net/publication/329314619_On_a_problem_of_Erdos_related_to_common_factor_differences).

Adjacent close-divisor / close-factorization line from the same 1997 paper:

- Tsz Ho Chan, "Factors of a perfect square", Acta Arithmetica 163.2 (2014),
  141-143. Links: [EuDML](https://eudml.org/doc/279082),
  [DOI](https://doi.org/10.4064/aa163-2-4).
- Tsz Ho Chan, "Factors of almost squares and lattice points on circles",
  Int. J. Number Theory 11.6 (2015), 1701-1708.
  Links: [arXiv:1406.2230](https://arxiv.org/abs/1406.2230),
  [DOI](https://doi.org/10.1142/S1793042115500911).
- Tsz Ho Chan, "Numbers with three close factorizations and lattice points on
  hyperbolas", Integers 18 (2018), A13.
  Link: [PDF](https://math.colgate.edu/~integers/s13/s13.pdf).
- Tsz Ho Chan, Laura Holmes, Michael Liu, Jose Villarreal, "Numbers with Four
  Close Factorizations", arXiv:2508.02818 (2025).
  Link: [arXiv](https://arxiv.org/abs/2508.02818).
- Patrick Letendre, "Divisors of an Integer in a Short Interval",
  arXiv:2503.12146 (2025).
  Link: [arXiv](https://arxiv.org/abs/2503.12146).

Forum/non-peer-reviewed partial notes:

- Sam Mausberg, "Two Formalized Partial Results Related to Erdos Problem E885",
  forum note bundle, 2026.
  Links: [GitHub bundle](https://github.com/SamMausberg/lean-formalizations/tree/main/FormalConjectures/Problems/Erdos/E885/ForumNote),
  [LaTeX note](https://github.com/SamMausberg/lean-formalizations/blob/main/FormalConjectures/Problems/Erdos/E885/ForumNote/erdos885_forum_note.tex).

## Known direct results

### k = 2: Erdos-Rosenfeld 1997

Erdos and Rosenfeld prove the stronger statement that, for every positive
integer `r`, there exist `r` integers `N_1 < ... < N_r` with

`|D(N_1) cap ... cap D(N_r)| >= 2`.

Thus EP885 is true for `k = 2`.

Their construction fixes two differences. Let `p_1, ..., p_m` be distinct odd
primes and choose

`alpha = (p_1...p_s + p_{s+1}...p_m)/2`,

`beta = (p_1...p_s - p_{s+1}...p_m)/2`,

so `(alpha - beta)(alpha + beta) = p_1...p_m`. For each factorization
`m_1 m_2 = p_1...p_m`, solve

`x + y = m_1`, `x - y = m_2`.

Then `x^2 - alpha^2 = y^2 - beta^2`, giving an integer `M` with
`{2 alpha, 2 beta} subset D(M)`. Taking enough factorizations gives as many
distinct `M` as needed.

The same paper records two Barry Guiduli examples of three integers sharing
four differences:

- `{420, 3780, 14940, 76860} subset D(6925500) cap D(37901500) cap D(108448956)`.
- `{420, 3780, 61695, 154332} subset D(2778300) cap D(862552800) cap D(5400442044)`.

These are not `k = 4` EP885 witnesses because there are only three `N_i`, but
they are important small search seeds.

### k = 3: Jimenez-Urroz 1999

Jimenez-Urroz proves the stronger statement that, for every positive integer
`r`, there exist `r` integers `N_1 < ... < N_r` with

`|D(N_1) cap ... cap D(N_r)| >= 3`.

Thus EP885 is true for `k = 3`.

The reduction is elliptic-curve based. Because scaling by `4` doubles
differences, one may work with even differences `2d_1, 2d_2, 2d_3`. A common
integer `N` with these differences is equivalent to

`N = x^2 - d_1^2 = y^2 - d_2^2 = z^2 - d_3^2`.

Putting `A = d_1^2 - d_2^2` and `B = d_1^2 - d_3^2`, this asks for many
solutions to

`x^2 - y^2 = A`, `x^2 - z^2 = B`.

Letting `lambda = x^2`, the condition is that `lambda`, `lambda - A`, and
`lambda - B` are squares. By the standard 2-descent criterion for

`E(A,B): Y^2 = X(X-A)(X-B)`,

such triples correspond to rational points in `2E(Q)`. A curve `E(A,B)` of
positive rank supplies infinitely many rational points, and clearing
denominators supplies the required integer examples. The paper reports positive
rank examples among small `(A,B)`, including `(4,6)`.

The DVI example from `E(4,6)` gives five integers sharing three common
differences. The common differences are very large:

- `d1 = 993243542205992332488058754263122078071239561123822165112`
- `d2 = 573704451935072432558657786561844237570109187841809114488`
- `d3 = 20948274110993405271036818636118416362912097297024759288`

The full five `N_i` values are in the author's DVI; extract them directly if
needed for regression tests, since manual transcription is error-prone.

### k = 4: Bremner 2019

Bremner proves EP885 for `k = 4` by proving that there are infinitely many sets
of four integers with four common factor differences. The ASU metadata and
World Scientific/ResearchGate preview identify the method keywords as "common
factor difference" and "elliptic curve".

Important gap in this scout: the open preview/metadata gives the theorem-level
result but not the full parametric construction or a compact numerical witness.
The full Bremner article should be obtained before the computational phase so
the exact `k = 4` families can be reconstructed and used as seeds.

## Useful algebra for computation

For `d >= 0`,

`d in D(N)` iff there is an integer `a >= 1` such that

`N = a(a + d)`.

Equivalently,

`4N + d^2 = (2a + d)^2`.

Thus a set of common differences `{d_1, ..., d_t}` for several `N_i` is the same
as a set of simultaneous square translates

`4N_i + d_j^2 = square`.

This is the bridge between the EP885 incidence graph search and the elliptic
curve / square-translate formulations in Jimenez-Urroz, Bremner, and the 2026
forum note.

## Later and adjacent work

I did not find a later direct paper proving `k = 5` or the full all-`k`
conjecture.

The related literature after Erdos-Rosenfeld mostly follows the "close
divisors near sqrt(n)" branch that Erdos and Rosenfeld also raised. This branch
does not solve EP885, but it is relevant because small factor differences are
equivalent to factor pairs close to `sqrt(n)`.

- EP887 records the close-divisor question and notes that Erdos-Rosenfeld
  proved infinitely many `n` have four divisors in
  `(n^(1/2), n^(1/2) + n^(1/4))`, and also proved an upper bound of
  `1 + C^2` divisors in
  `(n^(1/2), n^(1/2) + C n^(1/4))` for sufficiently large `n` depending on
  `C`.
- Chan 2014 proves the square case: if `n` is a sufficiently large square, then
  `n` has at most five divisors in the symmetric interval of radius
  `n^(1/4)(log n)^(1/7)` around `sqrt(n)`.
- Chan 2015 extends part of this to almost-squares
  `n = (N-a)(N+b)` with small `a,b`, giving at most eighteen divisors in a
  slightly shorter logarithmic window.
- Chan 2018 studies three close factorizations and proves sharp lower bounds
  for gaps between three close lattice points on `xy = n`.
- Chan-Holmes-Liu-Villarreal 2025 studies four close factorizations and reduces
  the problem to generalized Pell equations. This is close-divisor structure,
  not a four-common-difference EP885 witness.
- Letendre 2025 studies the general divisor-counting function
  `D_n(X,Y) = |{d | n : X <= d <= X+Y}|`; this is broad short-interval divisor
  work and not a direct EP885 solution.

## Forum note and verification

The 2026 EP885 thread records two non-solution partial claims:

1. Define
   `Y(a,b,c) = {z > 0 : z^2+a, z^2+b, z^2+c are all squares}`.
   The note claims
   `{330, 870, 2445, 4155, 10482} subset Y(756000, 15971200, 45130176)`,
   so the universal anchored cap `|Y(a,b,c)| <= 4` is false. This does not
   give a `k = 5` EP885 witness.

2. It claims the exact finite computation

   `D(79200) cap D(227205) cap D(1258560) = {36, 468, 692, 1028}`.

   I verified this locally by direct divisor enumeration on 2026-04-26.
   The Bloom reply in the thread appears to have a typo `{..., 1029}`; direct
   enumeration gives `1028`, and `1029` is not in any of the three displayed
   `D(N)` sets.

## Risk assessment for prior k = 5 / full solutions

Published direct solution risk: low, but not zero.

Reasons for low risk:

- The current EP885 page still marks the problem open and lists only `k = 2`,
  `k = 3`, and `k = 4`.
- The current thread has no claimed solution of EP885 and only records partial
  computations.
- Searches for the direct titles/phrases "factor-difference set",
  "common factor differences", "Erdos Rosenfeld", "Jimenez-Urroz", "Bremner",
  "k=5", and "E885" did not locate a later `k = 5` or all-`k` paper.
- Bremner 2019, the direct latest published step found here, states exactly the
  `k = 4` advance.

Reasons risk is not zero:

- EP885 has several equivalent languages: common factor differences,
  simultaneous square translates, close factorizations, lattice points on
  hyperbolas, and elliptic/hyperelliptic curve constructions. A solution could
  be hidden under a title that does not mention EP885.
- The problem page itself warns that the website's open status may miss
  literature.
- Bremner's full construction was not extracted in this scout because the
  article body was not openly available through the preview. Its references,
  examples, and remarks may point to unpublished or follow-up work.

Working estimate:

- Peer-reviewed `k = 5` solution already published: low probability.
- Unpublished preprint, forum note, or computational certificate not yet
  incorporated into EP885: moderate probability.
- Full all-`k` solution already known but hidden: low probability, because it
  would subsume a named open Erdos Problems entry and likely cite or update the
  1997/1999/2019 chain.

Recommended next literature actions:

1. Obtain Bremner 2019 full text and extract the exact parametric construction,
   sample four-integer/four-difference witnesses, and any remarks about the
   obstruction to `k = 5`.
2. Search citation databases for papers citing Bremner 2019 and Jimenez-Urroz
   1999, using title variants without accents.
3. Search the square-translate language directly:
   `z^2+a_i all squares`, `simultaneous square translates`, and
   `elliptic curve common factor differences`.
4. Reconstruct the `k = 3` and `k = 4` constructions inside the local incidence
   code before running broad `K_{5,5}` searches; they are the best calibration
   data for avoiding biased candidate families.
