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


def build(n: int, clique: int, max_edges: int | None, min_edges: int | None) -> CNF:
    edges, edge_id = edge_list(n)
    cnf = CNF()
    for S in itertools.combinations(range(n), clique):
        evars = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
        # no independent clique-sized set
        cnf.append(evars)
        # no complete clique-sized set
        cnf.append([-v for v in evars])
    top = len(edges)
    lits = list(range(1, len(edges) + 1))
    if max_edges is not None:
        atmost = CardEnc.atmost(lits=lits, bound=max_edges, top_id=top, encoding=EncType.seqcounter)
        cnf.extend(atmost.clauses)
        top = max(top, atmost.nv)
    if min_edges is not None:
        atleast = CardEnc.atleast(lits=lits, bound=min_edges, top_id=top, encoding=EncType.seqcounter)
        cnf.extend(atleast.clauses)
        top = max(top, atleast.nv)
    cnf.nv = max(cnf.nv, top)
    return cnf


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=26)
    parser.add_argument("--clique", type=int, default=6)
    parser.add_argument("--max-edges", type=int, default=65)
    parser.add_argument("--min-edges", type=int, default=None)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--conf-budget", type=int, default=0)
    parser.add_argument("--out", type=Path, default=Path("erdos/617/results/ramsey_26_6_max65_summary.json"))
    args = parser.parse_args()

    cnf = build(args.n, args.clique, args.max_edges, args.min_edges)
    with Solver(name=args.solver, bootstrap_with=cnf.clauses) as solver:
        if args.conf_budget:
            solver.conf_budget(args.conf_budget)
            result = solver.solve_limited()
        else:
            result = solver.solve()
        model = solver.get_model() if result is True else None

    summary = {
        "n": args.n,
        "clique": args.clique,
        "max_edges": args.max_edges,
        "min_edges": args.min_edges,
        "vars": cnf.nv,
        "clauses": len(cnf.clauses),
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "status": "sat" if result is True else ("unsat" if result is False else "unknown"),
    }
    if model:
        positive = {v for v in model if 1 <= v <= args.n * (args.n - 1) // 2}
        summary["edge_count"] = len(positive)
        edges, _ = edge_list(args.n)
        model_edges = [list(edges[v - 1]) for v in sorted(positive)]
        model_path = args.out.with_suffix(".model.json")
        model_path.write_text(json.dumps(model_edges, indent=2), encoding="utf-8")
        summary["model_path"] = str(model_path)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if result is True else (10 if result is False else 20)


if __name__ == "__main__":
    raise SystemExit(main())
