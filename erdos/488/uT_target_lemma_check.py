#!/usr/bin/env python3
"""
EP-488 v29: u_T target lemma checker (and counterexample miner).

Target lemma (as written in unified-truth-v29-april12.md):

  For any finite T ⊂ Z_{>=2}, let
      u_T(x) = #{ 1 <= k <= x : ∀t∈T, t ∤ k }.
  Claim: for all integers b >= a >= 1,
      u_T(b)/b <= 2 * u_T(a)/(a+1).

This script searches for violations and prints explicit counterexamples.

Notes:
  - If T contains a modulus that is a multiple of another, it is redundant:
      u_T == u_{primitivize(T)}.
    So it suffices to search primitive antichains T.
  - The checker only searches a finite window; it is meant as a diagnostic
    tool (to kill or to build evidence for a corrected statement).
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, List, Optional, Sequence, Tuple


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


def is_primitive_antichain(values: Sequence[int]) -> bool:
    vals = sorted(values)
    for i, a in enumerate(vals):
        for b in vals[i + 1 :]:
            if b % a == 0:
                return False
    return True


def u_prefix(T: Sequence[int], Bmax: int) -> List[int]:
    """Return u_T(x) for x=0..Bmax."""
    hit = bytearray(Bmax + 1)
    for t in T:
        for m in range(t, Bmax + 1, t):
            hit[m] = 1
    u = [0] * (Bmax + 1)
    s = 0
    for x in range(1, Bmax + 1):
        if not hit[x]:
            s += 1
        u[x] = s
    return u


@dataclass(frozen=True)
class Violation:
    T: Tuple[int, ...]
    a: int
    b: int
    ua: int
    ub: int

    def lhs(self) -> float:
        return self.ub / self.b

    def rhs(self) -> float:
        return 2 * self.ua / (self.a + 1)

    def ratio(self) -> float:
        return self.lhs() / self.rhs()


def find_violation_for_T(T: Sequence[int], *, Bmax: int) -> Optional[Violation]:
    T = primitivize(T)
    if not T:
        return None
    u = u_prefix(T, Bmax)
    for a in range(1, Bmax):
        ua = u[a]
        rhs_num = 2 * ua
        rhs_den = a + 1
        for b in range(a, Bmax + 1):
            # u(b)/b <= 2 u(a)/(a+1)  <=>  u(b)*(a+1) <= 2 u(a)*b
            if u[b] * rhs_den > rhs_num * b:
                return Violation(T=T, a=a, b=b, ua=ua, ub=u[b])
    return None


def all_primitive_T_upto(N: int) -> List[Tuple[int, ...]]:
    vals = list(range(2, N + 1))
    out: List[Tuple[int, ...]] = []
    for mask in range(1, 1 << len(vals)):
        T = tuple(vals[i] for i in range(len(vals)) if (mask >> i) & 1)
        if is_primitive_antichain(T):
            out.append(T)
    return out


def scan_all_T_upto(*, N: int, Bmax: int, limit: int) -> None:
    Ts = all_primitive_T_upto(N)
    found = 0
    worst: Optional[Violation] = None

    for T in Ts:
        v = find_violation_for_T(T, Bmax=Bmax)
        if v is None:
            continue
        found += 1
        if worst is None or v.ratio() > worst.ratio():
            worst = v
        print(
            f"VIOLATION {found}: T={list(v.T)}  a={v.a} b={v.b}  "
            f"u(a)={v.ua} u(b)={v.ub}  "
            f"lhs={v.lhs():.6f} rhs={v.rhs():.6f}  ratio={v.ratio():.6f}"
        )
        if found >= limit:
            break

    print()
    print("=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"primitive T subsets of [2,{N}]: {len(Ts)}")
    print(f"search window: 1<=a<=b<={Bmax}")
    print(f"violations found (up to limit): {found}")
    if worst is not None:
        print("\nWorst ratio (lhs/rhs) among printed violations:")
        print(
            f"  T={list(worst.T)}  a={worst.a} b={worst.b}  "
            f"u(a)={worst.ua} u(b)={worst.ub}  ratio={worst.ratio():.6f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_one = sub.add_parser("one", help="check a single T and print first violation (if any)")
    p_one.add_argument("--T", required=True, help="comma-separated moduli, e.g. 2,3")
    p_one.add_argument("--Bmax", type=int, default=400, help="search up to this b")

    p_all = sub.add_parser("scan", help="scan all primitive T ⊂ [2,N] for violations")
    p_all.add_argument("--N", type=int, default=12)
    p_all.add_argument("--Bmax", type=int, default=300)
    p_all.add_argument("--limit", type=int, default=20, help="max violations to print")

    args = parser.parse_args()

    if args.cmd == "one":
        T = parse_int_list(args.T)
        v = find_violation_for_T(T, Bmax=args.Bmax)
        if v is None:
            print("No violation found in the search window.")
            return
        print("=" * 80)
        print("u_T target lemma violation")
        print("=" * 80)
        print(f"T = {list(v.T)}")
        print(f"a = {v.a}, b = {v.b}")
        print(f"u_T(a) = {v.ua}, u_T(b) = {v.ub}")
        print(f"lhs = u(b)/b = {v.ub}/{v.b} = {v.lhs():.12f}")
        print(f"rhs = 2*u(a)/(a+1) = 2*{v.ua}/({v.a}+1) = {v.rhs():.12f}")
        print(f"lhs/rhs = {v.ratio():.12f}")

    if args.cmd == "scan":
        scan_all_T_upto(N=args.N, Bmax=args.Bmax, limit=args.limit)


if __name__ == "__main__":
    main()

