"""
C_local(A) = max_{x <= 10*max(A)} |F(x) - delta*x|.
Compute for prime sets, scaled prime sets, random sets.
Also: count subsets S with lcm(S) <= max(A).
"""
from math import gcd
from itertools import combinations
import random, time, sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def delta_product(primes):
    p = 1.0
    for a in primes:
        p *= (1 - 1.0/a)
    return 1 - p

def delta_ie(A):
    k = len(A)
    if k > 20:
        # Use sieve for large k
        return None
    d = 0.0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            d += ((-1)**(size+1)) / l
    return d

def delta_sieve(A, N=100000):
    hit = bytearray(N+1)
    for a in A:
        for m in range(a, N+1, a):
            hit[m] = 1
    return sum(hit[1:]) / N

def compute_C_local(A, mult=10):
    M = max(A)
    X = mult * M
    # Compute delta
    if all(gcd(A[i],A[j])==1 for i in range(len(A)) for j in range(i+1,len(A))):
        delta = delta_product(A)
    else:
        delta = delta_ie(A)
        if delta is None:
            delta = delta_sieve(A, max(X, 100000))
    # Sieve
    hit = bytearray(X+1)
    for a in A:
        for m in range(a, X+1, a):
            hit[m] = 1
    run = 0; mx = 0.0; mx_x = 0
    for x in range(1, X+1):
        run += hit[x]
        d = abs(run - delta*x)
        if d > mx:
            mx = d; mx_x = x
    return mx, mx_x, delta

def count_small_lcm_subsets(A):
    """Count non-empty subsets S of A with lcm(S) <= max(A)."""
    M = max(A)
    k = len(A)
    count = 0
    total = 0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            total += 1
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            if l <= M:
                count += 1
    return count, total

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

# ============================================
# PART 1: Prime sets {p : p <= P}
# ============================================
print("=" * 75)
print("C_local for A = {p : p <= P}")
print("=" * 75)
print(f"{'P':>4} {'k':>3} {'max':>4} {'C_local':>10} {'C/k':>8} {'delta':>8} {'at x':>8}")
print("-" * 60)

for P in [11, 23, 47, 73, 97]:
    A = [p for p in PRIMES if p <= P]
    k = len(A)
    C, cx, delta = compute_C_local(A)
    print(f"{P:>4} {k:>3} {max(A):>4} {C:>10.4f} {C/k:>8.4f} {delta:>8.6f} {cx:>8}")
sys.stdout.flush()

# ============================================
# PART 2: Scaled prime sets {2p : p <= P}
# ============================================
print("\n" + "=" * 75)
print("C_local for A = {2p : p prime, p <= P}")
print("=" * 75)
print(f"{'P':>4} {'k':>3} {'max':>4} {'C_local':>10} {'C/k':>8} {'delta':>8} {'at x':>8}")
print("-" * 60)

for P in [11, 23, 47, 73, 97]:
    A = [2*p for p in PRIMES if p <= P]
    k = len(A)
    C, cx, delta = compute_C_local(A)
    print(f"{P:>4} {k:>3} {max(A):>4} {C:>10.4f} {C/k:>8.4f} {delta:>8.6f} {cx:>8}")
sys.stdout.flush()

# ============================================
# PART 3: Random primitive sets
# ============================================
print("\n" + "=" * 75)
print("C_local for random primitive sets, max <= 200")
print("=" * 75)
print(f"{'k':>3} {'trial':>6} {'set':>40} {'C_local':>10} {'C/k':>8}")
print("-" * 75)

random.seed(42)
max_Ck = {}  # k -> max C/k found

for target_k in [5, 10, 15, 20]:
    for trial in range(20):
        # Build random primitive set
        pool = list(range(2, 201))
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
        k = len(A)
        C, cx, delta = compute_C_local(A)
        ck = C/k
        if k not in max_Ck or ck > max_Ck[k][0]:
            max_Ck[k] = (ck, C, tuple(A))
        if trial < 3 or ck > 4:
            Astr = str(A) if len(str(A)) < 38 else str(A[:5])[:-1] + f',...,{A[-1]}]'
            print(f"{k:>3} {trial:>6} {Astr:>40} {C:>10.4f} {ck:>8.4f}")
    sys.stdout.flush()

print("\nWorst C/k by target k:")
for k in sorted(max_Ck):
    ck, C, A = max_Ck[k]
    Astr = str(list(A)) if len(str(list(A))) < 50 else str(list(A[:5]))[:-1] + f',...,{A[-1]}]'
    print(f"  k={k:>2}: max C/k = {ck:.4f}, C = {C:.4f}, A = {Astr}")

# ============================================
# PART 4: Subsets with lcm <= max(A)
# ============================================
print("\n" + "=" * 75)
print("SUBSETS WITH lcm(S) <= max(A)")
print("=" * 75)

# Only feasible for small k (2^k subsets)
print(f"{'Set':>30} {'k':>3} {'count':>6} {'2^k-1':>7} {'k(k+1)/2':>9} {'count<=bound':>12}")
print("-" * 75)

test_sets = [
    [3, 5, 7],
    [2, 3, 5, 7, 11],
    [3, 5, 7, 11, 13],
    [2, 3, 5, 7, 11, 13, 17, 19],
    [4, 6, 10, 14],
    [4, 6, 9, 10, 14, 15],
    [6, 10, 14, 15, 21, 22],
    [3, 4, 5, 7, 11, 13, 17, 19],
    [4, 6, 10, 14, 22, 26, 34, 38],
]

for A in test_sets:
    A = sorted(A)
    if not is_primitive(A):
        continue
    k = len(A)
    if k > 18:
        continue
    cnt, total = count_small_lcm_subsets(A)
    bound = k*(k+1)//2
    Astr = str(A) if len(str(A)) < 28 else str(A[:4])[:-1] + f',...,{A[-1]}]'
    ok = "YES" if cnt <= bound else "NO"
    print(f"{Astr:>30} {k:>3} {cnt:>6} {total:>7} {bound:>9} {ok:>12}")

# More systematic: all primitive sets k=4..8, max<=25
print("\nSystematic check: count(lcm(S)<=max) vs k(k+1)/2")
violations = 0
checked = 0
worst_excess = 0
worst_set = None
for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 26) if x % a1 != 0][:14]
    for tk in range(4, 9):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            checked += 1
            k = len(A)
            cnt, _ = count_small_lcm_subsets(A)
            bound = k*(k+1)//2
            if cnt > bound:
                violations += 1
                excess = cnt - bound
                if excess > worst_excess:
                    worst_excess = excess
                    worst_set = (tuple(A), cnt, bound)

print(f"  Checked: {checked} sets")
print(f"  Violations (count > k(k+1)/2): {violations}")
if worst_set:
    A, cnt, bound = worst_set
    print(f"  Worst: {A}, count={cnt}, bound={bound}, excess={cnt-bound}")
else:
    print(f"  count(lcm(S) <= max(A)) <= k(k+1)/2 ALWAYS holds!")

# ============================================
# PART 5: Summary
# ============================================
print("\n" + "=" * 75)
print("SUMMARY")
print("=" * 75)

# Collect all C/k values
all_ck = []
for P in [11, 23, 47, 73, 97]:
    A = [p for p in PRIMES if p <= P]
    C, _, _ = compute_C_local(A)
    all_ck.append(("primes<="+str(P), len(A), C/len(A)))
for P in [11, 23, 47, 73, 97]:
    A = [2*p for p in PRIMES if p <= P]
    C, _, _ = compute_C_local(A)
    all_ck.append(("2*primes<="+str(P), len(A), C/len(A)))

print(f"  Max C/k across all structured sets: {max(ck for _,_,ck in all_ck):.4f}")
print(f"  Max C/k across random sets: {max(ck for ck,_,_ in max_Ck.values()):.4f}")
overall_max = max(max(ck for _,_,ck in all_ck), max(ck for ck,_,_ in max_Ck.values()))
print(f"  OVERALL max C/k: {overall_max:.4f}")
print(f"  C_local = O(k) with constant < {overall_max+0.5:.1f}: {'SUPPORTED' if overall_max < 5 else 'NOT SUPPORTED'}")

print("\nDONE.")
