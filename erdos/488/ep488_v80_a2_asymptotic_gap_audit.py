#!/usr/bin/env python3
"""Audit A2 asymptotic-gap and finite-window metrics.

Candidate A2 theorem surfaced by v79:

    delta(C,q) < D_C(n;q) / n

for reduced top-window connected high-defect components.  In the certificate
notation B = 2 D_C(n;q) / n, this is delta/B < 1/2.

This script audits that candidate and the induced finite-window ratio cutoff/n
on existing census/certificate JSON files.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def frac(value: Any) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(str(value))


def rows_from_high_defect_json(path: Path) -> list[dict[str, Any]]:
    data = json.load(open(path, encoding="utf-8"))
    rows = []
    for row in data["high_defect_rows"]:
        cert = row["certificate"]
        if "B" not in cert or "delta" not in cert:
            continue
        rows.append(
            {
                "source": str(path),
                "q": int(row["q"]),
                "n": int(row["n"]),
                "size": int(row["size"]),
                "epsilon": row["epsilon"],
                "B": frac(cert["B"]),
                "delta": frac(cert["delta"]),
                "delta_over_B": frac(cert["delta_over_B"]),
                "eta": frac(cert["eta"]),
                "cutoff": int(cert["cutoff"]) if cert.get("cutoff") is not None else None,
                "best_over_B": frac(cert["best_over_B"]) if cert.get("best_over_B") else None,
                "kind": "exact_row",
            }
        )
    return rows


def rows_from_representative_json(path: Path) -> list[dict[str, Any]]:
    data = json.load(open(path, encoding="utf-8"))
    rows = []
    for row in data["representatives"]:
        if "B" not in row or "delta" not in row:
            continue
        rows.append(
            {
                "source": str(path),
                "q": int(row["q"]),
                "n": int(row["n"]),
                "size": int(row["size"]),
                "epsilon": row["epsilon_values"],
                "B": frac(row["B"]),
                "delta": frac(row["delta"]),
                "delta_over_B": frac(row["delta"]) / frac(row["B"]),
                "eta": frac(row["eta"]),
                "cutoff": int(row["cutoff"]) if row.get("cutoff") is not None else None,
                "best_over_B": frac(row["best_over_B"]) if row.get("best_over_B") else None,
                "kind": "representative",
            }
        )
    return rows


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    bad_half = [row for row in rows if row["delta_over_B"] >= Fraction(1, 2)]
    certified = [row for row in rows if row["cutoff"] is not None]
    max_delta = max(rows, key=lambda row: row["delta_over_B"]) if rows else None
    max_best = max(
        (row for row in rows if row["best_over_B"] is not None),
        key=lambda row: row["best_over_B"],
        default=None,
    )
    max_cutoff = max(
        certified,
        key=lambda row: Fraction(row["cutoff"], row["n"]),
        default=None,
    )
    return {
        "row_count": len(rows),
        "bad_delta_ge_half_count": len(bad_half),
        "max_delta_over_B": printable_row(max_delta, include_fraction="delta_over_B"),
        "max_best_over_B": printable_row(max_best, include_fraction="best_over_B"),
        "max_cutoff_over_n": printable_row(max_cutoff, include_fraction="cutoff_over_n"),
        "bad_delta_ge_half_rows": [printable_row(row, include_fraction="delta_over_B") for row in bad_half[:20]],
    }


def printable_row(row: dict[str, Any] | None, include_fraction: str) -> dict[str, Any] | None:
    if row is None:
        return None
    out = {
        "source": row["source"],
        "kind": row["kind"],
        "q": row["q"],
        "n": row["n"],
        "size": row["size"],
        "epsilon": row["epsilon"],
    }
    if include_fraction == "delta_over_B":
        out["delta_over_B"] = str(row["delta_over_B"])
        out["delta_over_D_over_n"] = str(2 * row["delta_over_B"])
    elif include_fraction == "best_over_B":
        out["best_over_B"] = str(row["best_over_B"])
    elif include_fraction == "cutoff_over_n":
        out["cutoff"] = row["cutoff"]
        out["cutoff_over_n"] = str(Fraction(row["cutoff"], row["n"]))
    return out


def singleton_counterexample() -> dict[str, str | int]:
    # Shows the asymptotic half-gap is not true for arbitrary top-window sets.
    q = 101
    a = 100
    n = 253
    D = 2  # multiples 100, 200
    delta = Fraction(1, a) - Fraction(1, a * q)
    D_over_n = Fraction(D, n)
    return {
        "q": q,
        "C": "{100}",
        "n": n,
        "D_C_n": D,
        "delta": str(delta),
        "D_C_n_over_n": str(D_over_n),
        "delta_over_D_C_n_over_n": str(delta / D_over_n),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--exact-json",
        action="append",
        default=[],
        help="Census JSON with high_defect_rows. May be repeated.",
    )
    parser.add_argument(
        "--representatives-json",
        action="append",
        default=[],
        help="Representative certificate JSON. May be repeated.",
    )
    parser.add_argument("--json-out", default="ep488_v80_a2_asymptotic_gap_audit.json")
    args = parser.parse_args()

    groups: dict[str, list[dict[str, Any]]] = {}
    all_rows = []
    for raw in args.exact_json:
        path = Path(raw)
        rows = rows_from_high_defect_json(path)
        groups[str(path)] = rows
        all_rows.extend(rows)
    for raw in args.representatives_json:
        path = Path(raw)
        rows = rows_from_representative_json(path)
        groups[str(path)] = rows
        all_rows.extend(rows)

    result = {
        "sources": list(groups),
        "by_source": {source: summarize(rows) for source, rows in groups.items()},
        "combined": summarize(all_rows),
        "singleton_counterexample_to_unconditional_gap": singleton_counterexample(),
    }

    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    combined = result["combined"]
    print(
        f"rows={combined['row_count']} bad_delta_ge_half={combined['bad_delta_ge_half_count']} "
        f"max_delta={combined['max_delta_over_B']} "
        f"max_cutoff={combined['max_cutoff_over_n']}"
    )
    print(f"singleton_counterexample={result['singleton_counterexample_to_unconditional_gap']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
