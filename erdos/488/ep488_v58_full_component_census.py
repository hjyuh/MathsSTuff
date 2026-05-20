#!/usr/bin/env python3
"""EP-488 v58 sampled full-component high-defect census.

This script strengthens the Kimi full-top-window census by adding exact
finite-certificate data to every feasible high-defect component it finds.

Limitations:
- It analyzes connected components of the full top-window graph on
  {floor(q/2)+1, ..., q-1}; it is not an induced-subset census.
- For q > 100 it samples n-values, matching the Kimi search style.
- It skips exact finite certificates for components above max_cert_size.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import lcm
import argparse
import json
import sys
import time

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze, connected_components, lcm_graph_edges  # noqa: E402

from ep488_v57_checks import grouped_density, prefix_counts  # noqa: E402


@dataclass(frozen=True)
class CensusConfig:
    q_max: int
    max_cert_size: int
    max_cutoff: int


def n_values_for_q(q: int) -> list[int]:
    start = (5 * q + 1) // 2
    end = 3 * q
    if q <= 100:
        return list(range(start, end))
    step = max(1, (end - start) // 20)
    values = list(range(start, end, step))
    if end - 1 not in values:
        values.append(end - 1)
    return values


def finite_certificate(C: tuple[int, ...], q: int, n: int, D_n: int, max_cutoff: int) -> dict[str, object]:
    delta, E_abs, terms = grouped_density(C, q)
    B = Fraction(2 * D_n, n)
    eta = B - delta
    out: dict[str, object] = {
        "B": str(B),
        "delta": str(delta),
        "delta_over_B": str(delta / B) if B else None,
        "eta": str(eta),
        "E": str(E_abs),
        "terms": terms,
    }
    if eta <= 0:
        out["status"] = "eta_nonpositive"
        return out

    cutoff = E_abs.numerator * eta.denominator // (E_abs.denominator * eta.numerator)
    out["cutoff"] = cutoff
    if cutoff > max_cutoff:
        out["status"] = "large_cutoff"
        return out

    counts = prefix_counts(C, q, cutoff)
    best = (Fraction(0, 1), None, 0)
    failures = []
    for m in range(n + 1, cutoff + 1):
        value = Fraction(counts[m], m)
        if value > best[0]:
            best = (value, m, counts[m])
        if value > B:
            failures.append((m, counts[m], str(value)))

    out["status"] = "failure" if failures else "certified"
    out["best"] = (str(best[0]), best[1], best[2])
    out["best_over_B"] = str(best[0] / B) if B else None
    out["failures"] = failures[:20]
    return out


def full_component_census(config: CensusConfig) -> dict[str, object]:
    high_defect_rows = []
    status_counts: dict[str, int] = {}
    component_count = 0
    high_defect_count = 0

    for q in range(10, config.q_max + 1):
        vertices = list(range(q // 2 + 1, q))
        for n in n_values_for_q(q):
            edges = [tuple(e) for e in lcm_graph_edges(vertices, n, q)]
            if not edges:
                continue
            components = connected_components(vertices, edges)
            edge_set = set(edges)
            for comp_raw in components:
                C = tuple(sorted(comp_raw))
                if len(C) < 3:
                    continue
                C_set = set(C)
                comp_edges = [e for e in edge_set if e[0] in C_set and e[1] in C_set]
                if not comp_edges:
                    continue
                component_count += 1
                report = analyze(C, n, q)
                if report.eps_n < 2:
                    continue

                high_defect_count += 1
                row: dict[str, object] = {
                    "q": q,
                    "n": n,
                    "C": list(C),
                    "size": len(C),
                    "cyclomatic": report.cyclomatic,
                    "tau": report.tau_n,
                    "epsilon": report.eps_n,
                    "D_n": report.D_C_n,
                    "target_holds": report.target_holds,
                }

                if len(C) <= config.max_cert_size:
                    cert = finite_certificate(C, q, n, report.D_C_n, config.max_cutoff)
                else:
                    cert = {"status": "component_too_large"}
                row["certificate"] = cert
                status = str(cert["status"])
                status_counts[status] = status_counts.get(status, 0) + 1
                high_defect_rows.append(row)

    certified_rows = [r for r in high_defect_rows if r["certificate"]["status"] == "certified"]
    certified_rows.sort(
        key=lambda r: Fraction(str(r["certificate"].get("best_over_B", "0"))),
        reverse=True,
    )
    high_defect_rows.sort(key=lambda r: (r["q"], r["n"], r["size"]))
    return {
        "q_max": config.q_max,
        "max_cert_size": config.max_cert_size,
        "max_cutoff": config.max_cutoff,
        "component_count": component_count,
        "high_defect_count": high_defect_count,
        "status_counts": status_counts,
        "top_certified_by_best_over_B": certified_rows[:20],
        "high_defect_rows": high_defect_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=500)
    parser.add_argument("--max-cert-size", type=int, default=22)
    parser.add_argument("--max-cutoff", type=int, default=10_000_000)
    parser.add_argument("--json-out", default="ep488_v58_full_component_census.json")
    args = parser.parse_args()

    start = time.time()
    config = CensusConfig(args.q_max, args.max_cert_size, args.max_cutoff)
    result = full_component_census(config)
    result["elapsed_seconds"] = time.time() - start

    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"q_max={result['q_max']} components={result['component_count']} "
        f"high_defect={result['high_defect_count']} status_counts={result['status_counts']} "
        f"elapsed_seconds={result['elapsed_seconds']:.2f}"
    )
    for row in result["top_certified_by_best_over_B"][:10]:
        cert = row["certificate"]
        print(
            f"best_over_B={cert['best_over_B']} q={row['q']} n={row['n']} "
            f"size={row['size']} epsilon={row['epsilon']} best={cert['best']} C={row['C']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
