#!/usr/bin/env python3
"""EP-488 v68 scale-free crude bounds for A4 pure-cycle motifs.

For a fixed normalized ordered pure cycle P and any realization P*s, this
script tries to prove A4 by separating:

  1. a q,n-independent lower bound for 2H_Z#(n)/n, and
  2. a q-independent periodic upper envelope for N_Z(m)/m.

The result is a rigorous sufficient condition for each fixed normalized motif.
It is not a complete pure-cycle theorem if some motifs fail the crude bound.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, floor, gcd, lcm
import argparse
import json


def cycle_edges(cycle: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(lcm(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle)))


def cycle_lcm(cycle: tuple[int, ...]) -> int:
    out = 1
    for a in cycle:
        out = lcm(out, a)
    return out


def feasibility_bounds(cycle: tuple[int, ...]) -> tuple[Fraction, Fraction, int]:
    emax = max(cycle_edges(cycle))
    lower = max(Fraction(max(cycle), 1), Fraction(emax, 3))
    upper = Fraction(2 * min(cycle), 1)
    return lower, upper, emax


def min_h(lower: Fraction, d: int, forbid_divisibility: bool) -> int:
    """Lower bound h=q/gcd(ds,q).

    Since q/s > lower and gcd(ds,q) <= ds, h > lower/d. If q cannot divide
    ds, then h >= 2.
    """
    h = floor(lower / d) + 1
    if forbid_divisibility:
        h = max(h, 2)
    return h


def h_lower_vertex_terms(cycle: tuple[int, ...], y: int, lower: Fraction) -> int:
    total = 0
    for p in cycle:
        hp = min_h(lower, p, True)
        total += y // p - y // (p * hp)
    for e in cycle_edges(cycle):
        total -= y // e
    return total


def lower_B_constant(cycle: tuple[int, ...]) -> dict[str, object]:
    lower, upper, emax = feasibility_bounds(cycle)
    # n/s < 3 upper, so floor(n/s) <= ceil(3 upper)-1.
    y_min = emax
    y_max = ceil(3 * upper) - 1
    rows = []
    best = None
    for y in range(y_min, y_max + 1):
        H = h_lower_vertex_terms(cycle, y, lower)
        value = Fraction(2 * H, y + 1)
        row = {"y": y, "H_lower": H, "B_lower_const": str(value)}
        rows.append(row)
        if best is None or value < best[0]:
            best = (value, row)
    assert best is not None
    return {
        "lower": str(lower),
        "upper": str(upper),
        "edge_max": emax,
        "y_min": y_min,
        "y_max": y_max,
        "B_lower_const": str(best[0]),
        "worst_y": best[1],
        "rows": rows,
    }


def upper_envelope_data(cycle: tuple[int, ...]) -> dict[str, object]:
    lower, _, emax = feasibility_bounds(cycle)
    edges = cycle_edges(cycle)
    L = cycle_lcm(cycle)
    edge_corr = [e * min_h(lower, e, True) for e in edges]
    denoms = list(cycle) + list(edges) + edge_corr
    period = 1
    for d in denoms:
        period = lcm(period, d)
    slope = (
        sum(Fraction(1, p) for p in cycle)
        - sum(Fraction(1, e) for e in edges)
        + sum(Fraction(1, r) for r in edge_corr)
    )
    return {
        "edge_lcms": list(edges),
        "cycle_lcm": L,
        "edge_correction_denoms": edge_corr,
        "period": period,
        "slope_without_cycle_lcm": str(slope),
        "k_min": emax,
    }


def A0(cycle: tuple[int, ...], k: int) -> int:
    lower, _, _ = feasibility_bounds(cycle)
    edges = cycle_edges(cycle)
    edge_corr = [e * min_h(lower, e, True) for e in edges]
    return (
        sum(k // p for p in cycle)
        - sum(k // e for e in edges)
        + sum(k // r for r in edge_corr)
    )


def prove_motif(cycle: tuple[int, ...], period_cap: int) -> dict[str, object]:
    lower_data = lower_B_constant(cycle)
    upper_data = upper_envelope_data(cycle)
    B0 = Fraction(lower_data["B_lower_const"])
    L = int(upper_data["cycle_lcm"])
    target = B0 - Fraction(1, L)
    slope = Fraction(upper_data["slope_without_cycle_lcm"])
    period = int(upper_data["period"])
    k_min = int(upper_data["k_min"])

    result: dict[str, object] = {
        "ordered_cycle": list(cycle),
        "normalized_cycle": sorted(cycle),
        "length": len(cycle),
        "lower": lower_data,
        "upper": upper_data,
        "target_without_cycle_lcm": str(target),
        "status": "unknown",
    }
    if target <= 0:
        result["status"] = "target_nonpositive"
        return result
    if slope > target:
        result["status"] = "slope_exceeds_target"
        return result
    if period > period_cap:
        result["status"] = "period_too_large"
        return result

    worst = None
    failures = []
    for k in range(k_min, k_min + period):
        value = A0(cycle, k)
        margin = target * k - value
        row = {
            "k": k,
            "A0": value,
            "A0_over_k": str(Fraction(value, k)),
            "margin": str(margin),
        }
        if worst is None or margin < worst[0]:
            worst = (margin, row)
        if margin < 0:
            failures.append(row)
            if len(failures) >= 20:
                break
    result["worst_period_row"] = worst[1] if worst else None
    result["failures"] = failures
    result["status"] = "proved" if not failures else "period_failure"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--motifs-json", default="ep488_v63_a4_normalized_cycle_motifs_len16.json")
    parser.add_argument("--period-cap", type=int, default=2_000_000)
    parser.add_argument("--json-out", default="ep488_v68_a4_motif_crude_bounds.json")
    args = parser.parse_args()

    data = json.load(open(args.motifs_json, encoding="utf-8"))
    rows = []
    counts: dict[str, int] = {}
    for motif in data["motifs"]:
        cycle = tuple(int(x) for x in motif["ordered_cycle"])
        row = prove_motif(cycle, args.period_cap)
        rows.append(row)
        counts[row["status"]] = counts.get(row["status"], 0) + 1

    result = {
        "motifs_json": args.motifs_json,
        "period_cap": args.period_cap,
        "status_counts": counts,
        "rows": rows,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"status_counts={counts}")
    for status in sorted(counts):
        examples = [r for r in rows if r["status"] == status][:5]
        for r in examples:
            print(
                f"{status}: len={r['length']} norm={r['normalized_cycle']} "
                f"B0={r['lower']['B_lower_const']} period={r['upper']['period']} "
                f"target={r['target_without_cycle_lcm']}"
            )
    return 1 if counts.get("period_failure") else 0


if __name__ == "__main__":
    raise SystemExit(main())
