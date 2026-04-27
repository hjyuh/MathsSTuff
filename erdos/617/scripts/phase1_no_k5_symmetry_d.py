from __future__ import annotations

import argparse
import itertools
import json
import math
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results"


@dataclass(frozen=True)
class Branch:
    branch_id: int
    label: str
    root_degree: int | None = None


def edge_list(n: int) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return edges, {edge: idx + 1 for idx, edge in enumerate(edges)}


def edge_var(edge_id: dict[tuple[int, int], int], a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    return edge_id[(a, b)]


def incident_vars(n: int, edge_id: dict[tuple[int, int], int], vertex: int) -> list[int]:
    return [edge_var(edge_id, vertex, other) for other in range(n) if other != vertex]


def parse_int_set(text: str) -> list[int]:
    out: list[int] = []
    for chunk in text.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            left, right = chunk.split("-", 1)
            lo = int(left.strip())
            hi = int(right.strip())
            if hi < lo:
                raise argparse.ArgumentTypeError("ranges must be increasing")
            out.extend(range(lo, hi + 1))
        else:
            out.append(int(chunk))
    if not out:
        raise argparse.ArgumentTypeError("expected at least one integer")
    return sorted(set(out))


def status_name(result: bool | None) -> str:
    if result is True:
        return "sat"
    if result is False:
        return "unsat"
    return "unknown"


def stats_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    keys = sorted(set(before) | set(after))
    return {key: int(after.get(key, 0) - before.get(key, 0)) for key in keys}


def add_exact_edge_count(cnf: CNF, edge_vars: list[int], count: int, top_id: int) -> int:
    enc = CardEnc.equals(lits=edge_vars, bound=count, top_id=top_id, encoding=EncType.seqcounter)
    cnf.extend(enc.clauses)
    return max(top_id, enc.nv)


def add_lower6(cnf: CNF, n: int, edge_id: dict[tuple[int, int], int]) -> int:
    added = 0
    for subset in itertools.combinations(range(n), 6):
        cnf.append([edge_var(edge_id, a, b) for a, b in itertools.combinations(subset, 2)])
        added += 1
    return added


def add_forbid_k5(cnf: CNF, n: int, edge_id: dict[tuple[int, int], int]) -> int:
    added = 0
    for subset in itertools.combinations(range(n), 5):
        cnf.append([-edge_var(edge_id, a, b) for a, b in itertools.combinations(subset, 2)])
        added += 1
    return added


def build_base(args: argparse.Namespace) -> tuple[CNF, list[tuple[int, int]], dict[tuple[int, int], int], dict[str, int]]:
    edges, edge_id = edge_list(args.n)
    all_vars = list(range(1, len(edges) + 1))
    cnf = CNF()
    counts = {
        "lower6_clauses": add_lower6(cnf, args.n, edge_id),
        "forbid_k5_clauses": add_forbid_k5(cnf, args.n, edge_id),
        "edge_count_clauses": 0,
    }
    top = len(edges)
    before = len(cnf.clauses)
    top = add_exact_edge_count(cnf, all_vars, args.edges, top)
    counts["edge_count_clauses"] = len(cnf.clauses) - before
    cnf.nv = max(cnf.nv, top)
    return cnf, edges, edge_id, counts


def add_upper6_cardinality_cut(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    subset: tuple[int, ...],
    top_id: int,
) -> tuple[int, int]:
    evars = [edge_var(edge_id, a, b) for a, b in itertools.combinations(subset, 2)]
    atmost = CardEnc.atmost(lits=evars, bound=11, top_id=top_id, encoding=EncType.seqcounter)
    for clause in atmost.clauses:
        solver.add_clause(clause)
    return len(atmost.clauses), max(top_id, atmost.nv)


def upper6_violations(
    n: int,
    edge_id: dict[tuple[int, int], int],
    chosen: set[int],
    limit: int,
) -> list[tuple[int, ...]]:
    violations: list[tuple[int, ...]] = []
    for subset in itertools.combinations(range(n), 6):
        count = sum(
            1
            for a, b in itertools.combinations(subset, 2)
            if edge_var(edge_id, a, b) in chosen
        )
        if count > 11:
            violations.append(subset)
            if len(violations) >= limit:
                break
    return violations


def verify_skeleton(
    n: int,
    edges: list[tuple[int, int]],
    edge_id: dict[tuple[int, int], int],
    chosen: set[int],
    exact_edges: int,
) -> tuple[bool, str]:
    if len(chosen) != exact_edges:
        return False, f"edge count {len(chosen)} != {exact_edges}"
    for subset in itertools.combinations(range(n), 6):
        count = sum(
            1
            for a, b in itertools.combinations(subset, 2)
            if edge_var(edge_id, a, b) in chosen
        )
        if count < 1 or count > 11:
            return False, f"6-set {subset} has skeleton count {count}"
    for subset in itertools.combinations(range(n), 5):
        if all(edge_var(edge_id, a, b) in chosen for a, b in itertools.combinations(subset, 2)):
            return False, f"K5 skeleton on {subset}"
    missing = [idx for idx in chosen if idx < 1 or idx > len(edges)]
    if missing:
        return False, f"bad edge variables {missing[:5]}"
    return True, "ok"


def max_degree_range(n: int, edge_count: int) -> range:
    lo = math.ceil((2 * edge_count) / n)
    hi = min(n - 1, edge_count)
    return range(lo, hi + 1)


def make_branches(args: argparse.Namespace) -> tuple[list[Branch], bool]:
    if args.symmetry in {"none", "anchor-mixed"}:
        return [Branch(0, args.symmetry)], True

    if args.root_degrees is None:
        degrees = list(max_degree_range(args.n, args.edges))
        complete = True
    else:
        degrees = parse_int_set(args.root_degrees)
        full = set(max_degree_range(args.n, args.edges))
        complete = set(degrees) == full
    if args.max_branches > 0:
        degrees = degrees[: args.max_branches]
        complete = False

    branches = [Branch(i, f"maxdeg-star-d{degree}", degree) for i, degree in enumerate(degrees)]
    return branches, complete


def add_symmetry_clauses(
    solver: Solver,
    args: argparse.Namespace,
    edge_id: dict[tuple[int, int], int],
    branch: Branch,
    top_id: int,
) -> tuple[int, int, dict[str, object]]:
    added = 0
    meta: dict[str, object] = {"symmetry": args.symmetry, "branch_label": branch.label}

    if args.symmetry == "none":
        meta["safety"] = "no symmetry-breaking clauses"
        return added, top_id, meta

    if args.symmetry == "anchor-mixed":
        if not (0 < args.edges < math.comb(args.n, 2)):
            raise ValueError("anchor-mixed requires a nonempty, noncomplete graph")
        solver.add_clause([edge_var(edge_id, 0, 1)])
        solver.add_clause([-edge_var(edge_id, 0, 2)])
        meta["safety"] = (
            "safe for this branch: every nonempty noncomplete graph has a vertex incident "
            "to both an edge and a nonedge; relabel it to 0, a neighbor to 1, and a "
            "nonneighbor to 2"
        )
        added += 2
        return added, top_id, meta

    if args.symmetry != "maxdeg-star":
        raise ValueError(f"unknown symmetry mode: {args.symmetry}")
    if branch.root_degree is None:
        raise ValueError("maxdeg-star branch needs a root degree")
    d = branch.root_degree
    if d < 0 or d >= args.n:
        raise ValueError(f"root degree {d} outside [0,{args.n - 1}]")

    for vertex in range(1, args.n):
        lit = edge_var(edge_id, 0, vertex)
        solver.add_clause([lit] if vertex <= d else [-lit])
        added += 1

    for vertex in range(1, args.n):
        inc = incident_vars(args.n, edge_id, vertex)
        if d < len(inc):
            atmost = CardEnc.atmost(lits=inc, bound=d, top_id=top_id, encoding=EncType.seqcounter)
            for clause in atmost.clauses:
                solver.add_clause(clause)
            added += len(atmost.clauses)
            top_id = max(top_id, atmost.nv)

    meta.update(
        {
            "root_degree": d,
            "safety": (
                "safe when all root-degree branches are swept: choose a maximum-degree "
                "vertex as 0, let d be its degree, relabel its neighbors to 1..d and "
                "nonneighbors to d+1..n-1, then every other vertex has degree at most d"
            ),
        }
    )
    return added, top_id, meta


def solve_branch(
    args: argparse.Namespace,
    base: CNF,
    edges: list[tuple[int, int]],
    edge_id: dict[tuple[int, int], int],
    branch: Branch,
    out_prefix: Path,
) -> dict[str, object]:
    started = time.perf_counter()
    solve_calls = 0
    lazy_rounds = 0
    lazy_upper6_clauses = 0
    current_top = base.nv
    interrupted_by_wall_clock = False
    model: list[int] | None = None
    result: bool | None = None
    attempts_since_clause = 0

    with Solver(name=args.solver, bootstrap_with=base.clauses) as solver:
        symmetry_clauses, current_top, symmetry_meta = add_symmetry_clauses(
            solver, args, edge_id, branch, current_top
        )
        accum_before_branch = solver.accum_stats()

        while True:
            interrupted_this_call = False

            def interrupt_solver() -> None:
                nonlocal interrupted_by_wall_clock, interrupted_this_call
                interrupted_by_wall_clock = True
                interrupted_this_call = True
                solver.interrupt()

            timer: threading.Timer | None = None
            if args.max_seconds > 0:
                if hasattr(solver, "clear_interrupt"):
                    solver.clear_interrupt()
                timer = threading.Timer(args.max_seconds, interrupt_solver)
                timer.daemon = True
                timer.start()
            if args.conf_budget > 0:
                solver.conf_budget(args.conf_budget)
            solve_started = time.perf_counter()
            before = solver.accum_stats()
            try:
                if args.conf_budget > 0 or args.max_seconds > 0:
                    result = solver.solve_limited(expect_interrupt=True)
                else:
                    result = solver.solve()
            finally:
                if timer is not None:
                    timer.cancel()
                if hasattr(solver, "clear_interrupt"):
                    solver.clear_interrupt()
            after = solver.accum_stats()
            solve_calls += 1
            solve_seconds = time.perf_counter() - solve_started

            if result is None and args.conf_budget > 0 and attempts_since_clause + 1 < args.max_solve_attempts:
                attempts_since_clause += 1
                print(
                    json.dumps(
                        {
                            "branch": branch.label,
                            "solve_call": solve_calls,
                            "status": "unknown",
                            "solve_seconds": round(solve_seconds, 3),
                            "stats_delta": stats_delta(before, after),
                            "interrupted_by_wall_clock": interrupted_this_call,
                        }
                    ),
                    flush=True,
                )
                continue

            if result is not True:
                break

            attempts_since_clause = 0
            model = solver.get_model()
            chosen = {lit for lit in model if 1 <= lit <= len(edges)}
            violations = upper6_violations(args.n, edge_id, chosen, args.max_violations_per_round)
            if not violations:
                break

            lazy_rounds += 1
            for subset in violations:
                added, current_top = add_upper6_cardinality_cut(solver, edge_id, subset, current_top)
                lazy_upper6_clauses += added

            print(
                json.dumps(
                    {
                        "branch": branch.label,
                        "lazy_round": lazy_rounds,
                        "upper6_violations": len(violations),
                        "lazy_upper6_clauses": lazy_upper6_clauses,
                        "edge_count": len(chosen),
                    }
                ),
                flush=True,
            )
            if lazy_rounds >= args.max_lazy_rounds:
                result = None
                model = None
                break

        accum_after_branch = solver.accum_stats()

    row: dict[str, object] = {
        "branch_id": branch.branch_id,
        "branch_label": branch.label,
        "status": status_name(result),
        "n": args.n,
        "edges": args.edges,
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "max_seconds": args.max_seconds,
        "max_solve_attempts": args.max_solve_attempts,
        "solve_calls": solve_calls,
        "lazy_rounds": lazy_rounds,
        "lazy_upper6_clauses": lazy_upper6_clauses,
        "base_vars": base.nv,
        "vars_after_lazy": current_top,
        "base_clauses": len(base.clauses),
        "symmetry_clauses": symmetry_clauses,
        "interrupted_by_wall_clock": interrupted_by_wall_clock,
        "stats_delta": stats_delta(accum_before_branch, accum_after_branch),
        "seconds": round(time.perf_counter() - started, 3),
    }
    row.update(symmetry_meta)

    if model is not None and result is True:
        chosen = {lit for lit in model if 1 <= lit <= len(edges)}
        ok, message = verify_skeleton(args.n, edges, edge_id, chosen, args.edges)
        model_path = out_prefix.with_suffix(f".{branch.label}.model.json")
        model_edges = [list(edges[var - 1]) for var in sorted(chosen)]
        model_path.write_text(json.dumps(model_edges, indent=2), encoding="utf-8")
        row.update(
            {
                "edge_count": len(chosen),
                "model_path": str(model_path),
                "model_check": "valid" if ok else "invalid",
                "model_check_message": message,
            }
        )

    return row


def aggregate_status(rows: Iterable[dict[str, object]], complete_branch_sweep: bool) -> str:
    materialized = list(rows)
    if any(row["status"] == "sat" for row in materialized):
        return "sat_found"
    if materialized and all(row["status"] == "unsat" for row in materialized):
        return "all_unsat" if complete_branch_sweep else "selected_branches_unsat"
    return "incomplete"


def default_out(args: argparse.Namespace) -> Path:
    suffix = f"e{args.edges}_{args.symmetry}_{args.solver}_b{args.conf_budget}"
    if args.max_seconds > 0:
        suffix += f"_s{args.max_seconds:g}"
    if args.root_degrees:
        suffix += "_d" + args.root_degrees.replace(",", "-")
    if args.max_branches > 0:
        suffix += f"_first{args.max_branches}"
    return DEFAULT_RESULTS / f"phase1_d_{suffix}.json"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="EP617 Phase 1 Agent D: no-K5 minimum-colour skeleton symmetry triage."
    )
    parser.add_argument("--n", type=int, default=26)
    parser.add_argument("--edges", type=int, default=60, help="exact skeleton edge count")
    parser.add_argument(
        "--symmetry",
        choices=["none", "anchor-mixed", "maxdeg-star"],
        default="none",
    )
    parser.add_argument(
        "--root-degrees",
        default=None,
        help="for maxdeg-star, comma/range list such as 5-9; default sweeps all possible max degrees",
    )
    parser.add_argument("--max-branches", type=int, default=0, help="0 means no branch cap")
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--conf-budget", type=int, default=100000)
    parser.add_argument("--max-seconds", type=float, default=0.0, help="per solve call; 0 disables")
    parser.add_argument("--max-solve-attempts", type=int, default=1)
    parser.add_argument("--max-lazy-rounds", type=int, default=20)
    parser.add_argument("--max-violations-per-round", type=int, default=200)
    parser.add_argument("--stop-on-sat", action="store_true")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    if args.n != 26:
        raise SystemExit("this sprint script is scoped to n=26")
    if not 0 <= args.edges <= math.comb(args.n, 2):
        raise SystemExit("--edges outside graph edge range")
    if args.max_solve_attempts < 1:
        raise SystemExit("--max-solve-attempts must be positive")

    out_path = args.out or default_out(args)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_prefix = out_path.with_suffix("")

    build_started = time.perf_counter()
    base, edges, edge_id, base_counts = build_base(args)
    build_seconds = time.perf_counter() - build_started
    branches, complete_branch_sweep = make_branches(args)

    rows: list[dict[str, object]] = []
    for branch in branches:
        row = solve_branch(args, base, edges, edge_id, branch, out_prefix)
        rows.append(row)
        print(json.dumps(row), flush=True)
        if args.stop_on_sat and row["status"] == "sat":
            complete_branch_sweep = False
            break

    counts = {"sat": 0, "unsat": 0, "unknown": 0}
    for row in rows:
        counts[str(row["status"])] += 1

    summary = {
        "status": aggregate_status(rows, complete_branch_sweep),
        "agent": "D",
        "phase": "phase1_no_k5_minimum_colour",
        "n": args.n,
        "edges": args.edges,
        "constraints": {
            "exact_edges": args.edges,
            "every_6_set_has_at_least_one_skeleton_edge": True,
            "every_6_set_has_at_most_11_skeleton_edges": "lazy",
            "forbid_k5_skeleton": True,
        },
        "symmetry": args.symmetry,
        "complete_branch_sweep": complete_branch_sweep,
        "possible_max_degree_range": list(max_degree_range(args.n, args.edges)),
        "branches_requested": len(branches),
        "branches_completed": len(rows),
        "counts": counts,
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "max_seconds": args.max_seconds,
        "max_solve_attempts": args.max_solve_attempts,
        "max_lazy_rounds": args.max_lazy_rounds,
        "max_violations_per_round": args.max_violations_per_round,
        "base_vars": base.nv,
        "base_clauses": len(base.clauses),
        "base_counts": base_counts,
        "build_seconds": round(build_seconds, 3),
        "rows": rows,
        "safety_notes": {
            "anchor-mixed": (
                "Safe as a single global branch for 0 < e < C(n,2): relabel a mixed vertex "
                "to 0, one neighbor to 1, and one nonneighbor to 2."
            ),
            "maxdeg-star": (
                "Safe only as a complete sweep over d: every graph has a maximum-degree "
                "vertex; after relabeling it to 0, its d neighbors can be labeled 1..d, "
                "and all other vertices have degree at most d."
            ),
        },
    }
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)

    if summary["status"] == "sat_found":
        return 10
    if summary["status"] in {"all_unsat", "selected_branches_unsat"}:
        return 20
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
