#!/usr/bin/env python3
"""EP-488 v63 normalized pure-cycle motif enumerator.

The v62 q-census found 13 normalized pure-cycle motifs through q<=500. This
script derives motifs directly from the finite top-window edge-ratio alphabet:

    2:3, 3:4, 3:5, 4:5

It then filters by the real top-window feasibility inequality and constructs
one concrete (q,n,cycle) realization for each motif, checking the A4 pure-cycle
margin on that realization.

This is still not a proof of the pure-cycle theorem for all lengths. It is a
finite normalized census up to a requested cycle length.
"""

from __future__ import annotations

from fractions import Fraction
from functools import reduce
from math import ceil, gcd, lcm
import argparse
import json
import sys
import time

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from ep488_v57_checks import check_host_margin  # noqa: E402


EDGE_RATIOS = (Fraction(3, 2), Fraction(4, 3), Fraction(5, 3), Fraction(5, 4))


def canonical_cycle(cycle: list[Fraction]) -> tuple[Fraction, ...]:
    n = len(cycle)
    reps = []
    for seq in (cycle, list(reversed(cycle))):
        for i in range(n):
            reps.append(tuple(seq[i:] + seq[:i]))
    return min(reps)


def rational_nodes(max_len: int) -> list[Fraction]:
    nodes = {Fraction(1, 1)}
    frontier = {Fraction(1, 1)}
    for _ in range(max_len):
        new = set()
        for x in frontier:
            for r in EDGE_RATIOS:
                for y in (x * r, x / r):
                    if Fraction(1, 1) <= y < Fraction(2, 1) and y not in nodes:
                        new.add(y)
        nodes |= new
        frontier = new
    return sorted(nodes)


def ratio_graph(nodes: list[Fraction]) -> dict[Fraction, set[Fraction]]:
    adj = {x: set() for x in nodes}
    for i, a in enumerate(nodes):
        for b in nodes[i + 1 :]:
            if b / a in EDGE_RATIOS:
                adj[a].add(b)
                adj[b].add(a)
    return adj


def integer_cycle(cycle: tuple[Fraction, ...]) -> tuple[int, ...]:
    den = 1
    for x in cycle:
        den = lcm(den, x.denominator)
    arr = [x.numerator * (den // x.denominator) for x in cycle]
    g = reduce(gcd, arr)
    return tuple(a // g for a in arr)


def cycle_edges(cycle: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)]))) for i in range(len(cycle)))


def cycle_lcm(cycle: tuple[int, ...]) -> int:
    out = 1
    for a in cycle:
        out = lcm(out, a)
    return out


def feasibility(cycle: tuple[int, ...]) -> tuple[bool, Fraction, Fraction, int]:
    edge_max = max(lcm(a, b) for a, b in cycle_edges(cycle))
    lower = max(Fraction(max(cycle), 1), Fraction(edge_max, 3))
    upper = Fraction(2 * min(cycle), 1)
    return lower < upper, lower, upper, edge_max


def find_realization(cycle: tuple[int, ...], max_scale: int = 5000) -> dict[str, object] | None:
    ok, lower, upper, edge_max = feasibility(cycle)
    if not ok:
        return None
    edges = cycle_edges(cycle)
    for scale in range(1, max_scale + 1):
        q_min = lower * scale
        q_max = upper * scale
        lo = q_min.numerator // q_min.denominator + 1
        hi = (q_max.numerator - 1) // q_max.denominator
        for q in range(lo, hi + 1):
            actual_cycle = tuple(a * scale for a in cycle)
            actual_edges = cycle_edges(actual_cycle)
            if any(lcm(a, b) % q == 0 for a, b in actual_edges):
                continue
            n_lo = max(ceil(Fraction(5 * q, 2)), edge_max * scale)
            n_hi = 3 * q - 1
            if n_lo <= n_hi:
                return {
                    "scale": scale,
                    "q": q,
                    "n": n_lo,
                    "cycle": list(actual_cycle),
                    "edges": [list(e) for e in actual_edges],
                    "L_cyc": cycle_lcm(actual_cycle),
                    "edge_max": edge_max * scale,
                }
    return None


def enumerate_motifs(max_len: int) -> list[dict[str, object]]:
    nodes = rational_nodes(max_len)
    adj = ratio_graph(nodes)
    start = Fraction(1, 1)
    stack = [(start, [start], {start})]
    by_norm: dict[tuple[int, ...], dict[str, object]] = {}
    while stack:
        v, path, seen = stack.pop()
        if len(path) > max_len:
            continue
        for w in adj[v]:
            if w == start and len(path) >= 3:
                rat_cycle = canonical_cycle(path[:])
                int_ordered = integer_cycle(rat_cycle)
                ok, lower, upper, edge_max = feasibility(int_ordered)
                if not ok:
                    continue
                norm = tuple(sorted(int_ordered))
                if norm not in by_norm:
                    realization = find_realization(int_ordered)
                    margin = None
                    if realization is not None:
                        cycle = tuple(realization["cycle"])
                        edges = tuple(tuple(e) for e in realization["edges"])
                        host_ok, worst = check_host_margin(
                            int(realization["q"]),
                            int(realization["n"]),
                            cycle,
                            edges,
                            min(6 * int(realization["n"]), int(realization["n"]) + 5000),
                        )
                        margin = {
                            "ok": host_ok,
                            "worst": list(worst),
                        }
                    by_norm[norm] = {
                        "normalized_cycle": list(norm),
                        "ordered_cycle": list(int_ordered),
                        "length": len(norm),
                        "L_cyc_normalized": cycle_lcm(norm),
                        "edge_max_normalized": edge_max,
                        "s_lower": str(lower),
                        "s_upper": str(upper),
                        "realization": realization,
                        "a4_check": margin,
                    }
            elif w not in seen and len(path) < max_len:
                stack.append((w, path + [w], seen | {w}))
    return sorted(by_norm.values(), key=lambda x: (x["length"], x["normalized_cycle"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-len", type=int, default=12)
    parser.add_argument("--json-out", default="ep488_v63_a4_normalized_cycle_motifs.json")
    args = parser.parse_args()

    start = time.time()
    motifs = enumerate_motifs(args.max_len)
    result = {
        "max_len": args.max_len,
        "edge_ratios": [str(r) for r in EDGE_RATIOS],
        "motifs": motifs,
        "failures": [m for m in motifs if not m["a4_check"] or not m["a4_check"]["ok"]],
        "elapsed_seconds": time.time() - start,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    length_counts: dict[int, int] = {}
    for motif in motifs:
        length_counts[motif["length"]] = length_counts.get(motif["length"], 0) + 1
    print(
        f"max_len={args.max_len} motifs={len(motifs)} length_counts={length_counts} "
        f"failures={len(result['failures'])} elapsed_seconds={result['elapsed_seconds']:.2f}"
    )
    for motif in motifs:
        r = motif["realization"]
        a4 = motif["a4_check"]
        print(
            f"len={motif['length']} norm={motif['normalized_cycle']} "
            f"q={r and r['q']} n={r and r['n']} "
            f"margin={a4 and a4['worst'][0]}"
        )
    return 1 if result["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
