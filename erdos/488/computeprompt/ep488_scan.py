#!/usr/bin/env python3
"""
EP-488 quotient-core scan.

This script implements the prompt-defined symmetric quotient-core model

    Q_j = { a_i / gcd(a_i, a_j) : i != j, > 1 }

together with
    P_j = union of prime factors of Q_j
    q_j = product(P_j)
    rho_j = prod_p (1 - 1/p)

and the prompt-defined layer count
    K_{Q_j}(y) = #{n <= y : gcd(n, q_j) = 1}.

It also provides the exact peeling-by-divisibility decomposition:

    B_j = { a_i / gcd(a_i, a_j) : i < j, > 1 }
    L_j(y) = #{n <= y : b ∤ n for every b in B_j}

for which
    F_A(x) = sum_j L_j(floor(x/a_j))
is exact, by assigning each counted integer to the smallest layer that divides it.

The main driver reproduces the scans used in the attached report.
"""

from __future__ import annotations

import csv
import gzip
import json
import math
import os
import random
from collections import Counter
from functools import lru_cache
from typing import Dict, Iterable, List, Sequence, Tuple


def sieve_primes(n: int) -> List[int]:
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : n + 1 : p] = [False] * (((n - start) // p) + 1)
    return [i for i, ok in enumerate(is_prime) if ok]


PRIMES = sieve_primes(1000)
PRIME_FACTORS: Dict[int, Tuple[int, ...]] = {0: (), 1: ()}
for n in range(2, 1001):
    m = n
    factors: List[int] = []
    for p in PRIMES:
        if p * p > m:
            break
        if m % p == 0:
            factors.append(p)
            while m % p == 0:
                m //= p
        if m == 1:
            break
    if m > 1:
        factors.append(m)
    PRIME_FACTORS[n] = tuple(factors)


def largest_prime_factor(n: int) -> int:
    return PRIME_FACTORS[n][-1] if n > 1 else 1


def is_primitive(A: Sequence[int]) -> bool:
    A = sorted(A)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True


@lru_cache(maxsize=None)
def coprime_prefix(prime_tuple: Tuple[int, ...], max_y: int = 1000) -> Tuple[int, ...]:
    primes = list(prime_tuple)
    pref = [0] * (max_y + 1)
    c = 0
    for n in range(1, max_y + 1):
        ok = True
        for p in primes:
            if n % p == 0:
                ok = False
                break
        if ok:
            c += 1
        pref[n] = c
    return tuple(pref)


def K_Q(y: int, Q: Sequence[int]) -> int:
    """Prompt-defined K_Q: count n <= y coprime to every q in Q."""
    if y <= 0:
        return 0
    P = set()
    for q in Q:
        P.update(PRIME_FACTORS[q])
    return coprime_prefix(tuple(sorted(P)))[y]


def compute_quotient_cores(A: Sequence[int]) -> List[Dict[str, object]]:
    """
    Prompt-defined symmetric quotient-core data.
    """
    A = tuple(sorted(A))
    M = A[-1]
    layers: List[Dict[str, object]] = []
    for j, a_j in enumerate(A):
        Q_j = set()
        P_j = set()
        for i, a_i in enumerate(A):
            if i == j:
                continue
            b = a_i // math.gcd(a_i, a_j)
            if b > 1:
                Q_j.add(b)
                P_j.update(PRIME_FACTORS[b])
        q_j = 1
        rho_j = 1.0
        for p in sorted(P_j):
            q_j *= p
            rho_j *= 1.0 - 1.0 / p
        r_j = M / a_j
        c_j = r_j * rho_j
        e_j = (q_j + 1) * rho_j
        layers.append(
            {
                "a_j": a_j,
                "Q_j": tuple(sorted(Q_j)),
                "P_j": tuple(sorted(P_j)),
                "q_j": q_j,
                "r_j": r_j,
                "rho_j": rho_j,
                "c_j": c_j,
                "e_j": e_j,
                "r_over_q": (r_j / q_j if q_j else math.inf),
            }
        )
    return layers


def F_union_prefix(A: Sequence[int], Xmax: int) -> List[int]:
    arr = [0] * (Xmax + 1)
    for a in A:
        for m in range(a, Xmax + 1, a):
            arr[m] = 1
    pref = [0] * (Xmax + 1)
    c = 0
    for x in range(1, Xmax + 1):
        c += arr[x]
        pref[x] = c
    return pref


def exact_peeling_obstructions(A: Sequence[int]) -> List[Tuple[int, ...]]:
    """
    Exact peeling obstructions using only earlier layers and divisibility.
    """
    A = tuple(sorted(A))
    out: List[Tuple[int, ...]] = []
    for j, a_j in enumerate(A):
        B_j = []
        for i in range(j):
            b = A[i] // math.gcd(A[i], a_j)
            if b > 1 and b not in B_j:
                B_j.append(b)
        out.append(tuple(sorted(B_j)))
    return out


def exact_peeling_count(y: int, B_j: Sequence[int]) -> int:
    if y <= 0:
        return 0
    return sum(1 for n in range(1, y + 1) if all(n % b != 0 for b in B_j))


def verify_exact_peeling(A: Sequence[int]) -> bool:
    """
    Check the exact divisibility peeling identity on x in [M, 10M].
    """
    A = tuple(sorted(A))
    M = A[-1]
    union_pref = F_union_prefix(A, 10 * M)
    B = exact_peeling_obstructions(A)
    for x in range(M, 10 * M + 1):
        s = sum(exact_peeling_count(x // A[j], B[j]) for j in range(len(A)))
        if s != union_pref[x]:
            return False
    return True


def analyze_set(A: Sequence[int], need_union: bool = True, need_true_ratio: bool = True) -> Dict[str, object]:
    A = tuple(sorted(A))
    k = len(A)
    M = A[-1]
    Xmax = 10 * M

    layers = compute_quotient_cores(A)
    q_prefixes = [coprime_prefix(tuple(layer["P_j"])) for layer in layers]
    c_list = [float(layer["c_j"]) for layer in layers]

    actual_v = [0.0] * k
    actual_u = [0.0] * k
    sup_H = float("-inf")
    inf_H = float("inf")

    union_pref = F_union_prefix(A, Xmax) if need_union else None
    decomp_ok = True if need_union else None
    first_mismatch = None
    max_gap = 0

    sup_G = float("-inf") if need_true_ratio else None
    inf_G = float("inf") if need_true_ratio else None

    for x in range(M, Xmax + 1):
        M_over_x = M / x
        H = 0.0
        unscaled_sum = 0
        for j, a_j in enumerate(A):
            count = q_prefixes[j][x // a_j]
            unscaled_sum += count
            T = M_over_x * count
            eps = T - c_list[j]
            if eps > actual_v[j]:
                actual_v[j] = eps
            if -eps > actual_u[j]:
                actual_u[j] = -eps
            H += T

        sup_H = max(sup_H, H)
        inf_H = min(inf_H, H)

        if need_union and union_pref is not None:
            gap = unscaled_sum - union_pref[x]
            if gap != 0 and decomp_ok:
                decomp_ok = False
                first_mismatch = (x, unscaled_sum, union_pref[x])
            max_gap = max(max_gap, abs(gap))
            if need_true_ratio:
                G = M_over_x * union_pref[x]
                sup_G = max(sup_G, G)
                inf_G = min(inf_G, G)

    C = sum(float(layer["c_j"]) for layer in layers)
    E = sum(float(layer["e_j"]) for layer in layers)
    V = sum(actual_v)
    U = sum(actual_u)

    return {
        "A": A,
        "A_str": "{" + ",".join(map(str, A)) + "}",
        "M": M,
        "k": k,
        "layers": layers,
        "C": C,
        "E": E,
        "E_over_C": (E / C if C else math.inf),
        "surplus": sum(
            float(layer["rho_j"]) * (float(layer["r_j"]) - 3.0 * float(layer["q_j"]) - 2.0)
            for layer in layers
        ),
        "worst_r_over_q": min(float(layer["r_over_q"]) for layer in layers),
        "H_ratio": (sup_H / inf_H if inf_H > 0 else math.inf),
        "H_sup": sup_H,
        "H_inf": inf_H,
        "V": V,
        "U": U,
        "budget": V + 2.0 * U,
        "budget_ratio": ((V + 2.0 * U) / C if C else math.inf),
        "decomp_ok": decomp_ok,
        "first_mismatch": first_mismatch,
        "max_gap": max_gap,
        "true_ratio": (sup_G / inf_G if need_true_ratio and inf_G and inf_G > 0 else None),
        "G_sup": sup_G,
        "G_inf": inf_G,
        "theoretical_ok": (E < C / 3.0 if C else False),
        "actual_ok": ((V + 2.0 * U) < C if C else False),
        "actual_v": actual_v,
        "actual_u": actual_u,
    }


def primitive_sets_upto(N: int, max_size: int) -> Iterable[Tuple[int, ...]]:
    """
    Enumerate all primitive subsets of {1,...,N} with size <= max_size.
    """
    def backtrack(selected: List[int], remaining: List[int]) -> Iterable[Tuple[int, ...]]:
        if selected:
            yield tuple(selected)
        if len(selected) == max_size:
            return
        for idx, c in enumerate(remaining):
            new_remaining = [n for n in remaining[idx + 1 :] if n % c != 0]
            selected.append(c)
            yield from backtrack(selected, new_remaining)
            selected.pop()

    yield from backtrack([], list(range(1, N + 1)))


def primitive_prune(sample: Sequence[int]) -> Tuple[int, ...]:
    """
    Keep larger numbers and delete smaller divisors to get a primitive set.
    """
    kept: List[int] = []
    for n in sorted(set(sample), reverse=True):
        if all(m % n != 0 for m in kept):
            kept.append(n)
    return tuple(sorted(kept))


def random_primitive_set_general(rng: random.Random, Mmax: int = 100, kmax: int = 10) -> Tuple[int, ...]:
    while True:
        M = rng.randint(2, Mmax)
        target = rng.randint(1, kmax)
        pool = list(range(2, M + 1))
        sample_size = min(len(pool), max(target, target + rng.randint(0, target)))
        picks = rng.sample(pool, sample_size)
        picks.append(M)
        A = primitive_prune(picks)
        if not A:
            continue
        if A[-1] != M:
            A = primitive_prune(tuple(sorted(set(A + (M,)))))
        if len(A) > kmax:
            others = [n for n in A if n != M]
            rng.shuffle(others)
            A = tuple(sorted([M] + others[: kmax - 1]))
        if 1 <= len(A) <= kmax:
            return A


def random_primitive_set_smooth(
    rng: random.Random, pool: Sequence[int], kmax: int = 10
) -> Tuple[int, ...]:
    while True:
        M = rng.choice(list(pool))
        eligible = [n for n in pool if n <= M]
        target = rng.randint(1, kmax)
        sample_size = min(len(eligible), max(target, target + rng.randint(0, target + 2)))
        picks = rng.sample(eligible, sample_size)
        picks.append(M)
        A = primitive_prune(picks)
        if not A:
            continue
        if A[-1] != M:
            A = primitive_prune(tuple(sorted(set(A + (M,)))))
        if len(A) > kmax:
            others = [n for n in A if n != M]
            rng.shuffle(others)
            A = tuple(sorted([M] + others[: kmax - 1]))
        if 1 <= len(A) <= kmax:
            return A


def generate_unique_samples(
    generator_func,
    target_count: int,
    *args,
    **kwargs,
) -> List[Tuple[int, ...]]:
    seen = set()
    samples: List[Tuple[int, ...]] = []
    attempts = 0
    while len(samples) < target_count and attempts < 100 * target_count:
        A = generator_func(*args, **kwargs)
        attempts += 1
        if A not in seen:
            seen.add(A)
            samples.append(A)
    return samples


def write_summary_csv(path: str, category: str, results: Iterable[Dict[str, object]]) -> None:
    fieldnames = [
        "category",
        "A",
        "M",
        "k",
        "E_over_C",
        "surplus",
        "H_ratio",
        "budget_ratio",
        "worst_r_over_q",
        "theoretical_ok",
        "actual_ok",
        "decomp_ok",
        "first_mismatch_x",
        "first_mismatch_sum",
        "first_mismatch_F",
        "max_gap",
        "true_ratio",
        "C",
        "E",
        "V",
        "U",
        "budget",
    ]

    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "wt", newline="") as f:  # type: ignore[arg-type]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for res in results:
            fm = res["first_mismatch"] if res["first_mismatch"] else (None, None, None)
            writer.writerow(
                {
                    "category": category,
                    "A": res["A_str"],
                    "M": res["M"],
                    "k": res["k"],
                    "E_over_C": res["E_over_C"],
                    "surplus": res["surplus"],
                    "H_ratio": res["H_ratio"],
                    "budget_ratio": res["budget_ratio"],
                    "worst_r_over_q": res["worst_r_over_q"],
                    "theoretical_ok": res["theoretical_ok"],
                    "actual_ok": res["actual_ok"],
                    "decomp_ok": res["decomp_ok"],
                    "first_mismatch_x": fm[0],
                    "first_mismatch_sum": fm[1],
                    "first_mismatch_F": fm[2],
                    "max_gap": res["max_gap"],
                    "true_ratio": res["true_ratio"],
                    "C": res["C"],
                    "E": res["E"],
                    "V": res["V"],
                    "U": res["U"],
                    "budget": res["budget"],
                }
            )



def main() -> None:
    outdir = "ep488_outputs"
    os.makedirs(outdir, exist_ok=True)

    seed = 20260405
    rng = random.Random(seed)

    def exhaustive_iter():
        for A in primitive_sets_upto(30, 6):
            yield analyze_set(A)

    write_summary_csv(os.path.join(outdir, "ep488_exhaustive_results.csv.gz"), "exhaustive<=30", exhaustive_iter())

    rand_samples = generate_unique_samples(random_primitive_set_general, 10000, rng)
    def random_iter():
        for A in rand_samples:
            yield analyze_set(A)
    write_summary_csv(os.path.join(outdir, "ep488_random_results.csv"), "random<=100", random_iter())

    smooth_pool = [n for n in range(2, 101) if largest_prime_factor(n) <= 11]
    smooth_samples = generate_unique_samples(random_primitive_set_smooth, 5000, rng, smooth_pool)
    def smooth_iter():
        for A in smooth_samples:
            yield analyze_set(A)
    write_summary_csv(os.path.join(outdir, "ep488_smooth_adversarial_results.csv"), "smooth<=100", smooth_iter())

    payload = {
        "seed": seed,
        "random_count": len(rand_samples),
        "smooth_count": len(smooth_samples),
        "counterexample": analyze_set((10, 21)),
    }
    with open(os.path.join(outdir, "ep488_run_info.json"), "w") as f:
        json.dump(payload, f, indent=2)


if __name__ == "__main__":
    main()
