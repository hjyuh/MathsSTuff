# Erdos Candidate Scout: Combinatorics, Graph Theory, Discrete Geometry

Date: 2026-04-26

Scope: candidate triage only. I did not try to solve any problem. I used erdosproblems.com as the canonical problem list, then checked current web/literature signals where they matter. The site itself warns that "open" status can miss relevant literature, so every candidate below includes a risk note.

## Executive ranking

| Rank | Problem | Area | Scout verdict | Difficulty | Hidden-hard risk |
|---:|---|---|---|---:|---|
| 1 | [#734](https://www.erdosproblems.com/734) | finite combinatorics/designs | Best clean construction target | 4/10 | Medium-low |
| 2 | [#776](https://www.erdosproblems.com/776) | extremal set theory | Fresh partials, clear remaining gap | 4/10 partial, 6/10 full | Low-medium |
| 3 | [#506](https://www.erdosproblems.com/506) | discrete geometry | Finite-check geometry with known asymptotic resolution | 4/10 partial, 6/10 cleanup | Medium |
| 4 | [#993](https://www.erdosproblems.com/993) | graph theory / independence polynomials | Recursive/computational structure, real partial-result path | 5/10 partial, 8/10 full | Medium-high |
| 5 | [#617](https://www.erdosproblems.com/617) | graph coloring / Ramsey | Small-parameter and SAT/flag-algebra footholds | 5/10 partial, 7/10 full | Medium |

Near misses: [#128](https://www.erdosproblems.com/128) is tempting because flag algebra has already moved the constant, but it is likely a serious extremal graph theory problem. [#23](https://www.erdosproblems.com/23) is close to known bounds but looks more entrenched. [#634](https://www.erdosproblems.com/634) is attractive, but the literature around triangle dissections looks easy to misread, so I would verify Beeson/Laczkovich/Zhang implications before investing.

## 1. Problem #734: pairwise balanced designs with controlled block-size multiplicities

**Statement.** Find, for all large \(n\), a non-trivial pairwise balanced block design \(A_1,\ldots,A_m \subseteq \{1,\ldots,n\}\) such that, for every size \(t\), at most \(O(n^{1/2})\) blocks have size \(t\). A pairwise balanced block design means every pair of points is contained in exactly one block.

**Why tractable.**

- This is a construction problem, not a global obstruction problem.
- Erdos himself wrote that it would "probably not be very difficult", which is not proof of tractability but is a useful signal.
- The required bound is naturally sharp up to constants: de Bruijn-Erdos gives \(m \ge n\), forcing some repeated block-size scale of order \(n^{1/2}\).
- The bottleneck is concrete: build a PBD whose block-size histogram is flat enough.

**Known partial results/comments.**

- erdosproblems.com records de Bruijn-Erdos's lower bound \(m \ge n\), which implies the \(n^{1/2}\) scale is unavoidable.
- Search did not surface a modern resolution beyond the problem page and its history page.
- Related neighboring PBD/block-compatible sequence problems (#732/#733/#665) have recent-looking updates, so the risk is less "nobody looked" and more "the answer may be hidden in design-theory machinery".

**Likely first attack.**

Start by converting the task into a block-size sequence target:
\[
\sum_i \binom{|A_i|}{2}=\binom n2,\qquad
\#\{i: |A_i|=t\}=O(n^{1/2}).
\]
Then try to realize such sequences using known PBD existence theorems or Wilson-type constructions. A pragmatic first partial result would be \(O(n^{1/2}\log^C n)\), then remove the logarithm by smoothing block sizes.

**Difficulty.** 4/10 for a meaningful partial construction; 6/10 for full clean proof.

**Risk of being secretly famous/hard.** Medium-low. It is in design theory, where strong general existence theorems may either solve it quickly or impose non-obvious divisibility constraints. Literature check should start with modern PBD realization theorems.

**Could AI-assisted proof architecture help?** Yes. This is a good fit for generation-and-verification loops: propose block-size sequences, check divisibility constraints, map to PBD existence theorems, and isolate the exact construction lemma that needs human proof.

## 2. Problem #776: antichains with multiplicity \(r\) on each occurring level

**Statement.** Let \(r \ge 2\). Find how large \(n\) must be, as a function of \(r\), to ensure there is an antichain \(A_1,\ldots,A_m \subseteq \{1,\ldots,n\}\) with \(n-3\) distinct set sizes, where every occurring size occurs at least \(r\) times.

**Why tractable.**

- There is already a precise threshold formulation \(n_0(r)\).
- Very recent progress leaves a narrow asymptotic gap:
\[
2r+2 \le n_0(r) \le 2r+2\log_2 r+O(\log_2\log_2 r),
\]
so the next target is clear: remove or reduce the logarithmic overhead.
- The exact cases \(r=2,3\) are already done, which gives templates for finite search plus proof extraction.

**Known partial results/comments.**

- He and Tang's 2026 arXiv paper proves \(n_0(2)=3\), \(n_0(3)=8\), and \(n_0(r)=2r+o(r)\).
- The erdosproblems.com page notes the same result and explicitly says it was obtained with ChatGPT assistance.
- The forum thread says the authors iterated ChatGPT-5.2 Thinking hundreds of times to make progress.

**Likely first attack.**

Do not try to jump to exact \(n_0(r)\). First reproduce the lower-bound obstruction and the upper-bound construction from He-Tang in a clean internal notation. Then search for strengthened constructions with overhead \(O(\log\log r)\) or constant overhead. In parallel, compute exact \(n_0(r)\) for \(4 \le r \le 8\) using SAT/ILP to guess the true correction term.

**Difficulty.** 4/10 for improved exact small \(r\) or better explicit constants; 6/10 for closing the asymptotic gap.

**Risk of being secretly famous/hard.** Low-medium. It is active and recent, so there is little hidden old literature risk, but the remaining logarithmic gap may encode a real extremal-set obstruction.

**Could AI-assisted proof architecture help?** Strong yes. This is the clearest AI-fit candidate: finite construction search, obstruction-mining, lemma synthesis, and proof compression already seem to have worked once.

## 3. Problem #506: minimum number of circles determined by \(n\) points

**Statement.** Determine the minimum number of circles determined by any \(n\) points in \(\mathbb R^2\), not all on a circle. The site notes the intended non-degeneracy condition is probably either "not all on a line" or "no three collinear".

**Why tractable.**

- The large-\(n\) part is essentially resolved modulo a corrected bound: Elliott claimed a result for \(n>393\), and Purdy-Smith identified the corrected lower bound.
- erdosproblems.com marks this as "decidable", i.e. resolved up to finite check.
- The remaining work appears to be small-\(n\) classification plus cleaning up the exact non-degeneracy convention.
- This is discrete geometry but has a finite combinatorial core: point configurations, triples, concyclicity, and exception structures.

**Known partial results/comments.**

- Elliott claimed that for \(n>393\), assuming not all points are on a circle or line, the points determine at least \(\binom{n-1}{2}\) circles.
- Purdy and Smith observed Elliott's proof gives instead
\[
\binom{n-1}{2}+1-\left\lfloor\frac{n-1}{2}\right\rfloor,
\]
again for \(n>393\), and this corrected lower bound is sharp.
- Segre's projection of a cube shows the naive lower bound \(\binom{n-1}{2}\) is false for \(n=8\).
- Purdy-Smith's 2011 paper "Lines, Circles, Planes and Spheres" gives adjacent lower-bound technology for lines/circles/planes/spheres.

**Likely first attack.**

Clarify the intended statement in two versions:

- Version A: not all points on a line or circle.
- Version B: no three collinear, not all on a circle.

Then build a small-\(n\) catalogue using order types/oriented matroids and circle-incidence signatures. The first publishable partial is likely a table for \(n \le N\), with proofs for exceptional configurations and a precise restatement of the finite remainder.

**Difficulty.** 4/10 for finite catalogues and corrected formulation; 6/10 if the finite range requires serious oriented-matroid enumeration.

**Risk of being secretly famous/hard.** Medium. The main risk is not that the problem is famous-hard, but that small cases or corrected formulations are buried in older discrete-geometry literature.

**Could AI-assisted proof architecture help?** Yes. This is a good hybrid target: symbolic configuration enumeration, invariant discovery, proof sketching for exceptional cases, and Lean-style formal checks for small incidence claims.

## 4. Problem #993: unimodality of independent-set sequences of trees/forests

**Statement.** For every tree or forest \(T\), the sequence \(i_k(T)\), where \(i_k(T)\) counts independent vertex sets of size \(k\), is unimodal.

**Why tractable.**

- Trees have recursive structure, and independence polynomials satisfy clean deletion/branch recurrences.
- Counterexample search is straightforward computationally and has likely pushed far enough to inform conjectural structure.
- There are many partial results, including random-tree behavior and special families, so a partial theorem can be meaningful even if the full conjecture is hard.
- A false direction, log-concavity, appears separable from unimodality, so one can focus on the weaker property.

**Known partial results/comments.**

- The problem originates with Alavi, Malde, Schwenk, and Erdos; general graphs can realize arbitrary inequality patterns, so trees are the structured boundary case.
- Basit and Galvin (2021) prove that for uniformly random labelled trees, asymptotically almost surely the initial about 49.5 percent of the sequence is increasing and the terminal about 38.8 percent is decreasing, using the Matrix Tree Theorem plus computation.
- Recent work continues on special families and hypertree analogues; Galvin-Sharpe (2024) study related independent-set sequences for linear hypertrees.
- The erdosproblems.com page has comments but records no claimed solution.

**Likely first attack.**

Target structural subclasses rather than the whole conjecture:

- trees with bounded maximum degree,
- caterpillars/spiders/combs beyond the known families,
- trees with bounded number of high-degree vertices,
- trees whose independence polynomial has controlled root geometry.

Computationally generate minimal "near failures" and try to prove they cannot occur under a local tree surgery. A first useful output would be a reduction lemma: any counterexample can be assumed to satisfy a tight set of local constraints.

**Difficulty.** 5/10 for a new structural partial; 8/10 for the full conjecture.

**Risk of being secretly famous/hard.** Medium-high. It is a known 1987 conjecture with continuing literature. The tractable angle is partial progress, not an expectation of a quick full proof.

**Could AI-assisted proof architecture help?** Yes, but with guardrails. AI can help design recurrences, mine minimal counterexample patterns, and suggest local transformations. It should be paired with exact polynomial computation to avoid plausible but false unimodality arguments.

## 5. Problem #617: missing color in every \(r\)-coloring of \(K_{r^2+1}\)

**Statement.** For \(r \ge 3\), if the edges of \(K_{r^2+1}\) are colored with \(r\) colors, then there exist \(r+1\) vertices whose induced \(K_{r+1}\) misses at least one color.

Equivalently, there is no "balanced" coloring of \(K_{r^2+1}\) in which every \(r+1\)-vertex subset sees all \(r\) colors.

**Why tractable.**

- The conjecture is proved for \(r=3,4\), so \(r=5\) is an immediate concrete target.
- The threshold is tight-ish: Erdos and Gyarfas showed the property fails for infinitely many \(r\) if \(r^2+1\) is replaced by \(r^2\).
- The object is finite for each \(r\), and the \(r=5\) case is small enough to invite SAT/ILP plus symmetry breaking, even if a pure human proof is not immediate.
- There is a clean design/code-theory flavor: balanced colorings exist at related projective-plane-like parameter values.

**Known partial results/comments.**

- erdosproblems.com records the conjecture of Erdos-Gyarfas, proof for \(r=3,4\), and failure at \(r^2\) for infinitely many \(r\).
- Gyarfas's "Problems and memories" slides state the same balanced-coloring problem and note that balanced \(r\)-colorings exist when \(n=r^2+r+1\) and \(r+1\) is a prime power.
- The problem page is marked falsifiable and has a formalized statement.

**Likely first attack.**

Treat \(r=5\) as the first milestone. Encode an \(r\)-coloring of \(K_{26}\) with constraints that every 6-set uses all 5 colors, add color-permutation and vertex-symmetry breaking, and run SAT/CP-SAT. If unsat, extract a human-readable certificate or derive local counting lemmas from failed cores. If sat, the finite counterexample disproves the conjecture.

For the general proof direction, try double-counting color-missing \((r+1)\)-sets against color-degree distributions, then add stability input from the \(r^2\) constructions.

**Difficulty.** 5/10 for \(r=5\) computational progress; 7/10 for a general proof.

**Risk of being secretly famous/hard.** Medium. It is a Ramsey/coloring problem from Erdos-Gyarfas and could be tougher than the small statement suggests. The finite \(r=5\) target keeps the risk acceptable.

**Could AI-assisted proof architecture help?** Yes. This is a natural SAT-to-proof target: generate encodings, search for certificates, cluster unsat cores into lemmas, and attempt formal verification of the finite case.

## Source notes

- Main problem pages: [#734](https://www.erdosproblems.com/734), [#776](https://www.erdosproblems.com/776), [#506](https://www.erdosproblems.com/506), [#993](https://www.erdosproblems.com/993), [#617](https://www.erdosproblems.com/617).
- He and Tang, "An Erdos--Trotter problem on antichains with multiplicity \(r\) on each occurring level", arXiv:2602.09803, revised 2026-03-21: https://arxiv.org/abs/2602.09803.
- Basit and Galvin, "On the Independent Set Sequence of a Tree", Electronic Journal of Combinatorics 28(3), 2021: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i3p23.
- Purdy and Smith, "Lines, Circles, Planes and Spheres", Discrete & Computational Geometry 44, 2011; arXiv:0907.0724: https://arxiv.org/abs/0907.0724.
- Gyarfas, "Problems and memories" slides, balanced colorings section: https://www.renyi.hu/~gyarfas/Presentations/erdos100talk.pdf.
- AI-process caution/context: teorth/erdosproblems wiki, "AI contributions to Erdos problems": https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems.
