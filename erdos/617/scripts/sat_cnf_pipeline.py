from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator


try:
    from pysat.solvers import Solver

    PYSAT_IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover - exercised only without PySAT
    Solver = None  # type: ignore[assignment]
    PYSAT_IMPORT_ERROR = repr(exc)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results"


@dataclass(frozen=True)
class CnfInfo:
    mode: str
    r: int
    n: int
    variables: int
    clauses: int
    edges: int
    coverage_clauses: int
    exactly_one_clauses: int
    unit_clauses: int


def parse_pair(text: str) -> tuple[int, int]:
    parts = [int(x.strip()) for x in text.split(",")]
    if len(parts) != 2 or parts[0] == parts[1]:
        raise argparse.ArgumentTypeError("expected two distinct comma-separated integers")
    return parts[0], parts[1]


def make_edges(n: int) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return edges, {edge: idx for idx, edge in enumerate(edges)}


def edge_var(edge_id: int, color: int, r: int) -> int:
    return edge_id * r + color + 1


def star_var(vertex: int, color: int, r: int) -> int:
    return vertex * r + color + 1


def slope_class(p: int, a: tuple[int, int], b: tuple[int, int]) -> int:
    dx = (b[0] - a[0]) % p
    dy = (b[1] - a[1]) % p
    if dx == 0:
        return p
    return (dy * pow(dx, -1, p)) % p


def affine_coloring(p: int, merge: tuple[int, int]) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    """K_{p^2} coloring from affine-plane slopes, with two slopes merged."""
    if any(s < 0 or s > p for s in merge):
        raise ValueError(f"affine slopes must be in [0,{p}]")

    points = [(x, y) for x in range(p) for y in range(p)]
    color_of_slope: dict[int, int] = {}
    color = 0
    color_of_slope[merge[0]] = color
    color_of_slope[merge[1]] = color
    color += 1
    for slope in range(p + 1):
        if slope not in merge:
            color_of_slope[slope] = color
            color += 1
    if color != p:
        raise ValueError(f"merge={merge} did not produce {p} colors")

    edge_color = {}
    for i, u in enumerate(points):
        for j in range(i + 1, len(points)):
            v = points[j]
            edge_color[(i, j)] = color_of_slope[slope_class(p, u, v)]
    return points, edge_color


def colors_on_subset(subset: tuple[int, ...], edge_color: dict[tuple[int, int], int]) -> set[int]:
    colors = set()
    for i, j in itertools.combinations(subset, 2):
        if i > j:
            i, j = j, i
        colors.add(edge_color[(i, j)])
    return colors


def validate_affine_seed(r: int, merge: tuple[int, int]) -> tuple[bool, tuple[int, ...] | None]:
    points, edge_color = affine_coloring(r, merge)
    all_colors = set(range(r))
    for subset in itertools.combinations(range(len(points)), r + 1):
        if colors_on_subset(subset, edge_color) != all_colors:
            return False, subset
    return True, None


def exact_one_edge_clauses(edge_count: int, r: int) -> Iterator[list[int]]:
    for eid in range(edge_count):
        yield [edge_var(eid, color, r) for color in range(r)]
        for a, b in itertools.combinations(range(r), 2):
            yield [-edge_var(eid, a, r), -edge_var(eid, b, r)]


def exact_one_star_clauses(vertex_count: int, r: int) -> Iterator[list[int]]:
    for vertex in range(vertex_count):
        yield [star_var(vertex, color, r) for color in range(r)]
        for a, b in itertools.combinations(range(r), 2):
            yield [-star_var(vertex, a, r), -star_var(vertex, b, r)]


def full_symmetry_units(
    r: int,
    edge_id: dict[tuple[int, int], int],
    symmetry: str,
) -> Iterator[list[int]]:
    if symmetry == "none":
        return
    if symmetry == "edge":
        yield [edge_var(edge_id[(0, 1)], 0, r)]
        return
    if symmetry == "star":
        for color in range(r):
            yield [edge_var(edge_id[(0, color + 1)], color, r)]
        return
    raise ValueError(f"unknown symmetry mode: {symmetry}")


def affine_seed_units(
    r: int,
    edge_id: dict[tuple[int, int], int],
    merge: tuple[int, int],
) -> Iterator[list[int]]:
    _, edge_color = affine_coloring(r, merge)
    for edge, color in edge_color.items():
        yield [edge_var(edge_id[edge], color, r)]


def full_coverage_clauses(
    r: int,
    n: int,
    edge_id: dict[tuple[int, int], int],
) -> Iterator[list[int]]:
    for subset in itertools.combinations(range(n), r + 1):
        subset_edges = [edge_id[(i, j)] for i, j in itertools.combinations(subset, 2)]
        for color in range(r):
            yield [edge_var(eid, color, r) for eid in subset_edges]


def affine_extension_clauses(
    r: int,
    merge: tuple[int, int],
) -> Iterator[list[int]]:
    _, edge_color = affine_coloring(r, merge)
    all_mask = (1 << r) - 1
    for subset in itertools.combinations(range(r * r), r):
        mask = 0
        for i, j in itertools.combinations(subset, 2):
            if i > j:
                i, j = j, i
            mask |= 1 << edge_color[(i, j)]
        missing = all_mask ^ mask
        while missing:
            bit = missing & -missing
            color = bit.bit_length() - 1
            yield [star_var(vertex, color, r) for vertex in subset]
            missing ^= bit


def count_affine_extension_coverage(r: int, merge: tuple[int, int]) -> int:
    return sum(1 for _ in affine_extension_clauses(r, merge))


def count_units(r: int, symmetry: str, seed: str) -> int:
    units = 0
    if symmetry == "edge":
        units += 1
    elif symmetry == "star":
        units += r
    if seed == "affine":
        units += math.comb(r * r, 2)
    return units


def build_info(args: argparse.Namespace) -> CnfInfo:
    r = args.r
    if args.mode == "full":
        n = r * r + 1
        edge_count = math.comb(n, 2)
        exactly_one = edge_count * (1 + math.comb(r, 2))
        coverage = math.comb(n, r + 1) * r
        units = count_units(r, args.symmetry, args.seed)
        return CnfInfo(
            mode=args.mode,
            r=r,
            n=n,
            variables=edge_count * r,
            clauses=exactly_one + coverage + units,
            edges=edge_count,
            coverage_clauses=coverage,
            exactly_one_clauses=exactly_one,
            unit_clauses=units,
        )

    vertex_count = r * r
    exactly_one = vertex_count * (1 + math.comb(r, 2))
    coverage = count_affine_extension_coverage(r, args.affine_merge)
    return CnfInfo(
        mode=args.mode,
        r=r,
        n=r * r + 1,
        variables=vertex_count * r,
        clauses=exactly_one + coverage,
        edges=vertex_count,
        coverage_clauses=coverage,
        exactly_one_clauses=exactly_one,
        unit_clauses=0,
    )


def iter_clauses(args: argparse.Namespace) -> Iterator[list[int]]:
    r = args.r
    if args.mode == "full":
        n = r * r + 1
        edges, edge_id = make_edges(n)
        yield from exact_one_edge_clauses(len(edges), r)
        yield from full_coverage_clauses(r, n, edge_id)
        yield from full_symmetry_units(r, edge_id, args.symmetry)
        if args.seed == "affine":
            yield from affine_seed_units(r, edge_id, args.affine_merge)
    else:
        yield from exact_one_star_clauses(r * r, r)
        yield from affine_extension_clauses(r, args.affine_merge)


def write_dimacs(path: Path, info: CnfInfo, clauses: Iterable[list[int]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="ascii", newline="\n") as handle:
        handle.write(f"p cnf {info.variables} {info.clauses}\n")
        for clause in clauses:
            handle.write(" ".join(str(lit) for lit in clause))
            handle.write(" 0\n")


def model_to_color(model: list[int], item_count: int, r: int) -> list[int]:
    positive = {lit for lit in model if lit > 0}
    colors = []
    for item in range(item_count):
        chosen = [color for color in range(r) if item * r + color + 1 in positive]
        if len(chosen) != 1:
            raise ValueError(f"model has {len(chosen)} colors for item {item}")
        colors.append(chosen[0])
    return colors


def verify_full_coloring(r: int, colors: list[int]) -> tuple[bool, str]:
    n = r * r + 1
    edges, edge_id = make_edges(n)
    if len(colors) != len(edges):
        return False, f"expected {len(edges)} edge colors, found {len(colors)}"
    if any(color < 0 or color >= r for color in colors):
        return False, "edge color outside allowed range"
    for subset in itertools.combinations(range(n), r + 1):
        seen = set()
        for i, j in itertools.combinations(subset, 2):
            seen.add(colors[edge_id[(i, j)]])
        if len(seen) < r:
            return False, f"subset {subset} misses colors {sorted(set(range(r)) - seen)}"
    return True, "ok"


def verify_affine_extension(r: int, merge: tuple[int, int], star_colors: list[int]) -> tuple[bool, str]:
    if len(star_colors) != r * r:
        return False, f"expected {r * r} star colors, found {len(star_colors)}"
    if any(color < 0 or color >= r for color in star_colors):
        return False, "star color outside allowed range"
    _, edge_color = affine_coloring(r, merge)
    all_colors = set(range(r))
    for subset in itertools.combinations(range(r * r), r):
        seen = {star_colors[v] for v in subset}
        for i, j in itertools.combinations(subset, 2):
            if i > j:
                i, j = j, i
            seen.add(edge_color[(i, j)])
        if seen != all_colors:
            return False, f"old subset {subset} misses colors {sorted(all_colors - seen)}"
    return True, "ok"


def write_model(args: argparse.Namespace, model: list[int], out_prefix: Path) -> tuple[Path, bool, str]:
    r = args.r
    if args.mode == "full":
        edges, _ = make_edges(r * r + 1)
        colors = model_to_color(model, len(edges), r)
        ok, message = verify_full_coloring(r, colors)
        rows = [{"edge": list(edge), "color": color} for edge, color in zip(edges, colors)]
    else:
        colors = model_to_color(model, r * r, r)
        ok, message = verify_affine_extension(r, args.affine_merge, colors)
        rows = [{"edge": [r * r, vertex], "color": color} for vertex, color in enumerate(colors)]

    path = out_prefix.with_suffix(".model.json")
    path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    return path, ok, message


def solve_with_pysat(args: argparse.Namespace, info: CnfInfo) -> tuple[str, list[int] | None, dict[str, object]]:
    if Solver is None:
        return "unknown", None, {"pysat_error": PYSAT_IMPORT_ERROR}

    started = time.perf_counter()
    add_started = started
    with Solver(name=args.solver) as solver:
        for clause in iter_clauses(args):
            solver.add_clause(clause)
        add_seconds = time.perf_counter() - add_started

        solve_started = time.perf_counter()
        if args.max_conflicts > 0:
            solver.conf_budget(args.max_conflicts)
            result = solver.solve_limited()
        else:
            result = solver.solve()
        solve_seconds = time.perf_counter() - solve_started

        if result is True:
            status = "sat"
            model = solver.get_model()
        elif result is False:
            status = "unsat"
            model = None
        else:
            status = "unknown"
            model = None

    return status, model, {
        "solver": args.solver,
        "max_conflicts": args.max_conflicts,
        "add_seconds": round(add_seconds, 3),
        "solve_seconds": round(solve_seconds, 3),
        "total_seconds": round(time.perf_counter() - started, 3),
        "pysat_available": True,
        "clauses_added": info.clauses,
    }


def check_coloring_file(path: Path, r: int) -> tuple[bool, str]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    edge_colors: dict[tuple[int, int], int] = {}
    for row in rows:
        edge = tuple(row["edge"])
        if len(edge) != 2:
            return False, f"bad edge row: {row}"
        a, b = int(edge[0]), int(edge[1])
        if a > b:
            a, b = b, a
        edge_colors[(a, b)] = int(row["color"])

    edges, _ = make_edges(r * r + 1)
    try:
        colors = [edge_colors[edge] for edge in edges]
    except KeyError as exc:
        return False, f"missing edge {exc.args[0]}"
    return verify_full_coloring(r, colors)


def default_prefix(args: argparse.Namespace) -> Path:
    if args.mode == "full":
        seed = f"_seed-{args.seed}" if args.seed != "none" else ""
        return DEFAULT_RESULTS / f"sat_r{args.r}_full_sym-{args.symmetry}{seed}"
    merge = f"{args.affine_merge[0]}-{args.affine_merge[1]}"
    return DEFAULT_RESULTS / f"sat_r{args.r}_affine_extension_merge-{merge}"


def main() -> int:
    parser = argparse.ArgumentParser(description="SAT/CNF pipeline for EP617 r-coloring search.")
    parser.add_argument("--mode", choices=["full", "affine-extension"], default="full")
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--solve", action="store_true", help="solve with PySAT if available")
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--max-conflicts", type=int, default=0, help="0 means complete solve")
    parser.add_argument("--write-cnf", action="store_true", help="write a DIMACS file")
    parser.add_argument("--cnf", type=Path, default=None)
    parser.add_argument("--out-prefix", type=Path, default=None)
    parser.add_argument("--symmetry", choices=["none", "edge", "star"], default="edge")
    parser.add_argument("--seed", choices=["none", "affine"], default="none")
    parser.add_argument("--affine-merge", type=parse_pair, default=(0, 1))
    parser.add_argument("--check-coloring", type=Path, default=None)
    args = parser.parse_args()

    if args.r != 5:
        raise SystemExit("this EP617 pipeline is intended for r=5")

    out_prefix = args.out_prefix or default_prefix(args)
    out_prefix.parent.mkdir(parents=True, exist_ok=True)

    if args.check_coloring is not None:
        ok, message = check_coloring_file(args.check_coloring, args.r)
        print(json.dumps({"status": "valid" if ok else "invalid", "message": message}, indent=2))
        return 0 if ok else 1

    if args.mode == "affine-extension" or args.seed == "affine":
        seed_ok, bad_subset = validate_affine_seed(args.r, args.affine_merge)
        if not seed_ok:
            summary = {
                "status": "invalid_seed",
                "bad_subset": list(bad_subset or ()),
                "r": args.r,
                "affine_merge": list(args.affine_merge),
            }
            summary_path = out_prefix.with_suffix(".summary.json")
            summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
            print(json.dumps(summary, indent=2))
            return 2

    info = build_info(args)
    summary: dict[str, object] = {
        "status": "not_solved",
        "mode": info.mode,
        "r": info.r,
        "n": info.n,
        "variables": info.variables,
        "clauses": info.clauses,
        "edges": info.edges,
        "coverage_clauses": info.coverage_clauses,
        "exactly_one_clauses": info.exactly_one_clauses,
        "unit_clauses": info.unit_clauses,
        "symmetry": args.symmetry if args.mode == "full" else "n/a",
        "seed": args.seed if args.mode == "full" else "affine",
        "affine_merge": list(args.affine_merge),
    }

    should_write_cnf = args.write_cnf or (args.solve and Solver is None)
    if should_write_cnf:
        cnf_path = args.cnf or out_prefix.with_suffix(".cnf")
        started = time.perf_counter()
        write_dimacs(cnf_path, info, iter_clauses(args))
        summary["dimacs_path"] = str(cnf_path)
        summary["dimacs_seconds"] = round(time.perf_counter() - started, 3)
        if Solver is None and args.solve and not args.write_cnf:
            summary["dimacs_reason"] = "PySAT unavailable; wrote DIMACS fallback"

    if args.solve:
        status, model, solve_meta = solve_with_pysat(args, info)
        summary.update(solve_meta)
        summary["status"] = status
        if model is not None:
            model_path, ok, message = write_model(args, model, out_prefix)
            summary["model_path"] = str(model_path)
            summary["model_check"] = "valid" if ok else "invalid"
            summary["model_check_message"] = message

    summary_path = out_prefix.with_suffix(".summary.json")
    summary["summary_path"] = str(summary_path)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))

    if summary["status"] == "sat":
        return 10
    if summary["status"] == "unsat":
        return 20
    if summary["status"] == "unknown":
        return 30
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
