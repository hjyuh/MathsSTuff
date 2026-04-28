#!/usr/bin/env python3
"""
Computational scan for the post-peak coarse bound in one-anchor families.

For A = {a} U {ka+1, ..., ka+t} with a prime, k in {2,3,4}, and wide
t > 2*sqrt(a), this script:

1. finds m* = earliest maximizer of G(x) = F(x)/x on [M, bound],
2. computes the finite-horizon future envelope E_bound(n) = max_{m in (n,bound]} G(m),
3. maximizes E_bound(n) / (2 G(n)) over all n >= m*.

The scan is exact on the chosen finite horizon. To avoid a full F-array, it uses
only the hit positions h_j of S_A:

- maxima of G occur at hit positions,
- for n in [h_j, h_{j+1}-1], G(n) = j/n and E(n) is constant,
- hence the post-peak ratio is maximized at right endpoints h_{j+1}-1.

This gives an exact finite-horizon post-peak maximum from the hit list alone.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import asdict, dataclass
from math import isqrt
from pathlib import Path
from typing import Iterable

import numpy as np


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


def wide_t_values(a: int) -> range:
    return range(isqrt(4 * a) + 1, a)


@dataclass
class FamilyResult:
    a: int
    k: int
    t: int
    horizon: int
    m_star: int
    peak_ratio: float
    n_argmax: int
    m_future: int
    post_ratio: float
    offset_from_peak: int
    hit_count: int


def family_horizon(a: int, k: int, multiplier: int) -> int:
    return multiplier * a * (k * a + 1)


def scan_family_from_hits(hits: np.ndarray, a: int, k: int, t: int, bound: int) -> FamilyResult:
    pos = np.flatnonzero(hits)
    pos = pos[pos > 0]

    counts = np.arange(1, pos.size + 1, dtype=np.int32)
    ratios_hit = counts / pos.astype(np.float64)

    M = k * a + t
    i0 = int(np.searchsorted(pos, M, side="left"))
    peak_i = i0 + int(np.argmax(ratios_hit[i0:]))
    m_star = int(pos[peak_i])
    peak_ratio = float(ratios_hit[peak_i])

    suffix = np.maximum.accumulate(ratios_hit[::-1])[::-1]

    # For n in [pos[j], pos[j+1]-1], G(n)=counts[j]/n and E(n)=suffix[j+1].
    denom_n = pos[peak_i + 1 :] - 1
    curr_counts = counts[peak_i:-1].astype(np.float64)
    future = suffix[peak_i + 1 :]
    ratios = future / (2.0 * (curr_counts / denom_n.astype(np.float64)))

    best_off = int(np.argmax(ratios))
    best_j = peak_i + best_off
    n_argmax = int(denom_n[best_off])
    post_ratio = float(ratios[best_off])

    # Within the finite horizon, future envelope at this n is attained at the
    # first hit position with the suffix-max ratio.
    target = suffix[best_j + 1]
    rel = int(np.argmax(ratios_hit[best_j + 1 :] >= target - 1e-15))
    m_future = int(pos[best_j + 1 + rel])

    return FamilyResult(
        a=a,
        k=k,
        t=t,
        horizon=bound,
        m_star=m_star,
        peak_ratio=peak_ratio,
        n_argmax=n_argmax,
        m_future=m_future,
        post_ratio=post_ratio,
        offset_from_peak=n_argmax - m_star,
        hit_count=int(pos.size),
    )


def scan_block(a: int, k: int, multiplier: int) -> list[FamilyResult]:
    bound = family_horizon(a, k, multiplier)
    hits = np.zeros(bound + 1, dtype=np.uint8)
    hits[a::a] = 1

    results: list[FamilyResult] = []
    wide_start = isqrt(4 * a) + 1
    for t in range(1, a):
        d = k * a + t
        hits[d::d] = 1
        if t < wide_start:
            continue
        results.append(scan_family_from_hits(hits, a, k, t, bound))
    return results


def run_broad_scan(prime_limit: int, ks: Iterable[int], multiplier: int) -> list[FamilyResult]:
    results: list[FamilyResult] = []
    primes = [p for p in primes_upto(prime_limit) if p >= 5]
    for a in primes:
        for k in ks:
            block = scan_block(a, k, multiplier)
            if not block:
                continue
            block_best = max(block, key=lambda r: r.post_ratio)
            print(
                f"a={a}, k={k}: families={len(block)}, "
                f"block_max={block_best.post_ratio:.9f} at t={block_best.t}, "
                f"n={block_best.n_argmax}, offset={block_best.offset_from_peak}"
            )
            results.extend(block)
    return results


def scan_single_family(a: int, k: int, t: int, multiplier: int) -> FamilyResult:
    bound = family_horizon(a, k, multiplier)
    hits = np.zeros(bound + 1, dtype=np.uint8)
    hits[a::a] = 1
    for d in range(k * a + 1, k * a + t + 1):
        hits[d::d] = 1
    return scan_family_from_hits(hits, a, k, t, bound)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime-limit", type=int, default=199)
    parser.add_argument("--ks", type=int, nargs="*", default=[2, 3, 4])
    parser.add_argument("--multiplier", type=int, default=50)
    parser.add_argument("--top-k", type=int, default=40)
    parser.add_argument("--deep-multipliers", type=int, nargs="*", default=[100, 200, 500, 1000])
    parser.add_argument("--json-out", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.time()

    broad = run_broad_scan(args.prime_limit, args.ks, args.multiplier)
    broad.sort(key=lambda r: r.post_ratio, reverse=True)
    overall = broad[0]

    offset_hist: dict[int, int] = {}
    plus_one_count = 0
    for r in broad:
        offset_hist[r.offset_from_peak] = offset_hist.get(r.offset_from_peak, 0) + 1
        if r.offset_from_peak == 1:
            plus_one_count += 1
    top_offsets = sorted(offset_hist.items(), key=lambda kv: (-kv[1], kv[0]))[:20]

    deep_inputs = broad[: args.top_k]
    deep_results: list[dict] = []
    deep_overall = None
    for fam in deep_inputs:
        entry = {
            "a": fam.a,
            "k": fam.k,
            "t": fam.t,
            "broad": asdict(fam),
            "deep": [],
        }
        for mult in args.deep_multipliers:
            res = scan_single_family(fam.a, fam.k, fam.t, mult)
            item = {
                "multiplier": mult,
                **asdict(res),
            }
            entry["deep"].append(item)
            if deep_overall is None or res.post_ratio > deep_overall["post_ratio"]:
                deep_overall = item
        deep_results.append(entry)
        print(
            f"deep a={fam.a}, k={fam.k}, t={fam.t}: "
            + ", ".join(
                f"{item['multiplier']}x->{item['post_ratio']:.9f}"
                for item in entry["deep"]
            )
        )

    payload = {
        "parameters": {
            "prime_limit": args.prime_limit,
            "ks": args.ks,
            "multiplier": args.multiplier,
            "top_k": args.top_k,
            "deep_multipliers": args.deep_multipliers,
        },
        "totals": {
            "families": len(broad),
            "elapsed_seconds": round(time.time() - started, 3),
        },
        "broad_overall": asdict(overall),
        "broad_top_100": [asdict(r) for r in broad[:100]],
        "all_broad_lt_5_8": all(r.post_ratio < 0.625 for r in broad),
        "offset_plus_one_count": plus_one_count,
        "offset_hist_top": top_offsets,
        "deep_overall": deep_overall,
        "deep_results": deep_results,
    }

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print()
    print(json.dumps(payload["totals"], indent=2))
    print("broad_overall =", json.dumps(payload["broad_overall"], indent=2))
    print("all_broad_lt_5_8 =", payload["all_broad_lt_5_8"])
    print("offset_plus_one_count =", plus_one_count)
    print("offset_hist_top =", json.dumps(top_offsets))
    print("deep_overall =", json.dumps(deep_overall, indent=2))


if __name__ == "__main__":
    main()
