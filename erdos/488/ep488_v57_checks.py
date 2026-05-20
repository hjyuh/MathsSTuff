#!/usr/bin/env python3
"""EP-488 v57 checks.

This script keeps two current checks rerunnable:

1. Exact finite-certificate verification for the three high-defect
   regression/near-miss templates: theta13, Kimi, and the v56 strongest
   near-miss.
2. A4 host-margin search over induced connected unicyclic top-window hosts
   for small q.

It is not a proof of EP-488. It is a regression/evidence harness for the
remaining A2 and A4 branches.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import lcm
import sys
import time

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze, connected_components, lcm_graph_edges  # noqa: E402


@dataclass(frozen=True)
class Template:
    name: str
    q: int
    n: int
    C: tuple[int, ...]


TEMPLATES = [
    Template(
        "theta13",
        451,
        1350,
        (240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450),
    ),
    Template(
        "kimi",
        427,
        1280,
        (216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405),
    ),
    Template(
        "v56_near_miss",
        71440,
        213189,
        (
            35760,
            36207,
            36269,
            38144,
            38296,
            40230,
            42912,
            43640,
            44700,
            46678,
            47680,
            48276,
            53640,
            57216,
            60345,
            63116,
            64368,
            67050,
            68055,
        ),
    ),
]


def grouped_density(C: tuple[int, ...], q: int) -> tuple[Fraction, int, int]:
    """Return (delta, E, terms) from grouped inclusion-exclusion."""
    coeff: dict[int, int] = {}
    for a in C:
        updates = {a: 1}
        for L, c in list(coeff.items()):
            next_l = lcm(L, a)
            updates[next_l] = updates.get(next_l, 0) - c
        for L, c in updates.items():
            coeff[L] = coeff.get(L, 0) + c

    delta = Fraction(0, 1)
    abs_sum = 0
    terms = 0
    for L, c in coeff.items():
        if not c:
            continue
        terms += 1
        delta += c * (Fraction(1, L) - Fraction(1, lcm(L, q)))
        abs_sum += abs(c)
    return delta, 2 * abs_sum, terms


def prefix_counts(C: tuple[int, ...], q: int, limit: int) -> list[int]:
    hit = bytearray(limit + 1)
    for a in C:
        for m in range(a, limit + 1, a):
            if m % q:
                hit[m] = 1

    counts = [0] * (limit + 1)
    total = 0
    for m in range(1, limit + 1):
        total += hit[m]
        counts[m] = total
    return counts


def certify_template(t: Template) -> dict[str, object]:
    report = analyze(t.C, t.n, t.q)
    delta, E, terms = grouped_density(t.C, t.q)
    B = Fraction(2 * report.D_C_n, t.n)
    eta = B - delta
    if eta <= 0:
        raise RuntimeError(f"{t.name}: eta is nonpositive")

    cutoff = E.numerator * eta.denominator // (E.denominator * eta.numerator)
    counts = prefix_counts(t.C, t.q, cutoff)
    best = (Fraction(0, 1), None, 0)
    failures = []
    for m in range(t.n + 1, cutoff + 1):
        value = Fraction(counts[m], m)
        if value > best[0]:
            best = (value, m, counts[m])
        if value > B:
            failures.append((m, counts[m], value))

    return {
        "name": t.name,
        "q": t.q,
        "n": t.n,
        "size": len(t.C),
        "epsilon": report.eps_n,
        "cyclomatic": report.cyclomatic,
        "tau": report.tau_n,
        "D_n": report.D_C_n,
        "B": B,
        "delta": delta,
        "delta_over_B": delta / B,
        "E": E,
        "terms": terms,
        "eta": eta,
        "cutoff": cutoff,
        "best": best,
        "best_over_B": best[0] / B,
        "failures": failures,
    }


def c_x(d: int, x: int, q: int) -> int:
    return x // d - x // lcm(d, q)


def host_H(V: tuple[int, ...], E: tuple[tuple[int, int], ...], x: int, q: int) -> int:
    return sum(c_x(a, x, q) for a in V) - sum(c_x(lcm(a, b), x, q) for a, b in E)


def cycle_vertices(V: tuple[int, ...], E: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    adj = {v: set() for v in V}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)

    deg = {v: len(adj[v]) for v in V}
    stack = [v for v in V if deg[v] <= 1]
    removed: set[int] = set()
    while stack:
        v = stack.pop()
        if v in removed:
            continue
        removed.add(v)
        for u in list(adj[v]):
            adj[u].discard(v)
            deg[u] -= 1
            if deg[u] == 1:
                stack.append(u)

    return tuple(sorted(set(V) - removed))


def host_event_points(
    V: tuple[int, ...],
    E: tuple[tuple[int, int], ...],
    q: int,
    n: int,
    upper: int,
) -> tuple[list[int], int, tuple[int, ...]]:
    steps = set(V)
    steps.update(lcm(a, b) for a, b in E)
    cyc = cycle_vertices(V, E)
    L_cyc = 1
    for a in cyc:
        L_cyc = lcm(L_cyc, a)
    steps.add(L_cyc)
    for s in list(steps):
        steps.add(lcm(s, q))

    events = {n + 1}
    for s in steps:
        m = ((n + s) // s) * s
        while m <= upper:
            events.add(m)
            m += s
    return sorted(events), L_cyc, cyc


def check_host_margin(
    q: int,
    n: int,
    V: tuple[int, ...],
    E: tuple[tuple[int, int], ...],
    upper: int,
) -> tuple[bool, tuple[int, int, int, int, int, tuple[int, ...]]]:
    H_n = host_H(V, E, n, q)
    events, L_cyc, cyc = host_event_points(V, E, q, n, upper)
    worst = None
    for m in events:
        H_m = host_H(V, E, m, q)
        margin = 2 * m * H_n - n * H_m - n * c_x(L_cyc, m, q)
        item = (margin, m, H_n, H_m, L_cyc, cyc)
        if worst is None or margin < worst[0]:
            worst = item
        if margin < 0:
            return False, item
    assert worst is not None
    return True, worst


def induced_unicyclic_a4_search(max_q: int = 45, max_k: int = 8) -> dict[str, object]:
    checked = 0
    worsts = []
    for q in range(7, max_q + 1):
        V_full = list(range(q // 2 + 1, q))
        for n in range((5 * q + 1) // 2, 3 * q):
            E_full = [tuple(e) for e in lcm_graph_edges(V_full, n, q)]
            if len(E_full) < 3:
                continue
            for k in range(3, min(max_k, len(V_full)) + 1):
                for V_raw in combinations(V_full, k):
                    V = tuple(sorted(V_raw))
                    V_set = set(V)
                    E = tuple(e for e in E_full if e[0] in V_set and e[1] in V_set)
                    if len(E) != k:
                        continue
                    if len(connected_components(list(V), list(E))) != 1:
                        continue
                    checked += 1
                    ok, worst = check_host_margin(q, n, V, E, min(4 * n, n + 500))
                    if not ok:
                        return {
                            "ok": False,
                            "checked": checked,
                            "counterexample": (q, n, V, E, worst),
                        }
                    worsts.append((worst[0], q, n, V, E, worst))

    worsts.sort(key=lambda item: item[0])
    return {
        "ok": True,
        "checked": checked,
        "worst": worsts[:10],
    }


def induced_high_defect_a2_search(
    max_q: int = 45,
    max_k: int = 8,
    max_cutoff: int = 100_000,
) -> dict[str, object]:
    """Bounded exact census for small high-defect A2 components.

    This is not a proof of uniform high-defect safety. It enumerates induced
    connected top-window components with |C| <= max_k, computes the exact
    finite-certificate margin eta = 2D(n)/n - delta, and exhausts the finite
    window when the exact cutoff is at most max_cutoff.
    """
    connected_checked = 0
    high_defect = 0
    certified = 0
    large_cutoff = []
    eta_nonpositive = []
    failures = []
    bests = []
    smallest_eta = []

    for q in range(7, max_q + 1):
        V_full = list(range(q // 2 + 1, q))
        for n in range((5 * q + 1) // 2, 3 * q):
            E_full = [tuple(e) for e in lcm_graph_edges(V_full, n, q)]
            if len(E_full) < 2:
                continue
            for k in range(4, min(max_k, len(V_full)) + 1):
                for C_raw in combinations(V_full, k):
                    C = tuple(sorted(C_raw))
                    C_set = set(C)
                    E = [e for e in E_full if e[0] in C_set and e[1] in C_set]
                    if len(E) < k + 1:
                        continue
                    if len(connected_components(list(C), E)) != 1:
                        continue

                    connected_checked += 1
                    report = analyze(C, n, q)
                    if report.eps_n < 2:
                        continue

                    high_defect += 1
                    delta, E_abs, terms = grouped_density(C, q)
                    B = Fraction(2 * report.D_C_n, n)
                    eta = B - delta
                    row = {
                        "q": q,
                        "n": n,
                        "C": C,
                        "k": k,
                        "epsilon": report.eps_n,
                        "cyclomatic": report.cyclomatic,
                        "tau": report.tau_n,
                        "D_n": report.D_C_n,
                        "B": B,
                        "delta": delta,
                        "delta_over_B": delta / B if B else None,
                        "eta": eta,
                        "terms": terms,
                        "E": E_abs,
                    }
                    smallest_eta.append((eta / B if B else Fraction(0, 1), row))
                    if eta <= 0:
                        eta_nonpositive.append(row)
                        continue

                    cutoff = E_abs.numerator * eta.denominator // (E_abs.denominator * eta.numerator)
                    row["cutoff"] = cutoff
                    if cutoff > max_cutoff:
                        large_cutoff.append(row)
                        continue

                    counts = prefix_counts(C, q, cutoff)
                    best = (Fraction(0, 1), None, 0)
                    local_failures = []
                    for m in range(n + 1, cutoff + 1):
                        value = Fraction(counts[m], m)
                        if value > best[0]:
                            best = (value, m, counts[m])
                        if value > B:
                            local_failures.append((m, counts[m], value))
                    row["best"] = best
                    row["best_over_B"] = best[0] / B if B else None
                    certified += 1
                    bests.append((row["best_over_B"], row))
                    if local_failures:
                        row["failures"] = local_failures[:20]
                        failures.append(row)

    bests.sort(key=lambda item: item[0], reverse=True)
    smallest_eta.sort(key=lambda item: item[0])
    return {
        "ok": not failures and not eta_nonpositive,
        "connected_checked": connected_checked,
        "high_defect": high_defect,
        "certified": certified,
        "large_cutoff_count": len(large_cutoff),
        "large_cutoff": large_cutoff[:10],
        "eta_nonpositive": eta_nonpositive[:10],
        "failures": failures[:10],
        "best": bests[:10],
        "smallest_eta_over_B": smallest_eta[:10],
    }


def main() -> int:
    start = time.time()
    print("EP-488 v57 finite-certificate templates")
    for template in TEMPLATES:
        result = certify_template(template)
        print(
            f"{result['name']}: epsilon={result['epsilon']} D(n)={result['D_n']} "
            f"B={result['B']} delta/B={result['delta_over_B']} "
            f"cutoff={result['cutoff']} best={result['best']} "
            f"best/B={result['best_over_B']} failures={len(result['failures'])}"
        )
        if result["failures"]:
            return 1

    print()
    print("EP-488 v57 A2 induced high-defect finite-certificate census")
    a2 = induced_high_defect_a2_search()
    print(
        f"ok={a2['ok']} connected_checked={a2['connected_checked']} "
        f"high_defect={a2['high_defect']} certified={a2['certified']} "
        f"large_cutoff_count={a2['large_cutoff_count']}"
    )
    if a2["eta_nonpositive"]:
        print(f"eta_nonpositive={a2['eta_nonpositive']}")
        return 1
    if a2["failures"]:
        print(f"failures={a2['failures']}")
        return 1
    for ratio, row in a2["best"][:10]:
        print(
            f"best_over_B={ratio} q={row['q']} n={row['n']} "
            f"k={row['k']} epsilon={row['epsilon']} cutoff={row['cutoff']} "
            f"best={row['best']} C={row['C']}"
        )
    for eta_ratio, row in a2["smallest_eta_over_B"][:5]:
        print(
            f"smallest_eta_over_B={eta_ratio} q={row['q']} n={row['n']} "
            f"k={row['k']} epsilon={row['epsilon']} delta/B={row['delta_over_B']} C={row['C']}"
        )

    print()
    print("EP-488 v57 A4 induced-unicyclic search")
    a4 = induced_unicyclic_a4_search()
    print(f"ok={a4['ok']} checked={a4['checked']}")
    if not a4["ok"]:
        print(f"counterexample={a4['counterexample']}")
        return 1
    for item in a4["worst"]:
        print(f"worst={item}")

    print(f"elapsed_seconds={time.time() - start:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
