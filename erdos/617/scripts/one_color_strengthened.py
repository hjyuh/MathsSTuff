from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Solver


def edge_list(n: int) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return edges, {e: idx + 1 for idx, e in enumerate(edges)}


def build_cnf(
    n: int,
    max_edges: int,
    min_edges: int,
    clique_star: bool,
    upper6: bool,
    forbid_k5: bool,
) -> tuple[CNF, list[tuple[int, int]]]:
    edges, edge_id = edge_list(n)
    cnf = CNF()
    top = len(edges)

    # Every 6-set must contain at least one edge of the minimum color.
    # Optionally, eagerly enforce at most 11 such edges, since the other
    # four colors each need at least one edge in the same 6-set.
    for S in itertools.combinations(range(n), 6):
        evars = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
        cnf.append(evars)
        if upper6:
            atmost = CardEnc.atmost(lits=evars, bound=11, top_id=top, encoding=EncType.seqcounter)
            cnf.extend(atmost.clauses)
            top = max(top, atmost.nv)

    all_edges = list(range(1, len(edges) + 1))
    if min_edges > 0:
        atleast = CardEnc.atleast(lits=all_edges, bound=min_edges, top_id=top, encoding=EncType.seqcounter)
        cnf.extend(atleast.clauses)
        top = max(top, atleast.nv)
    if max_edges >= 0:
        atmost = CardEnc.atmost(lits=all_edges, bound=max_edges, top_id=top, encoding=EncType.seqcounter)
        cnf.extend(atmost.clauses)
        top = max(top, atmost.nv)

    if clique_star:
        # Projection of the K5-star rule for a minimum color:
        # if Q is a K5 in this color, any outside vertex has at most one
        # edge of this color into Q. Reified as:
        # not(all clique edges in Q) OR not(two star edges from v to Q).
        for Q in itertools.combinations(range(n), 5):
            clique_edges = [edge_id[(a, b)] for a, b in itertools.combinations(Q, 2)]
            qset = set(Q)
            for v in range(n):
                if v in qset:
                    continue
                star_edges = [edge_id[tuple(sorted((v, u)))] for u in Q]
                for e1, e2 in itertools.combinations(star_edges, 2):
                    cnf.append([-x for x in clique_edges] + [-e1, -e2])

    if forbid_k5:
        for Q in itertools.combinations(range(n), 5):
            clique_edges = [edge_id[(a, b)] for a, b in itertools.combinations(Q, 2)]
            cnf.append([-x for x in clique_edges])

    cnf.nv = max(cnf.nv, top)
    return cnf, edges


def add_k5_star_projection_for_pair(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    Q: tuple[int, ...],
    v: int,
) -> int:
    clique_edges = [edge_id[(a, b)] for a, b in itertools.combinations(Q, 2)]
    star_edges = [edge_id[tuple(sorted((v, u)))] for u in Q]
    added = 0
    for e1, e2 in itertools.combinations(star_edges, 2):
        solver.add_clause([-x for x in clique_edges] + [-e1, -e2])
        added += 1
    return added


def ensure_k5_aux(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    q_aux: dict[tuple[int, ...], int],
    top_id: int,
    Q: tuple[int, ...],
) -> tuple[int, int, int]:
    """Return an auxiliary variable equivalent to 'Q is a selected K5'."""
    if Q in q_aux:
        return q_aux[Q], top_id, 0
    qvar = top_id + 1
    q_aux[Q] = qvar
    clique_edges = [edge_id[(a, b)] for a, b in itertools.combinations(Q, 2)]
    added = 0
    # qvar -> every clique edge.
    for e in clique_edges:
        solver.add_clause([-qvar, e])
        added += 1
    # every clique edge -> qvar.
    solver.add_clause([qvar] + [-e for e in clique_edges])
    added += 1
    return qvar, qvar, added


def add_k5_star_projection_aux_for_pair(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    q_aux: dict[tuple[int, ...], int],
    top_id: int,
    Q: tuple[int, ...],
    v: int,
) -> tuple[int, int]:
    qvar, top_id, added = ensure_k5_aux(solver, edge_id, q_aux, top_id, Q)
    star_edges = [edge_id[tuple(sorted((v, u)))] for u in Q]
    for e1, e2 in itertools.combinations(star_edges, 2):
        solver.add_clause([-qvar, -e1, -e2])
        added += 1
    return added, top_id


def k5_star_violations(
    edges: list[tuple[int, int]],
    chosen: set[int],
    n: int,
    max_violations: int,
) -> list[tuple[tuple[int, ...], int]]:
    edge_id = {e: idx + 1 for idx, e in enumerate(edges)}
    violations = []
    for Q in itertools.combinations(range(n), 5):
        if not all(edge_id[(a, b)] in chosen for a, b in itertools.combinations(Q, 2)):
            continue
        qset = set(Q)
        for v in range(n):
            if v in qset:
                continue
            deg = sum(1 for u in Q if edge_id[tuple(sorted((v, u)))] in chosen)
            if deg > 1:
                violations.append((Q, v))
                if len(violations) >= max_violations:
                    return violations
    return violations


def upper6_violations(
    edges: list[tuple[int, int]],
    chosen: set[int],
    n: int,
    max_violations: int,
) -> list[tuple[int, ...]]:
    edge_id = {e: idx + 1 for idx, e in enumerate(edges)}
    violations = []
    for S in itertools.combinations(range(n), 6):
        count = sum(1 for a, b in itertools.combinations(S, 2) if edge_id[(a, b)] in chosen)
        if count > 11:
            violations.append(S)
            if len(violations) >= max_violations:
                return violations
    return violations


def add_upper6_cut(solver: Solver, edge_id: dict[tuple[int, int], int], S: tuple[int, ...]) -> int:
    # At most 11 of the 15 edges are selected: every 12-subset is forbidden.
    evars = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
    added = 0
    for twelve in itertools.combinations(evars, 12):
        solver.add_clause([-v for v in twelve])
        added += 1
    return added


def add_upper6_cardinality_cut(
    solver: Solver,
    edge_id: dict[tuple[int, int], int],
    S: tuple[int, ...],
    top_id: int,
) -> tuple[int, int]:
    evars = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
    atmost = CardEnc.atmost(lits=evars, bound=11, top_id=top_id, encoding=EncType.seqcounter)
    for clause in atmost.clauses:
        solver.add_clause(clause)
    return len(atmost.clauses), max(top_id, atmost.nv)


def verify_model(
    edges: list[tuple[int, int]],
    chosen: set[int],
    n: int,
    forbid_k5: bool,
) -> tuple[bool, str]:
    edge_id = {e: idx + 1 for idx, e in enumerate(edges)}
    for S in itertools.combinations(range(n), 6):
        count = sum(1 for a, b in itertools.combinations(S, 2) if edge_id[(a, b)] in chosen)
        if count < 1 or count > 11:
            return False, f"6-set {S} has count {count}"
    for Q in itertools.combinations(range(n), 5):
        q_clique = all(edge_id[(a, b)] in chosen for a, b in itertools.combinations(Q, 2))
        if not q_clique:
            continue
        qset = set(Q)
        for v in range(n):
            if v in qset:
                continue
            deg = sum(1 for u in Q if edge_id[tuple(sorted((v, u)))] in chosen)
            if deg > 1:
                return False, f"K5 {Q}, outside {v}, star deg {deg}"
        if forbid_k5:
            return False, f"forbidden K5 {Q}"
    return True, "ok"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=26)
    parser.add_argument("--min-edges", type=int, default=60)
    parser.add_argument("--max-edges", type=int, default=65)
    parser.add_argument("--no-k5-star", action="store_true")
    parser.add_argument(
        "--forbid-k5",
        action="store_true",
        help="Add omega(G) <= 4 for the one-color skeleton.",
    )
    parser.add_argument("--lazy-k5-star", action="store_true")
    parser.add_argument(
        "--lazy-k5-aux",
        action="store_true",
        help="When lazily adding K5-star projection cuts, use a short auxiliary K5 indicator.",
    )
    parser.add_argument("--lazy-upper6", action="store_true")
    parser.add_argument(
        "--lazy-upper6-card",
        action="store_true",
        help="When lazily adding upper-6 cuts, use a seqcounter instead of all 12-subset clauses.",
    )
    parser.add_argument("--max-lazy-rounds", type=int, default=50)
    parser.add_argument("--max-violations-per-round", type=int, default=200)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--conf-budget", type=int, default=0)
    parser.add_argument(
        "--max-solve-attempts",
        type=int,
        default=1,
        help="With --conf-budget, keep calling solve_limited this many times before returning unknown.",
    )
    parser.add_argument("--out", type=Path, default=Path("erdos/617/results/one_color_strengthened_e60_65.json"))
    args = parser.parse_args()

    cnf, edges = build_cnf(
        args.n,
        args.max_edges,
        args.min_edges,
        clique_star=(not args.no_k5_star and not args.lazy_k5_star),
        upper6=not args.lazy_upper6,
        forbid_k5=args.forbid_k5,
    )
    edge_id = {e: idx + 1 for idx, e in enumerate(edges)}
    lazy_rounds = 0
    lazy_clauses = 0
    lazy_upper6_clauses = 0
    lazy_k5_clauses = 0
    solve_calls = 0
    attempts_since_clause = 0
    current_top = cnf.nv
    k5_aux: dict[tuple[int, ...], int] = {}
    model = None
    with Solver(name=args.solver, bootstrap_with=cnf.clauses) as solver:
        while True:
            if args.conf_budget:
                solver.conf_budget(args.conf_budget)
                result = solver.solve_limited()
            else:
                result = solver.solve()
            solve_calls += 1
            if result is None and args.conf_budget and attempts_since_clause + 1 < args.max_solve_attempts:
                attempts_since_clause += 1
                print(
                    {
                        "solve_call": solve_calls,
                        "result": "unknown",
                        "attempts_since_clause": attempts_since_clause,
                        "lazy_clauses": lazy_clauses,
                    },
                    flush=True,
                )
                continue
            if result is not True:
                break
            attempts_since_clause = 0
            model = solver.get_model()
            positives = {v for v in model if 1 <= v <= len(edges)}
            upper_violations = []
            if args.lazy_upper6:
                upper_violations = upper6_violations(
                    edges,
                    positives,
                    args.n,
                    args.max_violations_per_round,
                )
            star_violations = []
            if args.lazy_k5_star and not args.no_k5_star:
                star_violations = k5_star_violations(
                    edges,
                    positives,
                    args.n,
                    args.max_violations_per_round,
                )
            if not upper_violations and not star_violations:
                break
            lazy_rounds += 1
            for S in upper_violations:
                if args.lazy_upper6_card:
                    added, current_top = add_upper6_cardinality_cut(solver, edge_id, S, current_top)
                else:
                    added = add_upper6_cut(solver, edge_id, S)
                lazy_clauses += added
                lazy_upper6_clauses += added
            for Q, v in star_violations:
                if args.lazy_k5_aux:
                    added, current_top = add_k5_star_projection_aux_for_pair(
                        solver, edge_id, k5_aux, current_top, Q, v
                    )
                else:
                    added = add_k5_star_projection_for_pair(solver, edge_id, Q, v)
                lazy_clauses += added
                lazy_k5_clauses += added
            print(
                {
                    "lazy_round": lazy_rounds,
                    "upper6_violations": len(upper_violations),
                    "k5_star_violations": len(star_violations),
                    "lazy_clauses": lazy_clauses,
                    "edge_count": len(positives),
                },
                flush=True,
            )
            if lazy_rounds >= args.max_lazy_rounds:
                result = None
                model = None
                break

    summary = {
        "n": args.n,
        "min_edges": args.min_edges,
        "max_edges": args.max_edges,
        "k5_star_projection": not args.no_k5_star,
        "forbid_k5": args.forbid_k5,
        "lazy_k5_star": args.lazy_k5_star,
        "lazy_upper6": args.lazy_upper6,
        "lazy_upper6_card": args.lazy_upper6_card,
        "lazy_k5_aux": args.lazy_k5_aux,
        "lazy_rounds": lazy_rounds,
        "lazy_clauses": lazy_clauses,
        "lazy_upper6_clauses": lazy_upper6_clauses,
        "lazy_k5_clauses": lazy_k5_clauses,
        "lazy_k5_aux_vars": len(k5_aux),
        "vars": cnf.nv,
        "vars_after_lazy": current_top,
        "clauses": len(cnf.clauses),
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "max_solve_attempts": args.max_solve_attempts,
        "solve_calls": solve_calls,
        "status": "sat" if result is True else ("unsat" if result is False else "unknown"),
    }
    if model:
        positives = {v for v in model if 1 <= v <= len(edges)}
        ok, message = verify_model(edges, positives, args.n, args.forbid_k5)
        model_path = args.out.with_suffix(".model.json")
        model_edges = [list(edges[v - 1]) for v in sorted(positives)]
        model_path.write_text(json.dumps(model_edges, indent=2), encoding="utf-8")
        summary["edge_count"] = len(positives)
        summary["model_path"] = str(model_path)
        summary["model_check"] = "valid" if ok else "invalid"
        summary["model_check_message"] = message

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if result is True else (10 if result is False else 20)


if __name__ == "__main__":
    raise SystemExit(main())
