#!/usr/bin/env python3
"""EP-488 v64 pure-cycle A4 finite certificates.

This script upgrades v63's bounded event-window checks. For a pure cycle Z,
the A4 target is

    H_Z#(m)/m + c_m(L_cyc)/m <= 2 H_Z#(n)/n.

The left side is a signed finite sum of q-excluded floor-count functions
c_x(d;q). Therefore the grouped finite-certificate theorem applies directly:

    N(m)/m <= delta + E/m.

When eta = 2H(n)/n - delta > 0, it suffices to check
n < m <= floor(E/eta).
"""

from __future__ import annotations

from fractions import Fraction
from math import lcm
import argparse
import json

from ep488_v57_checks import c_x


def cycle_lcm(cycle: tuple[int, ...]) -> int:
    out = 1
    for a in cycle:
        out = lcm(out, a)
    return out


def host_H(cycle: tuple[int, ...], q: int, x: int) -> int:
    total = sum(c_x(a, x, q) for a in cycle)
    for i, a in enumerate(cycle):
        total -= c_x(lcm(a, cycle[(i + 1) % len(cycle)]), x, q)
    return total


def N_coefficients(cycle: tuple[int, ...]) -> dict[int, int]:
    coeff: dict[int, int] = {}
    for a in cycle:
        coeff[a] = coeff.get(a, 0) + 1
    for i, a in enumerate(cycle):
        L = lcm(a, cycle[(i + 1) % len(cycle)])
        coeff[L] = coeff.get(L, 0) - 1
    L_cyc = cycle_lcm(cycle)
    coeff[L_cyc] = coeff.get(L_cyc, 0) + 1
    return {d: c for d, c in coeff.items() if c}


def N_value(cycle: tuple[int, ...], q: int, x: int) -> int:
    return sum(coeff * c_x(d, x, q) for d, coeff in N_coefficients(cycle).items())


def finite_certificate(cycle: tuple[int, ...], q: int, n: int) -> dict[str, object]:
    coeff = N_coefficients(cycle)
    delta = sum(
        Fraction(c) * (Fraction(1, d) - Fraction(1, lcm(d, q)))
        for d, c in coeff.items()
    )
    E = 2 * sum(abs(c) for c in coeff.values())
    B = Fraction(2 * host_H(cycle, q, n), n)
    eta = B - delta
    out: dict[str, object] = {
        "B": str(B),
        "delta": str(delta),
        "delta_over_B": str(delta / B) if B else None,
        "eta": str(eta),
        "E": E,
        "terms": len(coeff),
    }
    if eta <= 0:
        out["status"] = "eta_nonpositive"
        return out

    cutoff = E.numerator * eta.denominator // (E.denominator * eta.numerator)
    out["cutoff"] = cutoff
    best = (Fraction(0, 1), None, 0)
    failures = []
    for m in range(n + 1, cutoff + 1):
        value_int = N_value(cycle, q, m)
        value = Fraction(value_int, m)
        if value > best[0]:
            best = (value, m, value_int)
        if value > B:
            failures.append((m, value_int, str(value)))

    out["status"] = "failure" if failures else "certified"
    out["best"] = (str(best[0]), best[1], best[2])
    out["best_over_B"] = str(best[0] / B) if B else None
    out["failures"] = failures[:20]
    return out


def certify_motif_file(input_json: str) -> dict[str, object]:
    data = json.load(open(input_json, encoding="utf-8"))
    rows = []
    status_counts: dict[str, int] = {}
    max_cutoff = 0
    for motif in data["motifs"]:
        r = motif["realization"]
        cycle = tuple(r["cycle"])
        q = int(r["q"])
        n = int(r["n"])
        cert = finite_certificate(cycle, q, n)
        status_counts[cert["status"]] = status_counts.get(cert["status"], 0) + 1
        max_cutoff = max(max_cutoff, int(cert.get("cutoff", 0)))
        rows.append(
            {
                "normalized_cycle": motif["normalized_cycle"],
                "length": motif["length"],
                "q": q,
                "n": n,
                "cycle": list(cycle),
                "certificate": cert,
            }
        )

    certified = [r for r in rows if r["certificate"]["status"] == "certified"]
    certified.sort(key=lambda r: Fraction(r["certificate"]["best_over_B"]), reverse=True)
    return {
        "input_json": input_json,
        "motif_count": len(rows),
        "status_counts": status_counts,
        "max_cutoff": max_cutoff,
        "top_by_best_over_B": certified[:20],
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", default="ep488_v63_a4_normalized_cycle_motifs_len14.json")
    parser.add_argument("--json-out", default="ep488_v64_a4_pure_cycle_finite_cert_len14.json")
    args = parser.parse_args()

    result = certify_motif_file(args.input_json)
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"input={result['input_json']} motifs={result['motif_count']} "
        f"status_counts={result['status_counts']} max_cutoff={result['max_cutoff']}"
    )
    for row in result["top_by_best_over_B"][:10]:
        cert = row["certificate"]
        print(
            f"best_over_B={cert['best_over_B']} len={row['length']} "
            f"q={row['q']} n={row['n']} best={cert['best']} "
            f"norm={row['normalized_cycle']}"
        )
    return 1 if result["status_counts"].get("failure") or result["status_counts"].get("eta_nonpositive") else 0


if __name__ == "__main__":
    raise SystemExit(main())
