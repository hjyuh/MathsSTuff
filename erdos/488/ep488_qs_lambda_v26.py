"""
EP-488 (Open Field v26): resolve the Q_s(lambda) discrepancy.

This script computes the fully lambda-dependent recursive coefficient Q_s(lambda)
defined by:

  c_s(lambda) := max(0, (s+1) * (L_s(floor((s+1)*lambda)) - 2*lambda)),

  Q_s(lambda) := c_s(lambda) + sum_{(s->t,h) active at lambda} (h/2) * Q_t(lambda),

where:
  - L_s(t) counts integers 1 <= x <= t coprime to all primes <= s
    (equivalently: numbers whose smallest prime factor is > s, plus 1),
  - (s->t,h) is a geometric edge with odd h satisfying
        2s/(t+1) < h < 2(s+1)/t,
  - "active at lambda" means c_s(lambda) > 0 AND c_t(lambda) > 0.

Then it computes the v26 target sum

  g_N(lambda) = sum_{active s <= N} Q_s(lambda) * (2s+1) / (2*s^2*(s+1)^2).

We default to N=200 and the 7 test lambdas from the v26 prompt.

Optional: also compute the universal P_s (lambda-independent) recurrence to compare
Q_s(lambda)/s^2 vs P_s/s^2.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction
from typing import Iterable


def parse_fraction(text: str) -> Fraction:
    text = text.strip()
    if "/" in text:
        a, b = text.split("/", 1)
        return Fraction(int(a.strip()), int(b.strip()))
    if "." in text:
        return Fraction(text)
    return Fraction(int(text), 1)


def spf_sieve(n: int) -> list[int]:
    """
    Smallest-prime-factor sieve for 1..n.
    spf[1] = 1; for primes p, spf[p] = p.
    """
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if spf[p] == p:  # prime
            step = p
            start = p * p
            for m in range(start, n + 1, step):
                if spf[m] == m:
                    spf[m] = p
    return spf


def build_L_prefix(max_s: int, max_t: int) -> list[list[int]]:
    """
    For each s <= max_s, build prefix counts L_s_prefix[t] =
      #{1 <= x <= t : x is not divisible by any prime <= s}.

    This equals #{1 <= x <= t : spf[x] > s} with the convention spf[1]=1,
    so x=1 is included for all s.
    """
    spf = spf_sieve(max_t)
    L_prefix: list[list[int]] = [[0] * (max_t + 1) for _ in range(max_s + 1)]
    for s in range(max_s + 1):
        running = 0
        row = L_prefix[s]
        for x in range(1, max_t + 1):
            if x == 1 or spf[x] > s:
                running += 1
            row[x] = running
    return L_prefix


def coefficient_c_pos(s: int, lam: Fraction, L_prefix: list[list[int]]) -> Fraction:
    t = int((s + 1) * lam)  # floor
    l_val = L_prefix[s][t]
    coeff = (s + 1) * (Fraction(l_val, 1) - 2 * lam)
    return coeff if coeff > 0 else Fraction(0, 1)


def odd_integers_in_open_interval(left: Fraction, right: Fraction) -> Iterable[int]:
    h = math.floor(left) + 1
    if h % 2 == 0:
        h += 1
    while Fraction(h, 1) < right:
        yield h
        h += 2


def geometric_edges(max_s: int) -> dict[int, list[tuple[int, int]]]:
    """
    All geometric edges (s->t,h) with t < s, t != 5, s != 5, h odd >= 3.
    """
    edges: dict[int, list[tuple[int, int]]] = {s: [] for s in range(4, max_s + 1) if s != 5}
    for s in range(4, max_s + 1):
        if s == 5:
            continue
        out: list[tuple[int, int]] = []
        for t in range(4, s):
            if t == 5:
                continue
            left = Fraction(2 * s, t + 1)
            right = Fraction(2 * (s + 1), t)
            if left >= right:
                continue
            for h in odd_integers_in_open_interval(left, right):
                if h >= 3:
                    out.append((t, h))
        edges[s] = out
    return edges


def compute_Q(
    *,
    lam: Fraction,
    max_s: int,
    L_prefix: list[list[int]],
    edges: dict[int, list[tuple[int, int]]],
) -> tuple[dict[int, Fraction], dict[int, Fraction]]:
    """
    Return (Q, c_pos) for all s <= max_s (excluding s=5).
    """
    c_pos: dict[int, Fraction] = {}
    active: dict[int, bool] = {}
    for s in range(4, max_s + 1):
        if s == 5:
            continue
        c = coefficient_c_pos(s, lam, L_prefix)
        c_pos[s] = c
        active[s] = c > 0

    Q: dict[int, Fraction] = {}
    for s in range(4, max_s + 1):
        if s == 5:
            continue
        if not active[s]:
            Q[s] = Fraction(0, 1)
            continue
        total = c_pos[s]
        for t, h in edges[s]:
            if active.get(t, False):
                total += Fraction(h, 2) * Q[t]
        Q[s] = total

    return Q, c_pos


def g_partial_sums(
    *,
    Q: dict[int, Fraction],
    c_pos: dict[int, Fraction],
    N_values: list[int],
) -> dict[int, Fraction]:
    """
    Compute g_N(lam) for N in N_values:
      sum_{active s <= N} Q_s * (2s+1)/(2*s^2*(s+1)^2)
    where "active" means c_pos[s] > 0.
    """
    out: dict[int, Fraction] = {}
    N_values_sorted = sorted(N_values)
    running = Fraction(0, 1)
    idx = 0
    current_N = N_values_sorted[idx]

    max_N = max(N_values_sorted)
    for s in range(4, max_N + 1):
        if s == 5:
            continue
        if c_pos.get(s, Fraction(0, 1)) > 0:
            weight = Fraction(2 * s + 1, 2 * s * s * (s + 1) * (s + 1))
            running += Q[s] * weight
        while s >= current_N:
            out[current_N] = running
            idx += 1
            if idx >= len(N_values_sorted):
                return out
            current_N = N_values_sorted[idx]
    return out


def summarize_for_lambda(
    *,
    lam: Fraction,
    max_s: int,
    L_prefix: list[list[int]],
    edges: dict[int, list[tuple[int, int]]],
    N_values: list[int],
) -> dict[str, object]:
    Q, c_pos = compute_Q(lam=lam, max_s=max_s, L_prefix=L_prefix, edges=edges)

    active_bands = [s for s in range(4, max_s + 1) if s != 5 and c_pos[s] > 0]
    active_count = len(active_bands)

    gN = g_partial_sums(Q=Q, c_pos=c_pos, N_values=N_values)

    # First crossing (if any) of g_s(lambda) >= lambda, within the computed range.
    running = Fraction(0, 1)
    cross_s = None
    cross_g = None
    for s in range(4, max_s + 1):
        if s == 5:
            continue
        if c_pos.get(s, Fraction(0, 1)) > 0:
            weight = Fraction(2 * s + 1, 2 * s * s * (s + 1) * (s + 1))
            running += Q[s] * weight
        if running >= lam:
            cross_s = s
            cross_g = running
            break

    max_ratio = 0.0
    arg_max = None
    for s in active_bands:
        ratio = float(Q[s]) / (s * s)
        if ratio > max_ratio:
            max_ratio = ratio
            arg_max = s

    return {
        "lambda": lam,
        "active_count": active_count,
        "max_Q_over_s2": max_ratio,
        "argmax_Q_over_s2": arg_max,
        "gN": gN,
        "g_max": gN[max(N_values)],
        "cross_s": cross_s,
        "cross_g": cross_g,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=200)
    parser.add_argument(
        "--lambdas",
        default="29/20,7/5,3/2,13/9,2,5/2,3",
        help="Comma-separated list of lambdas (Fractions).",
    )
    parser.add_argument(
        "--partials",
        default="25,50,100,150,200",
        help="Comma-separated partial-sum cutoffs N.",
    )
    args = parser.parse_args()

    max_s = args.max_s
    lambdas = [parse_fraction(x) for x in args.lambdas.split(",") if x.strip()]
    N_values = [int(x) for x in args.partials.split(",") if x.strip()]

    max_lambda = max(lambdas)
    max_t = int((max_s + 1) * max_lambda)

    print(f"max_s={max_s}, max_lambda={max_lambda}, max_t={max_t}")
    print("Building L_s(t) prefix table via spf sieve...")
    L_prefix = build_L_prefix(max_s=max_s, max_t=max_t)
    print("Building geometric edges...")
    edges = geometric_edges(max_s=max_s)

    print()
    print("Lambda summary (Q_s recursion):")
    print("lambda   active  g(N=max)          g<lambda?  cross<=N?  max(Q/s^2)  at s")
    for lam in lambdas:
        summary = summarize_for_lambda(
            lam=lam,
            max_s=max_s,
            L_prefix=L_prefix,
            edges=edges,
            N_values=N_values,
        )
        g_val: Fraction = summary["g_max"]  # type: ignore[assignment]
        ok = "YES" if g_val < lam else "NO"
        cross = summary["cross_s"]
        cross_str = "-" if cross is None else str(cross)
        print(
            f"{lam!s:>6s}  {summary['active_count']:>6d}  {float(g_val):>14.9f}  "
            f"{ok:>8s}  {cross_str:>8s}  {summary['max_Q_over_s2']:>11.6f}  {summary['argmax_Q_over_s2']}"
        )

    # Tail diagnostics at the hardest point (default first lambda)
    lam0 = lambdas[0]
    print()
    print(f"Partial sums g_N(lambda) for lambda={lam0}:")
    summary0 = summarize_for_lambda(
        lam=lam0,
        max_s=max_s,
        L_prefix=L_prefix,
        edges=edges,
        N_values=N_values,
    )
    gN0: dict[int, Fraction] = summary0["gN"]  # type: ignore[assignment]
    for N in sorted(gN0):
        print(f"  N={N:3d}: g_N={float(gN0[N]):.9f} (exact {gN0[N]})")


if __name__ == "__main__":
    main()
