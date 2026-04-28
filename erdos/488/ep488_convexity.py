"""
EP-488 via convexity: compute max G / (2 min G) in first period [M, M+L).
For small k where L = lcm(A) is manageable.
"""
from math import gcd
from itertools import combinations
import time, sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def compute_lcm(A):
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    return L

def sieve_first_period(A):
    """Compute G in first period [M, M+L) and return max, min, ratio."""
    M = max(A)
    L = compute_lcm(A)

    if L > 50_000_000:
        return None, None, None, None, L

    # Sieve [1, M+L]
    end = M + L
    hit = bytearray(end + 1)
    for a in A:
        for m in range(a, end + 1, a):
            hit[m] = 1

    # Cumulative F
    F_M = 0
    for x in range(1, M + 1):
        F_M += hit[x]

    # Now scan [M, M+L)
    running_F = F_M
    min_g = float('inf')
    max_g = 0.0
    min_x = max_x = M

    # x = M
    g = running_F / M
    min_g = g; max_g = g; min_x = M; max_x = M

    for x in range(M + 1, end + 1):
        running_F += hit[x]
        g = running_F / x
        if g < min_g:
            min_g = g; min_x = x
        if g > max_g:
            max_g = g; max_x = x

    delta = sum(hit[1:L+1]) / L
    ratio = max_g / (2 * min_g) if min_g > 0 else 999
    return min_g, max_g, ratio, delta, L

# ============================================
# Test on growing k
# ============================================
print("EP-488 CONVEXITY FRAMEWORK: FIRST-PERIOD RATIO")
print("=" * 75)

# Coprime sets (primes)
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print("\nA = first k primes:")
print(f"{'k':>3} {'L':>14} {'delta':>8} {'minG':>10} {'maxG':>10} {'ratio':>8} {'pass':>5}")
print("-" * 65)

for k in range(3, 16):
    A = primes[:k]
    L = compute_lcm(A)
    if L > 50_000_000:
        print(f"{k:>3} {L:>14,d}  (L too large)")
        continue
    t0 = time.time()
    mn, mx, ratio, delta, _ = sieve_first_period(A)
    el = time.time() - t0
    if mn is not None:
        ok = "YES" if ratio < 1 else "NO"
        print(f"{k:>3} {L:>14,d} {delta:>8.6f} {mn:>10.6f} {mx:>10.6f} {ratio:>8.6f} {ok:>5} ({el:.1f}s)")
    sys.stdout.flush()

# Scaled sets {2p : p prime}
print("\nA = {2p : p prime, p <= P}:")
print(f"{'k':>3} {'L':>14} {'delta':>8} {'minG':>10} {'maxG':>10} {'ratio':>8} {'pass':>5}")
print("-" * 65)

for P in [7, 11, 13, 17, 19, 23, 29]:
    A = [2*p for p in primes if p <= P]
    k = len(A)
    L = compute_lcm(A)
    if L > 50_000_000:
        print(f"{k:>3} {L:>14,d}  (L too large)")
        continue
    t0 = time.time()
    mn, mx, ratio, delta, _ = sieve_first_period(A)
    el = time.time() - t0
    if mn is not None:
        ok = "YES" if ratio < 1 else "NO"
        print(f"{k:>3} {L:>14,d} {delta:>8.6f} {mn:>10.6f} {mx:>10.6f} {ratio:>8.6f} {ok:>5} ({el:.1f}s)")
    sys.stdout.flush()

# Non-coprime dense sets
print("\nDense non-coprime sets:")
print(f"{'set':>35} {'k':>3} {'L':>10} {'ratio':>8} {'pass':>5}")
print("-" * 65)

dense_sets = [
    [4, 6, 9, 10, 14, 15],
    [6, 10, 14, 15, 21, 22],
    [4, 6, 9, 10, 14, 15, 21, 22],
    [4, 5, 6, 14],
    [3, 4, 5, 7, 11],
    [3, 5, 7, 11, 13],
    [4, 6, 10, 14, 22],
]

for A in dense_sets:
    A = sorted(A)
    if not is_primitive(A):
        continue
    k = len(A)
    L = compute_lcm(A)
    if L > 50_000_000:
        print(f"{str(A):>35} {k:>3} {L:>10,d}  (L too large)")
        continue
    mn, mx, ratio, delta, _ = sieve_first_period(A)
    if mn is not None:
        ok = "YES" if ratio < 1 else "NO"
        print(f"{str(A):>35} {k:>3} {L:>10,d} {ratio:>8.6f} {ok:>5}")
    sys.stdout.flush()

# The consecutive quadruples (tightest cases)
print("\nConsecutive quadruples {a, a+1, a+2, a+3}:")
print(f"{'a':>5} {'L':>12} {'ratio':>10} {'pass':>5}")
print("-" * 40)

for a in [3, 5, 10, 20, 50, 100, 150, 197]:
    A = [a, a+1, a+2, a+3]
    if not is_primitive(A):
        continue
    L = compute_lcm(A)
    if L > 50_000_000:
        print(f"{a:>5} {L:>12,d}  (L too large)")
        continue
    mn, mx, ratio, delta, _ = sieve_first_period(A)
    if mn is not None:
        ok = "YES" if ratio < 1 else "NO"
        print(f"{a:>5} {L:>12,d} {ratio:>10.6f} {ok:>5}")
    sys.stdout.flush()

# ============================================
# KEY QUESTION: where in the period do min/max occur?
# ============================================
print("\n" + "=" * 75)
print("WHERE DO MIN AND MAX OCCUR IN THE FIRST PERIOD?")
print("=" * 75)

for A in [[2,3,5,7,11], [3,5,7,11,13], [4,6,10,14,22]]:
    A = sorted(A)
    if not is_primitive(A):
        continue
    M = max(A)
    L = compute_lcm(A)
    if L > 10_000_000:
        continue

    end = M + L
    hit = bytearray(end + 1)
    for a in A:
        for m in range(a, end + 1, a):
            hit[m] = 1
    F = [0] * (end + 1)
    for x in range(1, end + 1):
        F[x] = F[x-1] + hit[x]

    delta = F[L] / L
    min_g = float('inf'); max_g = 0
    min_x = max_x = M
    for x in range(M, end + 1):
        g = F[x] / x
        if g < min_g: min_g = g; min_x = x
        if g > max_g: max_g = g; max_x = x

    print(f"\n  A={A}, M={M}, L={L}, delta={delta:.6f}")
    print(f"  min G={min_g:.6f} at x={min_x} (offset {min_x-M} = {(min_x-M)/L:.2%} into period)")
    print(f"  max G={max_g:.6f} at x={max_x} (offset {max_x-M} = {(max_x-M)/L:.2%} into period)")
    print(f"  ratio = {max_g/(2*min_g):.6f}")

    # D(r) = F(r) - delta*r analysis
    max_D = -1e18; min_D = 1e18
    for r in range(1, min(L+1, 1000001)):
        Dr = F[r] - delta * r
        if Dr > max_D: max_D = Dr
        if Dr < min_D: min_D = Dr
    print(f"  max D(r) = {max_D:.4f}, min D(r) = {min_D:.4f} (checked r up to {min(L, 1000000)})")

print("\nDONE.")
