# EP885 known constructions

Date: 2026-04-26.  Accents are omitted in body text for plain-text portability.

This note translates the known `k = 2, 3, 4` literature into the local
incidence language

```text
d ~ N  iff  d in D(N)  iff  exists a >= 1 with N = a(a+d).
```

A certificate is therefore a biclique: sorted `N_values`, sorted `deltas`, and
factor pairs `(a, a+d)` for every incidence.

## Sources and retrieval status

- EP885 page and LaTeX source, accessed 2026-04-26:
  <https://www.erdosproblems.com/885>,
  <https://www.erdosproblems.com/latex/885>.  The page states the problem,
  says the current status is open, and records known cases `k = 2`
  (Erdos--Rosenfeld), `k = 3` (Jimenez-Urroz), and `k = 4` (Bremner).
- Paul Erdos and Moshe Rosenfeld, "The factor-difference set of integers",
  Acta Arithmetica 79.4 (1997), 353-359.  Metadata/full article link:
  <https://eudml.org/doc/206983>.
- Jorge Jimenez-Urroz, "A Note on a Conjecture of Erdos and Rosenfeld",
  Journal of Number Theory 78.1 (1999), 140-143, DOI
  `10.1006/jnth.1999.2407`.  ScienceDirect exposes metadata/abstract:
  <https://www.sciencedirect.com/science/article/pii/S0022314X99924071>.
  The author's publications page links a DVI:
  <https://web.mat.upc.edu/jorge.urroz/papers.htm>,
  <https://web.mat.upc.edu/jorge.urroz/erdosros.dvi>.  A local copy exists at
  `erdos/885/literature/jimenez-urroz-erdosros.dvi`; the large example below
  was extracted from it and verified.
- Andrew Bremner, "On a problem of Erdos related to common factor
  differences", International Journal of Number Theory 15.5 (2019),
  1059-1068, DOI `10.1142/S1793042119500581`.  Accessible metadata/preview:
  <https://experts.azregents.edu/en/publications/on-a-problem-of-erd%C3%B6s-related-to-common-factor-differences/>,
  <https://www.researchgate.net/publication/329314619_On_a_problem_of_Erdos_related_to_common_factor_differences>.
  Direct publisher PDF/ePDF/abstract fetches from World Scientific returned
  HTTP 403 from this workspace.  OpenAlex reports `is_oa: false`,
  `oa_status: closed`, no OA URL, and no repository full text.  Therefore the
  theorem-level `k = 4` result is recorded below, but the explicit Bremner
  construction has not been reconstructed here.

## Algebra used by all examples

For `d >= 0`,

```text
d in D(N)
<=> exists a >= 1 such that N = a(a+d)
<=> d^2 + 4N is a square s^2 and s == d mod 2.
```

If the common differences are `d_1, ..., d_t`, then every common `N` gives
simultaneous square translates

```text
d_j^2 + 4N = square,    j = 1, ..., t.
```

Equivalently, with `d_j = 2e_j` and `N = x_j^2 - e_j^2`, three common
differences reduce to

```text
x^2 - y^2 = e_1^2 - e_2^2,
x^2 - z^2 = e_1^2 - e_3^2.
```

Putting `lambda = x^2`, this means `lambda`, `lambda-A`, and `lambda-B` are
squares for `A = e_1^2 - e_2^2`, `B = e_1^2 - e_3^2`.  This is the bridge to
elliptic curves of the form

```text
E(A,B): Y^2 = X(X-A)(X-B).
```

The standard full-2-torsion descent criterion says that a rational point
`P = (X,Y)` on `E(A,B)` is in `2E(Q)` exactly when the three quantities
`X`, `X-A`, and `X-B` are rational squares, away from the 2-torsion
exceptional cases.  Positive rank then gives infinitely many rational
solutions; clearing denominators gives integer differences and integer `N`.

## k = 2: Erdos--Rosenfeld

Theorem statement used here: for every positive integer `r`, there exist
`r` integers `N_1 < ... < N_r` such that

```text
|D(N_1) cap ... cap D(N_r)| >= 2.
```

This proves EP885 for `k = 2`.

Construction.  Let `P = p_1 ... p_m` be a product of distinct odd primes, and
split its prime factors into two complementary products `U` and `V`.  Put

```text
alpha = (U+V)/2,
beta  = (U-V)/2,
```

so `(alpha-beta)(alpha+beta) = UV = P`.  For any factorization `m_1 m_2 = P`,
set

```text
x = (m_1+m_2)/2,
y = (m_1-m_2)/2.
```

Then

```text
x^2 - alpha^2 = y^2 - beta^2 =: N.
```

Thus `N = (x-alpha)(x+alpha)` has factor difference `2 alpha`, and
`N = (y-beta)(y+beta)` has factor difference `2 |beta|`.  Taking `P` with
enough divisors gives as many distinct positive `N` as needed.

Small explicit instance.  Take `P = 3*5*7 = 105`, `U = 15`, `V = 7`.  Then
`alpha = 11`, `beta = 4`, and the common differences are `22` and `8`.
The factorizations of `105` give the distinct positive values

```text
N_values = [48, 240, 2688]
deltas   = [8, 22]
```

Factor-pair certificate:

```text
48   = 4*12   = 2*24
240  = 12*20  = 8*30
2688 = 48*56  = 42*64
```

so `{8,22} subset D(48) cap D(240) cap D(2688)`.

Erdos--Rosenfeld also record two Barry Guiduli `K_{4,3}` seeds.  They are not
EP885 `k = 4` witnesses because there are only three `N` values, but they are
useful regression data:

```text
N_values = [6925500, 37901500, 108448956]
deltas   = [420, 3780, 14940, 76860]
```

```text
N_values = [2778300, 862552800, 5400442044]
deltas   = [420, 3780, 61695, 154332]
```

## k = 3: Jimenez-Urroz

Theorem statement used here: for every positive integer `r`, there exist
`r` integers `N_1 < ... < N_r` such that

```text
|D(N_1) cap ... cap D(N_r)| >= 3.
```

This proves EP885 for `k = 3`.

Method.  Jimenez-Urroz uses the square-translate/elliptic-curve reduction
above.  For fixed rational `A,B`, rational solutions of

```text
lambda, lambda-A, lambda-B all squares
```

are obtained from points in `2E(Q)` on

```text
E(A,B): Y^2 = X(X-A)(X-B).
```

A positive-rank example gives infinitely many rational points, hence
arbitrarily many rational square triples.  A common denominator clearing then
turns those into integer differences and integer `N` values.  The DVI example
uses the positive-rank case corresponding to `(A,B) = (4,6)` after scaling.

Explicit DVI example.  The following five integers share the following three
differences:

```text
deltas = [
  20948274110993405271036818636118416362912097297024759288,
  573704451935072432558657786561844237570109187841809114488,
  993243542205992332488058754263122078071239561123822165112,
]

N_values = [
  10162103952376812065984068367034286997213074008329441494778721098448355310617860988252607807756465444631925346864,
  42477647204058801499996894620438584695302071737432167732088209568215006571676202953757168308992222942860506726420,
  55255329302305667616382031961582117515131715299039049127712034438375518437082118207222225979167289125630480117753,
  150663274529569282064072003646177602927377024496937825623312349879413129373761483685425020517086615471768268066864,
  416252465020561454407395364419197194144012042895155178800638062718880469015509289397065832372310217474579962921088,
]
```

The scaling check against `(A,B)=(4,6)` is:

```text
d_3^2 - d_2^2 = 4 q^2,
d_3^2 - d_1^2 = 6 q^2,

q = 405399782919214522896010939580712190029199098946908977760.
```

The local verifier confirms all `5*3` incidences.  The values above should be
copied directly from this note or the DVI; manual retyping is error-prone.

## k = 4: Bremner

Theorem statement: Bremner proves the result true for `k = 4` by proving that
there are infinitely many sets of four integers with four common factor
differences.

The local PDF was obtained on 2026-04-26:

```text
Andrew Bremner, "On a problem of Erdos related to common factor differences",
International Journal of Number Theory 15.5 (2019), 1059-1068,
DOI 10.1142/S1793042119500581.
```

Local path:

```text
erdos/885/On a problem of Erdos related to common factor differences_ -- Bremner, Andrew ... .pdf
```

The paper uses half-differences `(x_0,y_0,z_0,t_0)`.  In the local incidence
language the deltas are twice those values.

First explicit K4,4 certificate:

```text
N_values = [26128575, 291722431, 561117375, 713526975]
deltas   = [126, 16110, 33390, 75390]
```

Verified in:

```text
erdos/885/results/bremner-example-1-k44-certificate.json
```

Second explicit K4,4 certificate:

```text
N_values = [26941381929, 94011840000, 455923353600, 728783193600]
deltas   = [83160, 451528, 910800, 1386000]
```

Verified in:

```text
erdos/885/results/bremner-example-2-k44-certificate.json
```

Third explicit K4,4 certificate:

```text
N_values = [
  3682673190625,
  94040161560576,
  292916434882500,
  1488767454720000
]
deltas = [1441440, 15615600, 27986400, 48620880]
```

Verified in:

```text
erdos/885/results/bremner-example-3-k44-certificate.json
```

The paper's concluding remark says the five-difference case appears much
harder because it leads to a system of 20 quadratic equations.  That matches
the local computational picture: the known K4,4 objects are real, but promoting
them to K5,5 is not a trivial extension step.

Cheap extension checks on the first certificate are recorded in
`sprint-4-bremner-found.md`.

## Forum and other verified seeds

The 2026 EP885 forum note gives another useful `K_{4,3}` object:

```text
N_values = [79200, 227205, 1258560]
deltas   = [36, 468, 692, 1028]
```

with exact intersection

```text
D(79200) cap D(227205) cap D(1258560) = {36, 468, 692, 1028}.
```

This is locally verified in `erdos/885/notes/verified-forum-triple.md` and
`erdos/885/results/forum-triple-certificate.json`.  The forum reply's value
`1029` is a typo; direct verification gives `1028`.

## Feeding examples into the local verifier

Use `scripts/verify_biclique.py`.  It takes comma-separated `--n` and `--d`
lists and optionally writes JSON with `--out`.

Small `k = 2` regression:

```powershell
python .\erdos\885\scripts\verify_biclique.py `
  --n "48,240,2688" `
  --d "8,22"
```

Guiduli seed 1:

```powershell
python .\erdos\885\scripts\verify_biclique.py `
  --n "6925500,37901500,108448956" `
  --d "420,3780,14940,76860"
```

Guiduli seed 2:

```powershell
python .\erdos\885\scripts\verify_biclique.py `
  --n "2778300,862552800,5400442044" `
  --d "420,3780,61695,154332"
```

Forum seed:

```powershell
python .\erdos\885\scripts\verify_biclique.py `
  --n "79200,227205,1258560" `
  --d "36,468,692,1028"
```

Jimenez-Urroz DVI example:

```powershell
$n = @(
  "10162103952376812065984068367034286997213074008329441494778721098448355310617860988252607807756465444631925346864",
  "42477647204058801499996894620438584695302071737432167732088209568215006571676202953757168308992222942860506726420",
  "55255329302305667616382031961582117515131715299039049127712034438375518437082118207222225979167289125630480117753",
  "150663274529569282064072003646177602927377024496937825623312349879413129373761483685425020517086615471768268066864",
  "416252465020561454407395364419197194144012042895155178800638062718880469015509289397065832372310217474579962921088"
) -join ","

$d = @(
  "20948274110993405271036818636118416362912097297024759288",
  "573704451935072432558657786561844237570109187841809114488",
  "993243542205992332488058754263122078071239561123822165112"
) -join ","

python .\erdos\885\scripts\verify_biclique.py --n $n --d $d
```

## Feeding examples into the search scripts

The current search scripts do not accept a manual seed file.  Without editing
scripts, there are only two ways to make a known example appear in a search:

1. Exact delta-first search: choose `--x >= max(N_values)`,
   `--delta-max >= max(deltas)`, `--min-support` equal to the number of common
   `N` values you want to detect, and `--target-k` equal to the number of
   deltas.  This is feasible for the small/forum examples and not feasible for
   the Jimenez-Urroz DVI-scale values.

2. Stage A search: choose parameters so the candidate generator happens to
   include the desired `N` values.  There is no current CLI for injecting manual
   candidates, and the Jimenez-Urroz values are far outside the intended Stage A
   range.

Example exact run that should include the small `k = 2` construction:

```powershell
python .\erdos\885\delta_first_search.py `
  --x 2688 `
  --delta-max 22 `
  --min-support 3 `
  --target-k 2 `
  --out-dir erdos\885\runs\manual_k2_small
```

Example exact run sized to include the forum `K_{4,3}` seed:

```powershell
python .\erdos\885\delta_first_search.py `
  --x 1258560 `
  --delta-max 1028 `
  --min-support 3 `
  --target-k 4 `
  --out-dir erdos\885\runs\manual_forum_K4_3
```

Use fresh output directories; the current scripts overwrite files in existing
directories.
