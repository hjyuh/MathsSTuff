# EP993

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/993

Status: falsifiable - open, but a finite counterexample could disprove it.

Tags: graph theory.

OEIS: possible.

## Statement

For every tree or forest `T`, the sequence counting independent vertex
sets by size should be unimodal. If `i_k(G)` is the number of independent
sets of size `k`, the conjecture asks for some mode `m` such that

```tex
i_0(T)\leq i_1(T)\leq\cdots\leq i_m(T)\geq i_{m+1}(T)\geq\cdots.
```

## Current Notes

Alavi, Malde, Schwenk, and Erdos showed that the analogous statement is
false for arbitrary graphs: possible inequality patterns can be realized
by graphs. Schwenk proved the edge-independent-set counting sequence is
unimodal for any graph.

The forum thread contains current computational/literature leads, all
marked here as unverified comments rather than accepted page remarks:

- Basit and Galvin are cited for work including Radcliffe's verification
  through `n <= 25`.
- A Jan. 2026 comment reports verification of unimodality for every tree
  through `n <= 29`.
- A Mar. 2026 comment links public artifacts for exhaustive `n = 28` and
  `n = 29` runs, reporting zero unimodality failures.
- An Apr. 2026 comment points to Kadrawi-Levit 2023 log-concavity failures
  for trees and Ramos-Sun 2025 machine-learning-assisted searches finding
  many more log-concavity failures, still apparently unimodal.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/993
- Discussion thread: https://www.erdosproblems.com/forum/thread/993
- Source keys on the page: `[AMSE87]`, `[Sc81]`

