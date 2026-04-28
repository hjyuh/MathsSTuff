"""Fixed version: memory-safe F(M) computation, finish all tasks."""
from math import gcd
from itertools import combinations
from fractions import Fraction
import random, time, sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def F_at_M_IE(A):
    """Compute F(M) via exact inclusion-exclusion (handles huge M)."""
    M = max(A)
    k = len(A)
    total = 0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            if l > M: continue
            total += ((-1)**(size+1)) * (M // l)
    return total

def F_at_M(A):
    M = max(A)
    if M > 50_000_000:
        return F_at_M_IE(A)
    hit = bytearray(M + 1)
    for e in A:
        for m in range(e, M + 1, e):
            hit[m] = 1
    return sum(hit)

def two_GM_and_S1(A):
    M = max(A)
    F_M = F_at_M(A)
    GM = F_M / M
    S1 = sum(1.0/e for e in A)
    return 2*GM, S1, F_M, GM

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
          101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]

# ============================================
# COMPLETE FAMILY 4 (coprime-plus-one)
# ============================================
print("FAMILY 4 (cont): Coprime-plus-one {q_1,...,q_{k-1}, Q+1}")
print(f"{'k':>3} {'Q+1':>10} {'M':>10} {'2G(M)':>10} {'S1':>10} {'margin':>12}")
print("-" * 70)
for k in [5, 6, 7, 8, 10, 12]:
    ps = PRIMES[:k-1]
    Q = 1
    for p in ps:
        Q *= p
    A = sorted(ps + [Q+1])
    if not is_primitive(A):
        continue
    try:
        twoGM, S1, F_M, _ = two_GM_and_S1(A)
        margin = twoGM - S1
        print(f"{k:>3} {Q+1:>10} {max(A):>10} {twoGM:>10.6f} {S1:>10.6f} {margin:>+12.6f}")
    except Exception as e:
        print(f"  k={k}: error {e}")
sys.stdout.flush()

# ============================================
# FAMILY 5 (random) - limited range
# ============================================
print("\nFAMILY 5: Random primitive sets k=8..20, max<=500")
random.seed(42)
worst_random_margin = float('inf')
worst_random_set = None
cnt = 0
for target_k in [8, 10, 12, 15, 20]:
    for trial in range(30):
        pool = list(range(2, 501))
        random.shuffle(pool)
        A = []
        for e in pool:
            ok = all(e % a != 0 and a % e != 0 for a in A)
            if ok:
                A.append(e)
            if len(A) == target_k:
                break
        if len(A) < target_k:
            continue
        A.sort()
        twoGM, S1, F_M, _ = two_GM_and_S1(A)
        margin = twoGM - S1
        cnt += 1
        if margin < worst_random_margin:
            worst_random_margin = margin
            worst_random_set = tuple(A)
        if trial < 2:
            print(f"  k={target_k} trial={trial}: M={max(A)}, 2G(M)={twoGM:.4f}, S1={S1:.4f}, margin={margin:+.4f}")
print(f"\n  Random sets checked: {cnt}")
print(f"  Worst random margin: {worst_random_margin:+.6f}")
print(f"  Worst random set: {worst_random_set}")
sys.stdout.flush()

# ============================================
# TASK 2: Floor rescue analysis
# ============================================
print("\n" + "=" * 80)
print("TASK 2: Floor rescue analysis — 2F(M) vs M*S1, 2(M*S1 - 2*M*S2)")
print("=" * 80)

test_families = [
    ("First 10 primes", PRIMES[:10]),
    ("First 15 primes", PRIMES[:15]),
    ("First 21 primes", PRIMES[:21]),
    ("First 25 primes", PRIMES[:25]),
    ("First 31 primes", PRIMES[:31]),
    ("2*first 21 primes", [2*p for p in PRIMES[:21]]),
    ("{4,6,9,10,14,15}", [4,6,9,10,14,15]),
    ("{4,6,9,10,14,15,21,22}", [4,6,9,10,14,15,21,22]),
    ("Co-atom k=5 (N=2310)", sorted([2310//p for p in [2,3,5,7,11]])),
    ("Co-atom k=6 (N=30030)", sorted([30030//p for p in [2,3,5,7,11,13]])),
    ("Co-atom k=7 (N=510510)", sorted([510510//p for p in [2,3,5,7,11,13,17]])),
]

print(f"\n{'family':<28} {'k':>3} {'M':>10} {'2F(M)':>8} {'M*S1':>10} {'2F-MS1':>10} {'R*M':>10}")
print("-" * 90)
for name, A in test_families:
    A = sorted(A)
    if not is_primitive(A):
        print(f"{name:<28}: NOT PRIMITIVE")
        continue
    M = max(A)
    k = len(A)
    F_M = F_at_M(A)
    S1f = sum(1.0/e for e in A)
    # Compute R*M exactly via fractions
    S1 = sum(Fraction(1, e) for e in A)
    S2 = Fraction(0)
    for i in range(k):
        for j in range(i+1, k):
            l = lcm2(A[i], A[j])
            S2 += Fraction(1, l)
    R_M_exact = float(M * (S1 - 2*S2))
    M_S1 = M * S1f
    diff = 2*F_M - M_S1
    print(f"{name:<28} {k:>3} {M:>10} {2*F_M:>8} {M_S1:>10.2f} {diff:>+10.2f} {R_M_exact:>+10.2f}")
sys.stdout.flush()

# Interpretation: even when R*M is NEGATIVE (asymptotic), 2F(M) - M*S1 is POSITIVE
# because of floor function corrections.

# ============================================
# TASK 3: Minimum margin search
# ============================================
print("\n" + "=" * 80)
print("TASK 3: Minimum margin across all primitive sets")
print("=" * 80)

min_margin = float('inf')
min_margin_set = None
total = 0
t0 = time.time()

for a1 in range(2, 16):
    pool = [x for x in range(a1+1, 80) if x % a1 != 0][:18]
    for tk in range(2, 10):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total += 1
            twoGM, S1, _, _ = two_GM_and_S1(A)
            margin = twoGM - S1
            if margin < min_margin:
                min_margin = margin
                min_margin_set = tuple(A)

elapsed = time.time() - t0
print(f"  Checked {total} primitive sets in {elapsed:.1f}s")
print(f"  Minimum margin: {min_margin:+.6f}")
print(f"  At set: {list(min_margin_set)}")
sys.stdout.flush()

# Find other sets close to the minimum
print("\n  Top 10 tightest margins:")
margins = []
for a1 in range(2, 16):
    pool = [x for x in range(a1+1, 80) if x % a1 != 0][:18]
    for tk in range(2, 10):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            twoGM, S1, _, _ = two_GM_and_S1(A)
            margin = twoGM - S1
            if margin < 0.01:  # only record tight ones
                margins.append((margin, tuple(A)))
margins.sort()
for margin, A in margins[:15]:
    print(f"    {margin:+.6f}  {list(A)}")

# Check: is minimum margin always POSITIVE?
if min_margin > 0:
    print(f"\n  ALL margins POSITIVE. 2G(M) > S1 holds for ALL tested sets.")
else:
    print(f"\n  NEGATIVE margin found! 2G(M) <= S1 for some set.")

print("\nDONE.")
