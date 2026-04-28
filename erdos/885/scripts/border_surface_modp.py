#!/usr/bin/env python3
"""Finite-field border-surface scan for EP885 K4,4 -> K5,5.

Given a Bremner K4,4 seed, reduce the rows N_i and columns x_j^2 modulo p and
count pairs (X, M) satisfying

    X^2 + N_i is a square for every old row N_i,
    M + x_j^2 is a square for every old column x_j,
    M + X^2 is a square.

This is a local diagnostic for the simultaneous bordering route.  It is not a
rational search and does not prove existence over Q.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import bremner_map


def prime_sieve(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for n in range(2, int(limit**0.5) + 1):
        if sieve[n]:
            step = n
            start = n * n
            sieve[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def sqrt_table_mod_p(p: int) -> dict[int, int]:
    """Return one square root for every quadratic residue modulo p."""
    table: dict[int, int] = {}
    for x in range(p):
        table[(x * x) % p] = x
    return table


def rank_mod_p(matrix: list[list[int]], p: int) -> int:
    """Row rank over F_p."""
    rows = [[value % p for value in row] for row in matrix]
    rank = 0
    col_count = len(rows[0]) if rows else 0
    for col in range(col_count):
        pivot = None
        for row in range(rank, len(rows)):
            if rows[row][col] % p:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [(value * inv) % p for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            factor = rows[row][col] % p
            if factor:
                rows[row] = [
                    (rows[row][j] - factor * rows[rank][j]) % p
                    for j in range(col_count)
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def border_jacobian_rank(
    x: int,
    x2: int,
    m: int,
    rows: list[int],
    cols: list[int],
    roots: dict[int, int],
    p: int,
) -> int:
    """Jacobian rank of the full border equations at one mod-p lift.

    Variables are ordered as

        X, M, U_1,...,U_4, V_1,...,V_4, W.

    Equations are

        U_i^2 - X^2 - N_i = 0,
        V_j^2 - M - x_j^2 = 0,
        W^2 - M - X^2 = 0.

    For odd p, the rank is independent of the choice of nonzero square-root
    signs because each root variable occurs in only one row.
    """
    matrix: list[list[int]] = []
    variable_count = 2 + len(rows) + len(cols) + 1
    for i, row_value in enumerate(rows):
        u = roots[(x2 + row_value) % p]
        jac_row = [0] * variable_count
        jac_row[0] = -2 * x
        jac_row[2 + i] = 2 * u
        matrix.append(jac_row)
    v_offset = 2 + len(rows)
    for j, col_value in enumerate(cols):
        v = roots[(m + col_value) % p]
        jac_row = [0] * variable_count
        jac_row[1] = -1
        jac_row[v_offset + j] = 2 * v
        matrix.append(jac_row)
    w = roots[(m + x2) % p]
    jac_row = [0] * variable_count
    jac_row[0] = -2 * x
    jac_row[1] = -1
    jac_row[-1] = 2 * w
    matrix.append(jac_row)
    return rank_mod_p(matrix, p)


def border_count_mod_p(n_values: list[int], deltas: list[int], p: int, sample_limit: int) -> dict:
    roots = sqrt_table_mod_p(p)
    residues = set(roots)
    rows = [n % p for n in n_values]
    cols = [pow((d // 2) % p, 2, p) for d in deltas]
    old_col_squares = set(cols)
    old_rows = set(rows)

    x_candidates: list[tuple[int, int, bool]] = []
    for x in range(p):
        x2 = (x * x) % p
        if all((x2 + row) % p in residues for row in rows):
            x_candidates.append((x, x2, x != 0 and x2 not in old_col_squares))

    m_candidates_for_old_cols: list[tuple[int, bool]] = []
    for m in range(p):
        if all((m + col) % p in residues for col in cols):
            m_candidates_for_old_cols.append((m, m != 0 and m not in old_rows))

    total = 0
    nontrivial = 0
    smooth = 0
    nontrivial_smooth = 0
    samples: list[dict] = []
    smooth_samples: list[dict] = []
    for x, x2, new_col in x_candidates:
        for m, new_row in m_candidates_for_old_cols:
            if (m + x2) % p not in residues:
                continue
            total += 1
            is_nontrivial = new_col and new_row
            jacobian_rank = border_jacobian_rank(x, x2, m, rows, cols, roots, p)
            is_smooth = jacobian_rank == 9
            if is_nontrivial:
                nontrivial += 1
            if is_smooth:
                smooth += 1
            if is_nontrivial and is_smooth:
                nontrivial_smooth += 1
                if len(smooth_samples) < sample_limit:
                    smooth_samples.append(
                        {
                            "X": x,
                            "X2": x2,
                            "M": m,
                            "jacobian_rank": jacobian_rank,
                        }
                    )
            if len(samples) < sample_limit:
                samples.append(
                    {
                        "X": x,
                        "X2": x2,
                        "M": m,
                        "new_col_mod_p": new_col,
                        "new_row_mod_p": new_row,
                        "jacobian_rank": jacobian_rank,
                        "smooth": is_smooth,
                    }
                )

    return {
        "p": p,
        "x_candidate_count": len(x_candidates),
        "m_candidate_count": len(m_candidates_for_old_cols),
        "border_pair_count": total,
        "nontrivial_pair_count": nontrivial,
        "smooth_pair_count": smooth,
        "nontrivial_smooth_pair_count": nontrivial_smooth,
        "samples": samples,
        "nontrivial_smooth_samples": smooth_samples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True, help="Use nQ on Bremner's final curve.")
    parser.add_argument("--torsion", action="store_true", help="Use nQ+T.")
    parser.add_argument("--prime", type=int, action="append", default=[])
    parser.add_argument("--prime-bound", type=int, default=0)
    parser.add_argument("--sample-limit", type=int, default=5)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    seed = bremner_map.generate(args.n, args.torsion)
    primes = list(args.prime)
    if args.prime_bound:
        primes.extend(q for q in prime_sieve(args.prime_bound) if q > 5)
    primes = sorted(set(primes))
    if not primes:
        raise SystemExit("provide --prime or --prime-bound")

    results = [
        border_count_mod_p(seed.N_values, seed.deltas, p, args.sample_limit)
        for p in primes
    ]
    payload = {
        "seed": f"{args.n}Q+T" if args.torsion else f"{args.n}Q",
        "deltas": seed.deltas,
        "N_values": seed.N_values,
        "results": results,
    }

    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
