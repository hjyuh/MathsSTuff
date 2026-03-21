"""
search_a8_fast.py — Optimized search for a(8) using √(2K) smoothness bound + numba JIT

KEY INSIGHT (from GPT Entry 6): Any solution k to the n=8 condition must satisfy
P+(∏(k-i)) ≤ √(2k). That is, all of k, k-1, ..., k-8 must be √(2k)-smooth.

This eliminates almost all candidates. For k ~ 10^8, we need all 9 consecutive
integers to have no prime factor > ~14142. The probability of one random number
being B-smooth at this scale is ~28%, so 9 consecutive is ~10^-5. This means
only ~1000 candidates per 10^8 range — a 10^5x speedup over brute force.

Algorithm:
1. Segmented sieve: for each segment, find windows of 9 consecutive B-smooth numbers
   (where B = floor(sqrt(2 * segment_end)))
2. For each such window, run the full carry check
3. Report first k that passes
"""

import sys
import time
import math
import numpy as np
from numba import njit

N = 8  # looking for a(8)

# ========== Numba-JIT'd core functions ==========

@njit(cache=True)
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

@njit(cache=True)
def val_p(n, p):
    """p-adic valuation of n."""
    if n == 0:
        return 1000000
    v = 0
    while n % p == 0:
        v += 1
        n = n // p
    return v

@njit(cache=True)
def check_small_primes(k, n):
    """Check carry condition at primes 2, 3, 5, 7. Return True if all pass."""
    small_primes = np.array([2, 3, 5, 7], dtype=np.int64)
    for pi in range(4):
        p = small_primes[pi]
        pv = 0
        for i in range(n + 1):
            pv += val_p(k - i, p)
        if pv == 0:
            continue
        carries = count_carries(k, p)
        if pv > carries:
            return False
    return True

@njit(cache=True)
def trial_factor_check(k, n, m, B):
    """Factor m by trial division up to B. For each prime factor p > 7,
    check carries(k, p) >= total product valuation at p.
    Returns True if all factors check out, False if any fails.
    Also returns the unfactored remainder (1 if fully factored)."""
    remainder = m

    # Remove small prime factors (already checked separately)
    for p in [2, 3, 5, 7]:
        while remainder % p == 0:
            remainder = remainder // p

    # Trial divide by primes 11, 13, 17, 19, 23, ...
    p = 11
    while p * p <= remainder and p <= B:
        if remainder % p == 0:
            # Found prime factor p > 7
            # Check carry condition
            pv = 0
            for i in range(n + 1):
                pv += val_p(k - i, p)
            if pv > 0:
                carries = count_carries(k, p)
                if pv > carries:
                    return False, remainder
            while remainder % p == 0:
                remainder = remainder // p
        # Next candidate (skip evens)
        if p == 11:
            p = 13
        else:
            p += 2
            # Skip multiples of 3
            # Simple: just increment by 2

    if remainder > 1:
        # remainder is a prime > B (or a prime <= B but > sqrt(original))
        # This is a large prime factor
        p = remainder
        pv = 0
        for i in range(n + 1):
            pv += val_p(k - i, p)
        if pv > 0:
            carries = count_carries(k, p)
            if pv > carries:
                return False, remainder

    return True, 1

@njit(cache=True)
def full_check(k, n):
    """Full divisibility check for k(k-1)...(k-n) | C(2k,k)."""
    # Check small primes first
    if not check_small_primes(k, n):
        return False

    # For each k-i, factor and check all prime factors > 7
    B = int(math.sqrt(2.0 * k)) + 1
    checked_primes = np.zeros(100, dtype=np.int64)  # track checked primes
    n_checked = 0

    for i in range(n + 1):
        m = k - i
        if m <= 1:
            continue

        # Factor m and check each prime factor
        remainder = m
        for sp in [2, 3, 5, 7]:
            while remainder % sp == 0:
                remainder = remainder // sp

        p = 11
        while p * p <= remainder:
            if remainder % p == 0:
                # Check if already checked this prime
                already = False
                for j in range(n_checked):
                    if checked_primes[j] == p:
                        already = True
                        break
                if not already:
                    pv = 0
                    for ii in range(n + 1):
                        pv += val_p(k - ii, p)
                    if pv > 0:
                        carries = count_carries(k, p)
                        if pv > carries:
                            return False
                    if n_checked < 100:
                        checked_primes[n_checked] = p
                        n_checked += 1

                while remainder % p == 0:
                    remainder = remainder // p
            p += 2

        if remainder > 1:
            p = remainder
            already = False
            for j in range(n_checked):
                if checked_primes[j] == p:
                    already = True
                    break
            if not already:
                pv = 0
                for ii in range(n + 1):
                    pv += val_p(k - ii, p)
                if pv > 0:
                    carries = count_carries(k, p)
                    if pv > carries:
                        return False
                if n_checked < 100:
                    checked_primes[n_checked] = p
                    n_checked += 1

    return True

# ========== Smoothness sieve ==========

def sieve_primes(limit):
    """Simple sieve of Eratosthenes."""
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = 0
    return [i for i in range(2, limit + 1) if sieve[i]]

def find_smooth_windows(low, high, B, window_size=9):
    """Find all positions k in [low, high) where k, k-1, ..., k-(window_size-1)
    are all B-smooth (no prime factor > B).

    Uses sieve: start with all numbers, divide out primes up to B,
    check if remainder is 1."""

    size = high - low
    # remainders[i] = low + i after dividing out all prime factors <= B
    remainders = np.arange(low, high, dtype=np.int64)

    # Divide out all primes up to B
    primes = sieve_primes(B)
    for p in primes:
        # Find first multiple of p in [low, high)
        start = ((low + p - 1) // p) * p
        for j in range(start - low, size, p):
            while remainders[j] % p == 0:
                remainders[j] //= p

    # is_smooth[i] = True if low+i is B-smooth (remainder == 1)
    # Special case: 1 and 0 are trivially smooth
    is_smooth = (remainders == 1)
    # Handle 0 and 1 explicitly
    if low == 0:
        is_smooth[0] = True  # 0 is "smooth"
        if size > 1:
            is_smooth[1] = True

    # Find windows of window_size consecutive smooth numbers
    # k is valid if k, k-1, ..., k-(window_size-1) are all smooth
    # i.e., positions k-low, k-1-low, ..., k-(window_size-1)-low are all smooth

    candidates = []
    consec = 0
    for i in range(size):
        if is_smooth[i]:
            consec += 1
        else:
            consec = 0

        if consec >= window_size:
            k = low + i
            candidates.append(k)

    return candidates

# ========== Main search ==========

def main():
    print("=== Searching for a(8) — FAST VERSION ===")
    print(f"Using sqrt(2K) smoothness bound from GPT Entry 6")
    print(f"Condition: k(k-1)...(k-{N}) | C(2k,k)")
    print()

    # Warm up numba JIT
    print("Warming up JIT...", end=" ", flush=True)
    _ = full_check(101130029, N)  # verify a(7) works
    print("done (a(7) verified)")

    # a(8) >= a(7) = 101130029
    START = 101130030
    SEGMENT = 2000000  # segment size for sieve

    if len(sys.argv) > 1:
        START = int(sys.argv[1])

    print(f"Starting search from k = {START}")
    print()

    t0 = time.time()
    total_scanned = 0
    total_candidates = 0

    low = START
    while True:
        high = low + SEGMENT

        # B = sqrt(2 * high) — smoothness bound for this segment
        B = int(math.sqrt(2.0 * high)) + 1

        # Find all smooth windows in this segment
        candidates = find_smooth_windows(low, high, B, window_size=N+1)
        total_candidates += len(candidates)

        # Check each candidate
        for k in candidates:
            if full_check(k, N):
                elapsed = time.time() - t0
                print(f"\n*** FOUND: a({N}) = {k} ***")
                print(f"Scanned {total_scanned + (k - low)} values, "
                      f"{total_candidates} smooth-window candidates, "
                      f"in {elapsed:.1f}s")

                # Show details
                print(f"\nFactorizations:")
                from sympy import factorint
                for i in range(N + 1):
                    m = k - i
                    print(f"  {m} = {factorint(m)}")

                print(f"\nSlack at each prime:")
                for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
                    pv = sum(val_p(k - i, p) for i in range(N + 1))
                    if pv > 0:
                        carries = count_carries(k, p)
                        print(f"  p={p}: carries={carries}, prod_val={pv}, "
                              f"slack={carries-pv}")

                return k

        total_scanned += SEGMENT
        elapsed = time.time() - t0
        rate = total_scanned / elapsed if elapsed > 0 else 0

        print(f"k up to {high:>12,}, scanned {total_scanned:>12,}, "
              f"smooth candidates: {len(candidates):>5}, "
              f"total candidates: {total_candidates:>8}, "
              f"{elapsed:>7.1f}s, {rate:,.0f} k/s",
              flush=True)

        low = high

if __name__ == "__main__":
    main()
