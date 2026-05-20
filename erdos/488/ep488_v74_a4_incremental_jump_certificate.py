#!/usr/bin/env python3
"""EP-488 v74 incremental wrapper for the v73 A4 jump certificate.

The v73 checker writes only at the end. For larger frontiers this script writes
one JSONL row per motif as soon as it is checked, then writes a summary JSON at
the end. If a run is interrupted, the JSONL file preserves completed work.
"""

from __future__ import annotations

from collections import Counter
import argparse
import json
import time

from ep488_v73_a4_jump_period_certificate import prove


def key_for_row(row: dict[str, object]) -> tuple[int, tuple[int, ...]]:
    return int(row["length"]), tuple(int(x) for x in row["ordered_cycle"])


def load_existing(jsonl_path: str) -> dict[tuple[int, tuple[int, ...]], dict[str, object]]:
    rows = {}
    try:
        with open(jsonl_path, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                rows[key_for_row(row)] = row
    except FileNotFoundError:
        pass
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--motifs-json", default="ep488_v74_a4_normalized_cycle_motifs_len17.json")
    parser.add_argument("--min-length", type=int, default=17)
    parser.add_argument("--max-length", type=int, default=17)
    parser.add_argument("--jsonl-out", default="ep488_v74_a4_jump_certificate_len17.jsonl")
    parser.add_argument("--summary-out", default="ep488_v74_a4_jump_certificate_len17_summary.json")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--compact-summary", action="store_true")
    args = parser.parse_args()

    data = json.load(open(args.motifs_json, encoding="utf-8"))
    motifs = [
        m
        for m in data["motifs"]
        if (args.min_length is None or int(m["length"]) >= args.min_length)
        and (args.max_length is None or int(m["length"]) <= args.max_length)
    ]
    existing = load_existing(args.jsonl_out) if args.resume else {}
    mode = "a" if args.resume else "w"
    start = time.time()
    completed = dict(existing)
    with open(args.jsonl_out, mode, encoding="utf-8") as out:
        for idx, motif in enumerate(motifs, start=1):
            cycle = tuple(int(x) for x in motif["ordered_cycle"])
            key = (int(motif["length"]), cycle)
            if key in completed:
                continue
            row = prove(cycle)
            row["motif_index"] = idx
            row["source_normalized_cycle"] = motif["normalized_cycle"]
            out.write(json.dumps(row, separators=(",", ":")) + "\n")
            out.flush()
            completed[key] = row
            print(
                f"{len(completed)}/{len(motifs)} status={row['status']} "
                f"len={row['length']} period={row['period']} "
                f"jumps={row.get('jump_points_checked')} norm={row['normalized_cycle']}"
            )

    rows = [completed[(int(m["length"]), tuple(int(x) for x in m["ordered_cycle"]))] for m in motifs if (int(m["length"]), tuple(int(x) for x in m["ordered_cycle"])) in completed]
    counts = Counter(r["status"] for r in rows)
    summary_rows = rows
    if args.compact_summary:
        summary_rows = [
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
        ]

    summary = {
        "motifs_json": args.motifs_json,
        "min_length": args.min_length,
        "max_length": args.max_length,
        "compact_summary": args.compact_summary,
        "selected_motifs": len(motifs),
        "completed": len(rows),
        "status_counts": dict(counts),
        "elapsed_seconds": time.time() - start,
        "rows": summary_rows,
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
