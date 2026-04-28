#!/usr/bin/env python3
"""
Adversarial miner for the Proposition 7.5 bridge gap

    gap(a,b,c,h;n) = E1(n) - 2 q_h(n) - 3

in the pair-vs-two-tail setting 2 <= a < b < c < h with {a,b,c,h} primitive.

The scan is organized by h-blocks:

    n in [s h, (s+1) h - 1],   s = floor(n / h),

because q_h(n) is constant on each block while E1(n) is nondecreasing. Hence the
minimum gap on a block occurs at n = s h. We only inspect blocks whose left-end
gap is <= 1, since blocks starting above 1 cannot contain equality or negative-gap
cases.
"""

from __future__ import annotations

import argparse
import json
import time
from math import gcd, lcm
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


IntTuple = Tuple[int, ...]


def primitive_reduce(values: Sequence[int]) -> IntTuple:
    """Delete duplicates and moduli divisible by a smaller surviving modulus."""
    kept: List[int] = []
    for value in sorted(set(values)):
        if any(value % small == 0 for small in kept):
            continue
        kept.append(value)
    return tuple(kept)


def reduced_ratio(num: int, den: int) -> IntTuple:
    g = gcd(num, den)
    return (num // g, den // g)


def primitive_quadruples(max_h: int) -> Iterable[Tuple[int, int, int, int]]:
    """Enumerate primitive ordered quadruples 2 <= a < b < c < h <= max_h."""
    for h in range(5, max_h + 1):
        for c in range(4, h):
            if h % c == 0:
                continue
            for b in range(3, c):
                if c % b == 0 or h % b == 0:
                    continue
                for a in range(2, b):
                    if b % a == 0 or c % a == 0 or h % a == 0:
                        continue
                    yield (a, b, c, h)


def e1_count(n: int, a: int, b: int, lab: int, lac: int, lbc: int, labc: int) -> int:
    """Count x <= n divisible by exactly one of a,b and not by c."""
    return (
        n // a
        + n // b
        - 2 * (n // lab)
        - n // lac
        - n // lbc
        + 2 * (n // labc)
    )


def pair_one_tail_count(
    n: int, a: int, b: int, lab: int, lac: int, lbc: int, labc: int
) -> int:
    """Count x <= n in ((aN union bN) \\ cN)."""
    return n // a + n // b - n // lab - n // lac - n // lbc + n // labc


def quotient_data(a: int, b: int, c: int, h: int) -> Tuple[int, int, int]:
    return (a // gcd(a, h), b // gcd(b, h), c // gcd(c, h))


def q_count(y: int, a1: int, b1: int, c1: int) -> int:
    """Count x <= y in ((a' N union b' N) \\ c' N) after quotient reduction."""
    include = primitive_reduce((a1, b1))
    if len(include) == 1:
        u = include[0]
        return y // u - y // lcm(u, c1)
    u, v = include
    luv = lcm(u, v)
    luc = lcm(u, c1)
    lvc = lcm(v, c1)
    luvc = lcm(luv, c1)
    return y // u + y // v - y // luv - y // luc - y // lvc + y // luvc


def bridge_gap(
    n: int,
    a: int,
    b: int,
    c: int,
    h: int,
    lab: int,
    lac: int,
    lbc: int,
    labc: int,
    a1: int,
    b1: int,
    c1: int,
) -> int:
    return e1_count(n, a, b, lab, lac, lbc, labc) - 2 * q_count(n // h, a1, b1, c1) - 3


def gap_signature(
    a: int,
    b: int,
    c: int,
    h: int,
    lab: int,
    lac: int,
    lbc: int,
    labc: int,
    a1: int,
    b1: int,
    c1: int,
) -> Dict[str, object]:
    return {
        "quotient_data": [a1, b1, c1],
        "pair_gcds": [gcd(a, b), gcd(a, c), gcd(b, c)],
        "h_gcds": [gcd(a, h), gcd(b, h), gcd(c, h)],
        "relative_lcms": {
            "ab_over_h": list(reduced_ratio(lab, h)),
            "ac_over_h": list(reduced_ratio(lac, h)),
            "bc_over_h": list(reduced_ratio(lbc, h)),
            "abc_over_h": list(reduced_ratio(labc, h)),
        },
    }


def signature_key(signature: Dict[str, object]) -> str:
    return json.dumps(signature, sort_keys=True, separators=(",", ":"))


def case_payload(
    gap: int,
    n: int,
    s: int,
    a: int,
    b: int,
    c: int,
    h: int,
    e1: int,
    qh: int,
    signature: Dict[str, object],
) -> Dict[str, object]:
    return {
        "gap": gap,
        "n": n,
        "block": s,
        "quadruple": [a, b, c, h],
        "E1": e1,
        "qh": qh,
        "signature": signature,
    }


def update_family(store: Dict[str, Dict[str, object]], case: Dict[str, object]) -> None:
    key = signature_key(case["signature"])
    family = store.get(key)
    if family is None:
        store[key] = {
            "signature": case["signature"],
            "count": 1,
            "smallest_case": case,
            "blocks": [case["block"]],
        }
        return
    family["count"] += 1
    if case["block"] not in family["blocks"]:
        family["blocks"].append(case["block"])
        family["blocks"].sort()
    smallest = family["smallest_case"]
    if (
        case["n"],
        case["quadruple"][3],
        *case["quadruple"],
    ) < (
        smallest["n"],
        smallest["quadruple"][3],
        *smallest["quadruple"],
    ):
        family["smallest_case"] = case


def sort_families(families: Dict[str, Dict[str, object]]) -> List[Dict[str, object]]:
    ordered = list(families.values())
    ordered.sort(
        key=lambda item: (
            item["smallest_case"]["n"],
            item["smallest_case"]["quadruple"][3],
            *item["smallest_case"]["quadruple"],
        )
    )
    return ordered


def pair_two_tail_worst_margin(
    a: int,
    b: int,
    c: int,
    h: int,
    max_multiple: int,
) -> Dict[str, object]:
    """Exact scan for F_{a,b|{c,h}}(m)/m < 2 F_{a,b|{c,h}}(n)/n up to max_multiple * h."""
    max_x = max_multiple * h
    lab = lcm(a, b)
    lac = lcm(a, c)
    lbc = lcm(b, c)
    labc = lcm(lab, c)
    a1, b1, c1 = quotient_data(a, b, c, h)

    counts = [0] * (max_x + 1)
    for x in range(h, max_x + 1):
        p = pair_one_tail_count(x, a, b, lab, lac, lbc, labc)
        counts[x] = p - q_count(x // h, a1, b1, c1)

    best_suffix_m = [0] * (max_x + 2)
    best_m = max_x
    best_suffix_m[max_x] = max_x
    for x in range(max_x - 1, h - 1, -1):
        left = x + 1
        if counts[left] * best_m >= counts[best_m] * left:
            best_m = left
        best_suffix_m[x] = best_m

    worst = None
    for n in range(h, max_x):
        m = best_suffix_m[n]
        margin_num = 2 * counts[n] * m - counts[m] * n
        item = {
            "n": n,
            "m": m,
            "F_n": counts[n],
            "F_m": counts[m],
            "margin_num": margin_num,
            "margin_den": n * m,
        }
        if worst is None or (
            item["margin_num"] * worst["margin_den"],
            item["n"],
            item["m"],
        ) < (
            worst["margin_num"] * item["margin_den"],
            worst["n"],
            worst["m"],
        ):
            worst = item
    assert worst is not None
    return worst


def run_scan(args: argparse.Namespace) -> Dict[str, object]:
    start = time.time()
    equality_families: Dict[str, Dict[str, object]] = {}
    near_miss_families: Dict[str, Dict[str, object]] = {}
    gap1_families: Dict[str, Dict[str, object]] = {}
    candidate_quads = set()
    smallest_negative_cases: List[Dict[str, object]] = []
    min_gap = None
    primitive_count = 0
    candidate_blocks = 0
    equality_cases = 0
    gap1_cases = 0
    negative_cases = 0

    for a, b, c, h in primitive_quadruples(args.max_h):
        primitive_count += 1
        lab = lcm(a, b)
        lac = lcm(a, c)
        lbc = lcm(b, c)
        labc = lcm(lab, c)
        a1, b1, c1 = quotient_data(a, b, c, h)
        signature = gap_signature(a, b, c, h, lab, lac, lbc, labc, a1, b1, c1)

        for s in range(1, args.max_multiple + 1):
            n0 = s * h
            gap0 = bridge_gap(n0, a, b, c, h, lab, lac, lbc, labc, a1, b1, c1)
            if min_gap is None or gap0 < min_gap:
                min_gap = gap0

            if gap0 > 1:
                continue

            candidate_blocks += 1
            block_end = (s + 1) * h - 1
            qh = q_count(s, a1, b1, c1)

            for n in range(n0, block_end + 1):
                e1 = e1_count(n, a, b, lab, lac, lbc, labc)
                gap = e1 - 2 * qh - 3
                if gap > 1:
                    break

                case = case_payload(gap, n, s, a, b, c, h, e1, qh, signature)
                candidate_quads.add((a, b, c, h))

                if gap == 0:
                    equality_cases += 1
                    update_family(equality_families, case)
                elif gap == 1:
                    gap1_cases += 1
                    update_family(gap1_families, case)
                else:
                    negative_cases += 1
                    update_family(near_miss_families, case)
                    smallest_negative_cases.append(case)

    smallest_negative_cases.sort(
        key=lambda item: (item["gap"], item["n"], item["quadruple"][3], *item["quadruple"])
    )
    smallest_negative_cases = smallest_negative_cases[: args.report_limit]

    pair_tail_checks = []
    pair_tail_counterexamples = []
    if args.check_pair_tail:
        for a, b, c, h in sorted(candidate_quads):
            worst = pair_two_tail_worst_margin(a, b, c, h, args.max_multiple)
            payload = {
                "quadruple": [a, b, c, h],
                **worst,
            }
            pair_tail_checks.append(payload)
            if worst["margin_num"] <= 0:
                pair_tail_counterexamples.append(payload)
        pair_tail_checks.sort(
            key=lambda item: (
                item["margin_num"] / item["margin_den"],
                item["quadruple"][3],
                *item["quadruple"],
            )
        )
        pair_tail_checks = pair_tail_checks[: args.report_limit]

    elapsed = time.time() - start
    return {
        "parameters": {
            "max_h": args.max_h,
            "max_multiple": args.max_multiple,
            "check_pair_tail": args.check_pair_tail,
            "report_limit": args.report_limit,
        },
        "totals": {
            "primitive_quadruples": primitive_count,
            "candidate_blocks": candidate_blocks,
            "equality_cases": equality_cases,
            "gap1_cases": gap1_cases,
            "negative_cases": negative_cases,
            "min_gap": min_gap,
            "candidate_quadruples_for_pair_tail": len(candidate_quads),
            "elapsed_seconds": round(elapsed, 3),
        },
        "smallest_equality_families": sort_families(equality_families)[: args.report_limit],
        "smallest_gap1_families": sort_families(gap1_families)[: args.report_limit],
        "smallest_near_miss_families": sort_families(near_miss_families)[: args.report_limit],
        "smallest_negative_cases": smallest_negative_cases,
        "pair_tail_worst_margins": pair_tail_checks,
        "pair_tail_counterexamples": pair_tail_counterexamples[: args.report_limit],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-h", type=int, default=80, help="scan 2 <= a < b < c < h <= max_h")
    parser.add_argument(
        "--max-multiple",
        type=int,
        default=12,
        help="scan h-blocks s = 1..max_multiple, i.e. n <= max_multiple * h",
    )
    parser.add_argument(
        "--report-limit",
        type=int,
        default=12,
        help="maximum number of families or witnesses reported in each bucket",
    )
    parser.add_argument(
        "--check-pair-tail",
        action="store_true",
        help="for candidate small-gap quadruples, also scan the full pair-vs-two-tail inequality",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="optional path for the JSON summary",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = run_scan(args)
    payload = json.dumps(summary, indent=2, sort_keys=False)
    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
