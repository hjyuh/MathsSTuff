#!/usr/bin/env python3
"""
Push the 10 hardest post-peak families to larger horizons at the stable 1000x
maximizing start n.

This script does NOT globally re-optimize n at 10000x / 50000x / 100000x.
Instead it:

1. recomputes the exact 1000x post-peak maximizer n_1000 for each family,
2. computes G(n_1000) exactly,
3. streams the exact future maximum E_H(n_1000) to horizons 10000x, 50000x,
   and 100000x,
4. reports the resulting ratios E_H(n_1000)/(2 G(n_1000)).

This is enough to test whether the hard post-peak ratio keeps growing or
appears to stabilize at the stable candidate start seen in the 200x/500x/1000x
 exact scans.
"""

from __future__ import annotations

import argparse
import json
import time
from math import isqrt
from pathlib import Path

import numpy as np


TOP10 = [
    (199, 2, 198),
    (199, 2, 197),
    (181, 2, 178),
    (199, 2, 196),
    (199, 2, 194),
    (197, 2, 196),
    (197, 2, 195),
    (193, 2, 192),
    (191, 2, 190),
    (181, 2, 180),
]


def base_horizon(a: int, k: int) -> int:
    return a * (k * a + 1)


def exact_family_scan(a: int, k: int, t: int, multiplier: int) -> dict:
    bound = multiplier * base_horizon(a, k)
    hits = np.zeros(bound + 1, dtype=np.uint8)
    hits[a::a] = 1
    for d in range(k * a + 1, k * a + t + 1):
        hits[d::d] = 1

    pos = np.flatnonzero(hits)
    pos = pos[pos > 0]
    counts = np.arange(1, pos.size + 1, dtype=np.int32)
    ratios_hit = counts / pos.astype(np.float64)

    M = k * a + t
    i0 = int(np.searchsorted(pos, M, side="left"))
    peak_i = i0 + int(np.argmax(ratios_hit[i0:]))
    m_star = int(pos[peak_i])

    suffix = np.maximum.accumulate(ratios_hit[::-1])[::-1]
    denom_n = pos[peak_i + 1 :] - 1
    curr_counts = counts[peak_i:-1].astype(np.float64)
    future = suffix[peak_i + 1 :]
    vals = future / (2.0 * (curr_counts / denom_n.astype(np.float64)))

    best_off = int(np.argmax(vals))
    best_j = peak_i + best_off
    n_argmax = int(denom_n[best_off])
    ratio = float(vals[best_off])

    target = suffix[best_j + 1]
    rel = int(np.argmax(ratios_hit[best_j + 1 :] >= target - 1e-15))
    m_future = int(pos[best_j + 1 + rel])

    return {
        "multiplier": multiplier,
        "horizon": bound,
        "m_star": m_star,
        "n_argmax": n_argmax,
        "m_future": m_future,
        "post_ratio": ratio,
        "G_n": float((counts[best_j]) / n_argmax),
        "E_n": float(target),
    }


def count_upto(n: int, a: int, k: int, t: int) -> int:
    hits = np.zeros(n + 1, dtype=np.uint8)
    hits[a::a] = 1
    for d in range(k * a + 1, k * a + t + 1):
        hits[d::d] = 1
    return int(hits.sum())


def stream_future_max(
    a: int,
    k: int,
    t: int,
    n: int,
    checkpoints: list[int],
    chunk_size: int,
) -> dict[int, dict]:
    count = count_upto(n, a, k, t)
    best_ratio = -1.0
    best_m = None
    cur = n + 1
    out: dict[int, dict] = {}

    for H in sorted(checkpoints):
        while cur <= H:
            R = min(H, cur + chunk_size - 1)
            arr = np.zeros(R - cur + 1, dtype=np.uint8)

            d = a
            first = ((cur + d - 1) // d) * d
            if first <= R:
                arr[first - cur :: d] = 1

            for d in range(k * a + 1, k * a + t + 1):
                first = ((cur + d - 1) // d) * d
                if first <= R:
                    arr[first - cur :: d] = 1

            pos = np.flatnonzero(arr)
            if pos.size:
                nums = count + np.arange(1, pos.size + 1, dtype=np.int64)
                dens = nums / (cur + pos).astype(np.float64)
                idx = int(np.argmax(dens))
                local_best = float(dens[idx])
                if local_best > best_ratio:
                    best_ratio = local_best
                    best_m = int(cur + pos[idx])
                count += int(pos.size)

            cur = R + 1

        out[H] = {
            "E_n": best_ratio,
            "m_future": best_m,
        }

    return out


def aitken_limit(r1: float, r2: float, r3: float) -> float | None:
    denom = r3 - 2.0 * r2 + r1
    if abs(denom) < 1e-15:
        return None
    return r3 - ((r3 - r2) ** 2) / denom


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chunk-size", type=int, default=50_000_000)
    parser.add_argument("--json-out", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.time()

    rows = []
    worst = None

    for a, k, t in TOP10:
        start_family = time.time()
        exact_1000 = exact_family_scan(a, k, t, 1000)
        n = exact_1000["n_argmax"]
        G_n = exact_1000["G_n"]

        base = base_horizon(a, k)
        checkpoints = [10_000 * base, 50_000 * base, 100_000 * base]
        future = stream_future_max(a, k, t, n, checkpoints, args.chunk_size)

        ratios = {}
        for H in checkpoints:
            ratios[H] = future[H]["E_n"] / (2.0 * G_n)

        r1000 = exact_1000["post_ratio"]
        r10000 = ratios[checkpoints[0]]
        r50000 = ratios[checkpoints[1]]
        r100000 = ratios[checkpoints[2]]

        delta_1k_10k = r10000 - r1000
        delta_10k_100k = r100000 - r10000
        delta_10k_50k = r50000 - r10000
        delta_50k_100k = r100000 - r50000
        decelerating = delta_10k_100k < delta_1k_10k
        limit_est = aitken_limit(r1000, r10000, r100000) if decelerating else None

        row = {
            "a": a,
            "k": k,
            "t": t,
            "n_1000x": n,
            "m_star": exact_1000["m_star"],
            "G_n": G_n,
            "ratio_1000x": r1000,
            "E_10000x": future[checkpoints[0]]["E_n"],
            "m_future_10000x": future[checkpoints[0]]["m_future"],
            "ratio_10000x": r10000,
            "E_50000x": future[checkpoints[1]]["E_n"],
            "m_future_50000x": future[checkpoints[1]]["m_future"],
            "ratio_50000x": r50000,
            "E_100000x": future[checkpoints[2]]["E_n"],
            "m_future_100000x": future[checkpoints[2]]["m_future"],
            "ratio_100000x": r100000,
            "n_argmax_changed_from_1000x": False,
            "growth_100000x_minus_10000x": delta_10k_100k,
            "delta_1000x_to_10000x": delta_1k_10k,
            "delta_10000x_to_50000x": delta_10k_50k,
            "delta_50000x_to_100000x": delta_50k_100k,
            "decelerating": decelerating,
            "aitken_limit_estimate": limit_est,
            "elapsed_seconds": round(time.time() - start_family, 3),
        }
        rows.append(row)

        if worst is None or row["ratio_100000x"] > worst["ratio_100000x"]:
            worst = row

        print(
            f"({a},{k},{t}) n={n}: "
            f"1000x={r1000:.9f}, 10000x={r10000:.9f}, "
            f"50000x={r50000:.9f}, 100000x={r100000:.9f}, "
            f"decelerating={decelerating}, time={row['elapsed_seconds']}s"
        )

    payload = {
        "parameters": {
            "top10": TOP10,
            "chunk_size": args.chunk_size,
        },
        "totals": {
            "families": len(rows),
            "elapsed_seconds": round(time.time() - started, 3),
        },
        "worst_at_100000x": worst,
        "rows": rows,
    }

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print()
    print(json.dumps(payload["totals"], indent=2))
    print("worst_at_100000x =", json.dumps(worst, indent=2))


if __name__ == "__main__":
    main()
