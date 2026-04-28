#!/usr/bin/env python3
"""
Finite verifier for the rowwise quota bound (RQ_q) in EP-488 one-anchor families.

We check, for A = {a} U {2a+1, ..., 2a+t} with a prime and t > 2*sqrt(a),
that for every pre-peak window I_x = (x, x+4a] and every active q >= 2,

    C_q(x) <= E_{q-1}(x),

where:
    R_q(x) = qB intersect I_x,
    C_q(x) = |R_q(x) intersect union_{r<q} R_r(x)|,
    E_{q-1}(x) = |B intersect (x/(q-1), (x+4a)/q]|.

The earliest peak m* is computed exactly on [M, m6], using the separately
verified finite peak-location bound m* < m6 for k=2 wide families up to a <= 401.
"""

from __future__ import annotations

import argparse
import json
import time
from math import isqrt
from pathlib import Path


DEFAULT_PRIMES = [
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
]


def m6(a: int, t: int) -> int:
    q6 = (6 * a + 6 + (t - 2)) // (t - 1)
    return (q6 + 5) * (2 * a + 1)


def wide_t_values(a: int) -> range:
    # Wide means t > 2*sqrt(a), i.e. t >= floor(2*sqrt(a)) + 1.
    return range(isqrt(4 * a) + 1, a)


def earliest_peak_upto_m6(a: int, t: int) -> tuple[int, int, int]:
    bound = m6(a, t)
    m_min = 2 * a + t
    hits = bytearray(bound + 1)

    for n in range(a, bound + 1, a):
        hits[n] = 1
    for d in range(2 * a + 1, 2 * a + t + 1):
        for n in range(d, bound + 1, d):
            hits[n] = 1

    best_num = -1
    best_den = 1
    best_x = None
    total = 0
    for x in range(1, bound + 1):
        total += hits[x]
        if x < m_min:
            continue
        if total * best_den > best_num * x:
            best_num = total
            best_den = x
            best_x = x

    assert best_x is not None
    return best_x, best_num, best_den


def verify_family(a: int, t: int) -> dict:
    m_star, peak_num, peak_den = earliest_peak_upto_m6(a, t)
    peak_bound = m6(a, t)
    peak_bound_ok = m_star < peak_bound

    b_lo = 2 * a + 1
    b_hi = 2 * a + t
    window = 4 * a

    marks = [0] * (window + 1)
    stamp = 0

    quadruples = 0
    worst_margin = 10**9
    worst_witness = None
    failures = []

    max_x = m_star - window
    for x in range(0, max_x + 1):
        stamp += 1
        q_min = x // b_hi + 1
        q_max = (x + window) // b_lo

        for q in range(q_min, q_max + 1):
            b_min = b_lo
            y = x // q + 1
            if y > b_min:
                b_min = y

            b_max = b_hi
            z = (x + window) // q
            if z < b_max:
                b_max = z

            if b_min > b_max:
                continue

            if q >= 2:
                eq_lo = b_lo
                y = x // (q - 1) + 1
                if y > eq_lo:
                    eq_lo = y

                eq_hi = b_hi
                z = (x + window) // q
                if z < eq_hi:
                    eq_hi = z

                e_prev = 0 if eq_lo > eq_hi else (eq_hi - eq_lo + 1)
                c_q = 0
                for b in range(b_min, b_max + 1):
                    pos = q * b - x
                    if marks[pos] == stamp:
                        c_q += 1

                margin = e_prev - c_q
                quadruples += 1

                if margin < worst_margin:
                    worst_margin = margin
                    worst_witness = {
                        "x": x,
                        "q": q,
                        "E_prev": e_prev,
                        "C_q": c_q,
                        "margin": margin,
                    }

                if margin < 0:
                    failures.append(
                        {
                            "x": x,
                            "q": q,
                            "E_prev": e_prev,
                            "C_q": c_q,
                            "margin": margin,
                        }
                    )

            for b in range(b_min, b_max + 1):
                marks[q * b - x] = stamp

    return {
        "a": a,
        "t": t,
        "m_star": m_star,
        "peak_ratio_num": peak_num,
        "peak_ratio_den": peak_den,
        "m6": peak_bound,
        "peak_bound_ok": peak_bound_ok,
        "quadruples": quadruples,
        "worst_margin": worst_margin,
        "worst_witness": worst_witness,
        "failures": failures,
    }


def summarize_prime(a: int) -> dict:
    family_count = 0
    quadruples = 0
    worst_margin = 10**9
    worst_family = None
    failures = []
    peak_bound_issues = []

    for t in wide_t_values(a):
        family_count += 1
        result = verify_family(a, t)
        quadruples += result["quadruples"]

        if result["worst_margin"] < worst_margin:
            worst_margin = result["worst_margin"]
            worst_family = {
                "t": t,
                "m_star": result["m_star"],
                "m6": result["m6"],
                "quadruples": result["quadruples"],
                "witness": result["worst_witness"],
            }

        if result["failures"]:
            failures.append(
                {
                    "t": t,
                    "m_star": result["m_star"],
                    "m6": result["m6"],
                    "failures": result["failures"][:5],
                }
            )

        if not result["peak_bound_ok"]:
            peak_bound_issues.append(
                {
                    "t": t,
                    "m_star": result["m_star"],
                    "m6": result["m6"],
                }
            )

    return {
        "a": a,
        "wide_t_count": family_count,
        "quadruples": quadruples,
        "worst_margin": worst_margin,
        "worst_family": worst_family,
        "failure_count": len(failures),
        "failures": failures,
        "peak_bound_issue_count": len(peak_bound_issues),
        "peak_bound_issues": peak_bound_issues,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--primes",
        type=int,
        nargs="*",
        default=DEFAULT_PRIMES,
        help="prime a values to scan",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="optional JSON output path",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.time()

    by_prime = []
    total_families = 0
    total_quadruples = 0
    total_failures = 0
    total_peak_bound_issues = 0
    global_worst = None

    for a in args.primes:
        summary = summarize_prime(a)
        by_prime.append(summary)
        total_families += summary["wide_t_count"]
        total_quadruples += summary["quadruples"]
        total_failures += summary["failure_count"]
        total_peak_bound_issues += summary["peak_bound_issue_count"]

        if (
            global_worst is None
            or summary["worst_margin"] < global_worst["worst_margin"]
            or (
                summary["worst_margin"] == global_worst["worst_margin"]
                and summary["a"] < global_worst["a"]
            )
        ):
            global_worst = {
                "a": summary["a"],
                "worst_margin": summary["worst_margin"],
                "family": summary["worst_family"],
            }

        print(
            f"a={a}: wide_t={summary['wide_t_count']}, "
            f"quadruples={summary['quadruples']}, "
            f"worst_margin={summary['worst_margin']}, "
            f"failures={summary['failure_count']}, "
            f"peak_bound_issues={summary['peak_bound_issue_count']}"
        )

    payload = {
        "primes": args.primes,
        "totals": {
            "families_checked": total_families,
            "quadruples_checked": total_quadruples,
            "failure_count": total_failures,
            "peak_bound_issue_count": total_peak_bound_issues,
            "elapsed_seconds": round(time.time() - started, 3),
        },
        "global_worst": global_worst,
        "by_prime": by_prime,
    }

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print()
    print(json.dumps(payload["totals"], indent=2))
    print("global_worst =", json.dumps(global_worst, indent=2))


if __name__ == "__main__":
    main()
