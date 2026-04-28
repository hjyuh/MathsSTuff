# EP885 literature risk pass

Date: 2026-04-26.

Scope: adversarial check for any post-2019 paper, preprint, thesis, forum
post, or GitHub note that appears to solve the first open case `k = 5` or the
full all-`k` conjecture.

## Verdict

I did not find any post-2019 work claiming or proving `k = 5`, nor any work
claiming or proving the all-`k` conjecture.

Current risk assessment:

- Direct published/preprint solution of `k = 5`: low.
- Direct published/preprint all-`k` solution: very low.
- Unincorporated partial or computational notes: moderate. The 2026 forum/GitHub
  note below is exactly this type of object, but it explicitly says it is not a
  solution of EP885.

The main adversarial caveat is vocabulary drift. A solution could be described
under square translates, close factorizations, rational points, elliptic curves,
or short-interval divisors without mentioning "EP885" or "factor-difference
set". I searched those variants as well; the post-2019 hits found there are
adjacent, not solutions.

## Queries used

Direct EP885 queries:

- `"Erdos Problem #885" OR "Erdos Problem #885"`
- `"Erdos Problem 885" "factor" "difference"`
- `"E885" "Erdos" "factor-difference"`
- `"erdosproblems.com/885"`
- `"Erdos Problem 885" "k = 5"`
- `"Erdos Problem 885" examples`
- `"D(79200)" "227205"`
- `"79200" "227205" "1258560" "1028"`
- `"756000" "15971200" "45130176"`
- `"330" "870" "2445" "4155" "10482" "756000"`

Direct title/phrase queries:

- `"factor-difference set" "Erdos" post 2019 OR 2020 OR 2021 OR 2022 OR 2023 OR 2024 OR 2025 OR 2026`
- `"common factor differences" "Erdos" "Bremner"`
- `"common factor difference" "k=5"`
- `"factor difference set" "k=5"`
- `"for every k" "factor-difference set"`
- `"for every positive integer" "common factor differences"`
- `"sets of five integers" "common factor differences"`
- `"five common factor differences" "Erdos"`
- `"Bremner" "five" "common factor differences"`
- `"Andrew Bremner" "factor-difference"`

Preprint/database queries:

- arXiv API: `all:"factor-difference set"`
- arXiv API: `all:"common factor differences"`
- arXiv API: `all:"common factor difference"`
- arXiv API: `all:"Erdos" AND all:"Rosenfeld" AND all:"factor" AND all:"difference"`
- arXiv API: `all:"Bremner" AND all:"common factor differences"`
- arXiv API: `all:"square translates" AND all:"perfect squares"`
- Crossref API: `"factor-difference set"`
- Crossref API: `"common factor differences"`
- Crossref API: `"Erdos Problem 885"`
- Crossref API: `"factor difference set" "Erdos"`
- Semantic Scholar API: DOI `10.1142/S1793042119500581`
- Semantic Scholar API: `factor-difference set`, `common factor differences`,
  `Erdos Problem 885`, `Bremner common factor differences`

Forum/GitHub/thesis queries:

- `site:github.com "factor-difference set"`
- `site:github.com "common factor differences"`
- `site:github.com "E885" "factorDiffSet"`
- `site:github.com "Erdos" "885" "factorDiffSet"`
- GitHub repository API: `Erdos 885`, `factor-difference set`,
  `common factor differences`, `factorDiffSet E885`
- `"new_3row_5col_packet"`
- `"guidepost_seed_rigid"`
- `"factorDiffSet" "E885"`
- `"FormalConjectures/Problems/Erdos/E885"`
- `"factor-difference set" thesis`
- `"common factor differences" thesis`
- `"Erdos and Rosenfeld" "factor-difference" thesis`
- `"Erdos and Rosenfeld" "factor-difference" dissertation`

Adjacent-language queries:

- `"simultaneous square translates" "Erdos"`
- `"square translates" "factor differences"`
- `"z^2+a" "z^2+b" "z^2+c" "perfect squares" "Erdos"`
- `"z^2+a" "z^2+b" "z^2+c" "perfect squares" "five"`
- `"12 distinct integers" "five partitions" "sums of the squares"`
- `"5 partitions" "6-tuples" "sums of squares" "Tarry"`
- `"Hua" "Tarry's problem" "factor-difference"`
- `"more than 4 small differences" "factor-difference"`

## Sources checked

### Official EP885 page and thread

- [Erdos Problem #885](https://www.erdosproblems.com/885), accessed
  2026-04-26.
  - Status is still `OPEN`.
  - The page states the problem and lists only the known cases `k = 2`,
    `k = 3`, and `k = 4`.
  - It also warns that the website's open status may miss literature, so this
    page is not treated as conclusive by itself.
- [EP885 LaTeX source](https://www.erdosproblems.com/latex/885), accessed
  2026-04-26.
  - References listed: Erdos-Rosenfeld 1997, Jimenez-Urroz 1999, Bremner 2019.
  - No post-2019 direct reference is listed.
- [EP885 history](https://www.erdosproblems.com/history/885), accessed
  2026-04-26.
  - The recorded current version still lists only the `k = 2,3,4` chain.
- [EP885 discussion thread](https://www.erdosproblems.com/forum/thread/885),
  accessed 2026-04-26.
  - The page header says no solution or partial solution is incorporated into
    the remarks.
  - The visible 2026 comment is a partial note, not a solution.

Assessment: no official indication of `k = 5` or all-`k` being solved.

### Primary direct literature

- Paul Erdos and Moshe Rosenfeld, "The factor-difference set of integers",
  Acta Arithmetica 79 (1997), 353-359.
  - Official metadata/full text: [IMPAN](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/79/4/109554/the-factor-difference-set-of-integers),
    [EuDML](https://eudml.org/doc/206983), [DOI](https://doi.org/10.4064/aa-79-4-353-359).
  - Role: poses the conjecture and proves the `k = 2` case in stronger form.
  - It includes Barry Guiduli examples of three integers sharing four
    differences; these are examples, not `k = 4` or `k = 5` witnesses.
- Jorge Jimenez-Urroz, "A Note on a Conjecture of Erdos and Rosenfeld",
  Journal of Number Theory 78.1 (1999), 140-143.
  - Links: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022314X99924071),
    [DOI](https://doi.org/10.1006/jnth.1999.2407), [author publications page](https://web.mat.upc.edu/jorge.urroz/papers.htm).
  - Role: proves a special case, recorded elsewhere as the `k = 3` case.
  - ScienceDirect reports "Cited by (0)" on the page checked.
- Andrew Bremner, "On a problem of Erdos related to common factor differences",
  International Journal of Number Theory 15.5 (2019), 1059-1068.
  - Links: [ASU/Arizona Regents metadata](https://experts.azregents.edu/en/publications/on-a-problem-of-erd%C3%B6s-related-to-common-factor-differences/),
    [ResearchGate preview](https://www.researchgate.net/publication/329314619_On_a_problem_of_Erdos_related_to_common_factor_differences),
    [DOI](https://doi.org/10.1142/S1793042119500581).
  - Role: proves `k = 4`, by proving infinitely many sets of four integers with
    four common factor differences.
  - This is the latest direct peer-reviewed advance found.

Assessment: direct literature chain stops at `k = 4`.

### Citation and preprint surfaces

- Crossref work lookup for Bremner 2019 DOI
  (`10.1142/S1793042119500581`).
  - `is-referenced-by-count`: 0 in Crossref on 2026-04-26.
  - Publisher references only Erdos-Rosenfeld 1997, Jimenez-Urroz 1999, and
    Piepmeyer 1996.
- Semantic Scholar DOI lookup for Bremner 2019.
  - `citationCount`: 0 on 2026-04-26.
  - No citing papers returned.
- arXiv API exact/near-exact searches:
  - No results for exact direct phrases `factor-difference set`,
    `common factor differences`, `common factor difference`,
    the combined Erdos-Rosenfeld factor/difference query, or the Bremner query.

Assessment: no citation/preprint trail to a post-2019 direct solution surfaced.

### Post-2019 forum/GitHub note

- Sam Mausberg, "Two Formalized Partial Results Related to Erdos Problem E885",
  2026 forum/GitHub note bundle.
  - Forum comment: [EP885 thread](https://www.erdosproblems.com/forum/thread/885).
  - GitHub bundle: [ForumNote directory](https://github.com/SamMausberg/lean-formalizations/tree/main/FormalConjectures/Problems/Erdos/E885/ForumNote).
  - Raw LaTeX note: [erdos885_forum_note.tex](https://raw.githubusercontent.com/SamMausberg/lean-formalizations/main/FormalConjectures/Problems/Erdos/E885/ForumNote/erdos885_forum_note.tex).
  - Companion README: [erdos885_forum_note_README.md](https://raw.githubusercontent.com/SamMausberg/lean-formalizations/main/FormalConjectures/Problems/Erdos/E885/ForumNote/erdos885_forum_note_README.md).

Contents checked:

- It explicitly says it is not a solution of EP885.
- It records an anchored three-shift square-translate packet:
  `{330, 870, 2445, 4155, 10482}` for shifts
  `(756000, 15971200, 45130176)`.
- It records the exact finite computation
  `D(79200) cap D(227205) cap D(1258560) = {36, 468, 692, 1028}`.
- The GitHub README says the forum-facing note intentionally restricts itself
  to two partial results.

Assessment: relevant partial result and useful examples, but explicitly not a
`k = 5` or all-`k` solution.

### Adjacent post-2019 work

- Tsz Ho Chan, Laura Holmes, Michael Liu, Jose Villarreal,
  "Numbers with Four Close Factorizations", arXiv:2508.02818 (2025).
  - Link: [arXiv:2508.02818](https://arxiv.org/abs/2508.02818).
  - Studies numbers with four close factorizations and transforms the question
    into generalized Pell equations.
  - This is close to the "small factor differences" branch, but it does not
    claim common factor differences across five `N_i` and does not solve EP885.
- Patrick Letendre, "Divisors of an Integer in a Short Interval",
  arXiv:2503.12146 (2025).
  - Link: [arXiv:2503.12146](https://arxiv.org/abs/2503.12146).
  - Broad short-interval divisor-counting work.
  - Relevant to close divisors, not a direct EP885 solution.
- Tsz Ho Chan, "Factors of almost squares and lattice points on circles",
  arXiv:1406.2230 (2014).
  - Link: [arXiv:1406.2230](https://arxiv.org/abs/1406.2230).
  - Pre-2019, checked because later work cites/extends this branch.
  - Adjacent close-divisor problem, not a direct solution.

Assessment: adjacent work does not collapse `k = 5` or all-`k`.

### Elsewhere listed with examples

- [OEIS A368312](https://oeis.org/A368312): "Irregular triangle read by rows
  where row n lists the factor differences of n."
  - Gives correct row examples, e.g. `n=4: 0, 3`, `n=6: 1, 5`,
    `n=9: 0, 8`.
  - This lists the object `D(n)`, not the EP885 conjecture itself.
- [OEIS A368571](https://oeis.org/A368571): triangle where `T(n,k)` counts
  positive integers `M` having both `n` and `k` as factor differences.
  - Cites Erdos-Rosenfeld and gives a formula from Proposition 3.1.
  - This is a related pair-count sequence, not a `k = 5` witness.
- [Kuloverse blog: "Erdos Problem 885: Exploring The Factor Difference Set"](https://kuloverse.site/blog/erdos-problem-885-exploring-the),
  2025.
  - It retells EP885 and says it is open.
  - It gives an example `D(12)` by subtracting all pairs of divisors, which is
    not the EP885 definition. Under the actual definition `ab = 12`, only factor
    pairs `(1,12)`, `(2,6)`, `(3,4)` contribute, so `D(12) = {1,4,11}`.
  - Treat this as a non-authoritative listing only.
- Original Erdos-Rosenfeld paper examples:
  - It includes Barry Guiduli examples of three integers sharing four common
    factor differences.
  - These are important examples/near-misses but not EP885 witnesses for
    `k = 4` or `k = 5` because they have only three `N_i`.
- EP885 forum/GitHub 2026 examples:
  - The anchored square-translate packet and the triple intersection above are
    listed publicly and are useful seeds.

Assessment: the problem/object is listed outside the official page, especially
in OEIS, but I found no external listing containing a correct `k = 5` example.

## Adversarial conclusion

The most credible current public state is:

- `k = 2`: Erdos-Rosenfeld 1997.
- `k = 3`: Jimenez-Urroz 1999.
- `k = 4`: Bremner 2019.
- `k = 5`: still first open case in the checked public record.

The 2026 Mausberg forum/GitHub note is the only post-2019 EP885-specific item
found. It should be incorporated as a partial-results/example source, not as a
solution-risk blocker.

Recommended next risk check, if this project moves toward a claim:

1. Obtain the full Bremner 2019 article and inspect its final remarks and any
   unpublished-construction references.
2. Run authenticated Google Scholar/MathSciNet/zbMATH citation checks for
   Bremner 2019 and Jimenez-Urroz 1999.
3. Repeat GitHub code search with an authenticated token for `factorDiffSet`,
   `E885`, and the concrete example numbers.
4. Search non-English thesis repositories for exact phrases from the original
   paper and for square-translate formulations.
