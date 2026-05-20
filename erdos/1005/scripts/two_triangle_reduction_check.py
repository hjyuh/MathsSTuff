#!/usr/bin/env python3
"""Check finite arithmetic reductions for the two-triangle slack lemma."""

from __future__ import annotations

import argparse
from typing import Optional, Sequence


def arithmetic_tables(n: int) -> tuple[list[int], list[int], list[int], list[float]]:
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:
            for k in range(p, n + 1, p):
                phi[k] -= phi[k] // p

    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for k in range(d, n + 1, d):
            tau[k] += 1

    phi_sum = [0] * (n + 1)
    tau_sum = [0] * (n + 1)
    fprefix = [0.0] * (n + 1)
    hfun = [0.0] * (n + 1)
    for k in range(1, n + 1):
        phi_sum[k] = phi_sum[k - 1] + phi[k]
        tau_sum[k] = tau_sum[k - 1] + tau[k]
        fprefix[k] = fprefix[k - 1] + phi[k] / k
        hfun[k] = fprefix[k] - phi_sum[k] / (k + 1)
    return phi_sum, tau, tau_sum, hfun


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100000)
    parser.add_argument("--x-box", type=int, default=168)
    parser.add_argument("--h-box", type=int, default=7800)
    args = parser.parse_args(argv)

    phi_sum, tau, tau_sum, hfun = arithmetic_tables(args.limit)

    bad_phi = []
    for x in range(13, min(args.limit, 1000) + 1):
        if phi_sum[x] / x - (x + 1) / 4 < x / 50:
            bad_phi.append(x)

    bad_h = []
    for h in range(4, min(args.limit, args.h_box) + 1):
        for r in range(1, h + 1):
            if hfun[r - 1] + hfun[h - r] - h / 4 < h / 24 - 1e-12:
                bad_h.append((h, r))
                break

    outside_fail = []
    for x in range(13, 1000):
        for h in range(4, args.limit):
            vertical = h * x / 50 >= 2 * tau_sum[x] + h / 4 + 4
            horizontal = x * h / 24 >= tau_sum[h - 1] + h / 2 + 3
            if not (vertical or horizontal):
                if x > args.x_box or h > args.h_box:
                    outside_fail.append((x, h))
                    if len(outside_fail) >= 20:
                        break
        if len(outside_fail) >= 20:
            break

    print(f"bad_phi={len(bad_phi)}")
    if bad_phi:
        print(f"bad_phi_first={bad_phi[:20]}")
    print(f"bad_h={len(bad_h)}")
    if bad_h:
        print(f"bad_h_first={bad_h[:20]}")
    print(f"outside_fail={len(outside_fail)}")
    if outside_fail:
        print(f"outside_fail_first={outside_fail[:20]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
