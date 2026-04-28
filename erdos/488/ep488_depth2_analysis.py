"""
EP-488: Depth-2 analysis for the bad-to-bad digraph.

Tests the claim: for every geometric two-step chain r->s->t,
U_r ∩ U_s ∩ U_t = ∅ (no lambda where all three are simultaneously bad).

Also computes the full digraph for j0 = 7, 8 and higher.
"""

from __future__ import annotations
from fractions import Fraction
from itertools import product


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for j in range(p * p, n + 1, p):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]


def survivor_count(primes: list[int], t: int) -> int:
    """Count integers 1..t coprime to all primes in the list."""
    c = 0
    for x in range(1, t + 1):
        if all(x % p != 0 for p in primes):
            c += 1
    return c


def band_kernel(s: int) -> list[int]:
    """Return the kernel (primes up to s) for a frozen band at depth s."""
    return primes_up_to(s)


def band_constant(s: int) -> int:
    """Compute C*(s) with t <= 10(s+1)."""
    primes = band_kernel(s)
    if survivor_count(primes, s) != 1:
        return -1  # not a valid frozen band
    t_max = 10 * (s + 1)
    best = -(10**18)
    for t in range(s + 1, t_max + 1):
        l = survivor_count(primes, t)
        c = (s + 1) * l - 2 * t
        if c > best:
            best = c
    return best


def geometric_edges(max_band: int) -> list[tuple[int, int, int]]:
    """
    Find all geometric edges r -> s via odd multiplier h >= 3.
    Edge r->s means: element in I_r can 2-witness element in I_s.
    Child a_s = (h/2)*a_r, so a_s > a_r (s < r means I_s has larger elements).

    Constraint: 2r/(s+1) < h < 2(r+1)/s, h odd, h >= 3.
    """
    edges = []
    for r in range(4, max_band + 1):
        for s in range(4, r):  # child is at shallower band
            if s == 5:
                continue  # band 5 is dead
            h_low = Fraction(2 * r, s + 1)
            h_high = Fraction(2 * (r + 1), s)
            for h in range(3, int(h_high) + 2, 2):  # odd h >= 3
                if h_low < h < h_high:
                    edges.append((r, s, h))
    return edges


def badness_range(s: int, max_lambda: float = 11.0, steps: int = 1000) -> list[tuple[float, float]]:
    """
    Compute the lambda ranges where band s can be bad.
    Band s bad at quotient tau iff L_K(tau) > 2*lambda.
    tau accessible iff tau in [floor(s*lambda), floor((s+1)*lambda)].

    Returns list of (lambda_min, lambda_max) intervals.
    """
    primes = band_kernel(s)
    if survivor_count(primes, s) != 1:
        return []

    ranges = []
    t_max = 10 * (s + 1)

    for tau in range(s + 1, t_max + 1):
        L = survivor_count(primes, tau)
        if (s + 1) * L <= 2 * tau:
            continue  # C for this tau is <= 0

        # Band s bad at tau: lambda < L/2
        lambda_upper = Fraction(L, 2)

        # tau accessible: s*lambda <= tau <= (s+1)*lambda
        # so tau/(s+1) <= lambda <= tau/s
        lambda_lo = Fraction(tau, s + 1)
        lambda_hi = Fraction(tau, s)

        # Combined: lambda in (lambda_lo, min(lambda_upper, lambda_hi))
        effective_hi = min(lambda_upper, lambda_hi)
        if lambda_lo < effective_hi:
            ranges.append((float(lambda_lo), float(effective_hi)))

    return ranges


def is_bad_at_lambda(s: int, lam: Fraction) -> bool:
    """Check if band s can be bad at the given lambda."""
    primes = band_kernel(s)
    if survivor_count(primes, s) != 1:
        return False

    # Check all accessible tau values
    tau_lo = int(s * lam)
    tau_hi = int((s + 1) * lam) + 1
    t_max = 10 * (s + 1)

    for tau in range(max(s + 1, tau_lo), min(t_max, tau_hi) + 1):
        L = survivor_count(primes, tau)
        if L > 2 * lam:
            return True
    return False


def find_chains(edges: list[tuple[int, int, int]], length: int = 2) -> list[list[tuple[int, int, int]]]:
    """Find all chains of the given length in the edge list."""
    if length == 1:
        return [[e] for e in edges]

    shorter = find_chains(edges, length - 1)
    result = []
    for chain in shorter:
        last_target = chain[-1][1]
        for e in edges:
            if e[0] == last_target:
                result.append(chain + [e])
    return result


def check_chain_live(chain: list[tuple[int, int, int]],
                      lambda_step: Fraction = Fraction(1, 200)) -> list[dict]:
    """
    Check if all bands in a chain can be simultaneously bad at some lambda.
    Returns list of lambda values where all are bad.
    """
    bands = [chain[0][0]] + [e[1] for e in chain]

    live_points = []
    # Scan lambda from 1.0 to 10.0 in small steps
    lam = Fraction(1, 1)
    max_lam = Fraction(10, 1)

    while lam < max_lam:
        all_bad = all(is_bad_at_lambda(s, lam) for s in bands)
        if all_bad:
            live_points.append({
                'lambda': float(lam),
                'bands': bands,
                'chain': [(e[0], e[1], e[2]) for e in chain],
            })
        lam += lambda_step

    return live_points


def main():
    print("=" * 70)
    print("EP-488 DEPTH-2 ANALYSIS")
    print("=" * 70)

    # Compute band constants
    print("\n--- Band Constants ---")
    print(f"{'s':>3} {'C*(s)':>6} {'kernel':>30}")
    cstar = {}
    for s in range(4, 22):
        c = band_constant(s)
        if c >= 0:
            cstar[s] = c
            print(f"{s:3d} {c:6d} {band_kernel(s)}")

    # Compute geometric edges up to band 20
    print("\n--- Geometric Edges (up to band 20) ---")
    edges = geometric_edges(20)
    for r, s, h in sorted(edges):
        if cstar.get(r, -1) >= 0 and cstar.get(s, -1) >= 0:
            print(f"  {r} -> {s}  (h={h})")

    # Filter to live bands only
    live_edges = [(r, s, h) for r, s, h in edges
                   if cstar.get(r, -1) >= 0 and cstar.get(s, -1) >= 0]

    # Find chains of length 2
    print("\n--- Geometric Chains of Length 2 ---")
    chains2 = find_chains(live_edges, 2)
    print(f"Found {len(chains2)} geometric 2-chains")
    for chain in chains2[:30]:
        bands = [chain[0][0]] + [e[1] for e in chain]
        mults = [e[2] for e in chain]
        print(f"  {bands[0]} -h{mults[0]}-> {bands[1]} -h{mults[1]}-> {bands[2]}")
    if len(chains2) > 30:
        print(f"  ... and {len(chains2) - 30} more")

    # TEST CRITICAL CHAINS for liveness
    print("\n--- Testing Key 2-Chains for Liveness ---")
    # Focus on the chains most relevant to j0 = 7
    key_chains = [c for c in chains2
                   if c[0][0] in {13, 14, 15, 16} and c[1][1] in {4, 6, 7, 8}]

    if not key_chains:
        key_chains = chains2[:10]

    for chain in key_chains:
        bands = [chain[0][0]] + [e[1] for e in chain]
        mults = [e[2] for e in chain]
        desc = f"{bands[0]} -h{mults[0]}-> {bands[1]} -h{mults[1]}-> {bands[2]}"

        # Quick scan with coarser step
        live = check_chain_live(chain, Fraction(1, 100))
        if live:
            print(f"\n  *** LIVE CHAIN: {desc}")
            print(f"      Bad at lambda = {live[0]['lambda']:.4f} (and {len(live)} scan points)")
            # Verify with exact arithmetic at a specific point
            lam = Fraction(live[0]['lambda']).limit_denominator(1000)
            print(f"      Verifying at lambda = {lam} = {float(lam):.6f}")
            for s in bands:
                bad = is_bad_at_lambda(s, lam)
                print(f"        Band {s}: {'BAD' if bad else 'GOOD'}")
        else:
            print(f"  DEAD: {desc}")

    # Find chains of length 3
    print("\n--- Geometric Chains of Length 3 ---")
    chains3 = find_chains(live_edges, 3)
    print(f"Found {len(chains3)} geometric 3-chains")

    # Test them
    live3_found = False
    for chain in chains3:
        bands = [chain[0][0]] + [e[1] for e in chain]
        live = check_chain_live(chain, Fraction(1, 50))
        if live:
            mults = [e[2] for e in chain]
            desc = " -> ".join(f"{bands[i]} -h{mults[i]}->" for i in range(len(mults))) + f" {bands[-1]}"
            print(f"\n  *** LIVE 3-CHAIN: {desc}")
            print(f"      Bad at lambda = {live[0]['lambda']:.4f}")
            live3_found = True

    if not live3_found:
        print("  No live 3-chains found (scanning lambda in [1, 10] with step 1/50)")

    # Explicit numerical verification of the 14->9->6 chain
    print("\n--- Explicit Verification: Chain 14 -> 9 -> 6 ---")
    n = 1000
    for m in range(1980, 2000):
        lam = Fraction(m, n)
        # Elements: a_r = 72, a_s = 108, a_t = 162 (ratio 3/2 each)
        a_r, a_s, a_t = 72, 108, 162

        # Check band membership
        in_14 = n / 15 < a_r <= n / 14
        in_9 = n / 10 < a_s <= n / 9
        in_6 = n / 7 < a_t <= n / 6

        if not (in_14 and in_9 and in_6):
            continue

        tau_r = m // a_r
        tau_s = m // a_s
        tau_t = m // a_t

        kernel_r = primes_up_to(14)
        kernel_s = primes_up_to(9)
        kernel_t = primes_up_to(6)

        L_r = survivor_count(kernel_r, tau_r)
        L_s = survivor_count(kernel_s, tau_s)
        L_t = survivor_count(kernel_t, tau_t)

        E_r = n * L_r - 2 * m
        E_s = n * L_s - 2 * m
        E_t = n * L_t - 2 * m

        if E_r > 0 and E_s > 0 and E_t > 0:
            print(f"  n={n}, m={m}, lambda={float(lam):.4f}")
            print(f"    a_r=72 in I_14: tau={tau_r}, L={L_r}, E={E_r}")
            print(f"    a_s=108 in I_9: tau={tau_s}, L={L_s}, E={E_s}")
            print(f"    a_t=162 in I_6: tau={tau_t}, L={L_t}, E={E_t}")
            print(f"    ALL THREE BAD! Chain 14->9->6 is LIVE at lambda={float(lam):.4f}")

    # Also check (68, 102, 153) triple
    print("\n--- Explicit Verification: Elements (68, 102, 153) ---")
    n = 1000
    for m in range(1980, 2000):
        a_r, a_s, a_t = 68, 102, 153

        in_14 = n / 15 < a_r <= n / 14
        in_9 = n / 10 < a_s <= n / 9
        in_6 = n / 7 < a_t <= n / 6

        if not (in_14 and in_9 and in_6):
            continue

        tau_r = m // a_r
        tau_s = m // a_s
        tau_t = m // a_t

        L_r = survivor_count(primes_up_to(14), tau_r)
        L_s = survivor_count(primes_up_to(9), tau_s)
        L_t = survivor_count(primes_up_to(6), tau_t)

        E_r = n * L_r - 2 * m
        E_s = n * L_s - 2 * m
        E_t = n * L_t - 2 * m

        if E_r > 0 and E_s > 0 and E_t > 0:
            print(f"  n={n}, m={m}, lambda={m/n:.4f}")
            print(f"    a_r=68 in I_14: tau={tau_r}, L={L_r}, E={E_r}")
            print(f"    a_s=102 in I_9: tau={tau_s}, L={L_s}, E={E_s}")
            print(f"    a_t=153 in I_6: tau={tau_t}, L={L_t}, E={E_t}")
            print(f"    ALL THREE BAD!")

    print("\n--- Summary ---")
    print("The depth-2 analysis reveals whether the bad-to-bad digraph")
    print("truly has no live 2-step chains, or if the claim needs revision.")


if __name__ == "__main__":
    main()
