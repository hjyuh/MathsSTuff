from __future__ import annotations

import argparse
import json
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from sat_cnf_pipeline import (
    Solver,
    PYSAT_IMPORT_ERROR,
    build_info,
    edge_var,
    iter_clauses,
    make_edges,
    model_to_color,
    parse_pair,
    verify_full_coloring,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results"


@dataclass(frozen=True)
class Cube:
    cube_id: int
    label: str
    edge_colors: tuple[tuple[tuple[int, int], int], ...]

    def assumptions(self, edge_id: dict[tuple[int, int], int], r: int) -> list[int]:
        return [edge_var(edge_id[edge], color, r) for edge, color in self.edge_colors]

    def to_json(self) -> dict[str, object]:
        return {
            "cube_id": self.cube_id,
            "label": self.label,
            "fixed_edges": [
                {"edge": list(edge), "color": color} for edge, color in self.edge_colors
            ],
        }


def parse_pattern(text: str) -> tuple[int, ...]:
    try:
        values = tuple(int(part.strip()) for part in text.split(",") if part.strip() != "")
    except ValueError as exc:
        raise argparse.ArgumentTypeError("pattern must be comma-separated integers") from exc
    if not values:
        raise argparse.ArgumentTypeError("pattern must contain at least one color")
    return values


def restricted_growth_words(length: int, color_count: int) -> Iterator[tuple[int, ...]]:
    """Canonical color assignments modulo color-name permutations."""
    if length < 1:
        return

    prefix = [0]

    def extend(max_seen: int) -> Iterator[tuple[int, ...]]:
        if len(prefix) == length:
            yield tuple(prefix)
            return
        for color in range(min(color_count - 1, max_seen + 1) + 1):
            prefix.append(color)
            yield from extend(max(max_seen, color))
            prefix.pop()

    yield from extend(0)


def prefix_edges(n: int, count: int) -> list[tuple[int, int]]:
    edges, _ = make_edges(n)
    if count < 1 or count > len(edges):
        raise ValueError(f"prefix edge count must be in [1,{len(edges)}]")
    return edges[:count]


def star_edges(n: int, count: int) -> list[tuple[int, int]]:
    if count < 1 or count >= n:
        raise ValueError(f"star edge count must be in [1,{n - 1}]")
    return [(0, vertex) for vertex in range(1, count + 1)]


def make_cubes(args: argparse.Namespace) -> tuple[list[Cube], int]:
    n = args.r * args.r + 1
    cubes: list[Cube] = []

    if args.cube_mode == "star-pattern":
        pattern = args.star_pattern
        if any(color < 0 or color >= args.r for color in pattern):
            raise ValueError(f"star pattern colors must be in [0,{args.r - 1}]")
        edges = star_edges(n, len(pattern))
        cube = Cube(
            cube_id=0,
            label="star:" + ",".join(str(color) for color in pattern),
            edge_colors=tuple(zip(edges, pattern)),
        )
        return [cube], 1

    if args.cube_mode == "star-rgs":
        edges = star_edges(n, args.prefix_edges)
    elif args.cube_mode == "edge-prefix-rgs":
        edges = prefix_edges(n, args.prefix_edges)
    else:
        raise ValueError(f"unknown cube mode: {args.cube_mode}")

    all_words = list(restricted_growth_words(len(edges), args.r))
    total = len(all_words)
    selected = all_words[args.offset :]
    if args.max_cubes > 0:
        selected = selected[: args.max_cubes]

    for local_id, word in enumerate(selected, start=args.offset):
        edge_colors = tuple(zip(edges, word))
        cubes.append(
            Cube(
                cube_id=local_id,
                label=f"{args.cube_mode}:k={len(edges)}:" + ",".join(str(c) for c in word),
                edge_colors=edge_colors,
            )
        )
    return cubes, total


def status_name(result: bool | None) -> str:
    if result is True:
        return "sat"
    if result is False:
        return "unsat"
    return "unknown"


def stats_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    keys = sorted(set(before) | set(after))
    return {key: int(after.get(key, 0) - before.get(key, 0)) for key in keys}


def write_model(path: Path, model: list[int], r: int) -> tuple[bool, str]:
    edges, _ = make_edges(r * r + 1)
    colors = model_to_color(model, len(edges), r)
    ok, message = verify_full_coloring(r, colors)
    rows = [{"edge": list(edge), "color": color} for edge, color in zip(edges, colors)]
    path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    return ok, message


def default_out_prefix(args: argparse.Namespace) -> Path:
    suffix = f"{args.cube_mode}_k{args.prefix_edges}_budget{args.max_conflicts}_sec{args.max_seconds}"
    if args.max_cubes > 0:
        suffix += f"_max{args.max_cubes}"
    if args.offset:
        suffix += f"_off{args.offset}"
    return DEFAULT_RESULTS / f"cube_conquer_r{args.r}_{suffix}"


def solve_cubes(args: argparse.Namespace, cubes: list[Cube], total_cubes: int, out_prefix: Path) -> dict[str, object]:
    if Solver is None:
        return {
            "status": "pysat_unavailable",
            "pysat_error": PYSAT_IMPORT_ERROR,
            "cubes": [],
        }

    info = build_info(args)
    edges, edge_id = make_edges(info.n)
    out_prefix.parent.mkdir(parents=True, exist_ok=True)
    cube_rows_path = out_prefix.with_suffix(".cubes.jsonl")

    started = time.perf_counter()
    add_started = time.perf_counter()
    cube_rows: list[dict[str, object]] = []
    sat_model_path: str | None = None

    with Solver(name=args.solver) as solver:
        for clause in iter_clauses(args):
            solver.add_clause(clause)
        add_seconds = time.perf_counter() - add_started

        with cube_rows_path.open("w", encoding="utf-8", newline="\n") as handle:
            for cube in cubes:
                assumptions = cube.assumptions(edge_id, args.r)
                before = solver.accum_stats()
                solve_started = time.perf_counter()
                interrupted_by_wall_clock = False

                def interrupt_solver() -> None:
                    nonlocal interrupted_by_wall_clock
                    interrupted_by_wall_clock = True
                    solver.interrupt()

                timer: threading.Timer | None = None
                if args.max_seconds > 0:
                    if hasattr(solver, "clear_interrupt"):
                        solver.clear_interrupt()
                    timer = threading.Timer(args.max_seconds, interrupt_solver)
                    timer.daemon = True
                    timer.start()
                if args.max_conflicts > 0:
                    solver.conf_budget(args.max_conflicts)
                if args.max_propagations > 0:
                    solver.prop_budget(args.max_propagations)
                try:
                    if args.max_conflicts > 0 or args.max_propagations > 0 or args.max_seconds > 0:
                        result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                    else:
                        result = solver.solve(assumptions=assumptions)
                finally:
                    if timer is not None:
                        timer.cancel()
                    if hasattr(solver, "clear_interrupt"):
                        solver.clear_interrupt()
                solve_seconds = time.perf_counter() - solve_started
                after = solver.accum_stats()

                row = cube.to_json()
                row.update(
                    {
                        "status": status_name(result),
                        "assumptions": assumptions,
                        "solve_seconds": round(solve_seconds, 3),
                        "interrupted_by_wall_clock": interrupted_by_wall_clock,
                        "stats_delta": stats_delta(before, after),
                    }
                )

                if result is True and sat_model_path is None:
                    model_path = out_prefix.with_suffix(f".cube{cube.cube_id}.model.json")
                    ok, message = write_model(model_path, solver.get_model(), args.r)
                    sat_model_path = str(model_path)
                    row["model_path"] = sat_model_path
                    row["model_check"] = "valid" if ok else "invalid"
                    row["model_check_message"] = message

                cube_rows.append(row)
                handle.write(json.dumps(row, sort_keys=True))
                handle.write("\n")
                handle.flush()
                print(
                    json.dumps(
                        {
                            "cube_id": cube.cube_id,
                            "status": row["status"],
                            "solve_seconds": row["solve_seconds"],
                            "interrupted_by_wall_clock": interrupted_by_wall_clock,
                        }
                    ),
                    flush=True,
                )

                if result is True and args.stop_on_sat:
                    break

    counts = {"sat": 0, "unsat": 0, "unknown": 0}
    for row in cube_rows:
        counts[str(row["status"])] += 1

    return {
        "status": "sat_found" if counts["sat"] else ("all_unsat" if counts["unsat"] == len(cube_rows) else "incomplete"),
        "mode": "full",
        "r": info.r,
        "n": info.n,
        "variables": info.variables,
        "clauses": info.clauses,
        "edges": info.edges,
        "coverage_clauses": info.coverage_clauses,
        "exactly_one_clauses": info.exactly_one_clauses,
        "unit_clauses": info.unit_clauses,
        "cube_mode": args.cube_mode,
        "prefix_edges": args.prefix_edges,
        "generated_cubes": len(cubes),
        "completed_cubes": len(cube_rows),
        "total_canonical_cubes": total_cubes,
        "canonical_cube_fraction": round(len(cube_rows) / total_cubes, 6) if total_cubes else 0.0,
        "counts": counts,
        "solver": args.solver,
        "max_conflicts_per_cube": args.max_conflicts,
        "max_propagations_per_cube": args.max_propagations,
        "max_seconds_per_cube": args.max_seconds,
        "base_symmetry": args.symmetry,
        "seed": args.seed,
        "add_seconds": round(add_seconds, 3),
        "total_seconds": round(time.perf_counter() - started, 3),
        "cube_rows_path": str(cube_rows_path),
        "sat_model_path": sat_model_path,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cube-and-conquer helper for the EP617 full K26 5-color CNF."
    )
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--max-conflicts", type=int, default=2000, help="per-cube conflict budget; 0 means complete")
    parser.add_argument("--max-propagations", type=int, default=0, help="per-cube propagation budget")
    parser.add_argument("--max-seconds", type=float, default=10.0, help="per-cube wall-clock interrupt; 0 disables")
    parser.add_argument("--cube-mode", choices=["edge-prefix-rgs", "star-rgs", "star-pattern"], default="edge-prefix-rgs")
    parser.add_argument("--prefix-edges", type=int, default=5)
    parser.add_argument("--star-pattern", type=parse_pattern, default=(0, 1, 2, 3, 4))
    parser.add_argument("--max-cubes", type=int, default=0, help="0 means all generated cubes")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--stop-on-sat", action="store_true")
    parser.add_argument("--out-prefix", type=Path, default=None)
    parser.add_argument("--symmetry", choices=["none", "edge", "star"], default="none")
    parser.add_argument("--seed", choices=["none", "affine"], default="none")
    parser.add_argument("--affine-merge", type=parse_pair, default=(0, 1))
    args = parser.parse_args()

    if args.r != 5:
        raise SystemExit("this helper is scoped to the EP617 r=5 sprint")
    if args.offset < 0:
        raise SystemExit("--offset must be nonnegative")
    args.mode = "full"

    out_prefix = args.out_prefix or default_out_prefix(args)
    out_prefix.parent.mkdir(parents=True, exist_ok=True)

    cubes, total_cubes = make_cubes(args)
    summary = solve_cubes(args, cubes, total_cubes, out_prefix)
    summary_path = out_prefix.with_suffix(".summary.json")
    summary["summary_path"] = str(summary_path)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))

    if summary["status"] == "sat_found":
        return 10
    if summary["status"] == "all_unsat":
        return 20
    if summary["status"] == "pysat_unavailable":
        return 30
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
