#!/usr/bin/env python3
"""Computational exploration for Erdos Problem 689.

Problem 689 asks whether, for all sufficiently large n, one can choose one
residue class modulo every prime p <= n so that each m in [1,n] is hit at
least twice.

This script focuses on the zero-residue staging discussed in the working
notes:

  * set a_p = 0 for primes p <= y;
  * compute residual demands d_y(m) = max(0, r - omega_y(m));
  * try to cover those residual demands using primes y < p <= n.

The heuristics here are exploratory only. A greedy failure is not a
certificate of impossibility.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import random
import sys
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


Demand = List[int]
Assignment = Dict[int, int]


def primes_up_to(n: int) -> List[int]:
    """Return all primes <= n by sieve."""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def parse_y(n: int, y_spec: str, z: Optional[float] = None) -> int:
    """Parse a y specification: integer, sqrt, n/z, or all."""
    spec = str(y_spec).strip().lower()
    if spec == "sqrt":
        return math.isqrt(n)
    if spec == "all":
        return n
    if spec in {"none", "0"}:
        return 0
    if spec in {"n/z", "n_over_z"}:
        if not z or z <= 0:
            raise ValueError("--z must be positive when --y n/z is used")
        return max(0, int(n / z))
    y = int(spec)
    if y < 0:
        raise ValueError("y must be nonnegative")
    return min(y, n)


def detect_optional_solvers() -> Dict[str, bool]:
    """Report optional exact-optimization packages if already installed."""
    def available(module: str) -> bool:
        try:
            return importlib.util.find_spec(module) is not None
        except ModuleNotFoundError:
            return False

    return {
        "scipy": available("scipy.optimize"),
        "pulp": available("pulp"),
        "ortools": available("ortools"),
        "z3": available("z3"),
    }


def residual_demands(n: int, y: int, r: int = 2) -> Tuple[Demand, List[int], List[int]]:
    """Compute d_y(m) after fixing zero residues for primes p <= y.

    Returns (demand, omega_y, small_primes), indexed by m with slot 0 unused.
    """
    small_primes = primes_up_to(min(y, n))
    omega = [0] * (n + 1)
    for p in small_primes:
        for m in range(p, n + 1, p):
            omega[m] += 1
    demand = [0] * (n + 1)
    for m in range(1, n + 1):
        demand[m] = max(0, r - omega[m])
    return demand, omega, small_primes


def total_deficit(demand: Demand) -> int:
    return sum(demand[1:])


def uncovered_count(demand: Demand) -> int:
    return sum(1 for x in demand[1:] if x > 0)


def demand_histogram(demand: Demand) -> Dict[int, int]:
    hist: Dict[int, int] = {}
    for x in demand[1:]:
        hist[x] = hist.get(x, 0) + 1
    return dict(sorted(hist.items()))


def least_prime_factors(n: int) -> List[int]:
    lpf = [0] * (n + 1)
    for i in range(2, n + 1):
        if lpf[i] == 0:
            lpf[i] = i
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    if lpf[j] == 0:
                        lpf[j] = i
    return lpf


def factor_distinct(m: int, lpf: Sequence[int]) -> List[Tuple[int, int]]:
    """Factor m as distinct prime powers using a least-prime-factor table."""
    out: List[Tuple[int, int]] = []
    while m > 1:
        p = lpf[m] or m
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        out.append((p, e))
    return out


def classify_residuals(n: int, y: int, demand: Demand, omega: Sequence[int]) -> Dict[str, Dict[str, int]]:
    """Classify positive residual-demand points into coarse arithmetic types."""
    lpf = least_prime_factors(n)
    stats: Dict[str, Dict[str, int]] = {}

    def add(name: str, d: int) -> None:
        if name not in stats:
            stats[name] = {"points": 0, "tokens": 0}
        stats[name]["points"] += 1
        stats[name]["tokens"] += d

    for m in range(1, n + 1):
        d = demand[m]
        if d <= 0:
            continue
        if m == 1:
            add("one", d)
            continue
        fac = factor_distinct(m, lpf)
        if len(fac) == 1:
            p, e = fac[0]
            add("prime" if e == 1 else "prime_power", d)
            continue
        small_distinct = sum(1 for p, _ in fac if p <= y)
        large_distinct = len(fac) - small_distinct
        if small_distinct == 1 and large_distinct == 1:
            add("one_small_one_large", d)
        elif small_distinct == 1:
            add("one_small_other", d)
        elif small_distinct == 0:
            add("all_large_composite", d)
        else:
            add("other_positive", d)
    return dict(sorted(stats.items()))


def residue_gain(n: int, demand: Demand, p: int, a: int) -> int:
    return sum(1 for m in range(a if a else p, n + 1, p) if demand[m] > 0)


def best_residue(n: int, demand: Demand, p: int, rng: Optional[random.Random] = None) -> Tuple[int, int]:
    """Return a residue modulo p with maximum current gain."""
    gains = [0] * p
    for m in range(1, n + 1):
        if demand[m] > 0:
            gains[m % p] += 1
    best = max(gains)
    residues = [a for a, g in enumerate(gains) if g == best]
    if rng is not None and len(residues) > 1:
        return rng.choice(residues), best
    return residues[0], best


def apply_residue(n: int, demand: Demand, p: int, a: int, delta: int = -1) -> int:
    """Apply or remove a chosen residue. Returns positive coverage gain.

    With delta=-1, positive demands hit by this class are decreased by one.
    With delta=+1, this undoes a previous application up to the natural cap
    used by coordinate_refine.
    """
    changed = 0
    start = a if a else p
    for m in range(start, n + 1, p):
        if delta < 0:
            if demand[m] > 0:
                demand[m] -= 1
                changed += 1
        else:
            demand[m] += 1
            changed += 1
    return changed


def build_coverage_from_assignment(
    n: int,
    base_demand: Demand,
    assignment: Assignment,
) -> Demand:
    demand = base_demand[:]
    for p, a in assignment.items():
        apply_residue(n, demand, p, a, -1)
    return demand


def reservoir_primes(n: int, y: int, cap: Optional[float] = None) -> List[int]:
    upper = n if cap is None else min(n, int(math.floor(cap * y)))
    return [p for p in primes_up_to(n) if y < p <= upper]


@dataclass
class GreedyResult:
    n: int
    y: int
    r: int
    primes_used: int
    total_deficit: int
    uncovered_points: int
    assignments: Assignment
    stages: List[Dict[str, int]]


def greedy_cover(
    n: int,
    y: int,
    r: int = 2,
    cap: Optional[float] = None,
    stages: Optional[Sequence[str]] = None,
    seed: Optional[int] = None,
    shuffle_primes: bool = False,
) -> GreedyResult:
    base, _, _ = residual_demands(n, y, r)
    demand = base[:]
    rng = random.Random(seed) if seed is not None else None
    assignment: Assignment = {}
    stage_rows: List[Dict[str, int]] = []

    if stages:
        stage_caps: List[Optional[float]] = []
        for item in stages:
            item = item.strip().lower()
            stage_caps.append(None if item == "all" else float(item))
    else:
        stage_caps = [cap]

    used: set[int] = set()
    for stage_cap in stage_caps:
        candidates = reservoir_primes(n, y, stage_cap)
        candidates = [p for p in candidates if p not in used]
        if shuffle_primes and rng is not None:
            rng.shuffle(candidates)
        else:
            candidates.sort()
        before = total_deficit(demand)
        for p in candidates:
            a, gain = best_residue(n, demand, p, rng)
            assignment[p] = a
            used.add(p)
            if gain:
                apply_residue(n, demand, p, a, -1)
        after = total_deficit(demand)
        stage_rows.append(
            {
                "cap": -1 if stage_cap is None else int(round(stage_cap * 1000)),
                "new_primes": len(candidates),
                "deficit_before": before,
                "deficit_after": after,
                "uncovered_after": uncovered_count(demand),
            }
        )
    return GreedyResult(
        n=n,
        y=y,
        r=r,
        primes_used=len(assignment),
        total_deficit=total_deficit(demand),
        uncovered_points=uncovered_count(demand),
        assignments=assignment,
        stages=stage_rows,
    )


def coordinate_refine(
    n: int,
    y: int,
    assignment: Assignment,
    r: int = 2,
    passes: int = 2,
    seed: Optional[int] = None,
) -> Tuple[Assignment, Demand, List[Dict[str, int]]]:
    """Local search over already-used primes.

    This is intentionally conservative: it only changes residues of primes
    already selected by greedy_cover, and it accepts the best residue for each
    prime in a fixed sweep. It is still a heuristic, not a proof.
    """
    base, _, _ = residual_demands(n, y, r)
    current = build_coverage_from_assignment(n, base, assignment)
    rng = random.Random(seed) if seed is not None else random.Random(0)
    primes = list(assignment)
    rows: List[Dict[str, int]] = []
    for pass_index in range(1, passes + 1):
        rng.shuffle(primes)
        before = total_deficit(current)
        for p in primes:
            # Rebuild rather than attempting an exact inverse, because some
            # covered points may have had demand > 1 before this prime was used.
            old = assignment[p]
            del assignment[p]
            without_p = build_coverage_from_assignment(n, base, assignment)
            a, _ = best_residue(n, without_p, p, rng)
            assignment[p] = a
            current = without_p
            apply_residue(n, current, p, a, -1)
            _ = old
        rows.append(
            {
                "pass": pass_index,
                "deficit_before": before,
                "deficit_after": total_deficit(current),
                "uncovered_after": uncovered_count(current),
            }
        )
        if total_deficit(current) >= before:
            # Additional passes usually churn when no improvement appears.
            break
    return assignment, current, rows


class SearchTimeout(RuntimeError):
    pass


@dataclass
class ExactResult:
    status: str
    n: int
    y: int
    r: int
    nodes: int
    seconds: float
    assignment: Optional[Assignment]
    final_deficit: int
    message: str


class BacktrackingSolver:
    def __init__(
        self,
        n: int,
        y: int,
        r: int = 2,
        cap: Optional[float] = None,
        time_limit: float = 10.0,
        node_limit: int = 200_000,
    ) -> None:
        self.n = n
        self.y = y
        self.r = r
        self.cap = cap
        self.time_limit = time_limit
        self.node_limit = node_limit
        self.base, _, _ = residual_demands(n, y, r)
        self.primes = tuple(reservoir_primes(n, y, cap))
        self.start = 0.0
        self.nodes = 0
        self.memo: set[Tuple[Tuple[int, ...], Tuple[int, ...]]] = set()

    def solve(self) -> ExactResult:
        self.start = time.perf_counter()
        try:
            assignment = self._dfs(tuple(self.base[1:]), self.primes)
            seconds = time.perf_counter() - self.start
            if assignment is None:
                return ExactResult(
                    "infeasible",
                    self.n,
                    self.y,
                    self.r,
                    self.nodes,
                    seconds,
                    None,
                    total_deficit(self.base),
                    "No staged cover exists for this fixed zero stage and reservoir.",
                )
            final = build_coverage_from_assignment(self.n, self.base, assignment)
            return ExactResult(
                "covered",
                self.n,
                self.y,
                self.r,
                self.nodes,
                seconds,
                assignment,
                total_deficit(final),
                "Found an exact staged cover.",
            )
        except SearchTimeout as exc:
            final_deficit = total_deficit(self.base)
            return ExactResult(
                "unknown",
                self.n,
                self.y,
                self.r,
                self.nodes,
                time.perf_counter() - self.start,
                None,
                final_deficit,
                str(exc),
            )

    def _check_limits(self) -> None:
        if self.nodes >= self.node_limit:
            raise SearchTimeout(f"node limit {self.node_limit} reached")
        if time.perf_counter() - self.start > self.time_limit:
            raise SearchTimeout(f"time limit {self.time_limit:.2f}s reached")

    def _best_possible_gain_sum(self, demands: Tuple[int, ...], remaining: Tuple[int, ...]) -> int:
        demand_list = [0] + list(demands)
        total = 0
        for p in remaining:
            _, gain = best_residue(self.n, demand_list, p)
            total += gain
        return total

    def _apply_tuple(self, demands: Tuple[int, ...], p: int, a: int) -> Tuple[int, ...]:
        arr = list(demands)
        start = a if a else p
        for m in range(start, self.n + 1, p):
            idx = m - 1
            if arr[idx] > 0:
                arr[idx] -= 1
        return tuple(arr)

    def _gain_tuple(self, demands: Tuple[int, ...], p: int, a: int) -> int:
        start = a if a else p
        return sum(1 for m in range(start, self.n + 1, p) if demands[m - 1] > 0)

    def _dfs(self, demands: Tuple[int, ...], remaining: Tuple[int, ...]) -> Optional[Assignment]:
        self._check_limits()
        self.nodes += 1
        deficit = sum(demands)
        if deficit == 0:
            return {}
        if not remaining:
            return None
        max_demand = max(demands)
        if max_demand > len(remaining):
            return None
        key = (demands, remaining)
        if key in self.memo:
            return None
        if self._best_possible_gain_sum(demands, remaining) < deficit:
            self.memo.add(key)
            return None

        # Pick a currently deficient point with largest demand; tie-break by
        # largest immediate aggregate gains across remaining primes.
        targets = [i + 1 for i, d in enumerate(demands) if d > 0]
        target = max(
            targets,
            key=lambda m: (
                demands[m - 1],
                sum(self._gain_tuple(demands, p, m % p) for p in remaining),
                -m,
            ),
        )

        options = []
        for index, p in enumerate(remaining):
            a = target % p
            gain = self._gain_tuple(demands, p, a)
            options.append((gain, p, a, index))
        options.sort(reverse=True)

        for _, p, a, index in options:
            next_demands = self._apply_tuple(demands, p, a)
            next_remaining = remaining[:index] + remaining[index + 1 :]
            result = self._dfs(next_demands, next_remaining)
            if result is not None:
                result[p] = a
                return result
        self.memo.add(key)
        return None


def make_summary(n: int, y: int, r: int) -> Dict[str, object]:
    demand, omega, small = residual_demands(n, y, r)
    return {
        "n": n,
        "y": y,
        "r": r,
        "small_primes": len(small),
        "total_residual_tokens": total_deficit(demand),
        "positive_residual_points": uncovered_count(demand),
        "demand_histogram": demand_histogram(demand),
        "classification": classify_residuals(n, y, demand, omega),
    }


def print_json(obj: object) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True))


def command_residual(args: argparse.Namespace) -> None:
    y = parse_y(args.n, args.y, args.z)
    print_json(make_summary(args.n, y, args.r))


def command_greedy(args: argparse.Namespace) -> None:
    y = parse_y(args.n, args.y, args.z)
    stages = [x for x in args.stages.split(",") if x.strip()] if args.stages else None
    result = greedy_cover(
        args.n,
        y,
        args.r,
        cap=args.cap,
        stages=stages,
        seed=args.seed,
        shuffle_primes=args.shuffle,
    )
    payload: Dict[str, object] = {
        "n": result.n,
        "y": result.y,
        "r": result.r,
        "primes_used": result.primes_used,
        "total_deficit": result.total_deficit,
        "uncovered_points": result.uncovered_points,
        "stages": result.stages,
    }
    if args.refine_passes:
        assignment, demand, rows = coordinate_refine(
            args.n,
            y,
            result.assignments.copy(),
            args.r,
            args.refine_passes,
            args.seed,
        )
        payload["after_refine"] = {
            "passes": rows,
            "total_deficit": total_deficit(demand),
            "uncovered_points": uncovered_count(demand),
            "primes_used": len(assignment),
        }
    if args.show_assignment:
        payload["assignment"] = dict(sorted(result.assignments.items()))
    print_json(payload)


def command_exact(args: argparse.Namespace) -> None:
    y = parse_y(args.n, args.y, args.z)
    if args.list_solvers:
        print_json({"optional_solvers_detected": detect_optional_solvers()})
    solver = BacktrackingSolver(
        args.n,
        y,
        args.r,
        cap=args.cap,
        time_limit=args.time_limit,
        node_limit=args.node_limit,
    )
    result = solver.solve()
    payload: Dict[str, object] = {
        "status": result.status,
        "n": result.n,
        "y": result.y,
        "r": result.r,
        "nodes": result.nodes,
        "seconds": round(result.seconds, 6),
        "initial_residual_tokens": total_deficit(solver.base),
        "final_deficit": result.final_deficit,
        "message": result.message,
        "reservoir_primes": len(solver.primes),
    }
    if args.show_assignment and result.assignment is not None:
        payload["assignment"] = dict(sorted(result.assignment.items()))
    print_json(payload)


def command_sweep(args: argparse.Namespace) -> None:
    ns = [int(x) for x in args.ns.split(",") if x.strip()]
    rows = []
    for n in ns:
        y = parse_y(n, args.y, args.z)
        demand, omega, small = residual_demands(n, y, args.r)
        greedy = greedy_cover(n, y, args.r, cap=args.cap, seed=args.seed)
        row: Dict[str, object] = {
            "n": n,
            "y": y,
            "small_primes": len(small),
            "initial_tokens": total_deficit(demand),
            "initial_points": uncovered_count(demand),
            "greedy_primes": greedy.primes_used,
            "greedy_deficit": greedy.total_deficit,
            "greedy_points": greedy.uncovered_points,
        }
        if args.exact_up_to and n <= args.exact_up_to:
            exact = BacktrackingSolver(
                n,
                y,
                args.r,
                cap=args.cap,
                time_limit=args.time_limit,
                node_limit=args.node_limit,
            ).solve()
            row["exact_status"] = exact.status
            row["exact_nodes"] = exact.nodes
            row["exact_seconds"] = round(exact.seconds, 6)
        rows.append(row)
    print_json(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore residual covering computations for Erdos Problem 689."
    )
    parser.add_argument("--version", action="version", version="explore_689.py 1.0")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--n", type=int, required=True, help="Interval endpoint.")
        p.add_argument("--y", default="sqrt", help="Zero-stage cutoff: sqrt, n/z, none, all, or integer.")
        p.add_argument("--z", type=float, default=None, help="Parameter for --y n/z.")
        p.add_argument("--r", type=int, default=2, help="Required multiplicity; default 2.")

    residual = sub.add_parser("residual", help="Compute residual demands after zero-residue stage.")
    add_common(residual)
    residual.set_defaults(func=command_residual)

    greedy = sub.add_parser("greedy", help="Run greedy/staged residual-cover heuristics.")
    add_common(greedy)
    greedy.add_argument("--cap", type=float, default=None, help="Use primes y < p <= cap*y; default all p <= n.")
    greedy.add_argument("--stages", default=None, help="Comma-separated cumulative caps, e.g. 1.5,2,4,all.")
    greedy.add_argument("--seed", type=int, default=None, help="Random seed for tie-breaking.")
    greedy.add_argument("--shuffle", action="store_true", help="Shuffle prime order.")
    greedy.add_argument("--refine-passes", type=int, default=0, help="Coordinate-refinement passes after greedy.")
    greedy.add_argument("--show-assignment", action="store_true", help="Print selected residues.")
    greedy.set_defaults(func=command_greedy)

    exact = sub.add_parser("exact", help="Run exact backtracking on a small staged instance.")
    add_common(exact)
    exact.add_argument("--cap", type=float, default=None, help="Use primes y < p <= cap*y; default all p <= n.")
    exact.add_argument("--time-limit", type=float, default=10.0, help="Seconds before returning unknown.")
    exact.add_argument("--node-limit", type=int, default=200_000, help="Search nodes before returning unknown.")
    exact.add_argument("--show-assignment", action="store_true", help="Print exact residue assignment if found.")
    exact.add_argument("--list-solvers", action="store_true", help="Report optional installed solver packages.")
    exact.set_defaults(func=command_exact)

    sweep = sub.add_parser("sweep", help="Run residual and greedy summaries over several n.")
    sweep.add_argument("--ns", required=True, help="Comma-separated n values.")
    sweep.add_argument("--y", default="sqrt", help="Zero-stage cutoff for each n.")
    sweep.add_argument("--z", type=float, default=None, help="Parameter for --y n/z.")
    sweep.add_argument("--r", type=int, default=2, help="Required multiplicity; default 2.")
    sweep.add_argument("--cap", type=float, default=None, help="Use primes y < p <= cap*y; default all p <= n.")
    sweep.add_argument("--seed", type=int, default=None, help="Random seed for greedy tie-breaking.")
    sweep.add_argument("--exact-up-to", type=int, default=0, help="Also run exact for n up to this value.")
    sweep.add_argument("--time-limit", type=float, default=10.0, help="Exact seconds per n.")
    sweep.add_argument("--node-limit", type=int, default=200_000, help="Exact node limit per n.")
    sweep.set_defaults(func=command_sweep)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.r <= 0:
        parser.error("--r must be positive")
    if hasattr(args, "n") and args.n <= 0:
        parser.error("--n must be positive")
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
