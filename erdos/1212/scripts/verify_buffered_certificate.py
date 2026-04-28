#!/usr/bin/env python3
"""Verify buffered live-pair ray certificates emitted by buffered_live_pair_stats.py."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


class BufferSpec:
    def __init__(self, kind: str, parameter: float) -> None:
        self.kind = kind
        self.parameter = parameter

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


def verify_path(
    certificate: list[list[int]],
    buffer: BufferSpec,
    factors: list[tuple[int, ...]],
    spf: list[int],
    core: bool,
    core_multiplier: float,
) -> None:
    if not certificate:
        return

    for pair in certificate:
        if len(pair) != 2:
            raise ValueError(f"Malformed pair: {pair}")
        left, right = pair
        if not (4 <= left < right):
            raise ValueError(f"Invalid ordered pair: {pair}")
        if spf[left] == left or spf[right] == right:
            raise ValueError(f"Non-composite coordinate in pair: {pair}")
        if right - left > buffer.value(right):
            raise ValueError(f"Pair exceeds buffer window: {pair}")
        if clearance(factors[left], right) < buffer.value(right):
            raise ValueError(f"Pair is not buffered: {pair}")
        if core:
            threshold = int(core_multiplier * buffer.value(right)) + 1
            if spf[left] <= threshold or spf[right] <= threshold:
                raise ValueError(f"Pair is not core at multiplier {core_multiplier}: {pair}")

    for current, target in zip(certificate, certificate[1:]):
        left, right = current
        next_left, candidate = target
        if next_left != right:
            raise ValueError(f"Non-shift edge: {current} -> {target}")
        if candidate - right > buffer.value(right):
            raise ValueError(f"Candidate exceeds successor window: {current} -> {target}")
        if not avoids_interval(factors[candidate], left, right):
            raise ValueError(f"Candidate fails raw live condition: {current} -> {target}")
        if clearance(factors[right], candidate) < buffer.value(candidate):
            raise ValueError(f"Candidate fails regeneration: {current} -> {target}")
        if core:
            threshold = int(core_multiplier * buffer.value(candidate)) + 1
            if spf[right] <= threshold or spf[candidate] <= threshold:
                raise ValueError(f"Candidate fails core condition at multiplier {core_multiplier}: {current} -> {target}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.json_file.read_text(encoding="utf-8"))
    cap = int(payload["cap"])
    successor_cap = max(
        [cap + 10000]
        + [int(result.get("successor_cap", cap)) for result in payload.get("results", [])]
    )
    spf = build_spf(successor_cap + 10000)
    factors = factor_sets(spf)

    checked = 0
    for result in payload["results"]:
        buffer_data = result["buffer"]
        buffer = BufferSpec(buffer_data["kind"], float(buffer_data["parameter"]))
        core_multiplier = float(result.get("core_multiplier", payload.get("core_multiplier", 1.0)))
        regenerative_certificate = result.get("longest_regenerative_ray_certificate", [])
        if regenerative_certificate:
            verify_path(regenerative_certificate, buffer, factors, spf, core=False, core_multiplier=1.0)
            checked += 1
        core_certificate = result.get("longest_core_ray_certificate", [])
        if core_certificate:
            verify_path(core_certificate, buffer, factors, spf, core=True, core_multiplier=core_multiplier)
            checked += 1
        for path_name in ("global_best_path", "earliest_to_top_path"):
            path_data = result.get(path_name)
            if path_data and path_data.get("certificate"):
                verify_path(
                    path_data.get("certificate", []),
                    buffer,
                    factors,
                    spf,
                    core=True,
                    core_multiplier=core_multiplier,
                )
                checked += 1

    print(f"verified {checked} certificate paths in {args.json_file}")


if __name__ == "__main__":
    main()
