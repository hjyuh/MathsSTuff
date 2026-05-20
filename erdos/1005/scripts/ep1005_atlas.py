#!/usr/bin/env python3
"""Exact EP1005 rank-gap and minimizer atlas utilities.

This complements ``farey_rank_gap.py``.  It keeps the simple Farey recurrence
as the oracle, but emits machine-readable data and verifies the standard
Mobius/floor rank-gap formula against direct Farey ranks.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from math import gcd
from pathlib import Path
from typing import Iterable, Optional, Sequence, Tuple

from farey_rank_gap import (
    PairRecord,
    SearchResult,
    farey_sequence,
    is_bad_pair,
    shortest_bad_pairs,
    term_text,
)


Term = Tuple[int, int]


@dataclass(frozen=True)
class AtlasRow:
    n: int
    farey_size: int
    raw_gap: int
    f_value: int
    total_pairs_at_gap: int
    rank_left: int
    rank_right: int
    left_num: int
    left_den: int
    right_num: int
    right_den: int
    delta_num: int
    delta_den_down: int
    det: int
    left_den_slack: int
    right_den_slack: int
    center2_left_offset: int
    center2_right_offset: int
    predicted_f: int
    excess_over_predicted: int
    predicted_template: bool


def mobius_sieve(n: int) -> list[int]:
    """Return mu[0..n]."""
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    primes: list[int] = []
    mu[0] = 0
    if n >= 1:
        mu[1] = 1
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > n:
                break
            is_prime[v] = False
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu


def all_numerator_count(q: int, left: Term, right: Term) -> int:
    """Count all integer p with left < p/q < right, before gcd filtering."""
    a, b = left
    c, d = right
    lo = (a * q) // b + 1
    hi = (c * q - 1) // d
    return max(0, hi - lo + 1)


def primitive_count_direct(q: int, left: Term, right: Term) -> int:
    """Count reduced p/q in the open interval by direct gcd tests."""
    a, b = left
    c, d = right
    lo = (a * q) // b + 1
    hi = (c * q - 1) // d
    if hi < lo:
        return 0
    return sum(1 for p in range(lo, hi + 1) if gcd(p, q) == 1)


def inside_count_direct(n: int, left: Term, right: Term) -> int:
    return sum(primitive_count_direct(q, left, right) for q in range(1, n + 1))


def inside_count_mobius(n: int, left: Term, right: Term, mu: Optional[list[int]] = None) -> int:
    """Exact count of reduced Farey fractions strictly between endpoints.

    Uses

        sum_{e<=n} mu(e) * #{t/s : s<=n/e, left < t/s < right}.

    The inner count is over all integer numerators before imposing coprimality.
    """
    if mu is None:
        mu = mobius_sieve(n)
    total = 0
    for e in range(1, n + 1):
        if mu[e] == 0:
            continue
        limit = n // e
        inner = sum(all_numerator_count(s, left, right) for s in range(1, limit + 1))
        total += mu[e] * inner
    return total


def predicted_value(n: int) -> int:
    d = [1, 2, 2, 4][n % 4]
    return n // 4 + d


def predicted_pair(n: int) -> Optional[Tuple[Term, Term]]:
    if n < 4:
        return None
    r = n % 4
    m = n // 4
    if r == 0:
        return (2 * m - 1, 4 * m), (2 * m, 4 * m - 1)
    if r in (1, 2):
        return (2 * m, 4 * m + 1), (2 * m + 1, 4 * m)
    if m == 1:
        return (1, 6), (2, 5)
    return (2 * m, 4 * m + 1), (2 * m + 1, 4 * m)


def pair_to_row(result: SearchResult, pair: PairRecord) -> AtlasRow:
    n = result.n
    left = pair.left
    right = pair.right
    pred = predicted_value(n)
    template = predicted_pair(n)
    return AtlasRow(
        n=n,
        farey_size=result.farey_size,
        raw_gap=result.raw_gap,
        f_value=result.in_between,
        total_pairs_at_gap=result.total_pairs_at_gap,
        rank_left=pair.left_rank,
        rank_right=pair.right_rank,
        left_num=left[0],
        left_den=left[1],
        right_num=right[0],
        right_den=right[1],
        delta_num=right[0] - left[0],
        delta_den_down=left[1] - right[1],
        det=left[1] * right[0] - left[0] * right[1],
        left_den_slack=n - left[1],
        right_den_slack=n - right[1],
        center2_left_offset=2 * left[0] - left[1],
        center2_right_offset=2 * right[0] - right[1],
        predicted_f=pred,
        excess_over_predicted=result.in_between - pred,
        predicted_template=template == (left, right),
    )


def write_atlas(start: int, stop: int, out_csv: Path, out_jsonl: Optional[Path], max_pairs: int) -> None:
    rows: list[AtlasRow] = []
    json_records: list[dict] = []
    for n in range(start, stop + 1):
        result = shortest_bad_pairs(n, max_pairs=max_pairs)
        for pair in result.shown_pairs:
            row = pair_to_row(result, pair)
            rows.append(row)
            json_records.append(
                {
                    **asdict(row),
                    "left": [pair.left[0], pair.left[1]],
                    "right": [pair.right[0], pair.right[1]],
                }
            )
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))
    if out_jsonl is not None:
        out_jsonl.parent.mkdir(parents=True, exist_ok=True)
        with out_jsonl.open("w", encoding="utf-8") as f:
            for record in json_records:
                f.write(json.dumps(record, sort_keys=True) + "\n")


def near_pairs_for_n(n: int, tau: int) -> tuple[SearchResult, list[PairRecord]]:
    """Return all bad pairs whose raw gap is at most the minimum plus tau."""
    result = shortest_bad_pairs(n, max_pairs=0)
    seq = farey_sequence(n)
    pairs: list[PairRecord] = []
    for gap in range(result.raw_gap, result.raw_gap + tau + 1):
        for i in range(len(seq) - gap):
            left = seq[i]
            right = seq[i + gap]
            if is_bad_pair(left, right):
                pairs.append(
                    PairRecord(
                        left_rank=i + 1,
                        right_rank=i + gap + 1,
                        left=left,
                        right=right,
                    )
                )
    return result, pairs


def write_near_atlas(start: int, stop: int, tau: int, out_jsonl: Path) -> None:
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("w", encoding="utf-8") as f:
        for n in range(start, stop + 1):
            result, pairs = near_pairs_for_n(n, tau)
            pred = predicted_value(n)
            template = predicted_pair(n)
            for pair in pairs:
                left = pair.left
                right = pair.right
                record = {
                    "n": n,
                    "farey_size": result.farey_size,
                    "g_min": result.raw_gap,
                    "f_value": result.in_between,
                    "raw_gap": pair.raw_gap,
                    "inside": pair.in_between,
                    "excess_over_min": pair.raw_gap - result.raw_gap,
                    "excess_over_predicted_gap": pair.raw_gap - (pred + 1),
                    "predicted_f": pred,
                    "left": [left[0], left[1]],
                    "right": [right[0], right[1]],
                    "rank_left": pair.left_rank,
                    "rank_right": pair.right_rank,
                    "delta_num": right[0] - left[0],
                    "delta_den_down": left[1] - right[1],
                    "det": left[1] * right[0] - left[0] * right[1],
                    "left_den_slack": n - left[1],
                    "right_den_slack": n - right[1],
                    "center2_left_offset": 2 * left[0] - left[1],
                    "center2_right_offset": 2 * right[0] - right[1],
                    "predicted_template": template == (left, right),
                    "diagonal": right[0] - left[0] == 1 and left[1] - right[1] == 1,
                }
                f.write(json.dumps(record, sort_keys=True) + "\n")


def verify_rank_formula(n_max: int, pairs_per_n: int) -> None:
    """Cross-check direct Farey rank gaps with direct and Mobius interval counts."""
    for n in range(4, n_max + 1):
        result = shortest_bad_pairs(n, max_pairs=pairs_per_n)
        mu = mobius_sieve(n)
        for pair in result.shown_pairs:
            direct = inside_count_direct(n, pair.left, pair.right)
            mobius = inside_count_mobius(n, pair.left, pair.right, mu)
            expected = pair.in_between
            if direct != expected or mobius != expected:
                raise AssertionError(
                    f"n={n}, {term_text(pair.left)} < {term_text(pair.right)}: "
                    f"rank={expected}, direct={direct}, mobius={mobius}"
                )
    print(f"rank formula verified for n=4..{n_max}, first {pairs_per_n} minimizer(s) per n")


def summarize(csv_path: Path) -> None:
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    exceptions = sorted({r["n"] for r in rows if int(r["excess_over_predicted"]) < 0}, key=int)
    non_templates = [r for r in rows if r["predicted_template"] != "True"]
    diagonal = [
        r
        for r in rows
        if int(r["delta_num"]) == 1 and int(r["delta_den_down"]) == 1
    ]
    print(f"rows: {len(rows)}")
    print(f"n range: {rows[0]['n']}..{rows[-1]['n']}")
    print(f"orders below predicted upper-bound value: {len(exceptions)}")
    if exceptions:
        print("  " + ", ".join(exceptions))
    print(f"shown pairs that are not the residue-class predicted template: {len(non_templates)}")
    if non_templates:
        print("  first non-template rows:")
        for r in non_templates[:20]:
            print(
                "  "
                + f"n={r['n']} f={r['f_value']} pair={r['left_num']}/{r['left_den']}<"
                + f"{r['right_num']}/{r['right_den']} det={r['det']}"
            )
    print(f"diagonal pairs among shown rows: {len(diagonal)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_atlas = sub.add_parser("atlas", help="write minimizer atlas data")
    p_atlas.add_argument("start", type=int)
    p_atlas.add_argument("stop", type=int)
    p_atlas.add_argument("--max-pairs", type=int, default=8)
    p_atlas.add_argument("--csv", type=Path, required=True)
    p_atlas.add_argument("--jsonl", type=Path)

    p_near = sub.add_parser("near-atlas", help="write all bad pairs within tau of g_min")
    p_near.add_argument("start", type=int)
    p_near.add_argument("stop", type=int)
    p_near.add_argument("--tau", type=int, default=10)
    p_near.add_argument("--jsonl", type=Path, required=True)

    p_verify = sub.add_parser("verify-rank", help="verify interval count formulas")
    p_verify.add_argument("n_max", type=int)
    p_verify.add_argument("--pairs-per-n", type=int, default=3)

    p_count = sub.add_parser("count", help="count fractions between two endpoints")
    p_count.add_argument("n", type=int)
    p_count.add_argument("left")
    p_count.add_argument("right")

    p_summary = sub.add_parser("summarize", help="summarize an atlas CSV")
    p_summary.add_argument("csv", type=Path)

    return parser


def parse_term(text: str) -> Term:
    a_text, b_text = text.split("/", 1)
    return int(a_text), int(b_text)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.cmd == "atlas":
        write_atlas(args.start, args.stop, args.csv, args.jsonl, args.max_pairs)
        return 0
    if args.cmd == "near-atlas":
        write_near_atlas(args.start, args.stop, args.tau, args.jsonl)
        return 0
    if args.cmd == "verify-rank":
        verify_rank_formula(args.n_max, args.pairs_per_n)
        return 0
    if args.cmd == "count":
        left = parse_term(args.left)
        right = parse_term(args.right)
        print(inside_count_mobius(args.n, left, right))
        return 0
    if args.cmd == "summarize":
        summarize(args.csv)
        return 0
    raise AssertionError(args.cmd)


if __name__ == "__main__":
    raise SystemExit(main())
