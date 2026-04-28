#!/usr/bin/env python3
"""
EP-488 Bridge Lemma diagnostics (v27): Tests 3 and 4 — April 11, 2026

Test 3 (sieve overshoot ratio):
  - Generate primitive sets A with max(A) in [50, 200] (random + structured).
  - Extract a quotient-core / quotient-tail antichain Q from anchor a=min(A):
        Q_raw = { b / gcd(a,b) : b in A, b != a }
        Q = prim(Q_raw \\ {1})   (remove q divisible by smaller q)
  - Define A_Q(x) = #{1<=n<=x : for all q in Q, q ∤ n}.
  - Compute δ_Q exactly:
      - if Q pairwise coprime: δ_Q = ∏_{q∈Q} (1 - 1/q)
      - else via inclusion-exclusion over subset lcms
  - Compute R(Q) = max_{x in [max(Q), 10*max(Q)]} A_Q(x) / (δ_Q x).
  - Report max R(Q) seen and compare to e^γ ≈ 1.78107241799.

Test 4 (sawtooth inner products):
  - For sampled primitive sets A (size 5..10), compute
        ψ_d(x) = {x/d} - 1/2  for integer x,
    and discrete inner products on [n,10n):
        <ψ_d,ψ_e> = (1/(9n)) Σ_{x=n}^{10n-1} ψ_d(x) ψ_e(x).
  - Report sign statistics (how often positive, max positive, min negative).

This script is computation-only; it does not attempt any proofs.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd
from typing import Iterable, List, Sequence, Tuple


EULER_GAMMA = 0.5772156649015328606065120900824024310421
E_GAMMA = 1.7810724179901979852365041031071795491696  # exp(EulerGamma)


def is_primitive(values: Sequence[int]) -> bool:
    A = sorted(values)
    for i, a in enumerate(A):
        for b in A[i + 1 :]:
            if b % a == 0:
                return False
    return True


def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def primitivize_antichain(values: Iterable[int]) -> Tuple[int, ...]:
    vals = sorted(set(v for v in values if v > 1))
    out: List[int] = []
    for v in vals:
        if any(v % u == 0 for u in out):
            continue
        out.append(v)
    return tuple(out)


def quotient_tail_antichain(A: Sequence[int], anchor: int | None = None) -> Tuple[int, ...]:
    A = sorted(A)
    if anchor is None:
        anchor = A[0]
    raw = []
    for b in A:
        if b == anchor:
            continue
        raw.append(b // gcd(anchor, b))
    return primitivize_antichain(raw)


def pairwise_coprime(Q: Sequence[int]) -> bool:
    for i, a in enumerate(Q):
        for b in Q[i + 1 :]:
            if gcd(a, b) != 1:
                return False
    return True


def delta_unsieved(Q: Sequence[int]) -> Fraction:
    """Exact density of integers not divisible by any q in Q."""
    Q = tuple(Q)
    if not Q:
        return Fraction(1, 1)
    if pairwise_coprime(Q):
        d = Fraction(1, 1)
        for q in Q:
            d *= Fraction(q - 1, q)
        return d

    # Inclusion-exclusion on lcms: δ = Σ_{S⊆Q} (-1)^{|S|} 1/lcm(S).
    lcms = [1]
    signs = [1]
    for q in Q:
        new_lcms = []
        new_signs = []
        for L, sgn in zip(lcms, signs):
            new_lcms.append(lcm2(L, q))
            new_signs.append(-sgn)
        lcms += new_lcms
        signs += new_signs

    total = Fraction(0, 1)
    for L, sgn in zip(lcms, signs):
        total += Fraction(sgn, L)
    return total


def overshoot_ratio(Q: Sequence[int]) -> Tuple[Fraction, int, Fraction]:
    """Return (max_ratio, argmax_x, delta_Q) with exact rationals."""
    Q = tuple(Q)
    if not Q:
        return Fraction(1, 1), 1, Fraction(1, 1)
    delta = delta_unsieved(Q)
    if delta <= 0:
        return Fraction(10**9, 1), max(Q), delta

    qmax = max(Q)
    X = 10 * qmax
    hit = bytearray(X + 1)
    for q in Q:
        for m in range(q, X + 1, q):
            hit[m] = 1

    unsieved = 0
    best_ratio = Fraction(-1, 1)
    best_x = qmax
    for x in range(1, X + 1):
        if not hit[x]:
            unsieved += 1
        if x < qmax:
            continue
        ratio = Fraction(unsieved, 1) / (delta * x)
        if ratio > best_ratio:
            best_ratio = ratio
            best_x = x
    return best_ratio, best_x, delta


def random_primitive_set(max_a: int, size: int, min_a: int = 2) -> Tuple[int, ...] | None:
    pool = list(range(min_a, max_a + 1))
    random.shuffle(pool)
    chosen: List[int] = []
    for v in pool:
        if any(v % u == 0 or u % v == 0 for u in chosen):
            continue
        chosen.append(v)
        if len(chosen) == size:
            return tuple(sorted(chosen))
    return None


@dataclass(frozen=True)
class Test3Row:
    A: Tuple[int, ...]
    Q: Tuple[int, ...]
    delta: Fraction
    best_x: int
    ratio: Fraction


def run_test3(sample_count: int, seed: int) -> Test3Row:
    random.seed(seed)

    best: Test3Row | None = None

    # Structured family: scaled primes {2p} clipped to max<=200.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    A_scaled = tuple(sorted(2 * p for p in primes if 2 * p <= 200))
    if is_primitive(A_scaled) and 50 <= max(A_scaled) <= 200:
        Q = quotient_tail_antichain(A_scaled, anchor=min(A_scaled))
        ratio, best_x, delta = overshoot_ratio(Q)
        best = Test3Row(A=A_scaled, Q=Q, delta=delta, best_x=best_x, ratio=ratio)

    # Random sampling.
    for i in range(sample_count):
        max_a = random.randint(50, 200)
        size = random.randint(5, 12)
        A = random_primitive_set(max_a=max_a, size=size, min_a=2)
        if A is None:
            continue
        if not (50 <= max(A) <= 200):
            continue
        Q = quotient_tail_antichain(A, anchor=min(A))
        if not Q:
            continue
        ratio, best_x, delta = overshoot_ratio(Q)
        row = Test3Row(A=A, Q=Q, delta=delta, best_x=best_x, ratio=ratio)
        if best is None or row.ratio > best.ratio:
            best = row
        if (i + 1) % 500 == 0:
            assert best is not None
            print(f"[test3] {i+1}/{sample_count}: current best R={float(best.ratio):.6f} at max(A)={max(best.A)} |Q|={len(best.Q)}")

    assert best is not None
    return best


def psi_frac(x: int, d: int) -> float:
    return (x % d) / d - 0.5


@dataclass(frozen=True)
class InnerProductStats:
    A: Tuple[int, ...]
    n: int
    pairs: int
    pos_pairs: int
    max_pos: float
    min_val: float


def inner_product_stats(A: Sequence[int], n: int) -> InnerProductStats:
    A = tuple(sorted(A))
    assert is_primitive(A)
    lo = n
    hi = 10 * n
    length = hi - lo
    assert length > 0

    pairs = 0
    pos_pairs = 0
    max_pos = -1e9
    min_val = 1e9
    for i, d in enumerate(A):
        for e in A[i + 1 :]:
            s = 0.0
            for x in range(lo, hi):
                s += psi_frac(x, d) * psi_frac(x, e)
            ip = s / length
            pairs += 1
            if ip > 0:
                pos_pairs += 1
                if ip > max_pos:
                    max_pos = ip
            if ip < min_val:
                min_val = ip
    if pos_pairs == 0:
        max_pos = 0.0
    return InnerProductStats(A=A, n=n, pairs=pairs, pos_pairs=pos_pairs, max_pos=max_pos, min_val=min_val)


def run_test4(sample_count: int, seed: int, n: int) -> InnerProductStats:
    random.seed(seed)
    best = None
    for i in range(sample_count):
        max_a = random.randint(50, 200)
        size = random.randint(5, 10)
        A = random_primitive_set(max_a=max_a, size=size, min_a=2)
        if A is None:
            continue
        stats = inner_product_stats(A, n=n)
        # “Worst” here means most positive cross-covariance observed.
        if best is None or stats.max_pos > best.max_pos:
            best = stats
        if (i + 1) % 200 == 0:
            assert best is not None
            print(f"[test4] {i+1}/{sample_count}: best max_pos={best.max_pos:.6e} with pos_pairs={best.pos_pairs}/{best.pairs}")
    assert best is not None
    return best


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test3-samples", type=int, default=3000)
    parser.add_argument("--test4-samples", type=int, default=800)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n", type=int, default=2000, help="inner-product window base n (uses [n,10n))")
    args = parser.parse_args()

    print("=" * 80)
    print("EP-488 Bridge Lemma — Test 3 (sieve overshoot ratio) — v27")
    print("=" * 80)
    best3 = run_test3(sample_count=args.test3_samples, seed=args.seed)
    print("\nWORST R(Q) FOUND (over sampled primitive sets, anchor=min(A))")
    print(f"  A = {list(best3.A)} (min={min(best3.A)}, max={max(best3.A)}, |A|={len(best3.A)})")
    print(f"  Q = {list(best3.Q)} (|Q|={len(best3.Q)}, max(Q)={max(best3.Q)})")
    print(f"  delta_Q = {best3.delta} = {float(best3.delta):.12f}")
    print(f"  argmax x = {best3.best_x}")
    print(f"  R(Q) = {best3.ratio} = {float(best3.ratio):.12f}")
    print(f"  compare: e^gamma ~ {E_GAMMA:.12f}")
    print(f"  ratio / e^gamma = {float(best3.ratio) / E_GAMMA:.6f}")

    print("\n" + "=" * 80)
    print("EP-488 Bridge Lemma — Test 4 (sawtooth inner-product sign) — v27")
    print("=" * 80)
    best4 = run_test4(sample_count=args.test4_samples, seed=args.seed + 1, n=args.n)
    print("\nMOST POSITIVE CROSS-INNER-PRODUCT FOUND (over sampled primitive sets)")
    print(f"  A = {list(best4.A)} (|A|={len(best4.A)}, max={max(best4.A)})")
    print(f"  window: [{best4.n}, {10*best4.n}) (length {9*best4.n})")
    print(f"  pairs = {best4.pairs}, positive pairs = {best4.pos_pairs}")
    print(f"  max positive <psi_d,psi_e> = {best4.max_pos:.12e}")
    print(f"  most negative <psi_d,psi_e> = {best4.min_val:.12e}")
    print("\nDONE.")


if __name__ == "__main__":
    main()
