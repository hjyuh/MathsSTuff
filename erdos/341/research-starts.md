# EP341 Research Starts

Researched: 2026-04-26

## Statement And Status

EP341 is open. Given a finite seed `A={a_1<...<a_k}` of positive
integers, extend greedily by taking `a_{n+1}` to be the least integer
greater than `a_n` that is not of the form `a_i+a_j` with `i,j <= n`.
Must the first differences `a_{m+1}-a_m` eventually be periodic?

The official page calls this an old problem of Dickson, cites
`[ErGr80,p.53]`, and notes that even the seed `{1,4,9,16,25}` takes
thousands of terms before periodicity appears. The page was last edited
2026-01-20 and had no comments when checked.

For an increasing sequence, eventual periodicity of the differences is
equivalent to the tail of the set being a finite union of arithmetic
progressions. In the sum-free-set formulation this is usually phrased as:
is every complete greedily generated sum-free set ultimately periodic?
Care is needed: EP341 allows equal summands and arbitrary finite seeds;
some nearby "0-additive" and Ulam/Queneau literature uses distinct
summands `i<j` or assumes a sum-free base.

## Known Results And Partials

- Calkin and Finch give necessary/sufficient periodicity criteria for
  sum-free sets via Cameron's bijection between binary decision strings
  and sum-free sets. For the Dickson/complete-sum-free subcase, the
  decision string has only finitely many zeros, so their criterion
  reframes EP341 as a boundedness problem for an auxiliary obstruction
  function `g`.
- They also give finite periodicity certificates: if a candidate tail
  exhibits enough consecutive cycles and the corresponding decision
  sequence is aligned, ultimate periodicity follows from a finite check.
- Their computations found many ultimately periodic examples but also
  apparent aperiodic complete sum-free bases. The paper reports checking
  76,080 sum-free bases up to 27, and three-element bases up to 35, up
  to `10^7`; listed apparent aperiodic examples include bases whose
  generated sets begin `{1,3,8,20,26,...}` and `{2,15,16,23,27,...}`.
- Calkin and Erdos show the natural irrational-rotation sum-free sets
  `S_alpha={n : {n alpha} in (1/3,2/3)}` are aperiodic but incomplete.
  Thus this attractive source of aperiodic sum-free sets cannot directly
  disprove Dickson's conjecture.
- Calkin, Finch, and Flowers introduce difference density
  `d_n(m)=#{x in S : x-m in S, x<=n}/#{x in S : x<=n}`. If `S` has
  ultimate period `p`, then `d(m)=1` for multiples of `p` and has a
  constrained rational pattern otherwise. Their tests on three candidate
  aperiodic sets computed to 50 million and `m <= 1.25e7` without seeing
  period evidence, but this remains finite evidence only.
- Later work on regular/automatic/Sturmian sum-free sets studies the
  Cameron-bijection side of the problem and may supply useful structure
  tools, but it does not appear to settle the finite-greedy complete case.

## Latest Relevant Literature And Comments

- Green's current "100 Open Problems" list discusses EP341 under Problem
  7, distinguishes Dickson's construction from Queneau's distinct-summand
  variant, and still says the eventual-periodicity question appears open.
- The official ErdosProblems page has no problem comments or claimed
  partial solutions as of 2026-04-26.
- A 2026 Lean formalization exists in the `formal-conjectures` repository.
  It states the official `i,j <= n` version using an `IsLeast` predicate
  and eventual periodicity of the difference sequence.

## Natural First Attack Routes

1. **Try to disprove via a known candidate.** Pick one small Calkin-Finch
   candidate under the EP341 convention, recompute deeply, and try to
   prove nonperiodicity by showing the Calkin-Finch obstruction function
   is unbounded or by turning the observed difference-density structure
   into a theorem.
2. **Build a modular certificate machine.** If a seed appears periodic
   with period `q` after cutoff `N`, certify it by checking two finite
   conditions: residues in the proposed tail are never pair-sums of
   allowed residues with feasible earlier offsets, and every missing
   residue class is eventually covered by such sums.
3. **Classify restricted bases.** Prove the conjecture for finite-zero
   decision strings with very small zero pattern, for one/two-element
   seeds, or for modular complete sum-free tails. This is more realistic
   than the full problem and may expose the obstruction.
4. **Look for automatic/self-similar structure.** The candidate aperiodic
   sets in the literature show congruence-class patterns in difference
   densities. If a candidate has a substitution or automaton description,
   nonperiodicity plus completeness could become provable.

## Computational And Formalization Hooks

- Implement a generator for the exact EP341 rule using a bitset of
  pair-sums. For each new selected `a`, update representability by
  setting `a+s` for previous selected `s`. This is enough for scouting
  and candidate-period discovery; for large bounds, switch to blocked
  bitsets or C/Rust.
- Record, for every run: seed, convention (`i,j` allowed equal), term
  bound, largest value, first suspected preperiod, period, and a separate
  certificate status. This avoids mixing Dickson and Queneau data.
- Add a finite verifier for proposed periodic tails. This can be tested
  first on known regular examples, then on `{1,4,9,16,25}`.
- Lean hook: formalize the finite periodic-tail certificate as a theorem
  implying the `formal-conjectures` EP341 statement for a given seed,
  rather than trying to formalize a global proof.
- Difference-density scans are useful triage: multiples of a true period
  should push density toward 1. Absence of such peaks is evidence only,
  but good for ranking candidates.

## Risks And Unknowns

- Convention drift is the main literature risk: EP341 allows equal
  summands and arbitrary seeds, while several related sequences use
  `i<j` and/or sum-free starting bases.
- Periods and preperiods can be very large. Calkin-Finch report a set
  with minimal period `2,875,722` after about `584,000` terms, and the
  official square-seed example already has a long transient.
- Finite computation cannot prove aperiodicity. It can only find periods,
  certify periods, or produce targets for a structural proof.
- The arbitrary-seed version may have behavior not captured by the
  clean complete-sum-free formulation, because the seed may already
  contain additive relations.
- The official problem page warns that its open status may miss outside
  literature; no recent proof or disproof was found in this scouting pass.

## Tractability Score

**3/10 for settling EP341 in a few days.** A serious attempt can probably
produce useful computations, certify additional examples, and maybe prove
restricted families. A full proof or counterexample looks unlikely on a
short timescale because the central aperiodicity evidence has resisted
conversion from finite computation to theorem.

## Three Concrete Next Steps

1. Reproduce the first several thousand terms for `{1,4,9,16,25}` and
   identify/certify its eventual period under the exact EP341 rule.
2. Recompute the Calkin-Finch candidate bases under the equal-summand
   EP341 convention and rank them by period evidence and
   difference-density behavior.
3. Write a finite modular-tail verifier and a Lean-friendly statement of
   the certificate theorem, then validate it on one small periodic seed.

## Sources

- Official EP341 page: https://www.erdosproblems.com/341
- Erdos-Graham source scan, p.53 context: https://mathweb.ucsd.edu/~ronspubs/80_11_number_theory.pdf
- Green, "100 Open Problems", Problem 7: https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf
- Calkin and Finch, "Conditions on Periodicity for Sum-Free Sets", Experimental Mathematics 5 (1996): https://emis.de/ft/51959
- Calkin and Erdos, "On a class of aperiodic sum-free sets", Math. Proc. Camb. Phil. Soc. 120 (1996): https://www.math.clemson.edu/~calkin/Papers/calkin_erdos.pdf
- Calkin, Finch, and Flowers, "Difference density and aperiodic sum-free sets", Integers 5 (2005): https://math.colgate.edu/~integers/a3int2003/a3int2003.pdf
- Wen, Wu, and Zhang, "On the regular sum-free sets", European J. Combin. 49 (2015): https://arxiv.org/abs/1405.6493
- Allouche, Shallit, Wen, Wu, and Zhang, "Sum-free sets generated by the period-k-folding sequences and some Sturmian sequences", Discrete Math. 343 (2020): https://arxiv.org/abs/1911.01687
- Formal Conjectures Lean statement: https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/341.lean
