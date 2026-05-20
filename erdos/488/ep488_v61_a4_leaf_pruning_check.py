#!/usr/bin/env python3
"""EP-488 v61 A4 leaf-pruning checks.

Supports the A4 leaf-pruning lemma:

For a leaf vertex a attached to b in a top-window unicyclic host, the host
contribution c_x(a)-c_x(lcm(a,b)) has nonnegative two-point margin. Therefore
leaf attachments can be pruned from A4; it is enough to prove the A4
host-margin inequality for the cycle core.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm
import argparse
import json


def c_x(d: int, x: int, q: int) -> int:
    return x // d - x // lcm(d, q)


def leaf_piece(q: int, a: int, L: int, x: int) -> int:
    return c_x(a, x, q) - c_x(L, x, q)


def leaf_margin(q: int, n: int, a: int, b: int, m: int) -> tuple[int, int, int, int]:
    L = lcm(a, b)
    Pn = leaf_piece(q, a, L, n)
    Pm = leaf_piece(q, a, L, m)
    return 2 * m * Pn - n * Pm, Pn, Pm, L


def event_points(q: int, n: int, a: int, b: int, upper: int) -> list[int]:
    L = lcm(a, b)
    steps = {a, L, lcm(a, q), lcm(L, q)}
    events = {n + 1}
    for s in steps:
        m = ((n + s) // s) * s
        while m <= upper:
            events.add(m)
            m += s
    return sorted(events)


def multiplier_count(k: int, r: int, h: int) -> int:
    return k - k // r - k // h + k // lcm(r, h)


def max_multiplier_ratio(f: int, r: int, h: int) -> tuple[Fraction, int, int]:
    """Return max_{k>=f} A(k)/k for h in {3,4,5}.

    The sequence is periodic-affine. Checking 100 periods is far beyond the
    exact maximum for these small periods; this is a regression guard, not the
    human proof of the table.
    """
    p = lcm(r, h)
    best = (Fraction(0, 1), f, 0)
    for k in range(f, 100 * p + 1):
        A = multiplier_count(k, r, h)
        value = Fraction(A, k)
        if value > best[0]:
            best = (value, k, A)
    return best


def max_nonmultiple_r_ratio(f: int, r: int) -> tuple[Fraction, int, int]:
    """Return max_{k>=f} (k-floor(k/r))/k for the h>=6 upper bound."""
    best = (Fraction(0, 1), f, 0)
    for k in range(f, 100 * r + 1):
        A = k - k // r
        value = Fraction(A, k)
        if value > best[0]:
            best = (value, k, A)
    return best


def finite_multiplier_table() -> dict[str, object]:
    rows = []
    failures = []
    impossible_exception = (2, 4, 3)
    for r in range(2, 6):
        for f in range(r, 6):
            # h = 3,4,5 exact cases.
            for h in (3, 4, 5):
                Af = multiplier_count(f, r, h)
                bound = Fraction(2 * Af, f + 1)
                best = max_multiplier_ratio(f, r, h)
                ok = best[0] <= bound
                exceptional = (r, f, h) == impossible_exception
                row = {
                    "r": r,
                    "f": f,
                    "h": h,
                    "A_f": Af,
                    "bound": str(bound),
                    "best_ratio": str(best[0]),
                    "best_k": best[1],
                    "best_A": best[2],
                    "ok": ok,
                    "top_window_exception": exceptional,
                }
                rows.append(row)
                if not ok and not exceptional:
                    failures.append(row)

            # h >= 6: no h-multiple occurs at n because f <= 5; use the
            # stronger upper bound that ignores h exclusions for all later k.
            Af = f - f // r
            bound = Fraction(2 * Af, f + 1)
            best = max_nonmultiple_r_ratio(f, r)
            ok = best[0] <= bound
            row = {
                "r": r,
                "f": f,
                "h": ">=6",
                "A_f": Af,
                "bound": str(bound),
                "best_ratio_upper": str(best[0]),
                "best_k": best[1],
                "best_A_upper": best[2],
                "ok": ok,
                "top_window_exception": False,
            }
            rows.append(row)
            if not ok:
                failures.append(row)
    return {
        "rows": rows,
        "failures": failures,
        "impossible_exception": {
            "r": 2,
            "f": 4,
            "h": 3,
            "reason": "h=3 forces q=3g and a=2g; r=2 gives L=4g. If lcm(a,b)=L then b divides 4g. With 3g/2<b<3g, b is either 2g=a or >3g, so no distinct top-window b exists.",
        },
    }


def exhaustive_edge_event_check(q_max: int, upper_factor: int = 8) -> dict[str, object]:
    checked = 0
    failures = []
    worst = None
    for q in range(7, q_max + 1):
        vertices = range(q // 2 + 1, q)
        for n in range((5 * q + 1) // 2, 3 * q):
            upper = upper_factor * n
            for a in vertices:
                for b in vertices:
                    if a == b:
                        continue
                    L = lcm(a, b)
                    if L > n or L % q == 0:
                        continue
                    for m in event_points(q, n, a, b, upper):
                        margin, Pn, Pm, L = leaf_margin(q, n, a, b, m)
                        checked += 1
                        item = {
                            "margin": margin,
                            "q": q,
                            "n": n,
                            "a": a,
                            "b": b,
                            "m": m,
                            "P_n": Pn,
                            "P_m": Pm,
                            "L": L,
                        }
                        if worst is None or margin < worst["margin"]:
                            worst = item
                        if margin < 0:
                            failures.append(item)
                            return {"q_max": q_max, "checked": checked, "failures": failures, "worst": worst}
    return {"q_max": q_max, "checked": checked, "failures": failures, "worst": worst}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=180)
    parser.add_argument("--json-out", default="ep488_v61_a4_leaf_pruning_check.json")
    args = parser.parse_args()

    table = finite_multiplier_table()
    edge_check = exhaustive_edge_event_check(args.q_max)
    result = {
        "finite_multiplier_table": table,
        "edge_event_check": edge_check,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"finite_table_failures={len(table['failures'])} "
        f"edge_q_max={edge_check['q_max']} edge_checked={edge_check['checked']} "
        f"edge_failures={len(edge_check['failures'])} worst={edge_check['worst']}"
    )
    return 1 if table["failures"] or edge_check["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
