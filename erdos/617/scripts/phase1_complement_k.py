from __future__ import annotations

import argparse
import itertools
import json
import threading
import time
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Solver


def edge_list(n: int) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return edges, {e: idx + 1 for idx, e in enumerate(edges)}


def complement_edges(n: int, edges: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return {
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if (i, j) not in edges
    }


def translate_g_to_h(n: int, min_g_edges: int, max_g_edges: int) -> dict[str, object]:
    total_edges = n * (n - 1) // 2
    return {
        "n": n,
        "total_edges": total_edges,
        "G_edge_range": [min_g_edges, max_g_edges],
        "H_edge_range": [total_edges - max_g_edges, total_edges - min_g_edges],
        "G_six_edge_range": [1, 11],
        "H_six_edge_range": [15 - 11, 15 - 1],
        "omega_G_le_4_equiv_alpha_H_le_4": True,
        "proof": [
            "e(H) = C(n,2) - e(G).",
            "For every 6-set S, e_H(S) = 15 - e_G(S), so 1 <= e_G(S) <= 11 becomes 4 <= e_H(S) <= 14.",
            "A 5-set is independent in H iff it is a K5 in G, so omega(G) <= 4 iff alpha(H) <= 4.",
            "The upper bound e_H(S) <= 14 is exactly omega(H) <= 5.",
        ],
    }


def build_cnf(
    n: int,
    min_edges: int,
    max_edges: int,
    fix_k5: bool,
    eager_lower6: bool,
) -> tuple[CNF, list[tuple[int, int]], dict[str, object]]:
    edges, edge_id = edge_list(n)
    cnf = CNF()
    anchor = tuple(range(5))

    five_set_clauses = 0
    for S in itertools.combinations(range(n), 5):
        cnf.append([edge_id[(a, b)] for a, b in itertools.combinations(S, 2)])
        five_set_clauses += 1

    six_set_clique_clauses = 0
    for S in itertools.combinations(range(n), 6):
        cnf.append([-edge_id[(a, b)] for a, b in itertools.combinations(S, 2)])
        six_set_clique_clauses += 1

    top = len(edges)
    lower6_clauses = 0
    if eager_lower6:
        for S in itertools.combinations(range(n), 6):
            evars = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
            atleast = CardEnc.atleast(lits=evars, bound=4, top_id=top, encoding=EncType.seqcounter)
            cnf.extend(atleast.clauses)
            top = max(top, atleast.nv)
            lower6_clauses += len(atleast.clauses)

    anchor_units = 0
    anchor_outside_clauses = 0
    if fix_k5:
        for a, b in itertools.combinations(anchor, 2):
            cnf.append([edge_id[(a, b)]])
            anchor_units += 1
        for v in range(5, n):
            cnf.append([-edge_id[tuple(sorted((v, u)))] for u in anchor])
            anchor_outside_clauses += 1

    all_edges = list(range(1, len(edges) + 1))
    atleast = CardEnc.atleast(lits=all_edges, bound=min_edges, top_id=top, encoding=EncType.seqcounter)
    cnf.extend(atleast.clauses)
    top = max(top, atleast.nv)
    atmost = CardEnc.atmost(lits=all_edges, bound=max_edges, top_id=top, encoding=EncType.seqcounter)
    cnf.extend(atmost.clauses)
    top = max(top, atmost.nv)

    cnf.nv = max(cnf.nv, top)
    metadata = {
        "five_set_clauses": five_set_clauses,
        "six_set_clique_clauses": six_set_clique_clauses,
        "lower6_clauses": lower6_clauses,
        "anchor": list(anchor) if fix_k5 else None,
        "anchor_units": anchor_units,
        "anchor_outside_clauses": anchor_outside_clauses,
    }
    return cnf, edges, metadata


def lower6_violations(
    edges: list[tuple[int, int]],
    chosen: set[int],
    n: int,
    max_violations: int,
) -> list[tuple[int, ...]]:
    edge_id = {e: idx + 1 for idx, e in enumerate(edges)}
    out = []
    for S in itertools.combinations(range(n), 6):
        count = sum(1 for a, b in itertools.combinations(S, 2) if edge_id[(a, b)] in chosen)
        if count < 4:
            out.append(S)
            if len(out) >= max_violations:
                return out
    return out


def add_lower6_cardinality_cut(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    S: tuple[int, ...],
    top_id: int,
) -> tuple[int, int]:
    evars = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
    atleast = CardEnc.atleast(lits=evars, bound=4, top_id=top_id, encoding=EncType.seqcounter)
    for clause in atleast.clauses:
        solver.add_clause(clause)
    return len(atleast.clauses), max(top_id, atleast.nv)


def summarise_graph(
    n: int,
    h_edge_set: set[tuple[int, int]],
    anchor: tuple[int, ...] | None = None,
) -> dict[str, object]:
    all_edges = {(i, j) for i in range(n) for j in range(i + 1, n)}
    g_edge_set = all_edges - h_edge_set

    min_h6 = 16
    max_h6 = -1
    min_h6_set: tuple[int, ...] | None = None
    max_h6_set: tuple[int, ...] | None = None
    min_g6 = 16
    max_g6 = -1
    min_g6_set: tuple[int, ...] | None = None
    max_g6_set: tuple[int, ...] | None = None
    lower6_violations = 0
    clique6_violations = 0

    for S in itertools.combinations(range(n), 6):
        pairs = list(itertools.combinations(S, 2))
        h_count = sum(1 for e in pairs if e in h_edge_set)
        g_count = 15 - h_count
        if h_count < min_h6:
            min_h6 = h_count
            min_h6_set = S
        if h_count > max_h6:
            max_h6 = h_count
            max_h6_set = S
        if g_count < min_g6:
            min_g6 = g_count
            min_g6_set = S
        if g_count > max_g6:
            max_g6 = g_count
            max_g6_set = S
        if h_count < 4:
            lower6_violations += 1
        if h_count == 15:
            clique6_violations += 1

    independent5_violations = 0
    first_independent5: tuple[int, ...] | None = None
    for S in itertools.combinations(range(n), 5):
        if all((a, b) not in h_edge_set for a, b in itertools.combinations(S, 2)):
            independent5_violations += 1
            if first_independent5 is None:
                first_independent5 = S

    anchor_histogram: dict[int, int] | None = None
    if anchor is not None:
        anchor_histogram = {}
        anchor_set = set(anchor)
        for v in range(n):
            if v in anchor_set:
                continue
            miss = sum(1 for u in anchor if tuple(sorted((u, v))) not in h_edge_set)
            anchor_histogram[miss] = anchor_histogram.get(miss, 0) + 1

    return {
        "edge_count_H": len(h_edge_set),
        "edge_count_G": len(g_edge_set),
        "alpha_H_le_4": independent5_violations == 0,
        "independent5_violations": independent5_violations,
        "first_independent5": list(first_independent5) if first_independent5 is not None else None,
        "omega_H_le_5": clique6_violations == 0,
        "clique6_violations": clique6_violations,
        "six_edge_range_H": [min_h6, max_h6],
        "six_edge_range_H_witnesses": {
            "min": list(min_h6_set) if min_h6_set is not None else None,
            "max": list(max_h6_set) if max_h6_set is not None else None,
        },
        "six_edge_range_G": [min_g6, max_g6],
        "six_edge_range_G_witnesses": {
            "min": list(min_g6_set) if min_g6_set is not None else None,
            "max": list(max_g6_set) if max_g6_set is not None else None,
        },
        "lower6_H_violations": lower6_violations,
        "anchor_missing_histogram": anchor_histogram,
    }


def write_model_files(
    out: Path,
    n: int,
    edges: list[tuple[int, int]],
    chosen: set[int],
) -> dict[str, str]:
    h_edge_set = {edges[v - 1] for v in chosen}
    g_edge_set = complement_edges(n, h_edge_set)
    h_model_path = out.with_suffix(".H.model.json")
    g_model_path = out.with_suffix(".G.model.json")
    h_model_path.write_text(json.dumps([list(e) for e in sorted(h_edge_set)], indent=2), encoding="utf-8")
    g_model_path.write_text(json.dumps([list(e) for e in sorted(g_edge_set)], indent=2), encoding="utf-8")
    return {
        "H_model_path": str(h_model_path),
        "G_model_path": str(g_model_path),
    }


def inspect_existing_g_model(args: argparse.Namespace) -> int:
    g_edges = {tuple(sorted((int(a), int(b)))) for a, b in json.loads(args.inspect_g_model.read_text(encoding="utf-8"))}
    h_edges = complement_edges(args.n, g_edges)
    summary = {
        "mode": "inspect_g_model",
        "input_path": str(args.inspect_g_model),
        "translation": translate_g_to_h(args.n, args.g_min_edges, args.g_max_edges),
        "analysis": summarise_graph(args.n, h_edges, anchor=tuple(range(5)) if args.fix_k5 else None),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Complement-side phase-1 analysis for EP617.")
    parser.add_argument("--n", type=int, default=26)
    parser.add_argument("--g-min-edges", type=int, default=60)
    parser.add_argument("--g-max-edges", type=int, default=65)
    parser.add_argument("--min-edges", type=int, default=260, help="lower bound on e(H)")
    parser.add_argument("--max-edges", type=int, default=265, help="upper bound on e(H)")
    parser.add_argument("--fix-k5", action="store_true")
    parser.add_argument("--eager-lower6", action="store_true")
    parser.add_argument("--lazy-lower6", action="store_true")
    parser.add_argument("--max-lazy-rounds", type=int, default=40)
    parser.add_argument("--max-violations-per-round", type=int, default=200)
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--conf-budget", type=int, default=0)
    parser.add_argument("--max-seconds", type=float, default=0.0, help="per solve-call wall-clock limit; 0 disables")
    parser.add_argument("--max-solve-attempts", type=int, default=1)
    parser.add_argument("--inspect-g-model", type=Path, default=None)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("erdos/617/results/phase1_k_complement_summary.json"),
    )
    args = parser.parse_args()

    if args.inspect_g_model is not None:
        return inspect_existing_g_model(args)

    translation = translate_g_to_h(args.n, args.g_min_edges, args.g_max_edges)
    cnf, edges, metadata = build_cnf(
        n=args.n,
        min_edges=args.min_edges,
        max_edges=args.max_edges,
        fix_k5=args.fix_k5,
        eager_lower6=args.eager_lower6,
    )
    edge_id = {e: idx + 1 for idx, e in enumerate(edges)}
    anchor = tuple(range(5)) if args.fix_k5 else None

    lazy_rounds = 0
    lazy_clauses = 0
    solve_calls = 0
    attempts_since_clause = 0
    current_top = cnf.nv
    model: list[int] | None = None
    result: bool | None = None
    total_solve_seconds = 0.0

    with Solver(name=args.solver, bootstrap_with=cnf.clauses) as solver:
        while True:
            interrupted_by_wall_clock = False

            def interrupt_solver() -> None:
                nonlocal interrupted_by_wall_clock
                interrupted_by_wall_clock = True
                solver.interrupt()

            timer: threading.Timer | None = None
            if args.conf_budget:
                solver.conf_budget(args.conf_budget)
            if args.max_seconds > 0:
                if hasattr(solver, "clear_interrupt"):
                    solver.clear_interrupt()
                timer = threading.Timer(args.max_seconds, interrupt_solver)
                timer.daemon = True
                timer.start()

            started = time.perf_counter()
            try:
                if args.conf_budget or args.max_seconds > 0:
                    result = solver.solve_limited(expect_interrupt=True)
                else:
                    result = solver.solve()
            finally:
                if timer is not None:
                    timer.cancel()
                if hasattr(solver, "clear_interrupt"):
                    solver.clear_interrupt()
            total_solve_seconds += time.perf_counter() - started
            solve_calls += 1

            if result is None and attempts_since_clause + 1 < args.max_solve_attempts:
                attempts_since_clause += 1
                print(
                    json.dumps(
                        {
                            "solve_call": solve_calls,
                            "status": "unknown",
                            "attempts_since_clause": attempts_since_clause,
                            "interrupted_by_wall_clock": interrupted_by_wall_clock,
                            "lazy_rounds": lazy_rounds,
                            "lazy_clauses": lazy_clauses,
                        }
                    ),
                    flush=True,
                )
                continue

            if result is not True:
                break

            attempts_since_clause = 0
            model = solver.get_model()
            chosen = {v for v in model if 1 <= v <= len(edges)}
            lower_violations = []
            if args.lazy_lower6:
                lower_violations = lower6_violations(
                    edges,
                    chosen,
                    args.n,
                    args.max_violations_per_round,
                )
            if not lower_violations:
                break

            lazy_rounds += 1
            for S in lower_violations:
                added, current_top = add_lower6_cardinality_cut(solver, edge_id, S, current_top)
                lazy_clauses += added
            print(
                json.dumps(
                    {
                        "lazy_round": lazy_rounds,
                        "lower6_violations": len(lower_violations),
                        "lazy_clauses": lazy_clauses,
                        "edge_count": len(chosen),
                    }
                ),
                flush=True,
            )
            if lazy_rounds >= args.max_lazy_rounds:
                result = None
                model = None
                break

    summary = {
        "mode": "solve",
        "translation": translation,
        "n": args.n,
        "min_edges": args.min_edges,
        "max_edges": args.max_edges,
        "fix_k5": args.fix_k5,
        "eager_lower6": args.eager_lower6,
        "lazy_lower6": args.lazy_lower6,
        "max_lazy_rounds": args.max_lazy_rounds,
        "max_violations_per_round": args.max_violations_per_round,
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "max_seconds": args.max_seconds,
        "max_solve_attempts": args.max_solve_attempts,
        "solve_calls": solve_calls,
        "solve_seconds": round(total_solve_seconds, 3),
        "lazy_rounds": lazy_rounds,
        "lazy_clauses": lazy_clauses,
        "vars": cnf.nv,
        "vars_after_lazy": current_top,
        "clauses": len(cnf.clauses),
        "status": "sat" if result is True else ("unsat" if result is False else "unknown"),
        "metadata": metadata,
    }

    if model is not None:
        chosen = {v for v in model if 1 <= v <= len(edges)}
        model_paths = write_model_files(args.out, args.n, edges, chosen)
        h_edge_set = {edges[v - 1] for v in chosen}
        summary["model_paths"] = model_paths
        summary["analysis"] = summarise_graph(args.n, h_edge_set, anchor=anchor)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    return 0 if result is True else (10 if result is False else 20)


if __name__ == "__main__":
    raise SystemExit(main())
