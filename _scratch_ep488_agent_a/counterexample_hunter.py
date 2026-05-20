from __future__ import annotations

import argparse
import heapq
import json
import math
import random
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


def lcm_many(values) -> int:
    out = 1
    for v in values:
        out = lcm(out, v)
    return out


def build_edges(q: int, C: list[int], n: int) -> list[tuple[int, int, int]]:
    edges = []
    for i, a in enumerate(C):
        for b in C[i + 1 :]:
            L = lcm(a, b)
            if L <= n and L % q != 0:
                edges.append((a, b, L))
    return edges


def components(C: list[int], edges: list[tuple[int, int, int]]) -> list[list[int]]:
    adj = {a: [] for a in C}
    for a, b, _ in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = set()
    comps = []
    for a in C:
        if a in seen:
            continue
        dq = deque([a])
        seen.add(a)
        comp = []
        while dq:
            u = dq.popleft()
            comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    dq.append(v)
        comps.append(sorted(comp))
    return comps


def tau_general(q: int, C: list[int], n: int) -> tuple[int, list[tuple[int, list[int]]]]:
    """Count q-excluded lcm collision fibers of size exactly 3."""
    candidate_lcms = set()
    for a, b, L in build_edges(q, C, n):
        candidate_lcms.add(L)
    fibers = []
    for L in sorted(candidate_lcms):
        S = [a for a in C if L % a == 0]
        if len(S) == 3:
            fibers.append((L, S))
    return len(fibers), fibers


def graph_metrics(q: int, C: list[int], n: int) -> dict:
    C = sorted(set(C))
    edges = build_edges(q, C, n)
    comps = components(C, edges)
    cyclomatic = len(edges) - len(C) + len(comps)
    tau, fibers = tau_general(q, C, n)
    return {
        "edges": edges,
        "components": comps,
        "cyclomatic": cyclomatic,
        "tau": tau,
        "epsilon": cyclomatic - tau,
        "fibers": fibers,
    }


def d_prefix(q: int, C: list[int], M: int) -> list[int]:
    hit = bytearray(M + 1)
    for a in C:
        for t in range(a, M + 1, a):
            if t % q:
                hit[t] = 1
    pref = [0] * (M + 1)
    s = 0
    for i in range(1, M + 1):
        s += hit[i]
        pref[i] = s
    return pref


def exact_D_by_ie(q: int, C: list[int], x: int) -> int:
    total = 0
    k = len(C)
    for mask in range(1, 1 << k):
        bits = 0
        L = 1
        for i, a in enumerate(C):
            if mask >> i & 1:
                bits += 1
                L = lcm(L, a)
                if L > x and lcm(L, q) > x:
                    # Still safe to continue, but no contribution possible.
                    pass
        count = x // L - x // lcm(L, q)
        total += count if bits % 2 else -count
    return total


def asymptotic_density_ie(q: int, C: list[int]) -> Fraction | None:
    # Inclusion-exclusion is fine for the component-sized cases that matter here.
    if len(C) > 22:
        return None
    total = Fraction(0, 1)
    k = len(C)
    for mask in range(1, 1 << k):
        bits = 0
        L = 1
        for i, a in enumerate(C):
            if mask >> i & 1:
                bits += 1
                L = lcm(L, a)
        term = Fraction(1, L) - Fraction(1, lcm(L, q))
        total += term if bits % 2 else -term
    return total


def event_scan(q: int, C: list[int], n: int, M: int) -> dict:
    pref = d_prefix(q, C, M)
    Dn = pref[n]
    threshold = Fraction(2 * Dn, n)
    best_ratio = Fraction(-1, 1)
    best_m = n + 1
    checked = 0
    first = n + 1
    if first <= M:
        best_ratio = Fraction(pref[first], first)
        checked += 1
    for m in range(max(n + 1, 1), M + 1):
        if pref[m] != pref[m - 1]:
            checked += 1
            r = Fraction(pref[m], m)
            if r > best_ratio:
                best_ratio = r
                best_m = m
    return {
        "D_n": Dn,
        "threshold": threshold,
        "best_m": best_m,
        "D_best": pref[best_m] if best_m <= M else None,
        "best_ratio": best_ratio,
        "relative": best_ratio / threshold if threshold else None,
        "violation": best_ratio > threshold,
        "events_checked": checked,
        "M": M,
    }


def union_bound(q: int, C: list[int]) -> Fraction:
    return sum(Fraction(1, a) for a in C)


def top_window_pair_edges(q: int) -> list[tuple[int, int, int]]:
    V = list(range(q // 2 + 1, q))
    edges = []
    for i, a in enumerate(V):
        for b in V[i + 1 :]:
            L = lcm(a, b)
            if L < 3 * q and L % q != 0:
                edges.append((L, a, b))
    edges.sort()
    return edges


def full_component_candidates(q_max: int, m_factor: int, keep: int) -> dict:
    best = []
    seq = 0
    violations = []
    eps_counts = defaultdict(int)
    eps2_total = 0
    union_cert = 0
    max_eps = -10**9

    for q in range(5, q_max + 1):
        pair_edges = top_window_pair_edges(q)
        n0 = (5 * q + 1) // 2
        for n in range(n0, 3 * q):
            C_all = list(range(q // 2 + 1, q))
            active = [(a, b, L) for (L, a, b) in pair_edges if L <= n]
            comps = components(C_all, active)
            active_set = {(min(a, b), max(a, b)): L for a, b, L in active}
            for comp in comps:
                if len(comp) < 3:
                    continue
                comp_edges = []
                for i, a in enumerate(comp):
                    for b in comp[i + 1 :]:
                        L = active_set.get((a, b))
                        if L is not None:
                            comp_edges.append((a, b, L))
                cyclomatic = len(comp_edges) - len(comp) + 1
                tau, _ = tau_general(q, comp, n)
                eps = cyclomatic - tau
                eps_counts[(cyclomatic, tau, eps)] += 1
                max_eps = max(max_eps, eps)
                if eps < 2:
                    continue
                eps2_total += 1
                scan = event_scan(q, comp, n, m_factor * q)
                ub = union_bound(q, comp)
                if ub <= scan["threshold"]:
                    union_cert += 1
                rec = {
                    "source": "full_component",
                    "q": q,
                    "n": n,
                    "C": comp,
                    "cyclomatic": cyclomatic,
                    "tau": tau,
                    "epsilon": eps,
                    "D_n": scan["D_n"],
                    "best_m": scan["best_m"],
                    "D_best": scan["D_best"],
                    "relative": float(scan["relative"]),
                    "threshold": f"{scan['threshold'].numerator}/{scan['threshold'].denominator}",
                    "best_ratio": f"{scan['best_ratio'].numerator}/{scan['best_ratio'].denominator}",
                    "union_bound": f"{ub.numerator}/{ub.denominator}",
                    "union_cert": ub <= scan["threshold"],
                }
                if scan["violation"]:
                    violations.append(rec)
                seq += 1
                heapq.heappush(best, (float(scan["relative"]), seq, rec))
                if len(best) > keep:
                    heapq.heappop(best)

    return {
        "q_max": q_max,
        "m_factor": m_factor,
        "epsilon_triples": {str(k): v for k, v in sorted(eps_counts.items())},
        "epsilon_ge_2_components": eps2_total,
        "union_certified": union_cert,
        "max_epsilon": max_eps,
        "violations": violations,
        "near_misses": [r for _, _, r in sorted(best, reverse=True)],
    }


def enumerate_induced_subsets_for_q(q: int, n: int, size_cap: int, sample_cap: int | None = None):
    C_all = list(range(q // 2 + 1, q))
    active = build_edges(q, C_all, n)
    comps = components(C_all, active)
    rng = random.Random(488000 + 1000 * q + n)
    for comp in comps:
        if len(comp) < 3:
            continue
        comp_edges = build_edges(q, comp, n)
        # Induced subgraphs cannot have larger cyclomatic number than the
        # ambient connected component. Epsilon >= 2 requires cyclomatic >= 2.
        if len(comp_edges) - len(comp) + 1 < 2:
            continue
        if len(comp) <= size_cap:
            masks = range(1, 1 << len(comp))
            for mask in masks:
                if mask.bit_count() < 3:
                    continue
                C = [comp[i] for i in range(len(comp)) if mask >> i & 1]
                met = graph_metrics(q, C, n)
                # Keep connected induced subsets only in this pass.
                if len(met["components"]) == 1:
                    yield C, met
        elif sample_cap:
            seen = set()
            for _ in range(sample_cap):
                k = rng.randint(3, min(len(comp), size_cap))
                C = tuple(sorted(rng.sample(comp, k)))
                if C in seen:
                    continue
                seen.add(C)
                met = graph_metrics(q, list(C), n)
                if len(met["components"]) == 1:
                    yield list(C), met


def induced_subset_search(
    q_min: int, q_max: int, m_factor: int, size_cap: int, keep: int, n_stride: int
) -> dict:
    best = []
    seq = 0
    violations = []
    total = 0
    eps2 = 0
    union_cert = 0
    for q in range(max(5, q_min), q_max + 1):
        for n in range((5 * q + 1) // 2, 3 * q, max(1, n_stride)):
            for C, met in enumerate_induced_subsets_for_q(q, n, size_cap=size_cap):
                total += 1
                if met["epsilon"] < 2:
                    continue
                eps2 += 1
                scan = event_scan(q, C, n, m_factor * q)
                ub = union_bound(q, C)
                if ub <= scan["threshold"]:
                    union_cert += 1
                rec = {
                    "source": "induced_subset",
                    "q": q,
                    "n": n,
                    "C": C,
                    "cyclomatic": met["cyclomatic"],
                    "tau": met["tau"],
                    "epsilon": met["epsilon"],
                    "D_n": scan["D_n"],
                    "best_m": scan["best_m"],
                    "D_best": scan["D_best"],
                    "relative": float(scan["relative"]),
                    "threshold": f"{scan['threshold'].numerator}/{scan['threshold'].denominator}",
                    "best_ratio": f"{scan['best_ratio'].numerator}/{scan['best_ratio'].denominator}",
                    "union_bound": f"{ub.numerator}/{ub.denominator}",
                    "union_cert": ub <= scan["threshold"],
                }
                if scan["violation"]:
                    violations.append(rec)
                seq += 1
                heapq.heappush(best, (float(scan["relative"]), seq, rec))
                if len(best) > keep:
                    heapq.heappop(best)
    return {
        "q_max": q_max,
        "q_min": q_min,
        "m_factor": m_factor,
        "size_cap": size_cap,
        "n_stride": n_stride,
        "connected_induced_subsets_checked": total,
        "epsilon_ge_2_subsets": eps2,
        "union_certified": union_cert,
        "violations": violations,
        "near_misses": [r for _, _, r in sorted(best, reverse=True)],
    }


def fixed_cases(m_factor: int) -> list[dict]:
    cases = [
        {
            "name": "theta13",
            "q": 451,
            "n": 1350,
            "C": [240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450],
        },
        {
            "name": "Kimi",
            "q": 427,
            "n": 1280,
            "C": [216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405],
        },
        {
            "name": "v52_run_count",
            "q": 47,
            "n": 135,
            "C": [24, 30, 36, 40, 45],
        },
        {
            "name": "m_gt_2n_false_reduction",
            "q": 19,
            "n": 49,
            "C": [12, 16, 18],
        },
    ]
    out = []
    for case in cases:
        q, n, C = case["q"], case["n"], case["C"]
        met = graph_metrics(q, C, n)
        scan = event_scan(q, C, n, m_factor * q)
        density = asymptotic_density_ie(q, C)
        ub = union_bound(q, C)
        rec = {
            **case,
            "cyclomatic": met["cyclomatic"],
            "tau": met["tau"],
            "epsilon": met["epsilon"],
            "fibers": met["fibers"],
            "D_n": scan["D_n"],
            "best_m": scan["best_m"],
            "D_best": scan["D_best"],
            "relative": float(scan["relative"]),
            "threshold": f"{scan['threshold'].numerator}/{scan['threshold'].denominator}",
            "best_ratio": f"{scan['best_ratio'].numerator}/{scan['best_ratio'].denominator}",
            "union_bound": f"{ub.numerator}/{ub.denominator}",
            "union_cert": ub <= scan["threshold"],
            "asymptotic_density": None
            if density is None
            else f"{density.numerator}/{density.denominator}",
            "asymptotic_over_threshold": None
            if density is None
            else float(density / scan["threshold"]),
        }
        out.append(rec)
    return out


def random_high_defect_search(q_min: int, q_max: int, trials: int, m_factor: int, keep: int) -> dict:
    rng = random.Random(48820260517)
    best = []
    seq = 0
    violations = []
    eps2 = 0
    for t in range(trials):
        q = rng.randint(q_min, q_max)
        n = rng.randint((5 * q + 1) // 2, 3 * q - 1)
        V = list(range(q // 2 + 1, q))
        # Bias toward smooth-ish/top-collision vertices by sampling from non-isolated
        # vertices of the ambient graph when possible.
        ambient_edges = build_edges(q, V, n)
        active_vertices = sorted({a for e in ambient_edges for a in e[:2]})
        pool = active_vertices if len(active_vertices) >= 3 else V
        if len(pool) < 3:
            continue
        k = rng.randint(3, min(len(pool), 22))
        C = sorted(rng.sample(pool, k))
        met = graph_metrics(q, C, n)
        if met["epsilon"] < 2:
            continue
        eps2 += 1
        scan = event_scan(q, C, n, m_factor * q)
        ub = union_bound(q, C)
        rec = {
            "source": "random",
            "q": q,
            "n": n,
            "C": C,
            "cyclomatic": met["cyclomatic"],
            "tau": met["tau"],
            "epsilon": met["epsilon"],
            "D_n": scan["D_n"],
            "best_m": scan["best_m"],
            "D_best": scan["D_best"],
            "relative": float(scan["relative"]),
            "threshold": f"{scan['threshold'].numerator}/{scan['threshold'].denominator}",
            "best_ratio": f"{scan['best_ratio'].numerator}/{scan['best_ratio'].denominator}",
            "union_bound": f"{ub.numerator}/{ub.denominator}",
            "union_cert": ub <= scan["threshold"],
        }
        if scan["violation"]:
            violations.append(rec)
        seq += 1
        heapq.heappush(best, (float(scan["relative"]), seq, rec))
        if len(best) > keep:
            heapq.heappop(best)
    return {
        "q_min": q_min,
        "q_max": q_max,
        "trials": trials,
        "m_factor": m_factor,
        "epsilon_ge_2_hits": eps2,
        "violations": violations,
        "near_misses": [r for _, _, r in sorted(best, reverse=True)],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["fixed", "full", "induced", "random", "all"], default="all")
    parser.add_argument("--q-max", type=int, default=500)
    parser.add_argument("--q-min", type=int, default=5)
    parser.add_argument("--m-factor", type=int, default=50)
    parser.add_argument("--keep", type=int, default=20)
    parser.add_argument("--size-cap", type=int, default=18)
    parser.add_argument("--n-stride", type=int, default=1)
    parser.add_argument("--trials", type=int, default=10000)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    result = {}
    if args.mode in ("fixed", "all"):
        result["fixed"] = fixed_cases(args.m_factor)
    if args.mode in ("full", "all"):
        result["full"] = full_component_candidates(args.q_max, args.m_factor, args.keep)
    if args.mode in ("induced", "all"):
        result["induced"] = induced_subset_search(
            args.q_min, args.q_max, args.m_factor, args.size_cap, args.keep, args.n_stride
        )
    if args.mode in ("random", "all"):
        result["random"] = random_high_defect_search(
            args.q_min, args.q_max, args.trials, args.m_factor, args.keep
        )

    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
