#!/usr/bin/env python3
"""
EP-488 v28: Two-point operator tooling.

We work with the sieve survivor count

  A_Q(x) := #{1 <= n <= x : for all q in Q, q ∤ n}

and the two-point operator

  O_Q(n,m) := 2*A_Q(n)/n - A_Q(m)/m.

This script computes exact maxima of O_Q on finite search windows using an
O(X) suffix-min trick (rather than O(X^2) brute force).

It also supports scanning all primitive pairs {r,q} with fixed max(Q)=q to
find the worst pair.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from itertools import combinations
from typing import Iterable, List, Optional, Sequence, Tuple


def parse_int_list(text: str) -> Tuple[int, ...]:
    parts = [p.strip() for p in text.split(",") if p.strip()]
    vals = tuple(sorted({int(p) for p in parts}))
    if any(v < 2 for v in vals):
        raise ValueError("All moduli must be >= 2.")
    return vals


def is_primitive_antichain(values: Sequence[int]) -> bool:
    vals = sorted(values)
    for i, a in enumerate(vals):
        for b in vals[i + 1 :]:
            if b % a == 0:
                return False
    return True


def build_hit_array(Q: Sequence[int], X: int) -> bytearray:
    hit = bytearray(X + 2)  # +1 so we can safely query hit[X+1]
    for q in Q:
        for m in range(q, X + 2, q):
            hit[m] = 1
    return hit


def survivors_prefix(hit: bytearray, X: int) -> List[int]:
    A = [0] * (X + 2)
    s = 0
    for x in range(1, X + 2):
        if not hit[x]:
            s += 1
        A[x] = s
    return A


def frac_le(num1: int, den1: int, num2: int, den2: int) -> bool:
    """Return (num1/den1) <= (num2/den2) with positive denominators."""
    return num1 * den2 <= num2 * den1


def frac_lt(num1: int, den1: int, num2: int, den2: int) -> bool:
    return num1 * den2 < num2 * den1


@dataclass(frozen=True)
class MaxOResult:
    Q: Tuple[int, ...]
    n: int
    m: int
    num: int
    den: int

    def value(self) -> Fraction:
        return Fraction(self.num, self.den)


def max_O_over_window(
    Q: Sequence[int],
    *,
    n_lo: int,
    n_hi: int,
    m_hi: int,
    use_run_ends: bool,
) -> Optional[MaxOResult]:
    Q = tuple(sorted(Q))
    assert Q
    assert is_primitive_antichain(Q)
    assert n_lo >= max(Q)
    assert n_hi < m_hi

    hit = build_hit_array(Q, m_hi)
    A = survivors_prefix(hit, m_hi)

    # Eligibility masks for the run-end lemma.
    eligible_n = [True] * (m_hi + 2)
    eligible_m = [True] * (m_hi + 2)
    if use_run_ends:
        for x in range(1, m_hi + 1):
            uncovered_x = hit[x] == 0
            uncovered_x1 = hit[x + 1] == 0
            eligible_n[x] = uncovered_x and (not uncovered_x1)  # n uncovered, n+1 covered
            eligible_m[x] = (not uncovered_x) and uncovered_x1  # m covered, m+1 uncovered

    # Suffix argmin for A(m)/m over eligible m.
    best_m_from = [0] * (m_hi + 3)
    has_best = False
    best_m = m_hi
    # Initialize with the last eligible m in [1..m_hi].
    for m in range(m_hi, 0, -1):
        if eligible_m[m]:
            best_m = m
            has_best = True
            break
    if not has_best:
        return None

    for i in range(m_hi, 0, -1):
        if eligible_m[i]:
            # Tie-break to smaller m (scan is descending, so update on equality).
            if frac_le(A[i], i, A[best_m], best_m):
                best_m = i
        best_m_from[i] = best_m

    best_num = -1
    best_den = 1
    best_pair: Tuple[int, int] | None = None

    for n in range(n_lo, n_hi + 1):
        if use_run_ends and not eligible_n[n]:
            continue
        m = best_m_from[n + 1]
        if m <= n:
            continue
        # O = 2*A(n)/n - A(m)/m = (2*A(n)*m - A(m)*n)/(n*m)
        num = 2 * A[n] * m - A[m] * n
        den = n * m
        if best_pair is None or frac_lt(best_num, best_den, num, den):
            best_num, best_den, best_pair = num, den, (n, m)

    if best_pair is None:
        return None
    n_best, m_best = best_pair
    g = gcd(best_num, best_den)
    return MaxOResult(Q=Q, n=n_best, m=m_best, num=best_num // g, den=best_den // g)


def singleton_max(q: int) -> Fraction:
    return Fraction(q * (2 * q - 1) - 1, q * (2 * q - 1))


def adjacent_pair_candidate(q: int) -> Fraction:
    # Value at (n,m)=(2q-3,2q) for Q={q-1,q}.
    return Fraction(q * (2 * q - 3) - 6, q * (2 * q - 3))


def adjacent_pair_lcm_edge_candidate(q: int) -> Fraction:
    # Value at (n,m)=(2q-3,(q-1)^2) for Q={q-1,q}.
    # This point is m = lcm(q-1,q) - (q-1) and empirically appears to be the true global max.
    den = (2 * q - 3) * (q - 1) * (q - 1)
    return Fraction(den - (4 * q - 5), den)


def consecutive_triple_candidate(q: int) -> Fraction:
    # Value at the observed/global maximizer for Q={q-2,q-1,q}.
    # Let a=q-2. The argmax is (n,m)=(2a-1, a^2/g) where g=gcd(a,q)=gcd(q,2).
    # The value depends on parity:
    #   q odd:  1 - 6/(2q-5) + 3(q-3)/(q-2)^2
    #   q even: 1 - 6/(2q-5) + (3q-10)/(q-2)^2
    if q < 5:
        raise ValueError("Need q >= 5 for the consecutive triple {q-2,q-1,q}.")
    a = q - 2
    den = (2 * a - 1) * a * a
    if q % 2 == 1:
        # 1 - 6/(2a-1) + 3(a-1)/a^2
        num = den - 6 * a * a + 3 * (a - 1) * (2 * a - 1)
        return Fraction(num, den)
    # 1 - 6/(2a-1) + (3a-4)/a^2
    num = den - 6 * a * a + (3 * a - 4) * (2 * a - 1)
    return Fraction(num, den)


def consecutive_triple_argmax(q: int) -> Tuple[int, int]:
    if q < 5:
        raise ValueError("Need q >= 5 for the consecutive triple {q-2,q-1,q}.")
    a = q - 2
    g = gcd(a, q)  # = gcd(q,2)
    return (2 * a - 1, (a * a) // g)


def scan_worst_pair(
    q: int,
    *,
    n_mult: int,
    m_mult: int,
    use_run_ends: bool,
) -> MaxOResult:
    n_hi = min(n_mult * q, m_mult * q - 1)
    if n_hi < q:
        raise ValueError("Search window invalid: need n_hi >= q and m_hi >= q+1.")
    best: MaxOResult | None = None
    for r in range(2, q):
        if q % r == 0:
            continue  # not primitive
        res = max_O_over_window(
            (r, q),
            n_lo=q,
            n_hi=n_hi,
            m_hi=m_mult * q,
            use_run_ends=use_run_ends,
        )
        if res is None:
            continue
        if best is None or best.value() < res.value():
            best = res
    assert best is not None
    return best


def scan_worst_compact(
    q: int,
    *,
    window: int,
    min_size: int,
    max_size: int,
    n_mult: int,
    m_mult: int,
    use_run_ends: bool,
) -> List[MaxOResult]:
    """
    Enumerate primitive antichains Q in [q-window, q] with q in Q and find,
    for each size in [min_size, max_size], the worst max O_Q on the window.
    """
    if q < 3:
        raise ValueError("q must be >= 3.")
    if window < 1:
        raise ValueError("window must be >= 1.")
    if not (2 <= min_size <= max_size):
        raise ValueError("Need 2 <= min_size <= max_size.")

    lo = max(2, q - window)
    candidates = list(range(lo, q))  # excludes q itself

    results_by_size: List[MaxOResult] = []
    for size in range(min_size, max_size + 1):
        best: MaxOResult | None = None
        choose = size - 1
        for subset in combinations(candidates, choose):
            Q = tuple(sorted(subset + (q,)))
            if not is_primitive_antichain(Q):
                continue
            res = max_O_over_window(
                Q,
                n_lo=q,
                n_hi=min(n_mult * q, m_mult * q - 1),
                m_hi=m_mult * q,
                use_run_ends=use_run_ends,
            )
            if res is None:
                continue
            if best is None or best.value() < res.value():
                best = res
        if best is not None:
            results_by_size.append(best)

    return results_by_size


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_max = sub.add_parser("maxO", help="compute max O_Q(n,m) on a window")
    p_max.add_argument("--Q", required=True, help="comma-separated moduli, e.g. 164,165")
    p_max.add_argument("--n-mult", type=int, default=10, help="search n in [max(Q), n_mult*max(Q)]")
    p_max.add_argument("--m-mult", type=int, default=10, help="search m in [n+1, m_mult*max(Q)]")
    p_max.add_argument("--no-run-ends", action="store_true", help="do not restrict to run-end pairs")

    p_pair = sub.add_parser("worstPair", help="scan primitive pairs {r,q} and find the worst")
    p_pair.add_argument("--q", type=int, required=True, help="max modulus q")
    p_pair.add_argument("--n-mult", type=int, default=10)
    p_pair.add_argument("--m-mult", type=int, default=10)
    p_pair.add_argument("--no-run-ends", action="store_true")

    p_compact = sub.add_parser("worstCompact", help="scan primitive Q in a top window [q-window,q]")
    p_compact.add_argument("--q", type=int, required=True, help="max modulus q")
    p_compact.add_argument("--window", type=int, default=12, help="scan Q in [q-window,q]")
    p_compact.add_argument("--min-size", type=int, default=2, help="minimum |Q| to scan")
    p_compact.add_argument("--max-size", type=int, default=6, help="maximum |Q| to scan")
    p_compact.add_argument("--n-mult", type=int, default=10)
    p_compact.add_argument("--m-mult", type=int, default=10)
    p_compact.add_argument("--no-run-ends", action="store_true")

    args = parser.parse_args()

    if args.cmd == "maxO":
        Q = parse_int_list(args.Q)
        if not is_primitive_antichain(Q):
            raise SystemExit("Q is not a primitive antichain (some element divides another).")
        q = max(Q)
        res = max_O_over_window(
            Q,
            n_lo=q,
            n_hi=min(args.n_mult * q, args.m_mult * q - 1),
            m_hi=args.m_mult * q,
            use_run_ends=not args.no_run_ends,
        )
        if res is None:
            raise SystemExit("No maximizing pair found in the window.")
        print("=" * 80)
        print("Two-point operator maximum on finite window")
        print("=" * 80)
        print(f"Q = {list(res.Q)} (|Q|={len(res.Q)}, max(Q)={max(res.Q)})")
        print(f"window: n in [{q}, {min(args.n_mult*q, args.m_mult*q-1)}], m in [n+1, {args.m_mult*q}]")
        print(f"run-end restriction: {'OFF' if args.no_run_ends else 'ON'}")
        print()
        print(f"argmax (n,m) = ({res.n}, {res.m})")
        print(f"max O_Q(n,m) = {res.num}/{res.den} = {float(res.value()):.12f}")
        if len(res.Q) == 1:
            q0 = res.Q[0]
            print(f"singleton theorem value = {singleton_max(q0)} = {float(singleton_max(q0)):.12f}")
        if len(res.Q) == 2 and res.Q[1] == res.Q[0] + 1:
            q0 = res.Q[1]
            cand = adjacent_pair_candidate(q0)
            print(f"adjacent-pair candidate at (2q-3,2q) = {cand} = {float(cand):.12f}")
            edge = adjacent_pair_lcm_edge_candidate(q0)
            print(f"adjacent-pair candidate at (2q-3,(q-1)^2) = {edge} = {float(edge):.12f}")
        if len(res.Q) == 3 and res.Q[0] + 2 == res.Q[2] and res.Q[1] == res.Q[0] + 1:
            q0 = res.Q[2]
            n0, m0 = consecutive_triple_argmax(q0)
            cand = consecutive_triple_candidate(q0)
            print(f"consecutive-triple candidate at (n,m)=({n0},{m0}) = {cand} = {float(cand):.12f}")

    if args.cmd == "worstPair":
        q = args.q
        if q < 3:
            raise SystemExit("q must be >= 3.")
        best = scan_worst_pair(
            q,
            n_mult=args.n_mult,
            m_mult=args.m_mult,
            use_run_ends=not args.no_run_ends,
        )
        print("=" * 80)
        print("Worst primitive pair (r,q) on finite window")
        print("=" * 80)
        print(f"q = {q}")
        print(f"window: n in [{q}, {args.n_mult*q}], m in [n+1, {args.m_mult*q}]")
        print(f"run-end restriction: {'OFF' if args.no_run_ends else 'ON'}")
        print()
        print(f"worst pair Q = {list(best.Q)}")
        print(f"argmax (n,m) = ({best.n}, {best.m})")
        print(f"max O_Q(n,m) = {best.num}/{best.den} = {float(best.value()):.12f}")
        print()
        print(f"singleton bound for q: 1 - 1/(q(2q-1)) = {singleton_max(q)} = {float(singleton_max(q)):.12f}")
        if best.Q == (q - 1, q):
            print(f"adjacent-pair candidate at (2q-3,2q): {adjacent_pair_candidate(q)} = {float(adjacent_pair_candidate(q)):.12f}")
            print(
                f"adjacent-pair candidate at (2q-3,(q-1)^2): {adjacent_pair_lcm_edge_candidate(q)} "
                f"= {float(adjacent_pair_lcm_edge_candidate(q)):.12f}"
            )

    if args.cmd == "worstCompact":
        q = args.q
        results = scan_worst_compact(
            q,
            window=args.window,
            min_size=args.min_size,
            max_size=args.max_size,
            n_mult=args.n_mult,
            m_mult=args.m_mult,
            use_run_ends=not args.no_run_ends,
        )
        print("=" * 80)
        print("Worst primitive Q in top window")
        print("=" * 80)
        print(f"q = {q}, window=[{max(2, q-args.window)},{q}]")
        print(f"scan sizes: {args.min_size}..{args.max_size}")
        print(f"window: n in [{q}, {min(args.n_mult*q, args.m_mult*q-1)}], m in [n+1, {args.m_mult*q}]")
        print(f"run-end restriction: {'OFF' if args.no_run_ends else 'ON'}")
        print()

        if not results:
            print("No primitive sets found in this window for the given sizes.")
            return

        overall = max(results, key=lambda r: r.value())
        print("Best-by-size:")
        for res in results:
            print(
                f"  |Q|={len(res.Q)}  Q={list(res.Q)}  "
                f"argmax=({res.n},{res.m})  O={res.num}/{res.den}={float(res.value()):.12f}"
            )
        print()
        print(
            f"Overall worst: |Q|={len(overall.Q)} Q={list(overall.Q)} "
            f"argmax=({overall.n},{overall.m}) O={overall.num}/{overall.den}={float(overall.value()):.12f}"
        )
        print()
        print(f"Singleton bound for q: {singleton_max(q)} = {float(singleton_max(q)):.12f}")
        print(f"Adjacent pair (q-1,q) candidate at (2q-3,2q): {adjacent_pair_candidate(q)} = {float(adjacent_pair_candidate(q)):.12f}")
        print(
            f"Adjacent pair (q-1,q) candidate at (2q-3,(q-1)^2): {adjacent_pair_lcm_edge_candidate(q)} "
            f"= {float(adjacent_pair_lcm_edge_candidate(q)):.12f}"
        )
        if q >= 5:
            n0, m0 = consecutive_triple_argmax(q)
            print(
                f"Consecutive triple (q-2,q-1,q) candidate at (n,m)=({n0},{m0}): {consecutive_triple_candidate(q)} "
                f"= {float(consecutive_triple_candidate(q)):.12f}"
            )


if __name__ == "__main__":
    main()
