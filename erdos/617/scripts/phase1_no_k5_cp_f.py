from __future__ import annotations

import argparse
import itertools
import json
import os
import platform
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


def _utc_now_compact() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _import_probe(modname: str) -> dict[str, Any]:
    try:
        mod = __import__(modname)
        ver = getattr(mod, "__version__", None)
        if modname == "z3":
            try:
                # z3-solver doesn't always expose __version__.
                ver = getattr(mod, "get_version_string")()
            except Exception:
                pass
        return {"module": modname, "ok": True, "version": ver}
    except Exception as e:
        return {"module": modname, "ok": False, "error": f"{type(e).__name__}: {e}"}


def probe_environment() -> dict[str, Any]:
    out: dict[str, Any] = {
        "timestamp_utc": _utc_now_compact(),
        "python": sys.version,
        "executable": sys.executable,
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
        },
        "cwd": os.getcwd(),
        "modules": {},
    }
    for name in ["ortools", "z3", "pulp", "scipy"]:
        out["modules"][name] = _import_probe(name)

    # Extra per-module details.
    try:
        import pulp  # type: ignore

        out["modules"]["pulp"]["available_solvers"] = pulp.listSolvers(onlyAvailable=True)
    except Exception:
        pass
    return out


def edge_indices(n: int) -> list[list[int]]:
    """Return an n x n matrix mapping (i,j) to edge variable index in [0,m)."""
    idx = [[-1] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            idx[i][j] = k
            idx[j][i] = k
            k += 1
    return idx


def iter_edge_idxs_for_vertices(verts: tuple[int, ...], eidx: list[list[int]]) -> list[int]:
    out: list[int] = []
    m = len(verts)
    for a_pos in range(m):
        a = verts[a_pos]
        row = eidx[a]
        for b_pos in range(a_pos + 1, m):
            b = verts[b_pos]
            out.append(row[b])
    return out


def solution_edge_count(sol: list[int]) -> int:
    return int(sum(sol))


def find_k_clique_violation(
    sol: list[int],
    n: int,
    k: int,
    max_hits: int,
) -> list[tuple[int, ...]]:
    if k <= 1:
        return []
    eidx = edge_indices(n)
    hits: list[tuple[int, ...]] = []
    for Q in itertools.combinations(range(n), k):
        ok = True
        for a, b in itertools.combinations(Q, 2):
            if sol[eidx[a][b]] == 0:
                ok = False
                break
        if ok:
            hits.append(Q)
            if len(hits) >= max_hits:
                return hits
    return hits


def find_subset_sum_violations(
    sol: list[int],
    n: int,
    subset_size: int,
    lower: int | None,
    upper: int | None,
    max_hits: int,
) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    """Return (too_low, too_high) vertex subsets violating sum bounds over induced edges."""
    eidx = edge_indices(n)
    too_low: list[tuple[int, ...]] = []
    too_high: list[tuple[int, ...]] = []

    for S in itertools.combinations(range(n), subset_size):
        s = 0
        verts = list(S)
        for i in range(subset_size):
            ai = verts[i]
            row = eidx[ai]
            for j in range(i + 1, subset_size):
                s += sol[row[verts[j]]]
                if upper is not None and s > upper:
                    break
            if upper is not None and s > upper:
                break

        if lower is not None and s < lower:
            too_low.append(S)
        if upper is not None and s > upper:
            too_high.append(S)
        if len(too_low) + len(too_high) >= max_hits:
            break
    return too_low, too_high


def verify_no_k_clique(sol: list[int], n: int, k: int) -> tuple[bool, str]:
    bad = find_k_clique_violation(sol, n, k, max_hits=1)
    if bad:
        return False, f"found K_{k} on vertices {bad[0]}"
    return True, "ok"


def verify_subset_bounds(
    sol: list[int],
    n: int,
    subset_size: int,
    lower: int | None,
    upper: int | None,
) -> tuple[bool, str]:
    low, high = find_subset_sum_violations(sol, n, subset_size, lower, upper, max_hits=1)
    if low:
        return False, f"subset {low[0]} has induced edge count below {lower}"
    if high:
        return False, f"subset {high[0]} has induced edge count above {upper}"
    return True, "ok"


def verify_global_edges(sol: list[int], min_edges: int, max_edges: int) -> tuple[bool, str]:
    m = solution_edge_count(sol)
    if m < min_edges:
        return False, f"edge_count={m} < min_edges={min_edges}"
    if m > max_edges:
        return False, f"edge_count={m} > max_edges={max_edges}"
    return True, "ok"


def verify_solution(
    sol: list[int],
    n: int,
    min_edges: int,
    max_edges: int,
    subset_size: int,
    subset_lb: int | None,
    subset_ub: int | None,
    forbid_clique_k: int | None,
) -> tuple[bool, str]:
    ok, msg = verify_global_edges(sol, min_edges, max_edges)
    if not ok:
        return ok, msg
    ok, msg = verify_subset_bounds(sol, n, subset_size, subset_lb, subset_ub)
    if not ok:
        return ok, msg
    if forbid_clique_k is not None:
        ok, msg = verify_no_k_clique(sol, n, forbid_clique_k)
        if not ok:
            return ok, msg
    return True, "ok"


@dataclass
class SolveSummary:
    backend: str
    mode: str
    n: int
    min_edges: int
    max_edges: int
    subset_size: int
    subset_lb: int | None
    subset_ub: int | None
    forbid_clique_k: int | None
    time_limit_s: float

    status: str
    wall_s: float
    iterations: int
    constraints_added: int
    notes: dict[str, Any]
    edge_count: int | None = None
    model_path: str | None = None
    model_check: str | None = None
    model_check_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "timestamp_utc": _utc_now_compact(),
            "backend": self.backend,
            "mode": self.mode,
            "n": self.n,
            "min_edges": self.min_edges,
            "max_edges": self.max_edges,
            "subset_size": self.subset_size,
            "subset_lb": self.subset_lb,
            "subset_ub": self.subset_ub,
            "forbid_clique_k": self.forbid_clique_k,
            "time_limit_s": self.time_limit_s,
            "status": self.status,
            "wall_s": self.wall_s,
            "iterations": self.iterations,
            "constraints_added": self.constraints_added,
            "edge_count": self.edge_count,
            "model_path": self.model_path,
            "model_check": self.model_check,
            "model_check_message": self.model_check_message,
            "notes": self.notes,
        }


def _write_model_edges(
    out_prefix: Path,
    sol: list[int],
    n: int,
) -> Path:
    eidx = edge_indices(n)
    edges: list[list[int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if sol[eidx[i][j]] == 1:
                edges.append([i, j])
    p = out_prefix.with_suffix(".model_edges.json")
    p.write_text(json.dumps(edges, indent=2), encoding="utf-8")
    return p


def solve_z3(
    *,
    n: int,
    min_edges: int,
    max_edges: int,
    subset_size: int,
    subset_lb: int | None,
    subset_ub: int | None,
    forbid_clique_k: int | None,
    mode: str,
    time_limit_s: float,
    max_round_violations: int,
    out_prefix: Path,
) -> SolveSummary:
    try:
        import z3  # type: ignore
    except Exception as e:
        return SolveSummary(
            backend="z3",
            mode=mode,
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
            time_limit_s=time_limit_s,
            status="missing",
            wall_s=0.0,
            iterations=0,
            constraints_added=0,
            notes={"error": f"{type(e).__name__}: {e}"},
        )

    eidx = edge_indices(n)
    m = eidx[n - 2][n - 1] + 1 if n >= 2 else 0
    x = [z3.Bool(f"e_{i}") for i in range(m)]

    s = z3.Solver()

    added = 0
    iterations = 0
    start = time.time()

    # Global edges in range.
    total = z3.PbSum([(x[i], 1) for i in range(m)])
    s.add(total >= min_edges, total <= max_edges)
    added += 2

    def add_k_clique_cut(Q: tuple[int, ...]) -> int:
        # sum(edges in Q) <= C(k,2)-1
        idxs = iter_edge_idxs_for_vertices(Q, eidx)
        s.add(z3.PbLe([(x[i], 1) for i in idxs], len(idxs) - 1))
        return 1

    def add_subset_lb_cut(S: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(S, eidx)
        s.add(z3.PbGe([(x[i], 1) for i in idxs], int(subset_lb)))
        return 1

    def add_subset_ub_cut(S: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(S, eidx)
        s.add(z3.PbLe([(x[i], 1) for i in idxs], int(subset_ub)))
        return 1

    if mode == "full":
        # Add all constraints upfront.
        if forbid_clique_k is not None:
            for Q in itertools.combinations(range(n), forbid_clique_k):
                added += add_k_clique_cut(Q)
                if time.time() - start >= time_limit_s:
                    return SolveSummary(
                        backend="z3",
                        mode=mode,
                        n=n,
                        min_edges=min_edges,
                        max_edges=max_edges,
                        subset_size=subset_size,
                        subset_lb=subset_lb,
                        subset_ub=subset_ub,
                        forbid_clique_k=forbid_clique_k,
                        time_limit_s=time_limit_s,
                        status="unknown",
                        wall_s=time.time() - start,
                        iterations=iterations,
                        constraints_added=added,
                        notes={"reason": "build_time_exceeded", "phase": "k_clique"},
                    )
        if subset_lb is not None or subset_ub is not None:
            lo = subset_lb if subset_lb is not None else -sys.maxsize
            hi = subset_ub if subset_ub is not None else sys.maxsize
            for S in itertools.combinations(range(n), subset_size):
                idxs = iter_edge_idxs_for_vertices(S, eidx)
                if subset_lb is not None:
                    s.add(z3.PbGe([(x[i], 1) for i in idxs], int(lo)))
                    added += 1
                if subset_ub is not None:
                    s.add(z3.PbLe([(x[i], 1) for i in idxs], int(hi)))
                    added += 1
                if time.time() - start >= time_limit_s:
                    return SolveSummary(
                        backend="z3",
                        mode=mode,
                        n=n,
                        min_edges=min_edges,
                        max_edges=max_edges,
                        subset_size=subset_size,
                        subset_lb=subset_lb,
                        subset_ub=subset_ub,
                        forbid_clique_k=forbid_clique_k,
                        time_limit_s=time_limit_s,
                        status="unknown",
                        wall_s=time.time() - start,
                        iterations=iterations,
                        constraints_added=added,
                        notes={"reason": "build_time_exceeded", "phase": "subset_constraints"},
                    )

    while True:
        iterations += 1
        remaining_ms = max(1, int((time_limit_s - (time.time() - start)) * 1000))
        s.set(timeout=remaining_ms)

        r = s.check()
        if r == z3.unknown:
            wall = time.time() - start
            return SolveSummary(
                backend="z3",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unknown",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"reason_unknown": s.reason_unknown()},
            )
        if r == z3.unsat:
            wall = time.time() - start
            return SolveSummary(
                backend="z3",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unsat",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={},
            )

        model = s.model()
        sol = [1 if z3.is_true(model.eval(x[i], model_completion=True)) else 0 for i in range(m)]

        if mode == "full":
            ok, msg = verify_solution(
                sol,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
            )
            wall = time.time() - start
            ss = SolveSummary(
                backend="z3",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="sat",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={},
                edge_count=solution_edge_count(sol),
            )
            model_path = _write_model_edges(out_prefix, sol, n)
            ss.model_path = str(model_path)
            ss.model_check = "valid" if ok else "invalid"
            ss.model_check_message = msg
            return ss

        # lazy: find violated constraints and add.
        cuts = 0
        if forbid_clique_k is not None:
            bad_cliques = find_k_clique_violation(sol, n, forbid_clique_k, max_hits=max_round_violations)
            for Q in bad_cliques:
                cuts += add_k_clique_cut(Q)
                if cuts >= max_round_violations:
                    break

        if cuts < max_round_violations and (subset_lb is not None or subset_ub is not None):
            low, high = find_subset_sum_violations(
                sol,
                n,
                subset_size,
                subset_lb,
                subset_ub,
                max_hits=max_round_violations - cuts,
            )
            for S in low:
                cuts += add_subset_lb_cut(S)
                if cuts >= max_round_violations:
                    break
            for S in high:
                if cuts >= max_round_violations:
                    break
                cuts += add_subset_ub_cut(S)

        if cuts == 0:
            ok, msg = verify_solution(
                sol,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
            )
            wall = time.time() - start
            ss = SolveSummary(
                backend="z3",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="sat",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"lazy": True},
                edge_count=solution_edge_count(sol),
            )
            model_path = _write_model_edges(out_prefix, sol, n)
            ss.model_path = str(model_path)
            ss.model_check = "valid" if ok else "invalid"
            ss.model_check_message = msg
            return ss

        added += cuts
        if time.time() - start >= time_limit_s:
            wall = time.time() - start
            return SolveSummary(
                backend="z3",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unknown",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"reason": "time_limit_exceeded"},
            )


def solve_ortools(
    *,
    n: int,
    min_edges: int,
    max_edges: int,
    subset_size: int,
    subset_lb: int | None,
    subset_ub: int | None,
    forbid_clique_k: int | None,
    mode: str,
    time_limit_s: float,
    max_round_violations: int,
    out_prefix: Path,
    workers: int,
) -> SolveSummary:
    try:
        from ortools.sat.python import cp_model  # type: ignore
    except Exception as e:
        return SolveSummary(
            backend="ortools",
            mode=mode,
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
            time_limit_s=time_limit_s,
            status="missing",
            wall_s=0.0,
            iterations=0,
            constraints_added=0,
            notes={"error": f"{type(e).__name__}: {e}"},
        )

    eidx = edge_indices(n)
    m = eidx[n - 2][n - 1] + 1 if n >= 2 else 0

    model = cp_model.CpModel()
    x = [model.new_bool_var(f"e_{i}") for i in range(m)]

    added = 0
    iterations = 0
    start = time.time()

    total = sum(x)
    model.add(total >= min_edges)
    model.add(total <= max_edges)
    added += 2

    def add_k_clique_cut(Q: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(Q, eidx)
        model.add(sum(x[i] for i in idxs) <= len(idxs) - 1)
        return 1

    def add_subset_lb_cut(S: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(S, eidx)
        model.add(sum(x[i] for i in idxs) >= int(subset_lb))
        return 1

    def add_subset_ub_cut(S: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(S, eidx)
        model.add(sum(x[i] for i in idxs) <= int(subset_ub))
        return 1

    if mode == "full":
        # Add all constraints upfront; abort if we spend the whole budget just building.
        if forbid_clique_k is not None:
            for Q in itertools.combinations(range(n), forbid_clique_k):
                added += add_k_clique_cut(Q)
                if time.time() - start >= time_limit_s:
                    wall = time.time() - start
                    return SolveSummary(
                        backend="ortools",
                        mode=mode,
                        n=n,
                        min_edges=min_edges,
                        max_edges=max_edges,
                        subset_size=subset_size,
                        subset_lb=subset_lb,
                        subset_ub=subset_ub,
                        forbid_clique_k=forbid_clique_k,
                        time_limit_s=time_limit_s,
                        status="unknown",
                        wall_s=wall,
                        iterations=iterations,
                        constraints_added=added,
                        notes={"reason": "build_time_exceeded", "phase": "k_clique"},
                    )

        if subset_lb is not None or subset_ub is not None:
            for S in itertools.combinations(range(n), subset_size):
                idxs = iter_edge_idxs_for_vertices(S, eidx)
                if subset_lb is not None:
                    model.add(sum(x[i] for i in idxs) >= int(subset_lb))
                    added += 1
                if subset_ub is not None:
                    model.add(sum(x[i] for i in idxs) <= int(subset_ub))
                    added += 1
                if time.time() - start >= time_limit_s:
                    wall = time.time() - start
                    return SolveSummary(
                        backend="ortools",
                        mode=mode,
                        n=n,
                        min_edges=min_edges,
                        max_edges=max_edges,
                        subset_size=subset_size,
                        subset_lb=subset_lb,
                        subset_ub=subset_ub,
                        forbid_clique_k=forbid_clique_k,
                        time_limit_s=time_limit_s,
                        status="unknown",
                        wall_s=wall,
                        iterations=iterations,
                        constraints_added=added,
                        notes={"reason": "build_time_exceeded", "phase": "subset_constraints"},
                    )

    while True:
        iterations += 1
        remaining = max(0.001, time_limit_s - (time.time() - start))
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = remaining
        if workers >= 1:
            solver.parameters.num_search_workers = workers

        status = solver.solve(model)
        if status in (cp_model.INFEASIBLE, cp_model.MODEL_INVALID):
            wall = time.time() - start
            return SolveSummary(
                backend="ortools",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unsat" if status == cp_model.INFEASIBLE else "invalid",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"ortools_status": int(status)},
            )
        if status == cp_model.UNKNOWN:
            wall = time.time() - start
            return SolveSummary(
                backend="ortools",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unknown",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"ortools_status": int(status)},
            )

        sol = [1 if solver.boolean_value(x[i]) else 0 for i in range(m)]

        if mode == "full":
            ok, msg = verify_solution(
                sol,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
            )
            wall = time.time() - start
            ss = SolveSummary(
                backend="ortools",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="sat",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"ortools_status": int(status)},
                edge_count=solution_edge_count(sol),
            )
            model_path = _write_model_edges(out_prefix, sol, n)
            ss.model_path = str(model_path)
            ss.model_check = "valid" if ok else "invalid"
            ss.model_check_message = msg
            ss.notes["ortools_stats"] = {
                "wall_time": solver.wall_time(),
                "num_branches": solver.num_branches(),
                "num_conflicts": solver.num_conflicts(),
            }
            return ss

        cuts = 0
        if forbid_clique_k is not None:
            bad_cliques = find_k_clique_violation(sol, n, forbid_clique_k, max_hits=max_round_violations)
            for Q in bad_cliques:
                cuts += add_k_clique_cut(Q)
                if cuts >= max_round_violations:
                    break

        if cuts < max_round_violations and (subset_lb is not None or subset_ub is not None):
            low, high = find_subset_sum_violations(
                sol,
                n,
                subset_size,
                subset_lb,
                subset_ub,
                max_hits=max_round_violations - cuts,
            )
            for S in low:
                cuts += add_subset_lb_cut(S)
                if cuts >= max_round_violations:
                    break
            for S in high:
                if cuts >= max_round_violations:
                    break
                cuts += add_subset_ub_cut(S)

        if cuts == 0:
            ok, msg = verify_solution(
                sol,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
            )
            wall = time.time() - start
            ss = SolveSummary(
                backend="ortools",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="sat",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"lazy": True},
                edge_count=solution_edge_count(sol),
            )
            model_path = _write_model_edges(out_prefix, sol, n)
            ss.model_path = str(model_path)
            ss.model_check = "valid" if ok else "invalid"
            ss.model_check_message = msg
            ss.notes["ortools_stats"] = {
                "wall_time": solver.wall_time(),
                "num_branches": solver.num_branches(),
                "num_conflicts": solver.num_conflicts(),
            }
            return ss

        added += cuts
        if time.time() - start >= time_limit_s:
            wall = time.time() - start
            return SolveSummary(
                backend="ortools",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unknown",
                wall_s=wall,
                iterations=iterations,
                constraints_added=added,
                notes={"reason": "time_limit_exceeded"},
            )


def solve_pulp(
    *,
    n: int,
    min_edges: int,
    max_edges: int,
    subset_size: int,
    subset_lb: int | None,
    subset_ub: int | None,
    forbid_clique_k: int | None,
    mode: str,
    time_limit_s: float,
    max_round_violations: int,
    out_prefix: Path,
) -> SolveSummary:
    try:
        import pulp  # type: ignore
    except Exception as e:
        return SolveSummary(
            backend="pulp",
            mode=mode,
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
            time_limit_s=time_limit_s,
            status="missing",
            wall_s=0.0,
            iterations=0,
            constraints_added=0,
            notes={"error": f"{type(e).__name__}: {e}"},
        )

    eidx = edge_indices(n)
    m = eidx[n - 2][n - 1] + 1 if n >= 2 else 0

    prob = pulp.LpProblem("phase1_no_k5", pulp.LpMinimize)
    x = [pulp.LpVariable(f"e_{i}", lowBound=0, upBound=1, cat=pulp.LpBinary) for i in range(m)]
    prob += 0  # dummy objective

    prob += pulp.lpSum(x) >= min_edges
    prob += pulp.lpSum(x) <= max_edges
    added = 2

    iterations = 0
    start = time.time()

    def extract_sol() -> list[int]:
        out: list[int] = []
        for v in x:
            val = pulp.value(v)
            out.append(1 if val is not None and val >= 0.5 else 0)
        return out

    def add_k_clique_cut(Q: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(Q, eidx)
        prob += pulp.lpSum(x[i] for i in idxs) <= len(idxs) - 1
        return 1

    def add_subset_lb_cut(S: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(S, eidx)
        prob += pulp.lpSum(x[i] for i in idxs) >= int(subset_lb)
        return 1

    def add_subset_ub_cut(S: tuple[int, ...]) -> int:
        idxs = iter_edge_idxs_for_vertices(S, eidx)
        prob += pulp.lpSum(x[i] for i in idxs) <= int(subset_ub)
        return 1

    if mode == "full":
        if forbid_clique_k is not None:
            for Q in itertools.combinations(range(n), forbid_clique_k):
                added += add_k_clique_cut(Q)
                if time.time() - start >= time_limit_s:
                    return SolveSummary(
                        backend="pulp",
                        mode=mode,
                        n=n,
                        min_edges=min_edges,
                        max_edges=max_edges,
                        subset_size=subset_size,
                        subset_lb=subset_lb,
                        subset_ub=subset_ub,
                        forbid_clique_k=forbid_clique_k,
                        time_limit_s=time_limit_s,
                        status="unknown",
                        wall_s=time.time() - start,
                        iterations=iterations,
                        constraints_added=added,
                        notes={"reason": "build_time_exceeded", "phase": "k_clique"},
                    )
        if subset_lb is not None or subset_ub is not None:
            for S in itertools.combinations(range(n), subset_size):
                idxs = iter_edge_idxs_for_vertices(S, eidx)
                if subset_lb is not None:
                    prob += pulp.lpSum(x[i] for i in idxs) >= int(subset_lb)
                    added += 1
                if subset_ub is not None:
                    prob += pulp.lpSum(x[i] for i in idxs) <= int(subset_ub)
                    added += 1
                if time.time() - start >= time_limit_s:
                    return SolveSummary(
                        backend="pulp",
                        mode=mode,
                        n=n,
                        min_edges=min_edges,
                        max_edges=max_edges,
                        subset_size=subset_size,
                        subset_lb=subset_lb,
                        subset_ub=subset_ub,
                        forbid_clique_k=forbid_clique_k,
                        time_limit_s=time_limit_s,
                        status="unknown",
                        wall_s=time.time() - start,
                        iterations=iterations,
                        constraints_added=added,
                        notes={"reason": "build_time_exceeded", "phase": "subset_constraints"},
                    )

    while True:
        iterations += 1
        remaining = max(0.0, time_limit_s - (time.time() - start))
        solver = pulp.PULP_CBC_CMD(msg=False, timeLimit=max(1, int(remaining)))
        prob.solve(solver)
        st = pulp.LpStatus.get(prob.status, "unknown")
        if st == "Infeasible":
            return SolveSummary(
                backend="pulp",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unsat",
                wall_s=time.time() - start,
                iterations=iterations,
                constraints_added=added,
                notes={"cbc_status": st},
            )
        if st not in ("Optimal", "Not Solved"):
            return SolveSummary(
                backend="pulp",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unknown",
                wall_s=time.time() - start,
                iterations=iterations,
                constraints_added=added,
                notes={"cbc_status": st},
            )
        if st == "Not Solved":
            return SolveSummary(
                backend="pulp",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unknown",
                wall_s=time.time() - start,
                iterations=iterations,
                constraints_added=added,
                notes={"cbc_status": st, "reason": "time_limit_or_stopped"},
            )

        sol = extract_sol()
        if mode == "full":
            ok, msg = verify_solution(
                sol,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
            )
            ss = SolveSummary(
                backend="pulp",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="sat",
                wall_s=time.time() - start,
                iterations=iterations,
                constraints_added=added,
                notes={"cbc_status": st},
                edge_count=solution_edge_count(sol),
            )
            model_path = _write_model_edges(out_prefix, sol, n)
            ss.model_path = str(model_path)
            ss.model_check = "valid" if ok else "invalid"
            ss.model_check_message = msg
            return ss

        cuts = 0
        if forbid_clique_k is not None:
            bad = find_k_clique_violation(sol, n, forbid_clique_k, max_hits=max_round_violations)
            for Q in bad:
                cuts += add_k_clique_cut(Q)
                if cuts >= max_round_violations:
                    break

        if cuts < max_round_violations and (subset_lb is not None or subset_ub is not None):
            low, high = find_subset_sum_violations(
                sol,
                n,
                subset_size,
                subset_lb,
                subset_ub,
                max_hits=max_round_violations - cuts,
            )
            for S in low:
                cuts += add_subset_lb_cut(S)
                if cuts >= max_round_violations:
                    break
            for S in high:
                if cuts >= max_round_violations:
                    break
                cuts += add_subset_ub_cut(S)

        if cuts == 0:
            ok, msg = verify_solution(
                sol,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
            )
            ss = SolveSummary(
                backend="pulp",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="sat",
                wall_s=time.time() - start,
                iterations=iterations,
                constraints_added=added,
                notes={"cbc_status": st, "lazy": True},
                edge_count=solution_edge_count(sol),
            )
            model_path = _write_model_edges(out_prefix, sol, n)
            ss.model_path = str(model_path)
            ss.model_check = "valid" if ok else "invalid"
            ss.model_check_message = msg
            return ss

        added += cuts
        if time.time() - start >= time_limit_s:
            return SolveSummary(
                backend="pulp",
                mode=mode,
                n=n,
                min_edges=min_edges,
                max_edges=max_edges,
                subset_size=subset_size,
                subset_lb=subset_lb,
                subset_ub=subset_ub,
                forbid_clique_k=forbid_clique_k,
                time_limit_s=time_limit_s,
                status="unknown",
                wall_s=time.time() - start,
                iterations=iterations,
                constraints_added=added,
                notes={"reason": "time_limit_exceeded"},
            )


def solve_scipy_milp(
    *,
    n: int,
    min_edges: int,
    max_edges: int,
    subset_size: int,
    subset_lb: int | None,
    subset_ub: int | None,
    forbid_clique_k: int | None,
    time_limit_s: float,
    out_prefix: Path,
) -> SolveSummary:
    try:
        import numpy as np
        from scipy.optimize import LinearConstraint, milp  # type: ignore
        from scipy.sparse import coo_matrix  # type: ignore
    except Exception as e:
        return SolveSummary(
            backend="scipy",
            mode="full",
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
            time_limit_s=time_limit_s,
            status="missing",
            wall_s=0.0,
            iterations=0,
            constraints_added=0,
            notes={"error": f"{type(e).__name__}: {e}"},
        )

    if subset_lb is None and subset_ub is None and forbid_clique_k is None:
        return SolveSummary(
            backend="scipy",
            mode="full",
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
            time_limit_s=time_limit_s,
            status="invalid",
            wall_s=0.0,
            iterations=0,
            constraints_added=0,
            notes={"error": "no constraints besides global edges; refuse"},
        )

    try:
        eidx = edge_indices(n)
        m = eidx[n - 2][n - 1] + 1 if n >= 2 else 0

        # Build constraints in sparse row form.
        row_idx: list[int] = []
        col_idx: list[int] = []
        data: list[float] = []
        lower: list[float] = []
        upper: list[float] = []

        row = 0

        def add_row(idxs: Iterable[int], lo: float, hi: float) -> None:
            nonlocal row
            for c in idxs:
                row_idx.append(row)
                col_idx.append(c)
                data.append(1.0)
            lower.append(lo)
            upper.append(hi)
            row += 1

        # Global edges.
        add_row(range(m), float(min_edges), float(max_edges))

        if forbid_clique_k is not None:
            for Q in itertools.combinations(range(n), forbid_clique_k):
                idxs = iter_edge_idxs_for_vertices(Q, eidx)
                add_row(idxs, -np.inf, float(len(idxs) - 1))

        if subset_lb is not None or subset_ub is not None:
            lo = float(subset_lb) if subset_lb is not None else -np.inf
            hi = float(subset_ub) if subset_ub is not None else np.inf
            for S in itertools.combinations(range(n), subset_size):
                idxs = iter_edge_idxs_for_vertices(S, eidx)
                add_row(idxs, lo, hi)

        A = coo_matrix((np.array(data), (np.array(row_idx), np.array(col_idx))), shape=(row, m)).tocsr()
        cons = LinearConstraint(A, np.array(lower), np.array(upper))

        integrality = np.ones(m, dtype=int)
        bounds = (np.zeros(m), np.ones(m))
        c = np.zeros(m)

        start = time.time()
        res = milp(c=c, constraints=cons, integrality=integrality, bounds=bounds, options={"time_limit": time_limit_s})
        wall = time.time() - start
    except Exception as e:
        return SolveSummary(
            backend="scipy",
            mode="full",
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
            time_limit_s=time_limit_s,
            status="error",
            wall_s=0.0,
            iterations=0,
            constraints_added=0,
            notes={"error": f"{type(e).__name__}: {e}"},
        )

    status = "unknown"
    if res.success and res.x is not None:
        status = "sat"
        sol = [1 if v >= 0.5 else 0 for v in res.x.tolist()]
        ok, msg = verify_solution(
            sol,
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
        )
        ss = SolveSummary(
            backend="scipy",
            mode="full",
            n=n,
            min_edges=min_edges,
            max_edges=max_edges,
            subset_size=subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_clique_k,
            time_limit_s=time_limit_s,
            status=status,
            wall_s=wall,
            iterations=1,
            constraints_added=row,
            notes={"highs_status": getattr(res, "status", None), "message": getattr(res, "message", None)},
            edge_count=solution_edge_count(sol),
        )
        model_path = _write_model_edges(out_prefix, sol, n)
        ss.model_path = str(model_path)
        ss.model_check = "valid" if ok else "invalid"
        ss.model_check_message = msg
        return ss

    if getattr(res, "status", None) in (2, 3):  # 2=Infeasible, 3=Unbounded in HiGHS, but can vary.
        status = "unsat"

    return SolveSummary(
        backend="scipy",
        mode="full",
        n=n,
        min_edges=min_edges,
        max_edges=max_edges,
        subset_size=subset_size,
        subset_lb=subset_lb,
        subset_ub=subset_ub,
        forbid_clique_k=forbid_clique_k,
        time_limit_s=time_limit_s,
        status=status,
        wall_s=wall,
        iterations=1,
        constraints_added=row,
        notes={"success": bool(getattr(res, "success", False)), "status": getattr(res, "status", None), "message": getattr(res, "message", None)},
    )


def _default_out_path(backend: str, action: str) -> Path:
    base = Path(__file__).resolve().parents[1] / "results"
    base.mkdir(parents=True, exist_ok=True)
    return base / f"phase1_f_{backend}_{action}_{_utc_now_compact()}.json"


def main() -> int:
    p = argparse.ArgumentParser(description="Phase 1 no-K5 minimum-colour branch: non-PySAT solver probes (Agent F).")
    p.add_argument("action", choices=["probe", "solve"], help="probe environment or attempt a solve")
    p.add_argument("--backend", choices=["ortools", "z3", "pulp", "scipy"], default="ortools")
    p.add_argument("--mode", choices=["lazy", "full"], default="lazy", help="lazy cut loop or full constraints upfront")
    p.add_argument("--n", type=int, default=26)
    p.add_argument("--min-edges", type=int, default=60)
    p.add_argument("--max-edges", type=int, default=65)
    p.add_argument("--subset-size", type=int, default=6)
    p.add_argument("--subset-lb", type=int, default=1)
    p.add_argument("--subset-ub", type=int, default=11)
    p.add_argument("--forbid-k", type=int, default=5, help="forbid K_k (i.e., omega <= k-1); set 0 to disable")
    p.add_argument("--time-limit-s", type=float, default=60.0)
    p.add_argument("--max-round-violations", type=int, default=200, help="lazy mode: max violated subsets to cut per round")
    p.add_argument("--workers", type=int, default=8, help="ortools only: num_search_workers")
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    out_path = args.out if args.out else _default_out_path(args.backend, args.action)
    out_prefix = out_path.with_suffix("")

    if args.action == "probe":
        data = probe_environment()
        out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(json.dumps(data, indent=2))
        return 0

    subset_lb = None if args.subset_lb < 0 else int(args.subset_lb)
    subset_ub = None if args.subset_ub < 0 else int(args.subset_ub)
    forbid_k = None if args.forbid_k <= 0 else int(args.forbid_k)

    if args.backend == "scipy" and args.mode != "full":
        raise SystemExit("scipy backend currently supports mode=full only")

    if args.backend == "ortools":
        summary = solve_ortools(
            n=args.n,
            min_edges=args.min_edges,
            max_edges=args.max_edges,
            subset_size=args.subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_k,
            mode=args.mode,
            time_limit_s=args.time_limit_s,
            max_round_violations=args.max_round_violations,
            out_prefix=out_prefix,
            workers=args.workers,
        )
    elif args.backend == "z3":
        summary = solve_z3(
            n=args.n,
            min_edges=args.min_edges,
            max_edges=args.max_edges,
            subset_size=args.subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_k,
            mode=args.mode,
            time_limit_s=args.time_limit_s,
            max_round_violations=args.max_round_violations,
            out_prefix=out_prefix,
        )
    elif args.backend == "pulp":
        summary = solve_pulp(
            n=args.n,
            min_edges=args.min_edges,
            max_edges=args.max_edges,
            subset_size=args.subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_k,
            mode=args.mode,
            time_limit_s=args.time_limit_s,
            max_round_violations=args.max_round_violations,
            out_prefix=out_prefix,
        )
    else:
        summary = solve_scipy_milp(
            n=args.n,
            min_edges=args.min_edges,
            max_edges=args.max_edges,
            subset_size=args.subset_size,
            subset_lb=subset_lb,
            subset_ub=subset_ub,
            forbid_clique_k=forbid_k,
            time_limit_s=args.time_limit_s,
            out_prefix=out_prefix,
        )

    data = summary.to_dict()
    data["env_probe"] = probe_environment()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps(data, indent=2))
    return 0 if summary.status == "sat" else (10 if summary.status == "unsat" else 20)


if __name__ == "__main__":
    raise SystemExit(main())
