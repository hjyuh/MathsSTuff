# EP1212

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/1212

Status: open.

Tags: number theory, primes.

OEIS: possible.

## Statement

Let `G` have as vertices the coprime lattice points `(x,y)` in `N^2`.
Two vertices are adjacent if they differ by `+1` or `-1` in exactly one
coordinate.

Is there an infinite path in `G` such that every vertex `(x,y)` on the path
has `min(x,y) > 1` and at least one of `x,y` composite?

## Current Notes

This is a visible-lattice-points graph problem. The page says Herzog and
Stewart studied this graph and conjectured a related statement about
points `(a,p)` with `p` prime and `p` not dividing `a`, but Bloom notes he
could not locate that exact result in their visible-lattice-points paper.

Erdos originally asked a weaker version with only `min(x,y)>1`; Stewart
gave a quick construction using paths from `(p_k,p_{k+1})` to
`(p_{k+1},p_{k+2})` through a rectangle when `p_{k+2}<2p_k`, true for all
`k >= 4`.

The official page also suggests stronger variants, such as asking for a
monotone path or one that changes direction only after boundedly many
steps.

## Current Work Products

- `buffered-live-pair-bridge.md`: formal reduction from an infinite ray of
  buffered composite live pairs to an EP1212 path.
- `exact-live-pair-dag.md`: scale-free exact live-pair DAG and equivalence
  with monotone all-composite two-window zig-zag chains.
- `scripts/buffered_live_pair_stats.py`: finite survival-statistics runner for
  raw, regenerative, right-core, and core-to-core live-pair successors.
- `scripts/verify_buffered_certificate.py`: verifier for stored longest-ray
  certificates.
- `buffered-live-pair-computational-pass.md`: first exact runs to `N=50000`.
- `right-core-survival-pass.md`: corrected right-core survival pass, with
  positive core-to-core branching evidence to `N=1e6`.
- `full-resolution-roadmap.md`: theorem stack needed for a complete solution.
- `closure-attempt-log.md`: orchestration log for the multi-agent closure pass.
- `closure-attempt-gpt52.md`, `closure-attempt-gpt54.md`,
  `closure-attempt-gpt55-final.md`: sequential xhigh closure attempts. All
  conclude `NOT CLOSED` and identify the same analytic slab-survival blocker.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/1212
- Source keys on the page: `[Er80,p.114]`, `[HeSt71]`
