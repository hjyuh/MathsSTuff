"""
Four tasks for tightening the EP-488 bound:
1. max G / S1 for spread sets (is S1 a loose bound?)
2. Where does max G actually occur? Formula?
3. Uniform bound: ratio <= 1 - 1/max(A)?
4. Fixed min, max: extremal arrangement
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

def analyze(A, mult=25):
    M = max(A); a = min(A); k = len(A)
    h_abs = max(5000, mult * M)
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    mn = float('inf'); mx = 0
    min_x = max_x = M
    for x in range(M, h_abs + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g; min_x = x
        if g > mx: mx = g; max_x = x
    S1 = sum(1.0/e for e in A)
    # Delta via sieve (long-term)
    delta = run / h_abs  # approximation
    return {
        'k': k, 'a': a, 'M': M, 'S1': S1,
        'min': mn, 'min_x': min_x,
        'max': mx, 'max_x': max_x,
        'ratio': mx/(2*mn) if mn > 0 else 999,
        'delta': delta,
    }

# ============================================
# TASK 1: max G / S1 for spread sets
# ============================================
print("TASK 1: max G / S1 for SPREAD primitive sets (max > 2*min)")
print("=" * 70)

max_ratio_to_S1 = 0
min_ratio_to_S1 = 1.0
stats_by_spread = {}  # spread_bucket -> list of max_G/S1

count = 0
for a1 in range(3, 12):
    for tk in range(3, 9):
        pool = [x for x in range(a1+1, 51) if x % a1 != 0][:18]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            M = max(A)
            if M <= 2*a1: continue  # not spread
            count += 1
            r = analyze(A, mult=15)
            ratio_mxS1 = r['max'] / r['S1'] if r['S1'] > 0 else 0
            if ratio_mxS1 > max_ratio_to_S1:
                max_ratio_to_S1 = ratio_mxS1
                max_set = tuple(A)
            if ratio_mxS1 < min_ratio_to_S1:
                min_ratio_to_S1 = ratio_mxS1
                min_set = tuple(A)
            # Bucket by M/a
            spread = M / a1
            bucket = int(spread)
            if bucket not in stats_by_spread:
                stats_by_spread[bucket] = []
            stats_by_spread[bucket].append(ratio_mxS1)

print(f"  Checked {count} spread sets")
print(f"  max(max G / S1) = {max_ratio_to_S1:.6f} at {max_set}")
print(f"  min(max G / S1) = {min_ratio_to_S1:.6f} at {min_set}")
print()
print(f"  By spread ratio M/a:")
for b in sorted(stats_by_spread):
    vals = stats_by_spread[b]
    print(f"    M/a ~ {b}: count={len(vals)}, avg max_G/S1={sum(vals)/len(vals):.4f}, "
          f"max={max(vals):.4f}, min={min(vals):.4f}")
sys.stdout.flush()

# ============================================
# TASK 2: Where does max G occur? Formula?
# ============================================
print("\n" + "=" * 70)
print("TASK 2: Location of max G for primitive sets")
print("=" * 70)

# For each set, record (max_x, M, k, a)
# Check: is max_x = M + 1? M + 2? Near M*a? Some formula?
print("\nMax G locations for selected sets:")
print(f"{'set':<35} {'a':>3} {'M':>4} {'max_x':>8} {'max_x/M':>8} {'max_x-M':>8} {'F(max_x)':>10}")

test = [
    [2, 3, 5, 7],
    [3, 5, 7, 11],
    [5, 7, 11, 13],
    [3, 5, 7, 11, 13],
    [4, 6, 10, 14],
    [4, 6, 9, 10],
    [5, 6, 7, 8],
    [10, 11, 12, 13],
    [3, 4, 5, 7],
    [9, 22, 23, 25, 26, 28, 29],
    [5, 8, 9, 11],
    [7, 10, 11, 12],
]
for A in test:
    A = sorted(A)
    if not is_primitive(A): continue
    r = analyze(A, mult=30)
    # F(max_x)
    M = r['M']
    h = max(5000, 30*M)
    hit = bytearray(h+1)
    for e in A:
        for m in range(e, h+1, e):
            hit[m] = 1
    F_max = sum(hit[1:r['max_x']+1])
    print(f"{str(A):<35} {r['a']:>3} {M:>4} {r['max_x']:>8} "
          f"{r['max_x']/M:>8.2f} {r['max_x']-M:>8} {F_max:>10}")
sys.stdout.flush()

# Check: is max G always at x = ceil((2a-1)·M/(2a)) or some similar formula?
# For pairs {a,b}: max G at x = a^2 (if a < b = a+1).
# For k=3 consecutive {a,a+1,a+2}: max at ?
# Try: is max G at F(x)/x maximized when F(x) = k · ceil(x/a) or similar?

# Pattern from data: for many sets, max_x is slightly > M (e.g., M+1, M+2)
# These are "small local max" points. The GLOBAL max might be at a later x.

# ============================================
# TASK 3: Uniform bound ratio <= 1 - 1/max(A)?
# ============================================
print("\n" + "=" * 70)
print("TASK 3: Is ratio <= 1 - 1/max(A) always?")
print("=" * 70)

# Also check 1 - c/max(A) for various c
worst_margin = 1e9  # inf = bound always works
worst_margin_set = None
worst_ratio = 0
worst_ratio_set = None

for a1 in range(3, 20):
    for tk in range(4, 9):
        pool = [x for x in range(a1+1, 60) if x % a1 != 0][:18]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            M = max(A)
            r = analyze(A, mult=15)
            ratio_val = r['ratio']
            if ratio_val > worst_ratio:
                worst_ratio = ratio_val
                worst_ratio_set = tuple(A)
            # Check: ratio <= 1 - 1/M?
            bound = 1 - 1/M
            margin = bound - ratio_val
            if margin < worst_margin:
                worst_margin = margin
                worst_margin_set = (tuple(A), ratio_val, bound)

# Also check consecutive with large a
for a in [50, 100, 200, 500, 1000]:
    for k in [2, 3, 4, 5]:
        A = list(range(a, a+k))
        if not is_primitive(A): continue
        r = analyze(A, mult=15)
        M = a+k-1
        ratio_val = r['ratio']
        if ratio_val > worst_ratio:
            worst_ratio = ratio_val
            worst_ratio_set = tuple(A)
        bound = 1 - 1/M
        margin = bound - ratio_val
        if margin < worst_margin:
            worst_margin = margin
            worst_margin_set = (tuple(A), ratio_val, bound)

print(f"  Worst overall ratio: {worst_ratio:.6f} at {worst_ratio_set}")
print(f"  Tightest (ratio, 1-1/M): ratio={worst_margin_set[1]:.6f}, "
      f"1-1/M={worst_margin_set[2]:.6f}, margin={worst_margin:.6f}")
print(f"  Set: {worst_margin_set[0]}")
print(f"  Bound ratio <= 1 - 1/M: {'HOLDS' if worst_margin >= 0 else 'FAILS'}")

# Try tighter: 1 - c/M for various c. What's the smallest c that always works?
# We need c such that ratio <= 1 - c/M for all A.
# c_max = min over all A of (1 - ratio) * M
print("\n  Computing max allowed c: c_max = min over A of (1-ratio)*M")
min_c = float('inf')
min_c_set = None
for a1 in range(3, 15):
    for tk in range(4, 8):
        pool = [x for x in range(a1+1, 50) if x % a1 != 0][:18]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            M = max(A)
            r = analyze(A, mult=15)
            c = (1 - r['ratio']) * M
            if c < min_c:
                min_c = c
                min_c_set = tuple(A)

# And consecutive at large a
for a in [100, 500, 1000]:
    for k in [2,3,4,5]:
        A = list(range(a, a+k))
        if not is_primitive(A): continue
        r = analyze(A, mult=15)
        M = a+k-1
        c = (1 - r['ratio']) * M
        if c < min_c:
            min_c = c
            min_c_set = tuple(A)

print(f"  Min c = {min_c:.4f} at {min_c_set}")
print(f"  This means: ratio <= 1 - {min_c:.3f}/M fails for some sets")
print(f"  The uniform bound becomes tighter as M grows")

# ============================================
# TASK 4: Fixed (a, M), extremal arrangement
# ============================================
print("\n" + "=" * 70)
print("TASK 4: Fixed a=5, M=20, find ratio-maximizing arrangement")
print("=" * 70)

a = 5
M_target = 20
print(f"\nPrimitive sets with min={a}, max={M_target}:")
for k in [3, 4, 5, 6]:
    candidates = []
    # Middle elements from {6, 7, ..., 19} not divisible by 5, not divisible by... etc
    middle = [x for x in range(a+1, M_target) if x % a != 0 and M_target % x != 0]
    for sub in combinations(middle, k-2):
        A = [a] + list(sub) + [M_target]
        if not is_primitive(A): continue
        r = analyze(A, mult=20)
        candidates.append((r['ratio'], tuple(A)))
    candidates.sort(reverse=True)
    print(f"\n  k={k}: {len(candidates)} sets")
    print(f"    {'ratio':<10} {'set'}")
    for rv, A in candidates[:5]:
        print(f"    {rv:.6f}  {list(A)}")
    if candidates:
        print(f"    ...")
        for rv, A in candidates[-3:]:
            print(f"    {rv:.6f}  {list(A)}")
sys.stdout.flush()

# Also a=3, M=30
print(f"\nPrimitive sets with min=3, max=30, k=4:")
a = 3; M_target = 30
middle = [x for x in range(a+1, M_target) if x % a != 0 and M_target % x != 0]
candidates = []
for sub in combinations(middle, 2):
    A = [a] + list(sub) + [M_target]
    if not is_primitive(A): continue
    r = analyze(A, mult=20)
    candidates.append((r['ratio'], tuple(A)))
candidates.sort(reverse=True)
print(f"  {len(candidates)} sets, top 10:")
for rv, A in candidates[:10]:
    print(f"    {rv:.6f}  {list(A)}")

print("\nDONE.")
