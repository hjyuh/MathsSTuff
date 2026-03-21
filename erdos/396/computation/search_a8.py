"""
search_a8.py — Optimized search for a(8) in Erdős Problem #396

a(n) = smallest k such that k(k-1)...(k-n) | C(2k, k)

Key insight: a(n) is monotone (if k works for n+1 terms, it works for n terms),
so a(8) >= a(7) = 101,130,029. We search from there.

CRITICAL OPTIMIZATION: If any of k, k-1, ..., k-8 is a prime p > 16,
then carries(k, p) = 0 but val_p(k-i) = 1, so the check FAILS.
Proof: k-i = p means k = p+i, so k in base p is [1, i]. Doubling gives
[2i] at units and [2] at tens. Since i <= 8 and p > 16, 2i < p and 2 < p,
so no carries. But val_p(k-i) = val_p(p) = 1 > 0. Contradiction.

So we ONLY check k where all of {k, k-1, ..., k-8} are composite.
This is found via sieve (prime gaps of length >= 10).
"""

import sys
import time
import math
from array import array

N = 8  # looking for a(8)

# ========== Core functions ==========

def count_carries(k, p):
    """Count carries when adding k + k in base p = v_p(C(2k,k)) by Kummer."""
    carry = 0
    count = 0
    m = k
    while m > 0 or carry > 0:
        d = m % p
        s = 2 * d + carry
        if s >= p:
            count += 1
            carry = s // p
        else:
            carry = 0
        m = m // p
    return count

def val_p(n, p):
    """p-adic valuation of n."""
    if n == 0:
        return 10**9
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def product_valuation(k, n, p):
    """Sum of v_p(k-i) for i=0..n."""
    return sum(val_p(k - i, p) for i in range(n + 1))

# ========== Factorization ==========

# Small primes for trial division
SMALL_PRIMES = []
def init_small_primes(limit=100000):
    """Sieve primes up to limit for trial division."""
    global SMALL_PRIMES
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = 0
    SMALL_PRIMES = [i for i in range(2, limit + 1) if sieve[i]]

def prime_factors(n):
    """Return set of prime factors of n using trial division."""
    factors = set()
    for p in SMALL_PRIMES:
        if p * p > n:
            break
        if n % p == 0:
            factors.add(p)
            while n % p == 0:
                n //= p
    if n > 1:
        factors.add(n)
    return factors

# ========== Main check ==========

# Primes to check explicitly (small primes that divide multiple terms)
EXPLICIT_PRIMES = [2, 3, 5, 7]

def check_k(k):
    """Check if k(k-1)...(k-8) | C(2k,k). Returns True if divisibility holds."""
    n = N

    # Check small primes first (most likely to fail)
    for p in EXPLICIT_PRIMES:
        pv = product_valuation(k, n, p)
        if pv == 0:
            continue
        carries = count_carries(k, p)
        if pv > carries:
            return False

    # Check medium primes 11..k by finding all prime factors of k-i
    # For primes p > 8: at most one of k,...,k-8 is divisible by p
    # So product_val = val_p(k-j) for the one j where p | k-j

    # Collect all prime factors > 7 from each k-i
    checked = set()
    for i in range(n + 1):
        m = k - i
        if m <= 1:
            continue
        for p in prime_factors(m):
            if p <= 7 or p in checked:
                continue
            checked.add(p)
            # For p > 8 and p > n=8, at most one term divisible
            # But we compute full sum to be safe
            pv = product_valuation(k, n, p)
            if pv == 0:
                continue
            carries = count_carries(k, p)
            if pv > carries:
                return False

    return True

# ========== Segmented sieve for prime-gap filter ==========

def segmented_sieve(low, high, base_primes):
    """Mark composites in [low, high) using base_primes."""
    size = high - low
    is_composite = bytearray(size)
    for p in base_primes:
        # Find first multiple of p >= low
        start = ((low + p - 1) // p) * p
        if start == p:
            start += p  # don't mark p itself
        for j in range(start - low, size, p):
            is_composite[j] = 1
    return is_composite

# ========== Main search ==========

def main():
    print("=== Searching for a(8) ===")
    print(f"Condition: k(k-1)...(k-{N}) | C(2k,k)")
    print()

    init_small_primes(100000)
    print(f"Initialized {len(SMALL_PRIMES)} small primes for trial division")

    # Sieve base primes up to sqrt of search range
    # For search up to 10^12, need primes up to 10^6
    SIEVE_LIMIT = 1000000
    base_sieve = bytearray(b'\x01') * (SIEVE_LIMIT + 1)
    base_sieve[0] = base_sieve[1] = 0
    for i in range(2, int(SIEVE_LIMIT**0.5) + 1):
        if base_sieve[i]:
            for j in range(i*i, SIEVE_LIMIT + 1, i):
                base_sieve[j] = 0
    base_primes = [i for i in range(2, SIEVE_LIMIT + 1) if base_sieve[i]]
    print(f"Initialized {len(base_primes)} base primes for sieve")

    # a(8) >= a(7) = 101130029 (monotonicity: if k works for 9 terms, works for 8)
    START = 101130030
    SEGMENT = 1000000  # sieve segment size

    # Allow command-line override
    if len(sys.argv) > 1:
        START = int(sys.argv[1])

    print(f"Starting search from k = {START}")
    print()

    t0 = time.time()
    total_checked = 0
    candidates_checked = 0

    low = START
    while True:
        high = low + SEGMENT

        # Sieve this segment
        is_composite = segmented_sieve(low, high, base_primes)

        # Also handle primes > SIEVE_LIMIT that fall in range
        # These are primes p where p^2 > high, so p itself might be in range
        # Actually, our sieve with base_primes up to 10^6 catches all composites
        # up to 10^12 (since every composite <= 10^12 has a factor <= 10^6).
        # For numbers in [low, high) that weren't marked, they're prime.

        # Find runs of 9+ consecutive composites
        # A candidate k needs k, k-1, ..., k-8 all composite
        # i.e., positions k-low, k-1-low, ..., k-8-low all marked composite

        # Build a running count of consecutive composites
        consec = 0
        for offset in range(SEGMENT):
            if is_composite[offset]:
                consec += 1
            else:
                consec = 0  # hit a prime, reset

            if consec >= 9:
                # k = low + offset has k, k-1, ..., k-8 all composite
                k = low + offset
                candidates_checked += 1

                if check_k(k):
                    elapsed = time.time() - t0
                    print(f"\n*** FOUND: a({N}) = {k} ***")
                    print(f"Searched {total_checked + offset + 1} values, "
                          f"{candidates_checked} candidates, in {elapsed:.1f}s")

                    # Verify and show details
                    print(f"\nFactorizations of k..k-{N}:")
                    for i in range(N + 1):
                        m = k - i
                        pf = prime_factors(m)
                        print(f"  {m} has prime factors: {sorted(pf)}")

                    print(f"\nSlack at each prime:")
                    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
                        pv = product_valuation(k, N, p)
                        if pv > 0:
                            carries = count_carries(k, p)
                            print(f"  p={p}: carries={carries}, prod_val={pv}, "
                                  f"slack={carries-pv}")

                    # Check large prime factors
                    print(f"\nLarge prime factors:")
                    for i in range(N + 1):
                        m = k - i
                        for p in prime_factors(m):
                            if p > 31:
                                carries = count_carries(k, p)
                                pv = val_p(m, p)
                                print(f"  p={p} | {m}: carries={carries}, "
                                      f"val={pv}, slack={carries-pv}")

                    return k

        total_checked += SEGMENT
        elapsed = time.time() - t0
        rate = total_checked / elapsed if elapsed > 0 else 0
        print(f"Progress: k up to {high}, checked {total_checked} values, "
              f"{candidates_checked} candidates, "
              f"{elapsed:.1f}s, {rate:.0f} k/s",
              flush=True)

        low = high

if __name__ == "__main__":
    main()
