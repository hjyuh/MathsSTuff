#!/usr/bin/env python3
"""Finite averaged-nibble simulations for Erdos Problem 689.

This script isolates the combinatorial part of the robust prime-difference
route.  It studies tripartite labelled graphs with

    x in A1, y in A2, P in R, y - x = 2P,

where A1 consists of v_2 = 1 targets, A2 consists of v_2 >= 2 targets, and the
label set R lies in the odd window (n/5, n/2].  The graph models the labelled
3-uniform hypergraph from the robust matching notes, but the experiments here
stay deliberately finite and combinatorial:

1. "actual" cases evaluate frozen finite residual-target instances coming from
   the existing robust-matching experiment;
2. "synthetic" cases replace those arithmetic target sets by random layered
   subsets with the same edge rule y - x = 2P, so one can test whether the
   matching bottleneck is genuinely combinatorial once degrees are high and the
   target sides have slack.

The matching routines are heuristic only:

- a deterministic greedy matcher that protects low-degree labels first;
- a round-based nibble heuristic followed by the same greedy cleanup.

Positive outcomes here are finite evidence about the labelled-matching step
only.  They do not provide arithmetic evidence that the robust label supply
exists asymptotically.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import random
import statistics
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


Edge = Tuple[int, int]
LabelledEdge = Tuple[int, int, int]


ACTUAL_CASES: Dict[str, Dict[str, object]] = {
    "s12_n4000": {
        "n": 4000,
        "sieve": [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
        "residues": {
            7: 5,
            11: 1,
            13: 10,
            17: 2,
            19: 9,
            23: 20,
            29: 2,
            31: 10,
            37: 15,
            41: 35,
            43: 16,
            47: 17,
        },
        "source": "frozen from robust-matching-results.md",
    },
    "s14_n8000": {
        "n": 8000,
        "sieve": [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59],
        "residues": {
            7: 5,
            11: 7,
            13: 5,
            17: 13,
            19: 15,
            23: 20,
            29: 2,
            31: 24,
            37: 17,
            41: 19,
            43: 29,
            47: 32,
            53: 39,
            59: 7,
        },
        "source": "frozen from one 8-trial finite search with robust_matching_experiment.py",
    },
}


SYNTHETIC_CASES: Dict[str, Dict[str, object]] = {
    "comparable_4000": {
        "n": 4000,
        "a1_size": 275,
        "a2_size": 248,
        "requested_labels": 10,
        "label_lower": 0.20,
        "label_upper": 0.50,
        "description": "random layered sets with the same side sizes as actual s12_n4000",
    },
    "favorable_40": {
        "n": 12000,
        "a1_size": 550,
        "a2_size": 550,
        "requested_labels": 40,
        "label_lower": 0.20,
        "label_upper": 0.33,
        "description": "high-degree synthetic case with wide target slack",
    },
    "favorable_60": {
        "n": 12000,
        "a1_size": 650,
        "a2_size": 650,
        "requested_labels": 60,
        "label_lower": 0.20,
        "label_upper": 0.33,
        "description": "higher-load synthetic case with wide target slack",
    },
}


@dataclass
class GraphInstance:
    name: str
    model: str
    n: int
    a1: List[int]
    a2: List[int]
    labels: List[int]
    edges_by_label: Dict[int, List[Edge]]
    metadata: Dict[str, object]


@dataclass
class MatchingResult:
    size: int
    matched_edges: List[LabelledEdge]
    rounds: int


def mean_or_zero(values: Sequence[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def stats(values: Iterable[int]) -> Dict[str, float]:
    data = sorted(values)
    if not data:
        return {"count": 0, "min": 0, "median": 0, "mean": 0.0, "max": 0}
    return {
        "count": len(data),
        "min": data[0],
        "median": statistics.median(data),
        "mean": round(statistics.fmean(data), 6),
        "max": data[-1],
    }


def load_robust_matching_module():
    path = Path(__file__).with_name("robust_matching_experiment.py")
    spec = importlib.util.spec_from_file_location("robust_matching_experiment", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def build_actual_instance(case_name: str) -> GraphInstance:
    config = ACTUAL_CASES[case_name]
    module = load_robust_matching_module()
    prepared = module.build_prepared_instance(config["n"], config["sieve"])
    result = module.evaluate(prepared, config["residues"])

    a1 = sorted(x for x in result.main_targets if x % 4 == 2)
    a2 = sorted(x for x in result.main_targets if x % 4 == 0)
    a2_set = set(a2)

    edges_by_label: Dict[int, List[Edge]] = {}
    for label in result.robust_pair:
        edges = []
        gap = 2 * label
        for x in a1:
            y = x + gap
            if y in a2_set:
                edges.append((x, y))
        if edges:
            edges_by_label[label] = edges

    metadata = {
        "source": config["source"],
        "sieve": config["sieve"],
        "residues": config["residues"],
        "main_targets": len(result.main_targets),
        "robust_pair_count": len(result.robust_pair),
        "robust_all_count": len(result.robust_all),
    }
    return GraphInstance(
        name=case_name,
        model="actual",
        n=config["n"],
        a1=a1,
        a2=a2,
        labels=sorted(edges_by_label),
        edges_by_label=edges_by_label,
        metadata=metadata,
    )


def odd_window(n: int, lower: float, upper: float) -> List[int]:
    start = max(int(lower * n), n // 5 + 1)
    stop = min(int(upper * n), n // 2)
    return [value for value in range(start, stop + 1) if value % 2 == 1]


def sample_synthetic_instance(case_name: str, seed: int) -> GraphInstance:
    config = SYNTHETIC_CASES[case_name]
    rng = random.Random(seed)
    n = int(config["n"])

    a1_pool = list(range(2, n + 1, 4))
    a2_pool = list(range(4, n + 1, 4))
    label_pool = odd_window(n, float(config["label_lower"]), float(config["label_upper"]))

    a1 = sorted(rng.sample(a1_pool, int(config["a1_size"])))
    a2 = sorted(rng.sample(a2_pool, int(config["a2_size"])))
    requested_labels = int(config["requested_labels"])
    labels_requested = sorted(rng.sample(label_pool, requested_labels))

    a2_set = set(a2)
    edges_by_label: Dict[int, List[Edge]] = {}
    for label in labels_requested:
        edges = []
        gap = 2 * label
        for x in a1:
            y = x + gap
            if y in a2_set:
                edges.append((x, y))
        if edges:
            edges_by_label[label] = edges

    metadata = {
        "description": config["description"],
        "requested_labels": requested_labels,
        "label_lower": config["label_lower"],
        "label_upper": config["label_upper"],
    }
    return GraphInstance(
        name=case_name,
        model="synthetic",
        n=n,
        a1=a1,
        a2=a2,
        labels=sorted(edges_by_label),
        edges_by_label=edges_by_label,
        metadata=metadata,
    )


def available_edges(
    instance: GraphInstance,
    free_a1: set[int],
    free_a2: set[int],
    remaining_labels: Sequence[int],
) -> Tuple[Dict[int, List[Edge]], Dict[int, int], Dict[int, int]]:
    available: Dict[int, List[Edge]] = {}
    degree_a1: Dict[int, int] = {}
    degree_a2: Dict[int, int] = {}
    for label in remaining_labels:
        label_edges = instance.edges_by_label.get(label)
        if not label_edges:
            continue
        kept: List[Edge] = []
        for x, y in label_edges:
            if x in free_a1 and y in free_a2:
                kept.append((x, y))
                degree_a1[x] = degree_a1.get(x, 0) + 1
                degree_a2[y] = degree_a2.get(y, 0) + 1
        if kept:
            available[label] = kept
    return available, degree_a1, degree_a2


def best_edge(
    edges: Sequence[Edge],
    degree_a1: Dict[int, int],
    degree_a2: Dict[int, int],
) -> Edge:
    return min(
        edges,
        key=lambda edge: (
            degree_a1.get(edge[0], 0) + degree_a2.get(edge[1], 0),
            degree_a1.get(edge[0], 0),
            degree_a2.get(edge[1], 0),
            edge[0],
            edge[1],
        ),
    )


def greedy_from_state(
    instance: GraphInstance,
    free_a1: set[int],
    free_a2: set[int],
    remaining_labels: List[int],
) -> MatchingResult:
    matched: List[LabelledEdge] = []
    rounds = 0
    labels = list(remaining_labels)

    while labels:
        available, degree_a1, degree_a2 = available_edges(instance, free_a1, free_a2, labels)
        if not available:
            break
        label = min(available, key=lambda value: (len(available[value]), value))
        x, y = best_edge(available[label], degree_a1, degree_a2)
        free_a1.remove(x)
        free_a2.remove(y)
        matched.append((x, y, label))
        labels = [value for value in labels if value != label]
        rounds += 1

    return MatchingResult(size=len(matched), matched_edges=matched, rounds=rounds)


def greedy_match(instance: GraphInstance) -> MatchingResult:
    return greedy_from_state(
        instance,
        set(instance.a1),
        set(instance.a2),
        list(instance.labels),
    )


def nibble_match(
    instance: GraphInstance,
    seed: int,
    tau: float,
    cleanup_cutoff: int,
) -> MatchingResult:
    rng = random.Random(seed)
    free_a1 = set(instance.a1)
    free_a2 = set(instance.a2)
    remaining_labels = list(instance.labels)
    matched: List[LabelledEdge] = []
    rounds = 0

    while remaining_labels:
        available, degree_a1, degree_a2 = available_edges(
            instance,
            free_a1,
            free_a2,
            remaining_labels,
        )
        active_labels = sorted(available)
        if not active_labels:
            break
        if len(active_labels) <= cleanup_cutoff:
            remaining_labels = active_labels
            break

        sampled = [label for label in active_labels if rng.random() < tau]
        if not sampled:
            sampled = [active_labels[rng.randrange(len(active_labels))]]

        proposals: List[LabelledEdge] = []
        for label in sampled:
            scored = sorted(
                available[label],
                key=lambda edge: (
                    degree_a1.get(edge[0], 0) + degree_a2.get(edge[1], 0),
                    degree_a1.get(edge[0], 0),
                    degree_a2.get(edge[1], 0),
                    rng.random(),
                ),
            )
            shortlist = scored[: min(4, len(scored))]
            x, y = rng.choice(shortlist)
            proposals.append((x, y, label))

        count_a1 = Counter(edge[0] for edge in proposals)
        count_a2 = Counter(edge[1] for edge in proposals)
        accepted = [
            edge
            for edge in proposals
            if count_a1[edge[0]] == 1 and count_a2[edge[1]] == 1
        ]
        if not accepted:
            forced_label = min(active_labels, key=lambda value: (len(available[value]), value))
            x, y = best_edge(available[forced_label], degree_a1, degree_a2)
            accepted = [(x, y, forced_label)]

        used_labels = set()
        for x, y, label in accepted:
            if label in used_labels or x not in free_a1 or y not in free_a2:
                continue
            used_labels.add(label)
            free_a1.remove(x)
            free_a2.remove(y)
            matched.append((x, y, label))

        remaining_labels = [label for label in remaining_labels if label not in used_labels]
        rounds += 1

    cleanup = greedy_from_state(instance, free_a1, free_a2, remaining_labels)
    matched.extend(cleanup.matched_edges)
    rounds += cleanup.rounds
    return MatchingResult(size=len(matched), matched_edges=matched, rounds=rounds)


def graph_summary(instance: GraphInstance) -> Dict[str, object]:
    label_degrees = [len(instance.edges_by_label[label]) for label in instance.labels]
    degree_a1: Dict[int, int] = {}
    degree_a2: Dict[int, int] = {}
    for label in instance.labels:
        for x, y in instance.edges_by_label[label]:
            degree_a1[x] = degree_a1.get(x, 0) + 1
            degree_a2[y] = degree_a2.get(y, 0) + 1
    nonzero_target_degrees = list(degree_a1.values()) + list(degree_a2.values())
    return {
        "n": instance.n,
        "a1_size": len(instance.a1),
        "a2_size": len(instance.a2),
        "active_labels": len(instance.labels),
        "edges": sum(label_degrees),
        "target_slack_a1": round(len(instance.a1) / len(instance.labels), 6) if instance.labels else 0.0,
        "target_slack_a2": round(len(instance.a2) / len(instance.labels), 6) if instance.labels else 0.0,
        "label_degree_stats": stats(label_degrees),
        "target_degree_stats": stats(nonzero_target_degrees),
        "nonisolated_targets": len(nonzero_target_degrees),
    }


def evaluate_actual_case(
    case_name: str,
    nibble_runs: int,
    sample_edges: int,
    tau: float,
    cleanup_cutoff: int,
    seed: int,
) -> Dict[str, object]:
    instance = build_actual_instance(case_name)
    summary = graph_summary(instance)
    greedy = greedy_match(instance)
    nibble_results = [
        nibble_match(instance, seed + 1009 * index, tau, cleanup_cutoff)
        for index in range(nibble_runs)
    ]
    return {
        "name": case_name,
        "model": "actual",
        "metadata": instance.metadata,
        **summary,
        "greedy_size": greedy.size,
        "greedy_saturation": round(greedy.size / len(instance.labels), 6) if instance.labels else 0.0,
        "greedy_sample": greedy.matched_edges[:sample_edges],
        "nibble_sizes": [result.size for result in nibble_results],
        "nibble_mean": round(mean_or_zero([result.size for result in nibble_results]), 6),
        "nibble_min": min((result.size for result in nibble_results), default=0),
        "nibble_saturation_mean": round(
            mean_or_zero(
                [result.size / len(instance.labels) for result in nibble_results]
            ),
            6,
        )
        if instance.labels
        else 0.0,
    }


def evaluate_synthetic_case(
    case_name: str,
    trials: int,
    nibble_runs: int,
    tau: float,
    cleanup_cutoff: int,
    seed: int,
) -> Dict[str, object]:
    label_counts: List[int] = []
    active_ratio: List[float] = []
    edge_counts: List[int] = []
    label_degree_means: List[float] = []
    label_degree_mins: List[int] = []
    target_degree_means: List[float] = []
    greedy_saturation: List[float] = []
    nibble_saturation: List[float] = []
    greedy_full = 0
    nibble_full = 0

    requested_labels = int(SYNTHETIC_CASES[case_name]["requested_labels"])

    for trial_index in range(trials):
        instance = sample_synthetic_instance(case_name, seed + 10007 * (trial_index + 1))
        summary = graph_summary(instance)
        label_counts.append(summary["active_labels"])
        active_ratio.append(summary["active_labels"] / requested_labels)
        edge_counts.append(summary["edges"])
        label_degree_means.append(float(summary["label_degree_stats"]["mean"]))
        label_degree_mins.append(int(summary["label_degree_stats"]["min"]))
        target_degree_means.append(float(summary["target_degree_stats"]["mean"]))

        if instance.labels:
            greedy = greedy_match(instance)
            greedy_rate = greedy.size / len(instance.labels)
            greedy_saturation.append(greedy_rate)
            if greedy.size == len(instance.labels):
                greedy_full += 1

            nibble_rates: List[float] = []
            for run_index in range(nibble_runs):
                result = nibble_match(
                    instance,
                    seed + 1000003 * (trial_index + 1) + run_index,
                    tau,
                    cleanup_cutoff,
                )
                nibble_rates.append(result.size / len(instance.labels))
            nibble_value = mean_or_zero(nibble_rates)
            nibble_saturation.append(nibble_value)
            if nibble_value == 1.0:
                nibble_full += 1
        else:
            greedy_saturation.append(0.0)
            nibble_saturation.append(0.0)

    config = SYNTHETIC_CASES[case_name]
    return {
        "name": case_name,
        "model": "synthetic",
        "description": config["description"],
        "n": config["n"],
        "a1_size": config["a1_size"],
        "a2_size": config["a2_size"],
        "requested_labels": requested_labels,
        "label_window": [config["label_lower"], config["label_upper"]],
        "trials": trials,
        "active_labels_mean": round(mean_or_zero(label_counts), 6),
        "active_ratio_mean": round(mean_or_zero(active_ratio), 6),
        "edges_mean": round(mean_or_zero(edge_counts), 6),
        "label_degree_mean": round(mean_or_zero(label_degree_means), 6),
        "label_degree_min_mean": round(mean_or_zero(label_degree_mins), 6),
        "target_degree_mean": round(mean_or_zero(target_degree_means), 6),
        "target_slack_a1": round(config["a1_size"] / requested_labels, 6),
        "target_slack_a2": round(config["a2_size"] / requested_labels, 6),
        "greedy_saturation_mean": round(mean_or_zero(greedy_saturation), 6),
        "greedy_saturation_min": round(min(greedy_saturation, default=0.0), 6),
        "greedy_full_rate": round(greedy_full / trials, 6) if trials else 0.0,
        "nibble_saturation_mean": round(mean_or_zero(nibble_saturation), 6),
        "nibble_saturation_min": round(min(nibble_saturation, default=0.0), 6),
        "nibble_full_rate": round(nibble_full / trials, 6) if trials else 0.0,
    }


def command_actual(args: argparse.Namespace) -> None:
    payload = evaluate_actual_case(
        args.case,
        args.nibble_runs,
        args.sample_edges,
        args.tau,
        args.cleanup_cutoff,
        args.seed,
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


def command_synthetic(args: argparse.Namespace) -> None:
    payload = evaluate_synthetic_case(
        args.case,
        args.trials,
        args.nibble_runs,
        args.tau,
        args.cleanup_cutoff,
        args.seed,
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


def command_suite(args: argparse.Namespace) -> None:
    start = time.perf_counter()
    payload = {
        "actual": [
            evaluate_actual_case(
                case_name,
                args.nibble_runs,
                args.sample_edges,
                args.tau,
                args.cleanup_cutoff,
                args.seed,
            )
            for case_name in ACTUAL_CASES
        ],
        "synthetic": [
            evaluate_synthetic_case(
                case_name,
                args.trials,
                args.nibble_runs,
                args.tau,
                args.cleanup_cutoff,
                args.seed,
            )
            for case_name in SYNTHETIC_CASES
        ],
        "seconds": round(time.perf_counter() - start, 6),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Finite averaged-nibble simulations for Erdos Problem 689."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    actual = sub.add_parser("actual", help="Evaluate one frozen actual finite graph.")
    actual.add_argument("--case", choices=sorted(ACTUAL_CASES), default="s12_n4000")
    actual.add_argument("--nibble-runs", type=int, default=8)
    actual.add_argument("--sample-edges", type=int, default=6)
    actual.add_argument("--tau", type=float, default=0.35)
    actual.add_argument("--cleanup-cutoff", type=int, default=8)
    actual.add_argument("--seed", type=int, default=689)
    actual.set_defaults(func=command_actual)

    synthetic = sub.add_parser("synthetic", help="Evaluate one synthetic scenario.")
    synthetic.add_argument("--case", choices=sorted(SYNTHETIC_CASES), default="comparable_4000")
    synthetic.add_argument("--trials", type=int, default=80)
    synthetic.add_argument("--nibble-runs", type=int, default=4)
    synthetic.add_argument("--tau", type=float, default=0.35)
    synthetic.add_argument("--cleanup-cutoff", type=int, default=8)
    synthetic.add_argument("--seed", type=int, default=689)
    synthetic.set_defaults(func=command_synthetic)

    suite = sub.add_parser("suite", help="Run the full actual plus synthetic suite.")
    suite.add_argument("--trials", type=int, default=80)
    suite.add_argument("--nibble-runs", type=int, default=4)
    suite.add_argument("--sample-edges", type=int, default=6)
    suite.add_argument("--tau", type=float, default=0.35)
    suite.add_argument("--cleanup-cutoff", type=int, default=8)
    suite.add_argument("--seed", type=int, default=689)
    suite.set_defaults(func=command_suite)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "trials") and args.trials <= 0:
        parser.error("--trials must be positive")
    if hasattr(args, "nibble_runs") and args.nibble_runs <= 0:
        parser.error("--nibble-runs must be positive")
    if hasattr(args, "tau") and not (0.0 < args.tau <= 1.0):
        parser.error("--tau must lie in (0, 1]")
    if hasattr(args, "cleanup_cutoff") and args.cleanup_cutoff < 1:
        parser.error("--cleanup-cutoff must be positive")
    args.func(args)


if __name__ == "__main__":
    main()
