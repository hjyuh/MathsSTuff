#!/usr/bin/env python3
"""
EP-488 v27: Target Lemma B sanity-check (Additive Contraction).

Lemma B as written in `unified-truth-v27-april11-evening.md` claims:

  For primitive Q with max(Q) <= y and δ_Q >= 0.28, letting d(Q)=1-δ_Q,
  for all x >= y:
      |Δ_Q(x)|/x < d(Q)/3,
  where Δ_Q(x) = A_Q(x) - δ_Q x and A_Q(x) counts integers <= x not divisible
  by any q in Q.

This script produces explicit counterexamples (family Q={y-1,y}) and, optionally,
randomly mines more.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Sequence, Tuple


def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def is_primitive(values: Sequence[int]) -> bool:
    vals = sorted(values)
    for i, a in enumerate(vals):
        for b in vals[i + 1 :]:
            if b % a == 0:
                return False
    return True


def primitivize_antichain(values: Iterable[int]) -> Tuple[int, ...]:
    vals = sorted(set(v for v in values if v > 1))
    out = []
    for v in vals:
        if any(v % u == 0 for u in out):
            continue
        out.append(v)
    return tuple(out)


def pairwise_coprime(Q: Sequence[int]) -> bool:
    Q = tuple(Q)
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


def A_Q_upto(Q: Sequence[int], X: int) -> list[int]:
    """Compute A_Q(x) for 0<=x<=X by marking multiples."""
    hit = bytearray(X + 1)
    for q in Q:
        for m in range(q, X + 1, q):
            hit[m] = 1
    A = [0] * (X + 1)
    s = 0
    for x in range(1, X + 1):
        if not hit[x]:
            s += 1
        A[x] = s
    return A


@dataclass(frozen=True)
class DiscrepancyMax:
    Q: Tuple[int, ...]
    y: int
    delta: Fraction
    d: Fraction
    bound: Fraction
    best_x: int
    best_ratio: Fraction
    best_delta: Fraction


def max_discrepancy_ratio(Q: Sequence[int], x0: int, X: int) -> DiscrepancyMax:
    Q = tuple(Q)
    assert Q
    assert is_primitive(Q)
    y = max(Q)
    delta = delta_unsieved(Q)
    d = Fraction(1, 1) - delta
    bound = d / 3
    A = A_Q_upto(Q, X)

    best_ratio = Fraction(-1, 1)
    best_x = x0
    best_delta = Fraction(0, 1)
    for x in range(x0, X + 1):
        disc = Fraction(A[x], 1) - delta * x
        ratio = abs(disc) / x
        if ratio > best_ratio:
            best_ratio = ratio
            best_x = x
            best_delta = disc

    return DiscrepancyMax(
        Q=Q,
        y=y,
        delta=delta,
        d=d,
        bound=bound,
        best_x=best_x,
        best_ratio=best_ratio,
        best_delta=best_delta,
    )


def show_family_counterexample(y: int) -> None:
    Q = (y - 1, y)
    assert y >= 3
    assert is_primitive(Q)

    x = 2 * y - 3
    delta = delta_unsieved(Q)
    d = Fraction(1, 1) - delta
    bound = d / 3

    A = A_Q_upto(Q, x)
    disc = Fraction(A[x], 1) - delta * x
    ratio = abs(disc) / x

    print("=" * 80)
    print("Explicit family counterexample to Lemma B")
    print("=" * 80)
    print(f"Q = {{y-1, y}} with y = {y}")
    print(f"  Q = {Q}, max(Q)=y={y}, x = 2y-3 = {x}")
    print(f"  delta_Q = {delta} = {float(delta):.12f}")
    print(f"  d(Q) = 1-delta_Q = {d} = {float(d):.12f}")
    print(f"  Lemma-B bound d(Q)/3 = {bound} = {float(bound):.12f}")
    print(f"  A_Q(x) = {A[x]}")
    print(f"  Delta_Q(x) = A_Q(x) - delta_Q*x = {disc} = {float(disc):.12f}")
    print(f"  |Delta_Q(x)|/x = {ratio} = {float(ratio):.12f}")
    if bound > 0:
        print(f"  (|Delta|/x) / (d/3) = {Fraction(ratio, bound)} = {float(ratio / bound):.12f}")
    print()
    print("As y->infty, (|Delta|/x)/(d/3) -> 3/2, so any universal constant < 1/2 is impossible.")


def random_primitive_antichain(max_q: int, size: int) -> Tuple[int, ...] | None:
    pool = list(range(2, max_q + 1))
    random.shuffle(pool)
    chosen = []
    for v in pool:
        if any(v % u == 0 or u % v == 0 for u in chosen):
            continue
        chosen.append(v)
        if len(chosen) == size:
            return tuple(sorted(chosen))
    return None


def mine_random(
    samples: int,
    seed: int,
    max_q: int,
    min_size: int,
    max_size: int,
    x_mult: int,
) -> None:
    random.seed(seed)
    worst: DiscrepancyMax | None = None
    violations = 0

    for _ in range(samples):
        size = random.randint(min_size, max_size)
        Q = random_primitive_antichain(max_q=max_q, size=size)
        if Q is None:
            continue
        delta = delta_unsieved(Q)
        if delta < Fraction(28, 100):
            continue
        y = max(Q)
        stats = max_discrepancy_ratio(Q, x0=y, X=x_mult * y)
        if stats.bound > 0 and stats.best_ratio >= stats.bound:
            violations += 1
        if worst is None and stats.bound > 0:
            worst = stats
        elif stats.bound > 0 and worst is not None:
            if stats.best_ratio / stats.bound > worst.best_ratio / worst.bound:
                worst = stats

    print("=" * 80)
    print("Random mining summary (not exhaustive)")
    print("=" * 80)
    print(f"samples={samples}, seed={seed}, max_q={max_q}, size∈[{min_size},{max_size}], x≤{x_mult}y")
    print(f"violations (best_ratio >= d/3): {violations}")
    if worst is None:
        return
    print("\nWorst (best_ratio / (d/3)) found:")
    print(f"  Q = {worst.Q} (|Q|={len(worst.Q)}, y={worst.y})")
    print(f"  delta_Q = {worst.delta} = {float(worst.delta):.12f}")
    print(f"  d(Q) = {worst.d} = {float(worst.d):.12f}")
    print(f"  bound d/3 = {worst.bound} = {float(worst.bound):.12f}")
    print(f"  best x = {worst.best_x}")
    print(f"  |Delta|/x = {worst.best_ratio} = {float(worst.best_ratio):.12f}")
    print(f"  Delta(best x) = {worst.best_delta} = {float(worst.best_delta):.12f}")
    print(f"  (|Delta|/x)/(d/3) = {Fraction(worst.best_ratio, worst.bound)} = {float(worst.best_ratio / worst.bound):.12f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--y", type=int, default=165, help="parameter for Q={y-1,y} family")
    parser.add_argument("--mine", action="store_true", help="also run random mining")
    parser.add_argument("--samples", type=int, default=8000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--max-q", type=int, default=200)
    parser.add_argument("--min-size", type=int, default=2)
    parser.add_argument("--max-size", type=int, default=6)
    parser.add_argument("--x-mult", type=int, default=2, help="mine x in [y, x_mult*y]")
    args = parser.parse_args()

    show_family_counterexample(y=args.y)
    if args.mine:
        mine_random(
            samples=args.samples,
            seed=args.seed,
            max_q=args.max_q,
            min_size=args.min_size,
            max_size=args.max_size,
            x_mult=args.x_mult,
        )


if __name__ == "__main__":
    main()
