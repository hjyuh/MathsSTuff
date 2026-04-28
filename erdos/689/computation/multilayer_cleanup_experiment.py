#!/usr/bin/env python3
"""Arbitrary-residue multi-layer cleanup experiments for Erdos Problem 689.

This script starts from the parity-first baseline

    a_2 = 1 mod 2,       a_p = 0 mod p for odd primes p <= n,

then switches a small repair sieve S to fixed nonzero residues c_s mod s.
Those residues do two jobs:

1. they directly cover some remaining deficit points;
2. they certify a medium/high prime p as repairable whenever
   p == c_s (mod s) for some s in S.

After fixing S, the script considers only repairable odd primes with p > n / K.
Each such prime may choose one arbitrary nonzero residue class modulo p, and we
greedily select residue classes using exact switching penalties throughout.

The implementation uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


Assignment = Dict[int, int]


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


def parse_sieve_specs(spec: str) -> List[List[int]]:
    return [parse_int_list(part) for part in spec.split(";") if part.strip()]


def histogram(values: Iterable[int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return dict(sorted(out.items()))


@dataclass
class Baseline:
    n: int
    primes: List[int]
    odd_primes: List[int]
    raw_base: List[int]
    demand: List[int]


@dataclass
class SearchState:
    n: int
    raw: List[int]
    demand: List[int]
    hits: List[int]
    residual: List[int]
    total_deficit: int


def build_baseline(n: int) -> Baseline:
    primes = primes_up_to(n)
    odd_primes = [p for p in primes if p != 2]

    c0 = [0] * (n + 1)
    for m in range(1, n + 1):
        c0[m] += m & 1
    for p in odd_primes:
        for m in range(p, n + 1, p):
            c0[m] += 1

    raw_base = [0] * (n + 1)
    demand = [0] * (n + 1)
    for m in range(1, n + 1):
        raw_base[m] = 2 - c0[m]
        demand[m] = max(0, raw_base[m])
    return Baseline(n=n, primes=primes, odd_primes=odd_primes, raw_base=raw_base, demand=demand)


def make_state_from_raw(n: int, raw: Sequence[int]) -> SearchState:
    demand = [0] * (n + 1)
    hits = [0] * (n + 1)
    residual = [0] * (n + 1)
    total = 0
    for m in range(1, n + 1):
        value = max(0, raw[m])
        demand[m] = value
        residual[m] = value
        total += value
    return SearchState(n=n, raw=list(raw), demand=demand, hits=hits, residual=residual, total_deficit=total)


def positive_points(values: Sequence[int]) -> int:
    return sum(1 for value in values[1:] if value > 0)


def max_positive(values: Sequence[int]) -> int:
    return max(values[1:], default=0)


def apply_residue(state: SearchState, p: int, a: int, delta: int) -> int:
    if not (0 < a < p):
        raise ValueError("residues must be nonzero")
    change = 0
    for m in range(a, state.n + 1, p):
        old_residual = state.residual[m]
        state.hits[m] += delta
        if state.hits[m] < 0:
            raise ValueError("internal error: negative hit count")
        new_residual = max(0, state.demand[m] - state.hits[m])
        state.residual[m] = new_residual
        change += new_residual - old_residual
    state.total_deficit += change
    return change


def apply_switch_requirement(state: SearchState, p: int, delta: int) -> int:
    change = 0
    for m in range(p, state.n + 1, p):
        old_residual = state.residual[m]
        state.raw[m] += delta
        state.demand[m] = max(0, state.raw[m])
        new_residual = max(0, state.demand[m] - state.hits[m])
        state.residual[m] = new_residual
        change += new_residual - old_residual
    state.total_deficit += change
    return change


def switching_penalty(state: SearchState, p: int) -> int:
    penalty = 0
    for m in range(p, state.n + 1, p):
        old = state.residual[m]
        new = max(0, state.demand[m] + 1 - state.hits[m])
        penalty += new - old
    return penalty


def best_residue(state: SearchState, p: int, prefer: Optional[int] = None) -> Tuple[int, int]:
    gains: Dict[int, int] = {}
    for m in range(1, state.n + 1):
        if state.residual[m] <= 0:
            continue
        residue = m % p
        if residue == 0:
            continue
        gains[residue] = gains.get(residue, 0) + 1
    if not gains:
        return 1, 0
    best_gain = max(gains.values())
    if prefer is not None and gains.get(prefer) == best_gain:
        return prefer, best_gain
    best_residues = [a for a, gain in gains.items() if gain == best_gain]
    return min(best_residues), best_gain


def repairable_pool(
    odd_primes: Sequence[int],
    sieve_assignment: Assignment,
    threshold: float,
) -> List[int]:
    pool: List[int] = []
    switched_sieve = set(sieve_assignment)
    for p in odd_primes:
        if p in switched_sieve or p <= threshold:
            continue
        if any(p % s == residue for s, residue in sieve_assignment.items()):
            pool.append(p)
    return pool


def build_state_with_switches(
    baseline: Baseline,
    sieve_assignment: Assignment,
    high_assignment: Optional[Assignment] = None,
) -> SearchState:
    state = make_state_from_raw(baseline.n, baseline.raw_base)
    switched = list(sieve_assignment)
    if high_assignment:
        switched.extend(high_assignment)
    for p in switched:
        apply_switch_requirement(state, p, +1)
    for p, residue in sieve_assignment.items():
        apply_residue(state, p, residue, +1)
    if high_assignment:
        for p, residue in high_assignment.items():
            apply_residue(state, p, residue, +1)
    return state


def capacity_score(
    baseline: Baseline,
    sieve_assignment: Assignment,
    k: int,
) -> Tuple[int, int, int, int, Tuple[int, ...]]:
    state = build_state_with_switches(baseline, sieve_assignment)
    pool = repairable_pool(baseline.odd_primes, sieve_assignment, baseline.n / k)
    weighted = sum(baseline.n // p for p in pool)
    direct_gain = sum(baseline.demand[1:]) - state.total_deficit
    tie_break = tuple(-sieve_assignment[s] for s in sorted(sieve_assignment))
    return (weighted, len(pool), direct_gain, -state.total_deficit, tie_break)


def greedy_sieve_assignment(
    baseline: Baseline,
    sieve: Sequence[int],
    k: int,
) -> Tuple[Assignment, str, int]:
    assignment: Assignment = {}
    search_points = 0
    for s in sieve:
        best_choice: Optional[Tuple[Tuple[int, int, int, int, Tuple[int, ...]], int]] = None
        for residue in range(1, s):
            trial = dict(assignment)
            trial[s] = residue
            score = capacity_score(baseline, trial, k)
            search_points += 1
            candidate = (score, residue)
            if best_choice is None or candidate > best_choice:
                best_choice = candidate
        assert best_choice is not None
        assignment[s] = best_choice[1]
    return assignment, "greedy", search_points


def exhaustive_sieve_assignment(
    baseline: Baseline,
    sieve: Sequence[int],
    k: int,
) -> Tuple[Assignment, str, int]:
    best: Optional[Tuple[Tuple[int, int, int, int, Tuple[int, ...]], Assignment]] = None
    search_points = 0
    for residues in itertools.product(*(range(1, s) for s in sieve)):
        assignment = dict(zip(sieve, residues))
        score = capacity_score(baseline, assignment, k)
        search_points += 1
        candidate = (score, assignment)
        if best is None or candidate > best:
            best = candidate
    assert best is not None
    return dict(sorted(best[1].items())), "exhaustive", search_points


def exact_exhaustive_sieve_assignment(
    baseline: Baseline,
    sieve: Sequence[int],
    k: int,
    min_net_gain: int,
) -> Tuple[Assignment, str, int]:
    best: Optional[Tuple[Tuple[int, int, int, int, int, Tuple[int, ...]], Assignment]] = None
    search_points = 0
    baseline_tokens = sum(baseline.demand[1:])
    for residues in itertools.product(*(range(1, s) for s in sieve)):
        assignment = dict(zip(sieve, residues))
        after_sieve = build_state_with_switches(baseline, assignment)
        final_state, chosen, trace = greedy_cleanup(baseline, assignment, k, min_net_gain)
        tie_break = tuple(-assignment[s] for s in sorted(assignment))
        score = (
            -final_state.total_deficit,
            baseline_tokens - after_sieve.total_deficit,
            trace["total_net_gain"],
            len(chosen),
            -after_sieve.total_deficit,
            tie_break,
        )
        search_points += 1
        candidate = (score, assignment)
        if best is None or candidate > best:
            best = candidate
    assert best is not None
    return dict(sorted(best[1].items())), "exact-exhaustive", search_points


def choose_sieve_assignment(
    baseline: Baseline,
    sieve: Sequence[int],
    k: int,
    search: str,
    exhaustive_limit: int,
    min_net_gain: int,
    exact_small_limit: int,
) -> Tuple[Assignment, str, int]:
    search_space = math.prod(max(1, s - 1) for s in sieve)
    if search in {"auto", "exhaustive"} and search_space <= exact_small_limit:
        return exact_exhaustive_sieve_assignment(baseline, sieve, k, min_net_gain)
    if search == "greedy":
        return greedy_sieve_assignment(baseline, sieve, k)
    if search == "exhaustive":
        return exhaustive_sieve_assignment(baseline, sieve, k)
    if search != "auto":
        raise ValueError("search must be auto, greedy, or exhaustive")
    if search_space <= exhaustive_limit:
        return exhaustive_sieve_assignment(baseline, sieve, k)
    return greedy_sieve_assignment(baseline, sieve, k)


def greedy_cleanup(
    baseline: Baseline,
    sieve_assignment: Assignment,
    k: int,
    min_net_gain: int,
) -> Tuple[SearchState, Assignment, Dict[str, object]]:
    state = build_state_with_switches(baseline, sieve_assignment)
    pool = repairable_pool(baseline.odd_primes, sieve_assignment, baseline.n / k)
    remaining = set(pool)
    chosen: Assignment = {}
    total_penalty = 0
    total_gross = 0
    steps = 0
    zero_net_steps = 0
    last_best: Optional[Dict[str, int]] = None

    while remaining:
        best: Optional[Tuple[int, int, int, int, int]] = None
        for p in sorted(remaining):
            penalty = switching_penalty(state, p)
            residue, gross = best_residue(state, p)
            net = gross - penalty
            candidate = (net, gross, -penalty, -p, -residue)
            if best is None or candidate > best:
                best = candidate
        assert best is not None
        net, gross, neg_penalty, neg_p, neg_residue = best
        p = -neg_p
        residue = -neg_residue
        penalty = -neg_penalty
        last_best = {"p": p, "residue": residue, "net": net, "gross": gross, "penalty": penalty}
        if net < min_net_gain:
            break
        apply_switch_requirement(state, p, +1)
        apply_residue(state, p, residue, +1)
        chosen[p] = residue
        remaining.remove(p)
        total_penalty += penalty
        total_gross += gross
        steps += 1
        if net == 0:
            zero_net_steps += 1

    trace: Dict[str, object] = {
        "pool_size": len(pool),
        "selected": steps,
        "zero_net_steps": zero_net_steps,
        "total_gross_gain": total_gross,
        "total_switch_penalty": total_penalty,
        "total_net_gain": total_gross - total_penalty,
        "stopped_reason": "pool exhausted" if len(chosen) == len(pool) else "best net below threshold",
        "last_best": last_best,
    }
    return state, chosen, trace


def evaluate_case(
    n: int,
    k: int,
    sieve: Sequence[int],
    search: str,
    exhaustive_limit: int,
    min_net_gain: int,
) -> Dict[str, object]:
    baseline = build_baseline(n)
    start = time.perf_counter()
    sieve_assignment, search_mode, search_points = choose_sieve_assignment(
        baseline,
        sieve,
        k,
        search,
        exhaustive_limit,
        min_net_gain,
        exact_small_limit=64,
    )
    after_sieve = build_state_with_switches(baseline, sieve_assignment)
    pool = repairable_pool(baseline.odd_primes, sieve_assignment, baseline.n / k)
    high_pool = [p for p in baseline.odd_primes if p not in sieve_assignment and p > baseline.n / k]
    independent_upper_gain = 0
    for p in pool:
        _, gross = best_residue(after_sieve, p)
        independent_upper_gain += gross

    final_state, chosen, trace = greedy_cleanup(baseline, sieve_assignment, k, min_net_gain)
    verification = build_state_with_switches(baseline, sieve_assignment, chosen)
    if verification.total_deficit != final_state.total_deficit:
        raise RuntimeError(
            f"verification mismatch: greedy={final_state.total_deficit}, check={verification.total_deficit}"
        )

    first_misses = [m for m in range(1, n + 1) if final_state.residual[m] > 0][:20]
    after_sieve_points = positive_points(after_sieve.residual)
    seconds = time.perf_counter() - start
    result: Dict[str, object] = {
        "n": n,
        "K": k,
        "sieve": list(sieve),
        "search_mode": search_mode,
        "search_points": search_points,
        "sieve_residues": dict(sorted(sieve_assignment.items())),
        "baseline_tokens": sum(baseline.demand[1:]),
        "baseline_points": positive_points(baseline.demand),
        "after_sieve_deficit": after_sieve.total_deficit,
        "after_sieve_points": after_sieve_points,
        "after_sieve_improvement": sum(baseline.demand[1:]) - after_sieve.total_deficit,
        "high_prime_pool_size": len(high_pool),
        "repairable_pool_size": len(pool),
        "repairable_share": (len(pool) / len(high_pool)) if high_pool else 0.0,
        "repairable_min": pool[0] if pool else None,
        "repairable_max": pool[-1] if pool else None,
        "repairable_capacity_weight": sum(n // p for p in pool),
        "repairable_capacity_histogram": histogram(n // p for p in pool),
        "independent_upper_gain": independent_upper_gain,
        "greedy_selected": len(chosen),
        "greedy_selected_min": min(chosen) if chosen else None,
        "greedy_selected_max": max(chosen) if chosen else None,
        "greedy_trace": trace,
        "final_deficit": final_state.total_deficit,
        "final_uncovered_points": positive_points(final_state.residual),
        "max_residual": max_positive(final_state.residual),
        "coverage_from_after_sieve": after_sieve.total_deficit - final_state.total_deficit,
        "coverage_ratio_from_after_sieve": (
            (after_sieve.total_deficit - final_state.total_deficit) / after_sieve.total_deficit
            if after_sieve.total_deficit
            else 0.0
        ),
        "first_misses": first_misses,
        "seconds": round(seconds, 6),
    }
    return result


def compact_result(result: Dict[str, object]) -> Dict[str, object]:
    return {
        "n": result["n"],
        "K": result["K"],
        "sieve": result["sieve"],
        "search_mode": result["search_mode"],
        "sieve_residues": result["sieve_residues"],
        "baseline_tokens": result["baseline_tokens"],
        "after_sieve_deficit": result["after_sieve_deficit"],
        "repairable_pool_size": result["repairable_pool_size"],
        "repairable_capacity_weight": result["repairable_capacity_weight"],
        "independent_upper_gain": result["independent_upper_gain"],
        "greedy_selected": result["greedy_selected"],
        "final_deficit": result["final_deficit"],
        "coverage_from_after_sieve": result["coverage_from_after_sieve"],
        "coverage_ratio_from_after_sieve": result["coverage_ratio_from_after_sieve"],
        "seconds": result["seconds"],
    }


def print_json(payload: object) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def command_run(args: argparse.Namespace) -> None:
    result = evaluate_case(
        n=args.n,
        k=args.k,
        sieve=parse_int_list(args.sieve),
        search=args.search,
        exhaustive_limit=args.exhaustive_limit,
        min_net_gain=args.min_net_gain,
    )
    print_json(result)


def command_suite(args: argparse.Namespace) -> None:
    rows: List[Dict[str, object]] = []
    total_start = time.perf_counter()
    for n in parse_int_list(args.ns):
        for k in parse_int_list(args.ks):
            for sieve in parse_sieve_specs(args.sieves):
                result = evaluate_case(
                    n=n,
                    k=k,
                    sieve=sieve,
                    search=args.search,
                    exhaustive_limit=args.exhaustive_limit,
                    min_net_gain=args.min_net_gain,
                )
                rows.append(compact_result(result))
    payload = {
        "rows": rows,
        "seconds": round(time.perf_counter() - total_start, 6),
    }
    print_json(payload)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Arbitrary-residue multi-layer cleanup experiments for Erdos Problem 689."
    )
    parser.add_argument(
        "--version",
        action="version",
        version="multilayer_cleanup_experiment.py 1.0",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Run one cleanup instance.")
    run.add_argument("--n", type=int, required=True)
    run.add_argument("--k", type=int, required=True, help="Allow repairable odd primes p > n / K.")
    run.add_argument("--sieve", required=True, help="Comma-separated repair sieve, e.g. 3,5,7.")
    run.add_argument(
        "--search",
        choices=["auto", "greedy", "exhaustive"],
        default="auto",
        help="How to choose the sieve residues c_s.",
    )
    run.add_argument(
        "--exhaustive-limit",
        type=int,
        default=10000,
        help="Use exhaustive sieve search in --search auto when the residue space is at most this size.",
    )
    run.add_argument(
        "--min-net-gain",
        type=int,
        default=0,
        help="Greedy cleanup stops when the best remaining prime has net gain below this threshold.",
    )
    run.set_defaults(func=command_run)

    suite = sub.add_parser("suite", help="Run a small suite of cleanup instances.")
    suite.add_argument("--ns", default="500,1000,2000")
    suite.add_argument("--ks", default="4,6,8")
    suite.add_argument("--sieves", default="3,5;3,5,7,11,13")
    suite.add_argument(
        "--search",
        choices=["auto", "greedy", "exhaustive"],
        default="auto",
        help="How to choose the sieve residues c_s.",
    )
    suite.add_argument("--exhaustive-limit", type=int, default=10000)
    suite.add_argument("--min-net-gain", type=int, default=0)
    suite.set_defaults(func=command_suite)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
