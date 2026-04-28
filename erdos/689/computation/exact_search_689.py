#!/usr/bin/env python3
"""Exact search for the original Erdos Problem 689 finite instances.

Problem 689 asks for one residue class a_p modulo every prime p <= n such
that every m in [1,n] lies in at least two chosen classes.  Unlike
explore_689.py, this script does not force an initial square-root zero stage.

The brancher is target driven: choose a still-deficient integer m, then branch
over remaining primes p by forcing a_p = m mod p.  This is complete because any
solution must use some remaining prime to cover the chosen target, and the
independent residue choices can be reordered.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


Assignment = Dict[int, int]
Demand = Tuple[int, ...]


class SearchStopped(RuntimeError):
    pass


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


def verify_assignment(n: int, assignment: Assignment, required: int = 2) -> Tuple[bool, List[int]]:
    coverage = [0] * (n + 1)
    for p, a in assignment.items():
        start = a if a else p
        for m in range(start, n + 1, p):
            coverage[m] += 1
    misses = [m for m in range(1, n + 1) if coverage[m] < required]
    return not misses, misses


@dataclass
class ExactResult:
    status: str
    n: int
    required: int
    primes: int
    nodes: int
    seconds: float
    initial_tokens: int
    final_deficit: int
    best_deficit: int
    memo_size: int
    root_capacity: int
    assignment: Optional[Assignment]
    message: str


class ExactSolver:
    def __init__(
        self,
        n: int,
        required: int = 2,
        time_limit: float = 10.0,
        node_limit: int = 1_000_000,
        target_policy: str = "tight",
        prefix_capacity: bool = True,
    ) -> None:
        if n < 1:
            raise ValueError("n must be positive")
        if required < 1:
            raise ValueError("required must be positive")
        if target_policy not in {"tight", "gain"}:
            raise ValueError("target_policy must be 'tight' or 'gain'")

        self.n = n
        self.required = required
        self.time_limit = time_limit
        self.node_limit = node_limit
        self.target_policy = target_policy
        self.prefix_capacity = prefix_capacity
        self.primes = tuple(primes_up_to(n))
        self.initial = tuple([required] * n)
        self.nodes = 0
        self.best_deficit = sum(self.initial)
        self.start = 0.0
        self.memo: set[Tuple[Demand, Tuple[int, ...]]] = set()
        self.root_capacity, _ = self._capacity_details(self.initial, self.primes)
        self.class_members: Dict[Tuple[int, int], Tuple[int, ...]] = {}
        for p in self.primes:
            for a in range(p):
                start = a if a else p
                self.class_members[(p, a)] = tuple(m - 1 for m in range(start, n + 1, p))

    def solve(self) -> ExactResult:
        self.start = time.perf_counter()
        try:
            partial = self._dfs(self.initial, self.primes)
            seconds = time.perf_counter() - self.start
        except SearchStopped as exc:
            return ExactResult(
                status="unknown",
                n=self.n,
                required=self.required,
                primes=len(self.primes),
                nodes=self.nodes,
                seconds=time.perf_counter() - self.start,
                initial_tokens=sum(self.initial),
                final_deficit=sum(self.initial),
                best_deficit=self.best_deficit,
                memo_size=len(self.memo),
                root_capacity=self.root_capacity,
                assignment=None,
                message=str(exc),
            )

        if partial is None:
            return ExactResult(
                status="infeasible",
                n=self.n,
                required=self.required,
                primes=len(self.primes),
                nodes=self.nodes,
                seconds=seconds,
                initial_tokens=sum(self.initial),
                final_deficit=sum(self.initial),
                best_deficit=self.best_deficit,
                memo_size=len(self.memo),
                root_capacity=self.root_capacity,
                assignment=None,
                message="No full assignment exists for this finite instance.",
            )

        assignment = self._complete_assignment(partial)
        ok, misses = verify_assignment(self.n, assignment, self.required)
        final_deficit = 0 if ok else len(misses)
        return ExactResult(
            status="covered" if ok else "internal-error",
            n=self.n,
            required=self.required,
            primes=len(self.primes),
            nodes=self.nodes,
            seconds=seconds,
            initial_tokens=sum(self.initial),
            final_deficit=final_deficit,
            best_deficit=0 if ok else self.best_deficit,
            memo_size=len(self.memo),
            root_capacity=self.root_capacity,
            assignment=assignment if ok else None,
            message="Found a full residue assignment." if ok else f"Verification failed: {misses[:10]}",
        )

    def _complete_assignment(self, partial: Assignment) -> Assignment:
        assignment = dict(partial)
        for p in self.primes:
            assignment.setdefault(p, 0)
        return dict(sorted(assignment.items()))

    def _check_limits(self) -> None:
        if self.nodes >= self.node_limit:
            raise SearchStopped(f"node limit {self.node_limit} reached")
        if time.perf_counter() - self.start > self.time_limit:
            raise SearchStopped(f"time limit {self.time_limit:.3f}s reached")

    def _gain(self, demand: Demand, p: int, a: int) -> int:
        return sum(1 for idx in self.class_members[(p, a)] if demand[idx] > 0)

    def _apply(self, demand: Demand, p: int, a: int) -> Demand:
        out = list(demand)
        for idx in self.class_members[(p, a)]:
            if out[idx] > 0:
                out[idx] -= 1
        return tuple(out)

    def _capacity_details(self, demand: Demand, remaining: Tuple[int, ...]) -> Tuple[int, Dict[int, int]]:
        total = 0
        by_prime: Dict[int, int] = {}
        positive = [idx for idx, d in enumerate(demand) if d > 0]
        if not positive:
            return 0, {p: 0 for p in remaining}
        for p in remaining:
            gains = [0] * p
            for idx in positive:
                gains[(idx + 1) % p] += 1
            best = max(gains)
            by_prime[p] = best
            total += best
        return total, by_prime

    def _prefix_capacity_ok(self, demand: Demand, remaining: Tuple[int, ...]) -> bool:
        if not self.prefix_capacity:
            return True
        positive = [idx for idx, d in enumerate(demand) if d > 0]
        if len(positive) < 2:
            return True
        scored = sorted(
            positive,
            key=lambda idx: (demand[idx], -idx),
            reverse=True,
        )
        sizes = (2, 3, 4, 6, 8, 12)
        for size in sizes:
            if size >= len(scored):
                continue
            subset = scored[:size]
            need = sum(demand[idx] for idx in subset)
            capacity = 0
            for p in remaining:
                counts: Dict[int, int] = {}
                for idx in subset:
                    a = (idx + 1) % p
                    counts[a] = counts.get(a, 0) + 1
                capacity += max(counts.values())
            if capacity < need:
                return False
        return True

    def _forced_gain_sum(self, demand: Demand, remaining: Tuple[int, ...], target_idx: int) -> int:
        m = target_idx + 1
        return sum(self._gain(demand, p, m % p) for p in remaining)

    def _eligible_count(
        self,
        demand: Demand,
        remaining: Tuple[int, ...],
        target_idx: int,
        slack: int,
        prime_capacity: Dict[int, int],
    ) -> int:
        m = target_idx + 1
        count = 0
        for p in remaining:
            if self._gain(demand, p, m % p) + slack >= prime_capacity[p]:
                count += 1
        return count

    def _select_target(
        self,
        demand: Demand,
        remaining: Tuple[int, ...],
        slack: int,
        prime_capacity: Dict[int, int],
    ) -> int:
        positive = [idx for idx, d in enumerate(demand) if d > 0]
        if self.target_policy == "gain":
            return max(
                positive,
                key=lambda idx: (
                    demand[idx],
                    self._forced_gain_sum(demand, remaining, idx),
                    -idx,
                ),
            )
        return max(
            positive,
            key=lambda idx: (
                demand[idx],
                -self._eligible_count(demand, remaining, idx, slack, prime_capacity),
                -self._forced_gain_sum(demand, remaining, idx),
                -idx,
            ),
        )

    def _dfs(self, demand: Demand, remaining: Tuple[int, ...]) -> Optional[Assignment]:
        self._check_limits()
        self.nodes += 1
        deficit = sum(demand)
        if deficit < self.best_deficit:
            self.best_deficit = deficit
        if deficit == 0:
            return {}
        if not remaining:
            return None
        if max(demand) > len(remaining):
            return None

        key = (demand, remaining)
        if key in self.memo:
            return None
        capacity, prime_capacity = self._capacity_details(demand, remaining)
        if capacity < deficit:
            self.memo.add(key)
            return None
        if not self._prefix_capacity_ok(demand, remaining):
            self.memo.add(key)
            return None

        slack = capacity - deficit
        target_idx = self._select_target(demand, remaining, slack, prime_capacity)
        m = target_idx + 1
        options = []
        for index, p in enumerate(remaining):
            a = m % p
            gain = self._gain(demand, p, a)
            if gain + slack < prime_capacity[p]:
                continue
            options.append((gain, -p, p, a, index))
        options.sort(reverse=True)

        for _, _, p, a, index in options:
            next_demand = self._apply(demand, p, a)
            next_remaining = remaining[:index] + remaining[index + 1 :]
            result = self._dfs(next_demand, next_remaining)
            if result is not None:
                result[p] = a
                return result

        self.memo.add(key)
        return None


def result_payload(result: ExactResult, show_assignment: bool = False) -> Dict[str, object]:
    payload: Dict[str, object] = {
        "status": result.status,
        "n": result.n,
        "required": result.required,
        "primes": result.primes,
        "nodes": result.nodes,
        "seconds": round(result.seconds, 6),
        "initial_tokens": result.initial_tokens,
        "final_deficit": result.final_deficit,
        "best_deficit": result.best_deficit,
        "memo_size": result.memo_size,
        "root_capacity": result.root_capacity,
        "message": result.message,
    }
    if show_assignment and result.assignment is not None:
        payload["assignment"] = result.assignment
    return payload


def print_json(obj: object) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True))


def command_exact(args: argparse.Namespace) -> None:
    solver = ExactSolver(
        args.n,
        required=args.required,
        time_limit=args.time_limit,
        node_limit=args.node_limit,
        target_policy=args.target_policy,
        prefix_capacity=not args.no_prefix_capacity,
    )
    print_json(result_payload(solver.solve(), args.show_assignment))


def command_sweep(args: argparse.Namespace) -> None:
    rows = []
    for n in parse_int_list(args.ns):
        solver = ExactSolver(
            n,
            required=args.required,
            time_limit=args.time_limit,
            node_limit=args.node_limit,
            target_policy=args.target_policy,
            prefix_capacity=not args.no_prefix_capacity,
        )
        result = solver.solve()
        rows.append(result_payload(result, args.show_assignment))
        if args.stop_on_covered and result.status == "covered":
            break
    print_json(rows)


def command_search_first(args: argparse.Namespace) -> None:
    rows = []
    first: Optional[Dict[str, object]] = None
    for n in range(args.min_n, args.max_n + 1):
        solver = ExactSolver(
            n,
            required=args.required,
            time_limit=args.time_limit,
            node_limit=args.node_limit,
            target_policy=args.target_policy,
            prefix_capacity=not args.no_prefix_capacity,
        )
        result = solver.solve()
        payload = result_payload(result, args.show_assignment)
        rows.append(payload)
        if result.status == "covered":
            first = payload
            break
        if result.status == "unknown" and args.stop_on_unknown:
            break
    print_json({"first_covered": first, "rows": rows})


def parse_int_list(text: str) -> List[int]:
    return [int(part) for part in text.split(",") if part.strip()]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Exact branch-and-bound search for original Erdos Problem 689 finite instances."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--required", type=int, default=2, help="Required hits per m; default 2.")
        p.add_argument("--time-limit", type=float, default=10.0, help="Seconds per instance.")
        p.add_argument("--node-limit", type=int, default=1_000_000, help="Search nodes per instance.")
        p.add_argument(
            "--target-policy",
            choices=("tight", "gain"),
            default="tight",
            help="Target tie-break: tight explores low forced-gain targets first; gain favors high-gain targets.",
        )
        p.add_argument(
            "--no-prefix-capacity",
            action="store_true",
            help="Disable small-prefix subset capacity pruning.",
        )
        p.add_argument("--show-assignment", action="store_true", help="Print full residue assignment when found.")

    exact = sub.add_parser("exact", help="Solve one finite instance.")
    exact.add_argument("--n", type=int, required=True)
    add_common(exact)
    exact.set_defaults(func=command_exact)

    sweep = sub.add_parser("sweep", help="Solve a comma-separated list of n values.")
    sweep.add_argument("--ns", required=True)
    sweep.add_argument("--stop-on-covered", action="store_true")
    add_common(sweep)
    sweep.set_defaults(func=command_sweep)

    search_first = sub.add_parser("search-first", help="Search increasing n for the first covered instance.")
    search_first.add_argument("--min-n", type=int, default=1)
    search_first.add_argument("--max-n", type=int, required=True)
    search_first.add_argument("--stop-on-unknown", action="store_true")
    add_common(search_first)
    search_first.set_defaults(func=command_search_first)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
