#!/usr/bin/env python3
"""Toy kernel-feasibility probe for Erdos Problem 689.

This script builds a simplified residue-free continuum model for the
deterministic kernel feasibility lemma from the averaged-nibble route.

Model choices:

- coefficient cores use odd ``a`` on the ``A1`` side and even ``b`` on the
  ``A2`` side, with ``gcd(a, b) = 1``;
- labels are binned by ``t = P / n`` in ``(1/5, beta]``;
- target positions are binned by ``z = x / n`` or ``y / n`` on ``(0, 1]``;
- an oriented cell contributes along the geometric relation
      z_y = z_x + 2 t
  or the reverse orientation;
- residue classes modulo ``W`` are ignored, while a scalar ``rho`` plays the
  role of a coarse robust-label density on the target sides.

For a cell with source-width ``dz`` and label-bin width ``dt``, the simplified
load coefficients are

    label gain = dz / (2 a b),
    A1 load    = rho * dt / b,
    A2 load    = rho * dt / a.

If SciPy is available, the script solves the exact discretized LP maximizing
``gamma`` subject to label load ``= 1`` and target loads ``<= 1 - gamma``.
Otherwise it falls back to a greedy fractional packer over a fixed gamma grid.

The greedy path is heuristic only.  Positive outcomes there are finite evidence
that this toy discretization can be balanced; negative outcomes are not
certificates against the actual deterministic kernel lemma.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import random
import statistics
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple


LABEL_LOWER = 0.2
DEFAULT_GAMMA_MAX = 0.40
DEFAULT_GAMMA_STEP = 0.02
DEFAULT_KERNEL_CAP = 128.0
TOL = 1e-9


@dataclass(frozen=True)
class CoreFamily:
    name: str
    a_values: Tuple[int, ...]
    b_values: Tuple[int, ...]
    description: str


@dataclass(frozen=True)
class Scenario:
    name: str
    beta: float
    rho: float
    description: str


@dataclass(frozen=True)
class Cell:
    label_index: int
    a1_index: int
    a2_index: int
    gain: float
    load_a1: float
    load_a2: float


@dataclass
class BuiltInstance:
    core: CoreFamily
    scenario: Scenario
    t_bins: int
    z_bins: int
    dt: float
    dz: float
    kernel_cap: float
    t_values: List[float]
    z_values: List[float]
    a1_vertices: List[Tuple[int, int]]
    a2_vertices: List[Tuple[int, int]]
    coprime_pairs: List[Tuple[int, int]]
    cells: List[Cell]
    cells_by_label: List[List[int]]
    cells_by_a1: List[List[int]]
    cells_by_a2: List[List[int]]


@dataclass
class GreedyResult:
    gamma: float
    fill_fraction: float
    full_saturation: bool
    unsatisfied_bins: int
    max_a1_load: float
    max_a2_load: float
    max_target_load: float
    mean_a1_load: float
    mean_a2_load: float
    tight_a1: int
    tight_a2: int
    used_cell_max: float
    cap_hits: int
    steps: int


DEFAULT_CORES: Dict[str, CoreFamily] = {
    "pair12": CoreFamily(
        name="pair12",
        a_values=(1,),
        b_values=(2,),
        description="single coefficient pair (1, 2)",
    ),
    "small": CoreFamily(
        name="small",
        a_values=(1, 3),
        b_values=(2, 4),
        description="two odd cores against two even cores",
    ),
    "medium": CoreFamily(
        name="medium",
        a_values=(1, 3, 5),
        b_values=(2, 4, 6),
        description="three odd cores against three even cores",
    ),
    "wide": CoreFamily(
        name="wide",
        a_values=(1, 3, 5, 7),
        b_values=(2, 4, 6, 8),
        description="four odd cores against four even cores",
    ),
}


DEFAULT_SCENARIOS: Dict[str, Scenario] = {
    "sanity_low": Scenario(
        name="sanity_low",
        beta=0.35,
        rho=0.75,
        description="easy sanity check far from the 10/11 window",
    ),
    "sanity_mid": Scenario(
        name="sanity_mid",
        beta=0.45,
        rho=0.85,
        description="tighter sanity check, still below the true density window",
    ),
    "threshold_like": Scenario(
        name="threshold_like",
        beta=0.49,
        rho=0.92,
        description="threshold-like test with rho > 10/11 and beta just above 1/rho - 3/5",
    ),
}


def scipy_available() -> bool:
    return importlib.util.find_spec("scipy") is not None


def parse_name_list(spec: str, available: Dict[str, object]) -> List[str]:
    names = [part.strip() for part in spec.split(",") if part.strip()]
    if not names or names == ["all"]:
        return list(available)
    bad = [name for name in names if name not in available]
    if bad:
        raise SystemExit(f"unknown names: {', '.join(bad)}")
    return names


def build_gamma_grid(gamma_max: float, gamma_step: float) -> List[float]:
    if gamma_max < 0 or gamma_step <= 0:
        raise SystemExit("--gamma-max must be nonnegative and --gamma-step positive")
    count = int(round(gamma_max / gamma_step))
    grid = [round(gamma_max - i * gamma_step, 10) for i in range(count + 1)]
    if not grid or grid[-1] != 0.0:
        grid.append(0.0)
    return sorted(set(max(0.0, value) for value in grid), reverse=True)


def round_float(value: float) -> float:
    return round(float(value), 6)


def mean_or_zero(values: Sequence[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def build_instance(
    core: CoreFamily,
    scenario: Scenario,
    t_bins: int,
    z_bins: int,
    kernel_cap: float,
) -> BuiltInstance:
    if t_bins <= 0 or z_bins <= 0:
        raise SystemExit("--t-bins and --z-bins must be positive")
    if not (LABEL_LOWER < scenario.beta < 0.5):
        raise SystemExit(f"beta must lie in (1/5, 1/2); got {scenario.beta}")

    dt = (scenario.beta - LABEL_LOWER) / t_bins
    dz = 1.0 / z_bins
    t_values = [LABEL_LOWER + (index + 0.5) * dt for index in range(t_bins)]
    z_values = [(index + 0.5) * dz for index in range(z_bins)]

    a1_vertices = [(a, z_index) for a in core.a_values for z_index in range(z_bins)]
    a2_vertices = [(b, z_index) for b in core.b_values for z_index in range(z_bins)]
    a1_lookup = {vertex: index for index, vertex in enumerate(a1_vertices)}
    a2_lookup = {vertex: index for index, vertex in enumerate(a2_vertices)}

    coprime_pairs = [
        (a, b)
        for a in core.a_values
        for b in core.b_values
        if math.gcd(a, b) == 1
    ]

    cells: List[Cell] = []
    cells_by_label: List[List[int]] = [[] for _ in range(t_bins)]
    cells_by_a1: List[List[int]] = [[] for _ in range(len(a1_vertices))]
    cells_by_a2: List[List[int]] = [[] for _ in range(len(a2_vertices))]

    z_top = z_values[-1] + 1e-12
    for label_index, t_value in enumerate(t_values):
        for a_value, b_value in coprime_pairs:
            gain = dz / (2.0 * a_value * b_value)
            load_a1 = scenario.rho * dt / b_value
            load_a2 = scenario.rho * dt / a_value
            for source_index, z_value in enumerate(z_values):
                shifted = z_value + 2.0 * t_value
                if shifted > z_top:
                    continue

                target_bin = min(z_bins - 1, max(0, int(shifted / dz)))

                forward = Cell(
                    label_index=label_index,
                    a1_index=a1_lookup[(a_value, source_index)],
                    a2_index=a2_lookup[(b_value, target_bin)],
                    gain=gain,
                    load_a1=load_a1,
                    load_a2=load_a2,
                )
                forward_index = len(cells)
                cells.append(forward)
                cells_by_label[label_index].append(forward_index)
                cells_by_a1[forward.a1_index].append(forward_index)
                cells_by_a2[forward.a2_index].append(forward_index)

                reverse = Cell(
                    label_index=label_index,
                    a1_index=a1_lookup[(a_value, target_bin)],
                    a2_index=a2_lookup[(b_value, source_index)],
                    gain=gain,
                    load_a1=load_a1,
                    load_a2=load_a2,
                )
                reverse_index = len(cells)
                cells.append(reverse)
                cells_by_label[label_index].append(reverse_index)
                cells_by_a1[reverse.a1_index].append(reverse_index)
                cells_by_a2[reverse.a2_index].append(reverse_index)

    return BuiltInstance(
        core=core,
        scenario=scenario,
        t_bins=t_bins,
        z_bins=z_bins,
        dt=dt,
        dz=dz,
        kernel_cap=kernel_cap,
        t_values=t_values,
        z_values=z_values,
        a1_vertices=a1_vertices,
        a2_vertices=a2_vertices,
        coprime_pairs=coprime_pairs,
        cells=cells,
        cells_by_label=cells_by_label,
        cells_by_a1=cells_by_a1,
        cells_by_a2=cells_by_a2,
    )


def lp_solution_summary(
    instance: BuiltInstance,
    gamma: float,
    weights: Sequence[float],
    seconds: float,
) -> Dict[str, object]:
    a1_loads = [0.0] * len(instance.a1_vertices)
    a2_loads = [0.0] * len(instance.a2_vertices)
    for index, cell in enumerate(instance.cells):
        weight = weights[index]
        if weight <= 0:
            continue
        a1_loads[cell.a1_index] += weight * cell.load_a1
        a2_loads[cell.a2_index] += weight * cell.load_a2

    cap = 1.0 - gamma
    return {
        "mode": "lp",
        "gamma": round_float(gamma),
        "full_saturation": True,
        "max_a1_load": round_float(max(a1_loads) if a1_loads else 0.0),
        "max_a2_load": round_float(max(a2_loads) if a2_loads else 0.0),
        "max_target_load": round_float(max(a1_loads + a2_loads) if a1_loads or a2_loads else 0.0),
        "mean_a1_load": round_float(mean_or_zero(a1_loads)),
        "mean_a2_load": round_float(mean_or_zero(a2_loads)),
        "tight_a1": sum(1 for value in a1_loads if value >= cap - 1e-6),
        "tight_a2": sum(1 for value in a2_loads if value >= cap - 1e-6),
        "used_cell_max": round_float(max(weights) if weights else 0.0),
        "cap_hits": sum(1 for value in weights if value >= instance.kernel_cap - 1e-6),
        "seconds": round_float(seconds),
    }


def solve_lp(instance: BuiltInstance, gamma_max: float) -> Dict[str, object]:
    from scipy.optimize import linprog

    start = time.perf_counter()
    variable_count = len(instance.cells) + 1
    gamma_index = len(instance.cells)

    objective = [0.0] * variable_count
    objective[gamma_index] = -1.0

    a_eq: List[List[float]] = []
    b_eq: List[float] = []
    for label_index, cell_indices in enumerate(instance.cells_by_label):
        row = [0.0] * variable_count
        for cell_index in cell_indices:
            row[cell_index] = instance.cells[cell_index].gain
        a_eq.append(row)
        b_eq.append(1.0)

    a_ub: List[List[float]] = []
    b_ub: List[float] = []
    for cell_indices in instance.cells_by_a1:
        row = [0.0] * variable_count
        for cell_index in cell_indices:
            row[cell_index] = instance.cells[cell_index].load_a1
        row[gamma_index] = 1.0
        a_ub.append(row)
        b_ub.append(1.0)

    for cell_indices in instance.cells_by_a2:
        row = [0.0] * variable_count
        for cell_index in cell_indices:
            row[cell_index] = instance.cells[cell_index].load_a2
        row[gamma_index] = 1.0
        a_ub.append(row)
        b_ub.append(1.0)

    bounds = [(0.0, instance.kernel_cap)] * len(instance.cells) + [(0.0, gamma_max)]
    result = linprog(
        c=objective,
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    seconds = time.perf_counter() - start

    if not result.success:
        return {
            "mode": "lp",
            "full_saturation": False,
            "gamma": None,
            "status": result.status,
            "message": result.message,
            "seconds": round_float(seconds),
        }

    gamma = float(result.x[gamma_index])
    weights = [float(value) for value in result.x[: len(instance.cells)]]
    summary = lp_solution_summary(instance, gamma, weights, seconds)
    summary["status"] = result.status
    summary["message"] = result.message
    return summary


def greedy_trial(instance: BuiltInstance, gamma: float, seed: int) -> GreedyResult:
    capacity = 1.0 - gamma
    remaining_a1 = [capacity] * len(instance.a1_vertices)
    remaining_a2 = [capacity] * len(instance.a2_vertices)
    remaining_label = [1.0] * len(instance.t_values)
    used = [0.0] * len(instance.cells)
    rng = random.Random(seed)

    progress = True
    steps = 0

    while progress and any(value > TOL for value in remaining_label):
        progress = False
        hardness: List[Tuple[float, int, float, int]] = []
        for label_index, demand in enumerate(remaining_label):
            if demand <= TOL:
                continue

            available_label_mass = 0.0
            active_cells = 0
            for cell_index in instance.cells_by_label[label_index]:
                cell = instance.cells[cell_index]
                max_weight = min(
                    instance.kernel_cap - used[cell_index],
                    remaining_a1[cell.a1_index] / cell.load_a1 if cell.load_a1 else 0.0,
                    remaining_a2[cell.a2_index] / cell.load_a2 if cell.load_a2 else 0.0,
                )
                if max_weight > TOL:
                    available_label_mass += max_weight * cell.gain
                    active_cells += 1

            hardness.append(
                (
                    available_label_mass / demand if demand else 0.0,
                    active_cells,
                    rng.random(),
                    label_index,
                )
            )

        if not hardness:
            break

        hardness.sort(key=lambda item: (item[0], item[1], item[2]))
        label_index = hardness[0][3]

        while remaining_label[label_index] > TOL:
            best_choice: Optional[Tuple[float, float, int, float]] = None
            for cell_index in instance.cells_by_label[label_index]:
                cell = instance.cells[cell_index]
                max_weight = min(
                    instance.kernel_cap - used[cell_index],
                    remaining_a1[cell.a1_index] / cell.load_a1 if cell.load_a1 else 0.0,
                    remaining_a2[cell.a2_index] / cell.load_a2 if cell.load_a2 else 0.0,
                    remaining_label[label_index] / cell.gain,
                )
                if max_weight <= TOL:
                    continue

                price = (
                    cell.load_a1 / (remaining_a1[cell.a1_index] + 1e-9)
                    + cell.load_a2 / (remaining_a2[cell.a2_index] + 1e-9)
                ) / cell.gain
                price += 0.03 * rng.random()
                choice = (price, -(max_weight * cell.gain), cell_index, max_weight)
                if best_choice is None or choice < best_choice:
                    best_choice = choice

            if best_choice is None:
                break

            _, _, cell_index, max_weight = best_choice
            cell = instance.cells[cell_index]
            used[cell_index] += max_weight
            remaining_a1[cell.a1_index] -= max_weight * cell.load_a1
            remaining_a2[cell.a2_index] -= max_weight * cell.load_a2
            remaining_label[label_index] -= max_weight * cell.gain
            progress = True
            steps += 1

    a1_loads = [capacity - value for value in remaining_a1]
    a2_loads = [capacity - value for value in remaining_a2]
    fill_fraction = 1.0 - sum(max(0.0, value) for value in remaining_label) / len(remaining_label)
    max_target_load = max(a1_loads + a2_loads) if a1_loads or a2_loads else 0.0
    full_saturation = fill_fraction >= 1.0 - 1e-7

    return GreedyResult(
        gamma=gamma,
        fill_fraction=fill_fraction,
        full_saturation=full_saturation,
        unsatisfied_bins=sum(1 for value in remaining_label if value > 1e-7),
        max_a1_load=max(a1_loads) if a1_loads else 0.0,
        max_a2_load=max(a2_loads) if a2_loads else 0.0,
        max_target_load=max_target_load,
        mean_a1_load=mean_or_zero(a1_loads),
        mean_a2_load=mean_or_zero(a2_loads),
        tight_a1=sum(1 for value in a1_loads if value >= capacity - 1e-6),
        tight_a2=sum(1 for value in a2_loads if value >= capacity - 1e-6),
        used_cell_max=max(used) if used else 0.0,
        cap_hits=sum(1 for value in used if value >= instance.kernel_cap - 1e-6),
        steps=steps,
    )


def greedy_key(result: GreedyResult) -> Tuple[bool, float, float, int]:
    return (
        result.full_saturation,
        result.fill_fraction,
        -result.max_target_load,
        -result.unsatisfied_bins,
    )


def greedy_result_summary(result: GreedyResult, seconds: float) -> Dict[str, object]:
    return {
        "gamma": round_float(result.gamma),
        "fill_fraction": round_float(result.fill_fraction),
        "full_saturation": result.full_saturation,
        "unsatisfied_bins": result.unsatisfied_bins,
        "max_a1_load": round_float(result.max_a1_load),
        "max_a2_load": round_float(result.max_a2_load),
        "max_target_load": round_float(result.max_target_load),
        "mean_a1_load": round_float(result.mean_a1_load),
        "mean_a2_load": round_float(result.mean_a2_load),
        "tight_a1": result.tight_a1,
        "tight_a2": result.tight_a2,
        "used_cell_max": round_float(result.used_cell_max),
        "cap_hits": result.cap_hits,
        "steps": result.steps,
        "seconds": round_float(seconds),
    }


def solve_greedy(
    instance: BuiltInstance,
    gamma_grid: Sequence[float],
    trials: int,
    seed: int,
) -> Dict[str, object]:
    start = time.perf_counter()
    attempts: List[Dict[str, object]] = []
    best_full: Optional[GreedyResult] = None
    baseline: Optional[GreedyResult] = None

    for gamma_index, gamma in enumerate(gamma_grid):
        gamma_start = time.perf_counter()
        best_attempt: Optional[GreedyResult] = None
        for trial_index in range(trials):
            attempt = greedy_trial(
                instance,
                gamma,
                seed + 1009 * gamma_index + 7919 * trial_index,
            )
            if best_attempt is None or greedy_key(attempt) > greedy_key(best_attempt):
                best_attempt = attempt

        assert best_attempt is not None
        attempt_summary = greedy_result_summary(best_attempt, time.perf_counter() - gamma_start)
        attempts.append(attempt_summary)
        if abs(gamma) <= 1e-12:
            baseline = best_attempt
        if best_attempt.full_saturation and (
            best_full is None or best_attempt.gamma > best_full.gamma
        ):
            best_full = best_attempt

    assert baseline is not None
    payload: Dict[str, object] = {
        "mode": "greedy",
        "best_full_gamma": round_float(best_full.gamma) if best_full is not None else None,
        "best_full_result": greedy_result_summary(best_full, 0.0) if best_full is not None else None,
        "gamma0_result": greedy_result_summary(baseline, 0.0),
        "gamma_grid_results": attempts,
        "seconds": round_float(time.perf_counter() - start),
        "trials_per_gamma": trials,
    }
    return payload


def run_probe(
    core: CoreFamily,
    scenario: Scenario,
    args: argparse.Namespace,
) -> Dict[str, object]:
    instance = build_instance(core, scenario, args.t_bins, args.z_bins, args.kernel_cap)
    gamma_grid = build_gamma_grid(args.gamma_max, args.gamma_step)
    label_supports = [len(cell_indices) for cell_indices in instance.cells_by_label]

    if args.solver == "lp":
        if not scipy_available():
            raise SystemExit("SciPy is not available, so --solver lp cannot run here")
        solve_payload = solve_lp(instance, args.gamma_max)
    elif args.solver == "auto" and scipy_available():
        solve_payload = solve_lp(instance, args.gamma_max)
    else:
        solve_payload = solve_greedy(instance, gamma_grid, args.trials, args.seed)

    return {
        "core": {
            "name": core.name,
            "a_values": list(core.a_values),
            "b_values": list(core.b_values),
            "description": core.description,
            "coprime_pairs": [list(pair) for pair in instance.coprime_pairs],
        },
        "scenario": {
            "name": scenario.name,
            "beta": round_float(scenario.beta),
            "rho": round_float(scenario.rho),
            "beta_threshold": round_float(1.0 / scenario.rho - 0.6),
            "description": scenario.description,
        },
        "grid": {
            "t_bins": instance.t_bins,
            "z_bins": instance.z_bins,
            "dt": round_float(instance.dt),
            "dz": round_float(instance.dz),
            "kernel_cap": round_float(instance.kernel_cap),
            "label_support_min": min(label_supports) if label_supports else 0,
            "label_support_mean": round_float(mean_or_zero(label_supports)),
            "label_support_max": max(label_supports) if label_supports else 0,
            "cell_count": len(instance.cells),
        },
        "solver": {
            "requested": args.solver,
            "scipy_available": scipy_available(),
            "gamma_grid": [round_float(value) for value in gamma_grid],
            "seed": args.seed,
        },
        "result": solve_payload,
    }


def command_run(args: argparse.Namespace) -> None:
    core = DEFAULT_CORES[args.core]
    scenario = DEFAULT_SCENARIOS[args.scenario]
    payload = run_probe(core, scenario, args)
    print(json.dumps(payload, indent=2, sort_keys=True))


def command_suite(args: argparse.Namespace) -> None:
    core_names = parse_name_list(args.cores, DEFAULT_CORES)
    scenario_names = parse_name_list(args.scenarios, DEFAULT_SCENARIOS)
    start = time.perf_counter()
    rows = []
    for scenario_name in scenario_names:
        scenario = DEFAULT_SCENARIOS[scenario_name]
        for core_name in core_names:
            core = DEFAULT_CORES[core_name]
            rows.append(run_probe(core, scenario, args))

    payload = {
        "rows": rows,
        "seconds": round_float(time.perf_counter() - start),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Toy discretized probe for the deterministic kernel feasibility lemma."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common_arguments(target: argparse.ArgumentParser) -> None:
        target.add_argument(
            "--solver",
            choices=("auto", "lp", "greedy"),
            default="auto",
            help="Use SciPy LP when available, otherwise the greedy fallback.",
        )
        target.add_argument("--t-bins", type=int, default=18)
        target.add_argument("--z-bins", type=int, default=48)
        target.add_argument("--kernel-cap", type=float, default=DEFAULT_KERNEL_CAP)
        target.add_argument("--gamma-max", type=float, default=DEFAULT_GAMMA_MAX)
        target.add_argument("--gamma-step", type=float, default=DEFAULT_GAMMA_STEP)
        target.add_argument("--trials", type=int, default=12)
        target.add_argument("--seed", type=int, default=689)

    run = sub.add_parser("run", help="Run one core/scenario pair.")
    run.add_argument("--core", choices=sorted(DEFAULT_CORES), required=True)
    run.add_argument("--scenario", choices=sorted(DEFAULT_SCENARIOS), required=True)
    add_common_arguments(run)
    run.set_defaults(func=command_run)

    suite = sub.add_parser("suite", help="Run the default toy-core suite.")
    suite.add_argument(
        "--cores",
        default="pair12,small,medium,wide",
        help="Comma-separated core family names or 'all'.",
    )
    suite.add_argument(
        "--scenarios",
        default="sanity_low,sanity_mid,threshold_like",
        help="Comma-separated scenario names or 'all'.",
    )
    add_common_arguments(suite)
    suite.set_defaults(func=command_suite)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.kernel_cap <= 0:
        parser.error("--kernel-cap must be positive")
    if args.trials <= 0:
        parser.error("--trials must be positive")
    args.func(args)


if __name__ == "__main__":
    main()
