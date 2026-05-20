#!/usr/bin/env python3
"""EP-488 v73 jump-point A4 pure-cycle period certificate.

This keeps the v71 correction-aware lower bound, but replaces the full period
scan by a jump-point scan. For the envelope

    A(k) = sum floor(k/p_i) - sum floor(k/e_i)
         + sum floor(k/(2e_i)) + floor(k/L),

the margin M(k)=B0*k-A(k) can only decrease at integers where the positive
floor jumps outnumber the negative floor jumps. It is therefore enough to
check k_min and those positive-net jump points in one period.
"""

from __future__ import annotations

from fractions import Fraction
from math import lcm
import argparse
import json

from ep488_v71_a4_vertex_correction_bounds import (
    A,
    bounds,
    cyc_lcm,
    edges,
    lower_B,
)


def envelope_denoms(cycle: tuple[int, ...]) -> tuple[list[int], list[int]]:
    es = list(edges(cycle))
    positives = list(cycle) + [2 * e for e in es] + [cyc_lcm(cycle)]
    negatives = es
    return positives, negatives


def period_and_slope(cycle: tuple[int, ...]) -> tuple[int, Fraction]:
    positives, negatives = envelope_denoms(cycle)
    period = 1
    for d in positives + negatives:
        period = lcm(period, d)
    slope = sum(Fraction(1, d) for d in positives) - sum(Fraction(1, d) for d in negatives)
    return period, slope


def jump_points(cycle: tuple[int, ...], start: int, stop: int) -> tuple[list[int], int]:
    positives, negatives = envelope_denoms(cycle)
    candidates = {start}
    raw_positive_events = 0
    for d in positives:
        first = ((start + d - 1) // d) * d
        for k in range(first, stop, d):
            candidates.add(k)
            raw_positive_events += 1
    filtered = []
    for k in candidates:
        delta = sum(1 for d in positives if k % d == 0) - sum(1 for d in negatives if k % d == 0)
        if k == start or delta > 0:
            filtered.append(k)
    return sorted(filtered), raw_positive_events


def prove(cycle: tuple[int, ...]) -> dict[str, object]:
    _, _, emax = bounds(cycle)
    bdata = lower_B(cycle)
    B0 = Fraction(bdata["B_lower"])
    period, slope = period_and_slope(cycle)
    row: dict[str, object] = {
        "ordered_cycle": list(cycle),
        "normalized_cycle": sorted(cycle),
        "length": len(cycle),
        "bounds": {"edge_max": emax},
        "lower_B": bdata,
        "period": period,
        "slope": str(slope),
        "status": "unknown",
    }
    if B0 <= 0:
        row["status"] = "nonpositive_B_lower"
        return row
    if slope > B0:
        row["status"] = "slope_exceeds_B"
        return row

    points, raw_events = jump_points(cycle, emax, emax + period)
    worst = None
    failures = []
    for k in points:
        value = A(cycle, k)
        margin = B0 * k - value
        item = {
            "k": k,
            "A": value,
            "A_over_k": str(Fraction(value, k)),
            "margin": str(margin),
        }
        if worst is None or margin < worst[0]:
            worst = (margin, item)
        if margin < 0:
            failures.append(item)
            if len(failures) >= 20:
                break
    row["jump_points_checked"] = len(points)
    row["raw_positive_events"] = raw_events
    row["worst_jump_row"] = worst[1] if worst else None
    row["failures"] = failures
    row["status"] = "proved" if not failures else "jump_failure"
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--motifs-json", default="ep488_v63_a4_normalized_cycle_motifs_len16.json")
    parser.add_argument("--min-length", type=int, default=None)
    parser.add_argument("--max-length", type=int, default=13)
    parser.add_argument("--json-out", default="ep488_v73_a4_jump_period_certificate.json")
    args = parser.parse_args()

    data = json.load(open(args.motifs_json, encoding="utf-8"))
    rows = []
    counts: dict[str, int] = {}
    for motif in data["motifs"]:
        if args.min_length is not None and int(motif["length"]) < args.min_length:
            continue
        if args.max_length is not None and int(motif["length"]) > args.max_length:
            continue
        cycle = tuple(int(x) for x in motif["ordered_cycle"])
        row = prove(cycle)
        rows.append(row)
        counts[row["status"]] = counts.get(row["status"], 0) + 1

    result = {
        "motifs_json": args.motifs_json,
        "min_length": args.min_length,
        "max_length": args.max_length,
        "status_counts": counts,
        "rows": rows,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"status_counts={counts}")
    for status in sorted(counts):
        for r in [x for x in rows if x["status"] == status][:10]:
            print(
                f"{status}: len={r['length']} norm={r['normalized_cycle']} "
                f"B0={r['lower_B']['B_lower']} slope={r['slope']} period={r['period']} "
                f"jumps={r.get('jump_points_checked')}"
            )
    return 1 if counts.get("jump_failure") or counts.get("slope_exceeds_B") else 0


if __name__ == "__main__":
    raise SystemExit(main())
