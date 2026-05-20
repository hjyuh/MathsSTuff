#!/usr/bin/env python3
"""EP-488 v69 finite tables for the A4 pentagon {8,9,10,12,15}."""

from __future__ import annotations

from fractions import Fraction


VERTICES = (8, 10, 15, 9, 12)
EDGES = (40, 30, 45, 36, 24)
L_CYC = 360
PERIOD = 720
K_MIN = 45
TARGET = Fraction(149, 360)


def upper_A(k: int) -> int:
    return (
        sum(k // p for p in VERTICES)
        - sum(k // e for e in EDGES)
        + sum(k // (2 * e) for e in EDGES)
        + k // L_CYC
    )


def vertex_correction_table() -> list[dict[str, object]]:
    rows = []
    for p in sorted(VERTICES):
        for h in range(2, 48 // p + 1):
            hp = h * p
            # If q-exclusion occurred, r = ps/gcd(ps,q) would be an integer
            # satisfying hp/16 < r < hp/15.
            possible_r = [
                r
                for r in range(1, hp + 1)
                if Fraction(hp, 16) < r < Fraction(hp, 15)
            ]
            rows.append(
                {
                    "p": p,
                    "h": h,
                    "hp": hp,
                    "r_interval": f"({hp}/16,{hp}/15)",
                    "possible_r": possible_r,
                }
            )
    return rows


def main() -> int:
    correction_rows = vertex_correction_table()
    correction_failures = [r for r in correction_rows if r["possible_r"]]
    worst = None
    failures = []
    for k in range(K_MIN, K_MIN + PERIOD):
        A = upper_A(k)
        ratio = Fraction(A, k)
        row = {"k": k, "A": A, "ratio": ratio}
        if worst is None or ratio > worst["ratio"]:
            worst = row
        if ratio > TARGET:
            failures.append(row)

    print(f"vertex_correction_rows={len(correction_rows)} failures={len(correction_failures)}")
    print(f"period_range={K_MIN}..{K_MIN + PERIOD - 1}")
    print(f"worst={worst}")
    print(f"target={TARGET} finite_failures={len(failures)}")
    print(f"target_lt_5_8={TARGET < Fraction(5, 8)}")
    if correction_failures:
        print(f"correction_failures={correction_failures}")
    if failures:
        print(f"finite_failures={failures[:10]}")
    return 1 if correction_failures or failures or not (TARGET < Fraction(5, 8)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
