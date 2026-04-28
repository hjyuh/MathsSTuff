#!/usr/bin/env python3
"""Bitset exact search for the original no-zero-stage Erdos 689 instances.

For a given n, choose one residue a_p modulo every prime p <= n so that every
1 <= m <= n is hit at least twice.  This v2 solver is independent of
exact_search_689.py and keeps the original, no-zero-stage model.

The search state stores the remaining demand with two bitsets:

* need1: points still needing at least one more hit;
* need2: points still needing two more hits.

This is specialized to the original required=2 problem.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass, field
from itertools import combinations
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


Assignment = Dict[int, int]
Choice = Tuple[int, int]
Domain = Dict[int, List[Tuple[int, int, int]]]


class SearchStopped(RuntimeError):
    pass


class InfeasibleState(RuntimeError):
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


def iter_bits(mask: int) -> Iterable[int]:
    while mask:
        lsb = mask & -mask
        yield lsb.bit_length() - 1
        mask ^= lsb


def verify_assignment(n: int, assignment: Assignment, required: int = 2) -> Tuple[bool, List[int]]:
    coverage = [0] * (n + 1)
    for p, a in assignment.items():
        start = a if a else p
        for m in range(start, n + 1, p):
            coverage[m] += 1
    misses = [m for m in range(1, n + 1) if coverage[m] < required]
    return not misses, misses


def root_capacity(n: int, primes: Sequence[int]) -> int:
    return sum((n + p - 1) // p for p in primes)


def max_parity_residue_count(n: int, p: int, parity: int) -> int:
    """Maximum points of one parity in a residue class modulo an odd prime p."""

    q, r = divmod(n, p)
    best = 0

    if r:
        length = q + 1
        if parity == 1:
            has_desired_start = True
        else:
            has_desired_start = r >= 2
        best = max(best, (length + 1) // 2 if has_desired_start else length // 2)

    length = q
    if parity == 1:
        has_desired_start = True
    else:
        has_desired_start = r <= p - 2
    best = max(best, (length + 1) // 2 if has_desired_start else length // 2)
    return best


def parity_capacity(n: int, primes: Sequence[int], parity: int) -> int:
    return sum(max_parity_residue_count(n, p, parity) for p in primes if p != 2)


def fast_precheck(n: int) -> Optional[ExactResult]:
    """Return a root-level exact infeasibility certificate when one is available."""

    start = time.perf_counter()
    primes = primes_up_to(n)
    cap = root_capacity(n, primes)
    if cap < 2 * n:
        return ExactResult(
            status="infeasible",
            n=n,
            required=2,
            primes=len(primes),
            nodes=0,
            seconds=time.perf_counter() - start,
            initial_tokens=2 * n,
            final_deficit=2 * n,
            best_deficit=2 * n,
            memo_size=0,
            root_capacity=cap,
            forced_assignments=0,
            prunes={"capacity": 1, "domain": 0, "memo": 0, "parity": 0, "point": 0, "subset": 0},
            assignment=None,
            message="Root capacity is below the 2n demand.",
        )

    if 2 in primes:
        even_need = 2 * (n // 2)
        odd_need = 2 * ((n + 1) // 2)
        even_cap = parity_capacity(n, primes, 0)
        odd_cap = parity_capacity(n, primes, 1)
        if even_cap < even_need and odd_cap < odd_need:
            return ExactResult(
                status="infeasible",
                n=n,
                required=2,
                primes=len(primes),
                nodes=0,
                seconds=time.perf_counter() - start,
                initial_tokens=2 * n,
                final_deficit=2 * n,
                best_deficit=2 * n,
                memo_size=0,
                root_capacity=cap,
                forced_assignments=0,
                prunes={"capacity": 0, "domain": 0, "memo": 0, "parity": 1, "point": 0, "subset": 0},
                assignment=None,
                message=(
                    "Parity subset-capacity obstruction: after either choice modulo 2, "
                    "the opposite parity has insufficient odd-prime capacity."
                ),
            )

    return None


def parse_int_list(text: str) -> List[int]:
    """Parse comma-separated integers and inclusive ranges such as 1-10,20."""

    out: List[int] = []
    for part in text.split(","):
        token = part.strip()
        if not token:
            continue
        if "-" in token:
            left, right = token.split("-", 1)
            start = int(left)
            stop = int(right)
            step = 1 if start <= stop else -1
            out.extend(range(start, stop + step, step))
        else:
            out.append(int(token))
    return out


def parse_moduli(text: str) -> Tuple[int, ...]:
    values = tuple(x for x in parse_int_list(text) if x >= 2)
    return values


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
    forced_assignments: int
    prunes: Dict[str, int]
    assignment: Optional[Assignment]
    message: str


@dataclass
class Branch:
    choices: Tuple[Choice, ...]
    score: Tuple[int, int, int]


class BitsetExactSolver:
    def __init__(
        self,
        n: int,
        *,
        time_limit: float = 10.0,
        node_limit: int = 1_000_000,
        cut_moduli: Tuple[int, ...] = (2, 3, 5, 7),
        prefix_cuts: bool = True,
        residue_partition_cuts: bool = True,
    ) -> None:
        if n < 1:
            raise ValueError("n must be positive")
        self.n = n
        self.required = 2
        self.time_limit = time_limit
        self.node_limit = node_limit
        self.cut_moduli = cut_moduli
        self.prefix_cuts = prefix_cuts
        self.residue_partition_cuts = residue_partition_cuts

        self.primes = tuple(primes_up_to(n))
        self.prime_count = len(self.primes)
        self.full_mask = (1 << n) - 1
        self.all_primes_mask = (1 << self.prime_count) - 1

        self.class_masks: List[Tuple[int, ...]] = []
        for p in self.primes:
            masks: List[int] = []
            for a in range(p):
                mask = 0
                start = a if a else p
                for m in range(start, n + 1, p):
                    mask |= 1 << (m - 1)
                masks.append(mask)
            self.class_masks.append(tuple(masks))

        self.partition_masks: List[int] = []
        if residue_partition_cuts:
            for q in cut_moduli:
                for a in range(q):
                    mask = 0
                    start = a if a else q
                    for m in range(start, n + 1, q):
                        mask |= 1 << (m - 1)
                    if mask:
                        self.partition_masks.append(mask)

        self.nodes = 0
        self.best_deficit = 2 * n
        self.start = 0.0
        self.memo: set[Tuple[int, int, int]] = set()
        self.forced_assignments = 0
        self.prunes: Dict[str, int] = {
            "capacity": 0,
            "domain": 0,
            "memo": 0,
            "parity": 0,
            "point": 0,
            "subset": 0,
        }
        self.root_capacity, _ = self._capacity_details(self.full_mask, self.all_primes_mask)

    def solve(self) -> ExactResult:
        self.start = time.perf_counter()
        try:
            partial = self._dfs(self.full_mask, self.full_mask, self.all_primes_mask)
            seconds = time.perf_counter() - self.start
        except SearchStopped as exc:
            return ExactResult(
                status="unknown",
                n=self.n,
                required=self.required,
                primes=self.prime_count,
                nodes=self.nodes,
                seconds=time.perf_counter() - self.start,
                initial_tokens=2 * self.n,
                final_deficit=2 * self.n,
                best_deficit=self.best_deficit,
                memo_size=len(self.memo),
                root_capacity=self.root_capacity,
                forced_assignments=self.forced_assignments,
                prunes=dict(self.prunes),
                assignment=None,
                message=str(exc),
            )

        if partial is None:
            return ExactResult(
                status="infeasible",
                n=self.n,
                required=self.required,
                primes=self.prime_count,
                nodes=self.nodes,
                seconds=seconds,
                initial_tokens=2 * self.n,
                final_deficit=2 * self.n,
                best_deficit=self.best_deficit,
                memo_size=len(self.memo),
                root_capacity=self.root_capacity,
                forced_assignments=self.forced_assignments,
                prunes=dict(self.prunes),
                assignment=None,
                message="No full assignment exists for this finite instance.",
            )

        assignment = self._complete_assignment(partial)
        ok, misses = verify_assignment(self.n, assignment, self.required)
        return ExactResult(
            status="covered" if ok else "internal-error",
            n=self.n,
            required=self.required,
            primes=self.prime_count,
            nodes=self.nodes,
            seconds=seconds,
            initial_tokens=2 * self.n,
            final_deficit=0 if ok else len(misses),
            best_deficit=0 if ok else self.best_deficit,
            memo_size=len(self.memo),
            root_capacity=self.root_capacity,
            forced_assignments=self.forced_assignments,
            prunes=dict(self.prunes),
            assignment=assignment if ok else None,
            message="Found a full residue assignment." if ok else f"Verification failed: {misses[:10]}",
        )

    def _complete_assignment(self, partial: Dict[int, int]) -> Assignment:
        assignment: Assignment = {}
        for index, p in enumerate(self.primes):
            assignment[p] = partial.get(index, 0)
        return dict(sorted(assignment.items()))

    def _check_limits(self) -> None:
        if self.nodes >= self.node_limit:
            raise SearchStopped(f"node limit {self.node_limit} reached")
        if time.perf_counter() - self.start > self.time_limit:
            raise SearchStopped(f"time limit {self.time_limit:.3f}s reached")

    @staticmethod
    def _deficit(need1: int, need2: int) -> int:
        return need1.bit_count() + need2.bit_count()

    def _capacity_details(self, need1: int, remaining: int) -> Tuple[int, Dict[int, int]]:
        total = 0
        caps: Dict[int, int] = {}
        for index in iter_bits(remaining):
            best = 0
            for mask in self.class_masks[index]:
                gain = (mask & need1).bit_count()
                if gain > best:
                    best = gain
            caps[index] = best
            total += best
        return total, caps

    def _domains(self, need1: int, remaining: int, caps: Dict[int, int], slack: int) -> Domain:
        domains: Domain = {}
        for index in iter_bits(remaining):
            cap = caps[index]
            choices: List[Tuple[int, int, int]] = []
            for a, mask in enumerate(self.class_masks[index]):
                gain = (mask & need1).bit_count()
                loss = cap - gain
                if loss <= slack:
                    choices.append((loss, -gain, a))
            choices.sort()
            domains[index] = choices
        return domains

    def _apply_choice(self, need1: int, need2: int, index: int, residue: int) -> Tuple[int, int]:
        mask = self.class_masks[index][residue]
        next_need1 = (need1 & ~mask) | (need2 & mask)
        next_need2 = need2 & ~mask
        return next_need1, next_need2

    def _apply_choices(
        self, need1: int, need2: int, remaining: int, choices: Tuple[Choice, ...]
    ) -> Optional[Tuple[int, int, int]]:
        next_need1 = need1
        next_need2 = need2
        next_remaining = remaining
        for index, residue in choices:
            bit = 1 << index
            if not (next_remaining & bit):
                return None
            next_need1, next_need2 = self._apply_choice(next_need1, next_need2, index, residue)
            next_remaining ^= bit
        return next_need1, next_need2, next_remaining

    def _subset_capacity(self, subset: int, remaining: int, domains: Optional[Domain]) -> int:
        total = 0
        for index in iter_bits(remaining):
            best = 0
            if domains is None:
                residues = range(len(self.class_masks[index]))
            else:
                residues = (choice[2] for choice in domains[index])
            for residue in residues:
                hits = (self.class_masks[index][residue] & subset).bit_count()
                if hits > best:
                    best = hits
            total += best
        return total

    def _subset_cut_ok(self, need1: int, need2: int, remaining: int, domains: Optional[Domain]) -> bool:
        subsets: List[int] = []
        if need2:
            subsets.append(need2)
        one_only = need1 & ~need2
        if one_only:
            subsets.append(one_only)

        for mask in self.partition_masks:
            subset = mask & need1
            if subset:
                subsets.append(subset)

        if self.prefix_cuts:
            subsets.extend(self._prefix_subsets(need1, need2, remaining, domains))

        seen: set[int] = set()
        for subset in subsets:
            if subset in seen:
                continue
            seen.add(subset)
            need = (subset & need1).bit_count() + (subset & need2).bit_count()
            capacity = self._subset_capacity(subset, remaining, domains)
            if capacity < need:
                self.prunes["subset"] += 1
                return False
        return True

    def _prefix_subsets(
        self, need1: int, need2: int, remaining: int, domains: Optional[Domain]
    ) -> List[int]:
        scores: List[Tuple[int, int, int]] = []
        domain_sets: Dict[int, set[int]] = {}
        if domains is not None:
            domain_sets = {index: {choice[2] for choice in choices} for index, choices in domains.items()}

        for point in iter_bits(need1):
            m = point + 1
            demand = 1 + ((need2 >> point) & 1)
            eligible = 0
            for index in iter_bits(remaining):
                residue = m % self.primes[index]
                if domains is None or residue in domain_sets[index]:
                    eligible += 1
            scores.append((eligible, -demand, point))

        scores.sort()
        sizes = {2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 48, 64, 96, 128}
        subsets: List[int] = []
        prefix = 0
        for position, (_, __, point) in enumerate(scores, start=1):
            prefix |= 1 << point
            if position in sizes and position < len(scores):
                subsets.append(prefix)
        return subsets

    def _propagate(
        self, need1: int, need2: int, remaining: int
    ) -> Optional[Tuple[int, int, int, Dict[int, int]]]:
        forced_assignment: Dict[int, int] = {}

        while True:
            deficit = self._deficit(need1, need2)
            if deficit == 0 or remaining == 0:
                return need1, need2, remaining, forced_assignment

            capacity, caps = self._capacity_details(need1, remaining)
            if capacity < deficit:
                self.prunes["capacity"] += 1
                return None
            slack = capacity - deficit
            domains = self._domains(need1, remaining, caps, slack)

            forced: Dict[int, int] = {}
            for index, choices in domains.items():
                if not choices:
                    self.prunes["domain"] += 1
                    return None
                if len(choices) == 1:
                    forced[index] = choices[0][2]

            domain_sets = {index: {choice[2] for choice in choices} for index, choices in domains.items()}
            for point in iter_bits(need1):
                m = point + 1
                demand = 1 + ((need2 >> point) & 1)
                options: List[Choice] = []
                for index in iter_bits(remaining):
                    residue = m % self.primes[index]
                    if residue in domain_sets[index]:
                        options.append((index, residue))
                if len(options) < demand:
                    self.prunes["point"] += 1
                    return None
                if len(options) == demand:
                    for index, residue in options:
                        old = forced.get(index)
                        if old is not None and old != residue:
                            self.prunes["point"] += 1
                            return None
                        forced[index] = residue

            if not self._subset_cut_ok(need1, need2, remaining, domains):
                return None

            if not forced:
                return need1, need2, remaining, forced_assignment

            for index, residue in sorted(
                forced.items(),
                key=lambda item: (self.class_masks[item[0]][item[1]] & need1).bit_count(),
                reverse=True,
            ):
                bit = 1 << index
                if not (remaining & bit):
                    continue
                need1, need2 = self._apply_choice(need1, need2, index, residue)
                remaining ^= bit
                forced_assignment[index] = residue
                self.forced_assignments += 1

    def _eligible_for_point(
        self,
        point: int,
        need1: int,
        remaining: int,
        caps: Dict[int, int],
        slack: int,
    ) -> List[Tuple[int, int, int, int]]:
        m = point + 1
        options: List[Tuple[int, int, int, int]] = []
        for index in iter_bits(remaining):
            residue = m % self.primes[index]
            gain = (self.class_masks[index][residue] & need1).bit_count()
            loss = caps[index] - gain
            if loss <= slack:
                options.append((loss, -gain, index, residue))
        options.sort()
        return options

    def _branch_choices(
        self, need1: int, need2: int, remaining: int, caps: Dict[int, int], slack: int
    ) -> List[Branch]:
        domains = self._domains(need1, remaining, caps, slack)
        best_kind = "prime"
        best_score = (10**18, 10**18, 10**18)
        best_payload: object = None

        for index, choices in domains.items():
            score = (len(choices), 1, self.primes[index])
            if score < best_score:
                best_kind = "prime"
                best_score = score
                best_payload = index

        for point in iter_bits(need1):
            demand = 1 + ((need2 >> point) & 1)
            options = self._eligible_for_point(point, need1, remaining, caps, slack)
            count = len(options)
            if slack == 0 and demand == 2:
                count = count * (count - 1) // 2
            score = (count, 0, point)
            if score < best_score:
                best_kind = "point"
                best_score = score
                best_payload = (point, demand, options)

        branches: List[Branch] = []
        if best_kind == "prime":
            index = int(best_payload)
            for loss, neg_gain, residue in domains[index]:
                branches.append(Branch(((index, residue),), (loss, neg_gain, self.primes[index])))
            return branches

        point, demand, options = best_payload  # type: ignore[misc]
        if slack == 0 and demand == 2:
            for left, right in combinations(options, 2):
                loss = left[0] + right[0]
                neg_gain = left[1] + right[1]
                branches.append(
                    Branch(
                        ((left[2], left[3]), (right[2], right[3])),
                        (loss, neg_gain, point),
                    )
                )
        else:
            for loss, neg_gain, index, residue in options:
                branches.append(Branch(((index, residue),), (loss, neg_gain, self.primes[index])))
        branches.sort(key=lambda branch: branch.score)
        return branches

    def _dfs(self, need1: int, need2: int, remaining: int) -> Optional[Dict[int, int]]:
        self._check_limits()
        self.nodes += 1

        propagated = self._propagate(need1, need2, remaining)
        if propagated is None:
            return None
        need1, need2, remaining, forced = propagated

        deficit = self._deficit(need1, need2)
        if deficit < self.best_deficit:
            self.best_deficit = deficit
        if deficit == 0:
            return dict(forced)
        if remaining == 0:
            return None

        key = (need1, need2, remaining)
        if key in self.memo:
            self.prunes["memo"] += 1
            return None

        capacity, caps = self._capacity_details(need1, remaining)
        if capacity < deficit:
            self.prunes["capacity"] += 1
            self.memo.add(key)
            return None
        slack = capacity - deficit
        domains = self._domains(need1, remaining, caps, slack)
        if not self._subset_cut_ok(need1, need2, remaining, domains):
            self.memo.add(key)
            return None

        for branch in self._branch_choices(need1, need2, remaining, caps, slack):
            next_state = self._apply_choices(need1, need2, remaining, branch.choices)
            if next_state is None:
                continue
            result = self._dfs(*next_state)
            if result is not None:
                for index, residue in branch.choices:
                    result[index] = residue
                result.update(forced)
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
        "forced_assignments": result.forced_assignments,
        "prunes": result.prunes,
        "message": result.message,
    }
    if show_assignment and result.assignment is not None:
        payload["assignment"] = result.assignment
    return payload


def print_json(obj: object) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True))


def make_solver(args: argparse.Namespace, n: int) -> BitsetExactSolver:
    return BitsetExactSolver(
        n,
        time_limit=args.time_limit,
        node_limit=args.node_limit,
        cut_moduli=parse_moduli(args.cut_moduli),
        prefix_cuts=not args.no_prefix_cuts,
        residue_partition_cuts=not args.no_residue_partition_cuts,
    )


def solve_instance(args: argparse.Namespace, n: int) -> ExactResult:
    if not args.no_fast_precheck:
        checked = fast_precheck(n)
        if checked is not None:
            return checked
    return make_solver(args, n).solve()


def command_exact(args: argparse.Namespace) -> None:
    print_json(result_payload(solve_instance(args, args.n), args.show_assignment))


def command_sweep(args: argparse.Namespace) -> None:
    rows = []
    for n in parse_int_list(args.ns):
        result = solve_instance(args, n)
        rows.append(result_payload(result, args.show_assignment))
        if args.stop_on_covered and result.status == "covered":
            break
        if args.stop_on_unknown and result.status == "unknown":
            break
    print_json(rows)


def command_search_first(args: argparse.Namespace) -> None:
    rows = []
    first: Optional[Dict[str, object]] = None
    for n in range(args.min_n, args.max_n + 1):
        result = solve_instance(args, n)
        payload = result_payload(result, args.show_assignment)
        rows.append(payload)
        if result.status == "covered":
            first = payload
            break
        if result.status == "unknown" and args.stop_on_unknown:
            break
    print_json({"first_covered": first, "rows": rows})


def command_certify_range(args: argparse.Namespace) -> None:
    started = time.perf_counter()
    counts: Dict[str, int] = {}
    first_unknown: Optional[Dict[str, object]] = None
    first_covered: Optional[Dict[str, object]] = None
    last_infeasible: Optional[Dict[str, object]] = None

    for n in range(args.min_n, args.max_n + 1):
        result = solve_instance(args, n)
        payload = result_payload(result, args.show_assignment)
        counts[result.status] = counts.get(result.status, 0) + 1
        if result.status == "infeasible":
            last_infeasible = payload
        elif result.status == "unknown" and first_unknown is None:
            first_unknown = payload
            if args.stop_on_unknown:
                break
        elif result.status == "covered" and first_covered is None:
            first_covered = payload
            if args.stop_on_covered:
                break

    print_json(
        {
            "min_n": args.min_n,
            "max_n": args.max_n,
            "counts": counts,
            "first_unknown": first_unknown,
            "first_covered": first_covered,
            "last_infeasible": last_infeasible,
            "seconds": round(time.perf_counter() - started, 6),
        }
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Bitset exact finite search for the original no-zero-stage Erdos 689 problem."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--time-limit", type=float, default=10.0, help="Seconds per instance.")
        p.add_argument("--node-limit", type=int, default=1_000_000, help="Search nodes per instance.")
        p.add_argument(
            "--cut-moduli",
            default="2,3,5,7",
            help="Small moduli used for residue-partition capacity cuts.",
        )
        p.add_argument("--no-prefix-cuts", action="store_true", help="Disable constrained-prefix cuts.")
        p.add_argument(
            "--no-residue-partition-cuts",
            action="store_true",
            help="Disable small residue-partition capacity cuts.",
        )
        p.add_argument(
            "--no-fast-precheck",
            action="store_true",
            help="Disable root capacity and parity prechecks before bitset search.",
        )
        p.add_argument("--show-assignment", action="store_true", help="Print full residue assignment when found.")

    exact = sub.add_parser("exact", help="Solve one finite instance.")
    exact.add_argument("--n", type=int, required=True)
    add_common(exact)
    exact.set_defaults(func=command_exact)

    sweep = sub.add_parser("sweep", help="Solve a comma-separated list or range of n values.")
    sweep.add_argument("--ns", required=True)
    sweep.add_argument("--stop-on-covered", action="store_true")
    sweep.add_argument("--stop-on-unknown", action="store_true")
    add_common(sweep)
    sweep.set_defaults(func=command_sweep)

    search_first = sub.add_parser("search-first", help="Search increasing n for the first covered instance.")
    search_first.add_argument("--min-n", type=int, default=1)
    search_first.add_argument("--max-n", type=int, required=True)
    search_first.add_argument("--stop-on-unknown", action="store_true")
    add_common(search_first)
    search_first.set_defaults(func=command_search_first)

    certify = sub.add_parser("certify-range", help="Summarize statuses over an interval without printing every row.")
    certify.add_argument("--min-n", type=int, default=1)
    certify.add_argument("--max-n", type=int, required=True)
    certify.add_argument("--stop-on-unknown", action="store_true")
    certify.add_argument("--stop-on-covered", action="store_true")
    add_common(certify)
    certify.set_defaults(func=command_certify_range)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
