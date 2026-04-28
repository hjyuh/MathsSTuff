#!/usr/bin/env python3
"""
Route 2, Step 2 sanity checks:

Compare max O_Q(n,m) for primitive Q with |Q|>=3 and max(Q)=q
against the proved adjacent-pair benchmark for {q-1,q}.

This is *evidence*, not a proof.
"""

from __future__ import annotations

import argparse
from itertools import combinations
from fractions import Fraction
from typing import Iterable, List, Sequence, Tuple

from two_point_operator_tools import (
    MaxOResult,
    adjacent_pair_lcm_edge_candidate,
    is_primitive_antichain,
    max_O_over_window,
)


def adjacent_pair_max(q: int) -> Fraction:
    # Exact global maximum for Q={q-1,q}.
    return adjacent_pair_lcm_edge_candidate(q)


def enumerate_primitive_Qs(
    q: int, *, window: int, min_size: int, max_size: int
) -> Iterable[Tuple[int, ...]]:
    lo = max(2, q - window)
    candidates = list(range(lo, q))  # exclude q itself
    for size in range(min_size, max_size + 1):
        choose = size - 1
        for subset in combinations(candidates, choose):
            Q = tuple(sorted(subset + (q,)))
            if is_primitive_antichain(Q):
                yield Q


def worst_in_window(
    q: int,
    *,
    window: int,
    min_size: int,
    max_size: int,
    n_hi: int,
    m_hi: int,
    use_run_ends: bool,
) -> MaxOResult | None:
    best: MaxOResult | None = None
    for Q in enumerate_primitive_Qs(q, window=window, min_size=min_size, max_size=max_size):
        res = max_O_over_window(
            Q,
            n_lo=q,
            n_hi=n_hi,
            m_hi=m_hi,
            use_run_ends=use_run_ends,
        )
        if res is None:
            continue
        if best is None or best.value() < res.value():
            best = res
    return best


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", type=int, required=True)
    ap.add_argument("--window", type=int, default=15, help="enumerate Q ⊂ [q-window,q]")
    ap.add_argument("--min-size", type=int, default=3)
    ap.add_argument("--max-size", type=int, default=6)
    ap.add_argument("--n-hi-mult", type=int, default=10, help="n_hi = n_hi_mult*q")
    ap.add_argument(
        "--m-hi",
        type=int,
        default=0,
        help="absolute m_hi (0 => use max((q-1)^2, m_mult*q) with --m-mult)",
    )
    ap.add_argument("--m-mult", type=int, default=200, help="used if --m-hi=0")
    ap.add_argument("--no-run-ends", action="store_true")
    args = ap.parse_args()

    q = args.q
    if q < 5:
        raise SystemExit("Need q>=5 for the |Q|>=3 scan to make sense.")
    if args.min_size < 3:
        raise SystemExit("Use min_size>=3 for Route 2 step 2.")

    n_hi = args.n_hi_mult * q
    if args.m_hi and args.m_hi > 0:
        m_hi = args.m_hi
    else:
        m_hi = max((q - 1) * (q - 1), args.m_mult * q)

    best = worst_in_window(
        q,
        window=args.window,
        min_size=args.min_size,
        max_size=args.max_size,
        n_hi=n_hi,
        m_hi=m_hi,
        use_run_ends=not args.no_run_ends,
    )
    if best is None:
        raise SystemExit("No primitive Q found in the given window.")

    adj = adjacent_pair_max(q)
    print("=" * 80)
    print("Route 2 step 2 check: |Q|>=3 vs adjacent-pair benchmark")
    print("=" * 80)
    print(f"q={q}, scan Q in [{max(2,q-args.window)},{q}] containing q")
    print(f"sizes: {args.min_size}..{args.max_size}")
    print(f"window: n in [{q},{n_hi}], m in [n+1,{m_hi}]")
    print(f"run-end restriction: {'OFF' if args.no_run_ends else 'ON'}")
    print()
    print(f"worst found Q = {list(best.Q)} (|Q|={len(best.Q)})")
    print(f"argmax (n,m)=({best.n},{best.m})  O={best.num}/{best.den}={float(best.value()):.12f}")
    print()
    print(f"adjacent pair max for {{q-1,q}}: {adj} = {float(adj):.12f}")
    if best.value() >= adj:
        print("!! VIOLATION on this search window !!")
    else:
        gap = adj - best.value()
        print(f"gap (adj - worst_found) = {gap} = {float(gap):.12e}")


if __name__ == "__main__":
    main()
