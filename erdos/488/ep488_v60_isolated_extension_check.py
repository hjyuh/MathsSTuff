#!/usr/bin/env python3
"""EP-488 v60 isolated-extension checks.

This file supports the v60 isolated-extension lemma:

If a reduced top-window set C0 is already safe and I is a set of vertices that
has no q-excluded B_n edge to C0 or within I, then adding I cannot create an EP
violation. The reason is that every singleton top-window vertex is individually
safe at factor 2, while D(n) is additive across B_n-isolated pieces and D(m) is
subadditive.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm
import json
import sys

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import D_C, analyze, lcm_graph_edges  # noqa: E402

from ep488_v57_checks import TEMPLATES  # noqa: E402
from ep488_v58_full_component_census import finite_certificate  # noqa: E402
from ep488_v59_theta_isolate_search import Q, N, M, THETA_CORE  # noqa: E402


def c_x(a: int, x: int, q: int) -> int:
    return x // a - x // lcm(a, q)


def singleton_margin(q: int, n: int, a: int) -> dict[str, object]:
    f = n // a
    c = c_x(a, n, q)
    return {
        "q": q,
        "n": n,
        "a": a,
        "floor_n_over_a": f,
        "c_n": c,
        "q_over_gcd": q // gcd(a, q),
        "strict_bound_holds": Fraction(1, a) < Fraction(2 * c, n),
        "margin": Fraction(2 * c, n) - Fraction(1, a),
    }


def exhaustive_singleton_bound_check(q_max: int = 500) -> dict[str, object]:
    checked = 0
    worst = None
    failures = []
    for q in range(3, q_max + 1):
        for n in range((5 * q + 1) // 2, 3 * q):
            for a in range(q // 2 + 1, q):
                row = singleton_margin(q, n, a)
                checked += 1
                if not row["strict_bound_holds"]:
                    failures.append(row)
                    continue
                if worst is None or row["margin"] < worst["margin"]:
                    worst = row
    return {
        "q_max": q_max,
        "checked": checked,
        "failures": failures[:20],
        "worst": worst,
    }


def is_bn_isolated_from(C0: tuple[int, ...], I: tuple[int, ...], q: int, n: int) -> bool:
    all_vertices = C0 + I
    edges = lcm_graph_edges(all_vertices, n, q)
    I_set = set(I)
    for a, b in edges:
        if a in I_set or b in I_set:
            return False
    return True


def extension_ceiling(D0_n: int, I: tuple[int, ...], q: int, n: int) -> Fraction:
    """Worst possible ratio to EP bound using c_m(a)/m <= 1/a."""
    singleton_sum_n = sum(c_x(a, n, q) for a in I)
    numerator = Fraction(2 * D0_n, 1) + sum(Fraction(n, a) for a in I)
    denominator = Fraction(2 * (D0_n + singleton_sum_n), 1)
    return numerator / denominator


def extension_density_margin(I: tuple[int, ...], q: int, n: int) -> Fraction:
    """Density slack: sum_a (2c_n(a)/n - 1/a)."""
    return sum(Fraction(2 * c_x(a, n, q), n) - Fraction(1, a) for a in I)


def check_extension_case(name: str, q: int, n: int, m_probe: int, C0: tuple[int, ...], I: tuple[int, ...]) -> dict[str, object]:
    C = tuple(sorted(C0 + I))
    core_report = analyze(C0, n, q)
    full_report = analyze(C, n, q)
    core_cert = finite_certificate(C0, q, n, core_report.D_C_n, 100_000_000)
    singleton_sum = sum(c_x(a, n, q) for a in I)
    full_D_probe = D_C(C, m_probe, q)
    full_probe_ratio = Fraction(full_D_probe, m_probe) / Fraction(2 * full_report.D_C_n, n)
    return {
        "name": name,
        "q": q,
        "n": n,
        "m_probe": m_probe,
        "core_size": len(C0),
        "isolate_size": len(I),
        "full_size": len(C),
        "isolated_at_n": is_bn_isolated_from(C0, I, q, n),
        "core_epsilon": core_report.eps_n,
        "full_epsilon": full_report.eps_n,
        "core_D_n": core_report.D_C_n,
        "full_D_n": full_report.D_C_n,
        "singleton_sum_n": singleton_sum,
        "D_n_additive": full_report.D_C_n == core_report.D_C_n + singleton_sum,
        "core_certificate_status": core_cert["status"],
        "core_best_over_B": core_cert.get("best_over_B"),
        "extension_ceiling": str(extension_ceiling(core_report.D_C_n, I, q, n)),
        "extension_ceiling_float": float(extension_ceiling(core_report.D_C_n, I, q, n)),
        "extension_density_margin": str(extension_density_margin(I, q, n)),
        "probe_D_m": full_D_probe,
        "probe_ratio": str(full_probe_ratio),
        "probe_ratio_float": float(full_probe_ratio),
        "isolate_singleton_bounds": [
            {
                "a": a,
                "c_n": c_x(a, n, q),
                "margin": str(singleton_margin(q, n, a)["margin"]),
            }
            for a in I
        ],
    }


def main() -> int:
    singleton_check = exhaustive_singleton_bound_check(500)
    print(
        f"singleton q<=500 checked={singleton_check['checked']} "
        f"failures={len(singleton_check['failures'])} worst={singleton_check['worst']}"
    )
    if singleton_check["failures"]:
        return 1

    v56 = next(t for t in TEMPLATES if t.name == "v56_near_miss")
    v56_core = THETA_CORE
    v56_isolates = tuple(a for a in v56.C if a not in v56_core)
    v59_data = json.load(open("ep488_v59_theta_isolate_greedy20.json", encoding="utf-8"))
    v59_isolates = tuple(step["vertex"] for step in v59_data["greedy_steps"])

    cases = [
        check_extension_case("v56_core_plus_original_isolates", v56.q, v56.n, 3411504, v56_core, v56_isolates),
        check_extension_case("v59_core_plus_20_near_q_isolates", Q, N, M, THETA_CORE, v59_isolates),
    ]
    for case in cases:
        print(
            f"{case['name']}: isolated_at_n={case['isolated_at_n']} "
            f"D_additive={case['D_n_additive']} core_cert={case['core_certificate_status']} "
            f"full_epsilon={case['full_epsilon']} ceiling={case['extension_ceiling']} "
            f"probe_ratio={case['probe_ratio']}"
        )
        if not case["isolated_at_n"] or not case["D_n_additive"] or case["core_certificate_status"] != "certified":
            return 1

    with open("ep488_v60_isolated_extension_check.json", "w", encoding="utf-8") as f:
        json.dump(
            {
                "singleton_check": {
                    "q_max": singleton_check["q_max"],
                    "checked": singleton_check["checked"],
                    "failures": singleton_check["failures"],
                    "worst": {
                        **singleton_check["worst"],
                        "margin": str(singleton_check["worst"]["margin"]),
                    },
                },
                "cases": cases,
            },
            f,
            indent=2,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
