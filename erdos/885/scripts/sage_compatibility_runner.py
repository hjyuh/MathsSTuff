#!/usr/bin/env sage -python
"""Sage translation of the genus-2 compatibility workflow for EP885.

Run with Sage, for example:

    sage -python scripts/sage_compatibility_runner.py --n-values ... --deltas ...

For fixed rows N_i and old columns t_j=(d_j/2)^2, this studies

    D_m: Z^2 = prod_{i != m} (W^2 + N_i - N_m).

The Jacobian of D_m is isogenous to the product of the triple elliptic factor
E_{I_m} and the quartic factor E_{1234}.  Sage can compute rank bounds for
those elliptic curves directly; this gives rank bounds for Jac(D_m) without
Magma.

The rational point search here is bounded and diagnostic.  It is not a
Chabauty/Mordell-Weil-sieve proof of completeness.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from sage.all import EllipticCurve, HyperellipticCurve, PolynomialRing, QQ, gcd


def parse_ints(spec: str | None) -> list[int]:
    if not spec:
        return []
    return [int(x.strip()) for x in spec.replace("\n", ",").split(",") if x.strip()]


def q_to_str(x) -> str:
    x = QQ(x)
    return str(x)


def sqrt_q(x):
    x = QQ(x)
    if x < 0:
        return None
    num = int(x.numerator())
    den = int(x.denominator())
    rn = math.isqrt(num)
    rd = math.isqrt(den)
    if rn * rn == num and rd * rd == den:
        return QQ(rn) / QQ(rd)
    return None


def rank_bounds(E) -> tuple[int | None, int | None, str | None]:
    try:
        lo, hi = E.rank_bounds()
        return int(lo), int(hi), None
    except Exception as err:  # Sage rank code can fail on large models.
        return None, None, str(err)


def triple_elliptic(n_values: list[int], indices: tuple[int, int, int]):
    p, q, r = indices
    a = (n_values[q] - n_values[p]) + (n_values[r] - n_values[p])
    b = (n_values[q] - n_values[p]) * (n_values[r] - n_values[p])
    return EllipticCurve(QQ, [0, a, 0, b, 0]), p


def quartic_elliptic(n_values: list[int], pivot: int = 3):
    others = [i for i in range(4) if i != pivot]
    d1, d2, d3 = [n_values[i] - n_values[pivot] for i in others]
    a = d1 * d2 * d3
    b = d1 * d2 + d1 * d3 + d2 * d3
    c = d1 + d2 + d3
    return EllipticCurve(QQ, [0, b, 0, a * c, a * a]), pivot, a


def roots_for_old_columns(n_values: list[int], deltas: list[int]) -> list[list[int]]:
    yold = []
    for d in deltas:
        t = (d // 2) ** 2
        roots = []
        for n in n_values:
            value = t + n
            root = math.isqrt(value)
            if root * root != value:
                raise ValueError(f"not a square: {t}+{n}={value}")
            roots.append(root)
        yold.append(roots)
    return yold


def rational_values(num_bound: int, den_bound: int):
    seen = set()
    for den in range(1, den_bound + 1):
        for num in range(-num_bound, num_bound + 1):
            if gcd(num, den) != 1:
                continue
            w = QQ(num) / QQ(den)
            if w in seen:
                continue
            seen.add(w)
            yield w


def lift_data(n_values: list[int], m: int, w):
    t = QQ(w) * QQ(w) - QQ(n_values[m])
    roots = []
    for n in n_values:
        root = sqrt_q(t + n)
        if root is None:
            return {
                "lifts_to_C": False,
                "t": q_to_str(t),
                "t_square": False,
                "roots": [],
            }
        roots.append(root)
    return {
        "lifts_to_C": True,
        "t": q_to_str(t),
        "t_square": sqrt_q(t) is not None,
        "roots": [q_to_str(root) for root in roots],
    }


def compatibility_report(
    n_values: list[int],
    deltas: list[int],
    num_bound: int,
    den_bound: int,
    max_samples: int,
) -> dict:
    old_t = [(d // 2) ** 2 for d in deltas]
    yold = roots_for_old_columns(n_values, deltas)
    quartic_E, _, _ = quartic_elliptic(n_values)
    q_lo, q_hi, q_err = rank_bounds(quartic_E)
    triples = {}
    for indices in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
        E, pivot = triple_elliptic(n_values, indices)
        lo, hi, err = rank_bounds(E)
        label = "".join(str(i + 1) for i in indices)
        triples[label] = {
            "indices": [i + 1 for i in indices],
            "pivot": pivot + 1,
            "rank_bounds": [lo, hi],
            "rank_error": err,
            "minimal_model": str(E.global_minimal_model()),
        }

    R = PolynomialRing(QQ, "W")
    W = R.gen()
    d_reports = []
    for m in range(4):
        indices = tuple(i for i in range(4) if i != m)
        label = "".join(str(i + 1) for i in indices)
        f = R(1)
        for i in indices:
            f *= W * W + QQ(n_values[i] - n_values[m])
        D = HyperellipticCurve(f)
        tri = triples[label]
        tri_lo, tri_hi = tri["rank_bounds"]
        jac_rank = [
            None if tri_lo is None or q_lo is None else tri_lo + q_lo,
            None if tri_hi is None or q_hi is None else tri_hi + q_hi,
        ]
        old_w_values = sorted({QQ(row[m]) for row in yold} | {-QQ(row[m]) for row in yold})
        d_point_count = 0
        d_point_samples = []
        lift_points = []
        square_t_points = []
        for w in rational_values(num_bound, den_bound):
            fval = QQ(f(w))
            zroot = sqrt_q(fval)
            if zroot is None:
                continue
            d_point_count += 1
            if len(d_point_samples) < max_samples:
                d_point_samples.append({"W": q_to_str(w), "Z_abs": q_to_str(zroot)})
            lifted = lift_data(n_values, m, w)
            if lifted["lifts_to_C"]:
                record = {
                    "W": q_to_str(w),
                    "Z_abs": q_to_str(zroot),
                    "old_W_abs": abs(w) in {abs(v) for v in old_w_values},
                    **lifted,
                }
                lift_points.append(record)
                if lifted["t_square"]:
                    square_t_points.append(record)
        d_reports.append(
            {
                "m": m + 1,
                "I": [i + 1 for i in indices],
                "f": str(f),
                "genus": int(D.genus()),
                "triple_factor": label,
                "triple_rank_bounds": tri["rank_bounds"],
                "quartic_rank_bounds": [q_lo, q_hi],
                "jacobian_rank_bounds_via_split": jac_rank,
                "old_W_values": [q_to_str(v) for v in old_w_values],
                "search_num_bound": num_bound,
                "search_den_bound": den_bound,
                "d_point_count": d_point_count,
                "d_point_samples": d_point_samples,
                "lift_point_count": len(lift_points),
                "lift_points": lift_points,
                "square_t_point_count": len(square_t_points),
                "square_t_points": square_t_points,
            }
        )

    return {
        "N_values": n_values,
        "deltas": deltas,
        "old_t": old_t,
        "yold": yold,
        "quartic_rank_bounds": [q_lo, q_hi],
        "quartic_rank_error": q_err,
        "quartic_minimal_model": str(quartic_E.global_minimal_model()),
        "triple_factors": triples,
        "compatibility_curves": d_reports,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-values", required=True)
    parser.add_argument("--deltas", required=True)
    parser.add_argument("--num-bound", type=int, default=20_000)
    parser.add_argument("--den-bound", type=int, default=1)
    parser.add_argument("--max-samples", type=int, default=30)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    payload = compatibility_report(
        parse_ints(args.n_values),
        parse_ints(args.deltas),
        args.num_bound,
        args.den_bound,
        args.max_samples,
    )
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
