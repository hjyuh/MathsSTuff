# EP424 Research Starts

Prepared: 2026-04-26

## Statement and Status

Let `A` be the smallest set of positive integers containing `2` and `3` and
closed under

```tex
a,b \in A,\ a \ne b \quad \Longrightarrow \quad ab-1 \in A.
```

EP424 asks whether `A` has positive lower natural density. The problem is
open. The stronger "almost all integers appear" formulation is false: by
induction all elements are `0` or `2 mod 3`, since `{0,2}` is closed under
`(x,y) -> xy-1 mod 3`; hence density is at most `2/3`.

Sources: [ErdosProblems #424](https://www.erdosproblems.com/424),
[OEIS A005244](https://oeis.org/A005244), [Green, Problem 63 in 100 Open
Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf).

## Known Results and Partials

- No claimed partial or complete solution is listed in the ErdosProblems
  comments as of its 2026-03-31 edit.
- The mod `3` obstruction is the only explicit congruence obstruction I found
  in the standard references. It gives the clean upper bound `d(A) <= 2/3`.
- OEIS gives the initial values
  `2,3,5,9,14,17,26,27,33,41,44,50,51,53,...`, a table to 10000 terms, the
  complement sequence [A171413](https://oeis.org/A171413), divisor-helper
  sequence [A139127](https://oeis.org/A139127), and representation counts
  [A139128](https://oeis.org/A139128).
- Green's updated list says the answer is "probably yes" and cautions that a
  proof may need both computation and theory. It also notes seed sensitivity:
  replacing `(2,3)` by `(9,10)` gives a negative-density analogue because word
  values grow too fast relative to the number of words.

## Latest Relevant Literature and Comments

- [Green's 100 Open Problems PDF](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)
  was updated in December 2025; Problem 63 is the same Hofstadter product
  closure problem and links to EP424.
- [MathWorld's Hofstadter Sequences entry](https://mathworld.wolfram.com/HofstadterSequences.html)
  was last updated 2026-03-25 and cites Guy's section E31, "Three Sequences of
  Hofstadter", in *Unsolved Problems in Number Theory*.
- OEIS A005244 and companion entries were active recently; A139128 includes
  Robert Israel's 2024 Maple code for representation counts.
- I found no direct arXiv/published paper attacking A005244 density. The closest
  recent Hofstadter item is Quanyu Tang's 2026 preprint on the adjacent
  consecutive-sum sequence [A005243](https://arxiv.org/abs/2603.09939), not this
  product-minus-one sequence.
- A 2024 Math StackExchange post reports an unverified computation with
  proportion above `50%` below `10^9`; useful as a lead, not as evidence to cite
  mathematically.

## Natural First Attack Routes

- **Divisor reformulation.** For `n > 3`, membership of `n` is equivalent to
  `n+1` having a factorization `uv` with distinct `u,v in A`. This suggests a
  sieve/branching view: estimate how often `n+1` has two allowed divisors.
- **Density bootstrap.** If `A` has many elements up to `X`, the maps
  `x -> ax-1` for small `a in A` generate structured subsets in longer
  intervals. Try to turn empirical density growth into an inequality
  `A(cX) >= (1+epsilon)A(X)` until linear density is reached.
- **Product-set energy.** Generated values below `X` are shifted products
  `ab-1 <= X`. Bounding collisions among pairs `(a,b)` could turn lower bounds
  on `|A cap [1,sqrt X]|` into new lower bounds on `|A cap [1,X]|`.
- **Modular bootstrap.** Search for finite modulus/certificate systems showing
  that every allowed residue class has a reduction path `(n+1)/a` back into a
  previously controlled range. Absence of further congruence obstructions is
  not enough, but it can guide a finite-computation proof.

## Computational and Formalization Hooks

- A deterministic scanner is simple: process `n` in increasing order, factor
  `n+1`, and test whether two distinct divisors are already marked in `A`.
  This exactly matches the recursive closure because both factors are `< n`.
- Local check on 2026-04-26 with this divisor scanner:
  - `|A cap [1,10^3]| = 250`
  - `|A cap [1,10^4]| = 3207`
  - `|A cap [1,10^5]| = 39843`
  - `|A cap [1,10^6]| = 457599`
  These data support a positive-density guess but do not prove a lower bound.
- Residue-closure scouting up to modulus `30` shows only the expected `1 mod 3`
  missing pattern in the coarse closure model; exact finite certificates should
  track distinct representatives, not just residue classes.
- The statement already has a Lean formalization:
  [google-deepmind/formal-conjectures, `ErdosProblems/424.lean`](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/424.lean).
  Formalizable subgoals: the mod `3` obstruction, correctness of the divisor
  scanner, and finite residue/reduction certificates.

## Risks and Unknowns

- Empirical density can be misleading; the set might thin out after very large
  scales if hidden congruence or factorization obstructions accumulate.
- The distinctness condition `a != b` is easy to mishandle in residue models and
  computations.
- Green's `(9,10)` warning means arguments based only on word-count growth are
  fragile; the special small seeds `2,3` probably matter.
- No published partial lower bound beyond trivial infinite families was found.
  A serious attempt may need new ideas, not just a longer computation.

## Tractability Score

**5/10 for a serious attempt over the next few days.** The problem is open and
likely nontrivial, but it has accessible computations, a clean divisor
reformulation, and plausible finite-certificate subgoals. A complete proof in a
few days is unlikely; a useful partial, reproducible data package, or certified
conditional bootstrap seems realistic.

## Three Concrete Next Steps

1. Build a fast exact generator to at least `10^8`, recording density by dyadic
   intervals, residue distributions, representation counts, and first misses in
   allowed residue classes.
2. Search for finite bootstrap certificates: choose a finite `F subset A`, and
   test whether divisibility by elements of `F` gives recursive coverage of a
   positive fraction of `0,2 mod 3` integers.
3. Prove and formalize the easy lemmas first: mod `3` obstruction, divisor-test
   equivalence, monotone closure below a cutoff, and correctness of any finite
   certificate checker.

## Source Links

- ErdosProblems #424: https://www.erdosproblems.com/424
- ErdosProblems #424 history: https://www.erdosproblems.com/history/424
- OEIS A005244: https://oeis.org/A005244
- OEIS A171413 complement: https://oeis.org/A171413
- OEIS A139127 divisor helper: https://oeis.org/A139127
- OEIS A139128 representation counts: https://oeis.org/A139128
- Ben Green, 100 Open Problems, Problem 63: https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf
- MathWorld, Hofstadter Sequences: https://mathworld.wolfram.com/HofstadterSequences.html
- Formal Conjectures Lean file: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/424.lean
- Tang 2026 adjacent Hofstadter A005243 preprint: https://arxiv.org/abs/2603.09939
- 2024 Math StackExchange computation lead: https://math.stackexchange.com/questions/4970785/show-that-the-set-ab-1-is-dense-in-natural-numbers
