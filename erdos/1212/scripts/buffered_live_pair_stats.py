#!/usr/bin/env python3
"""Finite survival statistics for the EP1212 buffered live-pair graph."""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BufferSpec:
    kind: str
    parameter: float

    @property
    def name(self) -> str:
        if self.kind == "power":
            return f"theta={self.parameter:g}"
        return f"log_power={self.parameter:g}"

    def value(self, x: int) -> int:
        if self.kind == "power":
            return max(1, int(x**self.parameter))
        if x <= 2:
            return 1
        return max(1, int(math.log(x) ** self.parameter))


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for value in range(2, int(limit**0.5) + 1):
        if spf[value] != value:
            continue
        for multiple in range(value * value, limit + 1, value):
            if spf[multiple] == multiple:
                spf[multiple] = value
    return spf


def factor_sets(spf: list[int]) -> list[tuple[int, ...]]:
    factors: list[tuple[int, ...]] = [tuple() for _ in spf]
    for value in range(2, len(spf)):
        current = value
        parts: list[int] = []
        while current > 1:
            prime = spf[current]
            parts.append(prime)
            while current % prime == 0:
                current //= prime
        factors[value] = tuple(parts)
    return factors


def composite_flags(spf: list[int]) -> list[bool]:
    return [value >= 4 and spf[value] != value for value in range(len(spf))]


def least_prime_factors(spf: list[int]) -> list[int]:
    least = [0 for _ in spf]
    for value in range(2, len(spf)):
        least[value] = spf[value]
    return least


def clearance(factors: tuple[int, ...], start: int) -> int:
    if not factors:
        return 10**18
    first_bad = min(((start + prime - 1) // prime) * prime for prime in factors)
    return first_bad - start - 1


def avoids_interval(factors: tuple[int, ...], low: int, high: int) -> bool:
    for prime in factors:
        if ((low + prime - 1) // prime) * prime <= high:
            return False
    return True


def is_right_core(value: int, buffer: BufferSpec, least_prime: list[int]) -> bool:
    return least_prime[value] > buffer.value(value) + 1


def encode(left: int, right: int, stride: int) -> int:
    return left * stride + right


def dyadic_bounds(value: int) -> tuple[int, int]:
    exponent = value.bit_length() - 1
    low = 1 << exponent
    return low, low << 1


def dyadic_label(value: int) -> str:
    low, high = dyadic_bounds(value)
    return f"[{low},{high})"


def find_buffered_pairs(
    cap: int,
    source_cap: int,
    buffer: BufferSpec,
    factors: list[tuple[int, ...]],
    is_composite: list[bool],
    least_prime: list[int],
) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    for right in range(4, source_cap + 1):
        if not is_composite[right]:
            continue
        span = buffer.value(right)
        rough_threshold = span + 1
        if right - 1 < (rough_threshold + 1) ** 2:
            continue
        if right + span > cap:
            continue
        left_min = max(4, right - span)
        for left in range(left_min, right):
            if not is_composite[left] or least_prime[left] <= rough_threshold:
                continue
            if clearance(factors[left], right) >= span:
                pairs.append((left, right))
    return pairs


def successor_counts(
    left: int,
    right: int,
    cap: int,
    buffer: BufferSpec,
    factors: list[tuple[int, ...]],
    is_composite: list[bool],
    least_prime: list[int],
) -> dict[str, int]:
    raw = 0
    regen = 0
    core_regen = 0
    end = min(cap, right + buffer.value(right))
    for candidate in range(right + 1, end + 1):
        if not is_composite[candidate]:
            continue
        if not avoids_interval(factors[candidate], left, right):
            continue
        raw += 1
        if clearance(factors[right], candidate) >= buffer.value(candidate):
            regen += 1
            if is_right_core(candidate, buffer, least_prime):
                core_regen += 1
    return {
        "raw": raw,
        "regen": regen,
        "core_regen": core_regen,
    }


def compute_dp(
    pairs: list[tuple[int, int]],
    cap: int,
    buffer: BufferSpec,
    factors: list[tuple[int, ...]],
    is_composite: list[bool],
    least_prime: list[int],
    core_only: bool,
) -> tuple[int, list[tuple[int, int]]]:
    stride = cap + 1
    if core_only:
        pair_set = {
            encode(left, right, stride)
            for left, right in pairs
            if is_right_core(right, buffer, least_prime)
        }
    else:
        pair_set = {encode(left, right, stride) for left, right in pairs}

    dp: dict[int, int] = {}
    next_node: dict[int, int] = {}

    for left, right in sorted(pairs, key=lambda item: item[1], reverse=True):
        key = encode(left, right, stride)
        if key not in pair_set:
            continue

        best = 1
        best_next = 0
        end = min(cap, right + buffer.value(right))
        for candidate in range(right + 1, end + 1):
            if not is_composite[candidate]:
                continue
            target = encode(right, candidate, stride)
            if target not in pair_set:
                continue
            if not avoids_interval(factors[candidate], left, right):
                continue
            score = 1 + dp.get(target, 1)
            if score > best:
                best = score
                best_next = target
        dp[key] = best
        if best_next:
            next_node[key] = best_next

    if not dp:
        return 0, []

    start = max(dp, key=dp.get)
    path_keys = [start]
    while path_keys[-1] in next_node:
        path_keys.append(next_node[path_keys[-1]])

    certificate = [(key // stride, key % stride) for key in path_keys]
    return dp[start] - 1, certificate


def summarize(values: list[int]) -> dict[str, float | int]:
    if not values:
        return {
            "count": 0,
            "zero_fraction": None,
            "mean": None,
            "max": None,
        }
    return {
        "count": len(values),
        "zero_fraction": sum(1 for value in values if value == 0) / len(values),
        "mean": sum(values) / len(values),
        "max": max(values),
    }


def complete_slab(label: str, cap: int) -> bool:
    high = int(label.split(",", 1)[1].split(")", 1)[0])
    return high - 1 <= cap


def run_for_buffer(cap: int, source_cap: int, buffer: BufferSpec, include_incomplete_slabs: bool) -> dict:
    successor_cap = cap + buffer.value(cap) + 2
    spf = build_spf(successor_cap)
    factors = factor_sets(spf)
    is_composite = composite_flags(spf)
    least_prime = least_prime_factors(spf)
    pairs = find_buffered_pairs(cap, source_cap, buffer, factors, is_composite, least_prime)

    slab_raw: dict[str, list[int]] = defaultdict(list)
    slab_regen: dict[str, list[int]] = defaultdict(list)
    slab_core_regen: dict[str, list[int]] = defaultdict(list)
    slab_core_regen_from_core: dict[str, list[int]] = defaultdict(list)
    slab_core_to_core: dict[str, list[int]] = defaultdict(list)
    slab_pair_counts: dict[str, int] = defaultdict(int)
    slab_right_core_counts: dict[str, int] = defaultdict(int)

    for left, right in pairs:
        label = dyadic_label(right)
        if not include_incomplete_slabs and not complete_slab(label, source_cap):
            continue
        counts = successor_counts(left, right, cap, buffer, factors, is_composite, least_prime)
        right_core = is_right_core(right, buffer, least_prime)
        slab_pair_counts[label] += 1
        if right_core:
            slab_right_core_counts[label] += 1
        slab_raw[label].append(counts["raw"])
        slab_regen[label].append(counts["regen"])
        slab_core_regen[label].append(counts["core_regen"])
        if right_core:
            slab_core_regen_from_core[label].append(counts["regen"])
            slab_core_to_core[label].append(counts["core_regen"])

    slabs = {}
    for label in sorted(slab_pair_counts, key=lambda text: int(text.split(",", 1)[0][1:])):
        raw_summary = summarize(slab_raw[label])
        regen_summary = summarize(slab_regen[label])
        core_regen_summary = summarize(slab_core_regen[label])
        right_core_regen_summary = summarize(slab_core_regen_from_core[label])
        core_to_core_summary = summarize(slab_core_to_core[label])
        pair_count = slab_pair_counts[label]
        right_core_count = slab_right_core_counts[label]
        slabs[label] = {
            "complete_slab": complete_slab(label, source_cap),
            "buffered_pairs": pair_count,
            "right_core_pairs": right_core_count,
            "right_core_fraction": right_core_count / pair_count if pair_count else None,
            "raw_mean": raw_summary["mean"],
            "raw_zero_fraction": raw_summary["zero_fraction"],
            "raw_max": raw_summary["max"],
            "regen_mean_all": regen_summary["mean"],
            "regen_zero_all": regen_summary["zero_fraction"],
            "regen_max_all": regen_summary["max"],
            "core_regen_mean_all": core_regen_summary["mean"],
            "core_regen_zero_all": core_regen_summary["zero_fraction"],
            "reg_mean_right_core": right_core_regen_summary["mean"],
            "reg_zero_right_core": right_core_regen_summary["zero_fraction"],
            "core_to_core_mean": core_to_core_summary["mean"],
            "core_to_core_zero": core_to_core_summary["zero_fraction"],
            "core_to_core_max": core_to_core_summary["max"],
        }

    longest_all, all_certificate = compute_dp(
        pairs, cap, buffer, factors, is_composite, least_prime, core_only=False
    )
    longest_core, core_certificate = compute_dp(
        pairs, cap, buffer, factors, is_composite, least_prime, core_only=True
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
        "buffered_pairs": len(pairs),
        "right_core_pairs": sum(1 for left, right in pairs if is_right_core(right, buffer, least_prime)),
        "longest_regenerative_ray_transitions_inside_cap": longest_all,
        "longest_regenerative_ray_certificate": all_certificate,
        "longest_core_ray_transitions_inside_cap": longest_core,
        "longest_core_ray_certificate": core_certificate,
        "slabs": slabs,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cap", type=int, default=5000, help="maximum coordinate allowed for edges and successors")
    parser.add_argument(
        "--source-cap",
        type=int,
        help="maximum second coordinate for source pairs; defaults to cap minus a guard band",
    )
    parser.add_argument(
        "--theta",
        type=float,
        nargs="*",
        default=[0.25, 0.33, 0.40, 0.45],
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
        help="include dyadic slabs whose upper endpoint exceeds source-cap",
    )
    parser.add_argument("--quiet", action="store_true", help="write JSON output without printing it")
    parser.add_argument("--json-out", type=Path, help="optional JSON output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.cap < 10:
        raise SystemExit("--cap must be at least 10")
    for theta in args.theta:
        if not (0 < theta < 0.5):
            raise SystemExit("all theta values must satisfy 0 < theta < 0.5")
    for power in args.log_power:
        if power <= 0:
            raise SystemExit("all log-power values must be positive")

    max_guard = 0
    specs = [BufferSpec("power", theta) for theta in args.theta]
    specs.extend(BufferSpec("log_power", power) for power in args.log_power)
    for spec in specs:
        max_guard = max(max_guard, spec.value(args.cap) + 2)

    source_cap = args.source_cap if args.source_cap is not None else args.cap - max_guard
    if source_cap < 10:
        raise SystemExit("source cap is too small after applying the guard band")
    if source_cap > args.cap:
        raise SystemExit("--source-cap cannot exceed --cap")

    results = [
        run_for_buffer(args.cap, source_cap, spec, args.include_incomplete_slabs)
        for spec in specs
    ]
    payload = {
        "cap": args.cap,
        "source_cap": source_cap,
        "buffers": [result["buffer"] for result in results],
        "include_incomplete_slabs": args.include_incomplete_slabs,
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
