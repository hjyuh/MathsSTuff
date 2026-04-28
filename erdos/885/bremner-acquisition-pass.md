# EP885 Bremner 2019 acquisition pass

Date: 2026-04-26.

Scope: locate legally usable data from Andrew Bremner, "On a problem of
Erdos related to common factor differences", International Journal of Number
Theory 15(5), 1059-1068, DOI `10.1142/S1793042119500581`, sufficient to build
an EP885 `K_{4,4}` verifier certificate.

## Verdict

No explicit Bremner `K_{4,4}` seed, construction formula, or full legal article
text was found in the workspace or on accessible public web surfaces in this
pass.

What was found:

- theorem-level confirmation that Bremner proves the `k = 4` case by producing
  infinitely many sets of four integers with four common factor differences;
- the first-page problem setup and geometric-to-factor-difference reduction
  from the publisher preview surfaced by ResearchGate;
- strong open-access evidence that the article is closed: OpenAlex, Unpaywall,
  and Semantic Scholar all report no OA PDF/repository copy;
- a direct author contact route: `bremner@asu.edu`.

Most promising legal route: email Andrew Bremner directly for either an
author-shareable accepted manuscript or the specific theorem/construction data
needed to produce one `K_{4,4}` certificate. Institutional access through World
Scientific is the next best route.

## Local sources inspected

- `erdos/885/known-constructions.md`
  - Records Bremner 2019 as the `k = 4` source.
  - Already notes that publisher PDF/ePDF/abstract fetches returned HTTP 403
    from the workspace.
  - Contains no Bremner numeric `K_{4,4}` seed.
- `erdos/885/literature-search.md`
  - Gives the direct literature chain and states that Bremner proves `k = 4`.
  - Contains no full construction data.
- `erdos/885/literature-risk-pass.md`
  - Confirms no later direct public solution found and identifies Bremner 2019
    as the latest direct peer-reviewed advance.
  - Contains no Bremner seed.
- `erdos/885/literature/initial-sources.md`
  - Lists the article metadata and source URLs only.
- `erdos/885/algebraic-lifting-notes.md`
  - Explains why future Bremner `K_{4,4}` data are needed for product/lift
    tests.
  - Contains no Bremner data.
- `erdos/885/seed-extension-plan.md` and `erdos/885/sprint-2-status.md`
  - Treat Bremner extraction as the main blocker.
- `erdos/885/literature/jimenez-urroz-erdosros.dvi`
  - Local `k = 3` source only; not Bremner.
- Local `k4.jsonl` outputs under `erdos/885/out_*` and
  `erdos/885/runs/20260426_150000_deltafirst_K44_X1e7_D5e3/k4.jsonl`
  are zero bytes.

Workspace-wide targeted sweeps for `Bremner`, `1950058`,
`1793042119500581`, and `common factor differences` did not expose a local
Bremner PDF or seed. Some broad recursive searches timed out in unrelated large
directories, but the relevant `erdos/885` tree was inspected directly.

## Web sources checked

### Official EP885 surfaces

- <https://www.erdosproblems.com/885>
  - Accessible.
  - States the problem with `D(n) = {|a-b| : n = ab}`.
  - Status is `OPEN`.
  - Records `k = 2` by Erdos--Rosenfeld, `k = 3` by Jimenez-Urroz, and
    `k = 4` by Bremner.
  - Says no solution or partial solution is claimed in incorporated comments.
- <https://www.erdosproblems.com/latex/885>
  - Accessible.
  - Lists `[Br19] Bremner, Andrew, On a problem of Erdos related to common
    factor differences. Int. J. Number Theory (2019), 1059--1068.`
- <https://www.erdosproblems.com/history/885>
  - Accessible.
  - Current version still lists only the same known `k = 2,3,4` chain.
- <https://www.erdosproblems.com/forum/thread/885>
  - Accessible.
  - Contains 2026 partial forum data, but no Bremner seed.

### Bremner article metadata and previews

- <https://asu.elsevierpure.com/en/publications/on-a-problem-of-erd%C3%B6s-related-to-common-factor-differences/>
  - Accessible.
  - Gives title, author, pages `1059-1068`, journal `International Journal of
    Number Theory`, volume `15`, issue `5`, DOI, and keywords:
    `Erdos problem`, `common factor difference`, `elliptic curve`.
  - Abstract confirms the `k = 4` theorem-level result.
  - No full text or seed data.
- <https://experts.azregents.edu/en/publications/on-a-problem-of-erd%C3%B6s-related-to-common-factor-differences/>
  - Accessible.
  - Same metadata as the ASU Pure page.
  - "Access to Document" points only to the DOI.
- <https://www.researchgate.net/publication/329314619_On_a_problem_of_Erdos_related_to_common_factor_differences>
  - Accessible.
  - Provides a World Scientific publisher preview, apparently only page 1059.
  - Full text is not downloadable without request/sign-in.
  - Page says the author has not claimed the publication on ResearchGate.
  - Gives author email in preview: `bremner@asu.edu`.
- <https://math.la.asu.edu/~andrew/>
  - Accessible.
  - Confirms Andrew Bremner's ASU page and email `bremner@asu.edu`.
  - No publication list or paper PDF found from the visible homepage.
- <https://eurekamag.com/research/104/208/104208297.php>
  - Accessible.
  - Gives metadata/summary only plus a paid full-text article service.
  - Not used for data; no theorem details or seed.
- <https://ftp.math.utah.edu/pub/tex/bib/ijnt.pdf>
  - Search-visible bibliography entry only.
  - Confirms the bibliographic listing/DOI; no article text.

### Publisher endpoints

All of these returned HTTP `403 Forbidden` from this workspace by both HEAD and
GET checks:

- <https://www.worldscientific.com/doi/abs/10.1142/S1793042119500581>
- <https://www.worldscientific.com/doi/pdf/10.1142/S1793042119500581>
- <https://www.worldscientific.com/doi/epdf/10.1142/S1793042119500581>
- <https://www.worldscientific.com/doi/full/10.1142/S1793042119500581>

### Index/API checks

- Crossref API:
  <https://api.crossref.org/works/10.1142/S1793042119500581>
  - Accessible.
  - Publisher: World Scientific.
  - `is-referenced-by-count`: `0`.
  - Published online date from Crossref: `2019-05-28`; print date:
    `2019-06`; pages `1059-1068`.
  - Crossref lists a PDF URL, but only as a publisher link:
    <https://www.worldscientific.com/doi/pdf/10.1142/S1793042119500581>,
    which is blocked here.
  - References listed only three DOIs:
    `10.4064/aa-79-4-353-359`, `10.1007/BF02711135`,
    `10.1006/jnth.1999.2407`.
- OpenAlex API:
  <https://api.openalex.org/works/doi:10.1142/S1793042119500581>
  - Accessible.
  - `is_oa: false`, `oa_status: closed`, `oa_url: null`,
    `any_repository_has_fulltext: false`, `pdf_url: null`.
  - `cited_by_count: 0`.
- Unpaywall API:
  <https://api.unpaywall.org/v2/10.1142/S1793042119500581?email=research@example.org>
  - Accessible.
  - `is_oa: false`, `oa_status: closed`, `has_repository_copy: false`,
    `oa_locations: []`.
- Semantic Scholar API:
  <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1142/S1793042119500581>
  - Accessible.
  - `isOpenAccess: false`.
  - `openAccessPdf.status: CLOSED`.
  - `citationCount: 0`.
- zbMATH author profile:
  <https://zbmath.org/authors/?q=ai%3Abremner.andrew>
  - Accessible.
  - Confirms Bremner author profile and homepage link.
  - Did not expose the article body or seed.
- GitHub code search API:
  - Exact title/DOI queries returned HTTP `401 Unauthorized`.
  - Web search for GitHub-hosted exact title/DOI did not surface a result.
- arXiv web search:
  - Exact phrase searches for the title, `common factor differences`, and
    `factor-difference set` surfaced no Bremner preprint.
  - A local arXiv API batch timed out, so this is not counted as a definitive
    arXiv API result.

Illegal/piracy sources were deliberately not queried or used.

## Explicit numbers and formulas found

Bibliographic data:

- Title: `On a problem of Erdos related to common factor differences`.
- Author: Andrew Bremner.
- Journal: `International Journal of Number Theory`.
- Volume/issue/pages: `15(5):1059-1068`.
- DOI: `10.1142/S1793042119500581`.
- ResearchGate preview dates: received `2018-07-02`, accepted `2018-11-26`,
  published `2019-01-14`.
- Crossref dates: published online `2019-05-28`, print `2019-06`.
- ASU metadata state: published `2019-06-01`.

Problem/formula data from accessible sources:

```text
D(n) = {|a-b| : ab = n}.
```

EP885 asks for, for every `k >= 1`, integers

```text
N_1 < ... < N_k
```

with

```text
| intersection_i D(N_i) | >= k.
```

The ResearchGate/World Scientific first-page preview includes the geometric
motivation:

```text
4 p_j^2 =
(2 d_{i,j} - (2 k_i + 1)) (2 d_{i,j} + (2 k_i + 1)),
```

so each `4 p_j^2` has factor difference

```text
4 k_i + 2.
```

Local verifier algebra already used by the project:

```text
d in D(N)
iff exists a >= 1 with N = a(a+d)
iff d^2 + 4N is a square s^2 and s == d mod 2.
```

No explicit Bremner deltas, `N` values, elliptic curve, parameterization, or
factor-pair matrix were found.

## Acquisition route

### Best route: direct author request

Use the email address visible both on Bremner's ASU homepage and in the
publisher preview:

```text
bremner@asu.edu
```

Suggested subject:

```text
Request for author manuscript or construction data for IJNT 2019 common factor differences paper
```

Suggested email:

```text
Dear Professor Bremner,

I am working through Erdos Problem 885 and trying to build a small exact
verifier certificate for the known k = 4 case from your paper

  Andrew Bremner, "On a problem of Erdos related to common factor differences",
  International Journal of Number Theory 15(5), 1059-1068 (2019),
  DOI 10.1142/S1793042119500581.

I do not currently have legal full-text access. Would you be willing to share an
author-distributable manuscript, or alternatively the specific construction data
needed to verify one K_{4,4} example?

The minimum data I need are:

  1. four common factor differences d_1,...,d_4;
  2. four integers N_1 < ... < N_4;
  3. optionally, the factor pairs a_{ij}(a_{ij}+d_i)=N_j for all 16 incidences,
     or the theorem/formulas from which those values are generated.

I am only looking to verify the construction by exact arithmetic and cite the
paper properly; I am not asking for any unauthorized copy.

Best,
```

### Second route: institutional access

Use a university/library World Scientific subscription or interlibrary loan for:

```text
Andrew Bremner,
"On a problem of Erdos related to common factor differences",
International Journal of Number Theory 15(5), 1059-1068,
DOI 10.1142/S1793042119500581.
Publisher URL: https://www.worldscientific.com/doi/10.1142/S1793042119500581
```

Pages needed: all pages `1059-1068`. The first preview page is not enough; the
construction must occur after the introduction.

### Third route: ResearchGate request

ResearchGate offers "Request full-text", but the page says Bremner has not
claimed the publication there, so this is probably weaker than direct email.
URL:

```text
https://www.researchgate.net/publication/329314619_On_a_problem_of_Erdos_related_to_common_factor_differences
```

## Data needed for certificate intake

Once the paper or author response is obtained, normalize the seed as:

```json
{
  "id": "bremner_2019_k44",
  "source": "Bremner 2019, DOI 10.1142/S1793042119500581",
  "n_values": ["... four integers ..."],
  "deltas": ["... four differences ..."],
  "relations": [
    {"n": "...", "delta": "...", "a": "...", "b": "..."}
  ]
}
```

If only deltas and `N` values are given, recover each relation with:

```text
s^2 = d^2 + 4N,
a = (s - d) / 2,
b = a + d.
```

Acceptance condition: all 16 relations satisfy `a*b = N` and `b-a = d` with
positive integers `a,b`.
