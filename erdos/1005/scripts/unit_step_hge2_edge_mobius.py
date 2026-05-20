#!/usr/bin/env python3
"""Mobius lower certificates for H>=2 unit-step edge minimal order."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value


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


def raw_scaled_count(g: int, x: int, y: int, d: int) -> int:
    """Raw count of points in the p<=gx minimal-order strip divisible by d."""
    g_x = g * x
    x_left = g_x - 1
    n = g * y + 1
    d_right = g * y - 1
    p_max = g_x // d
    q_max = n // d
    total = 0
    for p in range(1, p_max + 1):
        lo = (d_right * p) // g_x + 1
        hi = ((n * p) - 1) // x_left
        if hi > q_max:
            hi = q_max
        if hi >= lo:
            total += hi - lo + 1
    return total


def exact_subcount(g: int, x: int, y: int) -> int:
    total = 0
    g_x = g * x
    x_left = g_x - 1
    n = g * y + 1
    d_right = g * y - 1
    for p in range(1, g_x + 1):
        lo = (d_right * p) // g_x + 1
        hi = ((n * p) - 1) // x_left
        if hi > n:
            hi = n
        total += sum(1 for q in range(lo, hi + 1) if gcd(p, q) == 1)
    return total


def mobius_lower(g: int, x: int, y: int, mu: list[int], cutoff: int) -> int:
    g_x = g * x
    exact = 0
    for d in range(1, min(cutoff, g_x) + 1):
        if mu[d]:
            exact += mu[d] * raw_scaled_count(g, x, y, d)
    tail = 0
    for d in range(cutoff + 1, g_x + 1):
        tail += raw_scaled_count(g, x, y, d)
    return exact - tail


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--cutoff", type=int, default=64)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    mu = mobius_sieve(args.n_max)
    checked = 0
    exact_bad = 0
    mobius_bad: list[tuple[int, int, int, int, int, int, int]] = []
    exact_best: tuple[int, int, int, int, int, int, int] | None = None
    mobius_best: tuple[int, int, int, int, int, int, int] | None = None

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n = g * y + 1
            if n < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n) != 1:
                    continue
                target = predicted_value(n)
                exact = exact_subcount(g, x, y)
                lower = mobius_lower(g, x, y, mu, args.cutoff)
                checked += 1
                erow = (exact - target, n, g, x, y, exact, target)
                mrow = (lower - target, n, g, x, y, lower, target)
                if exact_best is None or erow < exact_best:
                    exact_best = erow
                if mobius_best is None or mrow < mobius_best:
                    mobius_best = mrow
                if exact < target:
                    exact_bad += 1
                if lower < target:
                    mobius_bad.append(mrow)

    mobius_bad.sort()
    print(f"checked={checked}")
    print(f"exact_bad={exact_bad}")
    print(f"exact_best={exact_best}")
    print(f"mobius_bad={len(mobius_bad)}")
    print(f"mobius_best={mobius_best}")
    for row in mobius_bad[: args.max_records]:
        print("MOBIUS_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
