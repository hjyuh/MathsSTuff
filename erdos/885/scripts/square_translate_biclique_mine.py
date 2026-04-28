#!/usr/bin/env python3
"""Mine square-translate bicliques for EP885.

We work in the normalization

    z^2 + N = y^2.

A biclique with row set {N_i} and column set {z_j} gives an EP885
certificate with differences d_j = 2 z_j, since

    d_j^2 + 4 N_i = 4(y_ij)^2.

The script enumerates all positive integer incidences with

    1 <= z <= z_max,   0 < N <= n_max,

then searches for K_{r,s} bicliques in the resulting bipartite graph.
It is meant as a seed miner: bounded, reproducible, and exact.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable


def factor_pair_for_difference(n: int, d: int) -> tuple[int, int] | None:
    disc = d * d + 4 * n
    s = math.isqrt(disc)
    if s * s != disc or (s - d) % 2:
        return None
    a = (s - d) // 2
    b = a + d
    if a <= 0 or a * b != n:
        return None
    return a, b


def verify(ns: Iterable[int], zs: Iterable[int]) -> dict:
    ns = list(ns)
    zs = list(zs)
    deltas = [2 * z for z in zs]
    ok = True
    matrix = []
    for n in ns:
        relations = []
        for z, d in zip(zs, deltas):
            y2 = z * z + n
            y = math.isqrt(y2)
            pair = factor_pair_for_difference(n, d)
            hit_ok = y * y == y2 and pair is not None
            ok = ok and hit_ok
            entry = {"z": z, "delta": d, "ok": hit_ok, "y": y if hit_ok else None}
            if pair is not None:
                entry["a"], entry["b"] = pair
            relations.append(entry)
        matrix.append({"N": n, "relations": relations})
    return {
        "ok": ok,
        "num_N": len(ns),
        "num_z": len(zs),
        "N_values": ns,
        "z_values": zs,
        "deltas": deltas,
        "matrix": matrix,
    }


def generate_graph(z_max: int, n_max: int, min_degree: int) -> tuple[dict[int, tuple[int, ...]], dict]:
    """Return row-neighbor lists N -> sorted z's with degree >= min_degree."""
    rows: dict[int, list[int]] = defaultdict(list)
    edge_count = 0
    for z in range(1, z_max + 1):
        k_max = math.isqrt(z * z + n_max) - z
        for k in range(1, k_max + 1):
            n = k * (2 * z + k)
            if n <= n_max:
                rows[n].append(z)
                edge_count += 1

    filtered = {
        n: tuple(zs)
        for n, zs in rows.items()
        if len(zs) >= min_degree
    }
    metadata = {
        "z_max": z_max,
        "n_max": n_max,
        "raw_row_count": len(rows),
        "filtered_row_count": len(filtered),
        "edge_count": edge_count,
        "min_degree": min_degree,
    }
    return filtered, metadata


def intersect_tuple_set(xs: tuple[int, ...], ys: frozenset[int]) -> frozenset[int]:
    if len(xs) <= len(ys):
        return frozenset(x for x in xs if x in ys)
    xset = set(xs)
    return frozenset(y for y in ys if y in xset)


def find_bicliques(
    rows: dict[int, tuple[int, ...]],
    target_rows: int,
    target_cols: int,
    row_limit: int,
    max_hits: int,
    max_nodes: int,
) -> dict:
    ordered = sorted(rows.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    if row_limit > 0:
        ordered = ordered[:row_limit]
    row_ns = [n for n, _ in ordered]
    row_zs = [tuple(zs) for _, zs in ordered]
    row_sets = [frozenset(zs) for zs in row_zs]

    hits = []
    near: dict[tuple[int, int], dict] = {}
    nodes = 0
    stopped_early = False

    def record(chosen: list[int], cols: frozenset[int]) -> None:
        if not chosen or not cols:
            return
        key = (len(chosen), len(cols))
        rec = near.get(key)
        sample_cols = sorted(cols)[:20]
        candidate = {
            "row_count": len(chosen),
            "col_count": len(cols),
            "N_values": chosen[:],
            "z_values_sample": sample_cols,
        }
        if rec is None or (len(cols), -max(chosen)) > (rec["col_count"], -max(rec["N_values"])):
            near[key] = candidate

    def rec(start: int, chosen: list[int], common: frozenset[int]) -> None:
        nonlocal nodes, stopped_early
        if stopped_early:
            return
        nodes += 1
        if nodes >= max_nodes:
            stopped_early = True
            return
        record(chosen, common)
        depth = len(chosen)
        if depth == target_rows:
            if len(common) >= target_cols:
                z_values = sorted(common)[:target_cols]
                ns = chosen[:target_rows]
                hits.append(
                    {
                        "N_values": ns,
                        "z_values": z_values,
                        "deltas": [2 * z for z in z_values],
                        "verification": verify(ns, z_values),
                    }
                )
            if len(hits) >= max_hits:
                stopped_early = True
            return
        remaining_needed = target_rows - depth
        last_start = len(row_ns) - remaining_needed + 1
        for i in range(start, last_start):
            if stopped_early:
                return
            if depth == 0:
                new_common = row_sets[i]
            else:
                new_common = intersect_tuple_set(row_zs[i], common)
            if len(new_common) < target_cols:
                continue
            chosen.append(row_ns[i])
            rec(i + 1, chosen, new_common)
            chosen.pop()

    rec(0, [], frozenset())
    near_records = sorted(
        near.values(),
        key=lambda r: (-min(r["row_count"], target_rows), -r["col_count"], r["N_values"]),
    )
    return {
        "searched_rows": len(row_ns),
        "nodes": nodes,
        "stopped_early": stopped_early,
        "hit_count": len(hits),
        "hits": hits,
        "near_records": near_records[:200],
    }


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Mine square-translate bicliques.")
    parser.add_argument("--z-max", type=int, required=True)
    parser.add_argument("--n-max", type=int, required=True)
    parser.add_argument("--target-rows", type=int, default=5)
    parser.add_argument("--target-cols", type=int, default=5)
    parser.add_argument("--row-limit", type=int, default=5000)
    parser.add_argument("--max-hits", type=int, default=20)
    parser.add_argument("--max-nodes", type=int, default=2_000_000)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    min_degree = args.target_cols
    start = dt.datetime.now(dt.UTC)
    rows, graph_meta = generate_graph(args.z_max, args.n_max, min_degree)
    search = find_bicliques(
        rows,
        args.target_rows,
        args.target_cols,
        args.row_limit,
        args.max_hits,
        args.max_nodes,
    )
    end = dt.datetime.now(dt.UTC)
    result = {
        "script": "square_translate_biclique_mine.py",
        "argv": sys.argv[1:],
        "started_utc": start.isoformat(),
        "finished_utc": end.isoformat(),
        "elapsed_seconds": (end - start).total_seconds(),
        "graph": graph_meta,
        "search": search,
    }
    write_json(args.out, result)
    print(
        json.dumps(
            {
                "elapsed_seconds": result["elapsed_seconds"],
                "filtered_row_count": graph_meta["filtered_row_count"],
                "searched_rows": search["searched_rows"],
                "nodes": search["nodes"],
                "hit_count": search["hit_count"],
                "stopped_early": search["stopped_early"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
