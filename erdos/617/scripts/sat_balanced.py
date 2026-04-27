from __future__ import annotations

import argparse
import itertools
import json
import time
from pathlib import Path

from pysat.formula import CNF
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver


def edge_list(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def var_id(edge_index: int, color: int, r: int) -> int:
    return edge_index * r + color + 1


def build_cnf(r: int, fix_first_edge: bool = True) -> tuple[CNF, list[tuple[int, int]]]:
    n = r * r + 1
    edges = edge_list(n)
    edge_id = {e: idx for idx, e in enumerate(edges)}
    cnf = CNF()

    # Each edge gets exactly one color.
    for eidx in range(len(edges)):
        cnf.append([var_id(eidx, c, r) for c in range(r)])
        for c1 in range(r):
            for c2 in range(c1 + 1, r):
                cnf.append([-var_id(eidx, c1, r), -var_id(eidx, c2, r)])

    # Color symmetry: some edge may be renamed to color 0.
    if fix_first_edge:
        cnf.append([var_id(0, 0, r)])

    # Every (r+1)-vertex set must see every color.
    for S in itertools.combinations(range(n), r + 1):
        eids = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
        for c in range(r):
            cnf.append([var_id(eidx, c, r) for eidx in eids])
    return cnf, edges


def add_edge_count_bounds(cnf: CNF, r: int, edge_count: int) -> None:
    # For r=5, use the sharpened Kang-Pikhurko + K5-star bound:
    # every colour class in a valid K_26 colouring has 60..85 edges.
    if r == 5:
        lower = 60
    else:
        lower = r * (r * r - r + 2) // 2 + 1
    upper = edge_count - (r - 1) * lower
    top_id = cnf.nv
    for c in range(r):
        lits = [var_id(eidx, c, r) for eidx in range(edge_count)]
        atleast = CardEnc.atleast(lits=lits, bound=lower, top_id=top_id, encoding=EncType.seqcounter)
        cnf.extend(atleast.clauses)
        top_id = max(top_id, atleast.nv)
        atmost = CardEnc.atmost(lits=lits, bound=upper, top_id=top_id, encoding=EncType.seqcounter)
        cnf.extend(atmost.clauses)
        top_id = max(top_id, atmost.nv)
    cnf.nv = max(cnf.nv, top_id)


def model_to_coloring(model: list[int], edges: list[tuple[int, int]], r: int) -> list[dict]:
    positive = set(v for v in model if v > 0)
    rows = []
    for eidx, edge in enumerate(edges):
        cols = [c for c in range(r) if var_id(eidx, c, r) in positive]
        if len(cols) != 1:
            raise ValueError(f"edge {edge} has colors {cols}")
        rows.append({"edge": list(edge), "color": cols[0]})
    return rows


def check_coloring(rows: list[dict], r: int) -> tuple[bool, str]:
    n = r * r + 1
    colors = {}
    for row in rows:
        a, b = row["edge"]
        if a > b:
            a, b = b, a
        colors[(a, b)] = row["color"]
    for S in itertools.combinations(range(n), r + 1):
        seen = set()
        for a, b in itertools.combinations(S, 2):
            if a > b:
                a, b = b, a
            seen.add(colors[(a, b)])
        if len(seen) < r:
            return False, f"bad subset {S}, seen={sorted(seen)}"
    return True, "ok"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--conf-budget", type=int, default=0)
    parser.add_argument("--prop-budget", type=int, default=0)
    parser.add_argument("--edge-count-bounds", action="store_true")
    parser.add_argument("--no-fix-first-edge", action="store_true")
    parser.add_argument("--out-dir", type=Path, default=Path("erdos/617/results"))
    args = parser.parse_args()

    start = time.time()
    cnf, edges = build_cnf(args.r, fix_first_edge=not args.no_fix_first_edge)
    if args.edge_count_bounds:
        add_edge_count_bounds(cnf, args.r, len(edges))
    build_time = time.time() - start
    print(
        json.dumps(
            {
                "phase": "built",
                "r": args.r,
                "n": args.r * args.r + 1,
                "vars": cnf.nv,
                "clauses": len(cnf.clauses),
                "build_seconds": build_time,
            },
            indent=2,
        ),
        flush=True,
    )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    cnf_path = args.out_dir / f"balanced_r{args.r}.cnf"
    cnf.to_file(str(cnf_path))

    with Solver(name=args.solver, bootstrap_with=cnf.clauses) as solver:
        if args.conf_budget:
            solver.conf_budget(args.conf_budget)
        if args.prop_budget:
            solver.prop_budget(args.prop_budget)
        solve_start = time.time()
        if args.conf_budget or args.prop_budget:
            sat = solver.solve_limited(expect_interrupt=True)
        else:
            sat = solver.solve()
        solve_seconds = time.time() - solve_start
        summary = {
            "r": args.r,
            "solver": args.solver,
            "sat": sat,
            "solve_seconds": solve_seconds,
            "vars": cnf.nv,
            "clauses": len(cnf.clauses),
            "cnf": str(cnf_path),
        }
        if sat is True:
            rows = model_to_coloring(solver.get_model(), edges, args.r)
            ok, message = check_coloring(rows, args.r)
            summary["checked"] = ok
            summary["check_message"] = message
            coloring_path = args.out_dir / f"balanced_r{args.r}_model.json"
            coloring_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
            summary["model"] = str(coloring_path)
        summary_path = args.out_dir / f"balanced_r{args.r}_sat_summary.json"
        summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(json.dumps(summary, indent=2), flush=True)
        return 0 if sat is True else (10 if sat is False else 20)


if __name__ == "__main__":
    raise SystemExit(main())
