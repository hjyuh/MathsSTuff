#!/usr/bin/env python3
"""EP-488 v66 A4 pure-cycle realization-window sampler.

v65 certified one canonical realization for each normalized pure-cycle motif
through length 16. This script probes whether the finite-certificate margin is
stable when the same ordered normalized cycle is realized with other admissible
scales, q values, and n values.

This is an evidence generator, not a proof. It deliberately records the exact
weakest sampled eta margins and then finite-certifies the weakest sampled rows.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, gcd, lcm
import argparse
import json

from ep488_v64_a4_pure_cycle_finite_cert import (
    finite_certificate,
    host_H,
    N_coefficients,
)


def F(text: str) -> Fraction:
    return Fraction(text)


def cycle_edges(cycle: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)])))
        for i in range(len(cycle))
    )


def edge_max(cycle: tuple[int, ...]) -> int:
    return max(lcm(a, b) for a, b in cycle_edges(cycle))


def feasibility_bounds(cycle: tuple[int, ...]) -> tuple[Fraction, Fraction, int]:
    emax = edge_max(cycle)
    lower = max(Fraction(max(cycle), 1), Fraction(emax, 3))
    upper = Fraction(2 * min(cycle), 1)
    return lower, upper, emax


def admissible_qs(
    norm_ordered: tuple[int, ...],
    scale: int,
    max_q_samples: int,
) -> list[int]:
    lower, upper, _ = feasibility_bounds(norm_ordered)
    lo = (lower * scale).numerator // (lower * scale).denominator + 1
    hi = ((upper * scale).numerator - 1) // (upper * scale).denominator
    if lo > hi:
        return []

    actual = tuple(scale * a for a in norm_ordered)
    edges = cycle_edges(actual)
    qs = [
        q
        for q in range(lo, hi + 1)
        if not any(lcm(a, b) % q == 0 for a, b in edges)
    ]
    if len(qs) <= max_q_samples:
        return qs

    picks = {qs[0], qs[-1]}
    for i in range(max_q_samples):
        picks.add(qs[(i * (len(qs) - 1)) // (max_q_samples - 1)])
    return sorted(picks)


def step_denominators_for_H(cycle: tuple[int, ...], q: int) -> set[int]:
    denoms = set(cycle)
    denoms.update(lcm(a, b) for a, b in cycle_edges(cycle))
    out = set(denoms)
    out.update(lcm(d, q) for d in denoms)
    return out


def dangerous_n_values(
    cycle: tuple[int, ...],
    q: int,
    max_n_samples: int,
) -> list[int]:
    n_lo = max(ceil(Fraction(5 * q, 2)), edge_max(cycle))
    n_hi = 3 * q - 1
    if n_lo > n_hi:
        return []

    candidates = {n_lo, n_hi}
    for d in step_denominators_for_H(cycle, q):
        first_k = (n_lo + 1 + d - 1) // d
        value = first_k * d
        while value <= n_hi:
            if value - 1 >= n_lo:
                candidates.add(value - 1)
            value += d

    ns = sorted(candidates)
    if len(ns) <= max_n_samples:
        return ns

    picks = {ns[0], ns[-1]}
    for i in range(max_n_samples):
        picks.add(ns[(i * (len(ns) - 1)) // (max_n_samples - 1)])
    return sorted(picks)


def delta_for_cycle(cycle: tuple[int, ...], q: int) -> tuple[Fraction, int, int]:
    coeff = N_coefficients(cycle)
    delta = sum(
        Fraction(c) * (Fraction(1, d) - Fraction(1, lcm(d, q)))
        for d, c in coeff.items()
    )
    E = 2 * sum(abs(c) for c in coeff.values())
    return delta, E, len(coeff)


def eta_summary(cycle: tuple[int, ...], q: int, n: int) -> dict[str, object]:
    delta, E, terms = delta_for_cycle(cycle, q)
    H_n = host_H(cycle, q, n)
    B = Fraction(2 * H_n, n)
    eta = B - delta
    row: dict[str, object] = {
        "B": str(B),
        "delta": str(delta),
        "delta_over_B": str(delta / B) if B else None,
        "eta": str(eta),
        "eta_over_B": str(eta / B) if B else None,
        "E": E,
        "terms": terms,
        "H_n": H_n,
        "status": "eta_nonpositive" if eta <= 0 else "eta_positive",
    }
    if eta > 0:
        row["cutoff"] = E.numerator * eta.denominator // (E.denominator * eta.numerator)
    return row


def load_selected_motifs(
    motifs_json: str,
    cert_json: str,
    top_best: int,
    include_all: bool,
    only_norm: str | None,
) -> list[dict[str, object]]:
    motif_data = json.load(open(motifs_json, encoding="utf-8"))
    motifs = motif_data["motifs"]
    by_norm = {
        tuple(m["normalized_cycle"]): m
        for m in motifs
    }
    if only_norm:
        norm = tuple(int(x) for x in only_norm.split(",") if x.strip())
        if norm not in by_norm:
            raise ValueError(f"normalized motif not found: {norm}")
        return [by_norm[norm]]
    if include_all:
        return motifs

    cert_data = json.load(open(cert_json, encoding="utf-8"))
    selected: set[tuple[int, ...]] = set()
    for row in cert_data["top_by_best_over_B"][:top_best]:
        selected.add(tuple(row["normalized_cycle"]))

    rows = cert_data["rows"]
    min_eta = min(
        rows,
        key=lambda r: F(r["certificate"]["eta"]) / F(r["certificate"]["B"]),
    )
    max_cutoff = max(rows, key=lambda r: int(r["certificate"]["cutoff"]))
    selected.add(tuple(min_eta["normalized_cycle"]))
    selected.add(tuple(max_cutoff["normalized_cycle"]))

    return [by_norm[norm] for norm in sorted(selected, key=lambda x: (len(x), x))]


def sample_windows(args: argparse.Namespace) -> dict[str, object]:
    motifs = load_selected_motifs(
        args.motifs_json,
        args.cert_json,
        args.top_best,
        args.all_motifs,
        args.only_norm,
    )
    sampled = []
    eta_nonpositive = []
    for motif in motifs:
        ordered = tuple(int(a) for a in motif["ordered_cycle"])
        norm = tuple(int(a) for a in motif["normalized_cycle"])
        for scale in range(1, args.max_scale + 1):
            actual = tuple(scale * a for a in ordered)
            for q in admissible_qs(ordered, scale, args.max_q_samples):
                for n in dangerous_n_values(actual, q, args.max_n_samples):
                    summary = eta_summary(actual, q, n)
                    row = {
                        "normalized_cycle": list(norm),
                        "ordered_cycle": list(ordered),
                        "length": len(norm),
                        "scale": scale,
                        "q": q,
                        "n": n,
                        "cycle": list(actual),
                        "summary": summary,
                    }
                    sampled.append(row)
                    if summary["status"] == "eta_nonpositive":
                        eta_nonpositive.append(row)

    positive = [r for r in sampled if r["summary"]["status"] == "eta_positive"]
    by_eta = sorted(
        positive,
        key=lambda r: F(r["summary"]["eta_over_B"]),
    )
    by_cutoff = sorted(
        positive,
        key=lambda r: int(r["summary"]["cutoff"]),
        reverse=True,
    )
    exact_candidates = []
    seen = set()
    for source in (by_eta[: args.exact_top], by_cutoff[: args.exact_top]):
        for row in source:
            key = (
                tuple(row["cycle"]),
                int(row["q"]),
                int(row["n"]),
            )
            if key not in seen:
                seen.add(key)
                exact_candidates.append(row)

    exact_checked = []
    exact_failures = []
    for row in exact_candidates[: 2 * args.exact_top]:
        cert = finite_certificate(
            tuple(int(a) for a in row["cycle"]),
            int(row["q"]),
            int(row["n"]),
        )
        exact = dict(row)
        exact["certificate"] = cert
        exact_checked.append(exact)
        if cert["status"] != "certified":
            exact_failures.append(exact)

    return {
        "motifs_json": args.motifs_json,
        "cert_json": args.cert_json,
        "all_motifs": args.all_motifs,
        "selected_motifs": len(motifs),
        "max_scale": args.max_scale,
        "max_q_samples": args.max_q_samples,
        "max_n_samples": args.max_n_samples,
        "sampled_cases": len(sampled),
        "eta_nonpositive_count": len(eta_nonpositive),
        "eta_nonpositive": eta_nonpositive[:20],
        "min_eta_over_B": by_eta[:20],
        "max_cutoff": by_cutoff[:20],
        "exact_checked_count": len(exact_checked),
        "exact_failures_count": len(exact_failures),
        "exact_failures": exact_failures[:20],
        "exact_checked": exact_checked,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--motifs-json", default="ep488_v63_a4_normalized_cycle_motifs_len16.json")
    parser.add_argument("--cert-json", default="ep488_v65_a4_pure_cycle_finite_cert_len16.json")
    parser.add_argument("--json-out", default="ep488_v66_a4_realization_window.json")
    parser.add_argument("--max-scale", type=int, default=3)
    parser.add_argument("--max-q-samples", type=int, default=25)
    parser.add_argument("--max-n-samples", type=int, default=80)
    parser.add_argument("--top-best", type=int, default=10)
    parser.add_argument("--exact-top", type=int, default=20)
    parser.add_argument("--all-motifs", action="store_true")
    parser.add_argument("--only-norm", default=None, help="comma-separated normalized cycle to sample")
    args = parser.parse_args()

    result = sample_windows(args)
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"selected_motifs={result['selected_motifs']} sampled_cases={result['sampled_cases']} "
        f"eta_nonpositive={result['eta_nonpositive_count']} "
        f"exact_checked={result['exact_checked_count']} exact_failures={result['exact_failures_count']}"
    )
    for row in result["min_eta_over_B"][:10]:
        s = row["summary"]
        print(
            f"min_eta_over_B={s['eta_over_B']} len={row['length']} scale={row['scale']} "
            f"q={row['q']} n={row['n']} cutoff={s.get('cutoff')} norm={row['normalized_cycle']}"
        )
    print("exact:")
    for row in result["exact_checked"][:10]:
        cert = row["certificate"]
        print(
            f"status={cert['status']} best_over_B={cert.get('best_over_B')} "
            f"len={row['length']} scale={row['scale']} q={row['q']} n={row['n']} "
            f"best={cert.get('best')} norm={row['normalized_cycle']}"
        )
    return 1 if result["eta_nonpositive_count"] or result["exact_failures_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
