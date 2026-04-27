# EP617 Phase 1 Agent J proof-log probe

Generated: 2026-04-26T20:26:00-05:00

## Feasibility

The PySAT wrappers accept `with_proof=True` and return UNSAT on the toy cases for: cadical153, glucose4, gluecard4, lingeling, maplecm, maplesat.
Non-empty `get_proof()` traces were observed for: none.
Stable child processes with non-empty proof traces were observed for: none.
Child processes using proof logging returned nonzero/crashed for: cadical153, glucose4, gluecard4, lingeling, maplecm, maplesat.
This PySAT API did not emit LRAT, did not expose a public proof-file streaming path, and produced no independent proof-check result.
On this Windows/Python 3.13 build, PySAT proof logging is not usable as the final certificate path. External proof-producing solvers and checkers are needed.

## Local external tools

Not found on PATH: cadical, cadical195, cadical153, kissat, glucose, minisat, drat-trim, gratgen, lrat-check, cake_lpr, lingeling, plingeling.

## Probe cases

- `php_3_2`: vars=6, clauses=9; Pigeonhole principle: 3 pigeons into 2 holes.
- `no_k5_n6_min14_forbid_no_upper6`: vars=29, clauses=48; One-colour no-K5 skeleton on n=6 with min_edges=14 and forbid_k5, omitting upper6 so UNSAT comes from the K5-free edge bound rather than a direct six-set upper contradiction.

## Solver results

| solver | API proof rows | non-empty | unstable children | errors/unsupported | notes |
| --- | ---: | ---: | ---: | ---: | --- |
| `cadical153` | 2 | 0 | 2 | 0 | RUP empty |
| `glucose4` | 2 | 0 | 2 | 0 | RUP empty |
| `gluecard4` | 2 | 0 | 2 | 0 | RUP empty |
| `lingeling` | 2 | 0 | 2 | 0 | RUP empty |
| `maplecm` | 2 | 0 | 2 | 0 | RUP empty |
| `maplesat` | 2 | 0 | 2 | 0 | RUP empty |
| `mergesat3` | 0 | 0 | 0 | 2 | errors: NotImplementedError |
| `minicard` | 0 | 0 | 0 | 2 | errors: KnownUnsupportedProofSolver |
| `minisat22` | 0 | 0 | 0 | 2 | errors: KnownUnsupportedProofSolver |

## Final certificate path

1. Materialize every final branch/cube as a standalone DIMACS file. Do not rely on `solve(assumptions=...)` for a final artifact; add cube literals as unit clauses so the proof checks against the exact CNF.
2. Do not use this local PySAT build as the final proof producer: the public proof API returned empty traces here and proof-logging children crashed/nonzero.
3. For the final certificate, install/use an external solver and checker. Produce a solver proof for each branch, independently check it against the exact DIMACS, and convert/check LRAT if the final archive requires LRAT.
4. Log the cube list and a separate coverage argument. Per-cube UNSAT proofs only certify the leaves; they do not certify that the leaves cover the root search unless the cube coverage artifact is also checked.

Concrete commands from this probe:

```powershell
python erdos\617\scripts\phase1_unsat_proof_probe_j.py --out-dir erdos\617\results
python erdos\617\scripts\phase1_unsat_proof_probe_j.py --cases no_k5_n5_complete_forbidden --solvers glucose4 --out-dir erdos\617\results
```

External final-certificate command pattern once tools are installed:

```powershell
# DRAT/DRUP checking path
cadical --no-binary final_branch.cnf final_branch.drat
drat-trim final_branch.cnf final_branch.drat

# LRAT archive path, if using drat-trim as converter/checker
drat-trim final_branch.cnf final_branch.drat -L final_branch.lrat
lrat-check final_branch.cnf final_branch.lrat
```

Command-source notes: CaDiCaL accepts `[input] [proof]` and writes DRAT when a proof path is supplied; `--no-binary` requests text proof output. Current `drat-trim` manpages use `drat-trim INPUT PROOF [options]`, with `-L LEMMAS` for LRAT output.

Source URLs: https://www.mankier.com/1/cadical and https://manpages.debian.org/unstable/drat-trim/drat-trim.1.en.html

## Assumption probe

{
  "solver": "glucose4",
  "base_cnf": [
    [
      1
    ]
  ],
  "assumptions": [
    -1
  ],
  "purpose": "Check proof behavior for solve(assumptions=...).",
  "status": "unsat",
  "proof_line_count": 0,
  "proof_last_line": null,
  "proof_path": "erdos\\617\\results\\phase1_j_assumption_probe_glucose4.drup",
  "proof_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "rup_check_against_base_without_assumption": {
    "status": "empty",
    "reason": "no proof lines returned"
  },
  "child_exit_code": "timeout",
  "process_stable": false,
  "child_timeout": true,
  "process_note": "child process returned nonzero after/while using PySAT proof logging",
  "child_stdout_tail": "__PHASE1_J_CHILD_ROW__{\"solver\": \"glucose4\", \"base_cnf\": [[1]], \"assumptions\": [-1], \"purpose\": \"Check proof behavior for solve(assumptions=...).\", \"status\": \"unsat\", \"proof_line_count\": 0, \"proof_last_line\": null, \"proof_path\": \"erdos\\\\617\\\\results\\\\phase1_j_assumption_probe_glucose4.drup\", \"proof_sha256\": \"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\", \"rup_check_against_base_without_assumption\": {\"status\": \"empty\", \"reason\": \"no proof lines returned\"}}"
}

## Unsupported/error solvers

mergesat3, minicard, minisat22
