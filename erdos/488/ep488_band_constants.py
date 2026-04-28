"""
Exact constrained band constants for the EP-488 frozen-layer excess model.

For a frozen layer at depth s, the worst admissible excess coefficient is

    C*(s) = max_{s < t < (s+1)^2 / 2} ((s+1)L_s(t) - 2t),

where L_s(t) counts integers 1 <= x <= t that avoid every prime <= s.

v25 correction (April 2026): the only universally justified bound on t comes
from the convexity window m <= 10n, giving

    t = floor((s+1)·lambda) <= 10·(s+1).

So the corrected universal constant is

    C*(s) = max_{s < t <= 10·(s+1)} ((s+1)L_s(t) - 2t).

This script supports both the corrected convexity bound and the historical
quadratic bound via CLI flags. It is dependency-free.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : n + 1 : step] = [False] * (((n - start) // step) + 1)
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def coprime_prefix_count(primes: list[int], t_max: int) -> list[int]:
    """
    Return prefix counts L[t] = #{1 <= x <= t : x is not divisible by any p in primes}.
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


@dataclass
class BandConstant:
    s: int
    t_max: int
    best_t: int
    best_l: int
    best_c: int
    primes: list[int]


def constrained_band_constant(s: int, *, mode: str, lam_max: int) -> BandConstant:
    primes = primes_up_to(s)
    # For the prime kernel {p <= s}, the layer is frozen: only x=1 survives in [1,s].
    frozen_prefix = coprime_prefix_count(primes, s)
    if frozen_prefix[s] != 1:
        raise ValueError(f"s={s} is not frozen by the prime kernel <= s")

    if mode == "quadratic":
        t_max = ((s + 1) * (s + 1) - 1) // 2
    elif mode == "convexity":
        t_max = lam_max * (s + 1)
    else:
        raise ValueError(f"Unknown mode: {mode!r}")

    prefix = coprime_prefix_count(primes, t_max)
    best_t = -1
    best_l = -1
    best_c = -(10**18)

    for t in range(s + 1, t_max + 1):
        l_val = prefix[t]
        c_val = (s + 1) * l_val - 2 * t
        if c_val > best_c:
            best_c = c_val
            best_t = t
            best_l = l_val

    return BandConstant(
        s=s,
        t_max=t_max,
        best_t=best_t,
        best_l=best_l,
        best_c=best_c,
        primes=primes,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=20)
    parser.add_argument(
        "--mode",
        choices=["convexity", "quadratic"],
        default="convexity",
        help="t-bound mode: convexity uses t<=lam_max·(s+1); quadratic uses t<(s+1)^2/2.",
    )
    parser.add_argument(
        "--lam-max",
        type=int,
        default=10,
        help="Max lambda for convexity mode (default: 10). Ignored for quadratic mode.",
    )
    args = parser.parse_args()

    print("s  r  t_max  C*  best_t  L(best_t)  kernel")
    for s in range(4, args.max_s + 1):
        result = constrained_band_constant(s, mode=args.mode, lam_max=args.lam_max)
        print(
            f"{result.s:2d} {len(result.primes):2d} {result.t_max:6d} "
            f"{result.best_c:4d} {result.best_t:7d} {result.best_l:10d} "
            f"{result.primes}"
        )


if __name__ == "__main__":
    main()
