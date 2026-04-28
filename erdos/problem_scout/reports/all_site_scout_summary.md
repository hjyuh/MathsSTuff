# Erdős Problems All-Site Scout Summary

Generated 2026-04-26.

Inputs:

- Local mirror `erdosproblems/data/problems.yaml`, 1217 entries.
- Live range page `https://www.erdosproblems.com/range/1-1217`, parsed into `erdos/problem_scout/data/problem_metadata.jsonl`.
- Four subagent range scouts: `1-350`, `351-700`, `701-1050`, `1051-1217`.

Metadata snapshot:

- Total problems parsed: 1217.
- Open-like candidates considered: 686 (`open`, `falsifiable`, `verifiable`, `decidable`).
- Zero-comment open-like candidates: 188.
- Site statuses in mirror: 643 open, 27 falsifiable, 9 decidable, 7 verifiable.

## Practical Shortlist

| Rank | Problem | Type | Why It Is Worth A Sprint | Main Risk |
|---:|---|---|---|---|
| 1 | [#617](https://www.erdosproblems.com/617) | finite SAT / graph coloring | First unknown case appears to be `r=5`: color edges of `K_26` with 5 colors so every 6-set sees all colors. A witness or UNSAT certificate would be concrete. | SAT instance may be too large without good symmetry breaking; all-`r` proof is harder. |
| 2 | [#506](https://www.erdosproblems.com/506) | decidable geometry | Page indicates large `n` handled after a correction, leaving small cases. Good candidate for finite configuration/oriented-matroid work. | Continuous geometry certificates can be delicate. |
| 3 | [#699](https://www.erdosproblems.com/699) | falsifiable binomial divisibility | Kummer/carry criterion gives a crisp computational attack on `(n,i,j)`. Good chance of either finding exceptions or reducing to prime-interval lemmas. | Global proof may run into prime distribution/binomial divisibility barriers. |
| 4 | [#302](https://www.erdosproblems.com/302) | extremal reciprocal hypergraph | Clean asymptotic target with known lower/upper gap; exact search, LP relaxations, containers, and structural mining are natural. | Asymptotic extremal structure may be hard. |
| 5 | [#273](https://www.erdosproblems.com/273) | covering systems / exact cover | Covering system with moduli `p-1`, `p>=5`; very direct SAT/ILP/exact-cover formulation. | Nonexistence certificate may require a global covering-systems theorem. |
| 6 | [#1212](https://www.erdosproblems.com/1212) | lattice graph / paths | Visible-lattice path problem with prime/composite constraints; concrete graph-search surface and low comments. | Infinite path proof may still need number-theoretic control. |
| 7 | [#1005](https://www.erdosproblems.com/1005) | Farey computation / lattice geometry | Constants are bounded but not settled; exhaustive Farey-block data could be useful quickly. | There may be active unpublished work; full constant proof nontrivial. |
| 8 | [#341](https://www.erdosproblems.com/341) | greedy sequence / eventual periodicity | Straightforward generator and period detection; good for automation and conjecture mining. | Eventual periodicity proof is not just computation. |
| 9 | [#424](https://www.erdosproblems.com/424) | closure sequence / density | Zero comments; fast generation and residue-closure analysis likely produce immediate data. | Positive density proof is global. |
| 10 | [#938](https://www.erdosproblems.com/938) | powerful numbers | Search/classification for 3-term APs of consecutive powerful numbers; formalized statement and low comments. | Finiteness proofs for powerful-number patterns can be Diophantine-heavy. |
| 11 | [#993](https://www.erdosproblems.com/993) | tree independence polynomials | Disproof is a finite tree; DP/canonical tree enumeration is straightforward. Good formal-certificate path. | If true, proof needs structural unimodality machinery. |
| 12 | [#1186](https://www.erdosproblems.com/1186) | finite AP coloring / SDP-SAT | Finite versions admit SAT/ILP/SDP and bounds for small `k`; useful for exact constants. | General asymptotics in extremal additive combinatorics are hard. |

## Best Next Sprint

The best immediate target is **#617**.

Reason: it has the cleanest finite-certificate interface. A counterexample is a 5-coloring of the 325 edges of `K_26`; a positive result for `r=5` could be a solver-backed UNSAT proof plus an independent checker. This is more concrete than EP885, where the next serious step needs arithmetic geometry tooling around genus-2/elliptic Chabauty.

The best number-theory target is **#699**.

Reason: it has a clear exact computational reduction through valuations of binomial coefficients, and failures would be cheaply verifiable. It is also close enough to prime-interval phenomena that even partial reductions may be interesting.

The best “underdeveloped data-mining” targets are **#341**, **#424**, and **#1212**.

## Lower Priority Despite High Metadata Scores

- [#723](https://www.erdosproblems.com/723): finite projective plane prime-power problem. Famous and not a realistic sprint target.
- [#548](https://www.erdosproblems.com/548), [#628](https://www.erdosproblems.com/628): famous graph conjectures with large existing literature.
- [#107](https://www.erdosproblems.com/107): Happy Ending problem, heavily worked.
- [#64](https://www.erdosproblems.com/64): tempting finite-counterexample framing, but likely much deeper than it looks.
- [#687](https://www.erdosproblems.com/687) and [#688](https://www.erdosproblems.com/688): likely prime-gap/Jacobsthal-hard.
- [#885](https://www.erdosproblems.com/885): still worth continuing if the goal is a serious Diophantine project, but not the highest-probability fast closure after the all-site scan.

## Files Produced

- `erdos/problem_scout/data/problem_metadata.jsonl`
- `erdos/problem_scout/data/problem_metadata.csv`
- `erdos/problem_scout/reports/metadata_top80.md`
- `erdos/problem_scout/reports/all_site_scout_summary.md`
