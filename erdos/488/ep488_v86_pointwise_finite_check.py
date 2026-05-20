#!/usr/bin/env python3
"""Exact finite certificate for the v86 pointwise extension theorem.

For each allowed pair (R,D), prove for all M>R:

    A_D(M)/M <= 2 A_D(R)/(R+1),

where A_D(M) counts integers 1<=k<=M not divisible by any d in D.

The proof is periodic modulo L=lcm(D).  For M=kL+r,

    A(M) = k A(L) + A(r).

Since A(L)/L is at most the target constant in every allowed case, it is
enough to check the least admissible k for each residue r.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import lcm
from pathlib import Path


ALLOWED = {
    2: [(), (2,)],
    3: [(), (2,), (3,), (2, 3)],
    4: [(), (3,), (4,), (3, 4)],
    5: [(), (3,), (4,), (5,), (3, 4), (3, 5), (4, 5), (3, 4, 5)],
}


def A(D: tuple[int, ...], M: int) -> int:
    return sum(1 for k in range(1, M + 1) if all(k % d for d in D))


def period(D: tuple[int, ...]) -> int:
    out = 1
    for d in D:
        out = lcm(out, d)
    return out


def certify_case(R: int, D: tuple[int, ...]) -> dict[str, object]:
    L = period(D)
    AR = A(D, R)
    target = Fraction(2 * AR, R + 1)
    period_density = Fraction(A(D, L), L)
    rows = []
    worst = (Fraction(-10, 1), None)
    ok = period_density <= target
    for r in range(L):
        k_min = max(0, (R - r) // L + 1)
        if r == 0:
            k_min = max(k_min, 1)
        M = k_min * L + r
        if M <= R:
            raise AssertionError((R, D, L, r, k_min, M))
        value = Fraction(A(D, M), M)
        slack = target - value
        rows.append({"residue": r, "M": M, "value": str(value), "slack": str(slack)})
        if value > worst[0]:
            worst = (value, M)
        if slack < 0:
            ok = False
    return {
        "R": R,
        "D": list(D),
        "L": L,
        "A_R": AR,
        "target": str(target),
        "period_density": str(period_density),
        "period_density_slack": str(target - period_density),
        "worst_value": str(worst[0]),
        "worst_M": worst[1],
        "worst_slack": str(target - worst[0]),
        "ok": ok,
        "residue_checks": rows,
    }


def main() -> int:
    cases = [certify_case(R, D) for R, ds in ALLOWED.items() for D in ds]
    output = {
        "case_count": len(cases),
        "all_ok": all(case["ok"] for case in cases),
        "cases": cases,
    }
    Path("ep488_v86_pointwise_finite_check.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
