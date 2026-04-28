#!/usr/bin/env python3
"""Run extension tests on mined square-translate candidates.

Inputs are JSON outputs from pair_column_extend_mine.py.  The script extracts
candidate bicliques and applies the two low-height extension tests:

* fixed columns z_j: search for extra shifts N;
* fixed rows N_i: search for extra rational columns X.

This is deliberately a bounded triage tool, not a proof of nonexistence.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import extra_shift_from_columns
import fifth_column_crt_search
from square_translate_biclique_mine import verify


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def candidate_kind(row_count: int, col_count: int) -> str | None:
    if row_count >= 5 and col_count >= 5:
        return "K55"
    if row_count >= 5 and col_count >= 4:
        return "K5_4"
    if row_count >= 4 and col_count >= 5:
        return "K4_5"
    if row_count >= 4 and col_count >= 4:
        return "K4_4"
    if row_count >= 3 and col_count >= 5:
        return "K3_5"
    return None


def normalize_candidate(ns: list[int], zs: list[int], source: str) -> dict | None:
    ns = sorted(dict.fromkeys(int(n) for n in ns))
    zs = sorted(dict.fromkeys(int(z) for z in zs))
    kind = candidate_kind(len(ns), len(zs))
    if kind is None:
        return None
    check = verify(ns, zs)
    if not check["ok"]:
        return None
    return {
        "kind": kind,
        "N_values": ns,
        "z_values": zs,
        "deltas": [2 * z for z in zs],
        "source": source,
        "verification": {
            "ok": check["ok"],
            "num_N": check["num_N"],
            "num_z": check["num_z"],
        },
    }


def extract_candidates(paths: list[Path], max_candidates: int) -> list[dict]:
    candidates: list[dict] = []
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()

    def add_candidate(ns: list[int], zs: list[int], source: str) -> None:
        candidate = normalize_candidate(ns, zs, source)
        if candidate is None:
            return
        key = (tuple(candidate["N_values"]), tuple(candidate["z_values"]))
        if key in seen:
            return
        seen.add(key)
        candidates.append(candidate)

    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for hit in data.get("hits", []):
            add_candidate(hit.get("N_values", []), hit.get("z_values", []), f"{path.name}:hit")
        for index, rec in enumerate(data.get("best_subsets", []), start=1):
            ns = rec.get("N_values_sample", [])
            zs = rec.get("z_values", [])
            row_count = int(rec.get("row_count", len(ns)))
            # Keep the strongest exact slices from the sample.  For row_count>5
            # this uses the smallest displayed rows; the verification step
            # makes sure the slice is a genuine biclique.
            for rows_needed in (5, 4, 3):
                if row_count >= rows_needed and len(ns) >= rows_needed:
                    add_candidate(ns[:rows_needed], zs, f"{path.name}:best_subset:{index}")
                    break
    candidates.sort(
        key=lambda c: (
            {"K55": 0, "K5_4": 1, "K4_5": 2, "K4_4": 3, "K3_5": 4}.get(c["kind"], 9),
            -len(c["N_values"]),
            -len(c["z_values"]),
            c["N_values"],
            c["z_values"],
        )
    )
    return candidates[:max_candidates]


def run_extra_shift(candidate: dict, args: argparse.Namespace) -> dict | None:
    zs = candidate["z_values"]
    if len(zs) < 4:
        return None
    scan = extra_shift_from_columns.scan(
        zs,
        candidate["N_values"],
        args.base_index,
        args.shift_prime_bound,
        args.shift_max_classes,
        args.shift_m_bound,
        args.max_hits,
    )
    known = set(candidate["N_values"])
    new_hits = [hit for hit in scan["hits"] if hit["shift"] not in known]
    return {
        "tested": scan["tested"],
        "classes": scan["classes"],
        "modulus": scan["modulus"],
        "hit_count": len(scan["hits"]),
        "new_hit_count": len(new_hits),
        "hits": scan["hits"],
        "new_hits": new_hits,
        "stopped_early": scan["stopped_early"],
    }


def run_fifth_column(candidate: dict, args: argparse.Namespace) -> dict | None:
    if len(candidate["N_values"]) < 4:
        return None
    seed = fifth_column_crt_search.SimpleSeed(
        candidate["N_values"], candidate["deltas"]
    )
    scan = fifth_column_crt_search.search(
        seed,
        args.column_prime_bound,
        args.column_height_bound,
        args.column_max_classes,
    )
    return {
        "height_bound": scan["height_bound"],
        "crt_modulus": scan["crt_modulus"],
        "crt_class_count": scan["crt_class_count"],
        "candidate_count": scan["candidate_count"],
        "hit_count": scan["hit_count"],
        "new_hit_count": scan["new_hit_count"],
        "hits": scan["hits"],
        "new_hits": scan["new_hits"],
        "used_primes": scan["used_primes"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Extend mined EP885 candidates.")
    parser.add_argument("--mine-json", action="append", type=Path, required=True)
    parser.add_argument("--max-candidates", type=int, default=12)
    parser.add_argument("--base-index", type=int, default=0)
    parser.add_argument("--shift-m-bound", type=int, default=10_000_000_000)
    parser.add_argument("--shift-prime-bound", type=int, default=120)
    parser.add_argument("--shift-max-classes", type=int, default=300_000)
    parser.add_argument("--column-height-bound", type=int, default=5000)
    parser.add_argument("--column-prime-bound", type=int, default=160)
    parser.add_argument("--column-max-classes", type=int, default=300_000)
    parser.add_argument("--max-hits", type=int, default=20)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    started = dt.datetime.now(dt.UTC)
    candidates = extract_candidates(args.mine_json, args.max_candidates)
    records = []
    for index, candidate in enumerate(candidates, start=1):
        record = dict(candidate)
        record["index"] = index
        record["extra_shift"] = run_extra_shift(candidate, args)
        record["fifth_column"] = run_fifth_column(candidate, args)
        records.append(record)

    finished = dt.datetime.now(dt.UTC)
    payload = {
        "script": "extend_mined_candidates.py",
        "argv": sys.argv[1:],
        "started_utc": started.isoformat(),
        "finished_utc": finished.isoformat(),
        "elapsed_seconds": (finished - started).total_seconds(),
        "candidate_count": len(records),
        "records": records,
        "positive_records": [
            rec
            for rec in records
            if (rec.get("extra_shift") and rec["extra_shift"]["new_hit_count"])
            or (rec.get("fifth_column") and rec["fifth_column"]["new_hit_count"])
        ],
    }
    write_json(args.out, payload)
    print(
        json.dumps(
            {
                "elapsed_seconds": payload["elapsed_seconds"],
                "candidate_count": payload["candidate_count"],
                "positive_count": len(payload["positive_records"]),
                "kinds": [rec["kind"] for rec in records],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
