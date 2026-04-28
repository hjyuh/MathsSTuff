"""
EP-488 (Open Field v25): recursive package coefficients + live-edge statistics.

This script implements the "recursive package" recurrence

    P_s = C*(s) +  Σ_{(s -> t, h) live} (h/2) · P_t ,

where:
  - s is a band index (s >= 4, with s = 5 globally dead),
  - (s -> t, h) is a geometric bad-to-bad edge with odd h,
  - edges are declared live iff the badness ranges U_s and U_t intersect,
  - C*(s) is the universal constrained excess constant with the only justified
    t-bound coming from the convexity window:
        t = floor((s+1)·lambda)  <=  (s+1)·lambda_max
    and we default lambda_max = 10 (so t <= 10·(s+1)).

It also computes exact band coefficients

    c_s(lambda) = (s+1)·(L_s(t) - 2·lambda),   t = floor((s+1)·lambda),

where L_s(t) counts integers 1 <= x <= t coprime to every prime <= s.

Requested diagnostics:
  - P_s for a given range (e.g. 15..25),
  - out-degree growth of the live bad-to-bad digraph,
  - exact sum at a fixed lambda:
        Σ_{active s <= S} c_s(lambda)·P_s·(2s+1)/(s^2 (s+1)^2).
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


def parse_fraction(text: str) -> Fraction:
    text = text.strip()
    if "/" in text:
        num, den = text.split("/", 1)
        return Fraction(int(num.strip()), int(den.strip()))
    if "." in text:
        return Fraction(text)  # exact from decimal string
    return Fraction(int(text), 1)


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def coprime_prefix_count(primes: list[int], t_max: int) -> list[int]:
    """
    Return prefix counts L[t] = #{1 <= x <= t : gcd(x, prod(primes)) = 1}.
    """
    bad = bytearray(t_max + 1)
    for p in primes:
        for m in range(p, t_max + 1, p):
            bad[m] = 1

    prefix = [0] * (t_max + 1)
    running = 0
    for x in range(1, t_max + 1):
        if not bad[x]:
            running += 1
        prefix[x] = running
    return prefix


Interval = tuple[Fraction, Fraction]


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    if not intervals:
        return []
    intervals = sorted(intervals)
    merged: list[list[Fraction]] = [[intervals[0][0], intervals[0][1]]]
    for left, right in intervals[1:]:
        if left > merged[-1][1]:
            merged.append([left, right])
        elif right > merged[-1][1]:
            merged[-1][1] = right
    return [(a, b) for a, b in merged]


def intervals_intersect(a: list[Interval], b: list[Interval]) -> bool:
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        left = max(a[i][0], b[j][0])
        right = min(a[i][1], b[j][1])
        if left < right:
            return True
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return False


@dataclass(frozen=True)
class BandData:
    s: int
    t_max: int
    c_star: int
    best_t: int
    L_prefix: list[int]
    U: list[Interval]


def band_data(s: int, lam_max: Fraction) -> BandData:
    primes = primes_up_to(s)
    t_max = int((s + 1) * lam_max)  # floor
    L_prefix = coprime_prefix_count(primes, t_max)

    best_t = -1
    c_star = -(10**30)
    for t in range(s + 1, t_max + 1):
        val = (s + 1) * L_prefix[t] - 2 * t
        if val > c_star:
            c_star = val
            best_t = t

    intervals: list[Interval] = []
    for t in range(s + 1, t_max + 1):
        l_val = L_prefix[t]
        left = Fraction(t, s + 1)
        right = min(Fraction(t + 1, s + 1), Fraction(l_val, 2), lam_max)
        if left < right:
            intervals.append((left, right))

    return BandData(
        s=s,
        t_max=t_max,
        c_star=int(c_star),
        best_t=best_t,
        L_prefix=L_prefix,
        U=merge_intervals(intervals),
    )


def odd_integers_in_open_interval(left: Fraction, right: Fraction) -> Iterable[int]:
    """
    Yield odd integers h with left < h < right.
    """
    h = math.floor(left) + 1
    if h % 2 == 0:
        h += 1
    while Fraction(h, 1) < right:
        yield h
        h += 2


def live_edges_for_root(root: int, U: dict[int, list[Interval]]) -> list[tuple[int, int]]:
    """
    Live edges (root -> child, h) with child < root and odd h satisfying
      2*root/(child+1) < h < 2*(root+1)/child
    and U_root ∩ U_child ≠ ∅.
    """
    edges: list[tuple[int, int]] = []
    for child in range(4, root):
        if child == 5:
            continue
        if not intervals_intersect(U[root], U[child]):
            continue
        left = Fraction(2 * root, child + 1)
        right = Fraction(2 * (root + 1), child)
        for h in odd_integers_in_open_interval(left, right):
            if h >= 3:
                edges.append((child, h))
    return edges


def coefficient_c(s: int, lam: Fraction, L_prefix: list[int]) -> Fraction:
    t = int((s + 1) * lam)  # floor
    l_val = L_prefix[t]
    return (s + 1) * (Fraction(l_val, 1) - 2 * lam)


def compute_all(max_s: int, lam_max: Fraction) -> tuple[dict[int, BandData], dict[int, Fraction], dict[int, list[tuple[int, int]]]]:
    bands: dict[int, BandData] = {}
    for s in range(4, max_s + 1):
        if s == 5:
            continue
        bands[s] = band_data(s, lam_max)

    U = {s: b.U for s, b in bands.items()}

    edges: dict[int, list[tuple[int, int]]] = {}
    for s in range(4, max_s + 1):
        if s == 5:
            continue
        edges[s] = live_edges_for_root(s, U)

    P: dict[int, Fraction] = {}
    for s in range(4, max_s + 1):
        if s == 5:
            continue
        total = Fraction(bands[s].c_star, 1)
        for child, h in edges[s]:
            total += Fraction(h, 2) * P[child]
        P[s] = total

    return bands, P, edges


def parse_range(text: str) -> tuple[int, int]:
    if "-" not in text:
        s = int(text)
        return s, s
    a, b = text.split("-", 1)
    return int(a), int(b)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lam-max", default="10", help="Max lambda used for the universal t-bound (default: 10).")
    parser.add_argument("--max-s", type=int, default=200, help="Compute bands/edges/P_s up to this s (default: 200).")
    parser.add_argument("--print-range", default="15-25", help="Print P_s table for this s-range (default: 15-25).")
    parser.add_argument("--degree-stats", type=int, default=500, help="Also compute out-degree stats up to this s (default: 500).")
    parser.add_argument("--lambda", dest="lam", default="29/20", help="Lambda value for exact sum check (default: 29/20).")
    parser.add_argument("--sum-max-s", type=int, default=200, help="Max s for the exact lambda-sum (default: 200).")
    args = parser.parse_args()

    lam_max = parse_fraction(args.lam_max)
    lam = parse_fraction(args.lam)
    max_s = max(args.max_s, args.degree_stats, args.sum_max_s)

    bands, P, edges = compute_all(max_s, lam_max)

    lo, hi = parse_range(args.print_range)
    lo = max(lo, 4)
    hi = min(hi, max_s)

    print(f"lam_max = {lam_max}  (t <= floor((s+1)*lam_max))")
    print()
    print("P_s table:")
    print("s  C*(s)  best_t  outdeg  P_s                  P_s/s^2")
    for s in range(lo, hi + 1):
        if s == 5:
            continue
        pdata = bands[s]
        ps = P[s]
        ratio = float(ps) / (s * s)
        print(f"{s:2d} {pdata.c_star:6d} {pdata.best_t:7d} {len(edges[s]):6d} {str(ps):>18s}  {ratio:10.6f}")

    print()
    print("Edges in range:")
    for s in range(lo, hi + 1):
        if s == 5:
            continue
        print(f"  s={s}: {edges[s]}")

    # Out-degree stats
    deg_max = min(args.degree_stats, max_s)
    max_out = -1
    arg_max = None
    for s in range(4, deg_max + 1):
        if s == 5:
            continue
        outdeg = len(edges[s])
        if outdeg > max_out:
            max_out = outdeg
            arg_max = s
    print()
    print(f"Live out-degree up to s={deg_max}: max {max_out} at s={arg_max}.")
    sample = [10, 14, 25, 50, 100, 150, 200, deg_max]
    sample = [s for s in sample if 4 <= s <= deg_max and s != 5]
    if sample:
        print("Sample out-degrees:", ", ".join(f"{s}:{len(edges[s])}" for s in sample))

    # Exact lambda-sum
    sum_max_s = min(args.sum_max_s, max_s)
    total = Fraction(0, 1)
    active_count = 0
    for s in range(4, sum_max_s + 1):
        if s == 5:
            continue
        coeff = coefficient_c(s, lam, bands[s].L_prefix)
        if coeff <= 0:
            continue
        active_count += 1
        geom = Fraction(2 * s + 1, s * s * (s + 1) * (s + 1))
        total += coeff * P[s] * geom

    print()
    print(f"lambda = {lam}  active bands in [4,{sum_max_s}] (excluding 5): {active_count}")
    print(f"Sum sum_{'{'}active s<=S{'}'} c_s(lambda)*P_s*(2s+1)/(s^2 (s+1)^2) = {total}")
    print(f"Float approx {float(total):.12g}")
    print(f"Comparison: sum < lambda ?  {total < lam}")


if __name__ == "__main__":
    main()
