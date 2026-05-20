#!/usr/bin/env python3
"""Summarize floor signatures for negative realizable four-band blocks.

This complements ``unit_step_hge2_negative_summary.py`` by grouping the
negative realizations by their alpha/beta/length signatures, not only by
primitive count patterns.  It is intended as a guard against overfitting the
buffered drift proof to the first length-three examples.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_four_band_buffer import cumulative_before
from unit_step_hge2_residue_bad import block_count, realizations


def rel_pattern(values: tuple[int, ...]) -> tuple[int, ...]:
    base = values[0]
    return tuple(value - base for value in values)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p_max", type=int)
    parser.add_argument("--p-min", type=int, default=24)
    parser.add_argument("--r-max-ratio", type=float, default=0.5)
    parser.add_argument("--target3-mod", action="store_true")
    parser.add_argument("--t-max", type=int, default=240)
    parser.add_argument("--alpha-window", type=int, default=180)
    parser.add_argument("--max-pure-records", type=int, default=200)
    parser.add_argument("--max-negative-records", type=int, default=500)
    parser.add_argument("--max-examples", type=int, default=5)
    args = parser.parse_args(argv)

    pure_records = 0
    negative_records = 0
    signatures: dict[
        tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], int, int],
        dict[str, object],
    ] = {}
    target_counts: dict[int, int] = defaultdict(int)
    residue_counts: dict[int, int] = defaultdict(int)

    for p in range(args.p_min, args.p_max + 1):
        r_max = int(args.r_max_ratio * p)
        for r in range(2, r_max + 1):
            if args.target3_mod and (p + r) % 4 != 0:
                continue
            total, _, _ = block_count(p, r)
            if total >= 3:
                continue
            pure_records += 1
            for realization in realizations(p, r, args.t_max, args.alpha_window):
                margin, K, A, t, count, target, lengths, counts, alphas, betas = realization
                if margin >= 0:
                    continue
                before_margin, _, _ = cumulative_before(K, A, t)
                negative_records += 1
                target_counts[target] += 1
                residue_counts[(p + r) % 4] += 1
                key = (lengths, rel_pattern(alphas), rel_pattern(betas), target, margin)
                if key not in signatures:
                    signatures[key] = {
                        "count": 0,
                        "min_buffer": before_margin,
                        "min_buffer_row": (
                            before_margin,
                            K,
                            A,
                            gcd(K, A),
                            t,
                            count,
                            target,
                            counts,
                            alphas,
                            betas,
                            p,
                            r,
                        ),
                        "examples": [],
                    }
                entry = signatures[key]
                entry["count"] = int(entry["count"]) + 1
                if before_margin < int(entry["min_buffer"]):
                    entry["min_buffer"] = before_margin
                    entry["min_buffer_row"] = (
                        before_margin,
                        K,
                        A,
                        gcd(K, A),
                        t,
                        count,
                        target,
                        counts,
                        alphas,
                        betas,
                        p,
                        r,
                    )
                examples = entry["examples"]
                if isinstance(examples, list) and len(examples) < args.max_examples:
                    examples.append(
                        (
                            before_margin,
                            K,
                            A,
                            gcd(K, A),
                            t,
                            count,
                            target,
                            counts,
                            alphas,
                            betas,
                            p,
                            r,
                        )
                    )
                if negative_records >= args.max_negative_records:
                    break
            if negative_records >= args.max_negative_records:
                break
            if pure_records >= args.max_pure_records:
                break
        if negative_records >= args.max_negative_records or pure_records >= args.max_pure_records:
            break

    print(f"pure_records={pure_records}")
    print(f"negative_records={negative_records}")
    print("target_counts")
    for key, value in sorted(target_counts.items()):
        print(f"{key}: {value}")
    print("residue_counts")
    for key, value in sorted(residue_counts.items()):
        print(f"{key}: {value}")
    print("signatures")
    ordered = sorted(
        signatures.items(),
        key=lambda item: (-int(item[1]["count"]), int(item[1]["min_buffer"]), item[0]),
    )
    for key, entry in ordered:
        lengths, alpha_rel, beta_rel, target, margin = key
        print(
            f"count={entry['count']} min_buffer={entry['min_buffer']} "
            f"lengths={lengths} alpha_rel={alpha_rel} beta_rel={beta_rel} "
            f"target={target} margin={margin}"
        )
        print(f"  min_row={entry['min_buffer_row']}")
        examples = entry["examples"]
        if isinstance(examples, list):
            for example in examples:
                print(f"  example={example}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
