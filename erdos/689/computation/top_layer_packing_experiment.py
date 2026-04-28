#!/usr/bin/env python3
"""Top-layer directed packing experiments for Erdos Problem 689.

This standalone script studies the simplified parity-first top-layer model from
`../parity-top-layer.md`.

Fix `n` and let

    H_top(n) = {2^k q : n/2 < 2^k q <= n, q <= n/2 an odd prime}.

For a selected set of switched primes `S`, choosing a nonzero residue for a
prime `p in S` of the form

    b_p == r (mod p)

with `r in S`, `r != p`, does two things inside this simplified model:

1. it repairs the switched prime `r`;
2. it covers the top targets `h in H_top(n)` with `h == r (mod p)`, i.e.
   `h = r + j p` for some `j >= 1`.

If every switched prime chooses exactly one repair target and every switched
prime must receive repair indegree at least one, then the selected primes form
a permutation / directed cycle cover.  This is the central finite model used
below.

The script offers three searches:

- `pair-greedy`: build disjoint 2-cycles greedily, mirroring the two-prime
  repair gadget;
- `assignment`: on a fixed pool, solve the maximum-raw-weight derangement via
  the Hungarian algorithm;
- `assignment-local`: start from `assignment` and hill-climb for distinct
  target coverage by swapping repair targets.

The implementation uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


def primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def parse_int_list(spec: str) -> List[int]:
    return [int(part.strip()) for part in spec.split(",") if part.strip()]


def parse_text_list(spec: str, separator: str = ";") -> List[str]:
    return [part.strip() for part in spec.split(separator) if part.strip()]


def histogram(values: Iterable[int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return dict(sorted(out.items()))


def top_layer_targets(n: int) -> List[int]:
    targets: List[int] = []
    for q in primes_up_to(n // 2):
        if q == 2:
            continue
        value = q
        while value <= n // 2:
            value *= 2
        if value <= n:
            targets.append(value)
    return sorted(targets)


def parse_pool_spec(n: int, odd_primes: Sequence[int], spec: str) -> Tuple[str, List[int]]:
    text = spec.strip().lower()
    if text.startswith("block:"):
        k = int(text.split(":", 1)[1])
        if k < 1:
            raise ValueError("block:K requires K >= 1")
        lo = n / (k + 1)
        hi = n / k
        return f"block:{k}", [p for p in odd_primes if lo < p <= hi]
    if text.startswith("blocks:"):
        ks = parse_int_list(text.split(":", 1)[1])
        if not ks:
            raise ValueError("blocks:K1,K2,... requires at least one block")
        allowed = set(ks)
        out = []
        for p in odd_primes:
            for k in allowed:
                if n / (k + 1) < p <= n / k:
                    out.append(p)
                    break
        return "blocks:" + ",".join(str(k) for k in ks), out
    if text in {"le-n/4", "<=n/4", "le-quarter", "quarter"}:
        return "le-n/4", [p for p in odd_primes if p <= n / 4]
    if text.startswith("le-n/"):
        k = int(text.split("/", 1)[1])
        if k < 1:
            raise ValueError("le-n/K requires K >= 1")
        return f"le-n/{k}", [p for p in odd_primes if p <= n / k]
    raise ValueError(f"unknown pool spec: {spec}")


@dataclass
class Instance:
    n: int
    pool_name: str
    pool: List[int]
    targets: List[int]
    arc_masks: List[List[int]]
    arc_weights: List[List[int]]
    reachable_mask: int
    reachable_targets: int
    max_arc_weight: int
    avg_arc_weight: float
    arc_histogram: Dict[int, int]


def build_instance(n: int, pool_spec: str) -> Instance:
    primes = primes_up_to(n)
    odd_primes = [p for p in primes if p != 2]
    pool_name, pool = parse_pool_spec(n, odd_primes, pool_spec)
    targets = top_layer_targets(n)

    arc_masks: List[List[int]] = []
    arc_weights: List[List[int]] = []
    weights: List[int] = []
    reachable_mask = 0

    for i, p in enumerate(pool):
        mask_row: List[int] = []
        weight_row: List[int] = []
        for j, r in enumerate(pool):
            if i == j:
                mask_row.append(0)
                weight_row.append(0)
                continue
            residue = r % p
            mask = 0
            for t, h in enumerate(targets):
                if h % p == residue:
                    mask |= 1 << t
            mask_row.append(mask)
            weight = mask.bit_count()
            weight_row.append(weight)
            weights.append(weight)
            reachable_mask |= mask
        arc_masks.append(mask_row)
        arc_weights.append(weight_row)

    max_arc_weight = max(weights, default=0)
    avg_arc_weight = (sum(weights) / len(weights)) if weights else 0.0
    return Instance(
        n=n,
        pool_name=pool_name,
        pool=pool,
        targets=targets,
        arc_masks=arc_masks,
        arc_weights=arc_weights,
        reachable_mask=reachable_mask,
        reachable_targets=reachable_mask.bit_count(),
        max_arc_weight=max_arc_weight,
        avg_arc_weight=avg_arc_weight,
        arc_histogram=histogram(weights),
    )


def cycle_histogram(perm: Sequence[int]) -> Dict[int, int]:
    n = len(perm)
    seen = [False] * n
    out: Dict[int, int] = {}
    for start in range(n):
        if perm[start] < 0 or seen[start]:
            continue
        cur = start
        length = 0
        while cur >= 0 and not seen[cur]:
            seen[cur] = True
            length += 1
            cur = perm[cur]
        out[length] = out.get(length, 0) + 1
    return dict(sorted(out.items()))


def evaluate_permutation(
    instance: Instance,
    perm: Sequence[int],
    seconds: float,
    method: str,
    extra: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    counts = [0] * len(instance.targets)
    raw_weight = 0
    selected = 0

    for i, j in enumerate(perm):
        if j < 0:
            continue
        selected += 1
        raw_weight += instance.arc_weights[i][j]
        mask = instance.arc_masks[i][j]
        bits = mask
        while bits:
            lsb = bits & -bits
            idx = lsb.bit_length() - 1
            counts[idx] += 1
            bits ^= lsb

    covered = sum(1 for count in counts if count > 0)
    result: Dict[str, object] = {
        "method": method,
        "selected_primes": selected,
        "covered_targets": covered,
        "uncovered_targets": len(instance.targets) - covered,
        "coverage_ratio": (covered / len(instance.targets)) if instance.targets else 0.0,
        "raw_weight": raw_weight,
        "cycle_histogram": cycle_histogram(perm),
        "seconds": seconds,
    }
    if extra:
        result.update(extra)
    return result


def pair_greedy(instance: Instance) -> Dict[str, object]:
    start = time.perf_counter()
    m = len(instance.pool)
    perm = [-1] * m
    used = [False] * m
    covered_mask = 0
    steps = 0

    while True:
        best_pair: Optional[Tuple[int, int, int, int]] = None
        for i in range(m):
            if used[i]:
                continue
            for j in range(i + 1, m):
                if used[j]:
                    continue
                pair_mask = instance.arc_masks[i][j] | instance.arc_masks[j][i]
                gain = (pair_mask & ~covered_mask).bit_count()
                raw = instance.arc_weights[i][j] + instance.arc_weights[j][i]
                if gain <= 0:
                    continue
                candidate = (gain, raw, i, j)
                if best_pair is None or candidate > best_pair:
                    best_pair = candidate
        if best_pair is None:
            break
        _, _, i, j = best_pair
        perm[i] = j
        perm[j] = i
        used[i] = True
        used[j] = True
        covered_mask |= instance.arc_masks[i][j] | instance.arc_masks[j][i]
        steps += 1

    seconds = time.perf_counter() - start
    return evaluate_permutation(
        instance,
        perm,
        seconds,
        "pair-greedy",
        {"pair_steps": steps},
    )


def hungarian_max_derangement(weights: Sequence[Sequence[int]]) -> List[int]:
    n = len(weights)
    if n == 0:
        return []
    if n == 1:
        return [-1]

    max_weight = 0
    for row in weights:
        if row:
            max_weight = max(max_weight, max(row))
    penalty = (max_weight + 1) * (n + 1)

    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = penalty
            else:
                cost[i][j] = max_weight - weights[i][j]

    # Standard O(n^3) Hungarian algorithm for square minimization.
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)

    for i in range(1, n + 1):
        p[0] = i
        minv = [10**18] * (n + 1)
        used = [False] * (n + 1)
        j0 = 0
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = 10**18
            j1 = 0
            for j in range(1, n + 1):
                if used[j]:
                    continue
                cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    assignment = [-1] * n
    for j in range(1, n + 1):
        if p[j] > 0:
            assignment[p[j] - 1] = j - 1
    return assignment


def assignment_search(instance: Instance) -> Tuple[List[int], Dict[str, object]]:
    start = time.perf_counter()
    perm = hungarian_max_derangement(instance.arc_weights)
    seconds = time.perf_counter() - start
    result = evaluate_permutation(instance, perm, seconds, "assignment")
    return perm, result


def delta_for_swap(
    counts: Sequence[int],
    old_a: int,
    old_b: int,
    new_a: int,
    new_b: int,
) -> int:
    delta = 0
    affected = old_a | old_b | new_a | new_b
    while affected:
        lsb = affected & -affected
        idx = lsb.bit_length() - 1
        new_count = counts[idx]
        if old_a & lsb:
            new_count -= 1
        if old_b & lsb:
            new_count -= 1
        if new_a & lsb:
            new_count += 1
        if new_b & lsb:
            new_count += 1
        old_positive = counts[idx] > 0
        new_positive = new_count > 0
        if old_positive and not new_positive:
            delta -= 1
        elif not old_positive and new_positive:
            delta += 1
        affected ^= lsb
    return delta


def apply_swap_to_counts(
    counts: List[int],
    old_a: int,
    old_b: int,
    new_a: int,
    new_b: int,
) -> None:
    affected = old_a | old_b | new_a | new_b
    while affected:
        lsb = affected & -affected
        idx = lsb.bit_length() - 1
        if old_a & lsb:
            counts[idx] -= 1
        if old_b & lsb:
            counts[idx] -= 1
        if new_a & lsb:
            counts[idx] += 1
        if new_b & lsb:
            counts[idx] += 1
        affected ^= lsb


def local_search(
    instance: Instance,
    initial_perm: Sequence[int],
    passes: int,
) -> Dict[str, object]:
    start = time.perf_counter()
    perm = list(initial_perm)

    counts = [0] * len(instance.targets)
    covered = 0
    for i, j in enumerate(perm):
        if j < 0:
            continue
        bits = instance.arc_masks[i][j]
        while bits:
            lsb = bits & -bits
            idx = lsb.bit_length() - 1
            if counts[idx] == 0:
                covered += 1
            counts[idx] += 1
            bits ^= lsb

    improvement = 0
    completed_moves = 0
    for _ in range(max(0, passes)):
        best_delta = 0
        best_raw_delta = 0
        best_pair: Optional[Tuple[int, int]] = None
        m = len(perm)
        for i in range(m):
            j_i = perm[i]
            if j_i < 0:
                continue
            for k in range(i + 1, m):
                j_k = perm[k]
                if j_k < 0:
                    continue
                if j_k == i or j_i == k:
                    continue
                old_a = instance.arc_masks[i][j_i]
                old_b = instance.arc_masks[k][j_k]
                new_a = instance.arc_masks[i][j_k]
                new_b = instance.arc_masks[k][j_i]
                delta = delta_for_swap(counts, old_a, old_b, new_a, new_b)
                raw_delta = (
                    instance.arc_weights[i][j_k]
                    + instance.arc_weights[k][j_i]
                    - instance.arc_weights[i][j_i]
                    - instance.arc_weights[k][j_k]
                )
                candidate = (delta, raw_delta)
                best = (best_delta, best_raw_delta)
                if candidate > best:
                    best_delta = delta
                    best_raw_delta = raw_delta
                    best_pair = (i, k)
        if best_pair is None or best_delta <= 0:
            break

        i, k = best_pair
        j_i = perm[i]
        j_k = perm[k]
        old_a = instance.arc_masks[i][j_i]
        old_b = instance.arc_masks[k][j_k]
        new_a = instance.arc_masks[i][j_k]
        new_b = instance.arc_masks[k][j_i]
        apply_swap_to_counts(counts, old_a, old_b, new_a, new_b)
        perm[i], perm[k] = perm[k], perm[i]
        covered += best_delta
        improvement += best_delta
        completed_moves += 1

    seconds = time.perf_counter() - start
    result = evaluate_permutation(
        instance,
        perm,
        seconds,
        "assignment-local",
        {
            "local_moves": completed_moves,
            "passes_requested": max(0, passes),
            "coverage_improvement": improvement,
            "start_covered_targets": covered - improvement,
        },
    )
    return result


def run_methods(
    instance: Instance,
    methods: Sequence[str],
    local_passes: int,
) -> Dict[str, Dict[str, object]]:
    out: Dict[str, Dict[str, object]] = {}
    assignment_perm: Optional[List[int]] = None

    for method in methods:
        name = method.strip().lower()
        if name == "pair-greedy":
            out[name] = pair_greedy(instance)
        elif name == "assignment":
            assignment_perm, result = assignment_search(instance)
            out[name] = result
        elif name == "assignment-local":
            if assignment_perm is None:
                assignment_perm, _ = assignment_search(instance)
            out[name] = local_search(instance, assignment_perm, local_passes)
        else:
            raise ValueError(f"unknown method: {method}")
    return out


def instance_summary(instance: Instance) -> Dict[str, object]:
    return {
        "n": instance.n,
        "pool_name": instance.pool_name,
        "pool_size": len(instance.pool),
        "top_targets": len(instance.targets),
        "reachable_targets": instance.reachable_targets,
        "reachable_ratio": (
            instance.reachable_targets / len(instance.targets) if instance.targets else 0.0
        ),
        "max_arc_weight": instance.max_arc_weight,
        "avg_arc_weight": instance.avg_arc_weight,
        "arc_histogram": instance.arc_histogram,
        "pool_primes": instance.pool,
    }


def command_run(args: argparse.Namespace) -> None:
    instance = build_instance(args.n, args.pool)
    result = instance_summary(instance)
    result["methods"] = run_methods(instance, args.methods, args.local_passes)
    print(json.dumps(result, indent=2, sort_keys=True))


def command_sweep(args: argparse.Namespace) -> None:
    rows = []
    for n in args.ns:
        for pool in args.pools:
            instance = build_instance(n, pool)
            row = instance_summary(instance)
            row["methods"] = run_methods(instance, args.methods, args.local_passes)
            rows.append(row)
    print(json.dumps(rows, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="run one n/pool instance")
    run_parser.add_argument("--n", type=int, required=True)
    run_parser.add_argument("--pool", required=True)

    sweep_parser = subparsers.add_parser("sweep", help="run a batch of instances")
    sweep_parser.add_argument("--ns", type=parse_int_list, required=True)
    sweep_parser.add_argument(
        "--pools",
        type=parse_text_list,
        required=True,
        help="semicolon-separated pool specs, e.g. block:4;blocks:4,5;le-n/4",
    )

    for subparser in (run_parser, sweep_parser):
        subparser.set_defaults(methods=["pair-greedy", "assignment", "assignment-local"])
        subparser.add_argument(
            "--methods",
            dest="methods",
            type=lambda s: [part.strip() for part in s.split(",") if part.strip()],
            help="comma-separated methods: pair-greedy,assignment,assignment-local",
        )
        subparser.add_argument("--local-passes", type=int, default=4)

    run_parser.set_defaults(handler=command_run)
    sweep_parser.set_defaults(handler=command_sweep)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
