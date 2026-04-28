# Goldbach / Prime-Distribution Inputs for Parity-First Directed Switching (Top Layer)

Created: 2026-04-25

This note isolates the analytic number theory inputs that would be needed to
make the "directed switching / top-layer" route from `parity-top-layer.md`
actually go through.

Throughout, \(n\) is large, \(I:=(n/2,n]\), and
\[
  H_{\rm top}(n):=\{2^k q:\ n/2<2^k q\le n,\ k\ge 1,\ q\le n/2\ \text{odd prime}\}.
\]
As recalled in `parity-top-layer.md`, \(|H_{\rm top}(n)|=\pi(n/2)-1\sim n/(2\log n)\).

## 0. Directed Switching Language (What Must Be "Packed")

In the parity-first baseline \(a_2\equiv 1\pmod 2\), \(a_p\equiv 0\pmod p\) for
odd primes, we change a set \(R\) of odd primes away from zero, choosing
nonzero residues \(b_p\pmod p\) for \(p\in R\).

The directed viewpoint is:

- choose, for each changed prime \(p\in R\), a *head prime* \(r=r(p)\) and set
  \[
    b_p\equiv r \pmod p;
  \]
- then \(p\) hits (covers) every integer of the form \(r+jp\le n\), \(j\ge 1\),
  and in particular it hits any \(h\in H_{\rm top}(n)\cap I\) with
  \[
    h=r+jp;
    \tag{A}
  \]
- simultaneously, \(p\) "repairs" the switched prime \(r\) by providing a hit
  at \(m=r\) (this is the switching-cost constraint \(G_R(r)\ge 1\) in
  `parity-top-layer.md`).

Thus the top-layer problem becomes:

1. **Coverage**: for every \(h\in H_{\rm top}(n)\), there exists \(p\in R\) and
   \(j\ge 1\) such that \(h=r(p)+jp\).
2. **Repair**: every switched prime \(r\in R\) has indegree \(\ge 1\) in the
   directed graph \(p\to r(p)\) (i.e. is hit by at least one changed modulus).

This is a global packing problem: each changed prime \(p\) chooses exactly one
residue class, hence exactly one head \(r(p)\), and that single choice must
simultaneously (i) pay the switching cost and (ii) cover a prescribed sparse
set \(H_{\rm top}(n)\).

## 1. What Arithmetic Information Controls "How Many Top Targets an Edge Hits"?

Fix an odd prime modulus \(p\le n/2\) and a head \(r\) (prime). The edge
\(p\to r\) covers the set
\[
  \mathcal{H}(p,r):=\{h\in H_{\rm top}(n)\cap I:\ h\equiv r\pmod p\}.
\]
Write \(H_k:=\{2^k q\in I:\ q\in (n/2^{k+1},n/2^k]\ \text{prime}\}\), so
\(H_{\rm top}(n)=\bigsqcup_{k\ge 1}H_k\).
For odd \(p\), the congruence \(2^k q\equiv r\pmod p\) is equivalent to
\[
  q \equiv 2^{-k} r \pmod p.
  \tag{B}
\]
Therefore, estimating \(|\mathcal{H}(p,r)|\) reduces to *primes in arithmetic
progressions in dyadic intervals*: for each \(k\), we need lower bounds on
\[
  \#\bigl\{q\ \text{prime}:\ q\in (n/2^{k+1},n/2^k],\ q\equiv a_k\pmod p\bigr\},
  \quad a_k:=2^{-k}r\ (\bmod p).
\]
Any route that tries to choose \(r(p)\) so that \(\mathcal{H}(p,r(p))\) is large
is ultimately asking for equidistribution of primes in arithmetic progressions,
uniformly in short (or at least dyadic) intervals.

There are two immediate barriers:

- **Modulus size barrier**: classical Bombieri--Vinogradov type theorems control
  primes in progressions only on average for moduli up to about \(x^{1/2}\),
  where \(x\) is the prime size (the "square-root barrier"). A standard entry
  point is Bombieri's large sieve paper.  
  Source: Bombieri, "On the large sieve" (Mathematika 12 (1965), 201-225).  
  URL: [Cambridge Core](https://www.cambridge.org/core/journals/mathematika/article/on-the-large-sieve/4AE92826645F6F3393D30AF0D2767346).

- **Short interval barrier**: even when \(p\le x^{1/2}\), getting BV-type
  equidistribution restricted to short intervals is strictly harder and is
  typically treated in specialized papers.  
  Source: Perelli--Pintz--Salerno, "Bombieri's theorem in short intervals"
  (Ann. Scuola Norm. Sup. Pisa (4) 11 (1984), 529-539).  
  URL: [Numdam](https://www.numdam.org/item/ASNSP_1984_4_11_4_529_0/).

For binary additive problems with primes simultaneously in arithmetic
progressions and short intervals, see e.g. Halupczok's mean-value results in
this direction (surveying and extending work of Perelli--Pintz and others).  
Source: Halupczok, "Goldbach's problem with primes in arithmetic progressions
and in short intervals" (JTNB 25 (2013), 331-351).  
URL: [Numdam](https://numdam.org/articles/10.5802/jtnb.839/).

## 2. The "Tight Top Block" Regime \(p\in(n/5,n/4]\): Why It Asks for Something Extremely Strong

The capacity computations in `parity-top-layer.md` show the first dyadic block
where the *raw* top-window capacity ceases to be impossible is roughly
\((n/5,n/4]\). But for such \(p\),
\[
  \nu_I(p)=\left\lceil\frac{n}{2p}\right\rceil \in \{2,3\}.
\]
So each changed prime in that block can place at most 2-3 points of its chosen
residue class into the entire top interval \(I\), and only *some* of those
points are even in \(H_{\rm top}(n)\).

Consequences for required inputs:

1. One needs a near-perfect *combinatorial packing*: a linear-sized family of
   moduli each contributing only \(O(1)\) candidate top hits cannot afford much
   statistical wastage. Any analytic result that only controls average
   distribution with power-savings exceptional sets is not obviously usable.

2. Any attempt to pick \(r(p)\) so that \(|\mathcal{H}(p,r(p))|\ge 1\) for most
   \(p\in(n/5,n/4]\) is effectively asking for "primes in very short segments of
   arithmetic progressions" at modulus size comparable to prime size, i.e.
   far beyond the BV range.

One quick way to see the "too tight for statistics" issue is to compare to the
naive density heuristic. Since \(|H_{\rm top}(n)|\sim n/(2\log n)\), the density
of \(H_{\rm top}(n)\) inside the top interval \(I\) is \(\asymp 1/\log n\). A
single residue class for \(p\in(n/5,n/4]\) contributes at most \(\nu_I(p)\le 3\)
points of \(I\), so the expected number of top targets inside a random residue
class is only \(\ll 3/\log n\), i.e. typically zero. Thus any construction in
this regime must systematically locate the rare residue classes which actually
contain top targets, and do so while also satisfying the repair indegree
constraints.

Known "beyond \(x^{1/2}\)" results still do not come close to the moduli
relevant here. A canonical benchmark is Bombieri--Friedlander--Iwaniec, which
pushes primes-in-AP information past \(x^{1/2}\) to about \(x^{4/7-\varepsilon}\)
in weighted/averaged forms (still \(\ll x^{1-\varepsilon}\)).  
Source: Bombieri--Friedlander--Iwaniec, "Primes in arithmetic progressions to
large moduli" (Acta Math. 156 (1986), 203-251).  
URL (PDF): [Tsinghua archive scan](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6385-11511_2006_Article_BF02399204.pdf).

Bottom line: the "use only \(p\asymp n\)" approach appears to require
distributional control on primes in residue classes for moduli comparable to
prime size, in intervals that contain only \(O(1)\) lattice points. That is
well outside currently proved theorems; it is closer in spirit to
Hardy--Littlewood prime tuples heuristics than to anything BV/BFI-type tools
currently deliver.

## 3. The \(j=1\) (Goldbach-Sum) Specialization and Why It Is Not Just "Goldbach"

If one forces \(j=1\) in (A), each top target \(h\) needs a representation
\[
  h=p+r,\qquad p,r\ \text{odd primes},
\]
and then the 2-cycle switching gadget from `parity-top-layer.md` repairs both
primes and covers \(h\).

Even before packing issues, this runs into the fact that binary Goldbach for
all even integers is open. There are deep partial results about exceptional
sets; for example, Montgomery--Vaughan show that the set of even integers up to
\(x\) that are not a sum of two primes is small.  
Source: Montgomery--Vaughan, "The exceptional set of Goldbach's problem"
Acta Arith. 27 (1975), 353-370.  
URL: [IM PAN / Acta Arithmetica](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/27/0/100637/the-exceptional-set-of-goldbach-s-problem).

For short-interval exceptional-set control in the same circle-method vein (but
still "almost all" rather than pointwise for a sparse structured set), see:  
Source: Perelli--Pintz, "On the exceptional set for Goldbach's problem in short
intervals" (J. London Math. Soc. (2) 47 (1993), 41-49).  
URL: [DOI](https://doi.org/10.1112/jlms/s2-47.1.41).

However, for the parity-first top layer we need Goldbach representations for a
*sparse structured set* of size \(\asymp x/\log x\) (namely \(H_{\rm top}(n)\)),
not for "almost all" even numbers. An exceptional set of size \(o(x)\) could
still, in principle, contain *all* of \(H_{\rm top}(n)\). Thus almost-all
Goldbach theorems alone do not certify the needed pointwise representations on
this set.

And then comes the real strengthening: we do not just need existence of a
representation for each \(h\), we need a disjoint packing of representations so
that no switched prime is asked to choose two residues. Even in a simplified
model "assign each \(h\) a distinct prime \(p\) with \(h-p\) prime", this is a
perfect-matching/SDR statement in a bipartite Goldbach graph, which is
strictly stronger than ordinary Goldbach.

## 4. Chen-Type Representations (\(h=\text{prime}+\text{semiprime}\)) Give Pointwise Edges, but Not the Packing

Chen's theorem gives, for all sufficiently large even \(N\), a representation
\[
  N = r + P_2,
\]
where \(r\) is prime and \(P_2\) is a product of at most two primes. In the
"generic" case \(P_2=p_1p_2\), this is exactly
\[
  N = r + jp_1,\qquad j=p_2\ \text{prime},
\]
which is a special case of (A). So pointwise, Chen supplies an edge
\(p_1\to r\) that covers \(N\) and repairs \(r\).

Sources:

- Chen, "On the representation of a large even integer as the sum of a prime
  and the product of at most two primes" (Sci. Sinica 16 (1973), 157-176).  
  URL: [SciEngine DOI landing page](https://sciengine.com/doi/10.1360/ya1973-16-2-157).
- Yamada, "Explicit Chen's theorem" (arXiv:1511.03409), for an accessible modern
  statement and explicit constants.  
  URL: [arXiv](https://arxiv.org/abs/1511.03409).

But Chen does not address the global constraints we need here:

- we need to choose a single head \(r(p)\) per modulus \(p\) that simultaneously
  covers many top targets and participates in the repair graph;
- we need to avoid overloading a small set of heads;
- we need this for the special set \(H_{\rm top}(n)\), not for a full density
  set of even integers.

To turn Chen into a parity-first top-layer repair, one would need a quantified,
well-distributed, many-representations version of Chen, strong enough to run a
matching/nibble that respects the one-residue-per-prime constraint. That is
substantially stronger than Chen's pointwise existence theorem.

## 5. Transference / Pseudorandomness Tools: What They Give and What They Don't

Transference results of Green--Tao type show that the primes behave like a
pseudorandom set for many linear patterns, allowing one to *count* solutions to
systems of linear equations in primes.  
Source: Green--Tao, "Linear equations in primes" (Annals 171 (2010), 1753-1850).  
URL: [Annals](https://annals.math.princeton.edu/2010/171-3/p08).

This is relevant philosophically because the directed-switching problem is a
global combinatorial selection problem constrained by linear congruences.
However, what we would need is closer to:

- a robust expansion property for a large bipartite graph of admissible
  \((p,r)\) edges together with lower bounds on how many top targets each edge
  covers, and
- a hypergraph matching argument ensuring a selection of one outgoing edge per
  vertex plus full coverage of \(H_{\rm top}(n)\).

Those are not consequences of the existing transference/circle-method theorems
in the literature, at least not without inserting additional very strong
distribution hypotheses (e.g. conjectural levels of distribution well beyond
\(1/2\)).

## 6. Working Conclusion (for the Top-Layer Route)

1. **Pointwise coverage of a single \(h\in H_{\rm top}(n)\)** by some
   representation \(h=r+jp\) with \(r,p\) primes is not the hard part; Chen
   already guarantees (for all sufficiently large even \(h\)) a representation
   of the needed form \(h=r+p_1p_2\).

2. **The hard part is the disjoint packing with repair.** The directed switching
   route demands a global selection of residues (one per changed prime) that
   simultaneously repairs all switched primes and covers all \(h\in H_{\rm top}(n)\).
   This is a matching/packing problem that is strictly stronger than:
   - binary Goldbach (if one tries \(j=1\)), and
   - Chen's theorem (if one allows \(j\) prime and uses semiprimes).

3. **If one insists on using only "near-\(n\)" moduli (e.g. \(p\in(n/5,n/4]\)),**
   then the analytic input would have to control primes in arithmetic
   progressions for moduli comparable to prime size, in segments with only
   \(O(1)\) candidates. This is far beyond the scope of Bombieri--Vinogradov
   and even beyond Bombieri--Friedlander--Iwaniec.

4. **If one allows substantially smaller moduli (say \(p\le n^{1/2}\) or smaller),**
   then BV-type distribution theorems (and their short-interval refinements)
   become relevant inputs for controlling \(|\mathcal{H}(p,r)|\) on average.
   This may plausibly support an almost-all version of top-layer repair, but
   a full "cover every \(h\in H_{\rm top}(n)\)" packing statement still looks
   stronger than what is currently proved.
