from __future__ import annotations

import argparse
import itertools
import json
import math
import threading
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results"
DEFAULT_N = 26


ENCODINGS = {
    "seqcounter": EncType.seqcounter,
    "sortnetwrk": EncType.sortnetwrk,
    "cardnetwrk": EncType.cardnetwrk,
    "totalizer": EncType.totalizer,
    "mtotalizer": EncType.mtotalizer,
    "kmtotalizer": EncType.kmtotalizer,
}


def edge_list(n: int) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return edges, {edge: idx + 1 for idx, edge in enumerate(edges)}


def edge_var(edge_id: dict[tuple[int, int], int], a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    return edge_id[(a, b)]


def parse_int_list(text: str) -> list[int]:
    try:
        values = [int(part.strip()) for part in text.split(",") if part.strip() != ""]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected a comma-separated integer list") from exc
    if not values:
        raise argparse.ArgumentTypeError("list must not be empty")
    return values


def status_name(result: bool | None) -> str:
    if result is True:
        return "sat"
    if result is False:
        return "unsat"
    return "unknown"


def stats_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    keys = sorted(set(before) | set(after))
    return {key: int(after.get(key, 0) - before.get(key, 0)) for key in keys}


def safe_accum_stats(solver: Solver) -> dict[str, int]:
    try:
        return solver.accum_stats()
    except NotImplementedError:
        return {}


def turan_edges(vertex_count: int, parts: int) -> int:
    if vertex_count <= 1:
        return 0
    q, r = divmod(vertex_count, parts)
    sizes = [q + 1] * r + [q] * (parts - r)
    return (vertex_count * vertex_count - sum(size * size for size in sizes)) // 2


def min_edges_with_alpha_at_most(vertex_count: int, alpha: int) -> int:
    """Minimum edges in an m-vertex graph with independence number <= alpha."""
    if vertex_count <= alpha:
        return 0
    return math.comb(vertex_count, 2) - turan_edges(vertex_count, alpha)


def literal_value(lit: int, fixed: dict[int, bool]) -> bool | None:
    value = fixed.get(abs(lit))
    if value is None:
        return None
    return value if lit > 0 else not value


@dataclass
class BuildResult:
    cnf: CNF
    edges: list[tuple[int, int]]
    edge_id: dict[tuple[int, int], int]
    fixed: dict[int, bool]
    top_id: int
    counts: dict[str, int]
    aux_counts: dict[str, int]
    build_seconds: float


class CnfBuilder:
    def __init__(self, n: int, encoding: int):
        self.n = n
        self.edges, self.edge_id = edge_list(n)
        self.edge_count = len(self.edges)
        self.encoding = encoding
        self.cnf = CNF()
        self.top_id = self.edge_count
        self.fixed: dict[int, bool] = {}
        self.counts: Counter[str] = Counter()
        self.aux_counts: Counter[str] = Counter()

    def add_clause(self, clause: Iterable[int], category: str) -> None:
        reduced: list[int] = []
        seen: set[int] = set()
        for lit in clause:
            value = literal_value(lit, self.fixed)
            if value is True:
                return
            if value is False:
                continue
            if -lit in seen:
                return
            if lit not in seen:
                reduced.append(lit)
                seen.add(lit)
        self.cnf.append(reduced)
        self.counts[category] += 1

    def fix_lit(self, lit: int, category: str = "symmetry_units") -> None:
        var = abs(lit)
        value = lit > 0
        old = self.fixed.get(var)
        if old is not None:
            if old != value:
                self.cnf.append([])
                self.counts[f"{category}_conflict"] += 1
            return
        self.fixed[var] = value
        self.cnf.append([lit])
        self.counts[category] += 1

    def _reduce_cardinality(self, lits: Iterable[int], bound: int) -> tuple[list[int], int]:
        remaining: list[int] = []
        true_count = 0
        for lit in lits:
            value = literal_value(lit, self.fixed)
            if value is True:
                true_count += 1
            elif value is None:
                remaining.append(lit)
        return remaining, bound - true_count

    def add_atmost(self, lits: Iterable[int], bound: int, category: str) -> None:
        remaining, reduced_bound = self._reduce_cardinality(lits, bound)
        if reduced_bound < 0:
            self.cnf.append([])
            self.counts[f"{category}_contradiction"] += 1
            return
        if reduced_bound >= len(remaining):
            return
        enc = CardEnc.atmost(
            lits=remaining,
            bound=reduced_bound,
            top_id=self.top_id,
            encoding=self.encoding,
        )
        self.cnf.extend(enc.clauses)
        self.counts[category] += len(enc.clauses)
        new_top = max(self.top_id, enc.nv)
        self.aux_counts[category] += new_top - self.top_id
        self.top_id = new_top

    def add_atleast(self, lits: Iterable[int], bound: int, category: str) -> None:
        remaining, reduced_bound = self._reduce_cardinality(lits, bound)
        if reduced_bound <= 0:
            return
        if reduced_bound > len(remaining):
            self.cnf.append([])
            self.counts[f"{category}_contradiction"] += 1
            return
        enc = CardEnc.atleast(
            lits=remaining,
            bound=reduced_bound,
            top_id=self.top_id,
            encoding=self.encoding,
        )
        self.cnf.extend(enc.clauses)
        self.counts[category] += len(enc.clauses)
        new_top = max(self.top_id, enc.nv)
        self.aux_counts[category] += new_top - self.top_id
        self.top_id = new_top

    def finish(self) -> CNF:
        self.cnf.nv = max(self.cnf.nv, self.top_id)
        return self.cnf


def add_degree0_prefix_units(builder: CnfBuilder, degree0: int) -> None:
    for v in range(1, builder.n):
        lit = edge_var(builder.edge_id, 0, v)
        builder.fix_lit(lit if v <= degree0 else -lit)


def all_edge_vars(edges: list[tuple[int, int]]) -> list[int]:
    return list(range(1, len(edges) + 1))


def subset_edge_vars(edge_id: dict[tuple[int, int], int], vertices: tuple[int, ...]) -> list[int]:
    return [edge_id[(a, b)] for a, b in itertools.combinations(vertices, 2)]


def incident_edge_vars(edge_id: dict[tuple[int, int], int], n: int, vertex: int) -> list[int]:
    return [edge_var(edge_id, vertex, other) for other in range(n) if other != vertex]


def add_lower6(builder: CnfBuilder) -> None:
    for subset in itertools.combinations(range(builder.n), 6):
        builder.add_clause(subset_edge_vars(builder.edge_id, subset), "lower6_alpha_le_5")


def add_no_k5(builder: CnfBuilder) -> None:
    for subset in itertools.combinations(range(builder.n), 5):
        builder.add_clause(
            [-var for var in subset_edge_vars(builder.edge_id, subset)],
            "no_k5_omega_le_4",
        )


def add_upper6_cards(builder: CnfBuilder, only_with_zero: bool = False) -> None:
    if only_with_zero:
        subsets = ((0, *rest) for rest in itertools.combinations(range(1, builder.n), 5))
        category = "upper6_zero_card"
    else:
        subsets = itertools.combinations(range(builder.n), 6)
        category = "upper6_card"
    for subset in subsets:
        builder.add_atmost(subset_edge_vars(builder.edge_id, tuple(subset)), 11, category)


def add_global_edge_count(
    builder: CnfBuilder,
    min_edges: int,
    max_edges: int,
) -> None:
    lits = all_edge_vars(builder.edges)
    builder.add_atleast(lits, min_edges, "global_edges_atleast")
    builder.add_atmost(lits, max_edges, "global_edges_atmost")


def add_min_degree_break(builder: CnfBuilder, degree0: int) -> None:
    for vertex in range(1, builder.n):
        builder.add_atleast(
            incident_edge_vars(builder.edge_id, builder.n, vertex),
            degree0,
            "min_degree_order",
        )


def add_degree_caps_from_edge_budget(builder: CnfBuilder, degree0: int, max_edges: int) -> None:
    # If vertex 0 is a minimum-degree vertex of degree d, then every other
    # vertex has degree at most 2e - (n-1)d. This is often redundant, but it
    # exposes the 5-regular branch when d=5 and e=65.
    upper = 2 * max_edges - (builder.n - 1) * degree0
    if upper >= builder.n - 1:
        return
    for vertex in range(1, builder.n):
        builder.add_atmost(
            incident_edge_vars(builder.edge_id, builder.n, vertex),
            upper,
            "degree_cap_from_edge_budget",
        )


def add_nonneighbor_turan_cut(builder: CnfBuilder, degree0: int) -> None:
    nonneighbors = tuple(range(degree0 + 1, builder.n))
    lower = min_edges_with_alpha_at_most(len(nonneighbors), 4)
    if lower <= 0:
        return
    builder.add_atleast(
        subset_edge_vars(builder.edge_id, nonneighbors),
        lower,
        "nonnbr_alpha4_turan",
    )


def branch_precheck(n: int, degree0: int | None, max_edges: int) -> str | None:
    if degree0 is None:
        return None
    if degree0 > (2 * max_edges) // n:
        return f"minimum degree {degree0} forces more than {max_edges} edges by averaging"
    nonneighbors = n - 1 - degree0
    nonneighbor_lower = min_edges_with_alpha_at_most(nonneighbors, 4)
    forced_lower = degree0 + nonneighbor_lower
    if forced_lower > max_edges:
        return (
            f"degree0={degree0} has {nonneighbors} fixed nonneighbors; "
            f"alpha<=5 forces at least {nonneighbor_lower} edges among them, "
            f"so e(G)>={forced_lower}>{max_edges}"
        )
    return None


def build_cnf(
    args: argparse.Namespace,
    degree0: int | None,
    edge_count: int | None,
) -> BuildResult:
    started = time.perf_counter()
    builder = CnfBuilder(args.n, ENCODINGS[args.card_encoding])
    if degree0 is not None:
        add_degree0_prefix_units(builder, degree0)

    add_lower6(builder)
    add_no_k5(builder)

    if args.upper6_mode == "eager-card":
        add_upper6_cards(builder, only_with_zero=False)
    elif args.upper6_mode == "lazy-card" and args.eager_zero_upper and degree0 is not None:
        add_upper6_cards(builder, only_with_zero=True)

    min_edges = edge_count if edge_count is not None else args.min_edges
    max_edges = edge_count if edge_count is not None else args.max_edges
    add_global_edge_count(builder, min_edges, max_edges)

    if degree0 is not None and args.min_degree_break:
        add_min_degree_break(builder, degree0)
    if degree0 is not None and args.degree_caps:
        add_degree_caps_from_edge_budget(builder, degree0, max_edges)
    if degree0 is not None and args.nonneighbor_turan:
        add_nonneighbor_turan_cut(builder, degree0)

    cnf = builder.finish()
    return BuildResult(
        cnf=cnf,
        edges=builder.edges,
        edge_id=builder.edge_id,
        fixed=builder.fixed,
        top_id=builder.top_id,
        counts=dict(sorted(builder.counts.items())),
        aux_counts=dict(sorted(builder.aux_counts.items())),
        build_seconds=time.perf_counter() - started,
    )


def solve_limited_with_interrupt(
    solver: Solver,
    max_seconds: float,
    conf_budget: int,
    prop_budget: int,
) -> tuple[bool | None, bool, float, str | None]:
    interrupted_by_wall_clock = False
    unsupported: str | None = None

    def interrupt_solver() -> None:
        nonlocal interrupted_by_wall_clock, unsupported
        interrupted_by_wall_clock = True
        try:
            solver.interrupt()
        except NotImplementedError as exc:
            unsupported = str(exc)

    timer: threading.Timer | None = None
    if max_seconds > 0:
        if hasattr(solver, "clear_interrupt"):
            try:
                solver.clear_interrupt()
            except NotImplementedError as exc:
                return None, False, 0.0, str(exc)
        timer = threading.Timer(max_seconds, interrupt_solver)
        timer.daemon = True
        timer.start()
    if conf_budget > 0:
        solver.conf_budget(conf_budget)
    if prop_budget > 0:
        solver.prop_budget(prop_budget)

    started = time.perf_counter()
    try:
        if max_seconds > 0 or conf_budget > 0 or prop_budget > 0:
            try:
                result = solver.solve_limited(expect_interrupt=True)
            except NotImplementedError as exc:
                unsupported = str(exc)
                result = None
        else:
            result = solver.solve()
    finally:
        if timer is not None:
            timer.cancel()
        if hasattr(solver, "clear_interrupt"):
            try:
                solver.clear_interrupt()
            except NotImplementedError as exc:
                unsupported = unsupported or str(exc)
    return result, interrupted_by_wall_clock, time.perf_counter() - started, unsupported


def chosen_edges_from_model(model: list[int], edge_count: int) -> set[int]:
    return {lit for lit in model if 1 <= lit <= edge_count}


def upper6_violations(
    edge_id: dict[tuple[int, int], int],
    chosen: set[int],
    n: int,
    max_violations: int,
    already_added: set[tuple[int, ...]],
) -> list[tuple[int, ...]]:
    violations: list[tuple[int, ...]] = []
    for subset in itertools.combinations(range(n), 6):
        if subset in already_added:
            continue
        count = 0
        for a, b in itertools.combinations(subset, 2):
            if edge_id[(a, b)] in chosen:
                count += 1
                if count > 11:
                    violations.append(subset)
                    break
        if len(violations) >= max_violations:
            break
    return violations


def add_lazy_upper6_card(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    fixed: dict[int, bool],
    subset: tuple[int, ...],
    top_id: int,
    encoding: int,
) -> tuple[int, int]:
    remaining: list[int] = []
    true_count = 0
    for var in subset_edge_vars(edge_id, subset):
        value = fixed.get(var)
        if value is True:
            true_count += 1
        elif value is None:
            remaining.append(var)
    bound = 11 - true_count
    if bound < 0:
        solver.add_clause([])
        return 1, top_id
    if bound >= len(remaining):
        return 0, top_id
    enc = CardEnc.atmost(lits=remaining, bound=bound, top_id=top_id, encoding=encoding)
    for clause in enc.clauses:
        solver.add_clause(clause)
    return len(enc.clauses), max(top_id, enc.nv)


def verify_model(
    edges: list[tuple[int, int]],
    chosen: set[int],
    n: int,
    min_edges: int,
    max_edges: int,
) -> tuple[bool, str]:
    edge_id = {edge: idx + 1 for idx, edge in enumerate(edges)}
    if not min_edges <= len(chosen) <= max_edges:
        return False, f"edge count {len(chosen)} outside [{min_edges},{max_edges}]"
    for subset in itertools.combinations(range(n), 6):
        count = sum(1 for a, b in itertools.combinations(subset, 2) if edge_id[(a, b)] in chosen)
        if count < 1 or count > 11:
            return False, f"6-set {subset} has {count} edges"
    for subset in itertools.combinations(range(n), 5):
        if all(edge_id[(a, b)] in chosen for a, b in itertools.combinations(subset, 2)):
            return False, f"K5 on {subset}"
    return True, "ok"


def model_path_for(out: Path, degree0: int | None, edge_count: int | None) -> Path:
    parts = [out.stem]
    parts.append("dall" if degree0 is None else f"d{degree0}")
    parts.append("erange" if edge_count is None else f"e{edge_count}")
    return out.with_name(".".join(parts) + ".model.json")


def write_model(path: Path, edges: list[tuple[int, int]], chosen: set[int]) -> None:
    rows = [list(edges[var - 1]) for var in sorted(chosen)]
    path.write_text(json.dumps(rows, indent=2), encoding="utf-8")


def solve_branch(
    args: argparse.Namespace,
    degree0: int | None,
    edge_count: int | None,
    out: Path,
) -> dict[str, object]:
    max_edges = edge_count if edge_count is not None else args.max_edges
    min_edges = edge_count if edge_count is not None else args.min_edges
    precheck = branch_precheck(args.n, degree0, max_edges) if args.precheck else None
    if precheck is not None:
        return {
            "degree0": degree0,
            "edge_count": edge_count,
            "status": "unsat",
            "precheck": precheck,
            "solver": "not_run",
        }

    built = build_cnf(args, degree0, edge_count)
    branch_started = time.perf_counter()
    lazy_added: set[tuple[int, ...]] = set()
    if args.upper6_mode == "lazy-card" and args.eager_zero_upper and degree0 is not None:
        lazy_added.update((0, *rest) for rest in itertools.combinations(range(1, args.n), 5))

    lazy_rounds = 0
    lazy_clauses = 0
    solve_calls = 0
    wall_interrupts = 0
    solve_seconds = 0.0
    limited_unknowns = 0
    unsupported_limited_solve: str | None = None
    model: list[int] | None = None
    current_top = built.top_id

    with Solver(name=args.solver, bootstrap_with=built.cnf.clauses) as solver:
        before_stats = safe_accum_stats(solver)
        while True:
            remaining_total = args.max_total_seconds - (time.perf_counter() - branch_started)
            if args.max_total_seconds > 0 and remaining_total <= 0:
                result = None
                break
            solve_limit = args.max_seconds
            if args.max_total_seconds > 0:
                solve_limit = min(solve_limit, remaining_total) if solve_limit > 0 else remaining_total

            result, interrupted, seconds, unsupported = solve_limited_with_interrupt(
                solver,
                solve_limit,
                args.conf_budget,
                args.prop_budget,
            )
            unsupported_limited_solve = unsupported_limited_solve or unsupported
            solve_calls += 1
            solve_seconds += seconds
            wall_interrupts += int(interrupted)
            if (
                result is None
                and not interrupted
                and (args.conf_budget > 0 or args.prop_budget > 0)
                and limited_unknowns + 1 < args.max_solve_attempts
            ):
                limited_unknowns += 1
                continue
            if result is not True:
                break

            limited_unknowns = 0
            model = solver.get_model()
            chosen = chosen_edges_from_model(model, len(built.edges))
            if args.upper6_mode != "lazy-card":
                break

            violations = upper6_violations(
                built.edge_id,
                chosen,
                args.n,
                args.max_violations_per_round,
                lazy_added,
            )
            if not violations:
                break
            lazy_rounds += 1
            for subset in violations:
                added, current_top = add_lazy_upper6_card(
                    solver,
                    built.edge_id,
                    built.fixed,
                    subset,
                    current_top,
                    ENCODINGS[args.card_encoding],
                )
                lazy_clauses += added
                lazy_added.add(subset)
            print(
                json.dumps(
                    {
                        "degree0": degree0,
                        "edge_count": edge_count,
                        "lazy_round": lazy_rounds,
                        "violations": len(violations),
                        "lazy_clauses": lazy_clauses,
                        "edge_model_count": len(chosen),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            if lazy_rounds >= args.max_lazy_rounds:
                result = None
                model = None
                break
        after_stats = safe_accum_stats(solver)

    status = status_name(result)
    row: dict[str, object] = {
        "degree0": degree0,
        "edge_count": edge_count,
        "status": status,
        "n": args.n,
        "min_edges": min_edges,
        "max_edges": max_edges,
        "upper6_mode": args.upper6_mode,
        "eager_zero_upper": args.eager_zero_upper,
        "min_degree_break": args.min_degree_break,
        "degree_caps": args.degree_caps,
        "nonneighbor_turan": args.nonneighbor_turan,
        "card_encoding": args.card_encoding,
        "vars": built.cnf.nv,
        "vars_after_lazy": current_top,
        "clauses": len(built.cnf.clauses),
        "constraint_counts": built.counts,
        "aux_counts": built.aux_counts,
        "build_seconds": round(built.build_seconds, 3),
        "solve_seconds": round(solve_seconds, 3),
        "branch_seconds": round(time.perf_counter() - branch_started, 3),
        "solve_calls": solve_calls,
        "limited_unknowns": limited_unknowns,
        "unsupported_limited_solve": unsupported_limited_solve,
        "lazy_rounds": lazy_rounds,
        "lazy_clauses": lazy_clauses,
        "lazy_upper6_sets": len(lazy_added),
        "wall_interrupts": wall_interrupts,
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "prop_budget": args.prop_budget,
        "max_seconds": args.max_seconds,
        "max_total_seconds": args.max_total_seconds,
        "stats_delta": stats_delta(before_stats, after_stats),
    }

    if result is True and model is not None:
        chosen = chosen_edges_from_model(model, len(built.edges))
        ok, message = verify_model(built.edges, chosen, args.n, min_edges, max_edges)
        path = model_path_for(out, degree0, edge_count)
        write_model(path, built.edges, chosen)
        row.update(
            {
                "edge_model_count": len(chosen),
                "model_path": str(path),
                "model_check": "valid" if ok else "invalid",
                "model_check_message": message,
            }
        )
    return row


def branch_specs(args: argparse.Namespace) -> list[tuple[int | None, int | None]]:
    if not args.triage:
        return [(args.degree0, args.edge_count)]
    degrees: list[int | None] = list(args.degrees)
    if args.include_unsymmetrized:
        degrees.append(None)
    if args.split_edges:
        edge_counts: list[int | None] = list(range(args.min_edges, args.max_edges + 1))
    else:
        edge_counts = [None]
    return [(degree, edge_count) for degree in degrees for edge_count in edge_counts]


def summarize_rows(rows: list[dict[str, object]]) -> dict[str, int]:
    counts = {"sat": 0, "unsat": 0, "unknown": 0}
    for row in rows:
        counts[str(row["status"])] += 1
    return counts


def run(args: argparse.Namespace) -> int:
    out = args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    jsonl_path = out.with_suffix(".jsonl")

    with jsonl_path.open("w", encoding="utf-8", newline="\n") as handle:
        for degree0, edge_count in branch_specs(args):
            row = solve_branch(args, degree0, edge_count, out)
            rows.append(row)
            handle.write(json.dumps(row, sort_keys=True))
            handle.write("\n")
            handle.flush()
            print(
                json.dumps(
                    {
                        "degree0": degree0,
                        "edge_count": edge_count,
                        "status": row["status"],
                        "build_seconds": row.get("build_seconds"),
                        "solve_seconds": row.get("solve_seconds"),
                        "lazy_rounds": row.get("lazy_rounds"),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            if row["status"] == "sat" and args.stop_on_sat:
                break

    counts = summarize_rows(rows)
    if counts["sat"]:
        overall = "sat"
    elif counts["unknown"]:
        overall = "unknown"
    else:
        overall = "unsat"

    summary = {
        "overall_status": overall,
        "counts": counts,
        "branches_requested": len(branch_specs(args)),
        "branches_run": len(rows),
        "rows_path": str(jsonl_path),
        "args": {
            "n": args.n,
            "min_edges": args.min_edges,
            "max_edges": args.max_edges,
            "degree0": args.degree0,
            "edge_count": args.edge_count,
            "triage": args.triage,
            "degrees": list(args.degrees),
            "split_edges": args.split_edges,
            "upper6_mode": args.upper6_mode,
            "eager_zero_upper": args.eager_zero_upper,
            "min_degree_break": args.min_degree_break,
            "degree_caps": args.degree_caps,
            "nonneighbor_turan": args.nonneighbor_turan,
            "card_encoding": args.card_encoding,
            "solver": args.solver,
            "conf_budget": args.conf_budget,
            "prop_budget": args.prop_budget,
            "max_seconds": args.max_seconds,
            "max_total_seconds": args.max_total_seconds,
            "max_lazy_rounds": args.max_lazy_rounds,
            "max_violations_per_round": args.max_violations_per_round,
            "max_solve_attempts": args.max_solve_attempts,
        },
        "rows": rows,
    }
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    if overall == "sat":
        return 10
    if overall == "unknown":
        return 20
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "EP617 Phase 1 Agent A: SAT test for a 26-vertex graph with "
            "60<=e<=65, every 6-set has 1..11 edges, and omega<=4."
        )
    )
    parser.add_argument("--n", type=int, default=DEFAULT_N)
    parser.add_argument("--min-edges", type=int, default=60)
    parser.add_argument("--max-edges", type=int, default=65)
    parser.add_argument("--edge-count", type=int, default=None, help="solve one exact edge count")
    parser.add_argument(
        "--degree0",
        type=int,
        default=None,
        help="symmetry branch: vertex 0 has this exact minimum degree and N(0)={1..d}",
    )
    parser.add_argument("--triage", action="store_true", help="run all requested degree/edge branches")
    parser.add_argument("--degrees", type=parse_int_list, default=parse_int_list("0,1,2,3,4,5"))
    parser.add_argument("--split-edges", action="store_true", help="triage exact e=60..65 branches")
    parser.add_argument("--include-unsymmetrized", action="store_true")
    parser.add_argument(
        "--upper6-mode",
        choices=["eager-card", "lazy-card"],
        default="lazy-card",
        help="eager-card is the complete up-front encoding; lazy-card adds violated upper-6 cards.",
    )
    parser.add_argument(
        "--no-eager-zero-upper",
        dest="eager_zero_upper",
        action="store_false",
        help="with lazy-card, skip eager upper-6 cards for 6-sets containing vertex 0",
    )
    parser.set_defaults(eager_zero_upper=True)
    parser.add_argument("--no-min-degree-break", dest="min_degree_break", action="store_false")
    parser.set_defaults(min_degree_break=True)
    parser.add_argument("--no-degree-caps", dest="degree_caps", action="store_false")
    parser.set_defaults(degree_caps=True)
    parser.add_argument("--no-nonneighbor-turan", dest="nonneighbor_turan", action="store_false")
    parser.set_defaults(nonneighbor_turan=True)
    parser.add_argument("--no-precheck", dest="precheck", action="store_false")
    parser.set_defaults(precheck=True)
    parser.add_argument("--card-encoding", choices=sorted(ENCODINGS), default="seqcounter")
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--conf-budget", type=int, default=0)
    parser.add_argument("--prop-budget", type=int, default=0)
    parser.add_argument("--max-seconds", type=float, default=0.0, help="per solve_limited wall-clock interrupt")
    parser.add_argument("--max-total-seconds", type=float, default=0.0, help="per branch wall-clock limit")
    parser.add_argument(
        "--max-solve-attempts",
        type=int,
        default=1,
        help="repeat solve_limited after non-wall-clock budget exhaustion",
    )
    parser.add_argument("--max-lazy-rounds", type=int, default=50)
    parser.add_argument("--max-violations-per-round", type=int, default=500)
    parser.add_argument("--stop-on-sat", action="store_true", default=True)
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_RESULTS / "phase1_a_triage.json",
    )
    args = parser.parse_args()

    if args.n != 26:
        raise SystemExit("Agent A phase-1 defaults and symmetry prechecks are intended for n=26")
    if args.edge_count is not None and not args.min_edges <= args.edge_count <= args.max_edges:
        raise SystemExit("--edge-count must lie inside [--min-edges,--max-edges]")
    for degree in args.degrees:
        if degree < 0 or degree >= args.n:
            raise SystemExit("--degrees entries must be in [0,n-1]")
    if args.degree0 is not None and (args.degree0 < 0 or args.degree0 >= args.n):
        raise SystemExit("--degree0 must be in [0,n-1]")
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
