"""
Two-regime check for EP-488:
Q1: For S1 >= 1, is min G > 1/2 always?
Q2: Is there a non-coprime primitive set with S1 >= 1 AND delta <= 1/2?
Q3: For S1 < 1, is 2*min G > S1 always?
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

def is_pairwise_coprime(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if gcd(A[i], A[j]) > 1:
                return False
    return True

def check(A, mult=15):
    M = max(A)
    h_abs = max(5000, mult * M)
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    mn = float('inf'); mx = 0
    for x in range(M, h_abs + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g
        if g > mx: mx = g
    # delta approximation: large-x value
    delta = run / h_abs
    S1 = sum(1.0/e for e in A)
    return mn, mx, S1, delta

# ============================================
# Q1: For S1 >= 1, is min G > 1/2?
# ============================================
print("Q1: Is min G > 1/2 for all primitive sets with S1 >= 1?")
print("=" * 70)
sys.stdout.flush()

t0 = time.time()
fail_Q1 = []
total_S1_ge_1 = 0
min_minG_for_S1_ge_1 = float('inf')
min_set = None

for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 200) if x % a1 != 0][:30]
    for tk in range(2, 16):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/e for e in A)
            if S1 < 1: continue
            total_S1_ge_1 += 1
            mn, mx, _, delta = check(A, mult=8)
            if mn <= 0.5 + 1e-12:
                fail_Q1.append((tuple(A), mn, S1, mx, delta))
            if mn < min_minG_for_S1_ge_1:
                min_minG_for_S1_ge_1 = mn
                min_set = tuple(A)

elapsed = time.time() - t0
print(f"  Checked {total_S1_ge_1} primitive sets with S1 >= 1 in {elapsed:.1f}s")
print(f"  Failures (min G <= 1/2): {len(fail_Q1)}")
print(f"  Min of min G across these sets: {min_minG_for_S1_ge_1:.6f}")
if min_set:
    print(f"  Achieved at: {list(min_set)}")

if fail_Q1:
    print(f"  FAIL examples (min G <= 1/2):")
    fail_Q1.sort(key=lambda x: x[1])
    for A, mn, S1, mx, delta in fail_Q1[:10]:
        print(f"    {list(A)}: minG={mn:.5f}, S1={S1:.4f}, maxG={mx:.5f}, delta={delta:.5f}")
sys.stdout.flush()

# ============================================
# Q2: Non-coprime set with S1 >= 1 AND delta <= 1/2?
# ============================================
print("\n" + "=" * 70)
print("Q2: Non-coprime primitive set with S1 >= 1 AND delta <= 1/2?")
print("=" * 70)
sys.stdout.flush()

t0 = time.time()
found_Q2 = []
total_nc_S1_ge_1 = 0

for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 100) if x % a1 != 0][:25]
    for tk in range(3, 16):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            # Must be non-coprime
            if is_pairwise_coprime(A): continue
            S1 = sum(1.0/e for e in A)
            if S1 < 1: continue
            total_nc_S1_ge_1 += 1
            # Compute delta more accurately
            mn, mx, _, delta = check(A, mult=10)
            if delta <= 0.5 + 1e-12:
                found_Q2.append((tuple(A), S1, delta, mn, mx))

elapsed = time.time() - t0
print(f"  Checked {total_nc_S1_ge_1} non-coprime sets with S1 >= 1 in {elapsed:.1f}s")
print(f"  Sets with delta <= 1/2: {len(found_Q2)}")
if found_Q2:
    print(f"  Examples:")
    found_Q2.sort(key=lambda x: x[2])
    for A, S1, delta, mn, mx in found_Q2[:10]:
        print(f"    {list(A)}: S1={S1:.4f}, delta={delta:.4f}, minG={mn:.4f}, maxG={mx:.4f}")
else:
    print(f"  NONE FOUND. All non-coprime sets with S1 >= 1 have delta > 1/2.")
sys.stdout.flush()

# ============================================
# Q3: For S1 < 1, is 2*min G > S1?
# ============================================
print("\n" + "=" * 70)
print("Q3: Is 2*min G > S1 for all primitive sets with S1 < 1?")
print("=" * 70)
sys.stdout.flush()

t0 = time.time()
fail_Q3 = []
total_S1_lt_1 = 0
worst_deficit_Q3 = 0
worst_set_Q3 = None

for a1 in range(2, 15):
    pool = [x for x in range(a1+1, 100) if x % a1 != 0][:25]
    for tk in range(2, 12):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/e for e in A)
            if S1 >= 1: continue
            total_S1_lt_1 += 1
            mn, mx, _, delta = check(A, mult=10)
            if 2*mn <= S1 + 1e-12:
                deficit = S1 - 2*mn
                if deficit > worst_deficit_Q3:
                    worst_deficit_Q3 = deficit
                    worst_set_Q3 = (tuple(A), mn, S1, mx)
                fail_Q3.append((tuple(A), mn, S1, mx, deficit))

elapsed = time.time() - t0
print(f"  Checked {total_S1_lt_1} sets with S1 < 1 in {elapsed:.1f}s")
print(f"  Failures (2*min G <= S1): {len(fail_Q3)}")
print(f"  Worst deficit: {worst_deficit_Q3:.6f}")
if worst_set_Q3:
    A, mn, S1, mx = worst_set_Q3
    r = mx/(2*mn) if mn > 0 else 999
    print(f"  At: {list(A)}: minG={mn:.4f}, S1={S1:.4f}, maxG={mx:.4f}, ratio={r:.4f}")
sys.stdout.flush()

# ============================================
# FINAL ASSESSMENT
# ============================================
print("\n" + "=" * 70)
print("FINAL ASSESSMENT")
print("=" * 70)

Q1_holds = len(fail_Q1) == 0
Q2_no_counter = len(found_Q2) == 0
Q3_holds = len(fail_Q3) == 0

print(f"\n  Q1 (S1>=1 implies min G > 1/2): {'HOLDS' if Q1_holds else 'FAILS'}")
print(f"  Q2 (no non-coprime with S1>=1 AND delta<=1/2): {'HOLDS' if Q2_no_counter else 'COUNTEREXAMPLE'}")
print(f"  Q3 (S1<1 implies 2*min G > S1): {'HOLDS' if Q3_holds else 'FAILS'}")

if Q1_holds and Q3_holds:
    print(f"\n  TWO-REGIME PROOF WORKS:")
    print(f"    Regime 1 (S1 < 1): 2*min G > S1 >= G(m), so 2*min G > G(m).")
    print(f"    Regime 2 (S1 >= 1): min G > 1/2, so 2*min G > 1 > G(m).")
    print(f"    Together: EP-488 holds.")
else:
    print(f"\n  TWO-REGIME PROOF:")
    if not Q1_holds:
        print(f"    FAILS in regime 2: min G can be <= 1/2 even with S1 >= 1")
    if not Q3_holds:
        print(f"    FAILS in regime 1: 2*min G can be <= S1")

print("\nDONE.")
