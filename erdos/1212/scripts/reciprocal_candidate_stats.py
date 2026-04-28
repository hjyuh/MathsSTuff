#!/usr/bin/env python3
"""Reciprocal-candidate diagnostics for the EP1212 rough-semiprime core.

For theta > 1/3 and H=x^theta, core successors are forced into a rigid form:
choose a large prime r, take the first multiple w of r after v, and require
w/r to be prime. This script measures that bottleneck before and after the
anchored exclusion and target-core filters.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

from buffered_live_pair_stats import (
    BufferSpec,
    avoids_interval,
    build_spf,
    clearance,
    composite_flags,
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


def prime_flags(spf: list[int]) -> list[bool]:
    return [value >= 2 and spf[value] == value for value in range(len(spf))]


def primes_between(is_prime: list[bool], low: int, high: int) -> list[int]:
    return [value for value in range(max(2, low), min(high, len(is_prime) - 1) + 1) if is_prime[value]]


def summarize(values: list[int]) -> dict[str, float | int | None]:
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


def reciprocal_counts(
    left: int,
    right: int,
    cap: int,
    buffer: BufferSpec,
    factors: list[tuple[int, ...]],
    least_prime: list[int],
    is_prime: list[bool],
    multiplier: float,
    prime_band: float | None,
) -> dict[str, int]:
    span = buffer.value(right)
    source_threshold = core_threshold(buffer, right, multiplier)
    low = source_threshold + 1
    if prime_band is None:
        high = int(math.isqrt(right + span))
    else:
        high = int(prime_band * span)

    tested_primes = 0
    window_multiples = 0
    reciprocal_semiprimes = 0
    backward_clean = 0
    forward_clear = 0
    valid_core_successors = 0

    for prime in primes_between(is_prime, low, high):
        tested_primes += 1
        residue = (-right) % prime
        if not (1 <= residue <= span):
            continue
        candidate = right + residue
        if candidate > cap or prime * prime > candidate:
            continue
        window_multiples += 1
        cofactor = candidate // prime
        if cofactor >= len(is_prime) or not is_prime[cofactor]:
            continue
        target_threshold = core_threshold(buffer, candidate, multiplier)
        if cofactor <= target_threshold or prime <= target_threshold:
            continue
        reciprocal_semiprimes += 1
        if not avoids_interval(factors[candidate], left, right):
            continue
        backward_clean += 1
        if clearance(factors[right], candidate) < buffer.value(candidate):
            continue
        forward_clear += 1
        if is_core_pair(right, candidate, buffer, least_prime, multiplier):
            valid_core_successors += 1

    return {
        "tested_primes": tested_primes,
        "window_multiples": window_multiples,
        "reciprocal_semiprimes": reciprocal_semiprimes,
        "backward_clean": backward_clean,
        "forward_clear": forward_clear,
        "valid_core_successors": valid_core_successors,
    }


def run_for_buffer(
    cap: int,
    source_cap: int,
    buffer: BufferSpec,
    multiplier: float,
    include_incomplete_slabs: bool,
    prime_band: float | None,
) -> dict:
    successor_cap = cap + buffer.value(cap) + 2
    spf = build_spf(successor_cap)
    factors = factor_sets(spf)
    is_composite = composite_flags(spf)
    least_prime = least_prime_factors(spf)
    is_prime = prime_flags(spf)

    pairs = find_buffered_pairs(cap, source_cap, buffer, factors, is_composite, least_prime)
    core_pairs = [
        (left, right)
        for left, right in pairs
        if is_core_pair(left, right, buffer, least_prime, multiplier)
        and (include_incomplete_slabs or slab_is_complete(slab_index(right), source_cap))
    ]

    slab_values: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    for left, right in core_pairs:
        counts = reciprocal_counts(
            left,
            right,
            cap,
            buffer,
            factors,
            least_prime,
            is_prime,
            multiplier,
            prime_band,
        )
        label = slab_label(slab_index(right))
        for name, value in counts.items():
            slab_values[label][name].append(value)

    slabs = {}
    for label in sorted(slab_values, key=lambda text: int(text.split(",", 1)[0][1:])):
        data = slab_values[label]
        slabs[label] = {
            "complete_slab": slab_is_complete(int(math.log2(int(label.split(",", 1)[0][1:]))), source_cap),
            "core_states": len(data["tested_primes"]),
        }
        for name in (
            "tested_primes",
            "window_multiples",
            "reciprocal_semiprimes",
            "backward_clean",
            "forward_clear",
            "valid_core_successors",
        ):
            summary = summarize(data[name])
            slabs[label][f"{name}_mean"] = summary["mean"]
            slabs[label][f"{name}_zero_fraction"] = summary["zero_fraction"]
            slabs[label][f"{name}_max"] = summary["max"]

    return {
        "cap": cap,
        "source_cap": source_cap,
        "successor_cap": successor_cap,
        "buffer": {
            "kind": buffer.kind,
            "parameter": buffer.parameter,
            "name": buffer.name,
        },
        "core_multiplier": multiplier,
        "prime_band": prime_band,
        "buffered_pairs": len(pairs),
        "core_pairs": len(core_pairs),
        "slabs": slabs,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cap", type=int, default=1000000)
    parser.add_argument("--source-cap", type=int)
    parser.add_argument("--theta", type=float, nargs="*", default=[0.36])
    parser.add_argument(
        "--core-multiplier",
        type=float,
        default=1.0,
        help="require P^-(u),P^-(v) > floor(core_multiplier*H(v))+1",
    )
    parser.add_argument(
        "--prime-band",
        type=float,
        help="optional upper prime cutoff as prime <= prime_band*H(v); default is sqrt(v+H)",
    )
    parser.add_argument("--include-incomplete-slabs", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json-out", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.cap < 10:
        raise SystemExit("--cap must be at least 10")
    if args.core_multiplier <= 0:
        raise SystemExit("--core-multiplier must be positive")
    if args.prime_band is not None and args.prime_band <= args.core_multiplier:
        raise SystemExit("--prime-band must be larger than --core-multiplier")
    for theta in args.theta:
        if not (0 < theta < 0.5):
            raise SystemExit("theta values must satisfy 0 < theta < 0.5")

    specs = [BufferSpec("power", theta) for theta in args.theta]
    max_guard = max(spec.value(args.cap) + 2 for spec in specs)
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
            args.core_multiplier,
            args.include_incomplete_slabs,
            args.prime_band,
        )
        for spec in specs
    ]
    payload = {
        "cap": args.cap,
        "source_cap": source_cap,
        "core_multiplier": args.core_multiplier,
        "prime_band": args.prime_band,
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
