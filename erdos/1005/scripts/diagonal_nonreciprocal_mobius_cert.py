#!/usr/bin/env python3
"""Explore truncated Mobius lower certificates for non-reciprocal strips."""

from __future__ import annotations

import argparse
from math import gcd, isqrt
from typing import Optional, Sequence


def predicted_value(n: int) -> int:
    return n // 4 + [1, 2, 2, 4][n % 4]


def mobius_sieve(n: int) -> list[int]:
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    primes: list[int] = []
    mu[0] = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > n:
                break
            is_prime[v] = False
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu


def raw_strip_count(a: int, c: int, r: int, d: int) -> int:
    k = a // d
    total = 0
    for p in range(1, k + 1):
        lo = (c * p) // (a + 1) + 1
        hi = (r * p - 1) // a
        if hi >= lo:
            total += hi - lo + 1
    return total


def mobius_lower(a: int, h: int, r: int, mu: list[int], cutoff: int) -> int:
    c = r - h - 1
    exact = 0
    for d in range(1, min(a, cutoff) + 1):
        if mu[d] != 0:
            exact += mu[d] * raw_strip_count(a, c, r, d)
    tail = 0
    for d in range(cutoff + 1, a + 1):
        tail += raw_strip_count(a, c, r, d)
    return exact - tail


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--cutoff-scale", type=int, default=4)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    mu = mobius_sieve(args.q_max)
    failures: list[tuple[int, int, int, int, int, int, int, int]] = []
    checked = 0
    certified = 0
    worst: tuple[int, int, int, int, int, int, int, int] | None = None

    for h in range(1, args.q_max + 1):
        for a in range(1, args.q_max // h + 1):
            max_r = min(a - 1, args.q_max - h * a)
            for r in range(h + 2, max_r + 1):
                c = r - h - 1
                if gcd(a, r) != 1 or gcd(a + 1, c) != 1:
                    continue
                q = h * a + r
                if q < 92:
                    continue
                cutoff = min(a, max(1, args.cutoff_scale * isqrt(a)))
                lower = mobius_lower(a, h, r, mu, cutoff)
                target = predicted_value(q)
                surplus = lower - target
                row = (surplus, q, h, a, r, cutoff, lower, target)
                checked += 1
                if surplus >= 0:
                    certified += 1
                else:
                    failures.append(row)
                if worst is None or row < worst:
                    worst = row

    failures.sort()
    print(f"checked={checked}")
    print(f"certified={certified}")
    print(f"failures={len(failures)}")
    print(f"worst={worst}")
    for row in failures[: args.max_records]:
        print("FAIL " + ",".join(str(x) for x in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

