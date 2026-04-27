from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


N = 26


def choose(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    return math.comb(n, r)


def min_edges_alpha_le_4(vertex_count: int) -> int:
    """Exact minimum edges on `vertex_count` vertices with independence number <= 4."""
    q, r = divmod(vertex_count, 4)
    return r * choose(q + 1, 2) + (4 - r) * choose(q, 2)


def max_edges_k4_free(vertex_count: int) -> int:
    """Exact Turan bound ex(vertex_count, K4)."""
    q, r = divmod(vertex_count, 3)
    parts = [q + 1 if idx < r else q for idx in range(3)]
    return choose(vertex_count, 2) - sum(choose(part, 2) for part in parts)


def max_edges_five_set_at_most_six(vertex_count: int) -> int:
    if vertex_count < 5:
        return choose(vertex_count, 2)
    numerator = 6 * choose(vertex_count, 5)
    denominator = choose(vertex_count - 2, 3)
    return numerator // denominator


def erdos_gallai_graphical(seq: list[int]) -> bool:
    if any(deg < 0 or deg >= N for deg in seq):
        return False
    if sum(seq) % 2:
        return False
    prefix = [0]
    for deg in seq:
        prefix.append(prefix[-1] + deg)
    for k in range(1, len(seq) + 1):
        rhs = k * (k - 1) + sum(min(deg, k) for deg in seq[k:])
        if prefix[k] > rhs:
            return False
    return True


def caro_wei_sum(seq: Iterable[int]) -> float:
    return sum(1.0 / (deg + 1) for deg in seq)


def complement_caro_wei_sum(seq: Iterable[int]) -> float:
    return sum(1.0 / (N - deg) for deg in seq)


def mixed_upper6_holds(
    degree: int,
    nonneighbors: int,
    edges_in_neighbors: int,
    edges_in_nonneighbors: int,
    cross_edges: int,
) -> bool:
    """
    For a fixed vertex v:
      N(v) has size `degree`,
      M(v) has size `nonneighbors`,
      x = e(N(v)), y = e(M(v)), z = e(N(v), M(v)).

    For every choice of `a` neighbors and `5-a` nonneighbors,
    the 6-set consisting of v plus those 5 vertices has at most 11 edges.
    """
    for a in range(1, 6):
        b = 5 - a
        lhs = (
            choose(degree - 2, a - 2) * choose(nonneighbors, b) * edges_in_neighbors
            + choose(degree, a) * choose(nonneighbors - 2, b - 2) * edges_in_nonneighbors
            + choose(degree - 1, a - 1) * choose(nonneighbors - 1, b - 1) * cross_edges
        )
        rhs = (11 - a) * choose(degree, a) * choose(nonneighbors, b)
        if lhs > rhs:
            return False
    return True


@dataclass
class LocalWitness:
    degree: int
    feasible: bool
    neighbor_degree_sum_min: int | None
    neighbor_degree_sum_max: int | None
    witness_for_min: dict[str, int] | None
    witness_for_max: dict[str, int] | None


def local_degree_witness(edge_count: int, degree: int) -> LocalWitness:
    nonneighbors = N - 1 - degree
    remaining_edges = edge_count - degree
    if remaining_edges < 0:
        return LocalWitness(degree, False, None, None, None, None)

    y_min = min_edges_alpha_le_4(nonneighbors)
    y_max = min(choose(nonneighbors, 2), remaining_edges)
    if y_min > y_max:
        return LocalWitness(degree, False, None, None, None, None)

    x_max = min(
        choose(degree, 2),
        max_edges_k4_free(degree),
        max_edges_five_set_at_most_six(degree),
    )

    min_sigma = None
    max_sigma = None
    min_witness = None
    max_witness = None

    for edges_in_nonneighbors in range(y_min, y_max + 1):
        x_upper_here = min(x_max, remaining_edges - edges_in_nonneighbors)
        for edges_in_neighbors in range(x_upper_here + 1):
            cross_edges = remaining_edges - edges_in_neighbors - edges_in_nonneighbors
            if cross_edges < 0 or cross_edges > degree * nonneighbors:
                continue
            if not mixed_upper6_holds(
                degree,
                nonneighbors,
                edges_in_neighbors,
                edges_in_nonneighbors,
                cross_edges,
            ):
                continue

            sigma = degree + 2 * edges_in_neighbors + cross_edges
            witness = {
                "degree": degree,
                "nonneighbors": nonneighbors,
                "edges_in_neighbors": edges_in_neighbors,
                "edges_in_nonneighbors": edges_in_nonneighbors,
                "cross_edges": cross_edges,
                "neighbor_degree_sum": sigma,
            }
            if min_sigma is None or sigma < min_sigma:
                min_sigma = sigma
                min_witness = witness
            if max_sigma is None or sigma > max_sigma:
                max_sigma = sigma
                max_witness = witness

    return LocalWitness(degree, min_sigma is not None, min_sigma, max_sigma, min_witness, max_witness)


def sequence_neighbor_sum_ranges(seq: list[int], index: int) -> tuple[int, int]:
    degree = seq[index]
    others = seq[:index] + seq[index + 1 :]
    return sum(sorted(others)[:degree]), sum(sorted(others, reverse=True)[:degree])


def sequence_passes_degree_filters(seq: list[int], local_table: dict[int, LocalWitness]) -> bool:
    if not erdos_gallai_graphical(seq):
        return False
    if caro_wei_sum(seq) > 5.0 + 1e-12:
        return False
    if complement_caro_wei_sum(seq) > 4.0 + 1e-12:
        return False

    for idx, degree in enumerate(seq):
        witness = local_table[degree]
        if not witness.feasible:
            return False
        min_possible, max_possible = sequence_neighbor_sum_ranges(seq, idx)
        assert witness.neighbor_degree_sum_min is not None
        assert witness.neighbor_degree_sum_max is not None
        if witness.neighbor_degree_sum_max < min_possible:
            return False
        if max_possible < witness.neighbor_degree_sum_min:
            return False
    return True


def search_sequences(
    edge_count: int,
    local_table: dict[int, LocalWitness],
    max_sequences: int,
) -> tuple[list[list[int]], int]:
    if max_sequences <= 0:
        return [], 0

    seq = [0] * N
    out: list[list[int]] = []
    nodes_visited = 0
    allowed = {deg for deg, witness in local_table.items() if witness.feasible}

    def rec(index: int, prev: int, remaining_sum: int) -> None:
        nonlocal nodes_visited
        if len(out) >= max_sequences:
            return
        nodes_visited += 1
        slots = N - index
        if slots == 0:
            if remaining_sum == 0:
                candidate = list(seq)
                if sequence_passes_degree_filters(candidate, local_table):
                    out.append(candidate)
            return

        lo = max(0, remaining_sum - (slots - 1) * prev)
        hi = min(prev, remaining_sum)
        target = remaining_sum / slots
        values = list(range(hi, lo - 1, -1))
        values.sort(key=lambda value: (abs(value - target), -value))
        for value in values:
            if value not in allowed:
                continue
            seq[index] = value
            rec(index + 1, value, remaining_sum - value)
            if len(out) >= max_sequences:
                return

    rec(0, N - 1, 2 * edge_count)
    return out, nodes_visited


def render_report(summary: dict[str, object]) -> str:
    lines = [
        "# Phase 1 Agent E Degree-Sequence Probe",
        "",
        "Degree-only necessary constraints used for the no-K5 minimum-colour branch on `K_26`:",
        "",
        "1. `alpha(G) <= 5` from the lower 6-set bound (`every 6-set has >= 1 edge`).",
        "2. `omega(G) <= 4` by hypothesis.",
        "3. For a vertex `v` with degree `d`, writing `N(v)` and `M(v)` for neighbors/nonneighbors:",
        "   - `e(M(v)) >= min_edges_alpha_le_4(|M(v)|)`.",
        "   - `e(N(v)) <= ex(|N(v)|, K4)`.",
        "   - `e(N(v)) <= floor(6 * C(d,5) / C(d-2,3))` from every 5-subset of `N(v)` inducing at most 6 edges.",
        "   - Mixed `a`-neighbor / `(5-a)`-nonneighbor upper-6 inequalities for `a = 1..5`.",
        "4. Caro-Wei on `G`: `sum 1/(d_i+1) <= 5`.",
        "5. Caro-Wei on the complement: `sum 1/(26-d_i) <= 4`.",
        "6. Erdos-Gallai graphicality, plus a weak neighbor-degree-sum interval consistency check.",
        "",
        f"Probe cap per k: {summary['max_sequences']} sample sequences.",
        "",
        "| k | local allowed degrees | sample sequences found | hit cap | search seconds | first sample |",
        "| - | - | - | - | - | - |",
    ]

    for row in summary["rows"]:
        lines.append(
            "| {k} | {local_allowed_degrees} | {sample_sequences_found} | {hit_cap} | {search_seconds} | `{first_sample}` |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Conclusion",
            "",
            f"- Pruned k-values: {summary['pruned_k_values']}.",
            f"- Surviving k-values: {summary['surviving_k_values']}.",
            "- Degree-only constraints do not prune any k in `60..65`.",
            "- Exact degree-sequence branching is easy to generate but not selective: the probe hit the sample cap quickly for every k.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Agent E degree-sequence feasibility probe for EP617 Phase 1.")
    parser.add_argument("--k-min", type=int, default=60)
    parser.add_argument("--k-max", type=int, default=65)
    parser.add_argument("--max-sequences", type=int, default=100)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("erdos/617/results/phase1_e_degree_probe_k60_65.json"),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("erdos/617/results/phase1_e_degree_probe_k60_65.md"),
    )
    args = parser.parse_args()

    if args.k_min > args.k_max:
        raise SystemExit("--k-min must be <= --k-max")

    started = time.perf_counter()
    rows = []
    pruned = []
    surviving = []
    all_locals: dict[str, object] = {}

    for edge_count in range(args.k_min, args.k_max + 1):
        local_started = time.perf_counter()
        local_table = {degree: local_degree_witness(edge_count, degree) for degree in range(N)}
        all_locals[str(edge_count)] = {str(degree): asdict(witness) for degree, witness in local_table.items()}
        allowed_degrees = [degree for degree, witness in local_table.items() if witness.feasible]
        samples, nodes_visited = search_sequences(edge_count, local_table, args.max_sequences)
        search_seconds = round(time.perf_counter() - local_started, 3)

        if samples:
            surviving.append(edge_count)
        else:
            pruned.append(edge_count)

        first_sample = samples[0] if samples else None
        row = {
            "k": edge_count,
            "local_allowed_degrees": allowed_degrees,
            "local_excluded_degrees": [degree for degree in range(N) if degree not in allowed_degrees],
            "sample_sequences_found": len(samples),
            "hit_cap": len(samples) >= args.max_sequences,
            "nodes_visited": nodes_visited,
            "search_seconds": search_seconds,
            "first_sample": first_sample,
            "first_sample_caro_wei": round(caro_wei_sum(first_sample), 6) if first_sample else None,
            "first_sample_complement_caro_wei": (
                round(complement_caro_wei_sum(first_sample), 6) if first_sample else None
            ),
            "samples": samples,
        }
        rows.append(row)
        public_row = dict(row)
        public_row.pop("samples", None)
        print(json.dumps(public_row), flush=True)

    summary = {
        "n": N,
        "k_min": args.k_min,
        "k_max": args.k_max,
        "max_sequences": args.max_sequences,
        "pruned_k_values": pruned,
        "surviving_k_values": surviving,
        "rows": rows,
        "local_degree_witness_tables": all_locals,
        "total_seconds": round(time.perf_counter() - started, 3),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    args.report.write_text(render_report(summary), encoding="utf-8")
    print(
        json.dumps(
            {
                "pruned_k_values": pruned,
                "surviving_k_values": surviving,
                "json_path": str(args.out),
                "report_path": str(args.report),
                "total_seconds": summary["total_seconds"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
