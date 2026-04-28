# EP273 research starts

Date: 2026-04-26

## Statement and status

Erdos Problem 273 asks whether there is a finite distinct covering system
of congruences
\[
  a_i \pmod {n_i}, \qquad 1 < n_1 < \cdots < n_r,
\]
such that every integer satisfies at least one congruence and every modulus
has the form \(n_i=p_i-1\) for a prime \(p_i \ge 5\).

The problem is listed as open on ErdosProblems and has no comments there as
of the page version last edited 2025-10-01. The distinct/strict reading is
essential: without it the problem is trivial, e.g. all four residue classes
modulo \(4=5-1\). The Google DeepMind formal-conjectures repository records
the statement as a `StrictCoveringSystem`.

## Known results and partials

- Erdos and Graham state the problem in *Old and New Problems and Results in
  Combinatorial Number Theory*, p. 24. They also record Selfridge's positive
  construction if \(p=3\) is allowed, using divisors of 360.
- In the 360-divisor pool, the admissible moduli with \(d+1\) prime and
  \(p \ge 3\) are
  \[
  2,4,6,10,12,18,30,36,40,60,72,180.
  \]
  Removing the banned modulus \(2=3-1\) leaves reciprocal sum \(7/9<1\), so
  those remaining divisors alone cannot cover by the standard density bound
  \(\sum 1/n_i \ge 1\).
- Among all allowed \(p-1\) with \(p\ge5\), the first 17 reciprocals sum to
  \(0.999174\ldots<1\), while adding \(70=71-1\) brings the sum above 1.
  Thus any EP273 example needs at least 18 moduli.
- Parity gives a useful equivalent formulation. Write \(n_i=2m_i\), where
  \(2m_i+1\) is prime. A residue class modulo \(2m_i\) covers only one
  parity; after dividing that parity by 2 it becomes one class modulo \(m_i\).
  Hence an EP273 example is equivalent to splitting a finite set of distinct
  \(m\) with \(2m+1\) prime into two disjoint covering systems, one for the
  even integers and one for the odd integers.
- Applying known theorems to each parity-side quotient cover: Hough--Nielsen
  imply each side must contain a modulus divisible by 2 or 3; the
  Balister--Bollobas--Morris--Sahasrabudhe--Tiba proof of Schinzel's
  conjecture implies each side must contain a divisibility pair \(m_i\mid m_j\).
  These are not decisive, but they are good search filters.

## Recent literature and comments

No recent paper found in this pass appears to attack the \(p-1\) restriction
directly. The closest useful developments are structural or computationally
suggestive:

- Hough--Nielsen (2019) prove every distinct covering system has a modulus
  divisible by 2 or 3.
- Balister, Bollobas, Morris, Sahasrabudhe, and Tiba (2021/2022) develop the
  distortion method, prove Schinzel's divisibility-pair conjecture, improve
  Hough-type minimum-modulus bounds, and rule out the squarefree version of
  the odd-moduli problem.
- Adenwalla (2025), and Jia--Li--Liu (2025), study the related
  Erdos--Graham divisor-moduli problem. This is relevant to attempts based on
  divisors of a highly composite integer, but it does not settle EP273.
- Bispels--Cohen--Harrington--Lowrance--Pontes--Schaumann--Wong (2025)
  continue the odd-moduli variant with one repeated odd modulus. The tree and
  lifting constructions may be useful templates, but the parity quotient here
  demands two disjoint distinct covers from \(2m+1\) prime moduli.

## Natural first attack routes

1. Search in the parity quotient. Generate \(M=\{m\ge2:2m+1\text{ prime}\}\)
   and try to find two disjoint distinct covering systems using moduli in
   \(M\). Enforce reciprocal sum at least 1, a 2-or-3-divisible modulus, and a
   divisibility pair on each side before doing residue search.
2. Reconstruct Selfridge's \(p=3\) construction over the divisors of 360.
   Identify exactly how the modulus 2 is used, then test whether its parity
   class can be replaced by a small quotient cover from \(M\).
3. Build around divisibility chains. Since each quotient cover needs
   \(m_i\mid m_j\), look for chains \(m,km,\ldots\) with all \(2m+1\),
   \(2km+1,\ldots\) prime; these are the likely backbone for efficient CRT
   residue assignments.
4. Try a negative-density approach only after computation exposes a pattern.
   Existing distortion-method results are powerful but too coarse here because
   the original moduli are all even, so the known small-prime obstruction is
   automatically satisfied.

## Computational and formalization hooks

- For a fixed finite modulus set \(S\), the residue-choice problem is finite:
  let \(L=\operatorname{lcm}(S)\), choose one residue for each modulus, and
  require every class modulo \(L\) to be covered. A direct SAT/ILP encoding
  has variables \(x_{n,r}\) and coverage clauses for residues modulo \(L\).
- Direct \(L\)-enumeration will blow up quickly. Prefer a lazy exact-cover
  search that stores uncovered CRT cells, branches on the largest uncovered
  cell, and uses reciprocal upper bounds to prune.
- The parity quotient halves the moduli and turns the problem into two
  independent cover searches plus a disjointness constraint.
- Lean hooks look approachable: formalize the density lower bound, the finite
  residue criterion modulo an lcm, and the parity-splitting equivalence around
  the existing `Erdos273.erdos_273` statement.

## Risks and unknowns

- The Selfridge construction is cited but not explicit in the sources found
  here; reconstructing it may take separate work.
- A positive example may require very large moduli, so small SAT failures will
  not mean much.
- A negative solution is unlikely from finite computation alone; it would need
  a structural theorem for the set \(\{m:2m+1\text{ prime}\}\).
- The condition \(p-1\) is dense enough in reciprocal mass that simple density
  arguments have little bite after the first small obstruction.

## Tractability score

4/10 for a serious attempt over the next few days. A complete solution is
unlikely, but a useful computational pipeline, the Selfridge reconstruction,
and several formal lemmas are realistic.

## Three next steps

1. Locate or reconstruct the Selfridge divisor-of-360 residue system and save a
   verified residue table.
2. Implement the parity-quotient search for \(m\le 500\) or \(1000\), with
   reciprocal, Hough--Nielsen, and divisibility-pair pruning.
3. Prove the parity-splitting lemma and \(\sum 1/n_i\ge1\) density bound in
   Lean against the existing `StrictCoveringSystem` formalization.

## Sources

- ErdosProblems #273: https://www.erdosproblems.com/273
- ErdosProblems LaTeX source for #273:
  https://www.erdosproblems.com/latex/273
- Erdos and Graham, *Old and New Problems and Results in Combinatorial Number
  Theory* (UCSD PDF): https://mathweb.ucsd.edu/~ronspubs/80_11_number_theory.pdf
- Formal conjectures Lean file:
  https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/273.lean
- Hough and Nielsen, "Covering systems with restricted divisibility":
  https://researchconnect.suny.edu/en/publications/covering-systems-with-restricted-divisibility/
- Balister--Bollobas--Morris--Sahasrabudhe--Tiba, "On the Erdos covering
  problem: the density of the uncovered set":
  https://digitalcommons.memphis.edu/facpubs/5342/
- Balister--Bollobas--Morris--Sahasrabudhe--Tiba, "The Erdos--Selfridge
  problem with square-free moduli":
  https://digitalcommons.memphis.edu/facpubs/5868/
- Hopper, "On covering systems of integers": https://arxiv.org/abs/1705.04372
- Adenwalla, "A Question of Erdos and Graham on Covering Systems":
  https://arxiv.org/abs/2501.15170
- Jia--Li--Liu, "Resolving Adenwalla's conjecture related to a question of
  Erdos and Graham about covering systems": https://arxiv.org/abs/2504.09579
- Bispels et al., "A further investigation on covering systems with odd
  moduli": https://arxiv.org/abs/2507.16135
