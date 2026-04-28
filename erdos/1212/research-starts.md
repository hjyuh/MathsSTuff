# EP1212 Research Starts

Researched: 2026-04-26

## Statement and Status

Let `G` be the graph on visible lattice points `(x,y) in N^2`, i.e.
`gcd(x,y)=1`, with edges between horizontal/vertical nearest neighbours.
EP1212 asks whether there is an infinite path in `G` using only vertices
with `x,y > 1` and not both coordinates prime. Equivalently, in the first
quadrant visible-point graph, delete row/column `1` and delete visible
prime-prime vertices `(p,q)`, and ask whether an infinite component remains.

Status: open on the official Erdos Problems page, last edited 2026-04-08,
with no claimed partial solution in comments.

## Known Results and Partials

- Erdos's weaker question, requiring only `x,y > 1`, has Stewart's simple
  construction: connect `(p_k,p_{k+1})` to `(p_{k+1},p_{k+2})` through the
  rectangle edge when `p_{k+2} < 2p_k`, true for `k >= 4`. This does not solve
  EP1212 because the construction uses prime-prime endpoints, exactly the
  vertices now forbidden.
- Herzog-Stewart (1971) characterized finite visible/nonvisible patterns by
  local congruence obstructions. The official page says Erdos attributed more
  graph-connectivity statements to them, but Bloom could not locate those in
  the visible-patterns paper.
- Vardi (1999) later proved strong facts about the full coprime graph
  `R={(m,n) in Z^2: gcd(m,n)=1}`: `R` has a unique infinite component, that
  component has asymptotic density, and computations suggested about 96% of
  visible points lie in it. Vardi's elementary uniqueness proof uses the
  coordinate-1 lines, so it does not directly survive the EP1212 deletions.
- A quick finite-box check of the EP1212 induced graph up to `N=1200` found no
  box-spanning or giant component; the largest component had 21423 vertices
  inside `[2,1200]^2`. This is only a scouting diagnostic: finite boxes can
  miss paths that leave and re-enter the box.

## Latest Relevant Literature and Comments

- Martineau (2022) gives a local-limit model for the random coprime colouring
  seen from a uniformly chosen far-away point, including gcd-profile limits and
  percolation comments derived from Vardi.
- Le Fourn-Liu-Martineau (2025) studies percolative properties of the random
  coprime colouring. This is the freshest nearby work found; it asks for the
  number of infinite black/white clusters in random-shift visibility models.
  It supports the heuristic that visible points are robustly percolating after
  local shifts, but it is not a deterministic proof for the origin-centred
  EP1212 graph with prime-prime vertices removed.
- Fernandez-Fernandez (2021) surveys divisibility/random-sample results and
  includes a useful visible-points section: hidden squares via CRT, the
  Herzog-Stewart realizability criterion, and references for random-walk,
  diffraction, ergodic, and percolative treatments.
- Random-walk visibility papers, e.g. Cilleruelo-Fernandez-Fernandez (2019),
  quantify how often paths visit visible points, but they do not directly give
  a deterministic nearest-neighbour infinite path inside the EP1212 subgraph.

## Natural First Attack Routes

1. Robust Vardi route. Try to adapt Vardi's rectangle/mesh proof to a graph
   where prime-prime vertices are deleted. Since prime-prime points have zero
   density, a density-level argument should still see many visible points, but
   the hard part is proving the mesh can be routed without using prime-prime
   junctions.
2. Modified Stewart ladders. Replace the prime-prime corner points in Stewart's
   construction by short detours through adjacent composite rows/columns inside
   prime gaps. This becomes a concrete local condition on consecutive prime
   gaps and coprimality of short horizontal/vertical segments.
3. CRT gadget construction. Use Herzog-Stewart finite-pattern realizability,
   plus extra congruences forcing selected coordinates composite, to build
   repeatable finite connectors. The challenge is chaining the gadgets so the
   endpoint of one forces the placement of the next.
4. Random local-limit heuristic to deterministic scales. Since a random far-away
   window almost never sees a prime coordinate at a specified local offset, the
   EP1212 deletion is invisible in the local coprime-colouring limit. Turning
   this into a deterministic cross-scale path is the main gap.

## Computational and Formalization Hooks

- Implement `H_N`: vertices `(x,y)` with `2 <= x,y <= N`, `gcd(x,y)=1`, and
  `not (prime(x) and prime(y))`; compute components, boundary-touching
  components, and candidate corridors. Store paths as explicit coordinate lists
  whose validity is checkable by gcd and primality tests.
- Search for ladder detours between prime gaps: for consecutive primes
  `p_i < p_{i+1} < p_{i+2}`, test whether the Stewart rectangle can be
  replaced by a path avoiding the two prime-prime corners.
- Encode fixed-size connector gadgets as SAT/CP-SAT: Boolean occupancy for a
  finite grid, arithmetic side constraints supplied by chosen congruence
  classes, then verify any proposed gadget by exact integer checks.
- Formalization-friendly lemmas: Stewart's weak construction from Bertrand
  bounds; finite path certificates; CRT pattern-realization statements; and
  monotone implications from a family of certified annular crossings to an
  infinite path.

## Risks and Unknowns

- Prime-prime vertices are sparse but may be strategically important: Stewart's
  known infinite path uses them as all transition corners.
- Vardi's full-graph infinite component relies on row/column `1` for the easy
  uniqueness argument; EP1212 explicitly removes that backbone.
- Existing percolation/local-limit results concern random shifts or density
  properties, not this exact deterministic induced subgraph.
- Finite computation cannot resolve the problem and may be misleading because
  components can route outside the box.
- A negative result would likely require finding deterministic separating
  barriers made from invisible points plus prime-prime deletions; no such
  barrier mechanism is currently visible.

## Tractability Score

4/10 for a serious attempt over the next few days. Meaningful progress looks
plausible: reproduce computations, test modified Stewart ladders, and isolate a
concrete sufficient crossing lemma. A complete proof seems unlikely in a few
days unless the ladder-detour condition turns out to have a clean prime-gap
argument.

## Three Concrete Next Steps

1. Build a reproducible component/corridor search to `N=5000+`, recording
   largest components, radial spans, and explicit near-miss connectors.
2. Exhaustively test modified Stewart rectangles for the first several thousand
   prime triples, then look for a simple sufficient condition that always holds
   past a finite threshold.
3. Read Vardi Sections 7-8 in detail and mark every use of coordinate-1 lines
   or prime-prime junctions; try to replace those uses with composite-coordinate
   line segments or short detour gadgets.

## Sources

- Official EP1212 page: https://www.erdosproblems.com/1212
- Erdos, "A survey of problems in combinatorial number theory" (1980):
  https://users.renyi.hu/~p_erdos/1980-03.pdf
- Herzog-Stewart, "Patterns of Visible and Nonvisible Lattice Points" (1971):
  https://www.tandfonline.com/doi/abs/10.1080/00029890.1971.11992790
- Vardi, "Deterministic Percolation" (1999):
  https://www.lix.polytechnique.fr/Labo/Ilan.Vardi/deterministic_percolation.pdf
- Martineau, "On coprime percolation, the visibility graphon, and the local
  limit of the GCD profile" (arXiv:1804.06486):
  https://arxiv.org/abs/1804.06486
- Le Fourn-Liu-Martineau, "Percolative properties of the random coprime
  colouring" (arXiv:2509.08452):
  https://arxiv.org/abs/2509.08452
- Fernandez-Fernandez, "Divisibility properties of random samples of integers"
  (2021): https://link.springer.com/article/10.1007/s13398-020-00960-x
- Cilleruelo-Fernandez-Fernandez, "Visible lattice points in random walks"
  (2019): https://www.sciencedirect.com/science/article/pii/S0195669818301380
