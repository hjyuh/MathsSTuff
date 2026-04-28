#!/usr/bin/env python3
"""
EP-488 v30: D(x) two-point inequality checker / counterexample miner.

Path 1 (v30) proposes:

  Fix a primitive modulus antichain Q with max(Q)=q.
  Let A_Q(x) be survivors up to x (not divisible by any d in Q).
  Let A_q(x) := A_{ {q} }(x) = x - floor(x/q).
  Define extra coverage beyond the singleton:

      D(x) := A_q(x) - A_Q(x)
           = #{ t <= x : q does NOT divide t, and t is divisible by some r in Q \\ {q} }.

Singleton dominance O_Q(n,m) <= O_{ {q} }(n,m) is equivalent to:

      D(m)/m <= 2 * D(n)/n   for all integers m > n >= q.

This script searches for violations on finite windows.
It is evidence/diagnostic tooling, not a proof.

Notes:
  - We only check the inequality on 1 <= n < m <= Bmax.
  - Console encoding on Windows can be cp1252; avoid unicode in output.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, List, Optional, Sequence, Tuple

from two_point_operator_tools import build_hit_array, is_primitive_antichain, survivors_prefix


def parse_int_list(text: str) -> Tuple[int, ...]:
    parts = [p.strip() for p in text.split(",") if p.strip()]
    vals = tuple(sorted({int(p) for p in parts}))
    if any(v < 2 for v in vals):
        raise ValueError("All moduli must be >= 2.")
    return vals


def primitivize(values: Iterable[int]) -> Tuple[int, ...]:
    vals = sorted(set(v for v in values if v >= 2))
    out: List[int] = []
    for v in vals:
        if any(v % u == 0 for u in out):
            continue
        out.append(v)
    return tuple(out)


def A_singleton_prefix(q: int, Bmax: int) -> List[int]:
    """Return A_{ {q} }(x) for x=0..Bmax."""
    A = [0] * (Bmax + 1)
    for x in range(1, Bmax + 1):
        A[x] = x - (x // q)
    return A


def D_prefix(Q: Sequence[int], Bmax: int) -> Tuple[int, List[int]]:
    """Return q=max(Q) and D(x) for x=0..Bmax."""
    Q = primitivize(Q)
    if not Q:
        raise ValueError("Q must be nonempty.")
    if not is_primitive_antichain(Q):
        raise ValueError("Q must be a primitive antichain (no divisibility among elements).")
    q = max(Q)
    if q not in Q:
        raise ValueError("Internal error: max(Q) not in Q.")

    hit = build_hit_array(Q, Bmax)
    A_Q = survivors_prefix(hit, Bmax)
    A_q = A_singleton_prefix(q, Bmax)

    D = [0] * (Bmax + 1)
    for x in range(1, Bmax + 1):
        D[x] = A_q[x] - A_Q[x]
        if D[x] < 0:
            raise AssertionError("Expected D(x) >= 0.")
    return q, D


def frac_ge(num1: int, den1: int, num2: int, den2: int) -> bool:
    """Return (num1/den1) >= (num2/den2) with positive denominators."""
    return num1 * den2 >= num2 * den1


@dataclass(frozen=True)
class Violation:
    Q: Tuple[int, ...]
    q: int
    n: int
    m: int
    Dn: int
    Dm: int

    def lhs(self) -> float:
        return self.Dm / self.m

    def rhs(self) -> float:
        return 2 * self.Dn / self.n

    def ratio(self) -> float:
        # lhs / rhs
        return (self.Dm * self.n) / (2 * self.Dn * self.m)


def find_violation_for_Q(Q: Sequence[int], *, Bmax: int) -> Optional[Violation]:
    Qp = primitivize(Q)
    if not Qp:
        return None
    if not is_primitive_antichain(Qp):
        return None

    q, D = D_prefix(Qp, Bmax)
    if Bmax <= q:
        raise ValueError("Need Bmax > max(Q)=q so that m>n is possible.")

    # Suffix argmax of D(m)/m.
    best_m_from = [0] * (Bmax + 2)
    best_m = 1
    for i in range(Bmax, 0, -1):
        if frac_ge(D[i], i, D[best_m], best_m):
            best_m = i
        best_m_from[i] = best_m

    for n in range(q, Bmax):
        Dn = D[n]
        # Dn should be positive for any Q with >=2 elements and n>=q, but guard anyway.
        if Dn == 0:
            continue
        m = best_m_from[n + 1]
        if m <= n:
            continue
        Dm = D[m]
        # Check: D(m)/m <= 2 D(n)/n  <=>  Dm*n <= 2*Dn*m
        if Dm * n > 2 * Dn * m:
            return Violation(Q=tuple(Qp), q=q, n=n, m=m, Dn=Dn, Dm=Dm)
    return None


def all_primitive_Q_upto(N: int, *, min_size: int) -> List[Tuple[int, ...]]:
    vals = list(range(2, N + 1))
    out: List[Tuple[int, ...]] = []
    for mask in range(1, 1 << len(vals)):
        Q = tuple(vals[i] for i in range(len(vals)) if (mask >> i) & 1)
        if len(Q) < min_size:
            continue
        if is_primitive_antichain(Q):
            out.append(Q)
    return out


def scan_all_Q_upto(*, N: int, Bmult: int, min_size: int, limit: int) -> None:
    Qs = all_primitive_Q_upto(N, min_size=min_size)
    found = 0
    worst: Optional[Violation] = None

    for Q in Qs:
        q = max(Q)
        Bmax = Bmult * q
        v = find_violation_for_Q(Q, Bmax=Bmax)
        if v is None:
            continue
        found += 1
        if worst is None or v.ratio() > worst.ratio():
            worst = v
        print(
            f"VIOLATION {found}: Q={list(v.Q)} q={v.q}  n={v.n} m={v.m}  "
            f"D(n)={v.Dn} D(m)={v.Dm}  lhs={v.lhs():.6f} rhs={v.rhs():.6f}  ratio={v.ratio():.6f}"
        )
        if found >= limit:
            break

    print()
    print("=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"primitive Q subsets of [2,{N}] with |Q|>={min_size}: {len(Qs)}")
    print(f"scan window: for each Q with max=q, checked q <= n < m <= {Bmult}*q")
    print(f"violations found (up to limit): {found}")
    if worst is not None:
        print("\nWorst ratio (lhs/rhs) among printed violations:")
        print(
            f"  Q={list(worst.Q)} q={worst.q} n={worst.n} m={worst.m}  "
            f"D(n)={worst.Dn} D(m)={worst.Dm}  ratio={worst.ratio():.6f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_one = sub.add_parser("one", help="check a single Q and print first violation (if any)")
    p_one.add_argument("--Q", required=True, help="comma-separated moduli, e.g. 98,99,100")
    p_one.add_argument("--Bmax", type=int, default=2000, help="search up to this m")

    p_all = sub.add_parser("scan", help="scan all primitive Q subset [2,N] for violations")
    p_all.add_argument("--N", type=int, default=15)
    p_all.add_argument("--Bmult", type=int, default=30, help="for each Q with max=q, check up to m<=Bmult*q")
    p_all.add_argument("--min-size", type=int, default=2, help="ignore smaller sets")
    p_all.add_argument("--limit", type=int, default=10, help="max violations to print")

    args = parser.parse_args()

    if args.cmd == "one":
        Q = parse_int_list(args.Q)
        v = find_violation_for_Q(Q, Bmax=args.Bmax)
        if v is None:
            print("No violation found in the search window.")
            return
        print("=" * 80)
        print("D(x) two-point inequality violation")
        print("=" * 80)
        print(f"Q = {list(v.Q)}  (q=max(Q)={v.q})")
        print(f"n = {v.n}, m = {v.m}")
        print(f"D(n) = {v.Dn}, D(m) = {v.Dm}")
        print(f"lhs = D(m)/m = {v.Dm}/{v.m} = {v.lhs():.12f}")
        print(f"rhs = 2*D(n)/n = 2*{v.Dn}/{v.n} = {v.rhs():.12f}")
        print(f"lhs/rhs = {v.ratio():.12f}")
        return

    if args.cmd == "scan":
        scan_all_Q_upto(N=args.N, Bmult=args.Bmult, min_size=args.min_size, limit=args.limit)


if __name__ == "__main__":
    main()

