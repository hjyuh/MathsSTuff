"""
Counterexample search for the proposed uniform depth-2 theorem in EP-488.

This script works with the exact band coefficient

    c_s(lambda) = (s + 1) * (L_s(t) - 2 * lambda),

where t = floor((s + 1) * lambda) and L_s(t) counts integers <= t coprime to
all primes <= s.

It shows that the proposed no-triple-overlap lemma is false: there are
geometric two-step chains r -> s -> t whose badness regions U_r, U_s, U_t have
nonempty triple intersection.
"""

from __future__ import annotations

from fractions import Fraction


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            sieve[p * p : n + 1 : p] = [False] * (((n - p * p) // p) + 1)
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def survivor_count(primes: list[int], t: int) -> int:
    return sum(1 for x in range(1, t + 1) if all(x % p for p in primes))


def band_intervals(s: int) -> list[tuple[Fraction, Fraction]]:
    primes = primes_up_to(s)
    t_max = ((s + 1) * (s + 1) - 1) // 2
    intervals: list[tuple[Fraction, Fraction]] = []
    for t in range(s + 1, t_max + 1):
        l_val = survivor_count(primes, t)
        left = Fraction(t, s + 1)
        right = min(Fraction(t + 1, s + 1), Fraction(l_val, 2))
        if left < right:
            intervals.append((left, right))
    return merge(intervals)


def merge(
    intervals: list[tuple[Fraction, Fraction]],
) -> list[tuple[Fraction, Fraction]]:
    if not intervals:
        return []
    intervals = sorted(intervals)
    merged: list[list[Fraction]] = [[intervals[0][0], intervals[0][1]]]
    for left, right in intervals[1:]:
        if left > merged[-1][1]:
            merged.append([left, right])
        elif right > merged[-1][1]:
            merged[-1][1] = right
    return [(left, right) for left, right in merged]


def intersect(
    a: list[tuple[Fraction, Fraction]],
    b: list[tuple[Fraction, Fraction]],
) -> list[tuple[Fraction, Fraction]]:
    out: list[tuple[Fraction, Fraction]] = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        left = max(a[i][0], b[j][0])
        right = min(a[i][1], b[j][1])
        if left < right:
            out.append((left, right))
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return out


def live_edges(max_s: int) -> list[tuple[int, int, int]]:
    edges: list[tuple[int, int, int]] = []
    for root in range(4, max_s + 1):
        for child in range(4, root):
            for h in range(3, 2 * root + 3, 2):
                if Fraction(2 * root, child + 1) < h < Fraction(2 * (root + 1), child):
                    edges.append((root, child, h))
    return edges


def band_coefficient(s: int, lam: Fraction) -> tuple[int, int, Fraction]:
    primes = primes_up_to(s)
    t = int((s + 1) * lam)
    l_val = survivor_count(primes, t)
    coeff = (s + 1) * (Fraction(l_val, 1) - 2 * lam)
    return t, l_val, coeff


def root_window_for_chain(
    root: int,
    mid: int,
    leaf: int,
    h1: int,
    h2: int,
) -> tuple[Fraction, Fraction]:
    left = max(
        Fraction(1, root + 1),
        Fraction(2, h1 * (mid + 1)),
        Fraction(4, h1 * h2 * (leaf + 1)),
    )
    right = min(
        Fraction(1, root),
        Fraction(2, h1 * mid),
        Fraction(4, h1 * h2 * leaf),
    )
    return left, right


def main() -> None:
    intervals = {s: band_intervals(s) for s in range(4, 21)}
    edge_map: dict[int, list[tuple[int, int]]] = {}
    for root, child, h in live_edges(20):
        edge_map.setdefault(root, []).append((child, h))

    print("Counterexamples to the proposed no-triple-overlap lemma:")
    count = 0
    for root in range(4, 21):
        for mid, h1 in edge_map.get(root, []):
            for leaf, h2 in edge_map.get(mid, []):
                overlap = intersect(
                    intersect(intervals[root], intervals[mid]),
                    intervals[leaf],
                )
                if overlap:
                    print(f"  {root}->{mid}->{leaf} via h=({h1},{h2}) on {overlap[0]}")
                    count += 1
    print(f"\nTotal chains up to 20 with triple overlap: {count}")

    lam = Fraction(15, 8)
    print("\nExplicit v24 obstruction:")
    print("  Chain: 13 -> 9 -> 6 via h = 3, 3")
    print("  Triple-overlap interval:", intersect(intersect(intervals[13], intervals[9]), intervals[6]))
    for s in (13, 9, 6):
        t, l_val, coeff = band_coefficient(s, lam)
        print(f"  s={s}: t={t}, L_s(t)={l_val}, c_s(15/8)={coeff}")

    left, right = root_window_for_chain(13, 9, 6, 3, 3)
    print(f"  Root window for w/n: ({left}, {right}]")
    print("  Example with n=1512: w=112, 3w/2=168, 9w/4=252")


if __name__ == "__main__":
    main()
