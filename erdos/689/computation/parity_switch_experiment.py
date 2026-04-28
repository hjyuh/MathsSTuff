#!/usr/bin/env python3
"""Parity-first switching experiments for Erdos Problem 689.

The baseline is

    a_2 = 1 mod 2,       a_p = 0 mod p for odd primes p <= n.

If R is the set of odd primes moved away from zero, the exact finite condition
is

    G_R(m) >= max(0, 2 - C0(m) + L_R(m))     (1 <= m <= n),

where C0 is the baseline coverage, L_R counts switched prime divisors of m,
and G_R counts hits from the new nonzero residues.  This script keeps that
switching cost inside the demand array throughout the greedy and local-search
heuristics.
"""

from __future__ import annotations

import argparse
import json
import math
import random
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
    omega_odd: List[int]
    c0: List[int]
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
    omega_odd = [0] * (n + 1)
    for p in odd_primes:
        for m in range(p, n + 1, p):
            omega_odd[m] += 1

    c0 = [0] * (n + 1)
    raw_base = [0] * (n + 1)
    demand = [0] * (n + 1)
    for m in range(1, n + 1):
        c0[m] = (m & 1) + omega_odd[m]
        raw_base[m] = 2 - c0[m]
        demand[m] = max(0, raw_base[m])
    return Baseline(n, primes, odd_primes, omega_odd, c0, raw_base, demand)


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
    return SearchState(n, list(raw), demand, hits, residual, total)


def make_fixed_state(baseline: Baseline, switched: Sequence[int]) -> SearchState:
    raw = baseline.raw_base[:]
    for p in switched:
        for m in range(p, baseline.n + 1, p):
            raw[m] += 1
    return make_state_from_raw(baseline.n, raw)


def positive_points(values: Sequence[int]) -> int:
    return sum(1 for value in values[1:] if value > 0)


def max_positive(values: Sequence[int]) -> int:
    return max(values[1:], default=0)


def is_power_of_two(m: int) -> bool:
    return m > 0 and (m & (m - 1)) == 0


def classify_baseline(baseline: Baseline) -> Dict[str, Dict[str, int]]:
    stats: Dict[str, Dict[str, int]] = {}

    def add(name: str, tokens: int) -> None:
        row = stats.setdefault(name, {"points": 0, "tokens": 0})
        row["points"] += 1
        row["tokens"] += tokens

    for m in range(1, baseline.n + 1):
        tokens = baseline.demand[m]
        if tokens <= 0:
            continue
        if m == 1:
            add("one", tokens)
        elif is_power_of_two(m):
            add("powers_of_two", tokens)
        elif m % 2 == 0 and baseline.omega_odd[m] == 1:
            add("even_one_odd_prime_factor", tokens)
        else:
            add("other_positive", tokens)
    return dict(sorted(stats.items()))


def baseline_summary(n: int) -> Dict[str, object]:
    baseline = build_baseline(n)
    return {
        "n": n,
        "primes": len(baseline.primes),
        "odd_primes": len(baseline.odd_primes),
        "baseline_tokens": sum(baseline.demand[1:]),
        "baseline_points": positive_points(baseline.demand),
        "baseline_max_demand": max_positive(baseline.demand),
        "baseline_demand_histogram": histogram(baseline.demand[1:]),
        "classification": classify_baseline(baseline),
    }


def parse_int_list(spec: str) -> List[int]:
    return [int(part.strip()) for part in spec.split(",") if part.strip()]


def parse_pool_spec(n: int, odd_primes: Sequence[int], spec: str) -> Tuple[str, List[int]]:
    text = spec.strip().lower()
    if text in {"all", "all-odd", "odd"}:
        return "all-odd", list(odd_primes)
    if text in {"le-half", "<=n/2", "half", "upto-half"}:
        return "le-half", [p for p in odd_primes if p <= n // 2]
    if text.startswith("block:"):
        k = int(text.split(":", 1)[1])
        if k < 1:
            raise ValueError("block:K requires K >= 1")
        lo = n / (k + 1)
        hi = n / k
        return f"block:{k}", [p for p in odd_primes if lo < p <= hi]
    if text.startswith("le-n/"):
        k = int(text.split("/", 1)[1])
        if k < 1:
            raise ValueError("le-n/K requires K >= 1")
        return f"le-n/{k}", [p for p in odd_primes if p <= n / k]
    if text.startswith("frac:"):
        parts = text.split(":")
        if len(parts) != 3:
            raise ValueError("frac pools use frac:LOW:HIGH")
        low = float(parts[1])
        high = float(parts[2])
        if low < 0 or high <= low:
            raise ValueError("frac:LOW:HIGH requires 0 <= LOW < HIGH")
        return f"frac:{low:g}:{high:g}", [p for p in odd_primes if low * n < p <= high * n]
    if text.startswith("range:"):
        parts = text.split(":")
        if len(parts) != 3:
            raise ValueError("range pools use range:LOW:HIGH")
        low = int(parts[1])
        high = int(parts[2])
        if low < 0 or high < low:
            raise ValueError("range:LOW:HIGH requires 0 <= LOW <= HIGH")
        return f"range:{low}:{high}", [p for p in odd_primes if low < p <= high]
    raise ValueError(f"unknown pool spec: {spec}")


def random_medium_pool(
    n: int,
    odd_primes: Sequence[int],
    count: int,
    seed: int,
    low_frac: float,
    high_frac: float,
) -> Tuple[str, List[int]]:
    if count < 0:
        raise ValueError("random count must be nonnegative")
    if low_frac < 0 or high_frac <= low_frac:
        raise ValueError("random fraction window must satisfy 0 <= low < high")
    pool = [p for p in odd_primes if low_frac * n < p <= high_frac * n]
    rng = random.Random(seed)
    sample_size = min(count, len(pool))
    chosen = sorted(rng.sample(pool, sample_size))
    return f"random:{low_frac:g}:{high_frac:g}:count={sample_size}:seed={seed}", chosen


def residue_gain(n: int, residual: Sequence[int], p: int, a: int) -> int:
    if a <= 0:
        return 0
    return sum(1 for m in range(a, n + 1, p) if residual[m] > 0)


def best_residue(
    n: int,
    residual: Sequence[int],
    p: int,
    rng: Optional[random.Random] = None,
    prefer: Optional[int] = None,
) -> Tuple[int, int]:
    gains = [0] * p
    for m in range(1, n + 1):
        if residual[m] > 0:
            a = m % p
            if a:
                gains[a] += 1
    best = max(gains[1:], default=0)
    if prefer is not None and 0 < prefer < p and gains[prefer] == best:
        return prefer, best
    residues = [a for a in range(1, p) if gains[a] == best]
    if not residues:
        return 1, 0
    if rng is not None and len(residues) > 1:
        return rng.choice(residues), best
    return residues[0], best


def apply_residue(state: SearchState, p: int, a: int, delta: int) -> int:
    """Change hit counts for residue a mod p. Returns deficit delta."""
    if not (0 < a < p):
        raise ValueError("switched residues must be nonzero")
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
    """Add or remove the L_R contribution for p. Returns deficit delta."""
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
    """Exact residual increase from adding p to R before choosing b_p."""
    penalty = 0
    for m in range(p, state.n + 1, p):
        if state.raw[m] >= 0:
            old = state.residual[m]
            new = max(0, state.demand[m] + 1 - state.hits[m])
            penalty += new - old
    return penalty


def fixed_greedy(
    baseline: Baseline,
    switched: Sequence[int],
    order: str,
    seed: Optional[int],
) -> Tuple[SearchState, Assignment, Dict[str, object]]:
    state = make_fixed_state(baseline, switched)
    assignment: Assignment = {}
    rng = random.Random(seed) if seed is not None else None
    initial_tokens = state.total_deficit
    total_gain = 0
    positive_steps = 0
    zero_steps = 0

    primes = list(switched)
    if order == "ascending":
        primes.sort()
    elif order == "descending":
        primes.sort(reverse=True)
    elif order == "initial-gain":
        scored = []
        for p in primes:
            a, gain = best_residue(baseline.n, state.residual, p, rng)
            scored.append((gain, -p, p, a))
        scored.sort(reverse=True)
        primes = [p for _, _, p, _ in scored]
    elif order == "dynamic":
        remaining = set(primes)
        while remaining:
            best: Optional[Tuple[int, int, int]] = None
            for p in sorted(remaining):
                a, gain = best_residue(baseline.n, state.residual, p, rng)
                candidate = (gain, -p, a)
                if best is None or candidate > best:
                    best = candidate
            assert best is not None
            gain, neg_p, a = best
            p = -neg_p
            if gain <= 0:
                for leftover in sorted(remaining):
                    a0, _ = best_residue(baseline.n, state.residual, leftover, rng)
                    assignment[leftover] = a0
                    apply_residue(state, leftover, a0, +1)
                    zero_steps += 1
                break
            assignment[p] = a
            apply_residue(state, p, a, +1)
            total_gain += gain
            positive_steps += 1
            remaining.remove(p)
        trace = {
            "strategy": "fixed",
            "order": order,
            "initial_exact_tokens": initial_tokens,
            "greedy_gain": total_gain,
            "positive_gain_steps": positive_steps,
            "zero_gain_steps": zero_steps,
        }
        return state, assignment, trace
    else:
        raise ValueError("order must be ascending, descending, initial-gain, or dynamic")

    for p in primes:
        a, gain = best_residue(baseline.n, state.residual, p, rng)
        assignment[p] = a
        apply_residue(state, p, a, +1)
        total_gain += gain
        if gain > 0:
            positive_steps += 1
        else:
            zero_steps += 1

    trace = {
        "strategy": "fixed",
        "order": order,
        "initial_exact_tokens": initial_tokens,
        "greedy_gain": total_gain,
        "positive_gain_steps": positive_steps,
        "zero_gain_steps": zero_steps,
    }
    return state, assignment, trace


def net_greedy(
    baseline: Baseline,
    pool: Sequence[int],
    seed: Optional[int],
    max_switches: int,
    min_net_gain: int,
) -> Tuple[SearchState, Assignment, Dict[str, object]]:
    state = make_state_from_raw(baseline.n, baseline.raw_base)
    assignment: Assignment = {}
    rng = random.Random(seed) if seed is not None else None
    remaining = set(pool)
    total_net = 0
    total_gross = 0
    total_penalty = 0
    iterations = 0
    stopped_reason = "pool exhausted"
    last_best: Optional[Dict[str, int]] = None

    while remaining:
        if max_switches and len(assignment) >= max_switches:
            stopped_reason = "max switches reached"
            break
        best: Optional[Tuple[int, int, int, int, int]] = None
        for p in sorted(remaining):
            penalty = switching_penalty(state, p)
            a, gross = best_residue(baseline.n, state.residual, p, rng)
            net = gross - penalty
            candidate = (net, gross, -penalty, -p, a)
            if best is None or candidate > best:
                best = candidate
        assert best is not None
        net, gross, neg_penalty, neg_p, a = best
        p = -neg_p
        penalty = -neg_penalty
        last_best = {"p": p, "a": a, "net": net, "gross": gross, "penalty": penalty}
        if net < min_net_gain:
            stopped_reason = "no candidate met min net gain"
            break
        apply_switch_requirement(state, p, +1)
        apply_residue(state, p, a, +1)
        assignment[p] = a
        remaining.remove(p)
        total_net += net
        total_gross += gross
        total_penalty += penalty
        iterations += 1

    trace = {
        "strategy": "net-greedy",
        "initial_exact_tokens": sum(baseline.demand[1:]),
        "iterations": iterations,
        "min_net_gain": min_net_gain,
        "max_switches": max_switches,
        "total_net_gain": total_net,
        "total_gross_gain": total_gross,
        "total_switch_penalty": total_penalty,
        "stopped_reason": stopped_reason,
        "last_best": last_best,
    }
    return state, assignment, trace


def local_refine(
    state: SearchState,
    assignment: Assignment,
    passes: int,
    seed: Optional[int],
) -> List[Dict[str, int]]:
    rows: List[Dict[str, int]] = []
    rng = random.Random(seed) if seed is not None else None
    for pass_index in range(1, passes + 1):
        before = state.total_deficit
        changed = 0
        for p in sorted(assignment):
            old_a = assignment[p]
            apply_residue(state, p, old_a, -1)
            new_a, _ = best_residue(state.n, state.residual, p, rng, prefer=old_a)
            apply_residue(state, p, new_a, +1)
            if new_a != old_a:
                assignment[p] = new_a
                changed += 1
        row = {
            "pass": pass_index,
            "deficit_before": before,
            "deficit_after": state.total_deficit,
            "improvement": before - state.total_deficit,
            "changed_residues": changed,
        }
        rows.append(row)
        if row["improvement"] <= 0 and changed == 0:
            break
    return rows


def score_assignment(baseline: Baseline, assignment: Assignment) -> Dict[str, object]:
    state = make_fixed_state(baseline, sorted(assignment))
    for p, a in assignment.items():
        apply_residue(state, p, a, +1)
    misses = [m for m in range(1, baseline.n + 1) if state.residual[m] > 0]
    return {
        "deficit": state.total_deficit,
        "uncovered_points": len(misses),
        "max_residual": max_positive(state.residual),
        "first_misses": misses[:20],
    }


def compact_result(result: Dict[str, object]) -> Dict[str, object]:
    return {
        "n": result["n"],
        "pool": result["pool"],
        "selection": result["selection"],
        "pool_size": result["pool_size"],
        "switched": result["switched"],
        "initial_exact_tokens": result["initial_exact_tokens"],
        "after_greedy_deficit": result["after_greedy_deficit"],
        "final_deficit": result["final_deficit"],
        "final_uncovered_points": result["final_uncovered_points"],
        "max_residual": result["max_residual"],
        "local_improvement": result["local_improvement"],
        "seconds": result["seconds"],
    }


def run_strategy(
    n: int,
    pool_label: str,
    pool: Sequence[int],
    selection: str,
    order: str,
    seed: Optional[int],
    local_passes: int,
    max_switches: int,
    min_net_gain: int,
    show_assignment: bool,
) -> Dict[str, object]:
    baseline = build_baseline(n)
    start = time.perf_counter()
    if selection == "fixed":
        state, assignment, trace = fixed_greedy(baseline, pool, order, seed)
    elif selection == "net-greedy":
        state, assignment, trace = net_greedy(baseline, pool, seed, max_switches, min_net_gain)
    else:
        raise ValueError("selection must be fixed or net-greedy")

    after_greedy = state.total_deficit
    local_rows = local_refine(state, assignment, local_passes, seed) if local_passes else []
    verification = score_assignment(baseline, assignment)
    seconds = time.perf_counter() - start
    if verification["deficit"] != state.total_deficit:
        raise RuntimeError(
            f"verification mismatch: state={state.total_deficit}, checked={verification['deficit']}"
        )

    switched = sorted(assignment)
    result: Dict[str, object] = {
        "n": n,
        "pool": pool_label,
        "selection": selection,
        "pool_size": len(pool),
        "switched": len(switched),
        "switched_min": switched[0] if switched else None,
        "switched_max": switched[-1] if switched else None,
        "baseline_tokens": sum(baseline.demand[1:]),
        "baseline_points": positive_points(baseline.demand),
        "initial_exact_tokens": trace["initial_exact_tokens"],
        "after_greedy_deficit": after_greedy,
        "final_deficit": state.total_deficit,
        "final_uncovered_points": verification["uncovered_points"],
        "max_residual": verification["max_residual"],
        "first_misses": verification["first_misses"],
        "local_passes": local_rows,
        "local_improvement": after_greedy - state.total_deficit,
        "trace": trace,
        "seconds": round(seconds, 6),
    }
    if show_assignment:
        result["assignment"] = dict(sorted(assignment.items()))
    return result


def print_json(payload: object) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def command_baseline(args: argparse.Namespace) -> None:
    print_json(baseline_summary(args.n))


def command_run(args: argparse.Namespace) -> None:
    baseline = build_baseline(args.n)
    label, pool = parse_pool_spec(args.n, baseline.odd_primes, args.pool)
    result = run_strategy(
        args.n,
        label,
        pool,
        args.selection,
        args.order,
        args.seed,
        args.local_passes,
        args.max_switches,
        args.min_net_gain,
        args.show_assignment,
    )
    print_json(result)


def command_random(args: argparse.Namespace) -> None:
    baseline = build_baseline(args.n)
    label, pool = random_medium_pool(
        args.n,
        baseline.odd_primes,
        args.count,
        args.seed,
        args.low_frac,
        args.high_frac,
    )
    result = run_strategy(
        args.n,
        label,
        pool,
        args.selection,
        args.order,
        args.seed,
        args.local_passes,
        args.max_switches,
        args.min_net_gain,
        args.show_assignment,
    )
    print_json(result)


def command_suite(args: argparse.Namespace) -> None:
    baseline = build_baseline(args.n)
    selections = ["fixed", "net-greedy"] if args.selection == "both" else [args.selection]
    rows: List[Dict[str, object]] = []

    for k in parse_int_list(args.blocks):
        label, pool = parse_pool_spec(args.n, baseline.odd_primes, f"block:{k}")
        for selection in selections:
            result = run_strategy(
                args.n,
                label,
                pool,
                selection,
                args.order,
                args.seed,
                args.local_passes,
                args.max_switches,
                args.min_net_gain,
                False,
            )
            rows.append(compact_result(result))

    label, pool = parse_pool_spec(args.n, baseline.odd_primes, "le-half")
    for selection in selections:
        result = run_strategy(
            args.n,
            label,
            pool,
            selection,
            args.order,
            args.seed,
            args.local_passes,
            args.max_switches,
            args.min_net_gain,
            False,
        )
        rows.append(compact_result(result))

    for trial in range(args.random_trials):
        trial_seed = args.seed + trial
        label, pool = random_medium_pool(
            args.n,
            baseline.odd_primes,
            args.random_count,
            trial_seed,
            args.random_low_frac,
            args.random_high_frac,
        )
        for selection in selections:
            result = run_strategy(
                args.n,
                label,
                pool,
                selection,
                args.order,
                trial_seed,
                args.local_passes,
                args.max_switches,
                args.min_net_gain,
                False,
            )
            rows.append(compact_result(result))

    print_json(
        {
            "n": args.n,
            "baseline_tokens": sum(baseline.demand[1:]),
            "baseline_points": positive_points(baseline.demand),
            "rows": rows,
        }
    )


def add_strategy_args(parser: argparse.ArgumentParser, include_seed: bool = True) -> None:
    parser.add_argument(
        "--selection",
        choices=["fixed", "net-greedy"],
        default="fixed",
        help="Use all primes in the pool, or greedily choose a positive-net subset.",
    )
    parser.add_argument(
        "--order",
        choices=["ascending", "descending", "initial-gain", "dynamic"],
        default="initial-gain",
        help="Residue assignment order for --selection fixed.",
    )
    if include_seed:
        parser.add_argument("--seed", type=int, default=None, help="Seed for tie-breaking.")
    parser.add_argument("--local-passes", type=int, default=2, help="Coordinate-refinement passes.")
    parser.add_argument("--max-switches", type=int, default=0, help="Limit net-greedy switches; 0 means no cap.")
    parser.add_argument("--min-net-gain", type=int, default=1, help="Minimum exact net gain for net-greedy.")
    parser.add_argument("--show-assignment", action="store_true", help="Print the final switched residues.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Standard-library parity-first switching experiment for Erdos Problem 689."
    )
    parser.add_argument("--version", action="version", version="parity_switch_experiment.py 1.0")
    sub = parser.add_subparsers(dest="command", required=True)

    baseline = sub.add_parser("baseline", help="Report parity-first baseline demand.")
    baseline.add_argument("--n", type=int, required=True)
    baseline.set_defaults(func=command_baseline)

    run = sub.add_parser("run", help="Run one fixed-pool switching experiment.")
    run.add_argument("--n", type=int, required=True)
    run.add_argument(
        "--pool",
        required=True,
        help="Pool spec: block:K, le-half, all-odd, le-n/K, frac:LOW:HIGH, or range:LOW:HIGH.",
    )
    add_strategy_args(run)
    run.set_defaults(func=command_run)

    random_cmd = sub.add_parser("random", help="Run one random medium-prime switching experiment.")
    random_cmd.add_argument("--n", type=int, required=True)
    random_cmd.add_argument("--count", type=int, required=True)
    random_cmd.add_argument("--seed", type=int, required=True, help="Seed for sampling and tie-breaking.")
    random_cmd.add_argument("--low-frac", type=float, default=0.05)
    random_cmd.add_argument("--high-frac", type=float, default=0.5)
    add_strategy_args(random_cmd, include_seed=False)
    random_cmd.set_defaults(func=command_random)

    suite = sub.add_parser("suite", help="Run block, half, and random medium-prime experiments.")
    suite.add_argument("--n", type=int, required=True)
    suite.add_argument("--blocks", default="2,3,4,5,8,12,16")
    suite.add_argument("--selection", choices=["fixed", "net-greedy", "both"], default="both")
    suite.add_argument(
        "--order",
        choices=["ascending", "descending", "initial-gain", "dynamic"],
        default="initial-gain",
    )
    suite.add_argument("--seed", type=int, default=689)
    suite.add_argument("--local-passes", type=int, default=2)
    suite.add_argument("--max-switches", type=int, default=0)
    suite.add_argument("--min-net-gain", type=int, default=1)
    suite.add_argument("--random-trials", type=int, default=3)
    suite.add_argument("--random-count", type=int, default=80)
    suite.add_argument("--random-low-frac", type=float, default=0.05)
    suite.add_argument("--random-high-frac", type=float, default=0.5)
    suite.set_defaults(func=command_suite)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, "n") and args.n <= 0:
        parser.error("--n must be positive")
    if hasattr(args, "local_passes") and args.local_passes < 0:
        parser.error("--local-passes must be nonnegative")
    if hasattr(args, "max_switches") and args.max_switches < 0:
        parser.error("--max-switches must be nonnegative")
    if hasattr(args, "min_net_gain") and args.min_net_gain < 0:
        parser.error("--min-net-gain must be nonnegative")
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
