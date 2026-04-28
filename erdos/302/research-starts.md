# EP302 research starts

Researched: 2026-04-26

## Statement and status

Let \(f(N)\) be the largest size of a set \(A\subseteq\{1,\ldots,N\}\) with no
distinct \(a,b,c\in A\) satisfying

\[
\frac1a=\frac1b+\frac1c.
\]

Equivalently, \(a<b,c\) and \((b-a)(c-a)=a^2\), or, for a pair \(b<c\),
\(a=bc/(b+c)\) is integral. The estimation problem is open. The original
candidate \(f(N)=(1/2+o(1))N\) is already ruled out by the current
\((5/8+o(1))N\) construction, but the true density is not known.

## Known results and partials

- Trivial lower bounds: all odd integers, or all integers in \((N/2,N]\), give
  \(f(N)\ge (1/2+o(1))N\).
- Stijn Cambie's construction improves this to \(f(N)\ge (5/8+o(1))N\): take
  odd integers up to \(N/4\) together with all integers in \([N/2,N]\).
- Wouter van Doorn's note proves \(f(N)\le (9/10+o(1))N\). The proof packs
  disjoint scaled copies of the forcing triples \(\{2a,3a,6a\}\) and
  \(\{4e,5e,20e\}\), using valuation classes to keep the copies disjoint; any
  admissible set omits at least one element from each block.
- If the condition is relaxed to allow \(b=c\), then \(n,2n\in A\) gives
  \(1/n=1/(2n)+1/(2n)\). The standard no-\(n,2n\) threshold gives a forced
  solution for \(|A|\ge (2/3+o(1))N\).

## Latest relevant literature and comments

- The official Erdos Problems page still lists EP302 as open, records the
  \(9/10\) upper bound and \(5/8\) lower bound, and shows no comments on the
  EP302 thread as of this check.
- OEIS A390395 now tracks exact finite values. Its linked table gives values
  through \(n=731\), with \(a(731)=606\) (about \(0.829N\)); this is useful for
  pattern mining but not asymptotic evidence by itself.
- Brown and Roedl proved the finite-colouring analogue: every finite colouring
  of the positive integers has a monochromatic solution to the unit-fraction
  equation with distinct terms. This supports existence in Ramsey settings but
  does not give a sharp positive-density threshold.
- Gaiser's 2024 paper on Rado numbers for unit-fraction equations improves
  finite two-colour bounds for \(1/x_1+\cdots+1/x_k=1/y\). It is adjacent
  rather than directly density-focused, but its finite-set/LCM viewpoint may
  help design small forcing templates.
- EP327 is adjacent via \(1/a+1/b\) being a unit fraction iff \(a+b\mid ab\).
  Comments there report MILP/SAT computations and a large-prime-factor
  construction idea for pair-avoidance; both look relevant for lower-bound
  experiments and for distinguishing pair-avoidance from triple-avoidance.

## Natural first attack routes

- Extend van Doorn's packing. Search over primitive triples
  \((r,s,t)\) with \(1/r=1/s+1/t\), then choose disjoint scaling classes via
  prime-adic signatures. The immediate target is to raise the forced omission
  density above \(1/10\).
- Treat the problem as a 3-uniform hypergraph independence problem and solve
  finite LP/MILP relaxations for template families. The dual hitting-set
  weights may suggest new disjoint or nearly-disjoint forcing blocks.
- Generalize Cambie's construction. Try unions of interval layers with parity
  or valuation restrictions, e.g. low odd/sifted layers plus high intervals,
  and test whether densities above \(5/8\) survive all generated triples.
- Use the EP327 pair-divisibility route for lower bounds: pair-avoiding sets
  automatically avoid EP302 triples, but EP302 permits pairs whose resulting
  unit denominator is outside \(A\), so there may be denser constructions after
  selective pruning.

## Computational and formalization hooks

- MaxSAT/ILP model: variables \(x_i\in\{0,1\}\); maximize \(\sum_i x_i\);
  for every \(1\le b<c\le N\) with \(a=bc/(b+c)\in\mathbb Z\), add
  \(x_a+x_b+x_c\le 2\). This is exactly the OEIS A390395 computation style.
- Faster triple generation: enumerate \(a\) and factor pairs \(uv=a^2\), with
  \(b=a+u\), \(c=a+v\), \(u\ne v\), \(b,c\le N\). This avoids scanning all
  pairs and exposes primitive/scaled structure.
- Template search: enumerate small primitive triples, assign scaling sets by
  residue or \(p\)-adic valuation constraints, and compute asymptotic density
  of disjoint blocks symbolically.
- Formalization looks approachable for fixed constructions and bounds:
  the identity \((b-a)(c-a)=a^2\), Cambie's lower-bound verification, and
  van Doorn-style disjointness by unique factorization are all Lean-friendly.

## Risks and unknowns

- The finite data remains far above both \(5/8\) and \(1/2\), so small-\(N\)
  optimization may overfit and miss the asymptotic obstruction.
- The gap \(5/8\le \liminf f(N)/N\le \limsup f(N)/N\le 9/10\) is wide; even a
  moderate improvement may require new structure, not just more computation.
- Disjoint-block packings may saturate early unless blocks with larger minimum
  deletion per covered element are found.
- Pair-avoidance is stronger than EP302-avoidance; constructions from EP327
  may leave density on the table.

## Tractability score

4/10 for a serious few-day attempt. Good chance of producing useful
computational data, a cleaner formulation, or a small improvement candidate;
low chance of a decisive asymptotic estimate in that time.

## Three concrete next steps

1. Reproduce A390395 up to a moderate \(N\) with OR-Tools CP-SAT or PySAT,
   saving both optimal sets and dual hitting sets for pattern inspection.
2. Build a primitive-triple catalogue up to a small height, then run a search
   for disjoint \(p\)-adic scaling families that improve van Doorn's \(1/10\)
   omitted-density packing.
3. Parameterize Cambie-type lower constructions by interval cutoffs and
   valuation/parity classes; use the solver to test candidate densities above
   \(5/8\) before trying to prove any stable family.

## Sources

- Official EP302 page: https://www.erdosproblems.com/302
- EP302 discussion thread, currently no comments: https://www.erdosproblems.com/forum/thread/302
- Wouter van Doorn note: https://github.com/Woett/Mathematical-shorts/blob/main/Two-colouring%20and%20density%20lead%20to%20solutions%20to%20an%20equation%20in%20unit%20fractions.pdf
- OEIS A390395: https://oeis.org/A390395
- A390395 table through 731: https://oeis.org/A390395/b390395.txt
- Brown and Roedl, "Monochromatic solutions to equations with unit fractions":
  https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/monochromatic-solutions-to-equations-with-unit-fractions/647E26A2255E9027AC1B1D8FCF86E8A8
- Collier Gaiser, "On Rado numbers for equations with unit fractions":
  https://arxiv.org/abs/2306.04029
- Original Erdos-Graham monograph scan:
  https://fanchung.ucsd.edu/ron/papers/80_11_number_theory.pdf
- Adjacent EP327 page and comments:
  https://www.erdosproblems.com/327
  https://www.erdosproblems.com/forum/thread/327
