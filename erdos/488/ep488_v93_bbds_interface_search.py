#!/usr/bin/env python3
"""Audit the BBDS bad-block interface in the top-window n>=3q regime.

This does not prove or disprove `extremizer_implies_bad_block` unless it finds
an actual EP488 counterexample. Instead it searches exact finite top-window
instances and records:

* worst ratio D(m)/m / (2D(n)/n) for n>=3q;
* whether the current height h=floor(n/q) is bad;
* whether any bad block of height >=3 occurs up to h;
* strongest near-misses with no current-height bad block.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from itertools import combinations
from math import gcd, lcm
from pathlib import Path


@dataclass
class Row:
    ratio_num: int
    ratio_den: int
    q: int
    C: list[int]
    n: int
    m: int
    Dn: int
    Dm: int
    h: int
    current_bad: bool
    any_bad_ge3_to_h: bool
    bad_blocks_ge3_to_h: list[int]
    any_bad_ge3_to_mheight: bool
    bad_blocks_ge3_to_mheight: list[int]
    block_cov_h: int
    slot_mass_h: int

    @property
    def ratio_float(self) -> float:
        return self.ratio_num / self.ratio_den


def primitive(C: tuple[int, ...]) -> bool:
    for i, a in enumerate(C):
        for b in C[i + 1 :]:
            if b % a == 0 or a % b == 0:
                return False
    return True


def connected_at_n(q: int, C: tuple[int, ...], n: int) -> bool:
    if len(C) <= 1:
        return True
    adj = {a: [] for a in C}
    for i, a in enumerate(C):
        for b in C[i + 1 :]:
            L = lcm(a, b)
            if L <= n and L % q != 0:
                adj[a].append(b)
                adj[b].append(a)
    seen = {C[0]}
    stack = [C[0]]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(C)


def build_prefix(q: int, C: tuple[int, ...], xmax: int) -> tuple[list[int], list[int]]:
    covered = [0] * (xmax + 2)
    mult = [0] * (xmax + 2)
    for t in range(1, xmax + 1):
        if t % q == 0:
            covered[t] = covered[t - 1]
            mult[t] = mult[t - 1]
            continue
        k = 0
        for a in C:
            if t % a == 0:
                k += 1
        covered[t] = covered[t - 1] + (1 if k else 0)
        mult[t] = mult[t - 1] + k
    return covered, mult


def block_values(prefix: list[int], q: int, j: int) -> int:
    lo = (j - 1) * q
    hi = j * q
    return prefix[hi] - prefix[lo]


def row_for(q: int, C: tuple[int, ...], n: int, m: int, D: list[int], S: list[int]) -> Row:
    h = n // q
    hm = m // q
    Dn = D[n]
    Dm = D[m]
    bad_blocks = []
    bad_blocks_to_m = []
    for j in range(3, hm + 1):
        cov = block_values(D, q, j)
        slot = block_values(S, q, j)
        if 2 * cov < slot:
            bad_blocks_to_m.append(j)
            if j <= h:
                bad_blocks.append(j)
    cov_h = block_values(D, q, h)
    slot_h = block_values(S, q, h)
    # ratio = (Dm/m)/(2Dn/n) = Dm*n/(2Dn*m)
    num = Dm * n
    den = 2 * Dn * m
    g = gcd(num, den)
    return Row(
        ratio_num=num // g,
        ratio_den=den // g,
        q=q,
        C=list(C),
        n=n,
        m=m,
        Dn=Dn,
        Dm=Dm,
        h=h,
        current_bad=2 * cov_h < slot_h,
        any_bad_ge3_to_h=bool(bad_blocks),
        bad_blocks_ge3_to_h=bad_blocks,
        any_bad_ge3_to_mheight=bool(bad_blocks_to_m),
        bad_blocks_ge3_to_mheight=bad_blocks_to_m,
        block_cov_h=cov_h,
        slot_mass_h=slot_h,
    )


def insert_top(rows: list[Row], row: Row, limit: int) -> None:
    rows.append(row)
    rows.sort(key=lambda r: (r.ratio_num / r.ratio_den, r.q, len(r.C)), reverse=True)
    del rows[limit:]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--q-max", type=int, default=22)
    ap.add_argument("--m-factor", type=int, default=40)
    ap.add_argument("--n-factor", type=int, default=12)
    ap.add_argument("--max-subset-size", type=int, default=0, help="0 means no cap")
    ap.add_argument("--min-subset-size", type=int, default=1)
    ap.add_argument("--connected-only", action="store_true")
    ap.add_argument(
        "--run-end-only",
        action="store_true",
        help="only test n,m with n uncovered, n+1 covered, m covered, m+1 uncovered",
    )
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    checked = 0
    violations: list[Row] = []
    worst: list[Row] = []
    worst_no_current_bad: list[Row] = []
    worst_no_any_bad: list[Row] = []

    for q in range(2, args.q_max + 1):
        vals = tuple(range(q // 2 + 1, q))
        max_size = len(vals) if args.max_subset_size <= 0 else min(args.max_subset_size, len(vals))
        xmax = args.m_factor * q
        for r in range(max(1, args.min_subset_size), max_size + 1):
            for C in combinations(vals, r):
                if not primitive(C):
                    continue
                D, S = build_prefix(q, C, xmax)
                for n in range(3 * q, min(args.n_factor * q, xmax - 1) + 1):
                    if args.connected_only and not connected_at_n(q, C, n):
                        continue
                    Dn = D[n]
                    if Dn == 0:
                        continue
                    if args.run_end_only and not (D[n] == D[n - 1] and D[n + 1] == D[n] + 1):
                        continue
                    best_m = None
                    best_num = -1
                    best_den = 1
                    for m in range(n + 1, xmax + 1):
                        if args.run_end_only and not (D[m] == D[m - 1] + 1 and D[m + 1] == D[m]):
                            continue
                        checked += 1
                        num = D[m] * n
                        den = 2 * Dn * m
                        if num * best_den > best_num * den:
                            best_num, best_den, best_m = num, den, m
                        if num > den:
                            row = row_for(q, C, n, m, D, S)
                            violations.append(row)
                            insert_top(worst, row, args.top)
                            if not row.current_bad:
                                insert_top(worst_no_current_bad, row, args.top)
                            if not row.any_bad_ge3_to_h:
                                insert_top(worst_no_any_bad, row, args.top)
                    if best_m is not None:
                        row = row_for(q, C, n, best_m, D, S)
                        insert_top(worst, row, args.top)
                        if not row.current_bad:
                            insert_top(worst_no_current_bad, row, args.top)
                        if not row.any_bad_ge3_to_h:
                            insert_top(worst_no_any_bad, row, args.top)

    data = {
        "q_max": args.q_max,
        "m_factor": args.m_factor,
        "n_factor": args.n_factor,
        "max_subset_size": args.max_subset_size or None,
        "min_subset_size": args.min_subset_size,
        "connected_only": args.connected_only,
        "run_end_only": args.run_end_only,
        "checked": checked,
        "violations": [asdict(v) for v in violations[: args.top]],
        "worst": [asdict(v) | {"ratio_float": v.ratio_float} for v in worst],
        "worst_no_current_bad": [
            asdict(v) | {"ratio_float": v.ratio_float} for v in worst_no_current_bad
        ],
        "worst_no_any_bad": [asdict(v) | {"ratio_float": v.ratio_float} for v in worst_no_any_bad],
    }
    text = json.dumps(data, indent=2)
    if args.json_out:
        args.json_out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
