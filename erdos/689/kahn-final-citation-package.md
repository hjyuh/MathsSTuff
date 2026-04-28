# Kahn (1996) citation package for the EP689 rounding step

Created: 2026-04-25

Scope: finish the Kahn citation + application package as far as possible
*without* Wiley/publisher PDF access. This note is citation-facing: it records
exact metadata, the theorem statement in a cite-ready form (with caveats), and
the exact EP689 verification needed to apply the theorem. It does **not**
re-prove preprocessing; see the AWN note for that.

Companion notes:

- [kahn-citation-verification.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-citation-verification.md)
- [kahn-alpha-paper-check.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-alpha-paper-check.md)
- [awn-preprocessing-mass-loss.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\awn-preprocessing-mass-loss.md)


## 0. Target reference (what we are citing)

Jeff Kahn, *A linear programming perspective on the Frankl--Rodl--Pippenger
theorem*, Random Structures and Algorithms **8** (1996), no. 2, 149--157.

We want Theorem 1.5 (as numbered in the abstract/preview sources) as a rounding
statement: a fractional matching with small pair co-load and a quadratic
condition can be rounded to an (almost as large) genuine matching preserving a
finite list of statistics. For EP689 we only need the single statistic
`C \equiv 1` (matching size).


## 1. What is verified without the publisher PDF

### 1.1 Bibliographic metadata (Crossref + DBLP + Rutgers)

Stable metadata agreed by major indices:

- Journal: *Random Structures and Algorithms*
- Volume/issue: 8(2)
- Month/year: March 1996
- Pages: 149--157
- Publisher: Wiley
- ISSN: 1042-9832 (print), 1098-2418 (electronic)

DOI ambiguity is real in secondary sources, but resolvable:

- Crossref has **two** DOI records:
  - `10.1002/(SICI)1098-2418(199603)8:2<149::AID-RSA5>3.0.CO;2-Y`
  - `10.1002/(SICI)1098-2418(199603)8:2<149::AID-RSA5>3.3.CO;2-S`
- As of **2026-04-25**, `doi.org` issues a `301 Moved Permanently` from the
  `3.3.CO;2-S` DOI to the `3.0.CO;2-Y` DOI, so the `3.3` DOI is an alias and
  `3.0` is the canonical target.
- The Rutgers "Cite this" widget currently displays the `3.3` DOI; DBLP and
  DeepDyve display the `3.0` DOI.

Practical upshot for our bibliography: use the `3.0.CO;2-Y` DOI, and optionally
note `3.3.CO;2-S` as an alias in internal notes only.


### 1.2 Theorem statement + definition of the smallness parameter

What we can see from accessible sources:

1. Rutgers reproduces an abstract that includes a displayed pair parameter
   `a(t) := max_{x != y} sum_{A : x,y in A} t(A)` and then describes Theorem 1.5
   with limits taken as `alpha(t) -> 0`. This leaves a symbol ambiguity:
   does the paper define `alpha(t)` to be this `a(t)`, or is `alpha(t)` some
   different smallness input?
2. DeepDyve's accessible first-page rendering shows the Greek letter directly:
   it defines
   \[
     \alpha(t)=\max_{x\ne y}\sum_{A\ni x,y} t(A),
   \]
   and then immediately states Theorem 1.5 with the limit taken as
   `alpha(t) -> 0`. This is strong evidence that Rutgers' `a(t)` is just a
   transcription of the same parameter.
3. A second public metadata page from the New Jersey Research Community repeats
   the same Rutgers abstract wording: it states the pair co-load parameter and
   the Theorem 1.5 matching conclusion with limits taken as \(\alpha(t)\to0\).

What is *not* yet checked (without a PDF scan):

- the printed PDF around Theorem 1.5 and Definition(s) of fractional matching,
  `k`-bounded, and `alpha(t)` has not been audited for hidden hypotheses beyond
  the abstract/first-page rendering.


## 2. The cite-ready theorem statement (paraphrase, pending PDF audit)

This is the exact form we want to cite/use in EP689. It is written as a
sequence/asymptotic statement because that is how it is presented in the
accessible abstract/preview. Once the PDF is in hand, this should be aligned
verbatim to the printed Theorem 1.5 (epsilon-delta form).

### Theorem (Kahn 1996, Thm 1.5; asymptotic paraphrase)

Fix integers `k >= 1` and `ell >= 1`. Let `H` be a finite `k`-bounded
hypergraph, and let `t : E(H) -> R_{>=0}` be a fractional matching (i.e.
`sum_{e ni v} t_e <= 1` for every vertex `v`).

Let `c_1, ..., c_ell : E(H) -> R_{>=0}` be nonnegative edge statistics such that
for each `i` one has the quadratic/second-moment condition
\[
  \sum_{e\in E(H)} c_i(e)^2 t_e
  =
  o\!\left(\left(\sum_{e\in E(H)} c_i(e)t_e\right)^2\right).
\]
Assume also that the pair co-load parameter
\[
  \alpha(t) := \max_{u\ne v}\sum_{e\supset\{u,v\}} t_e
\]
satisfies `alpha(t) -> 0` along the given sequence of instances.

Then there exists a matching `M` in `H` such that for each `i=1,...,ell`,
\[
  \sum_{e\in M} c_i(e)
  \sim
  \sum_{e\in E(H)} c_i(e)t_e,
\]
with limits taken along the same sequence (`alpha(t) -> 0`).

Status: supported by the Rutgers abstract + DeepDyve first-page rendering, but
still awaiting a publisher-PDF audit for final "no hidden hypotheses" certainty.


## 3. Exact EP689 verification (what we need to check to apply Kahn)

This is the self-contained bridge from the EP689 hypergraph model and the
preprocessing outputs to the hypotheses of Kahn's theorem.

### 3.1 EP689 hypergraph model and pair-codegree bound

EP689 uses the 3-partite 3-uniform hypergraph
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n),
  \qquad
  e=(x,y,P),\quad |y-x|=2P,
\]
where each edge contains exactly one label vertex `P in Z_n`. Thus every
trimmed subhypergraph `H_n'` is finite and `3`-bounded.

The correct pair-codegree bound is
\[
  \Delta_2(H_n') \le 2.
\]
Reason (case split on the pair type):

1. A pair `(x,y)` determines `P=|y-x|/2` uniquely, hence extends to at most one
   edge.
2. A pair `(x,P)` extends to at most the two choices `y=x+2P` and `y=x-2P`.
3. A pair `(y,P)` similarly extends to at most two choices of `x`.

### 3.2 Alpha(t) control from the small-atom bound

For any nonnegative weights `t` on `E(H_n')`,
\[
  \alpha(t)
  =
  \max_{u\ne v}\sum_{e\supset\{u,v\}} t_e
  \le
  \Delta_2(H_n')\max_e t_e
  \le
  2\max_e t_e.
\]
Also, because every edge `e` contains some pair `{u,v} subset e`,
\[
  \max_e t_e \le \alpha(t).
\]
So in EP689 the two notions are equivalent up to a factor `2`:
\[
  \max_e t_e \le \alpha(t) \le 2\max_e t_e.
\]
Thus any preprocessing output of the form `max_e t_e = o(1)` implies the Kahn
smallness input `alpha(t) -> 0`.

### 3.3 Quadratic condition for the EP689 statistic `C \equiv 1`

For the single statistic `c(e) \equiv 1`, the quadratic condition required by the
Kahn statement is
\[
  \sum_e t_e^2 = o\!\left(\left(\sum_e t_e\right)^2\right).
\]
Write `T_n := sum_e t_e`. Then
\[
  \sum_e t_e^2 \le (\max_e t_e)\sum_e t_e = (\max_e t_e)\,T_n.
\]
So if `max_e t_e = o(1)` and `T_n -> infty`, then automatically
\[
  \sum_e t_e^2 = o(T_n^2).
\]
In EP689, `T_n -> infty` is guaranteed once preprocessing gives
`T_n = (1-o(1)-o_eps(1))|Z_n|` and `|Z_n| -> infty`.

### 3.4 Resulting Kahn rounding step used in EP689

Assume preprocessing produces, on a trimmed finite hypergraph `H_n'`, a weight
function `t` with:

1. (fractional matching) `sum_{e ni v} t_e <= 1` for every vertex `v`;
2. (large total mass) `T_n := sum_e t_e = (1-o(1)-o_eps(1))|Z_n|`;
3. (small atoms) `max_e t_e = o(1)`.

Then:

- `H_n'` is `3`-bounded;
- `alpha(t) <= 2 max_e t_e = o(1)` by the `Delta_2 <= 2` bound;
- the `C \equiv 1` quadratic condition holds by Section 3.3.

So (under the identification `alpha(t)` = pair co-load from Section 1.2),
Kahn's theorem yields a *genuine* matching `M_n` in `H_n'` with
\[
  |M_n| = (1-o(1))T_n = (1-o(1)-o_eps(1))|Z_n|.
\]
Since every matching edge contains exactly one label vertex `P in Z_n`, the
matching covers exactly `|M_n|` labels.


## 4. Safe manuscript wording (until the PDF is audited)

Safe now (honest, cites Kahn while admitting the remaining audit step):

> We apply Kahn's rounding theorem [Kahn 1996, Thm. 1.5], which (in the paper's
> notation) assumes `alpha(t) -> 0` for a fractional matching `t`, where
> `alpha(t)` is the pair co-load `max_{u!=v} sum_{e sup {u,v}} t_e`, and a
> standard quadratic condition for the chosen statistic. In our 3-partite
> 3-graph we have `Delta_2 <= 2`, hence `alpha(t) <= 2 max_e t_e`, so the
> preprocessing small-atom output `max_e t_e=o(1)` gives `alpha(t)->0`.

Not safe to claim yet (requires checking the printed theorem and definitions):

> The Wiley PDF has been fully audited and contains no additional hypotheses
> beyond the displayed conditions.


## 5. Recommended bibliography entry (with DOI alias note)

Prefer this canonical DOI (the `3.3` DOI is an alias that redirects to it as of
2026-04-25).

```bibtex
@article{Kahn1996LPFRP,
  author  = {Kahn, Jeff},
  title   = {A linear programming perspective on the Frankl--R{\"o}dl--Pippenger theorem},
  journal = {Random Structures \& Algorithms},
  volume  = {8},
  number  = {2},
  pages   = {149--157},
  year    = {1996},
  month   = mar,
  doi     = {10.1002/(SICI)1098-2418(199603)8:2<149::AID-RSA5>3.0.CO;2-Y},
  url     = {https://doi.org/10.1002/(SICI)1098-2418(199603)8:2%3C149::AID-RSA5%3E3.0.CO;2-Y},
}
```

DOI alias (internal note only): `10.1002/(SICI)1098-2418(199603)8:2<149::AID-RSA5>3.3.CO;2-S`
redirects to the `3.0` DOI.


## 6. Remaining gaps / to close with a PDF or scan

1. Obtain an actual PDF scan of the article (library, author copy, or other
   lawful source).
2. Verify verbatim:
   - the printed statement of Theorem 1.5 (quantifiers and constants);
   - the printed definition of `alpha(t)` and that it is exactly the pair
     co-load parameter;
   - that there are no additional hypotheses (uniformity/linearity/regularity,
   extra bounds on `max_e t_e`, etc.) beyond those visible in the abstract.
3. After the PDF audit, replace Section 2 with a verbatim theorem statement and
   cite by theorem number + page.


## 6.1 Direct access check on 2026-04-25

I attempted to access the DOI and Wiley PDF endpoints directly from this
workspace:

- `https://doi.org/10.1002/(SICI)1098-2418(199603)8:2<149::AID-RSA5>3.0.CO;2-Y`
  redirects to Wiley.
- `https://doi.org/10.1002/(SICI)1098-2418(199603)8:2<149::AID-RSA5>3.3.CO;2-S`
  first redirects to the `3.0.CO;2-Y` DOI and then to Wiley.
- Wiley PDF and ePDF endpoints return `403 Forbidden` from this environment:
  `https://onlinelibrary.wiley.com/doi/pdf/...`
  and
  `https://onlinelibrary.wiley.com/doi/epdf/...`.

Public web search found Rutgers/New Jersey metadata pages and DeepDyve preview
material, but not a lawfully open standalone PDF of the article.  Therefore the
Kahn step is verified to the level of accessible abstracts/previews in this
environment, including the explicit DeepDyve first-page rendering of
\(\alpha(t)\) as the pair co-load.  A final public proof should still use a
library/user-supplied PDF or scan for the verbatim theorem statement and to
check that no extra hypotheses appear outside the abstract.


## 7. Sources used (accessible without the PDF)

- Rutgers metadata/abstract page (includes Theorem 1.5 in abstract form, but
  uses `a(t)` vs `alpha(t)`):  
  <https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/>
- DeepDyve preview (first page renders the definition with Greek `alpha(t)`):  
  <https://www.deepdyve.com/lp/wiley/a-linear-programming-perspective-on-the-frankl-r-dl-pippenger-theorem-0SnhVwEUF6>
- Crossref API records for the two DOIs:  
  <https://api.crossref.org/works/10.1002/%28SICI%291098-2418%28199603%298%3A2%3C149%3A%3AAID-RSA5%3E3.0.CO%3B2-Y>  
  <https://api.crossref.org/works/10.1002/%28SICI%291098-2418%28199603%298%3A2%3C149%3A%3AAID-RSA5%3E3.3.CO%3B2-S>
- DOI redirect check (performed via `curl -I` against `doi.org` on 2026-04-25):
  `3.3` returns `301` with `Location:` pointing to the `3.0` DOI.
- DBLP record (metadata + DOI):  
  <https://dblp.org/rec/journals/rsa/Kahn96>
