#!/usr/bin/env python3
"""
Dense-set scans for EP-488 follow-up.

Implemented exactly:
1. R = S1 - 2*S2 on all dense primitive k-sets for:
   - k=4, max(A)<=100
   - k=5,6,7, max(A)<=50
2. Rigorous EP-488 certification for all dense primitive quadruples with
   max(A)<=100 using the tail bound
       2G(n) - G(m) >= R - 8/n
   together with an exact early-range scan up to n <= floor(8/R)+1.
3. Exact finite-horizon worst ratio for dense quadruples with max(A)<=100:
   first compute a rigorous per-set upper bound
       UB(A) = S1 / (2 * min_{d<=n<=N0} G(n)),
   where N0 = max(d, floor(8/R)+1), then exact-scan only those sets with
   UB(A) above the current best exact ratio.
4. Exact discrepancy C(x)=max_{1<=t<=10000*max(A)} |F(t)-delta*t| for:
   - all consecutive dense k-sets with k=4..7 in the requested max ranges
   - the exact dense quadruple slice min(A)>=70, max(A)<=100

Not implemented exhaustively:
- task 2 exact global max C over *all* dense quadruples max<=100
- task 3 exact global max C over *all* dense k=5,6,7 sets max<=50

Those discrepancy tasks are still computationally much larger than the exact R
and EP scans. The script reports the strongest exact discrepancy data obtained.
"""

from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction
from math import gcd
from pathlib import Path

import numpy as np


EPS = 1e-15


def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def is_primitive(A: tuple[int, ...] | list[int]) -> bool:
    A = list(A)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True


def density_ie(A: tuple[int, ...] | list[int]) -> float:
    A = list(A)
    total = 0.0
    k = len(A)
    for mask in range(1, 1 << k):
        sign = 1.0 if bin(mask).count("1") % 2 else -1.0
        L = 1
        first = True
        for i in range(k):
            if (mask >> i) & 1:
                if first:
                    L = A[i]
                    first = False
                else:
                    L = lcm2(L, A[i])
        total += sign / L
    return total


def exact_R(A: tuple[int, ...] | list[int]) -> Fraction:
    A = list(A)
    s1 = sum(Fraction(1, a) for a in A)
    s2 = sum(Fraction(1, lcm2(A[i], A[j])) for i in range(len(A)) for j in range(i + 1, len(A)))
    return s1 - 2 * s2


def exact_ratio_scan(A: tuple[int, ...] | list[int], horizon: int) -> dict:
    A = list(A)
    M = max(A)
    hits = np.zeros(horizon + 1, dtype=np.uint8)
    for d in A:
        hits[d::d] = 1

    pos = np.flatnonzero(hits)
    i0 = int(np.searchsorted(pos, M, side="left"))
    pos2 = pos[i0:]
    counts = np.arange(i0 + 1, pos.size + 1, dtype=np.int64)
    ratios = counts / pos2.astype(np.float64)
    suffix = np.maximum.accumulate(ratios[::-1])[::-1]

    denom = pos2[1:] - 1
    curr = counts[:-1].astype(np.float64)
    vals = suffix[1:] / (2.0 * (curr / denom.astype(np.float64)))
    j = int(np.argmax(vals))
    target = float(suffix[j + 1])
    rel = int(np.argmax(ratios[j + 1 :] >= target - EPS))
    m_arg = int(pos2[j + 1 + rel])
    return {
        "ratio": float(vals[j]),
        "n_argmax": int(denom[j]),
        "m_argmax": m_arg,
        "future_G": target,
        "current_G": float(curr[j] / denom[j]),
    }


def discrepancy_horizon_np(A: tuple[int, ...] | list[int], horizon: int) -> dict:
    A = list(A)
    delta = density_ie(A)
    hit = np.zeros(horizon + 1, dtype=np.uint8)
    for a in A:
        hit[a::a] = 1
    running = np.cumsum(hit, dtype=np.int32)
    x = np.arange(horizon + 1, dtype=np.float64)
    disc = np.abs(running - delta * x)
    idx = int(np.argmax(disc))
    return {"C": float(disc[idx]), "argmax": idx, "delta": float(delta)}


def dense_recursion(k: int, maxA: int, visitor) -> None:
    for a in range(3, maxA + 1):
        cands = [x for x in range(a + 1, maxA + 1) if x % a != 0]
        target = 2.0 / a
        cur = [a]

        def dfs(start: int, s1: float, s2: float) -> None:
            need = k - len(cur)
            if need == 0:
                if s1 > target:
                    visitor(tuple(cur), s1, s2)
                return
            n = len(cands)
            if start + need > n:
                return
            max_add = 0.0
            for i in range(need):
                max_add += 1.0 / cands[start + i]
            if s1 + max_add <= target:
                return
            for idx in range(start, n - need + 1):
                x = cands[idx]
                add_s2 = 0.0
                ok = True
                for y in cur:
                    if x % y == 0:
                        ok = False
                        break
                    add_s2 += gcd(x, y) / (x * y)
                if not ok:
                    continue
                cur.append(x)
                dfs(idx + 1, s1 + 1.0 / x, s2 + add_s2)
                cur.pop()

        dfs(0, 1.0 / a, 0.0)


def task_R_scan(k: int, maxA: int) -> dict:
    total = 0
    neg = 0
    min_R = float("inf")
    min_set: tuple[int, ...] | None = None
    first_neg: tuple[int, ...] | None = None
    first_neg_R = None

    def visit(A: tuple[int, ...], s1: float, s2: float) -> None:
        nonlocal total, neg, min_R, min_set, first_neg, first_neg_R
        total += 1
        R = s1 - 2.0 * s2
        if R < min_R:
            min_R = R
            min_set = A
        if R <= 0:
            neg += 1
            if first_neg is None:
                first_neg = A
                first_neg_R = R

    t0 = time.time()
    dense_recursion(k, maxA, visit)
    exact_min_R = None if min_set is None else exact_R(min_set)
    exact_first_neg_R = None if first_neg is None else exact_R(first_neg)
    return {
        "k": k,
        "maxA": maxA,
        "dense_count": total,
        "nonpositive_R_count": neg,
        "min_R": min_R,
        "min_R_set": min_set,
        "min_R_exact": None if exact_min_R is None else str(exact_min_R),
        "first_nonpositive_set": first_neg,
        "first_nonpositive_R": first_neg_R,
        "first_nonpositive_R_exact": None if exact_first_neg_R is None else str(exact_first_neg_R),
        "elapsed_seconds": round(time.time() - t0, 3),
    }


def task_quad_ep_exact(maxA: int) -> dict:
    total = 0
    certified = 0
    worst_upper = -1.0
    worst_upper_set: tuple[int, ...] | None = None
    worst_upper_n = None
    worst_upper_minG = None
    candidate_sets: list[tuple[int, ...]] = []

    exact_best = {
        "ratio": 0.0,
        "A": None,
        "n_argmax": None,
        "m_argmax": None,
    }

    t0 = time.time()

    def visit(A: tuple[int, ...], s1: float, s2: float) -> None:
        nonlocal total, certified, worst_upper, worst_upper_set, worst_upper_n, worst_upper_minG
        R = s1 - 2.0 * s2
        N0 = max(A[-1], int(8.0 / R) + 1)
        hit = bytearray(N0 + 1)
        for v in A:
            for m in range(v, N0 + 1, v):
                hit[m] = 1
        running = 0
        minG = 10.0
        min_n = None
        for n in range(1, N0 + 1):
            running += hit[n]
            if n >= A[-1]:
                g = running / n
                if g < minG:
                    minG = g
                    min_n = n

        UB = s1 / (2.0 * minG)
        total += 1
        if UB < 1.0 - EPS:
            certified += 1
        if UB > worst_upper:
            worst_upper = UB
            worst_upper_set = A
            worst_upper_n = min_n
            worst_upper_minG = minG
        if UB > exact_best["ratio"] + EPS:
            candidate_sets.append(A)

    dense_recursion(4, maxA, visit)

    # Exact-scan only those sets whose rigorous upper bound exceeds the current exact best.
    filtered: list[tuple[int, ...]] = []
    exact_best = {"ratio": 0.0, "A": None, "n_argmax": None, "m_argmax": None}

    def collect_candidates(A: tuple[int, ...], s1: float, s2: float) -> None:
        R = s1 - 2.0 * s2
        N0 = max(A[-1], int(8.0 / R) + 1)
        hit = bytearray(N0 + 1)
        for v in A:
            for m in range(v, N0 + 1, v):
                hit[m] = 1
        running = 0
        minG = 10.0
        for n in range(1, N0 + 1):
            running += hit[n]
            if n >= A[-1]:
                g = running / n
                if g < minG:
                    minG = g
        UB = s1 / (2.0 * minG)
        if UB > exact_best["ratio"] + EPS:
            filtered.append(A)

    # seed with known hard family
    seed = (97, 98, 99, 100)
    seed_res = exact_ratio_scan(seed, 10000 * seed[-1])
    exact_best = {"ratio": seed_res["ratio"], "A": seed, "n_argmax": seed_res["n_argmax"], "m_argmax": seed_res["m_argmax"]}
    dense_recursion(4, maxA, collect_candidates)

    seen = set()
    exact_candidates = []
    for A in filtered:
        if A not in seen:
            seen.add(A)
            exact_candidates.append(A)

    for A in exact_candidates:
        res = exact_ratio_scan(A, 10000 * A[-1])
        if res["ratio"] > exact_best["ratio"] + EPS:
            exact_best = {
                "ratio": res["ratio"],
                "A": A,
                "n_argmax": res["n_argmax"],
                "m_argmax": res["m_argmax"],
            }

    return {
        "dense_count": total,
        "certified_count": certified,
        "worst_upper_bound": worst_upper,
        "worst_upper_set": worst_upper_set,
        "worst_upper_n": worst_upper_n,
        "worst_upper_minG": worst_upper_minG,
        "exact_candidate_count": len(exact_candidates),
        "exact_worst_ratio": exact_best["ratio"],
        "exact_worst_set": exact_best["A"],
        "exact_worst_n": exact_best["n_argmax"],
        "exact_worst_m": exact_best["m_argmax"],
        "elapsed_seconds": round(time.time() - t0, 3),
    }


def task_consecutive_C(k: int, maxA: int) -> dict:
    best_C = -1.0
    best_set = None
    best_arg = None
    best_delta = None
    t0 = time.time()
    for a in range(3, maxA - k + 2):
        A = tuple(range(a, a + k))
        if not is_primitive(A):
            continue
        if sum(1.0 / x for x in A) <= 2.0 / A[0]:
            continue
        res = discrepancy_horizon_np(A, 10000 * A[-1])
        if res["C"] > best_C:
            best_C = res["C"]
            best_set = A
            best_arg = res["argmax"]
            best_delta = res["delta"]
    return {
        "k": k,
        "maxA": maxA,
        "best_C": best_C,
        "best_set": best_set,
        "best_argmax": best_arg,
        "best_delta": best_delta,
        "elapsed_seconds": round(time.time() - t0, 3),
    }


def task_quad_C_slice(min_a: int, maxA: int) -> dict:
    count = 0
    best_C = -1.0
    best_set = None
    best_arg = None
    best_delta = None
    t0 = time.time()

    def visit(A: tuple[int, ...], s1: float, s2: float) -> None:
        nonlocal count, best_C, best_set, best_arg, best_delta
        if A[0] < min_a:
            return
        count += 1
        res = discrepancy_horizon_np(A, 10000 * A[-1])
        if res["C"] > best_C:
            best_C = res["C"]
            best_set = A
            best_arg = res["argmax"]
            best_delta = res["delta"]

    dense_recursion(4, maxA, visit)
    return {
        "min_a": min_a,
        "maxA": maxA,
        "dense_count": count,
        "best_C": best_C,
        "best_set": best_set,
        "best_argmax": best_arg,
        "best_delta": best_delta,
        "elapsed_seconds": round(time.time() - t0, 3),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.time()

    r4 = task_R_scan(4, 100)
    r5 = task_R_scan(5, 50)
    r6 = task_R_scan(6, 50)
    r7 = task_R_scan(7, 50)
    quad_ep = task_quad_ep_exact(100)
    c4_consec = task_consecutive_C(4, 100)
    c5_consec = task_consecutive_C(5, 50)
    c6_consec = task_consecutive_C(6, 50)
    c7_consec = task_consecutive_C(7, 50)
    c4_slice = task_quad_C_slice(70, 100)

    payload = {
        "R_scans": {
            "k4_max100": r4,
            "k5_max50": r5,
            "k6_max50": r6,
            "k7_max50": r7,
        },
        "dense_quad_ep": quad_ep,
        "C_consecutive": {
            "k4_max100": c4_consec,
            "k5_max50": c5_consec,
            "k6_max50": c6_consec,
            "k7_max50": c7_consec,
        },
        "C_quad_slice_min70": c4_slice,
        "totals": {
            "elapsed_seconds": round(time.time() - started, 3),
        },
    }

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
