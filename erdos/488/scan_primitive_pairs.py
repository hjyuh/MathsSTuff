#!/usr/bin/env python3
"""
Finite-horizon scan for EP-488 on primitive pairs {a, b}.

For each b in [3, b_max] and each a in [2, b-1] with a not dividing b, this
script computes the exact finite-horizon maximum

    max_{m > n >= b, m <= horizon_multiplier * b} G(m) / (2 G(n)),

where G(x) = F(x)/x and F counts integers <= x divisible by a or b.

The finite-horizon maximum is computed exactly from hit positions of S_A:

- maxima of G occur at hit positions,
- on each interval [h_j, h_{j+1}-1], G(n) = j/n and the future envelope is
  constant,
- hence the exact maximum over n is attained at right endpoints h_{j+1}-1.

The script reports the worst pair for each b, the overall worst pair, whether
all scanned ratios are < 1, whether the worst pair is always {b-1,b}, and
whether the worst adjacent-pair ratio matches ((2b-3)/(2b-2))^2.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np


EPS = 1e-15


@dataclass
class PairResult:
    a: int
    b: int
    horizon: int
    ratio: float
    n_argmax: int
    m_argmax: int
    F_n: int
    F_m: int
    hit_count: int


def scan_pair_with_buffer(a: int, b: int, hits: np.ndarray) -> PairResult:
    hits.fill(0)
    hits[a::a] = 1
    hits[b::b] = 1

    pos = np.flatnonzero(hits)
    i0 = int(np.searchsorted(pos, b, side="left"))
    pos2 = pos[i0:]
    counts2 = np.arange(i0 + 1, pos.size + 1, dtype=np.int32)
    ratios_hit = counts2 / pos2.astype(np.float64)
    suffix = np.maximum.accumulate(ratios_hit[::-1])[::-1]

    denom_n = pos2[1:] - 1
    curr_counts = counts2[:-1].astype(np.float64)
    vals = suffix[1:] / (2.0 * (curr_counts / denom_n.astype(np.float64)))

    best = int(np.argmax(vals))
    ratio = float(vals[best])
    n_argmax = int(denom_n[best])
    F_n = int(counts2[best])
    target = float(suffix[best + 1])
    rel = int(np.argmax(ratios_hit[best + 1 :] >= target - EPS))
    m_idx = best + 1 + rel
    m_argmax = int(pos2[m_idx])
    F_m = int(counts2[m_idx])

    return PairResult(
        a=a,
        b=b,
        horizon=hits.size - 1,
        ratio=ratio,
        n_argmax=n_argmax,
        m_argmax=m_argmax,
        F_n=F_n,
        F_m=F_m,
        hit_count=int(pos.size),
    )


def adjacent_formula_ratio(b: int) -> float:
    return ((2 * b - 3) / (2 * b - 2)) ** 2


def scan_b(task: tuple[int, int]) -> dict:
    b, horizon_multiplier = task
    H = horizon_multiplier * b
    started = time.time()
    hits = np.zeros(H + 1, dtype=np.uint8)

    pair_count = 0
    ge_one_count = 0
    best: PairResult | None = None
    worst_non_adjacent: PairResult | None = None

    for a in range(2, b):
        if b % a == 0:
            continue
        res = scan_pair_with_buffer(a, b, hits)
        pair_count += 1
        if res.ratio >= 1.0 - EPS:
            ge_one_count += 1
        if best is None or res.ratio > best.ratio + EPS:
            best = res
        if a != b - 1 and (worst_non_adjacent is None or res.ratio > worst_non_adjacent.ratio + EPS):
            worst_non_adjacent = res

    assert best is not None
    adjacent = best if best.a == b - 1 else scan_pair_with_buffer(b - 1, b, hits)
    formula = adjacent_formula_ratio(b)

    return {
        "b": b,
        "pair_count": pair_count,
        "elapsed_seconds": round(time.time() - started, 3),
        "any_ratio_ge_1": ge_one_count > 0,
        "ratio_ge_1_count": ge_one_count,
        "best_pair": asdict(best),
        "worst_non_adjacent_pair": None if worst_non_adjacent is None else asdict(worst_non_adjacent),
        "adjacent_pair": asdict(adjacent),
        "adjacent_formula_ratio": formula,
        "best_is_adjacent": best.a == b - 1,
        "adjacent_matches_formula": abs(adjacent.ratio - formula) <= 1e-12,
        "adjacent_expected_n": 2 * b - 3,
        "adjacent_expected_m": (b - 1) * (b - 1),
        "adjacent_n_matches_expected": adjacent.n_argmax == 2 * b - 3,
        "adjacent_m_matches_expected": adjacent.m_argmax == (b - 1) * (b - 1),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--b-max", type=int, default=500)
    parser.add_argument("--horizon-multiplier", type=int, default=10000)
    parser.add_argument("--workers", type=int, default=max(1, min(20, os.cpu_count() or 1)))
    parser.add_argument("--json-out", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.time()
    tasks = [(b, args.horizon_multiplier) for b in range(3, args.b_max + 1)]
    results: list[dict] = []

    with ProcessPoolExecutor(max_workers=min(args.workers, len(tasks))) as pool:
        futures = {pool.submit(scan_b, task): task[0] for task in tasks}
        for fut in as_completed(futures):
            row = fut.result()
            results.append(row)
            best = row["best_pair"]
            print(
                f"b={row['b']}: pairs={row['pair_count']}, "
                f"best=({best['a']},{best['b']}) ratio={best['ratio']:.12f}, "
                f"adjacent={row['best_is_adjacent']}, "
                f"lt1={not row['any_ratio_ge_1']}, "
                f"time={row['elapsed_seconds']}s"
            )

    results.sort(key=lambda row: row["b"])

    total_pairs = sum(row["pair_count"] for row in results)
    total_ge_one = sum(row["ratio_ge_1_count"] for row in results)
    overall_worst = max(results, key=lambda row: row["best_pair"]["ratio"])
    non_adjacent_worst = max(
        (row["worst_non_adjacent_pair"] for row in results if row["worst_non_adjacent_pair"] is not None),
        key=lambda row: row["ratio"],
    )

    not_adjacent_bs = [row["b"] for row in results if not row["best_is_adjacent"]]
    not_formula_bs = [row["b"] for row in results if not row["adjacent_matches_formula"]]
    wrong_adjacent_n_bs = [row["b"] for row in results if not row["adjacent_n_matches_expected"]]
    wrong_adjacent_m_bs = [row["b"] for row in results if not row["adjacent_m_matches_expected"]]

    payload = {
        "parameters": {
            "b_max": args.b_max,
            "horizon_multiplier": args.horizon_multiplier,
            "workers": min(args.workers, len(tasks)),
        },
        "totals": {
            "b_count": len(results),
            "pair_count": total_pairs,
            "ratio_ge_1_count": total_ge_one,
            "elapsed_seconds": round(time.time() - started, 3),
        },
        "all_ratios_lt_1": total_ge_one == 0,
        "worst_pair_always_adjacent": len(not_adjacent_bs) == 0,
        "adjacent_formula_holds_all_b": len(not_formula_bs) == 0,
        "adjacent_n_matches_all_b": len(wrong_adjacent_n_bs) == 0,
        "adjacent_m_matches_all_b": len(wrong_adjacent_m_bs) == 0,
        "b_not_adjacent": not_adjacent_bs,
        "b_formula_mismatch": not_formula_bs,
        "b_adjacent_n_mismatch": wrong_adjacent_n_bs,
        "b_adjacent_m_mismatch": wrong_adjacent_m_bs,
        "overall_worst_pair": overall_worst["best_pair"],
        "overall_worst_pair_b": overall_worst["b"],
        "overall_worst_non_adjacent_pair": non_adjacent_worst,
        "results": results,
    }

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print()
    print(json.dumps(payload["totals"], indent=2))
    print("all_ratios_lt_1 =", payload["all_ratios_lt_1"])
    print("worst_pair_always_adjacent =", payload["worst_pair_always_adjacent"])
    print("adjacent_formula_holds_all_b =", payload["adjacent_formula_holds_all_b"])
    print("b_not_adjacent =", payload["b_not_adjacent"])
    print("b_formula_mismatch =", payload["b_formula_mismatch"])
    print("overall_worst_pair =", json.dumps(payload["overall_worst_pair"], indent=2))
    print("overall_worst_non_adjacent_pair =", json.dumps(payload["overall_worst_non_adjacent_pair"], indent=2))


if __name__ == "__main__":
    main()
