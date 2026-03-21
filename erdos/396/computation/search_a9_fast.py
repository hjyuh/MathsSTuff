"""
search_a9_fast.py — Search for a(9) in Erdos Problem #396

a(9) >= a(8) = 339,949,252 by monotonicity.
Need k(k-1)...(k-9) | C(2k,k), i.e. 10 consecutive terms.

Uses sqrt(2K) smoothness filter + numba JIT.
"""

import sys
import time
import math
import numpy as np
from numba import njit

N = 9  # looking for a(9)

# ========== Numba-JIT'd core functions ==========

@njit(cache=True)
def count_carries(k, p):
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
    if n == 0:
        return 1000000
    v = 0
    while n % p == 0:
        v += 1
        n = n // p
    return v

@njit(cache=True)
def check_small_primes(k, n):
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
def full_check(k, n):
    if not check_small_primes(k, n):
        return False

    checked_primes = np.zeros(200, dtype=np.int64)
    n_checked = 0

    for i in range(n + 1):
        m = k - i
        if m <= 1:
            continue

        remainder = m
        for sp in [2, 3, 5, 7]:
            while remainder % sp == 0:
                remainder = remainder // sp

        p = 11
        while p * p <= remainder:
            if remainder % p == 0:
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
                    if n_checked < 200:
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
                if n_checked < 200:
                    checked_primes[n_checked] = p
                    n_checked += 1

    return True

# ========== Smoothness sieve ==========

def sieve_primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = 0
    return [i for i in range(2, limit + 1) if sieve[i]]

def find_smooth_windows(low, high, B, window_size):
    size = high - low
    remainders = np.arange(low, high, dtype=np.int64)

    primes = sieve_primes(B)
    for p in primes:
        start = ((low + p - 1) // p) * p
        for j in range(start - low, size, p):
            while remainders[j] % p == 0:
                remainders[j] //= p

    is_smooth = (remainders == 1)
    if low == 0:
        is_smooth[0] = True
        if size > 1:
            is_smooth[1] = True

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
    print(f"=== Searching for a({N}) ===")
    print(f"Using sqrt(2K) smoothness bound")
    print(f"Condition: k(k-1)...(k-{N}) | C(2k,k)")
    print(f"Window size: {N+1} consecutive smooth numbers needed")
    print()

    # Warm up JIT
    print("Warming up JIT...", end=" ", flush=True)
    _ = full_check(339949252, 8)
    _ = full_check(101130029, 7)
    print("done")

    # a(9) >= a(8) = 339949252
    START = 339949253
    SEGMENT = 2000000

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
        B = int(math.sqrt(2.0 * high)) + 1

        candidates = find_smooth_windows(low, high, B, window_size=N+1)
        total_candidates += len(candidates)

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
                    f = factorint(m)
                    maxp = max(f.keys()) if f else 0
                    print(f"  {m} = {f}  (max pf: {maxp})")

                print(f"\nsqrt(2K) = {int(math.sqrt(2.0*k))+1}")

                print(f"\nSlack at each prime:")
                all_primes = set()
                for i in range(N + 1):
                    m = k - i
                    if m > 1:
                        for p in factorint(m):
                            all_primes.add(p)
                for p in sorted(all_primes):
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
