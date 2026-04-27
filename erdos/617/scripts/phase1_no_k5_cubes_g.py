from __future__ import annotations

import argparse
import itertools
import json
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pysat.card import CardEnc, EncType
from pysat.solvers import Solver


N = 26
DEFAULT_K_VALUES = (60, 61, 62, 63, 64, 65)
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results"


@dataclass(frozen=True)
class BaseCnf:
    edges: list[tuple[int, int]]
    edge_id: dict[tuple[int, int], int]
    clauses: list[list[int]]
    top_id: int
    k_selectors: dict[int, int]
    lower6_clauses: int
    no_k5_clauses: int
    exact_k_clauses: int


@dataclass(frozen=True)
class Cube:
    cube_id: int
    k: int
    pattern: str
    assumptions: tuple[int, ...]
    selected_star: tuple[int, ...]
    forbidden_star: tuple[int, ...]

    def to_json(self) -> dict[str, object]:
        return {
            "cube_id": self.cube_id,
            "k": self.k,
            "pattern": self.pattern,
            "selected_star_neighbors": list(self.selected_star),
            "forbidden_star_neighbors": list(self.forbidden_star),
            "assumptions": list(self.assumptions),
        }


def edge_list(n: int = N) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return edges, {edge: idx + 1 for idx, edge in enumerate(edges)}


def parse_int_values(text: str, lo: int, hi: int, name: str) -> tuple[int, ...]:
    values: set[int] = set()
    for raw_part in text.split(","):
        part = raw_part.strip()
        if not part:
            continue
        if ".." in part:
            left, right = part.split("..", 1)
            start, stop = int(left), int(right)
            values.update(range(start, stop + 1))
        elif "-" in part:
            left, right = part.split("-", 1)
            start, stop = int(left), int(right)
            values.update(range(start, stop + 1))
        else:
            values.add(int(part))
    if not values:
        raise argparse.ArgumentTypeError(f"{name} must not be empty")
    bad = sorted(v for v in values if v < lo or v > hi)
    if bad:
        raise argparse.ArgumentTypeError(f"{name} values out of range [{lo},{hi}]: {bad}")
    return tuple(sorted(values))


def parse_k_values(text: str) -> tuple[int, ...]:
    return parse_int_values(text, 60, 65, "k")


def parse_degree_values(text: str) -> tuple[int, ...]:
    return parse_int_values(text, 0, 25, "degree")


def build_base(k_values: Iterable[int]) -> BaseCnf:
    edges, edge_id = edge_list()
    edge_vars = list(range(1, len(edges) + 1))
    clauses: list[list[int]] = []

    lower6_clauses = 0
    for subset in itertools.combinations(range(N), 6):
        clauses.append([edge_id[(a, b)] for a, b in itertools.combinations(subset, 2)])
        lower6_clauses += 1

    no_k5_clauses = 0
    for clique in itertools.combinations(range(N), 5):
        clauses.append([-edge_id[(a, b)] for a, b in itertools.combinations(clique, 2)])
        no_k5_clauses += 1

    top_id = len(edges)
    k_selectors: dict[int, int] = {}
    exact_k_clauses = 0
    for k in k_values:
        top_id += 1
        selector = top_id
        k_selectors[k] = selector
        enc = CardEnc.equals(
            lits=edge_vars,
            bound=k,
            top_id=top_id,
            encoding=EncType.seqcounter,
        )
        for clause in enc.clauses:
            clauses.append([-selector, *clause])
        exact_k_clauses += len(enc.clauses)
        top_id = max(top_id, enc.nv)

    return BaseCnf(
        edges=edges,
        edge_id=edge_id,
        clauses=clauses,
        top_id=top_id,
        k_selectors=k_selectors,
        lower6_clauses=lower6_clauses,
        no_k5_clauses=no_k5_clauses,
        exact_k_clauses=exact_k_clauses,
    )


def low_degree_star_assumptions(
    edge_id: dict[tuple[int, int], int],
    degree: int,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    selected = tuple(range(1, degree + 1))
    forbidden = tuple(range(degree + 1, N))
    assumptions: list[int] = []
    for vertex in selected:
        assumptions.append(edge_id[(0, vertex)])
    for vertex in forbidden:
        assumptions.append(-edge_id[(0, vertex)])
    return tuple(assumptions), selected, forbidden


def star_prefix_assumptions(
    edge_id: dict[tuple[int, int], int],
    width: int,
    mask: int,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    selected: list[int] = []
    forbidden: list[int] = []
    assumptions: list[int] = []
    for offset, vertex in enumerate(range(1, width + 1)):
        lit = edge_id[(0, vertex)]
        if mask & (1 << offset):
            selected.append(vertex)
            assumptions.append(lit)
        else:
            forbidden.append(vertex)
            assumptions.append(-lit)
    return tuple(assumptions), tuple(selected), tuple(forbidden)


def make_cubes(args: argparse.Namespace, base: BaseCnf) -> tuple[list[Cube], int]:
    cubes: list[Cube] = []

    if args.pattern_mode == "lowdeg-star":
        pattern_items = list(args.degrees)
    elif args.pattern_mode == "star-prefix":
        if args.star_width < 1 or args.star_width > 25:
            raise SystemExit("--star-width must be in [1,25]")
        pattern_items = list(range(1 << args.star_width))
    else:
        raise SystemExit(f"unknown pattern mode: {args.pattern_mode}")

    cube_id = 0
    for k in args.k_values:
        for item in pattern_items:
            if args.pattern_mode == "lowdeg-star":
                assumptions, selected, forbidden = low_degree_star_assumptions(base.edge_id, item)
                pattern = f"lowdeg-star:deg={item}"
            else:
                assumptions, selected, forbidden = star_prefix_assumptions(base.edge_id, args.star_width, item)
                bits = "".join("1" if item & (1 << offset) else "0" for offset in range(args.star_width))
                pattern = f"star-prefix:w={args.star_width}:bits={bits}"
            cubes.append(
                Cube(
                    cube_id=cube_id,
                    k=k,
                    pattern=pattern,
                    assumptions=(base.k_selectors[k], *assumptions),
                    selected_star=selected,
                    forbidden_star=forbidden,
                )
            )
            cube_id += 1

    total = len(cubes)
    selected_cubes = cubes[args.offset :]
    if args.max_cubes > 0:
        selected_cubes = selected_cubes[: args.max_cubes]
    return selected_cubes, total


def status_name(result: bool | None) -> str:
    if result is True:
        return "sat"
    if result is False:
        return "unsat"
    return "unknown"


def stats_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    keys = sorted(set(before) | set(after))
    return {key: int(after.get(key, 0) - before.get(key, 0)) for key in keys}


def clear_interrupt_if_supported(solver: Solver) -> None:
    if not hasattr(solver, "clear_interrupt"):
        return
    try:
        solver.clear_interrupt()
    except NotImplementedError:
        return


def upper6_violations(
    edge_id: dict[tuple[int, int], int],
    chosen: set[int],
    max_violations: int,
) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for subset in itertools.combinations(range(N), 6):
        count = 0
        for a, b in itertools.combinations(subset, 2):
            if edge_id[(a, b)] in chosen:
                count += 1
                if count > 11:
                    out.append(subset)
                    break
        if len(out) >= max_violations:
            break
    return out


def add_upper6_cardinality_cut(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    subset: tuple[int, ...],
    top_id: int,
) -> tuple[int, int]:
    lits = [edge_id[(a, b)] for a, b in itertools.combinations(subset, 2)]
    enc = CardEnc.atmost(lits=lits, bound=11, top_id=top_id, encoding=EncType.seqcounter)
    for clause in enc.clauses:
        solver.add_clause(clause)
    return len(enc.clauses), max(top_id, enc.nv)


def verify_model(
    edge_id: dict[tuple[int, int], int],
    chosen: set[int],
    k: int,
    cube: Cube,
) -> tuple[bool, str]:
    if len(chosen) != k:
        return False, f"edge count is {len(chosen)}, expected {k}"
    for subset in itertools.combinations(range(N), 6):
        count = sum(1 for a, b in itertools.combinations(subset, 2) if edge_id[(a, b)] in chosen)
        if count < 1 or count > 11:
            return False, f"6-set {subset} has {count} selected edges"
    for clique in itertools.combinations(range(N), 5):
        if all(edge_id[(a, b)] in chosen for a, b in itertools.combinations(clique, 2)):
            return False, f"K5 found on {clique}"
    for lit in cube.assumptions[1:]:
        if lit > 0 and lit not in chosen:
            return False, f"missing assumed edge var {lit}"
        if lit < 0 and -lit in chosen:
            return False, f"forbidden assumed edge var {-lit} is selected"
    return True, "ok"


def write_model(
    path: Path,
    edges: list[tuple[int, int]],
    chosen: set[int],
) -> None:
    rows = [
        {"edge": list(edge), "selected": (idx + 1) in chosen}
        for idx, edge in enumerate(edges)
    ]
    path.write_text(json.dumps(rows, indent=2), encoding="utf-8")


def solve_one_cube(
    solver: Solver,
    base: BaseCnf,
    cube: Cube,
    args: argparse.Namespace,
    state: dict[str, int],
    out_prefix: Path,
) -> dict[str, object]:
    started = time.perf_counter()
    deadline = started + args.max_seconds if args.max_seconds > 0 else None
    interrupted_by_wall_clock = False
    solve_calls = 0
    lazy_rounds = 0
    lazy_clauses = 0
    model_path: str | None = None
    model_check: str | None = None
    model_check_message: str | None = None
    result: bool | None = None

    before_stats = solver.accum_stats()

    while True:
        if deadline is not None:
            remaining = deadline - time.perf_counter()
            if remaining <= 0:
                interrupted_by_wall_clock = True
                result = None
                break
        else:
            remaining = 0.0

        def interrupt_solver() -> None:
            nonlocal interrupted_by_wall_clock
            interrupted_by_wall_clock = True
            try:
                solver.interrupt()
            except NotImplementedError:
                return

        timer: threading.Timer | None = None
        if deadline is not None:
            clear_interrupt_if_supported(solver)
            timer = threading.Timer(remaining, interrupt_solver)
            timer.daemon = True
            timer.start()
        if args.conf_budget > 0:
            solver.conf_budget(args.conf_budget)
        try:
            try:
                if args.conf_budget > 0 or deadline is not None:
                    result = solver.solve_limited(
                        assumptions=list(cube.assumptions),
                        expect_interrupt=True,
                    )
                else:
                    result = solver.solve(assumptions=list(cube.assumptions))
            except NotImplementedError as exc:
                raise RuntimeError(
                    f"solver {args.solver!r} does not support PySAT limited solve; "
                    "use glucose4 or minisat22 for wall-clock cubes"
                ) from exc
        finally:
            if timer is not None:
                timer.cancel()
            clear_interrupt_if_supported(solver)
        solve_calls += 1

        if result is not True:
            break

        model = solver.get_model()
        chosen = {lit for lit in model if 1 <= lit <= len(base.edges)}
        violations = upper6_violations(base.edge_id, chosen, args.max_violations_per_round)
        if not violations:
            ok, message = verify_model(base.edge_id, chosen, cube.k, cube)
            model_check = "valid" if ok else "invalid"
            model_check_message = message
            model_file = out_prefix.with_suffix(f".cube{cube.cube_id}.model.json")
            write_model(model_file, base.edges, chosen)
            model_path = str(model_file)
            break

        lazy_rounds += 1
        for subset in violations:
            added, state["top_id"] = add_upper6_cardinality_cut(
                solver,
                base.edge_id,
                subset,
                state["top_id"],
            )
            lazy_clauses += added
            state["global_lazy_upper6_clauses"] += added
        state["global_lazy_upper6_sets"] += len(violations)

        if lazy_rounds >= args.max_lazy_rounds:
            result = None
            break

    after_stats = solver.accum_stats()
    row = cube.to_json()
    row.update(
        {
            "status": status_name(result),
            "solve_calls": solve_calls,
            "solve_seconds": round(time.perf_counter() - started, 3),
            "interrupted_by_wall_clock": interrupted_by_wall_clock,
            "lazy_rounds": lazy_rounds,
            "lazy_upper6_clauses": lazy_clauses,
            "global_lazy_upper6_sets_after": state["global_lazy_upper6_sets"],
            "global_lazy_upper6_clauses_after": state["global_lazy_upper6_clauses"],
            "stats_delta": stats_delta(before_stats, after_stats),
        }
    )
    if model_path is not None:
        row["model_path"] = model_path
        row["model_check"] = model_check
        row["model_check_message"] = model_check_message
    return row


def default_out_prefix(args: argparse.Namespace) -> Path:
    k_part = f"k{min(args.k_values)}_{max(args.k_values)}" if len(args.k_values) > 1 else f"k{args.k_values[0]}"
    if args.pattern_mode == "lowdeg-star":
        pat = f"lowdeg_{min(args.degrees)}_{max(args.degrees)}"
    else:
        pat = f"prefix_w{args.star_width}"
    suffix = f"phase1_g_no_k5_{k_part}_{pat}_{args.solver}_b{args.conf_budget}_s{args.max_seconds:g}"
    if args.max_cubes > 0:
        suffix += f"_max{args.max_cubes}"
    if args.offset:
        suffix += f"_off{args.offset}"
    return DEFAULT_RESULTS / suffix


def solve_cubes(args: argparse.Namespace) -> dict[str, object]:
    base_started = time.perf_counter()
    base = build_base(args.k_values)
    base_seconds = time.perf_counter() - base_started
    cubes, total_cubes = make_cubes(args, base)
    out_prefix = args.out_prefix or default_out_prefix(args)
    out_prefix.parent.mkdir(parents=True, exist_ok=True)
    rows_path = out_prefix.with_suffix(".cubes.jsonl")

    rows: list[dict[str, object]] = []
    state = {
        "top_id": base.top_id,
        "global_lazy_upper6_sets": 0,
        "global_lazy_upper6_clauses": 0,
    }
    started = time.perf_counter()

    with Solver(name=args.solver, bootstrap_with=base.clauses) as solver:
        add_seconds = time.perf_counter() - started
        with rows_path.open("w", encoding="utf-8", newline="\n") as handle:
            for cube in cubes:
                row = solve_one_cube(solver, base, cube, args, state, out_prefix)
                rows.append(row)
                handle.write(json.dumps(row, sort_keys=True))
                handle.write("\n")
                handle.flush()
                print(
                    json.dumps(
                        {
                            "cube_id": row["cube_id"],
                            "k": row["k"],
                            "pattern": row["pattern"],
                            "status": row["status"],
                            "solve_seconds": row["solve_seconds"],
                            "lazy_rounds": row["lazy_rounds"],
                            "interrupted_by_wall_clock": row["interrupted_by_wall_clock"],
                        }
                    ),
                    flush=True,
                )
                if row["status"] == "sat" and args.stop_on_sat:
                    break

    counts = {"sat": 0, "unsat": 0, "unknown": 0}
    for row in rows:
        counts[str(row["status"])] += 1

    summary = {
        "status": "sat_found"
        if counts["sat"]
        else ("all_unsat" if rows and counts["unsat"] == len(rows) else "incomplete"),
        "agent": "G",
        "branch": "phase1_no_k5_minimum_colour",
        "n": N,
        "cube_design": {
            "exact_edge_count_k": list(args.k_values),
            "pattern_mode": args.pattern_mode,
            "degrees": list(args.degrees) if args.pattern_mode == "lowdeg-star" else None,
            "star_width": args.star_width if args.pattern_mode == "star-prefix" else None,
            "lowdeg_star_wlog": args.pattern_mode == "lowdeg-star"
            and max(args.k_values) <= 65
            and set(args.degrees).issuperset(set(range(0, 6))),
            "constraints": [
                "alpha(G) <= 5 via every 6-set has at least one selected edge",
                "omega(G) <= 4 via no selected K5",
                "exact edge count k activated by PySAT selector assumptions",
                "every 6-set has at most 11 selected edges, added lazily from SAT candidates",
            ],
        },
        "variables_initial": base.top_id,
        "variables_after_lazy": state["top_id"],
        "clauses_initial": len(base.clauses),
        "lower6_clauses": base.lower6_clauses,
        "no_k5_clauses": base.no_k5_clauses,
        "guarded_exact_k_clauses": base.exact_k_clauses,
        "global_lazy_upper6_sets": state["global_lazy_upper6_sets"],
        "global_lazy_upper6_clauses": state["global_lazy_upper6_clauses"],
        "total_cubes": total_cubes,
        "completed_cubes": len(rows),
        "offset": args.offset,
        "max_cubes": args.max_cubes,
        "counts": counts,
        "solver": args.solver,
        "conf_budget_per_solve_call": args.conf_budget,
        "max_seconds_per_cube": args.max_seconds,
        "max_lazy_rounds_per_cube": args.max_lazy_rounds,
        "max_violations_per_round": args.max_violations_per_round,
        "base_build_seconds": round(base_seconds, 3),
        "solver_bootstrap_seconds": round(add_seconds, 3),
        "total_seconds": round(time.perf_counter() - started, 3),
        "rows_path": str(rows_path),
        "hard_cubes": [
            {
                "cube_id": row["cube_id"],
                "k": row["k"],
                "pattern": row["pattern"],
                "solve_seconds": row["solve_seconds"],
                "lazy_rounds": row["lazy_rounds"],
            }
            for row in rows
            if row["status"] == "unknown"
        ],
        "rows": rows,
    }
    summary_path = out_prefix.with_suffix(".summary.json")
    summary["summary_path"] = str(summary_path)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Agent G cubes for the EP617 no-K5 minimum-colour branch."
    )
    parser.add_argument("--k-values", type=parse_k_values, default=DEFAULT_K_VALUES)
    parser.add_argument("--pattern-mode", choices=["lowdeg-star", "star-prefix"], default="lowdeg-star")
    parser.add_argument("--degrees", type=parse_degree_values, default=(0, 1, 2, 3, 4, 5))
    parser.add_argument("--star-width", type=int, default=6)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--conf-budget", type=int, default=0)
    parser.add_argument("--max-seconds", type=float, default=10.0)
    parser.add_argument("--max-lazy-rounds", type=int, default=20)
    parser.add_argument("--max-violations-per-round", type=int, default=100)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--max-cubes", type=int, default=0)
    parser.add_argument("--stop-on-sat", action="store_true")
    parser.add_argument("--out-prefix", type=Path, default=None)
    args = parser.parse_args()

    if args.offset < 0:
        raise SystemExit("--offset must be nonnegative")
    if args.conf_budget < 0:
        raise SystemExit("--conf-budget must be nonnegative")
    if args.max_seconds < 0:
        raise SystemExit("--max-seconds must be nonnegative")

    summary = solve_cubes(args)
    if summary["status"] == "sat_found":
        return 10
    if summary["status"] == "all_unsat":
        return 20
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
