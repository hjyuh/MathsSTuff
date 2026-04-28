#!/usr/bin/env python3
"""Exact analysis for the dense EP-488 region with max(A) <= 100.

Target region:
  - A primitive
  - S1(A) > 2 / min(A)
  - max(A) > 2 * min(A)
  - max(A) <= 100

Implemented pieces:
  1. Exact counting by min(A)=a, with a core/tail split at 50.
  2. Exact one-anchor-family count in the same region.
  3. Exact global-ratio search for primitive triples in the region.

The all-k worst-ratio search is still substantially larger than the exact count.
This script provides enough structure to batch the expensive pieces by a-range.
"""

from __future__ import annotations

import argparse
import json
import time
from bisect import bisect_right
from functools import lru_cache
from math import gcd
from pathlib import Path


EPS = 1e-15


def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exact_ratio_first_period(A: tuple[int, ...]) -> dict:
    M = A[-1]
    L = 1
    for a in A:
        L = lcm2(L, a)
    H = M + L
    hit = bytearray(H + 1)
    for a in A:
        for m in range(a, H + 1, a):
            hit[m] = 1

    running = 0
    min_g = float("inf")
    max_g = -1.0
    min_x = max_x = M
    for x in range(1, H + 1):
        running += hit[x]
        if x < M:
            continue
        g = running / x
        if g < min_g:
            min_g = g
            min_x = x
        if g > max_g:
            max_g = g
            max_x = x
    return {
        "A": list(A),
        "ratio": max_g / (2.0 * min_g),
        "min_x": min_x,
        "max_x": max_x,
        "min_g": min_g,
        "max_g": max_g,
        "period": L,
    }


def dense_region_count_for_a(a: int, max_a: int) -> dict:
    """Exact count for fixed min(A)=a in the target region."""

    core_vals = [x for x in range(a + 1, min(max_a, 50) + 1) if x % a != 0]
    tail_vals = [x for x in range(51, max_a + 1) if x % a != 0]
    n_core = len(core_vals)
    n_tail = len(tail_vals)
    core_w = [1.0 / x for x in core_vals]
    tail_w = [1.0 / x for x in tail_vals]

    big_core_mask = 0
    for i, x in enumerate(core_vals):
        if x > 2 * a:
            big_core_mask |= 1 << i

    big_tail_mask = 0
    for i, x in enumerate(tail_vals):
        if x > 2 * a:
            big_tail_mask |= 1 << i

    kill_core = [0] * n_core
    kill_tail = [0] * n_core
    for i, x in enumerate(core_vals):
        mask_core = 0
        for j in range(i + 1, n_core):
            if core_vals[j] % x == 0:
                mask_core |= 1 << j
        kill_core[i] = mask_core

        mask_tail = 0
        for j, y in enumerate(tail_vals):
            if y % x == 0:
                mask_tail |= 1 << j
        kill_tail[i] = mask_tail

    pow2 = [1] * (n_tail + 1)
    for i in range(1, n_tail + 1):
        pow2[i] = pow2[i - 1] * 2

    def sum_mask(mask: int, weights: list[float]) -> float:
        total = 0.0
        while mask:
            bit = mask & -mask
            idx = bit.bit_length() - 1
            total += weights[idx]
            mask ^= bit
        return total

    @lru_cache(maxsize=None)
    def ext_count(live_core_mask: int, live_tail_mask: int, big_hit: bool) -> int:
        if live_core_mask == 0:
            count_tail = live_tail_mask.bit_count()
            if big_hit:
                return pow2[count_tail]
            usable_big = live_tail_mask & big_tail_mask
            if usable_big == 0:
                return 0
            small_only_count = (live_tail_mask ^ usable_big).bit_count()
            return pow2[count_tail] - pow2[small_only_count]

        bit = live_core_mask & -live_core_mask
        idx = bit.bit_length() - 1
        exclude = ext_count(live_core_mask ^ bit, live_tail_mask, big_hit)
        include = ext_count(
            live_core_mask & ~(bit | kill_core[idx]),
            live_tail_mask & ~kill_tail[idx],
            big_hit or (core_vals[idx] > 2 * a),
        )
        return exclude + include

    @lru_cache(maxsize=None)
    def prep_tail(mask: int):
        idxs: list[int] = []
        work = mask
        while work:
            bit = work & -work
            idxs.append(bit.bit_length() - 1)
            work ^= bit

        vals = [tail_w[i] for i in idxs]
        bigs = [tail_vals[i] > 2 * a for i in idxs]
        mid = len(vals) // 2

        vals1 = vals[:mid]
        vals2 = vals[mid:]
        big1 = bigs[:mid]
        big2 = bigs[mid:]

        subs1: list[tuple[float, bool]] = []
        for mask1 in range(1 << len(vals1)):
            total = 0.0
            hit_big = False
            for j, w in enumerate(vals1):
                if (mask1 >> j) & 1:
                    total += w
                    hit_big = hit_big or big1[j]
            subs1.append((total, hit_big))

        subs2_any: list[float] = []
        subs2_no_big: list[float] = []
        for mask2 in range(1 << len(vals2)):
            total = 0.0
            hit_big = False
            for j, w in enumerate(vals2):
                if (mask2 >> j) & 1:
                    total += w
                    hit_big = hit_big or big2[j]
            subs2_any.append(total)
            if not hit_big:
                subs2_no_big.append(total)

        subs2_any.sort()
        subs2_no_big.sort()
        return subs1, subs2_any, subs2_no_big

    def tail_query(mask: int, residual: float, need_big: bool) -> int:
        if residual < EPS:
            count_tail = mask.bit_count()
            if not need_big:
                return pow2[count_tail]
            usable_big = mask & big_tail_mask
            if usable_big == 0:
                return 0
            small_only_count = (mask ^ usable_big).bit_count()
            return pow2[count_tail] - pow2[small_only_count]

        if mask == 0:
            return 0

        subs1, subs2_any, subs2_no_big = prep_tail(mask)
        total = 0
        len_any = len(subs2_any)
        len_no_big = len(subs2_no_big)

        for left_sum, left_has_big in subs1:
            threshold = residual - left_sum + EPS
            if (not need_big) or left_has_big:
                total += len_any - bisect_right(subs2_any, threshold)
            else:
                total += len_any - bisect_right(subs2_any, threshold)
                total -= len_no_big - bisect_right(subs2_no_big, threshold)
        return total

    target = 2.0 / a
    full_core_mask = (1 << n_core) - 1
    full_tail_mask = (1 << n_tail) - 1
    full_core_sum = sum(core_w)
    full_tail_sum = sum(tail_w)

    leaf_queries = 0

    def dfs(
        live_core_mask: int,
        live_tail_mask: int,
        cur_s1: float,
        rem_core_sum: float,
        rem_tail_sum: float,
        big_hit: bool,
    ) -> int:
        nonlocal leaf_queries

        if cur_s1 + rem_core_sum + rem_tail_sum <= target + EPS:
            return 0

        if cur_s1 > target + EPS:
            if big_hit or (live_core_mask & big_core_mask) or (live_tail_mask & big_tail_mask):
                return ext_count(live_core_mask, live_tail_mask, big_hit)
            return 0

        if live_core_mask == 0:
            leaf_queries += 1
            return tail_query(live_tail_mask, target - cur_s1, not big_hit)

        bit = live_core_mask & -live_core_mask
        idx = bit.bit_length() - 1

        removed_core = live_core_mask & (bit | kill_core[idx])
        removed_tail = live_tail_mask & kill_tail[idx]
        removed_core_sum = sum_mask(removed_core, core_w)
        removed_tail_sum = sum_mask(removed_tail, tail_w)

        include = dfs(
            live_core_mask & ~(bit | kill_core[idx]),
            live_tail_mask & ~kill_tail[idx],
            cur_s1 + core_w[idx],
            rem_core_sum - removed_core_sum,
            rem_tail_sum - removed_tail_sum,
            big_hit or (core_vals[idx] > 2 * a),
        )
        exclude = dfs(
            live_core_mask ^ bit,
            live_tail_mask,
            cur_s1,
            rem_core_sum - core_w[idx],
            rem_tail_sum,
            big_hit,
        )
        return include + exclude

    t0 = time.time()
    total_count = dfs(full_core_mask, full_tail_mask, 1.0 / a, full_core_sum, full_tail_sum, False)
    elapsed = time.time() - t0
    return {
        "a": a,
        "count": total_count,
        "core_size": n_core,
        "tail_size": n_tail,
        "leaf_queries": leaf_queries,
        "ext_cache": ext_count.cache_info()._asdict(),
        "tail_cache": prep_tail.cache_info()._asdict(),
        "elapsed_seconds": round(elapsed, 6),
    }


def count_range(a_start: int, a_end: int, max_a: int) -> dict:
    rows = []
    total = 0
    started = time.time()
    for a in range(a_start, a_end + 1):
        if 2 * a >= max_a:
            continue
        row = dense_region_count_for_a(a, max_a)
        rows.append(row)
        total += row["count"]
        print(
            f"a={a:2d} count={row['count']} subtotal={total} "
            f"time={row['elapsed_seconds']:.3f}s"
        )
    return {
        "a_start": a_start,
        "a_end": a_end,
        "max_a": max_a,
        "total_count": total,
        "rows": rows,
        "elapsed_seconds": round(time.time() - started, 6),
    }


def one_anchor_count(max_a: int) -> dict:
    total = 0
    rows = []
    for a in range(2, max_a + 1):
        is_prime = all(a % p for p in range(2, int(a**0.5) + 1))
        if not is_prime:
            continue
        local = 0
        for k in range(2, max_a + 1):
            start = k * a + 1
            if start > max_a:
                break
            max_t = min(a - 1, max_a - k * a)
            for t in range(1, max_t + 1):
                s1 = (1.0 / a) + sum(1.0 / (k * a + j) for j in range(1, t + 1))
                if s1 > 2.0 / a + EPS:
                    total += 1
                    local += 1
        if local:
            rows.append({"a": a, "count": local})
    return {"total_count": total, "rows": rows}


def exact_dense_triples(max_a: int) -> dict:
    total = 0
    best = None
    for a in range(2, max_a):
        for b in range(a + 1, max_a):
            if b % a == 0:
                continue
            for c in range(b + 1, max_a + 1):
                if c % a == 0 or c % b == 0:
                    continue
                s1 = (1.0 / a) + (1.0 / b) + (1.0 / c)
                if s1 <= 2.0 / a + EPS:
                    continue
                if c <= 2 * a:
                    continue
                total += 1
                stats = exact_ratio_first_period((a, b, c))
                if best is None or stats["ratio"] > best["ratio"] + EPS:
                    best = stats
    return {"count": total, "best": best}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("count-range", "one-anchor", "triples"), required=True)
    parser.add_argument("--a-start", type=int)
    parser.add_argument("--a-end", type=int)
    parser.add_argument("--max-a", type=int, default=100)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.mode == "count-range":
        if args.a_start is None or args.a_end is None:
            raise SystemExit("--a-start and --a-end are required for count-range")
        payload = count_range(args.a_start, args.a_end, args.max_a)
    elif args.mode == "one-anchor":
        payload = one_anchor_count(args.max_a)
    else:
        payload = exact_dense_triples(args.max_a)

    if args.output is not None:
        args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
