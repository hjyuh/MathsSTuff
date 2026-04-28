#!/usr/bin/env python3
"""Dyadic slab-flow diagnostics for the EP1212 right-core graph.

This script measures a finite version of the missing survival theorem:
whether right-core buffered states can flow through later dyadic slabs after
backward pruning. It deliberately reports reachability, not only local degree.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from buffered_live_pair_stats import (
    BufferSpec,
    avoids_interval,
    build_spf,
    composite_flags,
    encode,
    factor_sets,
    find_buffered_pairs,
    least_prime_factors,
)


def core_threshold(buffer: BufferSpec, right: int, multiplier: float) -> int:
    return int(multiplier * buffer.value(right)) + 1


def is_core_pair(
    left: int,
    right: int,
    buffer: BufferSpec,
    least_prime: list[int],
    multiplier: float,
) -> bool:
    threshold = core_threshold(buffer, right, multiplier)
    return least_prime[left] > threshold and least_prime[right] > threshold


def slab_index(value: int) -> int:
    return value.bit_length() - 1


def slab_label(index: int) -> str:
    return f"[{1 << index},{1 << (index + 1)})"


def slab_is_complete(index: int, source_cap: int) -> bool:
    return (1 << (index + 1)) - 1 <= source_cap


def summarize_numbers(values: list[int]) -> dict[str, float | int | None]:
    if not values:
        return {
            "count": 0,
            "mean": None,
            "max": None,
            "zero_fraction": None,
        }
    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "max": max(values),
        "zero_fraction": sum(1 for value in values if value == 0) / len(values),
    }


def decode(key: int, stride: int) -> tuple[int, int]:
    return key // stride, key % stride


def reconstruct_path(
    start_key: int | None,
    best_next: dict[int, int],
    stride: int,
    limit: int,
) -> tuple[list[tuple[int, int]], bool]:
    if start_key is None:
        return [], False

    path_keys = [start_key]
    while path_keys[-1] in best_next and len(path_keys) < limit:
        path_keys.append(best_next[path_keys[-1]])

    truncated = path_keys[-1] in best_next
    return [decode(key, stride) for key in path_keys], truncated


def run_for_buffer(
    cap: int,
    source_cap: int,
    buffer: BufferSpec,
    include_incomplete_slabs: bool,
    certificate_limit: int,
    core_multiplier: float,
) -> dict:
    successor_cap = cap + buffer.value(cap) + 2
    spf = build_spf(successor_cap)
    factors = factor_sets(spf)
    is_composite = composite_flags(spf)
    least_prime = least_prime_factors(spf)

    all_pairs = find_buffered_pairs(cap, source_cap, buffer, factors, is_composite, least_prime)
    raw_core_pairs = [
        (left, right)
        for left, right in all_pairs
        if is_core_pair(left, right, buffer, least_prime, core_multiplier)
    ]
    core_pairs = [
        (left, right)
        for left, right in raw_core_pairs
        if include_incomplete_slabs or slab_is_complete(slab_index(right), source_cap)
    ]

    stride = successor_cap + 1
    pair_set = {encode(left, right, stride) for left, right in core_pairs}
    key_to_pair = {encode(left, right, stride): (left, right) for left, right in core_pairs}

    max_reached_slab: dict[int, int] = {}
    longest_path: dict[int, int] = {}
    best_next: dict[int, int] = {}
    outdegree: dict[int, int] = {}

    for left, right in sorted(core_pairs, key=lambda item: (item[1], item[0]), reverse=True):
        key = encode(left, right, stride)
        own_slab = slab_index(right)
        best_reach = own_slab
        best_length = 0
        best_target = 0
        degree = 0

        end = min(source_cap, right + buffer.value(right))
        for candidate in range(right + 1, end + 1):
            target = encode(right, candidate, stride)
            if target not in pair_set:
                continue
            if not avoids_interval(factors[candidate], left, right):
                continue

            degree += 1
            target_reach = max_reached_slab[target]
            target_length = 1 + longest_path[target]
            if (target_reach, target_length) > (best_reach, best_length):
                best_reach = target_reach
                best_length = target_length
                best_target = target

        max_reached_slab[key] = best_reach
        longest_path[key] = best_length
        outdegree[key] = degree
        if best_target:
            best_next[key] = best_target

    slabs_present = sorted({slab_index(right) for _left, right in core_pairs})
    top_slab = max(slabs_present) if slabs_present else None

    per_slab_keys: dict[int, list[int]] = defaultdict(list)
    for key, (_left, right) in key_to_pair.items():
        per_slab_keys[slab_index(right)].append(key)

    slabs: dict[str, dict] = {}
    for index in slabs_present:
        keys = per_slab_keys[index]
        degrees = [outdegree[key] for key in keys]
        reach_next = [key for key in keys if max_reached_slab[key] >= index + 1]
        reach_top = [
            key
            for key in keys
            if top_slab is not None and max_reached_slab[key] >= top_slab
        ]
        max_reach_values = [max_reached_slab[key] for key in keys]
        path_lengths = [longest_path[key] for key in keys]
        degree_summary = summarize_numbers(degrees)

        slabs[slab_label(index)] = {
            "slab_index": index,
            "complete_slab": slab_is_complete(index, source_cap),
            "core_states": len(keys),
            "core_outdegree_mean": degree_summary["mean"],
            "core_outdegree_max": degree_summary["max"],
            "core_zero_outdegree_fraction": degree_summary["zero_fraction"],
            "reach_next_slab_count": len(reach_next),
            "reach_next_slab_fraction": len(reach_next) / len(keys) if keys else None,
            "survive_to_top_slab_count": len(reach_top),
            "survive_to_top_slab_fraction": len(reach_top) / len(keys) if keys else None,
            "max_reached_slab_index": max(max_reach_values) if max_reach_values else None,
            "max_reached_slab_label": slab_label(max(max_reach_values)) if max_reach_values else None,
            "longest_core_path_transitions": max(path_lengths) if path_lengths else None,
        }

    global_best_key = None
    if longest_path:
        global_best_key = max(longest_path, key=lambda key: (max_reached_slab[key], longest_path[key]))

    earliest_to_top_key = None
    if top_slab is not None:
        candidates = [
            key
            for key in longest_path
            if max_reached_slab[key] >= top_slab
        ]
        if candidates:
            earliest_to_top_key = max(
                candidates,
                key=lambda key: (-slab_index(key_to_pair[key][1]), longest_path[key]),
            )

    global_path, global_truncated = reconstruct_path(
        global_best_key,
        best_next,
        stride,
        certificate_limit,
    )
    top_path, top_truncated = reconstruct_path(
        earliest_to_top_key,
        best_next,
        stride,
        certificate_limit,
    )

    return {
        "cap": cap,
        "source_cap": source_cap,
        "successor_cap": successor_cap,
        "buffer": {
            "kind": buffer.kind,
            "parameter": buffer.parameter,
            "name": buffer.name,
        },
        "include_incomplete_slabs": include_incomplete_slabs,
        "core_multiplier": core_multiplier,
        "buffered_pairs_before_core_filter": len(all_pairs),
        "right_core_pairs_before_slab_filter": len(raw_core_pairs),
        "right_core_pairs_in_flow_graph": len(core_pairs),
        "top_slab_index": top_slab,
        "top_slab_label": slab_label(top_slab) if top_slab is not None else None,
        "global_best_path": {
            "transitions": longest_path.get(global_best_key, 0) if global_best_key is not None else 0,
            "max_reached_slab_index": max_reached_slab.get(global_best_key) if global_best_key is not None else None,
            "max_reached_slab_label": (
                slab_label(max_reached_slab[global_best_key]) if global_best_key is not None else None
            ),
            "certificate": global_path,
            "certificate_truncated": global_truncated,
        },
        "earliest_to_top_path": {
            "transitions": longest_path.get(earliest_to_top_key, 0) if earliest_to_top_key is not None else 0,
            "start_slab_index": (
                slab_index(key_to_pair[earliest_to_top_key][1]) if earliest_to_top_key is not None else None
            ),
            "start_slab_label": (
                slab_label(slab_index(key_to_pair[earliest_to_top_key][1]))
                if earliest_to_top_key is not None
                else None
            ),
            "certificate": top_path,
            "certificate_truncated": top_truncated,
        },
        "slabs": slabs,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cap", type=int, default=50000, help="maximum coordinate allowed")
    parser.add_argument(
        "--source-cap",
        type=int,
        help="maximum second coordinate for source states; defaults to cap minus a guard band",
    )
    parser.add_argument(
        "--theta",
        type=float,
        nargs="*",
        default=[0.36],
        help="theta values for H(x)=floor(x^theta)",
    )
    parser.add_argument(
        "--log-power",
        type=float,
        nargs="*",
        default=[],
        help="A values for H(x)=floor(log(x)^A)",
    )
    parser.add_argument(
        "--include-incomplete-slabs",
        action="store_true",
        help="include states from dyadic slabs whose upper endpoint exceeds source-cap",
    )
    parser.add_argument(
        "--core-multiplier",
        type=float,
        default=1.0,
        help=(
            "require P^-(left),P^-(right) > floor(core_multiplier*H(right))+1; "
            "use values above 2 for the strict C-core"
        ),
    )
    parser.add_argument(
        "--certificate-limit",
        type=int,
        default=2000,
        help="maximum number of states to store in each certificate path",
    )
    parser.add_argument("--quiet", action="store_true", help="write JSON output without printing it")
    parser.add_argument("--json-out", type=Path, help="optional JSON output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.cap < 10:
        raise SystemExit("--cap must be at least 10")
    if args.certificate_limit < 1:
        raise SystemExit("--certificate-limit must be positive")
    if args.core_multiplier <= 0:
        raise SystemExit("--core-multiplier must be positive")
    for theta in args.theta:
        if not (0 < theta < 0.5):
            raise SystemExit("all theta values must satisfy 0 < theta < 0.5")
    for power in args.log_power:
        if power <= 0:
            raise SystemExit("all log-power values must be positive")

    specs = [BufferSpec("power", theta) for theta in args.theta]
    specs.extend(BufferSpec("log_power", power) for power in args.log_power)

    max_guard = max((spec.value(args.cap) + 2 for spec in specs), default=0)
    source_cap = args.source_cap if args.source_cap is not None else args.cap - max_guard
    if source_cap < 10:
        raise SystemExit("source cap is too small after applying the guard band")
    if source_cap > args.cap:
        raise SystemExit("--source-cap cannot exceed --cap")

    results = [
        run_for_buffer(
            args.cap,
            source_cap,
            spec,
            args.include_incomplete_slabs,
            args.certificate_limit,
            args.core_multiplier,
        )
        for spec in specs
    ]
    payload = {
        "cap": args.cap,
        "source_cap": source_cap,
        "include_incomplete_slabs": args.include_incomplete_slabs,
        "core_multiplier": args.core_multiplier,
        "buffers": [result["buffer"] for result in results],
        "results": results,
    }

    text = json.dumps(payload, indent=2, sort_keys=True)
    if not args.quiet:
        print(text)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
