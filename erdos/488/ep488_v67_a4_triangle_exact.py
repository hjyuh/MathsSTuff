#!/usr/bin/env python3
"""EP-488 v67 exact checks for the A4 triangle motif {12,15,20}.

Every realization of the normalized pure triangle has

    Z_s = {12s, 15s, 20s},
    20s < q < 24s,
    q does not divide 60s,
    60s <= n < 3q.

This script exhausts those parameters up to a scale bound and finite-certifies
every (s,q,n) case for all m > n. It also records the exact extremal rows.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, lcm
import argparse
import json

from ep488_v64_a4_pure_cycle_finite_cert import (
    N_coefficients,
    finite_certificate,
    host_H,
)


def triangle_cases(s: int):
    cycle = (12 * s, 15 * s, 20 * s)
    for q in range(20 * s + 1, 24 * s):
        if (60 * s) % q == 0:
            continue
        n_lo = max(60 * s, ceil(Fraction(5 * q, 2)))
        n_hi = 3 * q - 1
        for n in range(n_lo, n_hi + 1):
            yield cycle, q, n


def eta_summary(cycle: tuple[int, ...], q: int, n: int) -> dict[str, object]:
    coeff = N_coefficients(cycle)
    delta = sum(
        c * (Fraction(1, d) - Fraction(1, lcm(d, q)))
        for d, c in coeff.items()
    )
    E = 2 * sum(abs(c) for c in coeff.values())
    H_n = host_H(cycle, q, n)
    B = Fraction(2 * H_n, n)
    eta = B - delta
    out: dict[str, object] = {
        "H_n": H_n,
        "B": str(B),
        "delta": str(delta),
        "delta_over_B": str(delta / B) if B else None,
        "eta": str(eta),
        "eta_over_B": str(eta / B) if B else None,
        "E": E,
        "terms": len(coeff),
        "status": "eta_nonpositive" if eta <= 0 else "eta_positive",
    }
    if eta > 0:
        out["cutoff"] = E.numerator * eta.denominator // (E.denominator * eta.numerator)
    return out


def run(max_s: int, keep_top: int, exact_top: int) -> dict[str, object]:
    total = 0
    eta_nonpositive = []
    min_eta_rows = []
    min_B_rows = []
    max_cutoff_rows = []
    h_counts: dict[str, int] = {}
    max_cutoff = 0
    for s in range(1, max_s + 1):
        for cycle, q, n in triangle_cases(s):
            total += 1
            summary = eta_summary(cycle, q, n)
            row = {
                "s": s,
                "q": q,
                "n": n,
                "cycle": list(cycle),
                "summary": summary,
            }
            h_counts[str(summary["H_n"])] = h_counts.get(str(summary["H_n"]), 0) + 1
            if summary["status"] == "eta_nonpositive":
                eta_nonpositive.append(row)
                continue
            max_cutoff = max(max_cutoff, int(summary["cutoff"]))
            min_eta_rows.append(row)
            min_B_rows.append(row)
            max_cutoff_rows.append(row)

    min_eta_rows.sort(
        key=lambda r: Fraction(r["summary"]["eta"]) / Fraction(r["summary"]["B"])
    )
    min_B_rows.sort(key=lambda r: Fraction(r["summary"]["B"]))
    max_cutoff_rows.sort(key=lambda r: int(r["summary"]["cutoff"]), reverse=True)

    exact_candidates = []
    seen = set()
    for source in (min_eta_rows[:exact_top], min_B_rows[:exact_top], max_cutoff_rows[:exact_top]):
        for row in source:
            key = (row["s"], row["q"], row["n"])
            if key not in seen:
                seen.add(key)
                exact_candidates.append(row)

    exact_checked = []
    failures = []
    for row in exact_candidates:
        cert = finite_certificate(tuple(row["cycle"]), int(row["q"]), int(row["n"]))
        exact = dict(row)
        exact["certificate"] = cert
        exact_checked.append(exact)
        if cert["status"] != "certified":
            failures.append(exact)

    exact_checked.sort(
        key=lambda r: Fraction(r["certificate"]["best_over_B"]),
        reverse=True,
    )
    return {
        "max_s": max_s,
        "total_cases": total,
        "H_n_counts": h_counts,
        "eta_nonpositive_count": len(eta_nonpositive),
        "failure_count": len(failures),
        "max_cutoff": max_cutoff,
        "exact_checked_count": len(exact_checked),
        "top_by_best_over_B": exact_checked[:keep_top],
        "min_eta_over_B": min_eta_rows[:keep_top],
        "min_B": min_B_rows[:keep_top],
        "max_cutoff_rows": max_cutoff_rows[:keep_top],
        "eta_nonpositive": eta_nonpositive[:keep_top],
        "failures": failures[:keep_top],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=200)
    parser.add_argument("--keep-top", type=int, default=40)
    parser.add_argument("--exact-top", type=int, default=80)
    parser.add_argument("--json-out", default="ep488_v67_a4_triangle_exact.json")
    args = parser.parse_args()

    result = run(args.max_s, args.keep_top, args.exact_top)
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"max_s={result['max_s']} total_cases={result['total_cases']} "
        f"H_n_counts={result['H_n_counts']} eta_nonpositive={result['eta_nonpositive_count']} "
        f"exact_checked={result['exact_checked_count']} failures={result['failure_count']} "
        f"max_cutoff={result['max_cutoff']}"
    )
    print("top_by_best_over_B:")
    for row in result["top_by_best_over_B"][:10]:
        cert = row["certificate"]
        print(
            f"best_over_B={cert['best_over_B']} s={row['s']} q={row['q']} n={row['n']} "
            f"H_n={row['summary']['H_n']} best={cert['best']} eta/B={Fraction(cert['eta'])/Fraction(cert['B'])}"
        )
    print("min_eta_over_B:")
    for row in result["min_eta_over_B"][:10]:
        summary = row["summary"]
        print(
            f"eta/B={summary['eta_over_B']} s={row['s']} "
            f"q={row['q']} n={row['n']} H_n={summary['H_n']} cutoff={summary.get('cutoff')}"
        )
    return 1 if result["eta_nonpositive_count"] or result["failure_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
