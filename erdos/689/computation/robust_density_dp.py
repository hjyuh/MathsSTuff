#!/usr/bin/env python3
"""Exact / high-precision robust-density dynamic program for Erdos 689.

The product model from ``robust-density-threshold.md`` is

    Z_s = (1, 0, 0), (0, 1, 0), (0, 0, 1) with probability 1 / (s - 1),
    Z_s = (0, 0, 0)                          with probability 1 - 3 / (s - 1),

independently over odd primes ``s >= 7``.  For an initial prime set

    S(y) = {p prime : 7 <= p <= y},

the robust density is

    delta_S = P(X1 >= 1, X2 >= 2, X4 >= 2),

where ``(X1, X2, X4) = sum_{s in S} Z_s``.

Because the event only depends on the truncated coordinates

    X1 in {0, 1+}, X2 in {0, 1, 2+}, X4 in {0, 1, 2+},

the exact computation is an 18-state dynamic program.

Arithmetic modes:

* ``exact`` keeps a common denominator ``prod_{s in S}(s - 1)`` and updates
  integer state weights exactly.
* ``decimal`` keeps 18 ``Decimal`` probabilities directly.
* ``auto`` starts exact and converts once the prime count exceeds
  ``--exact-primes-max``.

The script also reports the union-bound lower bound

    1 - A_S (3 + 2 mu'_S),

and the one-coordinate upper bound

    1 - A_S (1 + mu'_S),

where

    A_S = prod_{s in S} (s - 2) / (s - 1),
    mu'_S = sum_{s in S} 1 / (s - 2).
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from decimal import Decimal, getcontext
from math import exp, log, log10
from typing import Iterable, List, Optional, Sequence, Tuple


STATE_LIST: Tuple[Tuple[int, int, int], ...] = tuple(
    (x1, x2, x4) for x1 in (0, 1) for x2 in (0, 1, 2) for x4 in (0, 1, 2)
)
STATE_INDEX = {state: index for index, state in enumerate(STATE_LIST)}
ZERO_STATE_INDEX = STATE_INDEX[(0, 0, 0)]
TARGET_STATE_INDEX = STATE_INDEX[(1, 2, 2)]
X1_ZERO_INDICES = tuple(
    index for index, state in enumerate(STATE_LIST) if state[0] == 0
)
X2_LE1_INDICES = tuple(
    index for index, state in enumerate(STATE_LIST) if state[1] <= 1
)


def _next_state(state: Tuple[int, int, int], axis: int) -> Tuple[int, int, int]:
    values = list(state)
    caps = (1, 2, 2)
    values[axis] = min(caps[axis], values[axis] + 1)
    return tuple(values)  # type: ignore[return-value]


NEXT_X1 = tuple(STATE_INDEX[_next_state(state, 0)] for state in STATE_LIST)
NEXT_X2 = tuple(STATE_INDEX[_next_state(state, 1)] for state in STATE_LIST)
NEXT_X4 = tuple(STATE_INDEX[_next_state(state, 2)] for state in STATE_LIST)


@dataclass
class Snapshot:
    cutoff: int
    largest_prime: Optional[int]
    prime_count: int
    arithmetic: str
    delta: Decimal
    lower_bound: Decimal
    upper_bound: Decimal
    lambda_sum: Decimal
    a_value: Decimal
    mu_prime: Decimal
    x1_zero_mass: Decimal
    x2_le1_mass: Decimal
    x1_zero_error: Decimal
    x2_le1_error: Decimal
    exact_numerator: Optional[int] = None
    exact_denominator: Optional[int] = None


def odd_primes_up_to(limit: int) -> List[int]:
    if limit < 7:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [value for value in range(7, limit + 1, 2) if sieve[value]]


def decimal_zero() -> Decimal:
    return Decimal(0)


def decimal_one() -> Decimal:
    return Decimal(1)


def delta_star(precision: int) -> Decimal:
    current = getcontext().prec
    getcontext().prec = precision
    try:
        exp_two = Decimal(2).exp()
        ten = Decimal(10)
        return decimal_one() / (Decimal(11) / ten - Decimal(3) / (ten * exp_two))
    finally:
        getcontext().prec = current


class DensityAccumulator:
    def __init__(
        self,
        mode: str,
        precision: int,
        exact_primes_max: int,
    ) -> None:
        if mode not in {"auto", "exact", "decimal"}:
            raise ValueError(f"unknown mode: {mode}")
        self.requested_mode = mode
        self.precision = precision
        self.exact_primes_max = exact_primes_max
        self.prime_count = 0
        self.last_prime: Optional[int] = None

        self.a_value = decimal_one()
        self.mu_prime = decimal_zero()
        self.lambda_sum = decimal_zero()

        if mode == "decimal":
            self.arithmetic = "decimal"
            self.decimal_weights = [decimal_zero() for _ in STATE_LIST]
            self.decimal_weights[ZERO_STATE_INDEX] = decimal_one()
            self.int_weights = None
            self.denominator = None
        else:
            self.arithmetic = "exact"
            self.int_weights = [0 for _ in STATE_LIST]
            self.int_weights[ZERO_STATE_INDEX] = 1
            self.denominator = 1
            self.decimal_weights = None

    def _convert_to_decimal(self) -> None:
        if self.arithmetic != "exact":
            return
        assert self.int_weights is not None
        assert self.denominator is not None
        denominator = Decimal(self.denominator)
        self.decimal_weights = [Decimal(weight) / denominator for weight in self.int_weights]
        self.int_weights = None
        self.denominator = None
        self.arithmetic = "decimal(auto)"

    def step(self, prime: int) -> None:
        prime_decimal = Decimal(prime)
        self.a_value *= (prime_decimal - 2) / (prime_decimal - 1)
        self.mu_prime += decimal_one() / (prime_decimal - 2)
        self.lambda_sum += decimal_one() / (prime_decimal - 1)

        if self.arithmetic == "exact":
            assert self.int_weights is not None
            assert self.denominator is not None
            miss_weight = prime - 4
            new_weights = [0 for _ in STATE_LIST]
            for index, weight in enumerate(self.int_weights):
                if not weight:
                    continue
                new_weights[index] += weight * miss_weight
                new_weights[NEXT_X1[index]] += weight
                new_weights[NEXT_X2[index]] += weight
                new_weights[NEXT_X4[index]] += weight
            self.int_weights = new_weights
            self.denominator *= prime - 1
        else:
            assert self.decimal_weights is not None
            hit = decimal_one() / (prime_decimal - 1)
            miss = (prime_decimal - 4) / (prime_decimal - 1)
            new_weights = [decimal_zero() for _ in STATE_LIST]
            for index, weight in enumerate(self.decimal_weights):
                if not weight:
                    continue
                new_weights[index] += weight * miss
                new_weights[NEXT_X1[index]] += weight * hit
                new_weights[NEXT_X2[index]] += weight * hit
                new_weights[NEXT_X4[index]] += weight * hit
            self.decimal_weights = new_weights

        self.prime_count += 1
        self.last_prime = prime

        if (
            self.requested_mode == "auto"
            and self.arithmetic == "exact"
            and self.prime_count >= self.exact_primes_max
        ):
            self._convert_to_decimal()

    def current_delta(self) -> Decimal:
        if self.arithmetic == "exact":
            assert self.int_weights is not None
            assert self.denominator is not None
            return Decimal(self.int_weights[TARGET_STATE_INDEX]) / Decimal(self.denominator)
        assert self.decimal_weights is not None
        return self.decimal_weights[TARGET_STATE_INDEX]

    def snapshot(self, cutoff: int) -> Snapshot:
        expected_x1_zero = self.a_value
        expected_x2_le1 = self.a_value * (decimal_one() + self.mu_prime)
        lower = decimal_one() - self.a_value * (Decimal(3) + Decimal(2) * self.mu_prime)
        upper = decimal_one() - self.a_value * (decimal_one() + self.mu_prime)
        if lower < 0:
            lower = decimal_zero()

        if self.arithmetic == "exact":
            assert self.int_weights is not None
            assert self.denominator is not None
            denominator_decimal = Decimal(self.denominator)
            x1_zero_mass = Decimal(
                sum(self.int_weights[index] for index in X1_ZERO_INDICES)
            ) / denominator_decimal
            x2_le1_mass = Decimal(
                sum(self.int_weights[index] for index in X2_LE1_INDICES)
            ) / denominator_decimal
            delta = Decimal(self.int_weights[TARGET_STATE_INDEX]) / denominator_decimal
            exact_numerator = self.int_weights[TARGET_STATE_INDEX]
            exact_denominator = self.denominator
        else:
            assert self.decimal_weights is not None
            x1_zero_mass = sum(
                self.decimal_weights[index] for index in X1_ZERO_INDICES
            )
            x2_le1_mass = sum(
                self.decimal_weights[index] for index in X2_LE1_INDICES
            )
            delta = self.decimal_weights[TARGET_STATE_INDEX]
            exact_numerator = None
            exact_denominator = None

        return Snapshot(
            cutoff=cutoff,
            largest_prime=self.last_prime,
            prime_count=self.prime_count,
            arithmetic=self.arithmetic,
            delta=delta,
            lower_bound=lower,
            upper_bound=upper,
            lambda_sum=self.lambda_sum,
            a_value=self.a_value,
            mu_prime=self.mu_prime,
            x1_zero_mass=x1_zero_mass,
            x2_le1_mass=x2_le1_mass,
            x1_zero_error=abs(x1_zero_mass - expected_x1_zero),
            x2_le1_error=abs(x2_le1_mass - expected_x2_le1),
            exact_numerator=exact_numerator,
            exact_denominator=exact_denominator,
        )


def parse_int_list(spec: str) -> List[int]:
    values = []
    for part in spec.split(","):
        text = part.strip()
        if not text:
            continue
        value = int(text)
        if value < 0:
            raise SystemExit("cutoffs must be nonnegative")
        values.append(value)
    if not values:
        raise SystemExit("expected at least one integer cutoff")
    return sorted(set(values))


def parse_target(spec: str, precision: int) -> Decimal:
    text = spec.strip().lower()
    if text in {"delta_star", "delta-star", "star"}:
        return delta_star(precision)
    return Decimal(spec)


def format_fixed(value: Decimal, digits: int) -> str:
    return format(value, f".{digits}f")


def format_scientific(value: Decimal, digits: int = 3) -> str:
    return format(value, f".{digits}E")


def scan_cutoffs(
    cutoffs: Sequence[int],
    mode: str,
    precision: int,
    exact_primes_max: int,
) -> List[Snapshot]:
    unique_cutoffs = sorted(set(cutoffs))
    if not unique_cutoffs:
        return []
    accumulator = DensityAccumulator(mode=mode, precision=precision, exact_primes_max=exact_primes_max)
    primes = odd_primes_up_to(unique_cutoffs[-1])
    prime_index = 0
    rows: List[Snapshot] = []
    for cutoff in unique_cutoffs:
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            accumulator.step(primes[prime_index])
            prime_index += 1
        rows.append(accumulator.snapshot(cutoff))
    return rows


def search_target(
    y_max: int,
    target: Decimal,
    mode: str,
    precision: int,
    exact_primes_max: int,
) -> Tuple[bool, Snapshot]:
    accumulator = DensityAccumulator(mode=mode, precision=precision, exact_primes_max=exact_primes_max)
    primes = odd_primes_up_to(y_max)
    for prime in primes:
        accumulator.step(prime)
        if accumulator.current_delta() >= target:
            return True, accumulator.snapshot(prime)
    return False, accumulator.snapshot(y_max)


def print_markdown_table(rows: Sequence[Snapshot], digits: int, target: Decimal) -> None:
    headers = [
        "y",
        "p_max",
        "odd_primes",
        "mode",
        "lambda",
        "lower",
        "delta",
        "upper",
        "gap_to_delta_star",
    ]
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        gap = target - row.delta
        values = [
            str(row.cutoff),
            "-" if row.largest_prime is None else str(row.largest_prime),
            str(row.prime_count),
            row.arithmetic,
            format_fixed(row.lambda_sum, digits),
            format_fixed(row.lower_bound, digits),
            format_fixed(row.delta, digits),
            format_fixed(row.upper_bound, digits),
            format_fixed(gap, digits),
        ]
        print("| " + " | ".join(values) + " |")


def print_plain_table(rows: Sequence[Snapshot], digits: int, target: Decimal) -> None:
    headers = (
        "y",
        "p_max",
        "odd_primes",
        "mode",
        "lambda",
        "lower",
        "delta",
        "upper",
        "gap_to_delta_star",
    )
    print("\t".join(headers))
    for row in rows:
        gap = target - row.delta
        values = (
            str(row.cutoff),
            "-" if row.largest_prime is None else str(row.largest_prime),
            str(row.prime_count),
            row.arithmetic,
            format_fixed(row.lambda_sum, digits),
            format_fixed(row.lower_bound, digits),
            format_fixed(row.delta, digits),
            format_fixed(row.upper_bound, digits),
            format_fixed(gap, digits),
        )
        print("\t".join(values))


def print_snapshot(
    row: Snapshot,
    digits: int,
    target: Decimal,
    show_fraction: bool,
) -> None:
    print(f"cutoff y = {row.cutoff}")
    print(f"largest included prime = {row.largest_prime}")
    print(f"odd primes in S(y) = {row.prime_count}")
    print(f"arithmetic = {row.arithmetic}")
    print(f"lambda = {format_fixed(row.lambda_sum, digits)}")
    print(f"A_S = {format_fixed(row.a_value, digits)}")
    print(f"mu'_S = {format_fixed(row.mu_prime, digits)}")
    print(f"union-bound lower bound = {format_fixed(row.lower_bound, digits)}")
    print(f"delta_S = {format_fixed(row.delta, digits)}")
    print(f"one-coordinate upper bound = {format_fixed(row.upper_bound, digits)}")
    print(f"delta_* = {format_fixed(target, digits)}")
    print(f"gap to delta_* = {format_fixed(target - row.delta, digits)}")
    print(f"|P(X1=0) - A_S| = {format_scientific(row.x1_zero_error)}")
    print(f"|P(X2<=1) - A_S(1+mu'_S)| = {format_scientific(row.x2_le1_error)}")
    if show_fraction and row.exact_numerator is not None and row.exact_denominator is not None:
        print("exact_rational =")
        print(f"{row.exact_numerator}/{row.exact_denominator}")


def solve_monotone_float(target: float, func) -> float:
    lo = 0.0
    hi = 1.0
    while func(hi) < target:
        hi *= 2.0
        if hi > 1.0e6:
            raise RuntimeError("search interval grew unexpectedly large")
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if func(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def independent_poisson_delta(lam: float) -> float:
    exp_neg = exp(-lam)
    tail2 = 1.0 - exp_neg * (1.0 + lam)
    return (1.0 - exp_neg) * tail2 * tail2


def one_coordinate_two_hit_tail(lam: float) -> float:
    return 1.0 - exp(-lam) * (1.0 + lam)


def heuristic_report(calibrate_y: int, target: Decimal) -> None:
    primes = odd_primes_up_to(calibrate_y)
    lam = sum(1.0 / (prime - 1) for prime in primes)
    if calibrate_y <= math.e:
        raise SystemExit("--calibrate-y must exceed e")
    c_est = lam - log(log(calibrate_y))
    target_float = float(target)
    lam_two_hit = solve_monotone_float(target_float, one_coordinate_two_hit_tail)
    lam_full = solve_monotone_float(target_float, independent_poisson_delta)

    def log10_y_estimate(lambda_target: float) -> float:
        return exp(lambda_target - c_est) / log(10.0)

    print(f"calibration_y = {calibrate_y}")
    print(f"odd primes in S(y) = {len(primes)}")
    print(f"lambda(y) = {lam:.15f}")
    print(f"c_est = lambda(y) - log log y = {c_est:.15f}")
    print()
    print("Heuristic scales inferred from lambda(y) ~= log log y + c_est:")
    print(
        "one-coordinate two-hit scale "
        f"(needed even before intersecting all three conditions): "
        f"lambda ~= {lam_two_hit:.15f}, log10 y ~= {log10_y_estimate(lam_two_hit):.6f}"
    )
    print(
        "independent-Poisson crossover for "
        "P(X1>=1, X2>=2, X4>=2): "
        f"lambda ~= {lam_full:.15f}, log10 y ~= {log10_y_estimate(lam_full):.6f}"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--precision",
        type=int,
        default=80,
        help="Decimal working precision (default: 80)",
    )
    parser.add_argument(
        "--digits",
        type=int,
        default=18,
        help="digits after the decimal point in printed output (default: 18)",
    )
    parser.add_argument(
        "--mode",
        choices=("auto", "exact", "decimal"),
        default="auto",
        help="arithmetic mode for the 18-state DP (default: auto)",
    )
    parser.add_argument(
        "--exact-primes-max",
        type=int,
        default=2048,
        help="auto mode stays exact through this many odd primes (default: 2048)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    segment = subparsers.add_parser("segment", help="compute delta_S for one cutoff y")
    segment.add_argument("--y", type=int, required=True, help="use S(y) = {7 <= p <= y}")
    segment.add_argument(
        "--target",
        default="delta_star",
        help="comparison target, default delta_star",
    )
    segment.add_argument(
        "--show-fraction",
        action="store_true",
        help="print the exact rational when the current snapshot is exact",
    )

    sweep = subparsers.add_parser("sweep", help="compute several initial segments in one pass")
    sweep.add_argument("--ys", required=True, help="comma-separated cutoff list")
    sweep.add_argument(
        "--format",
        choices=("plain", "markdown"),
        default="plain",
        help="table output format (default: plain)",
    )
    sweep.add_argument(
        "--target",
        default="delta_star",
        help="comparison target, default delta_star",
    )

    search = subparsers.add_parser("search", help="search initial segments up to y_max")
    search.add_argument("--y-max", type=int, required=True, help="search over primes <= y_max")
    search.add_argument(
        "--target",
        default="delta_star",
        help="target density, default delta_star",
    )

    heuristic = subparsers.add_parser(
        "heuristic",
        help="report heuristic size scales from the observed prime harmonic sum",
    )
    heuristic.add_argument(
        "--calibrate-y",
        type=int,
        required=True,
        help="calibration cutoff for lambda(y)",
    )
    heuristic.add_argument(
        "--target",
        default="delta_star",
        help="target density, default delta_star",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    getcontext().prec = args.precision

    if args.command == "segment":
        target = parse_target(args.target, args.precision)
        row = scan_cutoffs(
            cutoffs=[args.y],
            mode=args.mode,
            precision=args.precision,
            exact_primes_max=args.exact_primes_max,
        )[0]
        print_snapshot(row, args.digits, target, show_fraction=args.show_fraction)
        return

    if args.command == "sweep":
        target = parse_target(args.target, args.precision)
        rows = scan_cutoffs(
            cutoffs=parse_int_list(args.ys),
            mode=args.mode,
            precision=args.precision,
            exact_primes_max=args.exact_primes_max,
        )
        if args.format == "markdown":
            print_markdown_table(rows, args.digits, target)
        else:
            print_plain_table(rows, args.digits, target)
        return

    if args.command == "search":
        target = parse_target(args.target, args.precision)
        reached, row = search_target(
            y_max=args.y_max,
            target=target,
            mode=args.mode,
            precision=args.precision,
            exact_primes_max=args.exact_primes_max,
        )
        if reached:
            print(f"target reached at y = {row.cutoff}")
        else:
            print(f"target not reached by y_max = {args.y_max}")
        print_snapshot(row, args.digits, target, show_fraction=False)
        return

    if args.command == "heuristic":
        target = parse_target(args.target, args.precision)
        heuristic_report(args.calibrate_y, target)
        return

    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    main()
