#!/usr/bin/env python3
"""Finite robust prime-difference probes for Erdos Problem 689.

This script studies the parity-first baseline

    a_2 = 1 mod 2,       a_p = 0 mod p for odd primes p <= n,

after switching a fixed small set S of odd primes to nonzero residues b_s mod s.
For a given switched assignment on S, it records three layers of data:

1. the exact residual demand after switching S only;
2. the exact positive-residual subset inside the main family
       m = 2^k d q
   with k >= 1, d S-smooth, and q an odd prime outside S;
3. robust cleanup primes P > n / 5 satisfying
       H_S(P) >= 1, H_S(2P) >= 2, H_S(4P) >= 2,
   where H_S(x) counts small switched hits from S.

For pairing, only robust labels P in (n/5, n/2] can support differences y - x = 2P.
The finite "pair-and-singleton" check used here is:

    main targets <= robust labels above n/5 + labelled-pair matching size.

Indeed a matched label covers two main targets, while an unused robust label can
still be spent on one singleton target.

The matching routine is greedy only.  Negative finite results are therefore not
certificates; they are probes of whether this route looks numerically plausible
for the tested instances.
"""

from __future__ import annotations

import argparse
import json
import random
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


Assignment = Dict[int, int]
Edge = Tuple[int, int, int]


def primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def histogram(values: Iterable[int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return dict(sorted(out.items()))


def parse_int_list(spec: str) -> List[int]:
    return [int(part.strip()) for part in spec.split(",") if part.strip()]


def parse_sieve_specs(spec: str) -> List[List[int]]:
    return [parse_int_list(part) for part in spec.split(";") if part.strip()]


def smooth_numbers(primes: Sequence[int], limit: int) -> List[int]:
    out = [1]

    def dfs(start: int, current: int) -> None:
        for i in range(start, len(primes)):
            p = primes[i]
            value = current * p
            while value <= limit:
                out.append(value)
                dfs(i + 1, value)
                value *= p

    dfs(0, 1)
    out.sort()
    return out


@dataclass
class PreparedInstance:
    n: int
    sieve: List[int]
    all_primes: List[int]
    odd_prime_divisors: List[int]
    raw_switch: List[int]
    main_candidates: List[int]
    robust_all_candidates: List[int]
    robust_pair_candidates: List[int]


@dataclass
class MatchingResult:
    size: int
    edges: List[Edge]
    unmatched_targets: List[int]
    unused_pair_labels: List[int]


@dataclass
class Evaluation:
    n: int
    sieve: List[int]
    residues: Assignment
    exact_tokens: int
    exact_points: int
    exact_max_residual: int
    main_targets: List[int]
    main_target_count: int
    main_share_exact_tokens: float
    exact_tokens_outside_main: int
    robust_all: List[int]
    robust_pair: List[int]
    robust_high: List[int]
    pair_edge_count: int
    pair_target_histogram: Dict[int, int]
    pair_label_histogram: Dict[int, int]
    pairable_targets: int
    isolated_targets: int
    labels_with_pairs: int
    matching: MatchingResult
    pair_singleton_slack_main: int
    pair_singleton_slack_exact: int
    seconds: float


def build_prepared_instance(n: int, sieve: Sequence[int]) -> PreparedInstance:
    sieve = sorted(sieve)
    sieve_set = set(sieve)
    all_primes = primes_up_to(n)
    odd_primes = [p for p in all_primes if p != 2]

    odd_prime_divisors = [0] * (n + 1)
    for p in odd_primes:
        for m in range(p, n + 1, p):
            odd_prime_divisors[m] += 1

    raw_switch = [0] * (n + 1)
    for m in range(1, n + 1):
        raw_switch[m] = 2 - (m & 1) - odd_prime_divisors[m]
    for s in sieve:
        for m in range(s, n + 1, s):
            raw_switch[m] += 1

    smooth = smooth_numbers(sieve, n)
    main_targets = set()
    for q in odd_primes:
        if q in sieve_set:
            continue
        if 2 * q > n:
            break
        max_d = n // (2 * q)
        for d in smooth:
            if d > max_d:
                break
            value = 2 * d * q
            while value <= n:
                main_targets.add(value)
                value *= 2

    robust_all_candidates = [p for p in odd_primes if n / 5 < p <= n]
    robust_pair_candidates = [p for p in robust_all_candidates if p <= n / 2]
    return PreparedInstance(
        n=n,
        sieve=list(sieve),
        all_primes=all_primes,
        odd_prime_divisors=odd_prime_divisors,
        raw_switch=raw_switch,
        main_candidates=sorted(main_targets),
        robust_all_candidates=robust_all_candidates,
        robust_pair_candidates=robust_pair_candidates,
    )


def build_hits(limit: int, residues: Assignment) -> List[int]:
    hits = [0] * (limit + 1)
    for s, residue in residues.items():
        for x in range(residue, limit + 1, s):
            hits[x] += 1
    return hits


def greedy_labelled_matching(edges: Sequence[Edge]) -> MatchingResult:
    unused_vertices = set()
    unused_pair_labels = set()
    for x, y, p in edges:
        unused_vertices.add(x)
        unused_vertices.add(y)
        unused_pair_labels.add(p)

    chosen: List[Edge] = []
    remaining = list(edges)

    while True:
        available = [
            edge
            for edge in remaining
            if edge[0] in unused_vertices and edge[1] in unused_vertices and edge[2] in unused_pair_labels
        ]
        if not available:
            break

        vertex_degree: Dict[int, int] = {}
        label_degree: Dict[int, int] = {}
        by_vertex: Dict[int, List[Edge]] = {}
        for edge in available:
            x, y, p = edge
            vertex_degree[x] = vertex_degree.get(x, 0) + 1
            vertex_degree[y] = vertex_degree.get(y, 0) + 1
            label_degree[p] = label_degree.get(p, 0) + 1
            by_vertex.setdefault(x, []).append(edge)
            by_vertex.setdefault(y, []).append(edge)

        pivot = min(by_vertex, key=lambda v: (len(by_vertex[v]), v))

        def edge_key(edge: Edge) -> Tuple[int, int, int, int, int, int]:
            x, y, p = edge
            other = y if pivot == x else x
            return (
                vertex_degree.get(other, 0),
                label_degree.get(p, 0),
                max(vertex_degree.get(x, 0), vertex_degree.get(y, 0)),
                p,
                x,
                y,
            )

        best = min(by_vertex[pivot], key=edge_key)
        x, y, p = best
        chosen.append(best)
        unused_vertices.remove(x)
        unused_vertices.remove(y)
        unused_pair_labels.remove(p)

    unmatched_targets = sorted(unused_vertices)
    return MatchingResult(
        size=len(chosen),
        edges=sorted(chosen),
        unmatched_targets=unmatched_targets,
        unused_pair_labels=sorted(unused_pair_labels),
    )


def evaluate(prepared: PreparedInstance, residues: Assignment) -> Evaluation:
    start = time.perf_counter()
    n = prepared.n
    hits = build_hits(4 * n, residues)

    exact_tokens = 0
    exact_points = 0
    exact_max_residual = 0
    for m in range(1, n + 1):
        residual = prepared.raw_switch[m] - hits[m]
        if residual > 0:
            exact_tokens += residual
            exact_points += 1
            if residual > exact_max_residual:
                exact_max_residual = residual

    main_targets = [m for m in prepared.main_candidates if hits[m] == 0]
    main_target_count = len(main_targets)
    main_share = (main_target_count / exact_tokens) if exact_tokens else 0.0
    exact_tokens_outside_main = exact_tokens - main_target_count

    robust_all = [
        p
        for p in prepared.robust_all_candidates
        if hits[p] >= 1 and hits[2 * p] >= 2 and hits[4 * p] >= 2
    ]
    robust_pair = [p for p in robust_all if p <= n / 2]
    robust_high = [p for p in robust_all if p > n / 2]

    main_set = set(main_targets)
    edges: List[Edge] = []
    target_degree: Dict[int, int] = {}
    label_edges: Dict[int, int] = {p: 0 for p in robust_pair}
    for p in robust_pair:
        gap = 2 * p
        for x in main_targets:
            y = x + gap
            if y in main_set:
                edges.append((x, y, p))
                target_degree[x] = target_degree.get(x, 0) + 1
                target_degree[y] = target_degree.get(y, 0) + 1
                label_edges[p] += 1

    matching = greedy_labelled_matching(edges)
    pairable_targets = len(target_degree)
    isolated_targets = main_target_count - pairable_targets
    labels_with_pairs = sum(1 for p in robust_pair if label_edges.get(p, 0) > 0)

    pair_singleton_slack_main = len(robust_all) + matching.size - main_target_count
    pair_singleton_slack_exact = len(robust_all) + matching.size - exact_tokens

    return Evaluation(
        n=n,
        sieve=prepared.sieve,
        residues=dict(sorted(residues.items())),
        exact_tokens=exact_tokens,
        exact_points=exact_points,
        exact_max_residual=exact_max_residual,
        main_targets=main_targets,
        main_target_count=main_target_count,
        main_share_exact_tokens=main_share,
        exact_tokens_outside_main=exact_tokens_outside_main,
        robust_all=robust_all,
        robust_pair=robust_pair,
        robust_high=robust_high,
        pair_edge_count=len(edges),
        pair_target_histogram=histogram(target_degree.get(m, 0) for m in main_targets),
        pair_label_histogram=histogram(label_edges.values()),
        pairable_targets=pairable_targets,
        isolated_targets=isolated_targets,
        labels_with_pairs=labels_with_pairs,
        matching=matching,
        pair_singleton_slack_main=pair_singleton_slack_main,
        pair_singleton_slack_exact=pair_singleton_slack_exact,
        seconds=time.perf_counter() - start,
    )


def evaluation_score(result: Evaluation) -> Tuple[int, int, int, int, int, int, int]:
    total_capacity = len(result.robust_all) + result.matching.size
    return (
        total_capacity,
        len(result.robust_all),
        result.matching.size,
        -result.main_target_count,
        result.pair_singleton_slack_main,
        result.pair_singleton_slack_exact,
        -result.exact_tokens,
    )


def random_assignment(sieve: Sequence[int], rng: random.Random) -> Assignment:
    return {s: rng.randrange(1, s) for s in sieve}


def improve_assignment(
    prepared: PreparedInstance,
    assignment: Assignment,
    passes: int,
    rng: random.Random,
) -> Tuple[Assignment, Evaluation]:
    current = dict(assignment)
    current_eval = evaluate(prepared, current)
    for _ in range(max(0, passes)):
        improved = False
        order = list(prepared.sieve)
        rng.shuffle(order)
        for s in order:
            best_assignment = current
            best_eval = current_eval
            current_residue = current[s]
            for residue in range(1, s):
                if residue == current_residue:
                    continue
                trial = dict(current)
                trial[s] = residue
                trial_eval = evaluate(prepared, trial)
                if evaluation_score(trial_eval) > evaluation_score(best_eval):
                    best_assignment = trial
                    best_eval = trial_eval
            if best_assignment is not current:
                current = best_assignment
                current_eval = best_eval
                improved = True
        if not improved:
            break
    return current, current_eval


def search_assignment(
    prepared: PreparedInstance,
    trials: int,
    passes: int,
    seed: int,
) -> Tuple[Assignment, Evaluation]:
    rng = random.Random(seed)
    starts: List[Assignment] = []
    starts.append({s: 1 for s in prepared.sieve})
    for _ in range(max(0, trials) - 1):
        starts.append(random_assignment(prepared.sieve, rng))

    best_assignment: Optional[Assignment] = None
    best_eval: Optional[Evaluation] = None
    for trial_index, start_assignment in enumerate(starts):
        local_rng = random.Random(seed + 1009 * (trial_index + 1))
        improved_assignment, improved_eval = improve_assignment(
            prepared,
            start_assignment,
            passes,
            local_rng,
        )
        if best_eval is None or evaluation_score(improved_eval) > evaluation_score(best_eval):
            best_assignment = improved_assignment
            best_eval = improved_eval

    assert best_assignment is not None and best_eval is not None
    return best_assignment, best_eval


def compact_evaluation(result: Evaluation, sample_edges: int) -> Dict[str, object]:
    robust_window = len(result.robust_all)
    robust_pair = len(result.robust_pair)
    robust_high = len(result.robust_high)
    matched_vertices = set()
    for x, y, _ in result.matching.edges:
        matched_vertices.add(x)
        matched_vertices.add(y)
    uncovered_main_targets = [m for m in result.main_targets if m not in matched_vertices]
    return {
        "n": result.n,
        "sieve": result.sieve,
        "residues": result.residues,
        "exact_tokens": result.exact_tokens,
        "exact_points": result.exact_points,
        "exact_max_residual": result.exact_max_residual,
        "main_target_count": result.main_target_count,
        "main_share_exact_tokens": result.main_share_exact_tokens,
        "exact_tokens_outside_main": result.exact_tokens_outside_main,
        "robust_all_count": robust_window,
        "robust_pair_count": robust_pair,
        "robust_high_count": robust_high,
        "pair_edge_count": result.pair_edge_count,
        "pairable_targets": result.pairable_targets,
        "isolated_targets": result.isolated_targets,
        "labels_with_pairs": result.labels_with_pairs,
        "pair_target_histogram": result.pair_target_histogram,
        "pair_label_histogram": result.pair_label_histogram,
        "matching_size": result.matching.size,
        "covered_by_pairs": 2 * result.matching.size,
        "unmatched_main_targets": len(uncovered_main_targets),
        "unused_pair_labels": len(result.matching.unused_pair_labels),
        "pair_singleton_slack_main": result.pair_singleton_slack_main,
        "pair_singleton_slack_exact": result.pair_singleton_slack_exact,
        "matching_edges_sample": result.matching.edges[:sample_edges],
        "unmatched_targets_sample": uncovered_main_targets[: sample_edges * 2],
        "robust_all_sample": result.robust_all[:sample_edges],
        "seconds": round(result.seconds, 6),
    }


def robust_density(count: int, candidates: Sequence[int]) -> float:
    return (count / len(candidates)) if candidates else 0.0


def command_run(args: argparse.Namespace) -> None:
    sieve = parse_int_list(args.sieve)
    residues_list = parse_int_list(args.residues)
    if len(residues_list) != len(sieve):
        raise SystemExit("--residues must have the same length as --sieve")
    residues = dict(zip(sieve, residues_list))
    prepared = build_prepared_instance(args.n, sieve)
    result = evaluate(prepared, residues)
    payload = compact_evaluation(result, args.sample_edges)
    payload["robust_all_density"] = robust_density(
        len(result.robust_all), prepared.robust_all_candidates
    )
    payload["robust_pair_density"] = robust_density(
        len(result.robust_pair), prepared.robust_pair_candidates
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


def command_suite(args: argparse.Namespace) -> None:
    ns = parse_int_list(args.ns)
    sieve_specs = parse_sieve_specs(args.sieves)
    reference_n = args.reference_n if args.reference_n else max(ns)
    total_start = time.perf_counter()

    rows: List[Dict[str, object]] = []
    for sieve in sieve_specs:
        prepared_ref = build_prepared_instance(reference_n, sieve)
        best_assignment, ref_eval = search_assignment(
            prepared_ref,
            args.trials,
            args.passes,
            args.seed,
        )
        search_row: Dict[str, object] = {
            "kind": "search",
            "reference_n": reference_n,
            "sieve": sieve,
            "residues": dict(sorted(best_assignment.items())),
            "reference_main_targets": ref_eval.main_target_count,
            "reference_exact_tokens": ref_eval.exact_tokens,
            "reference_robust_all": len(ref_eval.robust_all),
            "reference_robust_pair": len(ref_eval.robust_pair),
            "reference_matching_size": ref_eval.matching.size,
            "reference_pair_singleton_slack_main": ref_eval.pair_singleton_slack_main,
            "reference_pair_singleton_slack_exact": ref_eval.pair_singleton_slack_exact,
            "reference_robust_all_density": robust_density(
                len(ref_eval.robust_all), prepared_ref.robust_all_candidates
            ),
            "reference_robust_pair_density": robust_density(
                len(ref_eval.robust_pair), prepared_ref.robust_pair_candidates
            ),
        }
        rows.append(search_row)

        for n in ns:
            prepared = build_prepared_instance(n, sieve)
            result = evaluate(prepared, best_assignment)
            row = compact_evaluation(result, args.sample_edges)
            row.update(
                {
                    "kind": "evaluation",
                    "reference_n": reference_n,
                    "robust_all_density": robust_density(
                        len(result.robust_all), prepared.robust_all_candidates
                    ),
                    "robust_pair_density": robust_density(
                        len(result.robust_pair), prepared.robust_pair_candidates
                    ),
                }
            )
            rows.append(row)

    payload = {
        "ns": ns,
        "reference_n": reference_n,
        "trials": args.trials,
        "passes": args.passes,
        "seed": args.seed,
        "rows": rows,
        "seconds": round(time.perf_counter() - total_start, 6),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Finite robust prime-difference probe for Erdos Problem 689."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Evaluate one fixed sieve/residue choice.")
    run.add_argument("--n", type=int, required=True)
    run.add_argument("--sieve", required=True, help="Comma-separated switched primes.")
    run.add_argument(
        "--residues",
        required=True,
        help="Comma-separated residues in the same order as --sieve.",
    )
    run.add_argument("--sample-edges", type=int, default=10)
    run.set_defaults(func=command_run)

    suite = sub.add_parser("suite", help="Search residue choices and evaluate them on a small suite.")
    suite.add_argument("--ns", default="1000,2000,4000")
    suite.add_argument(
        "--sieves",
        default="7,11,13,17,19;7,11,13,17,19,23,29,31",
        help="Semicolon-separated switched-prime sets.",
    )
    suite.add_argument(
        "--reference-n",
        type=int,
        default=0,
        help="Optimize residues on this n; default is max(--ns).",
    )
    suite.add_argument("--trials", type=int, default=16, help="Random starts for residue search.")
    suite.add_argument("--passes", type=int, default=2, help="Coordinate-improvement passes per trial.")
    suite.add_argument("--seed", type=int, default=689)
    suite.add_argument("--sample-edges", type=int, default=6)
    suite.set_defaults(func=command_suite)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "n") and args.n <= 0:
        parser.error("--n must be positive")
    if hasattr(args, "reference_n") and args.reference_n < 0:
        parser.error("--reference-n must be nonnegative")
    if hasattr(args, "trials") and args.trials <= 0:
        parser.error("--trials must be positive")
    if hasattr(args, "passes") and args.passes < 0:
        parser.error("--passes must be nonnegative")
    args.func(args)


if __name__ == "__main__":
    main()
