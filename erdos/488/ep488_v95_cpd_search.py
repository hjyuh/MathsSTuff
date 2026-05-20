#!/usr/bin/env python3
"""Finite-CPD search for the EP-488 BBDS interface.

For top-window primitive C, let

  mu(t) = #{r in C : r | t and q does not divide t}
  D(x)  = #{t <= x : mu(t) > 0}
  M(x)  = sum_{t<=x} mu(t)
  S(x)  = 2D(x)-M(x)

The finite cyclic-prefix domination target says:

  if every full block j=3..P+2 has nonnegative slack
      sigma_j = 2 BlockCov(j) - SlotMass(j) >= 0,
  then every run-start n in [3q, 3q+qP) satisfies
      S(n) >= 2|C|.

Here P = lcm_{r in C} r/gcd(r,q), the block period.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from itertools import combinations
from math import gcd, lcm
from pathlib import Path


@dataclass
class Failure:
    q: int
    C: list[int]
    P: int
    n: int
    Dn: int
    Mn: int
    S: int
    reserve: int
    gap: int


def primitive(C: tuple[int, ...]) -> bool:
    for i, a in enumerate(C):
        for b in C[i + 1 :]:
            if b % a == 0 or a % b == 0:
                return False
    return True


def period(q: int, C: tuple[int, ...]) -> int:
    P = 1
    for r in C:
        P = lcm(P, r // gcd(r, q))
    return P


def mu_array(q: int, C: tuple[int, ...], xmax: int) -> list[int]:
    mu = [0] * (xmax + 2)
    for r in C:
        for t in range(r, xmax + 1, r):
            if t % q != 0:
                mu[t] += 1
    return mu


def block_cov_mass(q: int, C: tuple[int, ...], j: int) -> tuple[int, int]:
    lo = (j - 1) * q + 1
    hi = j * q
    counts: dict[int, int] = {}
    for r in C:
        first = ((lo + r - 1) // r) * r
        for t in range(first, hi + 1, r):
            if t % q != 0:
                counts[t] = counts.get(t, 0) + 1
    return len(counts), sum(counts.values())


def check_case(q: int, C: tuple[int, ...], P: int) -> Failure | None | bool:
    # Most candidates have an early bad block. Reject them before building the
    # full qP-period prefix arrays.
    for j in range(3, P + 3):
        cov, mass = block_cov_mass(q, C, j)
        if 2 * cov < mass:
            return None

    xmax = (P + 3) * q + 1
    mu = mu_array(q, C, xmax)

    D = [0] * (xmax + 1)
    M = [0] * (xmax + 1)
    for t in range(1, xmax + 1):
        D[t] = D[t - 1] + (1 if mu[t] else 0)
        M[t] = M[t - 1] + mu[t]

    reserve = 2 * len(C)
    for n in range(3 * q, 3 * q + q * P):
        if mu[n] == 0 and mu[n + 1] > 0:
            s = 2 * D[n] - M[n]
            if s < reserve:
                return Failure(
                    q=q,
                    C=list(C),
                    P=P,
                    n=n,
                    Dn=D[n],
                    Mn=M[n],
                    S=s,
                    reserve=reserve,
                    gap=reserve - s,
                )
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--q-max", type=int, default=40)
    ap.add_argument("--max-subset-size", type=int, default=6)
    ap.add_argument("--min-subset-size", type=int, default=1)
    ap.add_argument("--p-max", type=int, default=10000)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    checked = 0
    skipped_period = 0
    no_bad_period = 0
    failures: list[Failure] = []

    for q in range(2, args.q_max + 1):
        vals = tuple(range(q // 2 + 1, q))
        max_size = min(args.max_subset_size, len(vals))
        for r in range(max(1, args.min_subset_size), max_size + 1):
            for C in combinations(vals, r):
                if not primitive(C):
                    continue
                P = period(q, C)
                if P > args.p_max:
                    skipped_period += 1
                    continue
                checked += 1
                result = check_case(q, C, P)
                if result is True:
                    no_bad_period += 1
                elif isinstance(result, Failure):
                    failures.append(result)
                    data = {
                        "q_max": args.q_max,
                        "max_subset_size": args.max_subset_size,
                        "min_subset_size": args.min_subset_size,
                        "p_max": args.p_max,
                        "checked": checked,
                        "skipped_period": skipped_period,
                        "no_bad_period": no_bad_period,
                        "failures": [asdict(f) for f in failures],
                    }
                    text = json.dumps(data, indent=2)
                    if args.json_out:
                        args.json_out.write_text(text + "\n", encoding="utf-8")
                    print(text)
                    return

    data = {
        "q_max": args.q_max,
        "max_subset_size": args.max_subset_size,
        "min_subset_size": args.min_subset_size,
        "p_max": args.p_max,
        "checked": checked,
        "skipped_period": skipped_period,
        "no_bad_period": no_bad_period,
        "failures": [asdict(f) for f in failures],
    }
    text = json.dumps(data, indent=2)
    if args.json_out:
        args.json_out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
