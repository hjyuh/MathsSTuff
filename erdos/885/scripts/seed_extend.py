from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import subprocess
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Iterable


def parse_ints(spec: str | None) -> list[int]:
    if not spec:
        return []
    return [int(x.strip()) for x in spec.replace("\n", ",").split(",") if x.strip()]


def factor_pair(n: int, d: int) -> tuple[int, int] | None:
    if n <= 0 or d < 0:
        return None
    disc = d * d + 4 * n
    s = math.isqrt(disc)
    if s * s != disc:
        return None
    if (s - d) % 2:
        return None
    a = (s - d) // 2
    b = a + d
    if a <= 0 or a * b != n:
        return None
    return a, b


def a_max(delta: int, x_bound: int) -> int:
    return (math.isqrt(delta * delta + 4 * x_bound) - delta) // 2


def d_set(n: int, delta_max: int | None = None, max_sqrt: int = 5_000_000) -> set[int]:
    r = math.isqrt(n)
    if r > max_sqrt:
        raise ValueError(
            f"refusing complete D({n}) enumeration: sqrt(n)={r} exceeds {max_sqrt}"
        )
    out: set[int] = set()
    for a in range(1, r + 1):
        if n % a == 0:
            d = n // a - a
            if delta_max is None or d <= delta_max:
                out.add(d)
    return out


def load_seed(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "N_values" not in data or "deltas" not in data:
        raise ValueError(f"{path} does not look like a seed certificate")
    return data


def seed_relation_map(seed: dict) -> dict[tuple[int, int], tuple[int, int]]:
    matrix_by_n = {int(row["n"]): row for row in seed.get("matrix", [])}
    relmap: dict[tuple[int, int], tuple[int, int]] = {}
    ns = [int(n) for n in seed["N_values"]]
    deltas = [int(d) for d in seed["deltas"]]
    for n in ns:
        row = matrix_by_n.get(n, {})
        row_relations = {
            int(rel["delta"]): (int(rel["a"]), int(rel["b"]))
            for rel in row.get("relations", [])
            if rel.get("ok", True) and "a" in rel and "b" in rel
        }
        for d in deltas:
            pair = row_relations.get(d)
            if pair is None:
                pair = factor_pair(n, d)
            if pair is None:
                raise ValueError(f"seed relation missing or invalid for n={n}, delta={d}")
            relmap[(n, d)] = pair
    return relmap


def verify_seed(ns: Iterable[int], deltas: Iterable[int]) -> dict:
    ns = sorted(dict.fromkeys(int(n) for n in ns))
    deltas = sorted(dict.fromkeys(int(d) for d in deltas))
    matrix = []
    ok = True
    for n in ns:
        relations = []
        for d in deltas:
            pair = factor_pair(n, d)
            if pair is None:
                ok = False
                relations.append({"delta": d, "ok": False})
            else:
                a, b = pair
                relations.append({"delta": d, "ok": True, "a": a, "b": b})
        matrix.append({"n": n, "relations": relations})
    return {
        "ok": ok,
        "num_N": len(ns),
        "num_deltas": len(deltas),
        "N_values": ns,
        "deltas": deltas,
        "matrix": matrix,
    }


def git_status_short(cwd: Path) -> str:
    try:
        proc = subprocess.run(
            ["git", "status", "--short"],
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=5,
            check=False,
        )
    except Exception:
        return ""
    return proc.stdout


def make_run_dir(out_dir: Path, mode: str, argv: list[str]) -> None:
    if out_dir.exists():
        raise SystemExit(f"refusing to reuse existing out_dir: {out_dir}")
    out_dir.mkdir(parents=True)
    run = {
        "script": "scripts/seed_extend.py",
        "mode": mode,
        "argv": argv,
        "cwd": str(Path.cwd()),
        "start_time_utc": dt.datetime.now(dt.UTC).isoformat(),
        "python": sys.version,
        "git_status_short": git_status_short(Path.cwd()),
    }
    write_json(out_dir / "run.json", run)


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def write_jsonl(path: Path, records: Iterable[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    count = 0
    with tmp.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, sort_keys=True) + "\n")
            count += 1
    tmp.replace(path)
    return count


def common_deltas_for_ns(
    ns: list[int], delta_max: int | None, max_sqrt: int
) -> list[int]:
    sets = [d_set(n, delta_max=delta_max, max_sqrt=max_sqrt) for n in ns]
    if not sets:
        return []
    common = sets[0]
    for s in sets[1:]:
        common &= s
    return sorted(common)


def postings_for_delta(delta: int, x_bound: int) -> list[int]:
    return [a * (a + delta) for a in range(1, a_max(delta, x_bound) + 1)]


def intersect_sorted(left: list[int], right: list[int]) -> list[int]:
    out: list[int] = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        lv = left[i]
        rv = right[j]
        if lv == rv:
            out.append(lv)
            i += 1
            j += 1
        elif lv < rv:
            i += 1
        else:
            j += 1
    return out


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    r = math.isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]


def build_columns_from_ns(rows: list[int], ns: Iterable[int]) -> list[dict]:
    columns = []
    for n in sorted(dict.fromkeys(int(n) for n in ns)):
        rels = []
        ok = True
        for d in rows:
            pair = factor_pair(n, d)
            if pair is None:
                ok = False
                break
            rels.append({"delta": d, "a": pair[0], "b": pair[1]})
        if ok:
            columns.append({"n": n, "relations": rels})
    return columns


def sample_columns(rows: list[int], ns: Iterable[int], limit: int = 5) -> list[dict]:
    sample_ns = list(sorted(dict.fromkeys(int(n) for n in ns)))[:limit]
    return build_columns_from_ns(rows, sample_ns)


def enumerate_columns_for_rows(rows: list[int], x_bound: int) -> list[dict]:
    rows = sorted(dict.fromkeys(rows))
    if not rows:
        return []
    anchor = min(rows, key=lambda d: a_max(d, x_bound))
    columns = []
    seen: set[int] = set()
    for a0 in range(1, a_max(anchor, x_bound) + 1):
        n = a0 * (a0 + anchor)
        if n in seen:
            continue
        rels: dict[int, tuple[int, int]] = {}
        ok = True
        for d in rows:
            pair = factor_pair(n, d)
            if pair is None:
                ok = False
                break
            rels[d] = pair
        if ok:
            seen.add(n)
            columns.append(
                {
                    "n": n,
                    "relations": [
                        {"delta": d, "a": rels[d][0], "b": rels[d][1]} for d in rows
                    ],
                }
            )
    return sorted(columns, key=lambda rec: rec["n"])


def extra_delta_support(
    columns: list[dict],
    rows: list[int],
    delta_mode: str,
    delta_max: int | None,
    max_sqrt: int,
) -> tuple[list[dict], Counter[int], dict[int, list[int]]]:
    rows_set = set(rows)
    support: Counter[int] = Counter()
    supporters: dict[int, list[int]] = {}
    if delta_mode != "none":
        for col in columns:
            ds = d_set(col["n"], delta_max=delta_max, max_sqrt=max_sqrt)
            for d in ds:
                support[d] += 1
                if d not in rows_set:
                    supporters.setdefault(d, []).append(col["n"])

    extras = [
        {
            "delta": d,
            "support": c,
            "sample_N_values": supporters.get(d, [])[:20],
        }
        for d, c in sorted(support.items(), key=lambda kv: (-kv[1], kv[0]))
        if d not in rows_set
    ]
    return extras, support, supporters


def summarize_column_pool(
    columns: list[dict],
    rows: list[int],
    delta_mode: str,
    delta_max: int | None,
    max_sqrt: int,
    near_miss_min_support: int,
) -> tuple[dict, list[dict], list[dict]]:
    all_extras, _, supporters = extra_delta_support(
        columns, rows, delta_mode, delta_max, max_sqrt
    )
    extras = [extra for extra in all_extras if extra["support"] >= near_miss_min_support]

    witnesses = []
    if len(rows) >= 5 and len(columns) >= 5:
        witnesses.append(
            {
                "kind": "fixed_rows_K55_or_better",
                "deltas": rows[:5],
                "N_values": [c["n"] for c in columns[:5]],
            }
        )
    for extra in extras:
        if len(rows) + 1 >= 5 and extra["support"] >= 5:
            witnesses.append(
                {
                    "kind": "extra_delta_K55",
                    "deltas": sorted(rows + [extra["delta"]])[:5],
                    "N_values": extra["sample_N_values"][:5],
                    "extra_delta": extra["delta"],
                    "extra_support": extra["support"],
                }
            )

    summary = {
        "fixed_rows": rows,
        "column_count": len(columns),
        "delta_mode": delta_mode,
        "delta_max": delta_max,
        "top_extra_deltas": extras[:20],
        "witness_count": len(witnesses),
    }
    return summary, extras, witnesses


def is_trivial_square_scale(multiplier: int, surviving_rows: list[dict]) -> bool:
    root = math.isqrt(multiplier)
    if root * root != multiplier or not surviving_rows:
        return False
    return all(
        row["layout"] == "aligned"
        and row["split_u"] == root
        and row["split_v"] == root
        and row["new_delta"] == root * row["source_delta"]
        for row in surviving_rows
    )


def command_verify_seed(args: argparse.Namespace) -> None:
    out_dir = Path(args.out_dir)
    make_run_dir(out_dir, "verify-seed", sys.argv[1:])
    seed = load_seed(Path(args.seed))
    ns = seed["N_values"]
    deltas = seed["deltas"]
    result = verify_seed(ns, deltas)
    write_json(out_dir / "seed.json", seed)
    write_json(out_dir / "verified_seed.json", result)

    summary = {
        "ok": result["ok"],
        "num_N": result["num_N"],
        "num_deltas": result["num_deltas"],
    }
    if args.compute_common_deltas != "none":
        common = common_deltas_for_ns(ns, args.delta_max, args.max_sqrt)
        write_json(
            out_dir / "common_deltas.json",
            {
                "N_values": ns,
                "delta_max": args.delta_max,
                "common_delta_count": len(common),
                "common_deltas": common,
            },
        )
        summary["common_delta_count"] = len(common)
        summary["strict_extension_status"] = (
            "possible_by_common_deltas" if len(common) >= 5 else "impossible_retaining_all_seed_columns"
        )
        (out_dir / "strict_extension_status.txt").write_text(
            summary["strict_extension_status"] + "\n", encoding="utf-8"
        )

    write_json(out_dir / "summary.json", summary)
    write_json(out_dir / "complete.json", {"ok": True, "summary": summary})
    print(json.dumps(summary, indent=2, sort_keys=True))


def command_fixed_rows(args: argparse.Namespace) -> None:
    out_dir = Path(args.out_dir)
    make_run_dir(out_dir, "fixed-rows", sys.argv[1:])
    if args.seed:
        seed = load_seed(Path(args.seed))
        write_json(out_dir / "seed.json", seed)
    rows = parse_ints(args.rows) or (load_seed(Path(args.seed))["deltas"] if args.seed else [])
    rows = sorted(dict.fromkeys(rows))
    columns = enumerate_columns_for_rows(rows, args.x)
    column_count = write_jsonl(out_dir / "columns.jsonl", columns)
    summary, extras, witnesses = summarize_column_pool(
        columns,
        rows,
        args.delta_extra_mode,
        args.delta_max,
        args.max_sqrt,
        args.near_miss_min_support,
    )
    summary.update({"x_bound": args.x, "written_columns": column_count})
    write_json(out_dir / "summary.json", summary)
    write_jsonl(out_dir / "near_misses.jsonl", extras)
    write_jsonl(out_dir / "witnesses.jsonl", witnesses)
    write_json(out_dir / "complete.json", {"ok": True, "summary": summary})
    print(json.dumps(summary, indent=2, sort_keys=True))


def seed_pair_replacement_deltas(
    ns: list[int], current_rows: list[int], delta_max: int, max_sqrt: int
) -> list[tuple[int, int]]:
    support: Counter[int] = Counter()
    current = set(current_rows)
    for n in ns:
        for d in d_set(n, delta_max=delta_max, max_sqrt=max_sqrt):
            if d not in current:
                support[d] += 1
    return sorted(support.items(), key=lambda kv: (-kv[1], kv[0]))


def command_row_swap(args: argparse.Namespace) -> None:
    out_dir = Path(args.out_dir)
    make_run_dir(out_dir, "row-swap", sys.argv[1:])
    seed = load_seed(Path(args.seed))
    write_json(out_dir / "seed.json", seed)
    base_rows = sorted(dict.fromkeys(parse_ints(args.rows) or seed["deltas"]))
    candidates = seed_pair_replacement_deltas(
        seed["N_values"], base_rows, args.replacement_delta_max, args.max_sqrt
    )
    write_json(
        out_dir / "candidate_deltas.json",
        {
            "replacement_delta_max": args.replacement_delta_max,
            "candidate_count": len(candidates),
            "top_candidates": [
                {"delta": d, "seed_column_support": support} for d, support in candidates[:100]
            ],
        },
    )

    rowsets = []
    seen: set[tuple[int, ...]] = set()
    for dropped in base_rows:
        for d, support in candidates:
            new_rows = tuple(sorted((set(base_rows) - {dropped}) | {d}))
            if len(new_rows) != len(base_rows) or new_rows in seen:
                continue
            seen.add(new_rows)
            rowsets.append({"rows": list(new_rows), "dropped": dropped, "added": d, "seed_support": support})
            if len(rowsets) >= args.max_rowsets:
                break
        if len(rowsets) >= args.max_rowsets:
            break

    records = []
    witness_records = []
    for i, rowset in enumerate(rowsets, start=1):
        columns = enumerate_columns_for_rows(rowset["rows"], args.x)
        summary, extras, witnesses = summarize_column_pool(
            columns,
            rowset["rows"],
            args.delta_extra_mode,
            args.delta_max,
            args.max_sqrt,
            args.near_miss_min_support,
        )
        rec = {
            "index": i,
            "dropped": rowset["dropped"],
            "added": rowset["added"],
            "seed_support": rowset["seed_support"],
            "rows": rowset["rows"],
            "column_count": len(columns),
            "top_extra_deltas": summary["top_extra_deltas"][:10],
            "witness_count": len(witnesses),
            "sample_columns": columns[:10],
        }
        records.append(rec)
        for w in witnesses:
            w = dict(w)
            w["rowset_index"] = i
            w["rowset"] = rowset
            witness_records.append(w)

    write_jsonl(out_dir / "rowsets.jsonl", records)
    write_jsonl(out_dir / "witnesses.jsonl", witness_records)
    summary = {
        "base_rows": base_rows,
        "x_bound": args.x,
        "rowset_count": len(rowsets),
        "candidate_delta_count": len(candidates),
        "witness_count": len(witness_records),
        "best_rowsets": sorted(records, key=lambda r: (-r["column_count"], r["rows"]))[:20],
    }
    write_json(out_dir / "summary.json", summary)
    write_json(out_dir / "complete.json", {"ok": True, "summary": summary})
    print(json.dumps(summary, indent=2, sort_keys=True))


def command_product_lift(args: argparse.Namespace) -> None:
    out_dir = Path(args.out_dir)
    make_run_dir(out_dir, "product-lift", sys.argv[1:])
    seed = load_seed(Path(args.seed))
    write_json(out_dir / "seed.json", seed)

    seed_ns = [int(n) for n in seed["N_values"]]
    seed_rows = sorted(dict.fromkeys(int(d) for d in seed["deltas"]))
    selected_sizes = sorted(
        {
            size
            for size in parse_ints(args.selected_column_sizes)
            if 2 <= size <= len(seed_ns)
        }
    )
    if not selected_sizes:
        raise SystemExit("selected-column-sizes must contain values between 2 and the seed width")

    relations = seed_relation_map(seed)
    records = []
    seen: set[tuple[int, tuple[int, ...], tuple[int, ...]]] = set()
    column_subsets = [
        tuple(cols)
        for size in selected_sizes
        for cols in combinations(seed_ns, size)
    ]
    for selected_ns in column_subsets:
        for multiplier in range(1, args.m_max + 1):
            surviving_by_gap: dict[int, dict] = {}
            for source_delta in seed_rows:
                pairs = [relations[(n, source_delta)] for n in selected_ns]
                for u in divisors(multiplier):
                    v = multiplier // u
                    aligned_gaps = {abs(v * b - u * a) for a, b in pairs}
                    if len(aligned_gaps) == 1:
                        gap = next(iter(aligned_gaps))
                        if gap > 0:
                            candidate = {
                                "new_delta": gap,
                                "source_delta": source_delta,
                                "split_u": u,
                                "split_v": v,
                                "layout": "aligned",
                            }
                            prior = surviving_by_gap.get(gap)
                            if prior is None or (
                                candidate["source_delta"],
                                candidate["layout"],
                                candidate["split_u"],
                                candidate["split_v"],
                            ) < (
                                prior["source_delta"],
                                prior["layout"],
                                prior["split_u"],
                                prior["split_v"],
                            ):
                                surviving_by_gap[gap] = candidate

                    crossed_gaps = {abs(u * b - v * a) for a, b in pairs}
                    if len(crossed_gaps) == 1:
                        gap = next(iter(crossed_gaps))
                        if gap > 0:
                            candidate = {
                                "new_delta": gap,
                                "source_delta": source_delta,
                                "split_u": u,
                                "split_v": v,
                                "layout": "crossed",
                            }
                            prior = surviving_by_gap.get(gap)
                            if prior is None or (
                                candidate["source_delta"],
                                candidate["layout"],
                                candidate["split_u"],
                                candidate["split_v"],
                            ) < (
                                prior["source_delta"],
                                prior["layout"],
                                prior["split_u"],
                                prior["split_v"],
                            ):
                                surviving_by_gap[gap] = candidate

            surviving_rows = sorted(surviving_by_gap.values(), key=lambda row: row["new_delta"])
            if len(surviving_rows) < args.require_surviving_rows:
                continue

            rows = [row["new_delta"] for row in surviving_rows]
            transformed_ns = [multiplier * n for n in selected_ns]
            dedupe_key = (multiplier, tuple(selected_ns), tuple(rows))
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)

            verification = verify_seed(transformed_ns, rows)
            if not verification["ok"]:
                raise RuntimeError(
                    f"product lift verification failed for multiplier={multiplier}, rows={rows}"
                )

            records.append(
                {
                    "type": "product_lift",
                    "multiplier": multiplier,
                    "selected_seed_columns": list(selected_ns),
                    "transformed_N_values": transformed_ns,
                    "rows": rows,
                    "row_count": len(rows),
                    "column_count": len(selected_ns),
                    "surviving_rows": surviving_rows,
                    "trivial_square_scale": is_trivial_square_scale(multiplier, surviving_rows),
                    "verification": {
                        "ok": verification["ok"],
                        "num_N": verification["num_N"],
                        "num_deltas": verification["num_deltas"],
                    },
                    "sample_columns": sample_columns(rows, transformed_ns, limit=3),
                }
            )

    write_jsonl(out_dir / "product_lifts.jsonl", records)
    summary = {
        "seed_rows": seed_rows,
        "seed_column_count": len(seed_ns),
        "m_max": args.m_max,
        "selected_column_sizes": selected_sizes,
        "tested_column_subsets": len(column_subsets),
        "tested_multiplier_count": args.m_max,
        "lift_count": len(records),
        "nontrivial_lift_count": sum(not rec["trivial_square_scale"] for rec in records),
        "trivial_square_scale_count": sum(rec["trivial_square_scale"] for rec in records),
        "best_lifts": sorted(
            records,
            key=lambda rec: (
                rec["trivial_square_scale"],
                -rec["row_count"],
                -rec["column_count"],
                rec["multiplier"],
                rec["rows"],
            ),
        )[:20],
    }
    write_json(out_dir / "summary.json", summary)
    write_json(out_dir / "complete.json", {"ok": True, "summary": summary})
    print(json.dumps(summary, indent=2, sort_keys=True))


def build_delta_universe(
    seed: dict,
    mode: str,
    delta_max: int,
    max_deltas: int,
    max_sqrt: int,
) -> tuple[list[int], dict]:
    seed_rows = sorted(dict.fromkeys(int(d) for d in seed["deltas"]))
    if max_deltas < len(seed_rows):
        raise SystemExit("max-deltas must be at least the number of seed rows")

    support: Counter[int] = Counter()
    for n in [int(v) for v in seed["N_values"]]:
        for d in d_set(n, delta_max=delta_max, max_sqrt=max_sqrt):
            support[d] += 1

    if mode == "seed-pairs":
        min_seed_support = 2
    else:
        raise SystemExit(f"unsupported delta-universe mode: {mode}")

    ranked_extras = [
        d
        for d, c in sorted(support.items(), key=lambda kv: (-kv[1], kv[0]))
        if d not in seed_rows and c >= min_seed_support
    ]

    chosen = list(seed_rows)
    for d in ranked_extras:
        if len(chosen) >= max_deltas:
            break
        chosen.append(d)

    chosen_sorted = sorted(dict.fromkeys(chosen))
    metadata = {
        "mode": mode,
        "delta_max": delta_max,
        "max_deltas": max_deltas,
        "seed_rows": seed_rows,
        "seed_width": len(seed["N_values"]),
        "selected_delta_count": len(chosen_sorted),
        "truncated_extra_count": max(0, len(ranked_extras) - max(0, max_deltas - len(seed_rows))),
        "selected_deltas": [
            {
                "delta": d,
                "seed_column_support": support.get(d, len(seed["N_values"]) if d in seed_rows else 0),
                "source": "seed-row" if d in seed_rows else "seed-pair",
            }
            for d in chosen_sorted
        ],
    }
    return chosen_sorted, metadata


def command_restricted_delta_mine(args: argparse.Namespace) -> None:
    if args.delta_max is None:
        raise SystemExit("restricted-delta-mine requires --delta-max")

    out_dir = Path(args.out_dir)
    make_run_dir(out_dir, "restricted-delta-mine", sys.argv[1:])
    seed = load_seed(Path(args.seed))
    write_json(out_dir / "seed.json", seed)

    universe, universe_meta = build_delta_universe(
        seed, args.delta_universe, args.delta_max, args.max_deltas, args.max_sqrt
    )
    write_json(out_dir / "delta_universe.json", universe_meta)

    postings = {d: postings_for_delta(d, args.x) for d in universe}
    pair_cache_min = max(1, min(args.pair_min_support, args.triple_min_support))
    pair_common: dict[tuple[int, int], list[int]] = {}
    pair_records = []
    for i, d1 in enumerate(universe):
        if len(postings[d1]) < pair_cache_min:
            continue
        for d2 in universe[i + 1 :]:
            if len(postings[d2]) < pair_cache_min:
                continue
            common = intersect_sorted(postings[d1], postings[d2])
            support = len(common)
            if support < pair_cache_min:
                continue
            pair_common[(d1, d2)] = common
            if support >= args.pair_min_support:
                pair_records.append(
                    {
                        "type": "pair",
                        "support": support,
                        "deltas": [d1, d2],
                        "sample_N_values": common[:20],
                        "sample_columns": sample_columns([d1, d2], common, limit=5),
                    }
                )

    write_jsonl(out_dir / "pairs.jsonl", pair_records)

    quad_candidates: dict[tuple[int, ...], dict] = {}
    triple_records = []
    triple_count = 0
    extra_mode = args.delta_extra_mode
    for i, d1 in enumerate(universe):
        for j in range(i + 1, len(universe)):
            d2 = universe[j]
            common12 = pair_common.get((d1, d2))
            if common12 is None or len(common12) < args.triple_min_support:
                continue
            for d3 in universe[j + 1 :]:
                if (d1, d3) not in pair_common or (d2, d3) not in pair_common:
                    continue
                common = intersect_sorted(common12, postings[d3])
                support = len(common)
                if support < args.triple_min_support:
                    continue
                triple_count += 1
                rows = [d1, d2, d3]
                columns = build_columns_from_ns(rows, common)
                extras, _, supporters = extra_delta_support(
                    columns, rows, extra_mode, args.delta_max, args.max_sqrt
                )
                top_extras = [
                    extra for extra in extras if extra["support"] >= args.near_miss_min_support
                ][:10]
                triple_records.append(
                    {
                        "type": "triple",
                        "support": support,
                        "deltas": rows,
                        "sample_N_values": common[:20],
                        "sample_columns": columns[:5],
                        "top_extra_deltas": top_extras,
                    }
                )
                for extra in extras:
                    if extra["support"] < args.rowset_min_support:
                        continue
                    quad_rows = tuple(sorted(rows + [extra["delta"]]))
                    supporter_ns = supporters.get(extra["delta"], [])
                    candidate = {
                        "rows": list(quad_rows),
                        "support": extra["support"],
                        "source_triple": rows,
                        "extra_delta": extra["delta"],
                        "supporting_N_values": supporter_ns,
                    }
                    prior = quad_candidates.get(quad_rows)
                    if prior is None or (
                        candidate["support"],
                        len(set(candidate["rows"]) & set(seed["deltas"])),
                        -max(candidate["rows"]),
                    ) > (
                        prior["support"],
                        len(set(prior["rows"]) & set(seed["deltas"])),
                        -max(prior["rows"]),
                    ):
                        quad_candidates[quad_rows] = candidate

    write_jsonl(out_dir / "triples.jsonl", triple_records)

    quad_records = []
    witness_records = []
    sorted_quads = sorted(
        quad_candidates.values(),
        key=lambda rec: (-rec["support"], rec["rows"]),
    )[: args.max_rowsets]
    for index, quad in enumerate(sorted_quads, start=1):
        rows = quad["rows"]
        support_ns = quad["supporting_N_values"]
        columns = build_columns_from_ns(rows, support_ns)
        summary, extras, witnesses = summarize_column_pool(
            columns,
            rows,
            extra_mode,
            args.delta_max,
            args.max_sqrt,
            args.near_miss_min_support,
        )
        record = {
            "type": "rowset",
            "index": index,
            "support": len(columns),
            "deltas": rows,
            "source_triple": quad["source_triple"],
            "extra_delta": quad["extra_delta"],
            "sample_N_values": support_ns[:20],
            "sample_columns": columns[:10],
            "top_extra_deltas": extras[:10],
            "witness_count": len(witnesses),
        }
        quad_records.append(record)
        for witness in witnesses:
            verified = verify_seed(witness["N_values"], witness["deltas"])
            if not verified["ok"]:
                raise RuntimeError(
                    f"restricted delta witness verification failed for rows={witness['deltas']}"
                )
            witness_records.append(
                {
                    **witness,
                    "rowset_index": index,
                    "rowset": rows,
                    "verification": {
                        "ok": verified["ok"],
                        "num_N": verified["num_N"],
                        "num_deltas": verified["num_deltas"],
                    },
                }
            )

    write_jsonl(out_dir / "rowsets.jsonl", quad_records)
    write_jsonl(out_dir / "witnesses.jsonl", witness_records)
    summary = {
        "x_bound": args.x,
        "delta_max": args.delta_max,
        "delta_universe_count": len(universe),
        "pair_record_count": len(pair_records),
        "pair_cache_count": len(pair_common),
        "triple_count": triple_count,
        "rowset_count": len(quad_records),
        "witness_count": len(witness_records),
        "best_rowsets": sorted(quad_records, key=lambda rec: (-rec["support"], rec["deltas"]))[:20],
    }
    write_json(out_dir / "summary.json", summary)
    write_json(out_dir / "complete.json", {"ok": True, "summary": summary})
    print(json.dumps(summary, indent=2, sort_keys=True))


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--delta-max", type=int)
    parser.add_argument("--max-sqrt", type=int, default=5_000_000)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="EP885 seed-extension runner.")
    sub = parser.add_subparsers(dest="mode", required=True)

    p = sub.add_parser("verify-seed")
    add_common_args(p)
    p.add_argument("--seed", required=True)
    p.add_argument("--compute-common-deltas", choices=["none", "complete"], default="none")
    p.set_defaults(func=command_verify_seed)

    p = sub.add_parser("fixed-rows")
    add_common_args(p)
    p.add_argument("--seed")
    p.add_argument("--rows")
    p.add_argument("--x", type=int, required=True)
    p.add_argument("--delta-extra-mode", choices=["none", "complete"], default="none")
    p.add_argument("--near-miss-min-support", type=int, default=3)
    p.set_defaults(func=command_fixed_rows)

    p = sub.add_parser("row-swap")
    add_common_args(p)
    p.add_argument("--seed", required=True)
    p.add_argument("--rows")
    p.add_argument("--x", type=int, required=True)
    p.add_argument("--replacement-source", choices=["seed-pairs"], default="seed-pairs")
    p.add_argument("--replacement-delta-max", type=int, required=True)
    p.add_argument("--max-rowsets", type=int, default=200)
    p.add_argument("--delta-extra-mode", choices=["none", "complete"], default="none")
    p.add_argument("--near-miss-min-support", type=int, default=4)
    p.set_defaults(func=command_row_swap)

    p = sub.add_parser("product-lift")
    add_common_args(p)
    p.add_argument("--seed", required=True)
    p.add_argument("--m-max", type=int, required=True)
    p.add_argument("--selected-column-sizes", default="2,3")
    p.add_argument("--require-surviving-rows", type=int, default=4)
    p.set_defaults(func=command_product_lift)

    p = sub.add_parser("restricted-delta-mine")
    add_common_args(p)
    p.add_argument("--seed", required=True)
    p.add_argument("--x", type=int, required=True)
    p.add_argument("--delta-universe", choices=["seed-pairs"], default="seed-pairs")
    p.add_argument("--max-deltas", type=int, default=2000)
    p.add_argument("--pair-min-support", type=int, default=10)
    p.add_argument("--triple-min-support", type=int, default=4)
    p.add_argument("--rowset-min-support", type=int, default=4)
    p.add_argument("--near-miss-min-support", type=int, default=4)
    p.add_argument("--max-rowsets", type=int, default=200)
    p.add_argument("--delta-extra-mode", choices=["none", "complete"], default="complete")
    p.set_defaults(func=command_restricted_delta_mine)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
