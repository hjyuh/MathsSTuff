"""
TASK 1: Test 2G(M) > S1 for large k families.
TASK 2: Compare Bonferroni-2 at M (with floors) to asymptotic R.
TASK 3: Find the tightest margin (minimum 2G(M) - S1).
"""
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

def F_at_M(A):
    """Compute F(M) exactly via sieve up to M = max(A)."""
    M = max(A)
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

def bonferroni_2_at_M(A):
    """Compute Bonferroni-2 at M: sum floor(M/a_i) - sum floor(M/lcm(a_i,a_j))."""
    M = max(A)
    single = sum(M // e for e in A)
    pairs = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            l = lcm2(A[i], A[j])
            pairs += M // l
    return single - pairs  # lower bound on F(M)

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
          101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]

# ============================================
# TASK 1: Test 2G(M) > S1 on specific families
# ============================================
print("TASK 1: 2G(M) > S1 for LARGE k FAMILIES")
print("=" * 80)

print("\nFAMILY 1: First k primes {p : p <= P}")
print(f"{'P':>4} {'k':>3} {'M':>4} {'F(M)':>6} {'2G(M)':>10} {'S1':>10} {'margin':>12}")
print("-" * 60)
for P in [73, 97, 127, 151]:
    A = [p for p in PRIMES if p <= P]
    k = len(A)
    if k == 0: continue
    twoGM, S1, F_M, _ = two_GM_and_S1(A)
    margin = twoGM - S1
    print(f"{P:>4} {k:>3} {max(A):>4} {F_M:>6} {twoGM:>10.6f} {S1:>10.6f} {margin:>+12.6f}")
sys.stdout.flush()

print("\nFAMILY 2: Scaled primes {2p : p prime, p <= P}")
print(f"{'P':>4} {'k':>3} {'M':>4} {'F(M)':>6} {'2G(M)':>10} {'S1':>10} {'margin':>12}")
print("-" * 60)
for P in [73, 97, 127, 151]:
    A = [2*p for p in PRIMES if p <= P]
    k = len(A)
    if k == 0: continue
    twoGM, S1, F_M, _ = two_GM_and_S1(A)
    margin = twoGM - S1
    print(f"{P:>4} {k:>3} {max(A):>4} {F_M:>6} {twoGM:>10.6f} {S1:>10.6f} {margin:>+12.6f}")
sys.stdout.flush()

print("\nFAMILY 3: Co-atom families {N/p_i : p_i | N, p_i prime}")
print(f"{'N':>8} {'k':>3} {'M':>5} {'A (first few)':<30} {'2G(M)':>10} {'S1':>10} {'margin':>12}")
print("-" * 85)
# For k co-atoms: N = p_1 * p_2 * ... * p_k, set = {N/p_i}
for k in [5, 6, 7, 8]:
    ps = PRIMES[:k]
    N = 1
    for p in ps:
        N *= p
    A = sorted([N // p for p in ps])
    if not is_primitive(A):
        print(f"  NOT PRIMITIVE: N={N}, A={A}")
        continue
    twoGM, S1, F_M, _ = two_GM_and_S1(A)
    margin = twoGM - S1
    A_str = str(A[:4]) + "..." if len(A) > 4 else str(A)
    print(f"{N:>8} {k:>3} {max(A):>5} {A_str:<30} {twoGM:>10.6f} {S1:>10.6f} {margin:>+12.6f}")
sys.stdout.flush()

print("\nFAMILY 4: Coprime-plus-one {q_1,...,q_{k-1}, Q+1}")
print(f"{'k':>3} {'Q+1':>6} {'A':<40} {'2G(M)':>10} {'S1':>10} {'margin':>12}")
print("-" * 85)
for k in [5, 6, 7, 8, 10, 12]:
    # Q = product of first k-1 primes
    ps = PRIMES[:k-1]
    Q = 1
    for p in ps:
        Q *= p
    A = sorted(ps + [Q+1])
    if not is_primitive(A):
        # Check primitivity - Q+1 should be coprime to each p_i since Q+1 ≡ 1 mod p_i
        continue
    twoGM, S1, F_M, _ = two_GM_and_S1(A)
    margin = twoGM - S1
    A_str = str(A[:4]) + "..." if len(A) > 4 else str(A)
    print(f"{k:>3} {Q+1:>6} {A_str:<40} {twoGM:>10.6f} {S1:>10.6f} {margin:>+12.6f}")
sys.stdout.flush()

print("\nFAMILY 5: Random primitive sets k=8..20, max<=500")
print(f"{'k':>3} {'trial':>5} {'M':>4} {'2G(M)':>10} {'S1':>10} {'margin':>12}")
print("-" * 60)
random.seed(42)
worst_random_margin = float('inf')
worst_random_set = None
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
        if margin < worst_random_margin:
            worst_random_margin = margin
            worst_random_set = tuple(A)
        if trial < 2:
            print(f"{target_k:>3} {trial:>5} {max(A):>4} {twoGM:>10.6f} {S1:>10.6f} {margin:>+12.6f}")
print(f"\n  Worst random: margin={worst_random_margin:+.6f} at {worst_random_set}")
sys.stdout.flush()

# ============================================
# TASK 2: Compare Bonferroni-2 with floors vs asymptotic R
# ============================================
print("\n" + "=" * 80)
print("TASK 2: Floor rescue analysis")
print("Bonferroni-2 at M (with floors) vs asymptotic R = M*(S1 - 2*S2)")
print("=" * 80)

# For each key set: compute
# - F(M) (exact)
# - Bonferroni-2 lower bound at M: sum floor(M/a) - sum floor(M/lcm)
# - Asymptotic: M*S1 - M*S2
# - Floor correction: difference

test_families = [
    ("First 10 primes", [p for p in PRIMES if p <= 29]),
    ("First 15 primes", [p for p in PRIMES if p <= 47]),
    ("First 21 primes", [p for p in PRIMES if p <= 73]),
    ("First 25 primes", [p for p in PRIMES if p <= 97]),
    ("2*first 21 primes", [2*p for p in PRIMES if p <= 73]),
    ("{4,6,9,10,14,15}", [4,6,9,10,14,15]),
    ("{4,6,9,10,14,15,21,22}", [4,6,9,10,14,15,21,22]),
    ("Co-atom k=5", sorted([(2*3*5*7*11)//p for p in [2,3,5,7,11]])),
    ("Co-atom k=6", sorted([(2*3*5*7*11*13)//p for p in [2,3,5,7,11,13]])),
    ("Co-atom k=7", sorted([(2*3*5*7*11*13*17)//p for p in [2,3,5,7,11,13,17]])),
]

print(f"\n{'family':<30} {'k':>3} {'M':>7} {'F(M)':>7} {'Bonf2(M)':>9} {'asymp':>9} {'2*S2*M':>9} {'R*M':>10}")
print("-" * 95)
for name, A in test_families:
    A = sorted(A)
    if not is_primitive(A):
        print(f"{name:<30} NOT PRIMITIVE")
        continue
    M = max(A)
    k = len(A)
    F_M = F_at_M(A)
    bonf2 = bonferroni_2_at_M(A)
    # Asymptotic: M*(S1 - S2)
    S1 = sum(Fraction(1, e) for e in A)
    S2 = Fraction(0)
    for i in range(k):
        for j in range(i+1, k):
            l = lcm2(A[i], A[j])
            S2 += Fraction(1, l)
    M_S1_S2 = float(M * (S1 - S2))
    R_M = float(M * (S1 - 2*S2))
    S2_M_times_2 = float(2*S2*M)
    print(f"{name:<30} {k:>3} {M:>7} {F_M:>7} {bonf2:>9} {M_S1_S2:>9.2f} {S2_M_times_2:>9.2f} {R_M:>+10.2f}")
sys.stdout.flush()

# Key question: is F(M) - M*S1/2 positive?
# Equivalently: is 2*F(M) > M*S1, i.e., 2G(M) > S1?
print("\n  Test: 2F(M) > M*S1 (i.e., 2G(M) > S1)?")
print(f"{'family':<30} {'2F(M)':>8} {'M*S1':>10} {'diff':>10}")
for name, A in test_families:
    A = sorted(A)
    if not is_primitive(A): continue
    M = max(A)
    F_M = F_at_M(A)
    S1 = sum(1.0/e for e in A)
    diff = 2*F_M - M*S1
    print(f"{name:<30} {2*F_M:>8} {M*S1:>10.2f} {diff:>+10.4f}")
sys.stdout.flush()

# ============================================
# TASK 3: Find minimum margin 2G(M) - S1
# ============================================
print("\n" + "=" * 80)
print("TASK 3: Minimum margin search (tightest 2G(M) - S1)")
print("=" * 80)

# Systematic search over primitive sets
min_margin = float('inf')
min_margin_set = None
total = 0

for a1 in range(2, 20):
    pool = [x for x in range(a1+1, 80) if x % a1 != 0][:20]
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

print(f"  Checked {total} primitive sets")
print(f"  Minimum margin: {min_margin:+.6f}")
print(f"  At set: {list(min_margin_set) if min_margin_set else None}")

# Also look at the first-primes and scaled families
print("\n  Comparing to large-k families:")
for P in [31, 53, 73, 97, 127, 151, 199]:
    A = [p for p in PRIMES if p <= P]
    if not A: continue
    twoGM, S1, _, _ = two_GM_and_S1(A)
    margin = twoGM - S1
    k = len(A)
    print(f"    First {k} primes ({max(A)}): margin = {margin:+.6f}")

for P in [31, 73, 127, 199]:
    A = [2*p for p in PRIMES if p <= P]
    if not A: continue
    twoGM, S1, _, _ = two_GM_and_S1(A)
    margin = twoGM - S1
    k = len(A)
    print(f"    Scaled 2·first {k} primes ({max(A)}): margin = {margin:+.6f}")

print("\nDONE.")
