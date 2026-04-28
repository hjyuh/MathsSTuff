#!/usr/bin/env python3
"""Scan Bremner's rank-one family for accidental fifth common deltas."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import math
import multiprocessing as mp
import queue
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import bremner_map
import common_deltas_factor


def _factorint_worker(value: int, out_queue: mp.Queue) -> None:
    try:
        import sympy as sp

        factorization = {int(p): int(e) for p, e in sp.factorint(value).items()}
        out_queue.put(("factored", factorization, None))
    except BaseException as exc:
        out_queue.put(("error", None, f"{type(exc).__name__}: {exc}"))


def factorint_with_timeout(
    value: int, timeout_seconds: float | None
) -> tuple[str, dict[int, int] | None, str | None]:
    if timeout_seconds is None or timeout_seconds <= 0:
        try:
            import sympy as sp

            factorization = {int(p): int(e) for p, e in sp.factorint(value).items()}
            return "factored", factorization, None
        except Exception as exc:
            return "error", None, f"{type(exc).__name__}: {exc}"

    ctx = mp.get_context("spawn")
    out_queue = ctx.Queue(maxsize=1)
    process = ctx.Process(target=_factorint_worker, args=(value, out_queue))
    process.start()
    process.join(timeout_seconds)
    if process.is_alive():
        process.terminate()
        process.join()
        out_queue.close()
        return "timeout", None, f"factorization exceeded {timeout_seconds:g}s"

    try:
        status, factorization, error = out_queue.get(timeout=1)
    except queue.Empty:
        status, factorization, error = "error", None, "factorization worker exited without a result"
    out_queue.close()
    return status, factorization, error


def common_deltas_limited(
    n_values: list[int],
    factor_timeout_seconds: float | None,
    max_anchor_divisors: int | None,
) -> tuple[str, dict]:
    factorizations = []
    divisor_counts = []
    attempts = []
    for index, value in enumerate(n_values):
        started = time.perf_counter()
        status, factorization, error = factorint_with_timeout(value, factor_timeout_seconds)
        elapsed = time.perf_counter() - started
        attempt = {
            "index": index,
            "N_digits": len(str(abs(value))),
            "status": status,
            "elapsed_seconds": round(elapsed, 3),
        }
        if error:
            attempt["error"] = error
        if factorization is None:
            attempts.append(attempt)
            return (
                "skipped_factor_timeout" if status == "timeout" else "skipped_factor_error",
                {
                    "factorization_attempts": attempts,
                    "factorizations": factorizations,
                    "per_N_divisor_counts": divisor_counts,
                },
            )

        divisor_count = common_deltas_factor.divisor_count_from_factorization(factorization)
        attempt["factor_divisor_count"] = divisor_count
        attempts.append(attempt)
        factorizations.append(factorization)
        divisor_counts.append(divisor_count)

    anchor_index = min(range(len(n_values)), key=lambda index: divisor_counts[index])
    anchor_divisor_count = divisor_counts[anchor_index]
    if max_anchor_divisors is not None and anchor_divisor_count > max_anchor_divisors:
        return (
            "skipped_divisor_bound",
            {
                "anchor_index": anchor_index,
                "anchor_divisor_count": anchor_divisor_count,
                "factorization_attempts": attempts,
                "factorizations": factorizations,
                "per_N_divisor_counts": divisor_counts,
            },
        )

    anchor_n = n_values[anchor_index]
    root = math.isqrt(anchor_n)
    common = []
    for divisor in common_deltas_factor.iter_divisors_from_factorization(
        factorizations[anchor_index]
    ):
        if divisor > root:
            continue
        delta = anchor_n // divisor - divisor
        if all(
            index == anchor_index or common_deltas_factor.is_delta_for_n(delta, other_n)
            for index, other_n in enumerate(n_values)
        ):
            common.append(delta)

    return (
        "checked",
        {
            "anchor_index": anchor_index,
            "anchor_divisor_count": anchor_divisor_count,
            "common_delta_count": len(common),
            "common_deltas": sorted(common),
            "per_N_divisor_counts": divisor_counts,
            "factorizations": factorizations,
            "factorization_attempts": attempts,
        },
    )


def scan_entry(
    n: int,
    torsion: bool,
    max_digits: int | None,
    factor_timeout_seconds: float | None,
    max_anchor_divisors: int | None,
) -> dict:
    label = f"{n}Q+T" if torsion else f"{n}Q"
    try:
        generated = bremner_map.generate(n, torsion)
    except Exception as exc:
        return {"label": label, "status": "generation_error", "error": type(exc).__name__}

    max_n_digits = max(len(str(abs(z))) for z in generated.N_values)
    entry = {
        "label": label,
        "point": generated.to_jsonable()["point"],
        "status": "generated",
        "all_N_positive": generated.all_N_positive,
        "positive_N_count": generated.positive_N_count,
        "max_N_digits": max_n_digits,
        "N_values": generated.N_values,
        "deltas": generated.deltas,
    }

    if not generated.all_N_positive:
        entry["status"] = "skipped_nonpositive_N"
        return entry
    if max_digits is not None and max_n_digits > max_digits:
        entry["status"] = "skipped_digit_bound"
        return entry

    status, details = common_deltas_limited(
        generated.N_values, factor_timeout_seconds, max_anchor_divisors
    )
    entry.update({"status": status, **details})
    if entry.get("common_delta_count", 0) >= 5:
        entry["status"] = "candidate_k5_or_better"
    return entry


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-min", type=int, default=3)
    parser.add_argument("--n-max", type=int, required=True)
    parser.add_argument("--max-digits", type=int, default=60)
    parser.add_argument(
        "--factor-timeout-seconds",
        type=float,
        default=30.0,
        help="Per-N factorization timeout. Use 0 to disable.",
    )
    parser.add_argument(
        "--max-anchor-divisors",
        type=int,
        default=10_000_000,
        help="Skip exact common-delta enumeration if the anchor N has too many divisors. Use 0 to disable.",
    )
    parser.add_argument("--include-nonpositive", action="store_true")
    parser.add_argument("--no-progress", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    max_anchor_divisors = args.max_anchor_divisors if args.max_anchor_divisors > 0 else None
    started = time.perf_counter()
    all_entries = []
    entries = []
    for n in range(args.n_min, args.n_max + 1):
        for torsion in (False, True):
            entry = scan_entry(
                n,
                torsion,
                args.max_digits,
                args.factor_timeout_seconds,
                max_anchor_divisors,
            )
            all_entries.append(entry)
            if args.include_nonpositive or entry.get("all_N_positive"):
                entries.append(entry)
            if not args.no_progress:
                print(
                    f"{entry['label']}: {entry['status']} "
                    f"(positive={entry.get('positive_N_count')}/4, "
                    f"max_N_digits={entry.get('max_N_digits')})",
                    file=sys.stderr,
                    flush=True,
                )

    candidates = [e for e in all_entries if e.get("common_delta_count", 0) >= 5]
    status_counts = Counter(e["status"] for e in all_entries)
    checked_statuses = {"checked", "candidate_k5_or_better"}
    payload = {
        "n_min": args.n_min,
        "n_max": args.n_max,
        "limits": {
            "max_digits": args.max_digits,
            "factor_timeout_seconds": args.factor_timeout_seconds,
            "max_anchor_divisors": max_anchor_divisors,
        },
        "runtime_seconds": round(time.perf_counter() - started, 3),
        "attempted_count": len(all_entries),
        "included_count": len(entries),
        "checked_count": sum(1 for e in all_entries if e["status"] in checked_statuses),
        "skipped_count": sum(1 for e in all_entries if e["status"].startswith("skipped_")),
        "candidate_count": len(candidates),
        "status_counts": dict(sorted(status_counts.items())),
        "entries": entries,
    }

    text = json.dumps(payload, indent=2, sort_keys=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
