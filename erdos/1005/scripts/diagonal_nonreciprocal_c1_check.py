#!/usr/bin/env python3
"""Exact and lower-bound checks for the c=1 non-reciprocal diagonal strip."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence


D = [1, 2, 2, 4]


def predicted_value(n: int) -> int:
    return n // 4 + D[n % 4]


def totients_and_tau(n: int) -> tuple[list[int], list[int]]:
    phi = list(range(n + 1))
    tau = [0] * (n + 1)
    for p in range(2, n + 1):
        if phi[p] == p:
            for multiple in range(p, n + 1, p):
                phi[multiple] -= phi[multiple] // p
    for d in range(1, n + 1):
        for multiple in range(d, n + 1, d):
            tau[multiple] += 1
    return phi, tau


def base_count(a: int, h: int) -> int:
    total = 0
    r = h + 2
    for j in range(1, h + 2):
        lo = (a * j) // r + 1
        total += sum(1 for p in range(lo, a + 1) if gcd(p, j) == 1)
    return total


def slack_count(a: int, h: int, sigma: int) -> int:
    total = 0
    r = h + 2
    u_max = sigma // h + 1
    for u in range(1, u_max + 1):
        p = a + u
        lo = p // (a + 1) + 1
        hi = (r * p - 1) // a
        if hi > sigma - h * u + r:
            hi = sigma - h * u + r
        if hi >= lo:
            total += sum(1 for j in range(lo, hi + 1) if gcd(p, j) == 1)
    return total


def core_lower(a: int, h: int, sigma: int) -> int:
    total = 0
    u_max = min(a, sigma // h)
    for u in range(1, u_max + 1):
        p = a + u
        total += sum(1 for j in range(2, h + 3) if gcd(p, j) == 1)
    return total


def shifted_block_threshold(a: int, h: int, k: int) -> int:
    """Slack needed to include the full shifted block k."""
    u_hi = (k + 1) * (a + 1)
    j_hi = (k + 1) * (h + 2)
    return h * u_hi + j_hi - (h + 2)


def shifted_block_count(a: int, h: int, k: int) -> int:
    total = 0
    u_lo = k * (a + 1) + 1
    u_hi = (k + 1) * (a + 1)
    j_lo = k + 2
    j_hi = (k + 1) * (h + 2)
    for u in range(u_lo, u_hi + 1):
        p = a + u
        total += sum(1 for j in range(j_lo, j_hi + 1) if gcd(p, j) == 1)
    return total


def shifted_block_discrepancy_lower(
    a: int, h: int, k: int, phi: list[int], tau: list[int]
) -> float:
    j_lo = k + 2
    j_hi = (k + 1) * (h + 2)
    width = a + 1
    return sum(width * phi[j] / j - tau[j] for j in range(j_lo, j_hi + 1))


def shifted_blocks_lower(a: int, h: int, sigma: int) -> int:
    total = 0
    k = 0
    while shifted_block_threshold(a, h, k) <= sigma:
        total += shifted_block_count(a, h, k)
        k += 1
    return total


def shifted_block_prefix(a: int, h: int, sigma_max: int) -> list[tuple[int, int]]:
    """Return (threshold, cumulative_count) for full shifted blocks."""
    blocks: list[tuple[int, int]] = []
    total = 0
    k = 0
    while True:
        threshold = shifted_block_threshold(a, h, k)
        if threshold > sigma_max:
            break
        total += shifted_block_count(a, h, k)
        blocks.append((threshold, total))
        k += 1
    return blocks


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--sigma-max", type=int, default=0)
    parser.add_argument("--shifted-only", action="store_true")
    parser.add_argument("--large-slack-only", action="store_true")
    parser.add_argument("--discrepancy", action="store_true")
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    base_best: tuple[int, int, int, int, int, int] | None = None
    base_bad: list[tuple[int, int, int, int, int, int]] = []
    slack_best: tuple[int, int, int, int, int, int, int] | None = None
    slack_bad: list[tuple[int, int, int, int, int, int, int]] = []
    core_best: tuple[int, int, int, int, int, int, int] | None = None
    shifted_best: tuple[int, int, int, int, int, int, int] | None = None
    shifted_bad: list[tuple[int, int, int, int, int, int, int]] = []
    combined_best: tuple[int, int, int, int, int, int, int] | None = None
    combined_bad: list[tuple[int, int, int, int, int, int, int]] = []
    discrepancy_best: tuple[float, int, int, int, int, int, float] | None = None
    discrepancy_bad: list[tuple[float, int, int, int, int, int, float]] = []

    phi: list[int] = []
    tau: list[int] = []
    if args.discrepancy:
        phi, tau = totients_and_tau(args.sigma_max + args.q_max + 10)

    checked_base = 0
    checked_slack = 0
    for h in range(1, args.q_max + 1):
        r = h + 2
        for a in range(r + 1, args.q_max // h + 2):
            q = h * a + r
            if q > args.q_max or q < 92:
                continue
            if gcd(a, r) != 1:
                continue
            c0 = base_count(a, h)
            target = predicted_value(q)
            row = (c0 - target, q, h, a, c0, target)
            checked_base += 1
            if base_best is None or row < base_best:
                base_best = row
            if row[0] < 0:
                base_bad.append(row)

            block_prefix = shifted_block_prefix(a, h, args.sigma_max)
            discrepancy_prefix: list[tuple[int, float]] = []
            if args.discrepancy:
                running = 0.0
                for k, (threshold, _) in enumerate(block_prefix):
                    running += shifted_block_discrepancy_lower(a, h, k, phi, tau)
                    discrepancy_prefix.append((threshold, running))
            block_index = -1
            shifted_value = 0
            discrepancy_value = 0.0
            sigma_start = h * (a + 2) if args.large_slack_only else 1
            for sigma in range(sigma_start, args.sigma_max + 1):
                n = q + sigma
                target = predicted_value(n)
                if not args.shifted_only:
                    exact = c0 + slack_count(a, h, sigma)
                    srow = (exact - target, n, sigma, q, h, a, exact)
                    checked_slack += 1
                    if slack_best is None or srow < slack_best:
                        slack_best = srow
                    if srow[0] < 0:
                        slack_bad.append(srow)

                core = None
                if not args.shifted_only:
                    core = c0 + core_lower(a, h, sigma)
                    crow = (core - target, n, sigma, q, h, a, core)
                    if core_best is None or crow < core_best:
                        core_best = crow

                while (
                    block_index + 1 < len(block_prefix)
                    and block_prefix[block_index + 1][0] <= sigma
                ):
                    block_index += 1
                    shifted_value = block_prefix[block_index][1]
                    if args.discrepancy:
                        discrepancy_value = discrepancy_prefix[block_index][1]
                shifted = c0 + shifted_value
                shrow = (shifted - target, n, sigma, q, h, a, shifted)
                if shifted_best is None or shrow < shifted_best:
                    shifted_best = shrow
                if shrow[0] < 0:
                    shifted_bad.append(shrow)

                if sigma < h * (a + 2):
                    if core is None:
                        combined = c0 + core_lower(a, h, sigma)
                    else:
                        combined = core
                else:
                    combined = shifted
                combrow = (combined - target, n, sigma, q, h, a, combined)
                if combined_best is None or combrow < combined_best:
                    combined_best = combrow
                if combrow[0] < 0:
                    combined_bad.append(combrow)
                if args.discrepancy:
                    dlower = c0 + discrepancy_value
                    drow = (dlower - target, n, sigma, q, h, a, dlower)
                    if discrepancy_best is None or drow < discrepancy_best:
                        discrepancy_best = drow
                    if drow[0] < 0:
                        discrepancy_bad.append(drow)

    print(f"base_checked={checked_base}")
    print(f"base_bad={len(base_bad)}")
    print(f"base_best={base_best}")
    for row in base_bad[: args.max_records]:
        print("BASE_BAD " + ",".join(str(item) for item in row))

    if args.sigma_max:
        if not args.shifted_only:
            print(f"slack_checked={checked_slack}")
            print(f"slack_bad={len(slack_bad)}")
            print(f"slack_best={slack_best}")
        if not args.shifted_only:
            print(f"core_best={core_best}")
        print(f"shifted_bad={len(shifted_bad)}")
        print(f"shifted_best={shifted_best}")
        print(f"combined_bad={len(combined_bad)}")
        print(f"combined_best={combined_best}")
        if args.discrepancy:
            print(f"discrepancy_bad={len(discrepancy_bad)}")
            print(f"discrepancy_best={discrepancy_best}")
        if not args.shifted_only:
            for row in slack_bad[: args.max_records]:
                print("SLACK_BAD " + ",".join(str(item) for item in row))
        for row in shifted_bad[: args.max_records]:
            print("SHIFTED_BAD " + ",".join(str(item) for item in row))
        for row in combined_bad[: args.max_records]:
            print("COMBINED_BAD " + ",".join(str(item) for item in row))
        for row in discrepancy_bad[: args.max_records]:
            print("DISCREPANCY_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
