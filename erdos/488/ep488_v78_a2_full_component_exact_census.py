#!/usr/bin/env python3
"""EP-488 v78 exact full-component high-defect census.

This is an exact-n companion to the v58 sampled full-component census.  It
uses an incremental q-excluded lcm graph scan over the top window

    n in [ceil(5q/2), 3q)

so each q is scanned over every admissible n.  The model is still the v58
"full top-window component" model; it does not enumerate arbitrary induced
subsets.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import lcm
from pathlib import Path
from typing import Iterable

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze  # noqa: E402

from ep488_v58_full_component_census import finite_certificate  # noqa: E402


@dataclass(frozen=True)
class CensusConfig:
    q_values: tuple[int, ...]
    max_cert_size: int
    max_cutoff: int


class DSU:
    def __init__(self, vertices: Iterable[int]):
        self.parent = {v: v for v in vertices}
        self.size = {v: 1 for v in vertices}
        self.edge_count = {v: 0 for v in vertices}
        self.tau_count = {v: 0 for v in vertices}

    def find(self, v: int) -> int:
        path = []
        while self.parent[v] != v:
            path.append(v)
            v = self.parent[v]
        for u in path:
            self.parent[u] = v
        return v

    def add_edge(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            self.edge_count[ra] += 1
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.edge_count[ra] += self.edge_count[rb] + 1
        self.tau_count[ra] += self.tau_count[rb]

    def add_tau(self, fiber: tuple[int, int, int]) -> None:
        root = self.find(fiber[0])
        self.tau_count[root] += 1

    def component_map(self) -> dict[int, list[int]]:
        comps: dict[int, list[int]] = defaultdict(list)
        for v in self.parent:
            comps[self.find(v)].append(v)
        return comps

    def active_component_roots(self) -> list[int]:
        roots = []
        for root, vertices in self.component_map().items():
            if len(vertices) >= 3 and self.edge_count[self.find(root)] > 0:
                roots.append(self.find(root))
        return roots


def ceil_5q_over_2(q: int) -> int:
    return (5 * q + 1) // 2


def parse_range_token(token: str) -> list[int]:
    if "-" in token:
        left, right = token.split("-", 1)
        start = int(left)
        end = int(right)
        if end < start:
            raise ValueError(f"bad q range {token!r}")
        return list(range(start, end + 1))
    return [int(token)]


def q_values_from_ranges(text: str) -> tuple[int, ...]:
    values: set[int] = set()
    for raw in text.split(","):
        token = raw.strip()
        if not token:
            continue
        values.update(parse_range_token(token))
    return tuple(sorted(values))


def q_values_from_source(source: Path, expand: int = 0) -> tuple[int, ...]:
    data = json.loads(source.read_text(encoding="utf-8"))
    values: set[int] = set()
    for row in data.get("high_defect_rows", []):
        q = int(row["q"])
        values.update(range(max(10, q - expand), q + expand + 1))
    return tuple(sorted(values))


def edge_events_for_q(q: int, vertices: list[int], n_end: int) -> dict[int, list[tuple[int, int]]]:
    events: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i, a in enumerate(vertices):
        for b in vertices[i + 1 :]:
            L = lcm(a, b)
            if L < n_end and L % q != 0:
                events[L].append((a, b))
    return events


def tau_events_for_q(q: int, vertices: list[int], n_end: int) -> dict[int, list[tuple[int, int, int]]]:
    fibers: dict[int, list[int]] = defaultdict(list)
    for a in vertices:
        for t in range(a, n_end, a):
            if t % q != 0:
                fibers[t].append(a)
    return {
        t: [tuple(sorted(fiber))]  # type: ignore[list-item]
        for t, fiber in fibers.items()
        if len(fiber) == 3
    }


def certified_sort_key(row: dict[str, object]) -> Fraction:
    cert = row["certificate"]
    if not isinstance(cert, dict):
        return Fraction(0, 1)
    value = cert.get("best_over_B")
    return Fraction(str(value)) if value else Fraction(0, 1)


def exact_q_scan(q: int, config: CensusConfig) -> tuple[int, list[dict[str, object]], dict[str, int]]:
    vertices = list(range(q // 2 + 1, q))
    n_start = ceil_5q_over_2(q)
    n_end = 3 * q
    edge_events = edge_events_for_q(q, vertices, n_end)
    tau_events = tau_events_for_q(q, vertices, n_end)
    dsu = DSU(vertices)

    high_defect_rows: list[dict[str, object]] = []
    status_counts: dict[str, int] = {}
    component_count = 0

    def process_events_up_to(n: int, edge_cursor: int, tau_cursor: int) -> tuple[int, int]:
        while edge_cursor <= n:
            for a, b in edge_events.get(edge_cursor, []):
                dsu.add_edge(a, b)
            edge_cursor += 1
        while tau_cursor <= n:
            for fiber in tau_events.get(tau_cursor, []):
                dsu.add_tau(fiber)
            tau_cursor += 1
        return edge_cursor, tau_cursor

    edge_cursor = 1
    tau_cursor = 1
    edge_cursor, tau_cursor = process_events_up_to(n_start, edge_cursor, tau_cursor)

    for n in range(n_start, n_end):
        if n > n_start:
            edge_cursor, tau_cursor = process_events_up_to(n, edge_cursor, tau_cursor)

        comps = dsu.component_map()
        for root, comp_raw in comps.items():
            root = dsu.find(root)
            comp_edges = dsu.edge_count[root]
            if len(comp_raw) < 3 or comp_edges == 0:
                continue
            component_count += 1
            cyclomatic = comp_edges - len(comp_raw) + 1
            epsilon = cyclomatic - dsu.tau_count[root]
            if epsilon < 2:
                continue

            C = tuple(sorted(comp_raw))
            report = analyze(C, n, q)
            if report.eps_n != epsilon or report.cyclomatic != cyclomatic:
                raise RuntimeError(
                    f"incremental mismatch q={q} n={n} C={C}: "
                    f"eps {epsilon} vs {report.eps_n}, cyc {cyclomatic} vs {report.cyclomatic}"
                )

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

    return component_count, high_defect_rows, status_counts


def full_component_exact_census(config: CensusConfig) -> dict[str, object]:
    all_rows: list[dict[str, object]] = []
    status_counts: dict[str, int] = {}
    component_count = 0

    for index, q in enumerate(config.q_values, start=1):
        q_component_count, q_rows, q_status = exact_q_scan(q, config)
        component_count += q_component_count
        all_rows.extend(q_rows)
        for status, count in q_status.items():
            status_counts[status] = status_counts.get(status, 0) + count
        if index == 1 or index % 25 == 0 or q_rows:
            print(
                f"q={q} ({index}/{len(config.q_values)}) "
                f"components={q_component_count} high_defect={len(q_rows)} "
                f"status={q_status}",
                flush=True,
            )

    certified_rows = [
        row
        for row in all_rows
        if isinstance(row.get("certificate"), dict)
        and row["certificate"].get("status") == "certified"  # type: ignore[union-attr]
    ]
    certified_rows.sort(key=certified_sort_key, reverse=True)
    all_rows.sort(key=lambda row: (row["q"], row["n"], row["size"], row["C"]))
    return {
        "q_values": list(config.q_values),
        "q_min": min(config.q_values) if config.q_values else None,
        "q_max": max(config.q_values) if config.q_values else None,
        "q_count": len(config.q_values),
        "max_cert_size": config.max_cert_size,
        "max_cutoff": config.max_cutoff,
        "component_count": component_count,
        "high_defect_count": len(all_rows),
        "status_counts": status_counts,
        "top_certified_by_best_over_B": certified_rows[:20],
        "high_defect_rows": all_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-min", type=int, default=None)
    parser.add_argument("--q-max", type=int, default=None)
    parser.add_argument("--q-ranges", default=None, help="Comma-separated q values/ranges, e.g. 427-431,451-479")
    parser.add_argument("--source", default=None, help="Use q values appearing in source high_defect_rows")
    parser.add_argument("--expand-source-q", type=int, default=0)
    parser.add_argument("--max-cert-size", type=int, default=24)
    parser.add_argument("--max-cutoff", type=int, default=10_000_000)
    parser.add_argument("--json-out", default="ep488_v78_a2_full_component_exact_census.json")
    args = parser.parse_args()

    if args.q_ranges:
        q_values = q_values_from_ranges(args.q_ranges)
    elif args.source:
        q_values = q_values_from_source(Path(args.source), args.expand_source_q)
    elif args.q_min is not None and args.q_max is not None:
        q_values = tuple(range(args.q_min, args.q_max + 1))
    else:
        parser.error("provide --q-ranges, --source, or --q-min/--q-max")

    start = time.time()
    result = full_component_exact_census(
        CensusConfig(
            q_values=q_values,
            max_cert_size=args.max_cert_size,
            max_cutoff=args.max_cutoff,
        )
    )
    result["elapsed_seconds"] = time.time() - start

    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"q_count={result['q_count']} q_min={result['q_min']} q_max={result['q_max']} "
        f"components={result['component_count']} high_defect={result['high_defect_count']} "
        f"status_counts={result['status_counts']} elapsed_seconds={result['elapsed_seconds']:.2f}"
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
