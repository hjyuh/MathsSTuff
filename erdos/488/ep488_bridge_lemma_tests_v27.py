#!/usr/bin/env python3
"""
EP-488 Bridge Lemma diagnostics (v27) — April 11, 2026

Implements the computation-first tests from the Bridge Lemma document:

Test 1 (implemented):
  - Enumerate ALL primitive sets A with max(A) <= 20.
  - Build a partition of A into L-primitive blocks using an exact
    minimum-coloring of the L_a-overlap conflict graph (blocks are
    pairwise-disjoint in the sense L_a ∩ L_b = ∅ inside each block).
  - For n = max(A) and all m with n < m <= 10n, compute

      R(A,n,m) = ( Σ_ℓ E_ℓ(n,m)^2 / (m^2 n^2 D_ℓ) ) / ( Σ_ℓ D_ℓ ),

    where:
      D_ℓ = Σ_{a∈A^ℓ} d(L_a),
      M_ℓ(x) = Σ_{a∈A^ℓ} ( |L_a ∩ [1,x]| - d(L_a)·x ),
      E_ℓ(n,m) = 2m·M_ℓ(n) - n·M_ℓ(m).

    Here L_a is defined as in Lichtman-style “rough multiple” sets:
      L_a = { a·b : every prime factor of b is >= P(a) },
    where P(a) is the least prime factor of a.

    Then d(L_a) = (1/a)·∏_{p < P(a)} (1 - 1/p),
    and |L_a ∩ [1,x]| = #{ 1<=b<=⌊x/a⌋ : p|b ⇒ p>=P(a) }.

Test 3,4 are not yet implemented in this file; see follow-up scripts.

Notes:
  - This file is intentionally self-contained and uses exact rationals
    (fractions.Fraction) for determinism.
  - The search for n>max(A) is NOT done here; the Bridge Lemma test
    request emphasizes the convexity reduction m<=10n, and empirically
    the ratios decay quickly with n because discrepancies are periodic
    (bounded) for fixed P(a).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd
from typing import Dict, Iterable, List, Sequence, Tuple


def primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    out: List[int] = []
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            if p * p <= n:
                sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return out


PRIMES = primes_upto(100)


def least_prime_factor(a: int) -> int:
    assert a >= 2
    for p in PRIMES:
        if p * p > a:
            break
        if a % p == 0:
            return p
    return a


def is_primitive(A: Sequence[int]) -> bool:
    vals = sorted(A)
    for i, a in enumerate(vals):
        for b in vals[i + 1 :]:
            if b % a == 0:
                return False
    return True


def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def primes_lt(p0: int) -> List[int]:
    return [p for p in PRIMES if p < p0]


def ie_terms_for_primes(primes: Sequence[int]) -> List[Tuple[int, int]]:
    """Return (prod, sign) for inclusion-exclusion over divisibility by given primes.

    For y>=0:
      #{1<=n<=y : for all p in primes, p ∤ n} = Σ_{S⊆primes} (-1)^{|S|} ⌊y/∏S⌋.
    """
    terms: List[Tuple[int, int]] = [(1, 1)]
    for p in primes:
        terms += [(prod * p, -sign) for (prod, sign) in terms]
    return terms


IE_TERMS_BY_P0: Dict[int, List[Tuple[int, int]]] = {}
for p0 in [2, 3, 5, 7, 11, 13, 17, 19]:
    IE_TERMS_BY_P0[p0] = ie_terms_for_primes(primes_lt(p0))


def rough_count_ge_p0(y: int, p0: int) -> int:
    """Count b<=y with all prime factors >= p0 (equivalently: no primes < p0 divide b)."""
    if y <= 0:
        return 0
    terms = IE_TERMS_BY_P0[p0]
    total = 0
    for prod, sign in terms:
        total += sign * (y // prod)
    return total


def density_L_a(a: int) -> Fraction:
    p0 = least_prime_factor(a)
    d = Fraction(1, a)
    for p in primes_lt(p0):
        d *= Fraction(p - 1, p)
    return d


def count_L_a_upto(x: int, a: int) -> int:
    p0 = least_prime_factor(a)
    return rough_count_ge_p0(x // a, p0)


def M_a(x: int, a: int, d_a: Fraction) -> Fraction:
    return Fraction(count_L_a_upto(x, a)) - d_a * x


def l_sets_intersect(a: int, b: int) -> bool:
    """Decide whether L_a ∩ L_b is nonempty (using the lcm criterion)."""
    if a == b:
        return True
    la = least_prime_factor(a)
    lb = least_prime_factor(b)
    l = lcm2(a, b)
    qa = l // a
    qb = l // b
    # L_a contains l iff qa has no prime factor < la.
    for p in primes_lt(la):
        if qa % p == 0:
            return False
    for p in primes_lt(lb):
        if qb % p == 0:
            return False
    return True


def min_coloring_partition(vertices: List[int], conflict: Dict[Tuple[int, int], bool]) -> List[List[int]]:
    """Exact minimum coloring for small graphs (|V|<=10 typical here)."""
    if not vertices:
        return []

    # Order by decreasing degree for pruning.
    degrees = {}
    for v in vertices:
        deg = 0
        for u in vertices:
            if u == v:
                continue
            key = (min(u, v), max(u, v))
            if conflict.get(key, False):
                deg += 1
        degrees[v] = deg
    order = sorted(vertices, key=lambda v: (-degrees[v], v))

    best_k = len(order)
    best_blocks: List[List[int]] | None = None
    blocks: List[List[int]] = []

    def can_add_to_block(v: int, block: List[int]) -> bool:
        for u in block:
            key = (min(u, v), max(u, v))
            if conflict.get(key, False):
                return False
        return True

    def backtrack(i: int) -> None:
        nonlocal best_k, best_blocks
        if i == len(order):
            if best_blocks is None or len(blocks) < best_k:
                best_k = len(blocks)
                best_blocks = [list(b) for b in blocks]
            return
        if len(blocks) >= best_k:
            return

        v = order[i]
        # Try existing blocks first.
        for b in blocks:
            if can_add_to_block(v, b):
                b.append(v)
                backtrack(i + 1)
                b.pop()
        # Try new block.
        blocks.append([v])
        backtrack(i + 1)
        blocks.pop()

    backtrack(0)
    assert best_blocks is not None
    # Normalize block order for stability.
    return [sorted(b) for b in sorted(best_blocks, key=lambda b: (len(b), b))]


@dataclass(frozen=True)
class Test1Result:
    A: Tuple[int, ...]
    n: int
    m: int
    R: Fraction
    left: Fraction
    blocks: Tuple[Tuple[int, ...], ...]


def all_primitive_sets_max20() -> List[Tuple[int, ...]]:
    vals = list(range(2, 21))
    out: List[Tuple[int, ...]] = []
    for mask in range(1, 1 << len(vals)):
        A = tuple(vals[i] for i in range(len(vals)) if (mask >> i) & 1)
        if is_primitive(A):
            out.append(A)
    return out


def run_test1(max_a: int = 20) -> Tuple[Test1Result, Test1Result]:
    assert max_a == 20, "this script currently hardcodes the max=20 universe"

    # Precompute densities for a<=20.
    d_a: Dict[int, Fraction] = {a: density_L_a(a) for a in range(2, 21)}

    # Precompute M_a(x) for x up to 200 (since n=max(A)<=20 => m<=200).
    MAX_X = 200
    M_ax: Dict[int, List[Fraction]] = {a: [Fraction(0) for _ in range(MAX_X + 1)] for a in range(2, 21)}
    for a in range(2, 21):
        da = d_a[a]
        for x in range(0, MAX_X + 1):
            M_ax[a][x] = M_a(x, a, da)

    # Conflict matrix for a,b<=20.
    conflict: Dict[Tuple[int, int], bool] = {}
    for a in range(2, 21):
        for b in range(a + 1, 21):
            # conflict = NOT disjoint = intersection nonempty
            conflict[(a, b)] = l_sets_intersect(a, b)

    best: Test1Result | None = None
    best_left: Test1Result | None = None

    primitive_sets = all_primitive_sets_max20()
    for idx, A in enumerate(primitive_sets, start=1):
        M = A[-1]
        n = M
        vertices = list(A)
        blocks = min_coloring_partition(vertices, conflict)
        D_blocks = [sum(d_a[a] for a in block) for block in blocks]
        D_total = sum(D_blocks)
        if D_total == 0:
            continue

        # Precompute M_block(x) arrays for x up to 10n.
        x_max = 10 * n
        M_blocks_x: List[List[Fraction]] = []
        for block in blocks:
            arr = [Fraction(0) for _ in range(x_max + 1)]
            for a in block:
                ma = M_ax[a]
                for x in range(0, x_max + 1):
                    arr[x] += ma[x]
            M_blocks_x.append(arr)

        best_for_A: Fraction | None = None
        best_left_for_A: Fraction | None = None
        best_m_for_A = None
        for m in range(n + 1, 10 * n + 1):
            numerator = Fraction(0)
            for arr, D in zip(M_blocks_x, D_blocks):
                E = 2 * m * arr[n] - n * arr[m]
                numerator += (E * E) / D
            left = numerator / (m * m * n * n)
            R = left / D_total
            if best_for_A is None or R > best_for_A:
                best_for_A = R
                best_left_for_A = left
                best_m_for_A = m

        assert best_for_A is not None and best_m_for_A is not None and best_left_for_A is not None
        if best is None or best_for_A > best.R:
            best = Test1Result(
                A=A,
                n=n,
                m=best_m_for_A,
                R=best_for_A,
                left=best_left_for_A,
                blocks=tuple(tuple(b) for b in blocks),
            )

        if best_left is None or best_left_for_A > best_left.left:
            best_left = Test1Result(
                A=A,
                n=n,
                m=best_m_for_A,
                R=best_for_A,
                left=best_left_for_A,
                blocks=tuple(tuple(b) for b in blocks),
            )

        if idx % 1000 == 0:
            assert best is not None and best_left is not None
            print(
                f"[test1] processed {idx}/{len(primitive_sets)} sets; "
                f"best R={float(best.R):.6f} at A={best.A}; "
                f"best left={float(best_left.left):.6f} at A={best_left.A}"
            )

    assert best is not None and best_left is not None
    return best, best_left


def main() -> None:
    print("=" * 80)
    print("EP-488 Bridge Lemma - Test 1 (L^2 block-dispersion ratio) - v27")
    print("=" * 80)
    best, best_left = run_test1(max_a=20)
    print("\nMAXIMIZER OF R = left / (sum D) (as written in the Bridge Lemma Test 1)")
    print(f"  A = {list(best.A)}")
    print(f"  partition blocks = {[list(b) for b in best.blocks]}")
    print(f"  n = {best.n}, m = {best.m}")
    print(f"  left(A,n,m) = {best.left} = {float(best.left):.12f}")
    print(f"  R(A,n,m) = {best.R} = {float(best.R):.12f}")
    print(f"  margin to 1: 1 - R = {float(1 - best.R):.12f}")

    print("\nMAXIMIZER OF left = sum E_ell^2/(m^2 n^2 D_ell)  (no division by sum D_ell)")
    print(f"  A = {list(best_left.A)}")
    print(f"  partition blocks = {[list(b) for b in best_left.blocks]}")
    print(f"  n = {best_left.n}, m = {best_left.m}")
    print(f"  left(A,n,m) = {best_left.left} = {float(best_left.left):.12f}")
    print(f"  R(A,n,m) = {best_left.R} = {float(best_left.R):.12f}")
    print("\nDONE.")


if __name__ == "__main__":
    main()
