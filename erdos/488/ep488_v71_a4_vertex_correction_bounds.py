#!/usr/bin/env python3
"""EP-488 v71 correction-aware A4 pure-cycle motif certificate.

This extends v70. Positive q-excluded vertex corrections are allowed, but they
are grouped by the forced rational value of q/s. For each possible y=floor(n/s)
we subtract only corrections that can occur for a single q/s state.

The m-side envelope remains q-independent:

  c_m(ps;q) <= floor(k/p)
  -c_m(es;q) <= -floor(k/e) + floor(k/(2e))
  c_m(Ls;q) <= floor(k/L)

where k=floor(m/s).
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, lcm
import argparse
import json


def edges(cycle: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(lcm(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle)))


def cyc_lcm(cycle: tuple[int, ...]) -> int:
    out = 1
    for a in cycle:
        out = lcm(out, a)
    return out


def bounds(cycle: tuple[int, ...]) -> tuple[Fraction, Fraction, int]:
    es = edges(cycle)
    lower = max(Fraction(max(cycle), 1), Fraction(max(es), 3))
    upper = Fraction(2 * min(cycle), 1)
    return lower, upper, max(es)


def correction_states(cycle: tuple[int, ...]) -> dict[str, object]:
    lower, upper, _ = bounds(cycle)
    states: dict[str, list[dict[str, object]]] = {}
    for p in sorted(set(cycle)):
        max_h = ceil(Fraction(3 * upper, p)) - 1
        for h in range(2, max_h + 1):
            hp = h * p
            for r in range(1, hp + 1):
                alpha = Fraction(hp, r)
                if lower < alpha < upper:
                    key = str(alpha)
                    states.setdefault(key, []).append(
                        {
                            "p": p,
                            "h": h,
                            "r": r,
                            "denom": hp,
                            "q_over_s": str(alpha),
                        }
                    )
    return {
        "state_count": len(states),
        "states": [
            {"q_over_s": key, "corrections": value}
            for key, value in sorted(states.items(), key=lambda item: Fraction(item[0]))
        ],
    }


def raw_H(cycle: tuple[int, ...], y: int) -> int:
    return sum(y // p for p in cycle) - sum(y // e for e in edges(cycle))


def max_vertex_loss_for_y(state_data: dict[str, object], y: int) -> tuple[int, dict[str, object] | None]:
    best_loss = 0
    best_state = None
    for state in state_data["states"]:
        loss = sum(y // int(c["denom"]) for c in state["corrections"])
        if loss > best_loss:
            best_loss = loss
            best_state = state
    return best_loss, best_state


def lower_B(cycle: tuple[int, ...]) -> dict[str, object]:
    lower, upper, emax = bounds(cycle)
    state_data = correction_states(cycle)
    y_min = emax
    y_max = ceil(3 * upper) - 1
    rows = []
    worst = None
    for y in range(y_min, y_max + 1):
        raw = raw_H(cycle, y)
        loss, state = max_vertex_loss_for_y(state_data, y)
        H = raw - loss
        value = Fraction(2 * H, y + 1)
        row = {
            "y": y,
            "H_raw": raw,
            "max_vertex_loss": loss,
            "H_lower": H,
            "loss_state": state,
            "B_lower": str(value),
        }
        rows.append(row)
        if worst is None or value < worst[0]:
            worst = (value, row)
    assert worst is not None
    return {
        "lower": str(lower),
        "upper": str(upper),
        "edge_max": emax,
        "correction_states": state_data,
        "y_min": y_min,
        "y_max": y_max,
        "B_lower": str(worst[0]),
        "worst_y": worst[1],
        "rows": rows,
    }


def A(cycle: tuple[int, ...], k: int) -> int:
    es = edges(cycle)
    return (
        sum(k // p for p in cycle)
        - sum(k // e for e in es)
        + sum(k // (2 * e) for e in es)
        + k // cyc_lcm(cycle)
    )


def prove(cycle: tuple[int, ...], period_cap: int) -> dict[str, object]:
    lower, upper, emax = bounds(cycle)
    bdata = lower_B(cycle)
    B0 = Fraction(bdata["B_lower"])
    denoms = list(cycle) + list(edges(cycle)) + [2 * e for e in edges(cycle)] + [cyc_lcm(cycle)]
    period = 1
    for d in denoms:
        period = lcm(period, d)
    slope = (
        sum(Fraction(1, p) for p in cycle)
        - sum(Fraction(1, e) for e in edges(cycle))
        + sum(Fraction(1, 2 * e) for e in edges(cycle))
        + Fraction(1, cyc_lcm(cycle))
    )
    row: dict[str, object] = {
        "ordered_cycle": list(cycle),
        "normalized_cycle": sorted(cycle),
        "length": len(cycle),
        "bounds": {"lower": str(lower), "upper": str(upper), "edge_max": emax},
        "lower_B": bdata,
        "period": period,
        "slope": str(slope),
        "status": "unknown",
    }
    if B0 <= 0:
        row["status"] = "nonpositive_B_lower"
        return row
    if slope > B0:
        row["status"] = "slope_exceeds_B"
        return row
    if period > period_cap:
        row["status"] = "period_too_large"
        return row
    worst = None
    failures = []
    for k in range(emax, emax + period):
        value = A(cycle, k)
        margin = B0 * k - value
        item = {"k": k, "A": value, "A_over_k": str(Fraction(value, k)), "margin": str(margin)}
        if worst is None or margin < worst[0]:
            worst = (margin, item)
        if margin < 0:
            failures.append(item)
            if len(failures) >= 20:
                break
    row["worst_period_row"] = worst[1] if worst else None
    row["failures"] = failures
    row["status"] = "proved" if not failures else "period_failure"
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--motifs-json", default="ep488_v63_a4_normalized_cycle_motifs_len16.json")
    parser.add_argument("--period-cap", type=int, default=4_000_000)
    parser.add_argument("--max-length", type=int, default=12)
    parser.add_argument("--json-out", default="ep488_v71_a4_vertex_correction_bounds.json")
    args = parser.parse_args()

    data = json.load(open(args.motifs_json, encoding="utf-8"))
    rows = []
    counts: dict[str, int] = {}
    for motif in data["motifs"]:
        if args.max_length is not None and int(motif["length"]) > args.max_length:
            continue
        cycle = tuple(int(x) for x in motif["ordered_cycle"])
        row = prove(cycle, args.period_cap)
        rows.append(row)
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    result = {
        "motifs_json": args.motifs_json,
        "period_cap": args.period_cap,
        "max_length": args.max_length,
        "status_counts": counts,
        "rows": rows,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"status_counts={counts}")
    for status in sorted(counts):
        for r in [x for x in rows if x["status"] == status][:10]:
            print(
                f"{status}: len={r['length']} norm={r['normalized_cycle']} "
                f"B0={r['lower_B']['B_lower']} slope={r['slope']} period={r['period']} "
                f"states={r['lower_B']['correction_states']['state_count']}"
            )
    return 1 if counts.get("period_failure") else 0


if __name__ == "__main__":
    raise SystemExit(main())
