#!/usr/bin/env python3
"""
Finite-horizon scan for the singleton-extremal conjecture.

For each M in a requested range, this script:

1. enumerates all primitive sets A with max(A)=M and |A| bounded by the
   requested limit,
2. computes the exact finite-horizon EP-488 ratio
      max_{M <= n < m <= H} G(m) / (2 G(n)),
   where H = horizon_multiplier * M,
3. enumerates all one-anchor families with the same max M and computes the same
   finite-horizon ratio,
4. reports whether any primitive set beats the worst one-anchor family.

The finite-horizon ratio is computed exactly from hit positions h_j of S_A:

- maxima of G(x)=F(x)/x occur at hit positions,
- for n in [h_j, h_{j+1}-1], G(n)=j/n and the future envelope is constant,
- hence the exact maximum over n is attained at right endpoints h_{j+1}-1.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


EPS = 1e-15


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    out: list[int] = []
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            if p * p <= n:
                sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return out


def fill_hits(hits: np.ndarray, values: Iterable[int]) -> None:
    hits.fill(0)
    for d in values:
        hits[d::d] = 1


def ratio_details_from_hits(hits: np.ndarray, M: int) -> dict:
    pos = np.flatnonzero(hits)
    i0 = int(np.searchsorted(pos, M, side="left"))
    if pos.size - i0 < 2:
        return {
            "ratio": 0.0,
            "n_argmax": None,
            "m_argmax": None,
            "hit_count": int(pos.size),
        }

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
    target = float(suffix[best + 1])
    rel = int(np.argmax(ratios_hit[best + 1 :] >= target - EPS))
    m_argmax = int(pos2[best + 1 + rel])

    return {
        "ratio": ratio,
        "n_argmax": n_argmax,
        "m_argmax": m_argmax,
        "hit_count": int(pos.size),
    }


def ratio_only_from_hits(hits: np.ndarray, M: int) -> float:
    pos = np.flatnonzero(hits)
    i0 = int(np.searchsorted(pos, M, side="left"))
    if pos.size - i0 < 2:
        return 0.0

    pos2 = pos[i0:]
    counts2 = np.arange(i0 + 1, pos.size + 1, dtype=np.int32)
    ratios_hit = counts2 / pos2.astype(np.float64)
    suffix = np.maximum.accumulate(ratios_hit[::-1])[::-1]

    denom_n = pos2[1:] - 1
    curr_counts = counts2[:-1].astype(np.float64)
    vals = suffix[1:] / (2.0 * (curr_counts / denom_n.astype(np.float64)))
    return float(vals.max())


def primitive_candidates(M: int) -> list[int]:
    return [x for x in range(2, M) if M % x != 0]


def primitive_adjacency(cands: list[int]) -> list[int]:
    n = len(cands)
    adj = [0] * n
    for i, x in enumerate(cands):
        mask = 0
        for j in range(i + 1, n):
            if cands[j] % x == 0:
                mask |= 1 << j
        adj[i] = mask
    return adj


def one_anchor_families(M: int) -> list[tuple[int, int, int, tuple[int, ...]]]:
    out: list[tuple[int, int, int, tuple[int, ...]]] = []
    for a in primes_upto(M - 1):
        for k in range(2, (M - 1) // a + 1):
            t = M - k * a
            if 1 <= t < a:
                fam = (a,) + tuple(range(k * a + 1, M + 1))
                out.append((a, k, t, fam))
    return out


@dataclass
class SetSummary:
    ratio: float
    size: int
    values: tuple[int, ...]
    n_argmax: int | None
    m_argmax: int | None
    hit_count: int


def summarize_set(values: tuple[int, ...], M: int, H: int) -> SetSummary:
    hits = np.zeros(H + 1, dtype=np.uint8)
    fill_hits(hits, values)
    info = ratio_details_from_hits(hits, M)
    return SetSummary(
        ratio=info["ratio"],
        size=len(values),
        values=values,
        n_argmax=info["n_argmax"],
        m_argmax=info["m_argmax"],
        hit_count=info["hit_count"],
    )


def scan_one_anchor_baseline(M: int, H: int) -> dict:
    best_ratio = -1.0
    best_params: tuple[int, int, int] | None = None
    best_values: tuple[int, ...] | None = None
    families = one_anchor_families(M)

    hits = np.zeros(H + 1, dtype=np.uint8)
    for a, k, t, values in families:
        fill_hits(hits, values)
        ratio = ratio_only_from_hits(hits, M)
        if ratio > best_ratio + EPS:
            best_ratio = ratio
            best_params = (a, k, t)
            best_values = values

    if best_values is None or best_params is None:
        return {
            "family_count": 0,
            "best": None,
        }

    detail = summarize_set(best_values, M, H)
    return {
        "family_count": len(families),
        "best": {
            "a": best_params[0],
            "k": best_params[1],
            "t": best_params[2],
            **asdict(detail),
        },
    }


def scan_M(task: tuple[int, int, int]) -> dict:
    M, size_limit, horizon_multiplier = task
    H = horizon_multiplier * M
    started = time.time()

    baseline = scan_one_anchor_baseline(M, H)
    baseline_ratio = -1.0
    if baseline["best"] is not None:
        baseline_ratio = float(baseline["best"]["ratio"])

    cands = primitive_candidates(M)
    adj = primitive_adjacency(cands)
    n = len(cands)

    hits = np.zeros(H + 1, dtype=np.uint8)
    current = [M] + [0] * (size_limit - 1)

    total_sets = 0
    beater_count = 0
    multi_beater_count = 0

    best_ratio = -1.0
    best_values = (M,)

    best_multi_ratio = -1.0
    best_multi_values: tuple[int, ...] | None = None

    def evaluate(depth: int) -> float:
        fill_hits(hits, current[: depth + 1])
        return ratio_only_from_hits(hits, M)

    def dfs(start: int, depth: int, banned: int) -> None:
        nonlocal total_sets, beater_count, multi_beater_count
        nonlocal best_ratio, best_values, best_multi_ratio, best_multi_values

        ratio = evaluate(depth)
        values = tuple(current[: depth + 1])
        size = depth + 1

        total_sets += 1

        if ratio > best_ratio + EPS:
            best_ratio = ratio
            best_values = values
        if size >= 2 and ratio > best_multi_ratio + EPS:
            best_multi_ratio = ratio
            best_multi_values = values

        if ratio > baseline_ratio + EPS:
            beater_count += 1
            if size >= 2:
                multi_beater_count += 1

        if depth + 1 == size_limit:
            return

        for i in range(start, n):
            if (banned >> i) & 1:
                continue
            current[depth + 1] = cands[i]
            dfs(i + 1, depth + 1, banned | (1 << i) | adj[i])

    dfs(0, 0, 0)

    best_detail = asdict(summarize_set(best_values, M, H))
    best_multi_detail = None
    if best_multi_values is not None:
        best_multi_detail = asdict(summarize_set(best_multi_values, M, H))

    return {
        "M": M,
        "size_limit": size_limit,
        "horizon": H,
        "elapsed_seconds": round(time.time() - started, 3),
        "one_anchor": baseline,
        "primitive": {
            "total_sets": total_sets,
            "best": best_detail,
            "best_multi": best_multi_detail,
            "beater_count": beater_count,
            "multi_element_beater_count": multi_beater_count,
            "best_minus_one_anchor": best_detail["ratio"] - baseline_ratio,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m-start", type=int, default=17)
    parser.add_argument("--m-end", type=int, default=50)
    parser.add_argument("--size-limit-default", type=int, default=6)
    parser.add_argument("--size-limit-small", type=int, default=8)
    parser.add_argument("--size-limit-small-max", type=int, default=30)
    parser.add_argument("--horizon-multiplier", type=int, default=1000)
    parser.add_argument("--workers", type=int, default=max(1, min(20, os.cpu_count() or 1)))
    parser.add_argument("--json-out", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.time()

    tasks = []
    for M in range(args.m_start, args.m_end + 1):
        size_limit = args.size_limit_small if M <= args.size_limit_small_max else args.size_limit_default
        tasks.append((M, size_limit, args.horizon_multiplier))

    results: list[dict] = []
    with ProcessPoolExecutor(max_workers=min(args.workers, len(tasks))) as pool:
        futures = {pool.submit(scan_M, task): task[0] for task in tasks}
        for fut in as_completed(futures):
            result = fut.result()
            results.append(result)
            M = result["M"]
            prim = result["primitive"]
            anchor = result["one_anchor"]["best"]
            anchor_ratio = None if anchor is None else anchor["ratio"]
            print(
                f"M={M}: primitive_sets={prim['total_sets']}, "
                f"best={prim['best']['ratio']:.9f}, "
                f"one_anchor={anchor_ratio:.9f}, "
                f"beaters={prim['beater_count']}, "
                f"multi_beaters={prim['multi_element_beater_count']}, "
                f"time={result['elapsed_seconds']}s"
            )

    results.sort(key=lambda row: row["M"])

    total_sets = sum(row["primitive"]["total_sets"] for row in results)
    total_beaters = sum(row["primitive"]["beater_count"] for row in results)
    total_multi_beaters = sum(row["primitive"]["multi_element_beater_count"] for row in results)
    Ms_with_beaters = [row["M"] for row in results if row["primitive"]["beater_count"] > 0]
    Ms_with_multi_beaters = [
        row["M"] for row in results if row["primitive"]["multi_element_beater_count"] > 0
    ]

    overall_best = max(results, key=lambda row: row["primitive"]["best"]["ratio"])
    worst_gap = max(results, key=lambda row: row["primitive"]["best_minus_one_anchor"])

    payload = {
        "parameters": {
            "m_start": args.m_start,
            "m_end": args.m_end,
            "size_limit_default": args.size_limit_default,
            "size_limit_small": args.size_limit_small,
            "size_limit_small_max": args.size_limit_small_max,
            "horizon_multiplier": args.horizon_multiplier,
            "workers": min(args.workers, len(tasks)),
        },
        "totals": {
            "M_count": len(results),
            "primitive_sets": total_sets,
            "beater_count": total_beaters,
            "multi_element_beater_count": total_multi_beaters,
            "elapsed_seconds": round(time.time() - started, 3),
        },
        "any_beater": total_beaters > 0,
        "any_multi_element_beater": total_multi_beaters > 0,
        "Ms_with_beaters": Ms_with_beaters,
        "Ms_with_multi_element_beaters": Ms_with_multi_beaters,
        "overall_best_primitive": {
            "M": overall_best["M"],
            **overall_best["primitive"]["best"],
        },
        "worst_gap_vs_one_anchor": {
            "M": worst_gap["M"],
            "gap": worst_gap["primitive"]["best_minus_one_anchor"],
            "primitive_best": worst_gap["primitive"]["best"],
            "one_anchor_best": worst_gap["one_anchor"]["best"],
        },
        "results": results,
    }

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print()
    print(json.dumps(payload["totals"], indent=2))
    print("any_beater =", payload["any_beater"])
    print("any_multi_element_beater =", payload["any_multi_element_beater"])
    print(
        "worst_gap_vs_one_anchor =",
        json.dumps(payload["worst_gap_vs_one_anchor"], indent=2),
    )


if __name__ == "__main__":
    main()
