#!/usr/bin/env python3
"""EP-488 v59 theta-core plus near-q isolate search.

The v56 strongest recorded near-miss used the theta13 core scaled by 149 plus
six isolated vertices. This script tests whether that isolate layer is locally
optimized. It is not: greedy near-q isolated vertices give stronger certified
near-misses while remaining safely below the EP bound.

The search is deliberately narrow:
- q = 71440, n = 213189, m = 3411504 are fixed to the v56 near-miss values.
- The cyclic core is theta13 scaled by 149.
- Candidate added vertices must be isolated from the theta core in B_n(C,q).
- Greedy fitness is the exact fixed-m ratio
      (D_C(m)/m) / (2D_C(n)/n).
- Prefixes of the greedy isolate list are then checked with the existing exact
  finite-certificate theorem while the cutoff remains feasible.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import lcm
import argparse
import json
import sys
import time

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import D_C, analyze  # noqa: E402

from ep488_v58_full_component_census import finite_certificate  # noqa: E402


Q = 71440
N = 213189
M = 3411504
SCALE = 149
THETA13_BASE = (240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450)
THETA_CORE = tuple(a * SCALE for a in THETA13_BASE)


@dataclass(frozen=True)
class GreedyStep:
    step: int
    vertex: int
    gain_n: int
    gain_m: int
    ratio: Fraction


def no_bn_edge(a: int, b: int, q: int = Q, n: int = N) -> bool:
    L = lcm(a, b)
    return L > n or L % q == 0


def add_hits(hit: bytearray, limit: int, a: int, q: int = Q) -> int:
    gain = 0
    for x in range(a, limit + 1, a):
        if x % q and not hit[x]:
            hit[x] = 1
            gain += 1
    return gain


def gain_against(hit: bytearray, limit: int, a: int, q: int = Q) -> int:
    gain = 0
    for x in range(a, limit + 1, a):
        if x % q and not hit[x]:
            gain += 1
    return gain


def core_hits() -> tuple[bytearray, bytearray, int, int]:
    hit_n = bytearray(N + 1)
    hit_m = bytearray(M + 1)
    D_n = 0
    D_m = 0
    for a in THETA_CORE:
        D_n += add_hits(hit_n, N, a)
        D_m += add_hits(hit_m, M, a)
    return hit_n, hit_m, D_n, D_m


def ratio(D_n: int, D_m: int) -> Fraction:
    return Fraction(D_m, M) / Fraction(2 * D_n, N)


def greedy_isolates(max_steps: int) -> tuple[list[GreedyStep], int, int]:
    hit_n, hit_m, D_n, D_m = core_hits()
    candidates = [
        a
        for a in range(Q // 2 + 1, Q)
        if a not in THETA_CORE and all(no_bn_edge(a, b) for b in THETA_CORE)
    ]
    selected: list[int] = []
    steps: list[GreedyStep] = []

    for step in range(max_steps):
        current = ratio(D_n, D_m)
        best: tuple[Fraction, int, int, int] | None = None
        for a in candidates:
            if any(not no_bn_edge(a, b) for b in selected):
                continue
            gain_n = gain_against(hit_n, N, a)
            if gain_n == 0:
                continue
            gain_m = gain_against(hit_m, M, a)
            candidate_ratio = ratio(D_n + gain_n, D_m + gain_m)
            if best is None or candidate_ratio > best[0]:
                best = (candidate_ratio, a, gain_n, gain_m)

        if best is None or best[0] <= current:
            break

        best_ratio, vertex, gain_n, gain_m = best
        selected.append(vertex)
        D_n += add_hits(hit_n, N, vertex)
        D_m += add_hits(hit_m, M, vertex)
        candidates = [a for a in candidates if a != vertex and no_bn_edge(a, vertex)]
        steps.append(GreedyStep(step + 1, vertex, gain_n, gain_m, best_ratio))

    return steps, D_n, D_m


def certify_prefixes(vertices: list[int], max_cert_k: int, max_cutoff: int) -> list[dict[str, object]]:
    rows = []
    for k in range(0, min(max_cert_k, len(vertices)) + 1):
        C = tuple(sorted(THETA_CORE + tuple(vertices[:k])))
        report = analyze(C, N, Q)
        D_m = D_C(C, M, Q)
        fixed_ratio = ratio(report.D_C_n, D_m)
        cert = finite_certificate(C, Q, N, report.D_C_n, max_cutoff)
        rows.append(
            {
                "k": k,
                "size": len(C),
                "q": Q,
                "n": N,
                "m": M,
                "C": list(C),
                "epsilon": report.eps_n,
                "cyclomatic": report.cyclomatic,
                "tau": report.tau_n,
                "D_n": report.D_C_n,
                "D_m": D_m,
                "fixed_m_ratio": str(fixed_ratio),
                "fixed_m_ratio_float": float(fixed_ratio),
                "certificate": cert,
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-greedy", type=int, default=10)
    parser.add_argument("--max-cert-k", type=int, default=10)
    parser.add_argument("--max-cutoff", type=int, default=80_000_000)
    parser.add_argument("--json-out", default="ep488_v59_theta_isolate_search.json")
    args = parser.parse_args()

    start = time.time()
    steps, final_D_n, final_D_m = greedy_isolates(args.max_greedy)
    vertices = [s.vertex for s in steps]
    rows = certify_prefixes(vertices, args.max_cert_k, args.max_cutoff)
    result = {
        "q": Q,
        "n": N,
        "m": M,
        "scale": SCALE,
        "theta_core": list(THETA_CORE),
        "greedy_steps": [
            {
                "step": s.step,
                "vertex": s.vertex,
                "gain_n": s.gain_n,
                "gain_m": s.gain_m,
                "ratio": str(s.ratio),
                "ratio_float": float(s.ratio),
            }
            for s in steps
        ],
        "final_greedy_D_n": final_D_n,
        "final_greedy_D_m": final_D_m,
        "prefix_certificates": rows,
        "elapsed_seconds": time.time() - start,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"greedy_vertices={vertices} final_fixed_ratio={ratio(final_D_n, final_D_m)} "
        f"elapsed_seconds={result['elapsed_seconds']:.2f}"
    )
    for row in rows:
        cert = row["certificate"]
        print(
            f"k={row['k']} size={row['size']} epsilon={row['epsilon']} "
            f"D_n={row['D_n']} D_m={row['D_m']} fixed={row['fixed_m_ratio']} "
            f"status={cert['status']} cutoff={cert.get('cutoff')} "
            f"best_over_B={cert.get('best_over_B')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
