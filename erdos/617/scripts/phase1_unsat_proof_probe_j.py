from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

from pysat.formula import CNF
from pysat.solvers import Solver

try:
    import pysat
except Exception:  # pragma: no cover - import already required above
    pysat = None  # type: ignore[assignment]

from one_color_strengthened import build_cnf


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

DEFAULT_SOLVERS = [
    "cadical103",
    "cadical153",
    "cadical195",
    "glucose3",
    "glucose4",
    "glucose42",
    "gluecard3",
    "gluecard4",
    "lingeling",
    "maplechrono",
    "maplecm",
    "maplesat",
    "mergesat3",
    "minicard",
    "minisat22",
    "minisatgh",
]

KNOWN_UNSUPPORTED_PROOF_SOLVERS = {
    "minicard": "PySAT raises: Proof logging is not supported by Minicard.",
    "minisat22": "PySAT raises: Proof logging is not supported by Minisat22.",
    "minisatgh": "This local PySAT install does not expose minisatgh.",
}

EXTERNAL_TOOLS = [
    "cadical",
    "cadical195",
    "cadical153",
    "kissat",
    "glucose",
    "minisat",
    "drat-trim",
    "gratgen",
    "lrat-check",
    "cake_lpr",
    "lingeling",
    "plingeling",
]

CHILD_PREFIX = "__PHASE1_J_CHILD_ROW__"


@dataclass(frozen=True)
class ProbeCase:
    name: str
    description: str
    cnf: CNF


def cnf_from_clauses(clauses: list[list[int]]) -> CNF:
    cnf = CNF(from_clauses=clauses)
    cnf.nv = max((abs(lit) for clause in clauses for lit in clause), default=0)
    return cnf


def build_cases() -> dict[str, ProbeCase]:
    no_k5_n5, _ = build_cnf(
        n=5,
        max_edges=10,
        min_edges=10,
        clique_star=False,
        upper6=True,
        forbid_k5=True,
    )
    no_k5_n6_empty, _ = build_cnf(
        n=6,
        max_edges=0,
        min_edges=0,
        clique_star=False,
        upper6=True,
        forbid_k5=True,
    )
    no_k5_n6_complete, _ = build_cnf(
        n=6,
        max_edges=15,
        min_edges=15,
        clique_star=False,
        upper6=True,
        forbid_k5=True,
    )
    no_k5_n6_min14, _ = build_cnf(
        n=6,
        max_edges=15,
        min_edges=14,
        clique_star=False,
        upper6=False,
        forbid_k5=True,
    )
    return {
        "unit_contradiction": ProbeCase(
            name="unit_contradiction",
            description="Toy CNF containing x and not x.",
            cnf=cnf_from_clauses([[1], [-1]]),
        ),
        "four_clause_xor": ProbeCase(
            name="four_clause_xor",
            description="Unsatisfiable two-variable four-clause XOR-style toy.",
            cnf=cnf_from_clauses([[1, 2], [-1, 2], [1, -2], [-1, -2]]),
        ),
        "php_3_2": ProbeCase(
            name="php_3_2",
            description="Pigeonhole principle: 3 pigeons into 2 holes.",
            cnf=cnf_from_clauses(
                [
                    [1, 2],
                    [3, 4],
                    [5, 6],
                    [-1, -3],
                    [-1, -5],
                    [-3, -5],
                    [-2, -4],
                    [-2, -6],
                    [-4, -6],
                ]
            ),
        ),
        "no_k5_n5_complete_forbidden": ProbeCase(
            name="no_k5_n5_complete_forbidden",
            description=(
                "Same one-colour no-K5 skeleton on n=5: exact 10 selected edges "
                "forces K5, while forbid_k5 forbids it."
            ),
            cnf=no_k5_n5,
        ),
        "no_k5_n6_zero_edges_coverage": ProbeCase(
            name="no_k5_n6_zero_edges_coverage",
            description=(
                "Same one-colour no-K5 skeleton on n=6: exact zero selected edges "
                "contradicts the one 6-set lower coverage clause."
            ),
            cnf=no_k5_n6_empty,
        ),
        "no_k5_n6_complete_forbidden": ProbeCase(
            name="no_k5_n6_complete_forbidden",
            description=(
                "Same one-colour no-K5 skeleton on n=6: exact complete graph "
                "contradicts forbid_k5."
            ),
            cnf=no_k5_n6_complete,
        ),
        "no_k5_n6_min14_forbid_no_upper6": ProbeCase(
            name="no_k5_n6_min14_forbid_no_upper6",
            description=(
                "One-colour no-K5 skeleton on n=6 with min_edges=14 and forbid_k5, "
                "omitting upper6 so UNSAT comes from the K5-free edge bound rather "
                "than a direct six-set upper contradiction."
            ),
            cnf=no_k5_n6_min14,
        ),
    }


def write_dimacs(path: Path, cnf: CNF, comments: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="ascii", newline="\n") as handle:
        for comment in comments:
            handle.write(f"c {comment}\n")
        handle.write(f"p cnf {cnf.nv} {len(cnf.clauses)}\n")
        for clause in cnf.clauses:
            handle.write(" ".join(str(lit) for lit in clause))
            handle.write(" 0\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_proof_clause(line: str) -> tuple[str, list[int]] | None:
    parts = line.strip().split()
    if not parts or parts[0] == "c":
        return None
    kind = "add"
    if parts[0] == "d":
        kind = "delete"
        parts = parts[1:]
    if not parts:
        return None
    lits = [int(part) for part in parts]
    if not lits or lits[-1] != 0:
        raise ValueError(f"proof line is not zero-terminated: {line!r}")
    return kind, lits[:-1]


def has_unit_conflict(clauses: list[list[int]], assumptions: list[int]) -> bool:
    assigns: dict[int, bool] = {}

    def assign(lit: int) -> bool:
        var = abs(lit)
        val = lit > 0
        old = assigns.get(var)
        if old is not None:
            return old == val
        assigns[var] = val
        return True

    for lit in assumptions:
        if not assign(lit):
            return True

    changed = True
    while changed:
        changed = False
        for clause in clauses:
            unassigned = []
            satisfied = False
            for lit in clause:
                val = assigns.get(abs(lit))
                if val is None:
                    unassigned.append(lit)
                elif val == (lit > 0):
                    satisfied = True
                    break
            if satisfied:
                continue
            if not unassigned:
                return True
            if len(unassigned) == 1:
                if not assign(unassigned[0]):
                    return True
                changed = True
    return False


def rup_check(cnf: CNF, proof: list[str], max_lines: int = 200000) -> dict[str, object]:
    if not proof:
        return {"status": "empty", "reason": "no proof lines returned"}
    if len(proof) > max_lines:
        return {"status": "skipped", "reason": f"proof has more than {max_lines} lines"}

    clauses = [list(clause) for clause in cnf.clauses]
    additions = 0
    deletions = 0
    try:
        for line_no, line in enumerate(proof, start=1):
            parsed = parse_proof_clause(line)
            if parsed is None:
                continue
            kind, clause = parsed
            if kind == "delete":
                deletions += 1
                continue
            assumptions = [-lit for lit in clause]
            if not has_unit_conflict(clauses, assumptions):
                return {
                    "status": "failed",
                    "line": line_no,
                    "clause": clause,
                    "reason": "line is not RUP against retained clauses",
                }
            clauses.append(clause)
            additions += 1
        return {"status": "passed", "additions": additions, "deletions": deletions}
    except Exception as exc:
        return {"status": "error", "error": f"{type(exc).__name__}: {exc}"}


def write_proof(path: Path, proof: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="ascii", newline="\n") as handle:
        for line in proof:
            handle.write(line.rstrip())
            handle.write("\n")


def run_solver(case: ProbeCase, solver_name: str, out_dir: Path, write_all: bool) -> dict[str, object]:
    row: dict[str, object] = {
        "case": case.name,
        "solver": solver_name,
        "vars": case.cnf.nv,
        "clauses": len(case.cnf.clauses),
        "expected": "unsat",
    }
    if solver_name in KNOWN_UNSUPPORTED_PROOF_SOLVERS:
        row.update(
            {
                "status": "skipped_unsupported",
                "proof_supported": False,
                "error_type": "KnownUnsupportedProofSolver",
                "error": KNOWN_UNSUPPORTED_PROOF_SOLVERS[solver_name],
                "seconds": 0.0,
            }
        )
        return row

    started = time.perf_counter()
    try:
        with Solver(
            name=solver_name,
            bootstrap_with=case.cnf.clauses,
            use_timer=True,
            with_proof=True,
        ) as solver:
            result = solver.solve()
            row["solve_result"] = result
            row["status"] = "sat" if result is True else ("unsat" if result is False else "unknown")
            proof = solver.get_proof()
            row["solver_time"] = solver.time()
    except Exception as exc:
        row.update(
            {
                "status": "error",
                "proof_supported": False,
                "error_type": type(exc).__name__,
                "error": str(exc),
                "seconds": round(time.perf_counter() - started, 6),
            }
        )
        return row

    row["seconds"] = round(time.perf_counter() - started, 6)
    if proof is None:
        row["proof_supported"] = False
        row["proof_line_count"] = 0
        row["proof_note"] = "get_proof returned None"
        return row

    proof_lines = [str(line) for line in proof]
    row["proof_supported"] = True
    row["proof_line_count"] = len(proof_lines)
    row["proof_nonempty"] = bool(proof_lines)
    row["proof_last_line"] = proof_lines[-1] if proof_lines else None
    row["rup_check"] = rup_check(case.cnf, proof_lines)

    if write_all or case.name.startswith("no_k5"):
        proof_path = out_dir / f"phase1_j_{case.name}_{solver_name}.drup"
        write_proof(proof_path, proof_lines)
        row["proof_path"] = str(proof_path)
        row["proof_sha256"] = sha256_file(proof_path)
    return row


def tail_text(text: str, limit: int = 12) -> str:
    lines = text.splitlines()
    return "\n".join(lines[-limit:])


def parse_child_row(stdout: str) -> dict[str, object] | None:
    for line in reversed(stdout.splitlines()):
        if line.startswith(CHILD_PREFIX):
            return json.loads(line[len(CHILD_PREFIX) :])
    return None


def normalize_timeout_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value


def run_solver_isolated(
    case: ProbeCase,
    solver_name: str,
    out_dir: Path,
    write_all: bool,
    child_timeout: float,
) -> dict[str, object]:
    if solver_name in KNOWN_UNSUPPORTED_PROOF_SOLVERS:
        return run_solver(case, solver_name, out_dir, write_all)

    cmd = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--child-probe",
        case.name,
        solver_name,
        "--out-dir",
        str(out_dir),
    ]
    if write_all:
        cmd.append("--write-all-proofs")

    started = time.perf_counter()
    try:
        completed = subprocess.run(
            cmd,
            cwd=str(ROOT.parents[1]),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=child_timeout,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        returncode: int | str = completed.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        stdout = normalize_timeout_text(exc.stdout)
        stderr = normalize_timeout_text(exc.stderr)
        returncode = "timeout"
        timed_out = True

    child_row = parse_child_row(stdout)
    if child_row is None:
        child_row = {
            "case": case.name,
            "solver": solver_name,
            "vars": case.cnf.nv,
            "clauses": len(case.cnf.clauses),
            "status": "child_error",
            "proof_supported": False,
            "error_type": "ChildResultMissing",
            "error": "child process did not emit a parseable result row",
        }
    child_row["child_exit_code"] = returncode
    child_row["child_seconds"] = round(time.perf_counter() - started, 6)
    child_row["process_stable"] = returncode == 0
    child_row["child_timeout"] = timed_out
    if returncode != 0:
        child_row["process_note"] = "child process returned nonzero after/while using PySAT proof logging"
    if stdout:
        child_row["child_stdout_tail"] = tail_text(stdout)
    if stderr:
        child_row["child_stderr_tail"] = tail_text(stderr)
    return child_row


def run_assumption_probe(out_dir: Path, solver_name: str) -> dict[str, object]:
    row: dict[str, object] = {
        "solver": solver_name,
        "base_cnf": [[1]],
        "assumptions": [-1],
        "purpose": "Check proof behavior for solve(assumptions=...).",
    }
    try:
        with Solver(name=solver_name, bootstrap_with=[[1]], with_proof=True) as solver:
            result = solver.solve(assumptions=[-1])
            proof = solver.get_proof()
    except Exception as exc:
        row.update({"status": "error", "error_type": type(exc).__name__, "error": str(exc)})
        return row
    row["status"] = "sat" if result is True else ("unsat" if result is False else "unknown")
    if proof is not None:
        proof_lines = [str(line) for line in proof]
        path = out_dir / f"phase1_j_assumption_probe_{solver_name}.drup"
        write_proof(path, proof_lines)
        row["proof_line_count"] = len(proof_lines)
        row["proof_last_line"] = proof_lines[-1] if proof_lines else None
        row["proof_path"] = str(path)
        row["proof_sha256"] = sha256_file(path)
        row["rup_check_against_base_without_assumption"] = rup_check(cnf_from_clauses([[1]]), proof_lines)
    else:
        row["proof_line_count"] = 0
        row["proof_note"] = "get_proof returned None"
    return row


def run_assumption_probe_isolated(out_dir: Path, solver_name: str, child_timeout: float) -> dict[str, object]:
    cmd = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--child-assumption",
        solver_name,
        "--out-dir",
        str(out_dir),
    ]
    try:
        completed = subprocess.run(
            cmd,
            cwd=str(ROOT.parents[1]),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=child_timeout,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        returncode: int | str = completed.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        stdout = normalize_timeout_text(exc.stdout)
        stderr = normalize_timeout_text(exc.stderr)
        returncode = "timeout"
        timed_out = True

    row = parse_child_row(stdout)
    if row is None:
        row = {
            "solver": solver_name,
            "status": "child_error",
            "error_type": "ChildResultMissing",
            "error": "child process did not emit a parseable assumption-probe row",
        }
    row["child_exit_code"] = returncode
    row["process_stable"] = returncode == 0
    row["child_timeout"] = timed_out
    if returncode != 0:
        row["process_note"] = "child process returned nonzero after/while using PySAT proof logging"
    if stdout:
        row["child_stdout_tail"] = tail_text(stdout)
    if stderr:
        row["child_stderr_tail"] = tail_text(stderr)
    return row


def external_tool_map() -> dict[str, str | None]:
    return {tool: shutil.which(tool) for tool in EXTERNAL_TOOLS}


def write_report(path: Path, summary: dict[str, object]) -> None:
    rows = summary["rows"]  # type: ignore[index]
    api_supported = sorted(
        {
            str(row["solver"])
            for row in rows  # type: ignore[union-attr]
            if row.get("status") == "unsat" and row.get("proof_supported") is True
        }
    )
    nonempty_supported = sorted(
        {
            str(row["solver"])
            for row in rows  # type: ignore[union-attr]
            if row.get("status") == "unsat" and row.get("proof_nonempty") is True
        }
    )
    stable_nonempty_supported = sorted(
        {
            str(row["solver"])
            for row in rows  # type: ignore[union-attr]
            if row.get("status") == "unsat"
            and row.get("proof_nonempty") is True
            and row.get("child_exit_code", 0) == 0
        }
    )
    unstable = sorted(
        {
            str(row["solver"])
            for row in rows  # type: ignore[union-attr]
            if row.get("child_exit_code", 0) != 0
        }
    )
    unsupported = sorted(
        {
            str(row["solver"])
            for row in rows  # type: ignore[union-attr]
            if row.get("proof_supported") is False or row.get("status") == "error"
        }
    )
    external = summary["external_tools"]  # type: ignore[index]
    missing_external = [name for name, found in external.items() if found is None]  # type: ignore[union-attr]

    lines = [
        "# EP617 Phase 1 Agent J proof-log probe",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Feasibility",
        "",
        (
            "The PySAT wrappers accept `with_proof=True` and return UNSAT on the "
            f"toy cases for: {', '.join(api_supported) or 'none'}."
        ),
        (
            "Non-empty `get_proof()` traces were observed for: "
            f"{', '.join(nonempty_supported) or 'none'}."
        ),
        (
            "Stable child processes with non-empty proof traces were observed for: "
            f"{', '.join(stable_nonempty_supported) or 'none'}."
        ),
        (
            "Child processes using proof logging returned nonzero/crashed for: "
            f"{', '.join(unstable) or 'none'}."
        ),
        (
            "This PySAT API did not emit LRAT, did not expose a public proof-file "
            "streaming path, and produced no independent proof-check result."
        ),
        (
            "On this Windows/Python 3.13 build, PySAT proof logging is not usable "
            "as the final certificate path. External proof-producing solvers and "
            "checkers are needed."
        ),
        "",
        "## Local external tools",
        "",
    ]
    if missing_external:
        lines.append("Not found on PATH: " + ", ".join(missing_external) + ".")
    else:
        lines.append("All probed external tools were found on PATH.")

    lines.extend(
        [
            "",
            "## Probe cases",
            "",
        ]
    )
    for case in summary["cases"]:  # type: ignore[index]
        lines.append(
            f"- `{case['name']}`: vars={case['vars']}, clauses={case['clauses']}; {case['description']}"
        )

    lines.extend(
        [
            "",
            "## Solver results",
            "",
            "| solver | API proof rows | non-empty | unstable children | errors/unsupported | notes |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    solvers = summary["solvers"]  # type: ignore[index]
    for solver in solvers:
        solver_rows = [row for row in rows if row["solver"] == solver]  # type: ignore[index]
        proof_count = sum(
            1 for row in solver_rows if row.get("status") == "unsat" and row.get("proof_supported") is True
        )
        nonempty_count = sum(
            1 for row in solver_rows if row.get("status") == "unsat" and row.get("proof_nonempty") is True
        )
        unstable_count = sum(1 for row in solver_rows if row.get("child_exit_code", 0) != 0)
        bad_count = sum(1 for row in solver_rows if row.get("proof_supported") is False or row.get("status") == "error")
        notes = []
        errors = sorted({str(row.get("error_type")) for row in solver_rows if row.get("error_type")})
        if errors:
            notes.append("errors: " + ", ".join(errors))
        rup = sorted({str(row.get("rup_check", {}).get("status")) for row in solver_rows if row.get("rup_check")})
        if rup:
            notes.append("RUP " + ", ".join(rup))
        lines.append(
            f"| `{solver}` | {proof_count} | {nonempty_count} | {unstable_count} | {bad_count} | {'; '.join(notes)} |"
        )

    lines.extend(
        [
            "",
            "## Final certificate path",
            "",
            "1. Materialize every final branch/cube as a standalone DIMACS file. Do not rely on `solve(assumptions=...)` for a final artifact; add cube literals as unit clauses so the proof checks against the exact CNF.",
            "2. Do not use this local PySAT build as the final proof producer: the public proof API returned empty traces here and proof-logging children crashed/nonzero.",
            "3. For the final certificate, install/use an external solver and checker. Produce a solver proof for each branch, independently check it against the exact DIMACS, and convert/check LRAT if the final archive requires LRAT.",
            "4. Log the cube list and a separate coverage argument. Per-cube UNSAT proofs only certify the leaves; they do not certify that the leaves cover the root search unless the cube coverage artifact is also checked.",
            "",
            "Concrete commands from this probe:",
            "",
            "```powershell",
            "python erdos\\617\\scripts\\phase1_unsat_proof_probe_j.py --out-dir erdos\\617\\results",
            "python erdos\\617\\scripts\\phase1_unsat_proof_probe_j.py --cases no_k5_n5_complete_forbidden --solvers glucose4 --out-dir erdos\\617\\results",
            "```",
            "",
            "External final-certificate command pattern once tools are installed:",
            "",
            "```powershell",
            "# DRAT/DRUP checking path",
            "cadical --no-binary final_branch.cnf final_branch.drat",
            "drat-trim final_branch.cnf final_branch.drat",
            "",
            "# LRAT archive path, if using drat-trim as converter/checker",
            "drat-trim final_branch.cnf final_branch.drat -L final_branch.lrat",
            "lrat-check final_branch.cnf final_branch.lrat",
            "```",
            "",
            "Command-source notes: CaDiCaL accepts `[input] [proof]` and writes DRAT when a proof path is supplied; `--no-binary` requests text proof output. Current `drat-trim` manpages use `drat-trim INPUT PROOF [options]`, with `-L LEMMAS` for LRAT output.",
            "",
            "Source URLs: https://www.mankier.com/1/cadical and https://manpages.debian.org/unstable/drat-trim/drat-trim.1.en.html",
            "",
            "## Assumption probe",
            "",
            json.dumps(summary["assumption_probe"], indent=2),
            "",
            "## Unsupported/error solvers",
            "",
            ", ".join(unsupported) if unsupported else "None.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_csv(text: str) -> list[str]:
    return [part.strip() for part in text.split(",") if part.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe PySAT proof logging for EP617 no-K5 UNSAT branches.")
    parser.add_argument("--out-dir", type=Path, default=RESULTS)
    parser.add_argument("--solvers", type=parse_csv, default=DEFAULT_SOLVERS)
    parser.add_argument(
        "--cases",
        type=parse_csv,
        default=None,
        help="Comma-separated case names; defaults to all toy and no-K5 cases.",
    )
    parser.add_argument("--write-all-proofs", action="store_true")
    parser.add_argument("--assumption-solver", default="glucose4")
    parser.add_argument("--child-timeout", type=float, default=3.0)
    parser.add_argument("--child-probe", nargs=2, metavar=("CASE", "SOLVER"), help=argparse.SUPPRESS)
    parser.add_argument("--child-assumption", metavar="SOLVER", help=argparse.SUPPRESS)
    args = parser.parse_args()

    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    cases = build_cases()
    if args.child_probe is not None:
        case_name, solver_name = args.child_probe
        if case_name not in cases:
            raise SystemExit(f"unknown case: {case_name}")
        row = run_solver(cases[case_name], solver_name, out_dir, args.write_all_proofs)
        print(CHILD_PREFIX + json.dumps(row), flush=True)
        return 0

    if args.child_assumption is not None:
        row = run_assumption_probe(out_dir, args.child_assumption)
        print(CHILD_PREFIX + json.dumps(row), flush=True)
        return 0

    selected_names = args.cases if args.cases is not None else list(cases)
    missing = [name for name in selected_names if name not in cases]
    if missing:
        raise SystemExit(f"unknown case(s): {', '.join(missing)}")

    case_rows = []
    rows = []
    for case_name in selected_names:
        case = cases[case_name]
        cnf_path = out_dir / f"phase1_j_{case.name}.cnf"
        write_dimacs(
            cnf_path,
            case.cnf,
            comments=[
                "EP617 Agent J proof-log probe",
                case.name,
                case.description,
            ],
        )
        case_rows.append(
            {
                "name": case.name,
                "description": case.description,
                "vars": case.cnf.nv,
                "clauses": len(case.cnf.clauses),
                "cnf_path": str(cnf_path),
                "cnf_sha256": sha256_file(cnf_path),
            }
        )
        for solver_name in args.solvers:
            row = run_solver_isolated(case, solver_name, out_dir, args.write_all_proofs, args.child_timeout)
            rows.append(row)
            print(json.dumps(row), flush=True)

    summary: dict[str, object] = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "python": sys.version,
        "platform": platform.platform(),
        "pysat_version": getattr(pysat, "__version__", None),
        "pysat_path": getattr(pysat, "__file__", None),
        "solvers": args.solvers,
        "cases": case_rows,
        "rows": rows,
        "assumption_probe": run_assumption_probe_isolated(out_dir, args.assumption_solver, args.child_timeout),
        "external_tools": external_tool_map(),
    }

    summary_path = out_dir / "phase1_j_probe_summary.json"
    report_path = out_dir / "phase1_j_probe_report.md"
    summary["summary_path"] = str(summary_path)
    summary["report_path"] = str(report_path)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_report(report_path, summary)
    print(json.dumps({"summary_path": str(summary_path), "report_path": str(report_path)}, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
