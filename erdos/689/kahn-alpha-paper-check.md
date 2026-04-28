# Kahn alpha(t) paper check for EP689

Created: 2026-04-25

This note checks the exact Kahn input needed for the EP689 rounding step, using
the existing local notes:

- [kahn-citation-verification.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-citation-verification.md)
- [gtz-kahn-proof-chain.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-kahn-proof-chain.md)
- [claim-language-and-citations.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\claim-language-and-citations.md)

The target citation is:

Jeff Kahn, "A linear programming perspective on the
Frankl--Rodl--Pippenger theorem", Random Structures and Algorithms 8(2)
(1996), 149--157.

## Short verdict

The accessible evidence is strong that Kahn's \(\alpha(t)\) is exactly the
pair co-load
\[
  \alpha(t)=\max_{x\ne y}\sum_{A\ni x,y} t(A).
\]

Under that reading, the EP689 Kahn step is covered by the current condition
package:

1. \(H_n'\) is finite and \(3\)-bounded.
2. \(t\) is a fractional matching.
3. The relevant statistics are finite; for EP689 we only need \(C\equiv 1\).
4. The finite-statistic quadratic condition holds, for \(C\equiv 1\), from
   \(\max_e t_e=o(1)\) and total mass \(T_n=\sum_e t_e\to\infty\).
5. \(\alpha(t)\to0\) follows from the EP689 pair-codegree bound
   \(\Delta_2\le2\):
   \[
     \alpha(t)
     =
     \max_{u\ne v}\sum_{e\supset\{u,v\}}t_e
     \le 2\max_e t_e=o(1).
   \]

I did not obtain the publisher PDF or an independent scan in this pass. So the
remaining citation gap is only the final PDF-level audit of the printed theorem
and surrounding definitions.

## Sources checked

1. Rutgers/ResearchWithRutgers metadata page:
   <https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/>

   This page gives the article metadata, pages 149--157, journal/volume/issue,
   and an abstract/theorem statement. It defines the displayed pair parameter as
   \(a(t)=\max_{x\ne y}\sum_{A\ni x,y}t(A)\), then states Theorem 1.5 with
   limits as \(\alpha(t)\to0\). This source alone leaves a notation ambiguity:
   is \(a(t)\) the same as \(\alpha(t)\), or only a related quantity?

2. DeepDyve first-page rendering:
   <https://www.deepdyve.com/lp/wiley/a-linear-programming-perspective-on-the-frankl-r-dl-pippenger-theorem-0SnhVwEUF6>

   The accessible first-page text renders the opening definition with the Greek
   letter:
   \[
     \alpha(t)=\max\left\{\sum\{t(A):x,y\in A\in H\}:x,y\in V,\ x\ne y\right\}.
   \]
   It then immediately states Theorem 1.5 with the limit taken as
   \(\alpha(t)\to0\). This strongly indicates that the Rutgers \(a(t)\) is just
   a transcription/OCR variant of Kahn's \(\alpha(t)\).

3. OpenAlex/Crossref metadata:
   <https://api.openalex.org/works/doi:10.1002/%28SICI%291098-2418%28199603%298%3A2%3C149%3A%3AAID-RSA5%3E3.0.CO%3B2-Y>
   and
   <https://api.crossref.org/works/10.1002/%28SICI%291098-2418%28199603%298%3A2%3C149%3A%3AAID-RSA5%3E3.0.CO%3B2-Y>

   Crossref confirms the publisher, journal, volume, issue, and pages. OpenAlex
   reconstructs the same abstract and also has the Greek-letter
   \(\alpha(t)\) definition in its abstract index. OpenAlex marks the work as
   closed access and lists no PDF URL.

4. DBLP:
   <https://dblp.org/rec/journals/rsa/Kahn96>

   DBLP confirms the article metadata and marks access as closed. It also lists
   an unpaywall lookup path, but no open copy was surfaced through the checks
   above.

5. Publisher access attempt:
   the Wiley Online Library PDF and abstract URLs returned Cloudflare 403 from
   this environment. Wiley's TDM API endpoint returned "No TDM Client Token was
   found". Thus I did not inspect the publisher PDF.

## What the accessible theorem statement contains

The rendered theorem statement has the following inputs:

1. fixed \(k\) and fixed finite number of statistics \(\ell\);
2. a \(k\)-bounded hypergraph \(H\);
3. a fractional matching \(t\) of \(H\);
4. nonnegative edge statistics \(c_1,\ldots,c_\ell:H\to\mathbb R_+\);
5. for each statistic,
   \[
     \sum_{A\in H} c_i(A)^2t(A)
     =
     o\left(\left(\sum_{A\in H}c_i(A)t(A)\right)^2\right);
   \]
6. the asymptotic limit \(\alpha(t)\to0\).

The conclusion is a matching \(M\) preserving each statistic asymptotically:
\[
  \sum_{A\in M}c_i(A)\sim \sum_{A\in H}c_i(A)t(A)
  \qquad (i=1,\ldots,\ell).
\]

No additional visible hypothesis appears in the accessible theorem statement:
not uniformity, not linearity, not regularity, not vertex balance, not a
separate maximum-atom bound, and not a degree lower bound. Finiteness is
implicit in the finite sums and is harmless for EP689 because the hypergraphs
\(H_n'\) are finite.

The statement does require a finite list of statistics. This is why the EP689
application should use \(C\equiv1\) to round total matching size, rather than
one statistic per label.

## EP689 alpha check

For the EP689 prime-difference hypergraph,
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n),
  \qquad
  e=(x,y,P),\quad |y-x|=2P,
\]
each edge has size \(3\), so \(H_n\) and every trimmed \(H_n'\) are
\(3\)-bounded.

The correct pair-codegree bound is \(\Delta_2\le2\), not linearity:

1. A pair \((x,y)\) determines \(P=|y-x|/2\), so it extends to at most one
   edge.
2. A pair \((x,P)\) has at most the two extensions \(y=x+2P\) and
   \(y=x-2P\).
3. A pair \((y,P)\) similarly has at most two extensions.

Therefore for any nonnegative weights \(t\),
\[
  \alpha(t)
  =
  \max_{u\ne v}\sum_{e\supset\{u,v\}}t_e
  \le
  \Delta_2(H_n')\max_e t_e
  \le
  2\max_e t_e.
\]

Since every EP689 edge has size \(3\), the reverse inequality
\[
  \max_e t_e\le \alpha(t)
\]
also holds: choose any pair inside an edge \(e\), and the pair co-load includes
\(t_e\). Thus in this setting \(\alpha(t)\) and \(\max_e t_e\) are equivalent
up to the factor \(2\).

Consequently the local small-atom output
\[
  \max_e t_e=o(1)
\]
is enough to force Kahn's smallness parameter \(\alpha(t)\to0\).

## EP689 quadratic statistic check

For the only statistic needed in EP689, \(C\equiv1\), Kahn's quadratic
condition is
\[
  \sum_e t_e^2=o\left(\left(\sum_e t_e\right)^2\right).
\]

Let \(T_n=\sum_e t_e\). Then
\[
  \sum_e t_e^2\le(\max_e t_e)\sum_e t_e=(\max_e t_e)T_n.
\]

So if \(\max_e t_e=o(1)\) and \(T_n\to\infty\), then
\[
  \sum_e t_e^2=o(T_n^2).
\]

In the intended EP689 chain, preprocessing gives
\[
  T_n=(1-o(1)-o_\varepsilon(1))|Z_n|,
\]
and \(|Z_n|\to\infty\). Hence the quadratic condition for \(C\equiv1\) is
automatic once the small-atom and large-mass claims are proved.

## Resulting Kahn step

Assume the preprocessing proposition has produced weights \(t\) on a trimmed
finite hypergraph \(H_n'\) such that:

1. \(t\) is a fractional matching;
2. \(\sum_e t_e=T_n=(1-o(1)-o_\varepsilon(1))|Z_n|\);
3. \(\max_e t_e=o(1)\).

Then, using the accessible Kahn statement and the identification
\(\alpha(t)=\) pair co-load:

1. \(H_n'\) is \(3\)-bounded;
2. \(\alpha(t)\le2\max_e t_e=o(1)\);
3. the \(C\equiv1\) quadratic condition holds;
4. Kahn gives a matching \(M_n\) with
   \[
     |M_n|=(1-o(1))T_n
     =
     (1-o(1)-o_\varepsilon(1))|Z_n|.
   \]

Each edge contains exactly one label \(P\in Z_n\), so the matching covers the
same number of labels. Kahn supplies the rounding; the mass estimate
\(T_n\sim |Z_n|\) must still come from the GTZ/preprocessing side.

## Remaining gaps

1. The actual journal PDF/scan was not located. The accessible first-page
   rendering is strong evidence, but the final writeup should still inspect the
   printed Theorem 1.5 and surrounding definitions.
2. The PDF-level check should verify that no earlier definition of
   "fractional matching", \(k\)-bounded, or \(\alpha(t)\) adds a condition not
   visible in the abstract/theorem rendering.
3. The DOI metadata is mildly inconsistent across sources:
   Crossref/DBLP/DeepDyve use a suffix ending in `3.0.CO;2-Y`, while Rutgers
   displays one ending in `3.3.CO;2-S`. This is bibliographic cleanup, not a
   mathematical obstruction.
4. The Kahn check does not prove the preprocessing inputs. The remaining EP689
   work is still the GTZ moment verification, deterministic mass-loss bounds,
   coefficient-tail bound, and final cleanup theorem listed in
   [gtz-kahn-proof-chain.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-kahn-proof-chain.md).

## Safe claim language

Safe now:

> The accessible first-page/theorem renderings identify Kahn's
> \(\alpha(t)\) with the pair co-load
> \(\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e\). Under this identification, the
> EP689 rounding step needs no extra smallness hypothesis beyond producing a
> fractional matching with small atoms and the finite-statistic quadratic
> condition; the EP689 bound \(\Delta_2\le2\) gives
> \(\alpha(t)\le2\max_e t_e=o(1)\).

Not safe until the PDF/scan is inspected:

> The printed paper has been fully audited and contains no hidden hypotheses.
