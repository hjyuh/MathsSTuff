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


R = 5
N = 26


def edge_list() -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(N) for j in range(i + 1, N)]
    return edges, {e: idx for idx, e in enumerate(edges)}


def var_id(edge_index: int, color: int) -> int:
    return edge_index * R + color + 1


def parse_profile(text: str) -> tuple[int, int, int, int]:
    try:
        values = tuple(int(part.strip()) for part in text.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("profile must be comma-separated integers") from exc
    if len(values) != 4:
        raise argparse.ArgumentTypeError("profile must have four entries")
    if tuple(sorted(values)) != values:
        raise argparse.ArgumentTypeError("profile must be sorted nondecreasing")
    return values  # type: ignore[return-value]


def residual_profiles(k: int) -> list[tuple[int, int, int, int]]:
    total = 325 - k
    out: list[tuple[int, int, int, int]] = []
    for a in range(k, 86):
        for b in range(a, 86):
            for c in range(b, 86):
                d = total - a - b - c
                if c <= d <= 85:
                    out.append((a, b, c, d))
    return out


def add_exactly_one(cnf: CNF, edge_count: int) -> None:
    for eidx in range(edge_count):
        cnf.append([var_id(eidx, c) for c in range(R)])
        for c1, c2 in itertools.combinations(range(R), 2):
            cnf.append([-var_id(eidx, c1), -var_id(eidx, c2)])


def add_coverage(cnf: CNF, edge_id: dict[tuple[int, int], int]) -> None:
    for S in itertools.combinations(range(N), 6):
        eids = [edge_id[(a, b)] for a, b in itertools.combinations(S, 2)]
        for color in range(R):
            cnf.append([var_id(eidx, color) for eidx in eids])


def add_count_equals(cnf: CNF, edge_count: int, color: int, count: int, top_id: int) -> int:
    lits = [var_id(eidx, color) for eidx in range(edge_count)]
    enc = CardEnc.equals(lits=lits, bound=count, top_id=top_id, encoding=EncType.seqcounter)
    cnf.extend(enc.clauses)
    return max(top_id, enc.nv)


def build_base(fix_min_edge: bool) -> tuple[CNF, list[tuple[int, int]]]:
    edges, edge_id = edge_list()
    cnf = CNF()
    add_exactly_one(cnf, len(edges))
    add_coverage(cnf, edge_id)
    if fix_min_edge:
        cnf.append([var_id(edge_id[(0, 1)], 0)])
    cnf.nv = max(cnf.nv, len(edges) * R)
    return cnf, edges


def add_profile_constraints(cnf: CNF, edge_count: int, k: int, profile: tuple[int, int, int, int]) -> None:
    top = cnf.nv
    top = add_count_equals(cnf, edge_count, 0, k, top)
    for color, count in enumerate(profile, start=1):
        top = add_count_equals(cnf, edge_count, color, count, top)
    cnf.nv = max(cnf.nv, top)


def model_to_rows(model: list[int], edges: list[tuple[int, int]]) -> list[dict[str, object]]:
    positive = {lit for lit in model if lit > 0}
    rows: list[dict[str, object]] = []
    for eidx, edge in enumerate(edges):
        colors = [c for c in range(R) if var_id(eidx, c) in positive]
        if len(colors) != 1:
            raise ValueError(f"edge {edge} has colors {colors}")
        rows.append({"edge": list(edge), "color": colors[0]})
    return rows


def verify_rows(rows: list[dict[str, object]]) -> tuple[bool, str]:
    colors: dict[tuple[int, int], int] = {}
    for row in rows:
        a, b = row["edge"]  # type: ignore[index]
        a = int(a)
        b = int(b)
        if a > b:
            a, b = b, a
        colors[(a, b)] = int(row["color"])
    for S in itertools.combinations(range(N), 6):
        seen = {colors[(a, b)] for a, b in itertools.combinations(S, 2)}
        if len(seen) != R:
            return False, f"bad subset {S}, seen={sorted(seen)}"
    return True, "ok"


def solve_profile(
    base: CNF,
    edges: list[tuple[int, int]],
    k: int,
    profile: tuple[int, int, int, int],
    args: argparse.Namespace,
    profile_index: int,
) -> dict[str, object]:
    cnf = base.copy()
    add_profile_constraints(cnf, len(edges), k, profile)

    started = time.perf_counter()
    with Solver(name=args.solver, bootstrap_with=cnf.clauses) as solver:
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
        seconds = time.perf_counter() - started

        row: dict[str, object] = {
            "profile_index": profile_index,
            "k": k,
            "profile": list(profile),
            "status": "sat" if result is True else ("unsat" if result is False else "unknown"),
            "vars": cnf.nv,
            "clauses": len(cnf.clauses),
            "solver": args.solver,
            "conf_budget": args.conf_budget,
            "max_seconds": args.max_seconds,
            "interrupted_by_wall_clock": interrupted_by_wall_clock,
            "seconds": round(seconds, 3),
        }
        if result is True:
            rows = model_to_rows(solver.get_model(), edges)
            ok, message = verify_rows(rows)
            model_path = args.out.with_suffix(f".k{k}.p{profile_index}.model.json")
            model_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
            row["model_path"] = str(model_path)
            row["model_check"] = "valid" if ok else "invalid"
            row["model_check_message"] = message
        return row


def main() -> int:
    parser = argparse.ArgumentParser(description="Minimum-colour profile SAT branches for EP617 r=5.")
    parser.add_argument("--k", type=int, default=65, help="exact size of minimum colour 0")
    parser.add_argument("--profile", type=parse_profile, default=None, help="exact sorted residual profile")
    parser.add_argument("--max-profiles", type=int, default=1)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--conf-budget", type=int, default=500000)
    parser.add_argument("--max-seconds", type=float, default=0.0, help="per-profile wall-clock limit; 0 disables")
    parser.add_argument("--no-fix-min-edge", action="store_true")
    parser.add_argument("--out", type=Path, default=Path("erdos/617/results/mincolor_profile.json"))
    args = parser.parse_args()

    if not 60 <= args.k <= 65:
        raise SystemExit("--k must be in [60,65]")

    profiles = [args.profile] if args.profile is not None else residual_profiles(args.k)
    profiles = profiles[args.offset :]
    if args.max_profiles > 0:
        profiles = profiles[: args.max_profiles]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    base_started = time.perf_counter()
    base, edges = build_base(fix_min_edge=not args.no_fix_min_edge)
    base_seconds = time.perf_counter() - base_started

    rows = []
    for local_index, profile in enumerate(profiles, start=args.offset):
        row = solve_profile(base, edges, args.k, profile, args, local_index)
        rows.append(row)
        print(json.dumps(row), flush=True)
        if row["status"] == "sat":
            break

    counts = {"sat": 0, "unsat": 0, "unknown": 0}
    for row in rows:
        counts[str(row["status"])] += 1
    summary = {
        "k": args.k,
        "profile": list(args.profile) if args.profile is not None else None,
        "offset": args.offset,
        "requested_profiles": args.max_profiles,
        "run_profiles": len(rows),
        "available_profiles_for_k": len(residual_profiles(args.k)),
        "counts": counts,
        "base_vars": base.nv,
        "base_clauses": len(base.clauses),
        "base_seconds": round(base_seconds, 3),
        "solver": args.solver,
        "conf_budget": args.conf_budget,
        "max_seconds": args.max_seconds,
        "rows": rows,
    }
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    if counts["sat"]:
        return 10
    if counts["unknown"]:
        return 20
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
