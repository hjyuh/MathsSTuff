#!/usr/bin/env python3
"""Extend dense row-pairs in the square-translate graph.

This is a faster companion to square_translate_biclique_mine.py.  It first
finds pairs of shifts N_1,N_2 with many common columns z, then asks whether
some fixed subset of those columns has many *other* shifts as well.  This is
well suited to finding K_{3,5}, K_{4,5}, and K_{5,4} near-misses.
"""

from __future__ import annotations

import argparse
import datetime as dt
import itertools
import json
import sys
from pathlib import Path

from square_translate_biclique_mine import generate_graph, verify


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def build_column_index(rows: dict[int, tuple[int, ...]]) -> dict[int, frozenset[int]]:
    mutable: dict[int, list[int]] = {}
    for n, zs in rows.items():
        for z in zs:
            mutable.setdefault(z, []).append(n)
    return {z: frozenset(ns) for z, ns in mutable.items()}


def limited_combinations(values: list[int], size: int, limit: int):
    count = 0
    for combo in itertools.combinations(values, size):
        yield combo
        count += 1
        if limit > 0 and count >= limit:
            return


def main() -> None:
    parser = argparse.ArgumentParser(description="Extend dense square-translate row pairs.")
    parser.add_argument("--z-max", type=int, required=True)
    parser.add_argument("--n-max", type=int, required=True)
    parser.add_argument("--target-rows", type=int, default=5)
    parser.add_argument("--target-cols", type=int, default=5)
    parser.add_argument("--row-limit", type=int, default=5000)
    parser.add_argument("--max-pairs", type=int, default=2_000_000)
    parser.add_argument("--max-subsets-per-pair", type=int, default=200)
    parser.add_argument("--max-hits", type=int, default=20)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    start = dt.datetime.now(dt.UTC)
    rows, graph_meta = generate_graph(args.z_max, args.n_max, args.target_cols)
    col_index = build_column_index(rows)
    ordered = sorted(rows.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    if args.row_limit > 0:
        ordered = ordered[: args.row_limit]

    row_sets = [(n, frozenset(zs)) for n, zs in ordered]
    hits = []
    best_subsets: dict[tuple[int, ...], dict] = {}
    best_pairs = []
    tested_pairs = 0
    qualifying_pairs = 0
    tested_subsets = 0
    stopped_early = False

    for i in range(len(row_sets)):
        if stopped_early:
            break
        n1, zs1 = row_sets[i]
        for j in range(i + 1, len(row_sets)):
            tested_pairs += 1
            if tested_pairs > args.max_pairs:
                stopped_early = True
                break
            n2, zs2 = row_sets[j]
            common = sorted(zs1 & zs2)
            if len(common) < args.target_cols:
                continue
            qualifying_pairs += 1
            best_pairs.append({"N_pair": [n1, n2], "common_col_count": len(common), "z_sample": common[:20]})
            best_pairs.sort(key=lambda r: (-r["common_col_count"], r["N_pair"]))
            del best_pairs[50:]

            for cols in limited_combinations(common, args.target_cols, args.max_subsets_per_pair):
                tested_subsets += 1
                common_rows = set(col_index[cols[0]])
                for z in cols[1:]:
                    common_rows &= col_index[z]
                rows_for_cols = sorted(common_rows)
                key = tuple(cols)
                prior = best_subsets.get(key)
                if prior is None or len(rows_for_cols) > prior["row_count"]:
                    best_subsets[key] = {
                        "z_values": list(cols),
                        "row_count": len(rows_for_cols),
                        "N_values_sample": rows_for_cols[:20],
                    }
                if len(rows_for_cols) >= args.target_rows:
                    ns = rows_for_cols[: args.target_rows]
                    zs = list(cols)
                    hits.append(
                        {
                            "N_values": ns,
                            "z_values": zs,
                            "deltas": [2 * z for z in zs],
                            "all_supporting_N_values": rows_for_cols,
                            "verification": verify(ns, zs),
                        }
                    )
                    if len(hits) >= args.max_hits:
                        stopped_early = True
                        break

    end = dt.datetime.now(dt.UTC)
    best_subset_records = sorted(
        best_subsets.values(),
        key=lambda r: (-r["row_count"], r["z_values"]),
    )[:100]
    result = {
        "script": "pair_column_extend_mine.py",
        "argv": sys.argv[1:],
        "started_utc": start.isoformat(),
        "finished_utc": end.isoformat(),
        "elapsed_seconds": (end - start).total_seconds(),
        "graph": graph_meta,
        "searched_row_count": len(row_sets),
        "tested_pairs": tested_pairs,
        "qualifying_pairs": qualifying_pairs,
        "tested_subsets": tested_subsets,
        "stopped_early": stopped_early,
        "hit_count": len(hits),
        "hits": hits,
        "best_pairs": best_pairs,
        "best_subsets": best_subset_records,
    }
    write_json(args.out, result)
    print(
        json.dumps(
            {
                "elapsed_seconds": result["elapsed_seconds"],
                "filtered_row_count": graph_meta["filtered_row_count"],
                "searched_row_count": len(row_sets),
                "tested_pairs": tested_pairs,
                "qualifying_pairs": qualifying_pairs,
                "tested_subsets": tested_subsets,
                "hit_count": len(hits),
                "stopped_early": stopped_early,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
