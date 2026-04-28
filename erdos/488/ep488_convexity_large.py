"""
For large k where L is too big: compute min/max G near x = M using sieve
up to a large horizon. The convexity guarantees these are the global extrema.
"""
from math import gcd
import time, sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def sieve_minmax(A, horizon):
    """Compute min G and max G for x in [max(A), horizon]."""
    M = max(A)
    hit = bytearray(horizon + 1)
    for a in A:
        for m in range(a, horizon + 1, a):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    # Now at x = M-1, run = F(M-1)

    min_g = float('inf'); max_g = 0
    min_x = max_x = M

    for x in range(M, horizon + 1):
        run += hit[x]
        g = run / x
        if g < min_g: min_g = g; min_x = x
        if g > max_g: max_g = g; max_x = x

    return min_g, max_g, min_x, max_x

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]

# ============================================
# First 21 primes: compute near-M extrema
# ============================================
print("FIRST 21 PRIMES: near-M extrema")
print("=" * 60)

A = PRIMES[:]
M = max(A)  # 73
S1 = sum(1.0/p for p in A)
delta = 1.0
for p in A:
    delta *= (1 - 1.0/p)
delta = 1 - delta

print(f"A = first 21 primes up to 73")
print(f"|A| = {len(A)}, M = {M}, delta = {delta:.8f}, S1 = {S1:.6f}")
print(f"2*delta = {2*delta:.6f}, S1 = {S1:.6f}, 2d > S1: {2*delta > S1}")

# Sieve up to increasing horizons
for h in [1000, 10000, 100000, 1000000, 10000000]:
    t0 = time.time()
    mn, mx, mn_x, mx_x = sieve_minmax(A, h)
    el = time.time() - t0
    ratio = mx / (2*mn) if mn > 0 else 999
    print(f"  horizon={h:>10,d}: minG={mn:.8f} at x={mn_x:>10,d}, "
          f"maxG={mx:.8f} at x={mx_x:>10,d}, ratio={ratio:.6f} ({el:.1f}s)")
    sys.stdout.flush()

# ============================================
# Scaled set {2p : p <= 73}
# ============================================
print(f"\nSCALED SET {{2p : p prime, p <= 73}}")
print("=" * 60)

A2 = [2*p for p in PRIMES]
M2 = max(A2)  # 146
S1_2 = sum(1.0/a for a in A2)

print(f"|A| = {len(A2)}, M = {M2}, S1 = {S1_2:.6f}")

for h in [1000, 10000, 100000, 1000000]:
    t0 = time.time()
    mn, mx, mn_x, mx_x = sieve_minmax(A2, h)
    el = time.time() - t0
    ratio = mx / (2*mn) if mn > 0 else 999
    print(f"  horizon={h:>10,d}: minG={mn:.8f} at x={mn_x:>10,d}, "
          f"maxG={mx:.8f} at x={mx_x:>10,d}, ratio={ratio:.6f} ({el:.1f}s)")
    sys.stdout.flush()

# ============================================
# Key analysis: does the ratio STABILIZE as horizon grows?
# ============================================
print(f"\nSTABILITY ANALYSIS: does ratio converge?")
print("=" * 60)
print("If max G and min G are achieved near x = M, the ratio should stabilize")
print("quickly as horizon grows, confirming the first-period reduction.")

# For k=9 (first 9 primes): L = 223M, can't enumerate
# But sieve up to 10M should find the true min/max
A9 = PRIMES[:9]
M9 = max(A9)
print(f"\nA = first 9 primes: {A9}, M = {M9}")
for h in [1000, 5000, 10000, 50000, 100000, 500000, 1000000]:
    mn, mx, mn_x, mx_x = sieve_minmax(A9, h)
    ratio = mx / (2*mn) if mn > 0 else 999
    print(f"  h={h:>10,d}: ratio={ratio:.8f}, minG at {mn_x}, maxG at {mx_x}")

# For k=10
A10 = PRIMES[:10]
M10 = max(A10)
print(f"\nA = first 10 primes: {A10}, M = {M10}")
for h in [1000, 10000, 100000, 1000000]:
    mn, mx, mn_x, mx_x = sieve_minmax(A10, h)
    ratio = mx / (2*mn) if mn > 0 else 999
    print(f"  h={h:>10,d}: ratio={ratio:.8f}, minG at {mn_x}, maxG at {mx_x}")

# For k=15
A15 = PRIMES[:15]
M15 = max(A15)
print(f"\nA = first 15 primes: {A15}, M = {M15}")
for h in [1000, 10000, 100000, 1000000, 5000000]:
    t0 = time.time()
    mn, mx, mn_x, mx_x = sieve_minmax(A15, h)
    ratio = mx / (2*mn) if mn > 0 else 999
    el = time.time() - t0
    print(f"  h={h:>10,d}: ratio={ratio:.8f}, minG at {mn_x}, maxG at {mx_x} ({el:.1f}s)")
    sys.stdout.flush()

# Consecutive quadruples with large a (tightest known cases)
print(f"\nConsecutive quads (tightest):")
for a in [100, 200, 500, 1000]:
    A = [a, a+1, a+2, a+3]
    from math import prod
    if not all(gcd(A[i],A[j])==1 or True for i in range(4) for j in range(i+1,4)):
        pass
    M = max(A)
    h = max(100000, 30*M)
    mn, mx, mn_x, mx_x = sieve_minmax(A, h)
    ratio = mx / (2*mn) if mn > 0 else 999
    print(f"  a={a}: ratio={ratio:.6f}, minG={mn:.8f} at {mn_x}, maxG={mx:.8f} at {mx_x}")
    sys.stdout.flush()

print("\nDONE.")
