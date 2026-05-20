#!/usr/bin/env python3
"""EP-488 v70 automatic no-vertex-correction A4 motif certificate.

For a normalized pure-cycle motif, this proves a sufficient condition:

1. no q-excluded correction can occur in any positive vertex term throughout
   the top-window realization interval;
2. the raw host lower bound at n beats a q-independent m-side envelope that
   allows every edge correction at denominator 2e.

This generalizes the v69 pentagon proof. Motifs not proved here may still be
safe; they just need sharper handling.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, floor, lcm
import argparse
import json


def edges(cycle: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(lcm(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle)))


def cyc_lcm(cycle: tuple[int, ...]) -> int:
    out = 1
    for a in cycle:
        out = lcm(out, a)
    return out


def bounds(cycle: tuple[int, ...]) -> tuple[Fraction, Fraction, int]:
    es = edges(cycle)
    lower = max(Fraction(max(cycle), 1), Fraction(max(es), 3))
    upper = Fraction(2 * min(cycle), 1)
    return lower, upper, max(es)


def vertex_correction_obstructions(cycle: tuple[int, ...]) -> list[dict[str, object]]:
    lower, upper, _ = bounds(cycle)
    obstructions = []
    # If lcm(ps,q) can be <= n, then p*h < 3*upper.
    for p in sorted(set(cycle)):
        max_h = ceil(Fraction(3 * upper, p)) - 1
        for h in range(2, max_h + 1):
            hp = h * p
            possible = [
                r
                for r in range(1, hp + 1)
                if Fraction(hp, upper) < r < Fraction(hp, lower)
            ]
            if possible:
                obstructions.append(
                    {
                        "p": p,
                        "h": h,
                        "hp": hp,
                        "r_interval": f"({hp}/{upper},{hp}/{lower})",
                        "possible_r": possible,
                    }
                )
    return obstructions


def raw_H(cycle: tuple[int, ...], y: int) -> int:
    return sum(y // p for p in cycle) - sum(y // e for e in edges(cycle))


def lower_B(cycle: tuple[int, ...]) -> dict[str, object]:
    lower, upper, emax = bounds(cycle)
    y_min = emax
    y_max = ceil(3 * upper) - 1
    rows = []
    worst = None
    for y in range(y_min, y_max + 1):
        H = raw_H(cycle, y)
        value = Fraction(2 * H, y + 1)
        row = {"y": y, "H_raw": H, "B_lower": str(value)}
        rows.append(row)
        if worst is None or value < worst[0]:
            worst = (value, row)
    assert worst is not None
    return {
        "lower": str(lower),
        "upper": str(upper),
        "edge_max": emax,
        "y_min": y_min,
        "y_max": y_max,
        "B_lower": str(worst[0]),
        "worst_y": worst[1],
        "rows": rows,
    }


def A(cycle: tuple[int, ...], k: int) -> int:
    es = edges(cycle)
    return (
        sum(k // p for p in cycle)
        - sum(k // e for e in es)
        + sum(k // (2 * e) for e in es)
        + k // cyc_lcm(cycle)
    )


def prove(cycle: tuple[int, ...], period_cap: int) -> dict[str, object]:
    lower, upper, emax = bounds(cycle)
    obstructions = vertex_correction_obstructions(cycle)
    bdata = lower_B(cycle)
    B0 = Fraction(bdata["B_lower"])
    denoms = list(cycle) + list(edges(cycle)) + [2 * e for e in edges(cycle)] + [cyc_lcm(cycle)]
    period = 1
    for d in denoms:
        period = lcm(period, d)
    slope = (
        sum(Fraction(1, p) for p in cycle)
        - sum(Fraction(1, e) for e in edges(cycle))
        + sum(Fraction(1, 2 * e) for e in edges(cycle))
        + Fraction(1, cyc_lcm(cycle))
    )
    row: dict[str, object] = {
        "ordered_cycle": list(cycle),
        "normalized_cycle": sorted(cycle),
        "length": len(cycle),
        "bounds": {"lower": str(lower), "upper": str(upper), "edge_max": emax},
        "vertex_obstructions": obstructions[:20],
        "vertex_obstruction_count": len(obstructions),
        "lower_B": bdata,
        "period": period,
        "slope": str(slope),
        "status": "unknown",
    }
    if obstructions:
        row["status"] = "vertex_correction_possible"
        return row
    if slope > B0:
        row["status"] = "slope_exceeds_B"
        return row
    if period > period_cap:
        row["status"] = "period_too_large"
        return row
    worst = None
    failures = []
    for k in range(emax, emax + period):
        value = A(cycle, k)
        ratio = Fraction(value, k)
        margin = B0 * k - value
        item = {"k": k, "A": value, "A_over_k": str(ratio), "margin": str(margin)}
        if worst is None or margin < worst[0]:
            worst = (margin, item)
        if margin < 0:
            failures.append(item)
            if len(failures) >= 20:
                break
    row["worst_period_row"] = worst[1] if worst else None
    row["failures"] = failures
    row["status"] = "proved" if not failures else "period_failure"
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--motifs-json", default="ep488_v63_a4_normalized_cycle_motifs_len16.json")
    parser.add_argument("--period-cap", type=int, default=2_000_000)
    parser.add_argument("--max-length", type=int, default=None)
    parser.add_argument("--json-out", default="ep488_v70_a4_no_vertex_correction_bounds.json")
    args = parser.parse_args()

    data = json.load(open(args.motifs_json, encoding="utf-8"))
    rows = []
    counts: dict[str, int] = {}
    for motif in data["motifs"]:
        if args.max_length is not None and int(motif["length"]) > args.max_length:
            continue
        cycle = tuple(int(x) for x in motif["ordered_cycle"])
        row = prove(cycle, args.period_cap)
        rows.append(row)
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    result = {
        "motifs_json": args.motifs_json,
        "period_cap": args.period_cap,
        "status_counts": counts,
        "rows": rows,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"status_counts={counts}")
    for status in sorted(counts):
        for r in [x for x in rows if x["status"] == status][:8]:
            print(
                f"{status}: len={r['length']} norm={r['normalized_cycle']} "
                f"B0={r['lower_B']['B_lower']} slope={r['slope']} period={r['period']} "
                f"obs={r['vertex_obstruction_count']}"
            )
    return 1 if counts.get("period_failure") else 0


if __name__ == "__main__":
    raise SystemExit(main())
