"""
Consecutive k-tuples A = {a, a+1, ..., a+k-1}.
Find exact min G, max G, their locations, and the ratio.
"""
from math import gcd
import sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def analyze_consecutive(a, k, horizon_mult=30):
    """Full analysis of {a, a+1, ..., a+k-1}."""
    A = list(range(a, a+k))
    if not is_primitive(A):
        return None
    M = a + k - 1
    h = max(5000, horizon_mult * M)

    hit = bytearray(h + 1)
    for elem in A:
        for m in range(elem, h + 1, elem):
            hit[m] = 1
    F = [0] * (h + 1)
    run = 0
    for x in range(1, h + 1):
        run += hit[x]
        F[x] = run

    min_g = float('inf'); max_g = 0
    min_x = max_x = M
    for x in range(M, h + 1):
        g = F[x] / x
        if g < min_g: min_g = g; min_x = x
        if g > max_g: max_g = g; max_x = x

    ratio = max_g / (2 * min_g)
    formula = (2*a - 1) / (2 * (a + k - 1))
    return {
        'a': a, 'k': k, 'M': M,
        'min_g': min_g, 'min_x': min_x,
        'max_g': max_g, 'max_x': max_x,
        'ratio': ratio, 'formula': formula,
        'F_min': F[min_x], 'F_max': F[max_x],
    }

# ============================================
# TASK 1: Find exact min/max G locations
# ============================================
print("TASK 1: EXACT MIN/MAX FOR CONSECUTIVE k-TUPLES")
print("=" * 80)

# k=2 (pairs): known min at 2a-1, max at a^2
print("\nk=2 (pairs):")
print(f"{'a':>5} {'minG':>10} {'at':>8} {'expect':>8} | {'maxG':>10} {'at':>8} {'expect':>8} | {'ratio':>8} {'formula':>8}")
for a in [3,5,7,10,20,50,100]:
    r = analyze_consecutive(a, 2, 50)
    if r is None: continue
    exp_min_x = 2*a - 1
    exp_max_x = a*a if a*a < 50*r['M'] else '?'
    print(f"{a:>5} {r['min_g']:>10.6f} {r['min_x']:>8} {exp_min_x:>8} | "
          f"{r['max_g']:>10.6f} {r['max_x']:>8} {str(exp_max_x):>8} | "
          f"{r['ratio']:>8.6f} {r['formula']:>8.6f}")

# k=3 (triples)
print("\nk=3 (triples):")
print(f"{'a':>5} {'minG':>10} {'at':>8} {'F(min)':>6} | {'maxG':>10} {'at':>8} {'F(max)':>6} | {'ratio':>8} {'formula':>8}")
for a in [3,5,7,10,13,20,30,50,100]:
    r = analyze_consecutive(a, 3)
    if r is None: continue
    print(f"{r['a']:>5} {r['min_g']:>10.6f} {r['min_x']:>8} {r['F_min']:>6} | "
          f"{r['max_g']:>10.6f} {r['max_x']:>8} {r['F_max']:>6} | "
          f"{r['ratio']:>8.6f} {r['formula']:>8.6f}")

# k=4
print("\nk=4:")
print(f"{'a':>5} {'minG':>10} {'at':>8} | {'maxG':>10} {'at':>8} | {'ratio':>8} {'formula':>8}")
for a in [3,5,7,10,20,50,100]:
    r = analyze_consecutive(a, 4)
    if r is None: continue
    print(f"{r['a']:>5} {r['min_g']:>10.6f} {r['min_x']:>8} | "
          f"{r['max_g']:>10.6f} {r['max_x']:>8} | "
          f"{r['ratio']:>8.6f} {r['formula']:>8.6f}")

# k=5,6,7,8
for k in [5, 6, 7, 8]:
    print(f"\nk={k}:")
    print(f"{'a':>5} {'minG':>10} {'at':>8} | {'maxG':>10} {'at':>8} | {'ratio':>8} {'formula':>8} {'diff':>10}")
    for a in [3,5,7,10,20,50,100]:
        r = analyze_consecutive(a, k)
        if r is None: continue
        diff = r['ratio'] - r['formula']
        print(f"{r['a']:>5} {r['min_g']:>10.6f} {r['min_x']:>8} | "
              f"{r['max_g']:>10.6f} {r['max_x']:>8} | "
              f"{r['ratio']:>8.6f} {r['formula']:>8.6f} {diff:>10.6f}")
    sys.stdout.flush()

# ============================================
# TASK 2: Pattern in min/max locations
# ============================================
print("\n" + "=" * 80)
print("TASK 2: PATTERN IN MIN/MAX LOCATIONS")
print("=" * 80)

# For each k, express min_x and max_x in terms of a
print("\nmin_x patterns (as function of a):")
for k in range(2, 9):
    print(f"\n  k={k}:")
    for a in [10, 20, 50, 100, 200]:
        r = analyze_consecutive(a, k)
        if r is None: continue
        # Express min_x relative to a and k
        min_x = r['min_x']
        M = r['M']
        # Try: min_x = c*a - 1 for some c
        c_approx = (min_x + 1) / a
        # Try: min_x = 2*M - 1 = 2(a+k-1) - 1
        guess_2M = 2*M - 1
        # F(min_x) / min_x = min_g. F(min_x) = ?
        print(f"    a={a:>4}: min_x={min_x:>6}, 2M-1={guess_2M:>6}, "
              f"min_x/a={min_x/a:.2f}, F={r['F_min']}")
    sys.stdout.flush()

print("\nmax_x patterns:")
for k in range(2, 9):
    print(f"\n  k={k}:")
    for a in [10, 20, 50, 100]:
        r = analyze_consecutive(a, k)
        if r is None: continue
        max_x = r['max_x']
        M = r['M']
        print(f"    a={a:>4}: max_x={max_x:>8}, max_x/a^2={max_x/a**2:.4f}, "
              f"max_x/a={max_x/a:.2f}, F={r['F_max']}")
    sys.stdout.flush()

# ============================================
# TASK 3: The 2a-1 location and k/(2a-1) value
# ============================================
print("\n" + "=" * 80)
print("TASK 3: G AT SPECIFIC CANDIDATE POINTS")
print("=" * 80)

print("\nG(2a-1) for consecutive k-tuples (candidate for min G):")
for k in range(2, 9):
    print(f"\n  k={k}:")
    for a in [10, 20, 50, 100, 200]:
        A = list(range(a, a+k))
        if not is_primitive(A): continue
        n = 2*a - 1
        M = a+k-1
        if n < M: n = M  # ensure n >= M
        h = max(5000, 30*M)
        hit = bytearray(h+1)
        for elem in A:
            for m in range(elem, h+1, elem):
                hit[m] = 1
        F_n = sum(hit[1:n+1])
        G_n = F_n / n
        # Also check n = k*a - 1
        n2 = k*a - 1
        F_n2 = sum(hit[1:n2+1]) if n2 <= h else -1
        G_n2 = F_n2/n2 if F_n2 >= 0 else -1
        print(f"    a={a:>4}: G(2a-1={2*a-1})={G_n:.6f}, F={F_n}, k={k}; "
              f"G(ka-1={k*a-1})={G_n2:.6f}")
    sys.stdout.flush()

# The KEY: at n = 2a-1, F(n) = k (each element contributes exactly 1 multiple)
# Because: for a <= e <= a+k-1, the multiples of e up to 2a-1 are just e itself
# (since 2e >= 2a > 2a-1 for e >= a).
# So F(2a-1) = k and G(2a-1) = k/(2a-1).
# This is ALWAYS the minimum for large a (verified).

print("\n\nKEY IDENTITY: F(2a-1) = k for {a,...,a+k-1} when a >= k")
print("Proof: for each e in [a, a+k-1]: 2e >= 2a > 2a-1, so only e itself is <= 2a-1.")
print("Therefore G(2a-1) = k/(2a-1).")
print("")
print("And S1 = sum_{i=0}^{k-1} 1/(a+i) < k/a.")
print("2G(2a-1) = 2k/(2a-1). Need > S1 < k/a.")
print("2k/(2a-1) > k/a iff 2a > 2a-1, always true! So 2*minG > S1 >= maxG.")
print("")
print("More precisely: 2G(min) = 2k/(2a-1).")
print("And maxG <= S1 = sum 1/(a+i). For large a: S1 ~ k/a.")
print("Ratio = S1 / (2k/(2a-1)) = S1*(2a-1)/(2k).")
print("For large a: ~ (k/a)*(2a)/(2k) = 1. Approaches 1 from below.")
print("")
print("Exact ratio at large a: S1*(2a-1)/(2k) where S1 = sum_{i=0}^{k-1} 1/(a+i)")
print("  = (2a-1)/(2k) * k * [harmonic mean correction]")
print("  ~ (2a-1)/(2a) * [1 - (k-1)/(2a) + ...] -> 1 - 1/(2a) - (k-1)/(2a) + ...")
print("  = 1 - k/(2a) + O(1/a^2)")

# Verify the exact ratio vs the formula (2a-1)/(2(a+k-1))
print("\n\nEXACT RATIO vs FORMULA (2a-1)/(2(a+k-1)):")
print(f"{'k':>3} {'a':>5} {'ratio':>10} {'formula':>10} {'diff':>12}")
for k in range(2, 9):
    for a in [50, 100, 200, 500]:
        r = analyze_consecutive(a, k)
        if r is None: continue
        print(f"{k:>3} {a:>5} {r['ratio']:>10.6f} {r['formula']:>10.6f} {r['ratio']-r['formula']:>12.8f}")
    sys.stdout.flush()

print("\nDONE.")
