from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from types import SimpleNamespace

from pysat.solvers import Solver

import sat_cnf_pipeline as pipe


def partitions_nonincreasing(total: int, parts: int, max_part: int | None = None):
    if parts == 0:
        if total == 0:
            yield ()
        return
    if max_part is None:
        max_part = total
    for x in range(min(max_part, total), -1, -1):
        for rest in partitions_nonincreasing(total - x, parts - 1, x):
            yield (x,) + rest


def star_assumptions(r: int, counts: tuple[int, ...]) -> list[int]:
    n = r * r + 1
    _, edge_id = pipe.make_edges(n)
    assumptions = []
    vertex = 1
    for color, count in enumerate(counts):
        for _ in range(count):
            assumptions.append(pipe.edge_var(edge_id[(0, vertex)], color, r))
            vertex += 1
    assert vertex == n
    return assumptions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--conf-budget", type=int, default=20000)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--out", type=Path, default=Path("erdos/617/results/star_partition_probe.json"))
    args = parser.parse_args()

    ns = SimpleNamespace(r=args.r, mode="full", symmetry="none", seed="none", affine_merge=(0, 1))
    info = pipe.build_info(ns)
    partitions = list(partitions_nonincreasing(args.r * args.r, args.r))
    if args.limit:
        partitions = partitions[: args.limit]

    start = time.perf_counter()
    results = []
    with Solver(name=args.solver) as solver:
        for clause in pipe.iter_clauses(ns):
            solver.add_clause(clause)
        add_seconds = time.perf_counter() - start
        for idx, counts in enumerate(partitions):
            assumptions = star_assumptions(args.r, counts)
            t0 = time.perf_counter()
            if args.conf_budget:
                solver.conf_budget(args.conf_budget)
                sat = solver.solve_limited(assumptions=assumptions)
            else:
                sat = solver.solve(assumptions=assumptions)
            elapsed = time.perf_counter() - t0
            status = "sat" if sat is True else ("unsat" if sat is False else "unknown")
            row = {
                "index": idx,
                "counts": counts,
                "status": status,
                "seconds": round(elapsed, 3),
            }
            results.append(row)
            print(row, flush=True)
            if sat is True:
                break

    summary = {
        "r": args.r,
        "n": args.r * args.r + 1,
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "partitions_tested": len(results),
        "total_partitions": len(list(partitions_nonincreasing(args.r * args.r, args.r))),
        "add_seconds": round(add_seconds, 3),
        "statuses": {s: sum(1 for row in results if row["status"] == s) for s in ["sat", "unsat", "unknown"]},
        "results": results,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "results"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
