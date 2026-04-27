from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def iter_rows(payload: Any, path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not isinstance(payload, dict):
        return rows

    if "rows" in payload and isinstance(payload["rows"], list):
        for row in payload["rows"]:
            if isinstance(row, dict):
                out = dict(row)
                out["_source"] = str(path)
                rows.append(out)
        return rows

    if "status" in payload:
        out = dict(payload)
        out["_source"] = str(path)
        rows.append(out)
    return rows


def status_of(row: dict[str, Any]) -> str:
    status = row.get("status")
    if isinstance(status, str):
        return status.lower()
    sat = row.get("sat")
    if sat is True:
        return "sat"
    if sat is False:
        return "unsat"
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregate EP617 SAT result JSON files.")
    parser.add_argument("--results", type=Path, default=Path("erdos/617/results"))
    parser.add_argument("--glob", default="*.json")
    parser.add_argument("--out", type=Path, default=Path("erdos/617/results/aggregate_sat_results.json"))
    args = parser.parse_args()

    all_rows: list[dict[str, Any]] = []
    for path in sorted(args.results.glob(args.glob)):
        payload = read_json(path)
        if payload is None:
            continue
        all_rows.extend(iter_rows(payload, path))

    counts: dict[str, int] = {}
    by_family: dict[str, dict[str, int]] = {}
    for row in all_rows:
        status = status_of(row)
        counts[status] = counts.get(status, 0) + 1
        source = Path(str(row.get("_source", ""))).name
        family = source.split("_")[0] if "_" in source else source.split(".")[0]
        by_family.setdefault(family, {})
        by_family[family][status] = by_family[family].get(status, 0) + 1

    sat_rows = [row for row in all_rows if status_of(row) == "sat"]
    unsat_rows = [row for row in all_rows if status_of(row) == "unsat"]
    unknown_rows = [row for row in all_rows if status_of(row) == "unknown"]

    summary = {
        "result_files_scanned": len(list(args.results.glob(args.glob))),
        "rows": len(all_rows),
        "counts": counts,
        "by_family": by_family,
        "sat_rows": sat_rows[:20],
        "unsat_rows": unsat_rows[:20],
        "unknown_rows_sample": unknown_rows[:20],
    }
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
