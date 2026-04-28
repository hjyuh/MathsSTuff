#!/usr/bin/env python3
"""Analyze the EP-488 monotonicity prompt."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


EPS = 1e-12


@dataclass(frozen=True)
class WindowStats:
    ratio: float
    min_g: float
    max_g: float
    min_x: int
    max_x: int
    hit_count: int


def is_primitive(values: tuple[int, ...] | list[int]) -> bool:
    A = list(values)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True


def ratio_stats_window(A: tuple[int, ...]) -> tuple[WindowStats, np.ndarray]:
    M = A[-1]
    H = 10 * M
    hits = np.zeros(H + 1, dtype=np.uint8)
    for d in A:
        hits[d::d] = 1

    pos = np.flatnonzero(hits)
    i0 = int(np.searchsorted(pos, M, side="left"))
    pos2 = pos[i0:]
    counts = np.arange(i0 + 1, pos.size + 1, dtype=np.int32)

    ratios_hit = counts / pos2.astype(np.float64)
    max_i = int(np.argmax(ratios_hit))
    max_g = float(ratios_hit[max_i])
    max_x = int(pos2[max_i])

    rights = np.empty(pos2.size, dtype=np.int32)
    if pos2.size > 1:
        rights[:-1] = pos2[1:] - 1
    rights[-1] = H
    ratios_gap = counts / rights.astype(np.float64)
    min_i = int(np.argmin(ratios_gap))
    min_g = float(ratios_gap[min_i])
    min_x = int(rights[min_i])

    return WindowStats(
        ratio=max_g / (2.0 * min_g),
        min_g=min_g,
        max_g=max_g,
        min_x=min_x,
        max_x=max_x,
        hit_count=int(pos.size),
    ), pos


def lcm2(a: int, b: int) -> int:
    from math import gcd

    return a * b // gcd(a, b)


def ratio_stats_first_period(A: tuple[int, ...]) -> dict:
    M = A[-1]
    L = 1
    for a in A:
        L = lcm2(L, a)
    H = M + L
    hits = np.zeros(H + 1, dtype=np.uint8)
    for d in A:
        hits[d::d] = 1
    pos = np.flatnonzero(hits)
    i0 = int(np.searchsorted(pos, M, side="left"))
    pos2 = pos[i0:]
    counts = np.arange(i0 + 1, pos.size + 1, dtype=np.int32)
    ratios_hit = counts / pos2.astype(np.float64)
    max_i = int(np.argmax(ratios_hit))
    max_g = float(ratios_hit[max_i])
    max_x = int(pos2[max_i])
    rights = np.empty(pos2.size, dtype=np.int32)
    if pos2.size > 1:
        rights[:-1] = pos2[1:] - 1
    rights[-1] = H
    ratios_gap = counts / rights.astype(np.float64)
    min_i = int(np.argmin(ratios_gap))
    min_g = float(ratios_gap[min_i])
    min_x = int(rights[min_i])
    return {
        "A": list(A),
        "L": int(L),
        "ratio": max_g / (2.0 * min_g),
        "min_g": min_g,
        "max_g": max_g,
        "min_x": min_x,
        "max_x": max_x,
    }


def s1(A: tuple[int, ...]) -> float:
    return sum(1.0 / a for a in A)


def consecutive_baseline(a: int, k: int, cache: dict[tuple[int, int], WindowStats]) -> WindowStats | None:
    if a < k:
        return None
    key = (a, k)
    if key not in cache:
        A = tuple(range(a, a + k))
        assert is_primitive(A)
        cache[key] = ratio_stats_window(A)[0]
    return cache[key]


def analyze_set(A: tuple[int, ...], cache: dict[tuple[int, int], WindowStats]) -> dict:
    stats, pos = ratio_stats_window(A)
    a = A[0]
    k = len(A)
    M = A[-1]
    x0 = 2 * a - 1
    legal_2a1 = x0 >= M
    F_x0 = int(np.searchsorted(pos, x0, side="right"))
    G_x0 = F_x0 / x0
    h = sum(1 for b in A if b <= x0)
    s1_val = s1(A)
    baseline = consecutive_baseline(a, k, cache)

    row = {
        "A": list(A),
        "a": a,
        "k": k,
        "M": M,
        "ratio": stats.ratio,
        "min_x": stats.min_x,
        "max_x": stats.max_x,
        "min_g": stats.min_g,
        "max_g": stats.max_g,
        "x0": x0,
        "x0_legal": legal_2a1,
        "F_2a_minus_1": F_x0,
        "G_2a_minus_1": G_x0,
        "h": h,
        "S1": s1_val,
        "h_threshold_passes": h * (2 * a + 1) > k * (2 * a - 1),
        "actual_2a1_beats_S1": (2.0 * G_x0) > s1_val + EPS,
        "min_at_2a_minus_1": legal_2a1 and stats.min_x == x0,
        "min_at_M": stats.min_x == M,
        "min_at_max_M_2a1": stats.min_x == max(M, x0),
        "min_at_2M_minus_1": stats.min_x == 2 * M - 1,
        "baseline_defined": baseline is not None,
        "baseline_ratio": None if baseline is None else baseline.ratio,
        "monotonicity_gap": None if baseline is None else baseline.ratio - stats.ratio,
        "monotonicity_holds": None if baseline is None else stats.ratio <= baseline.ratio + EPS,
    }
    return row


def primitive_pairs(max_b: int):
    for a in range(2, max_b):
        for b in range(a + 1, max_b + 1):
            if b % a != 0:
                yield (a, b)


def primitive_triples(max_c: int):
    for a in range(2, max_c - 1):
        for b in range(a + 1, max_c):
            if b % a == 0:
                continue
            for c in range(b + 1, max_c + 1):
                if c % a == 0 or c % b == 0:
                    continue
                yield (a, b, c)


def dense_k_sets(k: int, max_a: int):
    for a in range(2, max_a + 1):
        candidates = [x for x in range(a + 1, max_a + 1) if x % a != 0]
        target = 2.0 / a
        cur = [a]

        def dfs(start: int, s1_cur: float):
            need = k - len(cur)
            if need == 0:
                if s1_cur > target and is_primitive(cur):
                    yield tuple(cur)
                return

            n = len(candidates)
            if start + need > n:
                return

            max_add = 0.0
            for i in range(need):
                max_add += 1.0 / candidates[start + i]
            if s1_cur + max_add <= target:
                return

            for idx in range(start, n - need + 1):
                x = candidates[idx]
                ok = True
                for y in cur:
                    if x % y == 0 or y % x == 0:
                        ok = False
                        break
                if not ok:
                    continue
                cur.append(x)
                yield from dfs(idx + 1, s1_cur + 1.0 / x)
                cur.pop()

        yield from dfs(0, 1.0 / a)


def update_summary(summary: dict, row: dict) -> None:
    summary["total_sets"] += 1
    summary["x0_legal_count"] += int(row["x0_legal"])
    summary["x0_illegal_count"] += int(not row["x0_legal"])
    summary["min_at_2a_minus_1_count"] += int(row["min_at_2a_minus_1"])
    summary["min_at_M_count"] += int(row["min_at_M"])
    summary["min_at_max_M_2a1_count"] += int(row["min_at_max_M_2a1"])
    summary["min_at_2M_minus_1_count"] += int(row["min_at_2M_minus_1"])
    summary["h_threshold_pass_count"] += int(row["h_threshold_passes"])
    summary["actual_2a1_beats_S1_count"] += int(row["actual_2a1_beats_S1"])

    if row["baseline_defined"]:
        summary["baseline_defined_count"] += 1
        if row["monotonicity_holds"]:
            summary["monotonicity_hold_count"] += 1
        else:
            summary["monotonicity_violation_count"] += 1
            if len(summary["violations"]) < 10:
                summary["violations"].append(compact_row(row))

        gap = row["monotonicity_gap"]
        if summary["tightest_gap"] is None or gap < summary["tightest_gap"]["gap"] - EPS:
            summary["tightest_gap"] = {
                "gap": gap,
                "set": compact_row(row),
                "baseline_ratio": row["baseline_ratio"],
            }

        closeness = row["ratio"] / row["baseline_ratio"] if row["baseline_ratio"] else 0.0
        if len(summary["closest_to_baseline"]) < 10:
            summary["closest_to_baseline"].append((closeness, compact_row(row)))
            summary["closest_to_baseline"].sort(key=lambda item: item[0], reverse=True)
        elif closeness > summary["closest_to_baseline"][-1][0] + EPS:
            summary["closest_to_baseline"][-1] = (closeness, compact_row(row))
            summary["closest_to_baseline"].sort(key=lambda item: item[0], reverse=True)

    if not row["min_at_2a_minus_1"] and len(summary["moved_min_examples"]) < 10:
        summary["moved_min_examples"].append(compact_row(row))


def compact_row(row: dict) -> dict:
    out = {
        "A": row["A"],
        "ratio": round(row["ratio"], 12),
        "min_x": row["min_x"],
        "max_x": row["max_x"],
        "x0": row["x0"],
        "x0_legal": row["x0_legal"],
        "h": row["h"],
        "S1": round(row["S1"], 12),
        "G_2a_minus_1": round(row["G_2a_minus_1"], 12),
    }
    if row["baseline_ratio"] is not None:
        out["baseline_ratio"] = round(row["baseline_ratio"], 12)
        out["monotonicity_gap"] = round(row["monotonicity_gap"], 12)
    return out


def make_summary() -> dict:
    return {
        "total_sets": 0,
        "x0_legal_count": 0,
        "x0_illegal_count": 0,
        "min_at_2a_minus_1_count": 0,
        "min_at_M_count": 0,
        "min_at_max_M_2a1_count": 0,
        "min_at_2M_minus_1_count": 0,
        "h_threshold_pass_count": 0,
        "actual_2a1_beats_S1_count": 0,
        "baseline_defined_count": 0,
        "monotonicity_hold_count": 0,
        "monotonicity_violation_count": 0,
        "tightest_gap": None,
        "violations": [],
        "closest_to_baseline": [],
        "moved_min_examples": [],
    }


def targeted_hard_examples(cache: dict[tuple[int, int], WindowStats]) -> list[dict]:
    out = []
    examples = [
        (4, 6, 10, 14, 22, 26),
        (30, 42, 70, 105),
        (210, 330, 462, 770, 1155),
        (2, 3, 5, 31),
        (2, 3, 5, 7, 211),
    ]
    for A in examples:
        out.append(compact_row(analyze_set(tuple(A), cache)))
    return out


def normalize_summary(summary: dict) -> dict:
    out = dict(summary)
    out["closest_to_baseline"] = [
        {"ratio_over_baseline": round(score, 12), **row} for score, row in summary["closest_to_baseline"]
    ]
    return out


def explicit_counterexamples() -> list[dict]:
    pairs = [
        ((4, 6, 7), (4, 5, 6)),
        ((6, 9, 10, 11), (6, 7, 8, 9)),
        ((8, 12, 13, 14, 15), (8, 9, 10, 11, 12)),
        ((8, 20, 28, 29, 30, 31), (8, 9, 10, 11, 12, 13)),
    ]
    out = []
    for witness, baseline in pairs:
        w = ratio_stats_first_period(witness)
        b = ratio_stats_first_period(baseline)
        out.append(
            {
                "witness": w,
                "baseline": b,
                "gap": w["ratio"] - b["ratio"],
            }
        )
    return out


def build_report(payload: dict) -> str:
    lines: list[str] = []
    lines.append("# Monotonicity prompt analysis")
    lines.append("")
    lines.append("This scan uses the same operational ratio as the current Codex workspace:")
    lines.append("")
    lines.append("`ratio(A) = max_{x in [M,10M]} G(x) / (2 min_{x in [M,10M]} G(x))`, where `M = max(A)`.")
    lines.append("")
    lines.append("## Immediate structural issues")
    lines.append("")
    lines.append("- The conjecture as stated is ill-posed when `k > a`, because `{a, a+1, ..., a+k-1}` is then not primitive.")
    lines.append("- The proposed point `x = 2a-1` is outside the EP-488 range whenever `max(A) >= 2a`, because EP-488 requires `n >= max(A)`.")
    lines.append("- So the `2a-1` method can only be a direct proof strategy for sets contained in the strip `[a, 2a-1]`.")
    lines.append("")
    lines.append("## What works analytically")
    lines.append("")
    lines.append("- If every element of `A` lies in `[a, 2a-1]`, then `F(2a-1) = |A| = k` exactly, so `G(2a-1) = k/(2a-1)`.")
    lines.append("- Also `S1(A) = sum 1/b <= k/a`, hence `2G(2a-1) = 2k/(2a-1) > k/a >= S1(A) >= G(m)` for all `m`.")
    lines.append("- Therefore the `2a-1` argument extends from consecutive tuples to every primitive set with `max(A) <= 2a-1`.")
    lines.append("- This proves EP-488 on that whole strip, but it does not prove the monotonicity conjecture about the global ratio.")
    lines.append("")
    lines.append("## Computational scan")
    lines.append("")
    corpus = payload["corpus"]
    lines.append(f"Scanned {corpus['total_sets']} sets total:")
    lines.append(f"- pairs with `max <= {payload['parameters']['pair_max']}`")
    lines.append(f"- triples with `max <= {payload['parameters']['triple_max']}`")
    lines.append(f"- dense `k=4,5,6` primitive sets with `max <= {payload['parameters']['dense_max']}`")
    lines.append("")
    for family_name, family in payload["families"].items():
        lines.append(f"### {family_name}")
        lines.append("")
        lines.append(f"- total sets: {family['total_sets']}")
        lines.append(f"- `2a-1` legal in EP range: {family['x0_legal_count']}")
        lines.append(f"- `2a-1` illegal in EP range: {family['x0_illegal_count']}")
        lines.append(f"- `min G` exactly at `2a-1`: {family['min_at_2a_minus_1_count']}")
        lines.append(f"- `h`-threshold passes: {family['h_threshold_pass_count']}")
        lines.append(f"- actual `2G(2a-1) > S1` passes: {family['actual_2a1_beats_S1_count']}")
        lines.append(f"- monotonicity comparison defined (`a >= k`): {family['baseline_defined_count']}")
        lines.append(f"- monotonicity holds in scan: {family['monotonicity_hold_count']}")
        lines.append(f"- monotonicity violations found: {family['monotonicity_violation_count']}")
        if family["tightest_gap"] is not None:
            lines.append(
                f"- tightest monotonicity gap: {family['tightest_gap']['gap']:.12f} at `{family['tightest_gap']['set']['A']}`"
            )
        lines.append("")
    lines.append("## Explicit counterexamples")
    lines.append("")
    for item in payload["counterexamples"]:
        w = item["witness"]
        b = item["baseline"]
        lines.append(
            f"- `{w['A']}` beats consecutive `{b['A']}` on the full first period: "
            f"{w['ratio']:.12f} > {b['ratio']:.12f} (gap {item['gap']:.12f})"
        )
    lines.append("")
    lines.append("## Targeted examples where `min G` moves")
    lines.append("")
    for row in payload["targeted_examples"]:
        lines.append(
            f"- `{row['A']}`: `x0=2a-1={row['x0']}` legal={row['x0_legal']}, but `min_x={row['min_x']}`, `ratio={row['ratio']:.12f}`"
        )
    lines.append("")
    lines.append("## Conclusion")
    lines.append("")
    lines.append("- The monotonicity conjecture is false. Small full-period counterexample: `{4,6,7}` has ratio `11/16 = 0.6875`, while consecutive `{4,5,6}` has ratio `7/12 = 0.583333...`.")
    lines.append("- The prompt's original `2a-1` strategy does not extend to the general case, mainly because `2a-1` is usually not even in the admissible range once some element is `>= 2a`.")
    lines.append("- Computationally, `min G` is not universally at `2a-1`; it often moves far to the right for non-consecutive sets.")
    lines.append("- The viable positive statement is narrower: the `2a-1` proof works cleanly for the full strip `max(A) <= 2a-1`.")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pair-max", type=int, default=500)
    parser.add_argument("--triple-max", type=int, default=180)
    parser.add_argument("--dense-max", type=int, default=40)
    parser.add_argument(
        "--json-out",
        type=Path,
        default=Path("C:/Users/z20ma/OneDrive/Documents/!math/erdos/488/codex-monotonicity-results.json"),
    )
    parser.add_argument(
        "--report-out",
        type=Path,
        default=Path("C:/Users/z20ma/OneDrive/Documents/!math/erdos/488/codex-monotonicity-results.md"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cache: dict[tuple[int, int], WindowStats] = {}

    families = {
        "pairs_max_500": make_summary(),
        "triples_max_180": make_summary(),
        "dense_k4_max_40": make_summary(),
        "dense_k5_max_40": make_summary(),
        "dense_k6_max_40": make_summary(),
    }

    for A in primitive_pairs(args.pair_max):
        update_summary(families["pairs_max_500"], analyze_set(A, cache))
    for A in primitive_triples(args.triple_max):
        update_summary(families["triples_max_180"], analyze_set(A, cache))
    for A in dense_k_sets(4, args.dense_max):
        update_summary(families["dense_k4_max_40"], analyze_set(A, cache))
    for A in dense_k_sets(5, args.dense_max):
        update_summary(families["dense_k5_max_40"], analyze_set(A, cache))
    for A in dense_k_sets(6, args.dense_max):
        update_summary(families["dense_k6_max_40"], analyze_set(A, cache))

    normalized = {name: normalize_summary(summary) for name, summary in families.items()}
    total_sets = sum(item["total_sets"] for item in normalized.values())
    total_baseline = sum(item["baseline_defined_count"] for item in normalized.values())
    total_holds = sum(item["monotonicity_hold_count"] for item in normalized.values())
    total_violations = sum(item["monotonicity_violation_count"] for item in normalized.values())

    payload = {
        "parameters": {
            "pair_max": args.pair_max,
            "triple_max": args.triple_max,
            "dense_max": args.dense_max,
        },
        "corpus": {
            "total_sets": total_sets,
            "baseline_defined_total": total_baseline,
            "monotonicity_hold_total": total_holds,
            "monotonicity_violation_total": total_violations,
        },
        "families": normalized,
        "counterexamples": explicit_counterexamples(),
        "targeted_examples": targeted_hard_examples(cache),
    }

    report = build_report(payload)
    args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report_out.write_text(report + "\n", encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
