from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from pysat.solvers import Solver


def var_id(distance: int, color: int, r: int) -> int:
    # distances are 1..floor(n/2)
    return (distance - 1) * r + color + 1


def cyclic_distance(n: int, a: int, b: int) -> int:
    d = abs(a - b) % n
    return min(d, n - d)


def solve_cyclic(r: int, solver_name: str) -> dict:
    n = r * r + 1
    max_d = n // 2
    clauses = []
    for d in range(1, max_d + 1):
        clauses.append([var_id(d, c, r) for c in range(r)])
        for c1, c2 in itertools.combinations(range(r), 2):
            clauses.append([-var_id(d, c1, r), -var_id(d, c2, r)])
    clauses.append([var_id(1, 0, r)])

    coverage = 0
    for S in itertools.combinations(range(n), r + 1):
        dists = sorted({cyclic_distance(n, a, b) for a, b in itertools.combinations(S, 2)})
        for c in range(r):
            clauses.append([var_id(d, c, r) for d in dists])
            coverage += 1

    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        sat = solver.solve()
        model = solver.get_model() if sat else None

    assignment = None
    if model:
        pos = set(v for v in model if v > 0)
        assignment = {
            d: next(c for c in range(r) if var_id(d, c, r) in pos)
            for d in range(1, max_d + 1)
        }

    return {
        "r": r,
        "n": n,
        "family": "cyclic_distance",
        "variables": max_d * r,
        "clauses": len(clauses),
        "coverage_clauses": coverage,
        "status": "sat" if sat else "unsat",
        "assignment": assignment,
    }


def core_var(distance: int, color: int, r: int) -> int:
    return (distance - 1) * r + color + 1


def star_var(vertex: int, color: int, r: int, max_d: int) -> int:
    return max_d * r + vertex * r + color + 1


def solve_cyclic_core_plus_star(r: int, solver_name: str) -> dict:
    old_n = r * r
    max_d = old_n // 2
    clauses = []

    for d in range(1, max_d + 1):
        clauses.append([core_var(d, c, r) for c in range(r)])
        for c1, c2 in itertools.combinations(range(r), 2):
            clauses.append([-core_var(d, c1, r), -core_var(d, c2, r)])
    clauses.append([core_var(1, 0, r)])

    for v in range(old_n):
        clauses.append([star_var(v, c, r, max_d) for c in range(r)])
        for c1, c2 in itertools.combinations(range(r), 2):
            clauses.append([-star_var(v, c1, r, max_d), -star_var(v, c2, r, max_d)])

    coverage = 0
    for S in itertools.combinations(range(old_n), r + 1):
        dists = sorted({cyclic_distance(old_n, a, b) for a, b in itertools.combinations(S, 2)})
        for c in range(r):
            clauses.append([core_var(d, c, r) for d in dists])
            coverage += 1

    for S in itertools.combinations(range(old_n), r):
        dists = sorted({cyclic_distance(old_n, a, b) for a, b in itertools.combinations(S, 2)})
        for c in range(r):
            clause = [core_var(d, c, r) for d in dists]
            clause.extend(star_var(v, c, r, max_d) for v in S)
            clauses.append(clause)
            coverage += 1

    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        sat = solver.solve()
        model = solver.get_model() if sat else None

    assignment = None
    if model:
        pos = set(v for v in model if v > 0)
        assignment = {
            "core": {
                d: next(c for c in range(r) if core_var(d, c, r) in pos)
                for d in range(1, max_d + 1)
            },
            "star": {
                v: next(c for c in range(r) if star_var(v, c, r, max_d) in pos)
                for v in range(old_n)
            },
        }

    return {
        "r": r,
        "n": r * r + 1,
        "family": "cyclic_core_plus_arbitrary_star",
        "variables": max_d * r + old_n * r,
        "clauses": len(clauses),
        "coverage_clauses": coverage,
        "status": "sat" if sat else "unsat",
        "assignment": assignment,
    }


def f5_points() -> list[tuple[int, int]]:
    return [(x, y) for x in range(5) for y in range(5)]


def canonical_diff(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    dx = (b[0] - a[0]) % 5
    dy = (b[1] - a[1]) % 5
    neg = ((-dx) % 5, (-dy) % 5)
    cur = (dx, dy)
    return min(cur, neg)


def diff_var(diff_idx: int, color: int, r: int) -> int:
    return diff_idx * r + color + 1


def f5_star_var(vertex: int, color: int, r: int, diff_count: int) -> int:
    return diff_count * r + vertex * r + color + 1


def solve_f5_cayley_core_plus_star(solver_name: str) -> dict:
    r = 5
    points = f5_points()
    diffs = sorted(
        {
            canonical_diff((0, 0), p)
            for p in points
            if p != (0, 0)
        }
    )
    diff_id = {d: i for i, d in enumerate(diffs)}
    edge_diff = {}
    for i, a in enumerate(points):
        for j in range(i + 1, len(points)):
            edge_diff[(i, j)] = diff_id[canonical_diff(a, points[j])]

    clauses = []
    for did in range(len(diffs)):
        clauses.append([diff_var(did, c, r) for c in range(r)])
        for c1, c2 in itertools.combinations(range(r), 2):
            clauses.append([-diff_var(did, c1, r), -diff_var(did, c2, r)])
    clauses.append([diff_var(0, 0, r)])

    for v in range(len(points)):
        clauses.append([f5_star_var(v, c, r, len(diffs)) for c in range(r)])
        for c1, c2 in itertools.combinations(range(r), 2):
            clauses.append(
                [
                    -f5_star_var(v, c1, r, len(diffs)),
                    -f5_star_var(v, c2, r, len(diffs)),
                ]
            )

    coverage = 0
    for S in itertools.combinations(range(len(points)), r + 1):
        dids = sorted({edge_diff[tuple(sorted((a, b)))] for a, b in itertools.combinations(S, 2)})
        for c in range(r):
            clauses.append([diff_var(d, c, r) for d in dids])
            coverage += 1

    for S in itertools.combinations(range(len(points)), r):
        dids = sorted({edge_diff[tuple(sorted((a, b)))] for a, b in itertools.combinations(S, 2)})
        for c in range(r):
            clause = [diff_var(d, c, r) for d in dids]
            clause.extend(f5_star_var(v, c, r, len(diffs)) for v in S)
            clauses.append(clause)
            coverage += 1

    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        sat = solver.solve()
        model = solver.get_model() if sat else None

    assignment = None
    if model:
        pos = set(v for v in model if v > 0)
        assignment = {
            "diffs": {
                str(diffs[did]): next(c for c in range(r) if diff_var(did, c, r) in pos)
                for did in range(len(diffs))
            },
            "star": {
                v: next(c for c in range(r) if f5_star_var(v, c, r, len(diffs)) in pos)
                for v in range(len(points))
            },
        }

    return {
        "r": r,
        "n": 26,
        "family": "F5^2_cayley_core_plus_arbitrary_star",
        "variables": len(diffs) * r + len(points) * r,
        "diff_pairs": len(diffs),
        "clauses": len(clauses),
        "coverage_clauses": coverage,
        "status": "sat" if sat else "unsat",
        "assignment": assignment,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--family", choices=["cyclic", "cyclic-core-star", "f5-cayley-core-star"], default="cyclic")
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--out", type=Path, default=Path("erdos/617/results/cyclic_r5_summary.json"))
    args = parser.parse_args()
    if args.family == "cyclic":
        result = solve_cyclic(args.r, args.solver)
    elif args.family == "cyclic-core-star":
        result = solve_cyclic_core_plus_star(args.r, args.solver)
    else:
        result = solve_f5_cayley_core_plus_star(args.solver)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "sat" else 1


if __name__ == "__main__":
    raise SystemExit(main())
