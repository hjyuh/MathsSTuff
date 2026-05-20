#!/usr/bin/env python3
"""EP-488 v75 compact A4 jump-period certificate.

This is the same mathematical certificate as v73, but it avoids storing the
full finite y-table for the lower-bound side. It keeps only the worst y row and
the correction-state summary. That makes larger frontiers practical while
remaining rerunnable for full verification.
"""

from __future__ import annotations

from collections import Counter
from collections import defaultdict
from fractions import Fraction
from math import ceil, lcm
import argparse
import json
import time

from ep488_v71_a4_vertex_correction_bounds import (
    A,
    bounds,
    correction_states,
    cyc_lcm,
    edges,
    max_vertex_loss_for_y,
    raw_H,
)
from ep488_v73_a4_jump_period_certificate import envelope_denoms, period_and_slope


def compact_lower_B(cycle: tuple[int, ...]) -> dict[str, object]:
    lower, upper, emax = bounds(cycle)
    state_data = correction_states(cycle)
    y_min = emax
    y_max = ceil(3 * upper) - 1
    worst = None
    for y in range(y_min, y_max + 1):
        raw = raw_H(cycle, y)
        loss, state = max_vertex_loss_for_y(state_data, y)
        H = raw - loss
        value = Fraction(2 * H, y + 1)
        row = {
            "y": y,
            "H_raw": raw,
            "max_vertex_loss": loss,
            "H_lower": H,
            "loss_state": state,
            "B_lower": str(value),
        }
        if worst is None or value < worst[0]:
            worst = (value, row)
    assert worst is not None
    return {
        "lower": str(lower),
        "upper": str(upper),
        "edge_max": emax,
        "correction_states": state_data,
        "y_min": y_min,
        "y_max": y_max,
        "B_lower": str(worst[0]),
        "worst_y": worst[1],
    }


def prove_compact(cycle: tuple[int, ...]) -> dict[str, object]:
    _, _, emax = bounds(cycle)
    bdata = compact_lower_B(cycle)
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

    scan = fast_jump_scan(cycle, emax, emax + period, B0)
    row.update(scan)
    row["status"] = "proved" if not scan["failures"] else "jump_failure"
    return row


def fast_jump_scan(cycle: tuple[int, ...], start: int, stop: int, B0: Fraction) -> dict[str, object]:
    positives, negatives = envelope_denoms(cycle)
    net: dict[int, int] = defaultdict(int)
    raw_events = 0
    for sign, denoms in ((1, positives), (-1, negatives)):
        for d in denoms:
            first = ((start + d - 1) // d) * d
            for k in range(first, stop, d):
                net[k] += sign
                if sign > 0:
                    raw_events += 1

    current_A = A(cycle, start)
    start_item = {
        "k": start,
        "A": current_A,
        "A_over_k": str(Fraction(current_A, start)),
        "margin": str(B0 * start - current_A),
    }
    worst = None
    failures = []
    checked = 1
    margin = B0 * start - current_A
    worst = (margin, start_item)
    if margin < 0:
        failures.append(start_item)

    for k in sorted(net):
        if k == start:
            continue
        current_A += net[k]
        if net[k] <= 0:
            continue
        checked += 1
        value = current_A
        margin = B0 * k - value
        item = {
            "k": k,
            "A": value,
            "A_over_k": str(Fraction(value, k)),
            "margin": str(margin),
        }
        if margin < worst[0]:
            worst = (margin, item)
        if margin < 0:
            failures.append(item)
            if len(failures) >= 20:
                break

    return {
        "jump_points_checked": checked,
        "raw_positive_events": raw_events,
        "event_points_total": len(net),
        "worst_jump_row": worst[1],
        "failures": failures,
    }


def load_existing(jsonl_path: str) -> dict[tuple[int, tuple[int, ...]], dict[str, object]]:
    rows = {}
    try:
        with open(jsonl_path, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                rows[(int(row["length"]), tuple(int(x) for x in row["ordered_cycle"]))] = row
    except FileNotFoundError:
        pass
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--motifs-json", default="ep488_v75_a4_normalized_cycle_motifs_len18.json")
    parser.add_argument("--min-length", type=int, default=18)
    parser.add_argument("--max-length", type=int, default=18)
    parser.add_argument("--jsonl-out", default="ep488_v75_a4_compact_jump_certificate_len18.jsonl")
    parser.add_argument("--summary-out", default="ep488_v75_a4_compact_jump_certificate_len18_summary.json")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--start-index", type=int, default=None, help="1-based index within the selected motif list")
    parser.add_argument("--end-index", type=int, default=None, help="inclusive 1-based index within the selected motif list")
    args = parser.parse_args()

    data = json.load(open(args.motifs_json, encoding="utf-8"))
    motifs = [
        m
        for m in data["motifs"]
        if (args.min_length is None or int(m["length"]) >= args.min_length)
        and (args.max_length is None or int(m["length"]) <= args.max_length)
    ]
    total_selected_before_index = len(motifs)
    if args.start_index is not None or args.end_index is not None:
        start = 1 if args.start_index is None else args.start_index
        end = len(motifs) if args.end_index is None else args.end_index
        motifs = motifs[start - 1 : end]
    completed = load_existing(args.jsonl_out) if args.resume else {}
    mode = "a" if args.resume else "w"
    start = time.time()
    with open(args.jsonl_out, mode, encoding="utf-8") as out:
        for idx, motif in enumerate(motifs, start=1):
            cycle = tuple(int(x) for x in motif["ordered_cycle"])
            key = (int(motif["length"]), cycle)
            if key in completed:
                continue
            row = prove_compact(cycle)
            row["motif_index"] = idx
            row["source_normalized_cycle"] = motif["normalized_cycle"]
            out.write(json.dumps(row, separators=(",", ":")) + "\n")
            out.flush()
            completed[key] = row
            print(
                f"{len(completed)}/{len(motifs)} status={row['status']} "
                f"period={row['period']} jumps={row.get('jump_points_checked')} "
                f"norm={row['normalized_cycle']}"
            )

    rows = [
        completed[(int(m["length"]), tuple(int(x) for x in m["ordered_cycle"]))]
        for m in motifs
        if (int(m["length"]), tuple(int(x) for x in m["ordered_cycle"])) in completed
    ]
    counts = Counter(r["status"] for r in rows)
    summary = {
        "motifs_json": args.motifs_json,
        "min_length": args.min_length,
        "max_length": args.max_length,
        "start_index": args.start_index,
        "end_index": args.end_index,
        "total_selected_before_index": total_selected_before_index,
        "selected_motifs": len(motifs),
        "completed": len(rows),
        "status_counts": dict(counts),
        "elapsed_seconds": time.time() - start,
        "rows": [
            {
                "motif_index": r.get("motif_index"),
                "status": r["status"],
                "length": r["length"],
                "normalized_cycle": r["normalized_cycle"],
                "period": r["period"],
                "slope": r["slope"],
                "B0": r["lower_B"]["B_lower"],
                "jump_points_checked": r.get("jump_points_checked"),
                "worst_jump_row": r.get("worst_jump_row"),
                "state_count": r["lower_B"]["correction_states"]["state_count"],
            }
            for r in rows
        ],
    }
    with open(args.summary_out, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(
        f"selected={len(motifs)} completed={len(rows)} status_counts={dict(counts)} "
        f"elapsed_seconds={summary['elapsed_seconds']:.2f}"
    )
    return 1 if counts.get("jump_failure") or counts.get("slope_exceeds_B") or len(rows) != len(motifs) else 0


if __name__ == "__main__":
    raise SystemExit(main())
