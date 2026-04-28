"""
A = {2p : p prime, p <= 73} -- the scaling counterexample from the paper.
Compute quotient-core, density, transfer lemma horizon, EP-488 verification.
Also: search for EP-488 failures with |A| <= 15, max <= 200.
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

def sieve_F(h, A):
    hit = bytearray(h + 1)
    for a in A:
        for m in range(a, h + 1, a):
            hit[m] = 1
    f = [0]*(h+1)
    r = 0
    for x in range(1, h+1):
        r += hit[x]
        f[x] = r
    return f

def delta_ie(A):
    k = len(A)
    d = 0.0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            d += ((-1)**(size+1)) / l
    return d

# ============================================
# PART 1: THE SCALING EXAMPLE A = {2p : p <= 73}
# ============================================
print("=" * 70)
print("A = {2p : p prime, p <= 73}")
print("=" * 70)

primes_le73 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]
A = [2*p for p in primes_le73]
print(f"A = {A}")
print(f"|A| = {len(A)}, min = {min(A)}, max = {max(A)}")
print(f"Primitive: {is_primitive(A)}")

S1_A = sum(1.0/a for a in A)
print(f"S1(A) = {S1_A:.6f}")

# Peel off min(A) = 4
a_min = 4
A_prime = [x for x in A if x != a_min]
print(f"\nPeeling off min(A) = {a_min}")
print(f"A' = A \\ {{{a_min}}} = {A_prime}")

# Quotient-core Q_4
Q4_raw = []
for b in A_prime:
    g = gcd(a_min, b)
    q = b // g
    Q4_raw.append(q)

print(f"\nRaw quotients b/gcd(4,b) for b in A': {Q4_raw}")

# Primitivize (remove elements that divide others)
Q4_raw_sorted = sorted(set(Q4_raw))
Q4 = []
for i, x in enumerate(Q4_raw_sorted):
    divisible = False
    for j, y in enumerate(Q4_raw_sorted):
        if i != j and y < x and x % y == 0:
            divisible = True
            break
    if not divisible:
        Q4.append(x)

print(f"Q_4 = prim(quotients) = {Q4}")
print(f"|Q_4| = {len(Q4)}")
print(f"Q_4 is the set of odd primes <= 73: {Q4 == [p for p in primes_le73 if p > 2]}")

# Compute delta_{Q4} exactly (primes are coprime, so product formula)
prod_Q4 = 1.0
for p in Q4:
    prod_Q4 *= (1 - 1.0/p)
delta_Q4 = 1 - prod_Q4
S1_Q4 = sum(1.0/p for p in Q4)

print(f"\ndelta(Q_4) = 1 - prod(1-1/p) = {delta_Q4:.10f}")
print(f"S1(Q_4) = {S1_Q4:.6f}")
print(f"2*delta(Q_4) = {2*delta_Q4:.6f}")
print(f"2*delta(Q_4) > S1(Q_4): {2*delta_Q4 > S1_Q4} (ratio {2*delta_Q4/S1_Q4:.6f})")
print(f"delta(Q_4) > 1/2: {delta_Q4 > 0.5}")
print(f"1 - 2*delta(Q_4) = {1-2*delta_Q4:.6f} (margin contribution sign: {'NEGATIVE' if delta_Q4 > 0.5 else 'positive'})")

# Transfer lemma horizon
# Need C_{Q4}: discrepancy of Q4. Since Q4 = odd primes <= 73, coprime.
# C < 2^{|Q4|-1} = 2^19 universally. But let's try to compute via sieve.
L_Q4 = Q4[0]
for p in Q4[1:]:
    L_Q4 = lcm2(L_Q4, p)
print(f"\nlcm(Q_4) = {L_Q4}")
print(f"lcm(Q_4) = product of primes 3..73 (since coprime)")

# L_Q4 is product of primes 3 to 73 -- this is HUGE. Can't sieve.
# Use the universal bound C < 2^{k-1} = 2^19 = 524288
C_Q4_bound = 2**(len(Q4)-1)
print(f"C(Q_4) < 2^{{|Q_4|-1}} = 2^{len(Q4)-1} = {C_Q4_bound}")

horizon = 3 * a_min * (C_Q4_bound + 1) / (1 - delta_Q4)
print(f"\nTransfer lemma horizon: 3*{a_min}*(C_Q4+1)/(1-delta_Q4)")
print(f"  = 3*4*{C_Q4_bound+1}/{1-delta_Q4:.6f}")
print(f"  = {horizon:.0f}")
print(f"  (This is HUGE due to exponential C bound)")

# But we can verify EP-488 DIRECTLY by sieve
print(f"\n--- Direct EP-488 verification for A ---")
# Use sieve up to a reasonable horizon
h = 30000  # Should be enough for density convergence
f = sieve_F(h, A)

# Compute delta via sieve at large x
delta_A = f[h] / h
S1_A = sum(1.0/a for a in A)
print(f"delta(A) approx = {delta_A:.6f} (sieve at {h})")
print(f"S1(A) = {S1_A:.6f}")
print(f"2*delta(A) = {2*delta_A:.6f}")
print(f"2*delta > S1: {2*delta_A > S1_A}")

# EP-488: check 2*minG > maxG
M = max(A)
min_g = float('inf')
max_g = 0.0
for x in range(M, h+1):
    gx = f[x]/x
    if gx < min_g: min_g = gx
    if gx > max_g: max_g = gx

passes = 2*min_g > max_g
ratio = max_g/(2*min_g) if min_g > 0 else 999
print(f"min G = {min_g:.6f}, max G = {max_g:.6f}")
print(f"2*minG = {2*min_g:.6f}")
print(f"EP-488 (2*minG > maxG): {'PASS' if passes else 'FAIL'}")
print(f"Ratio maxG/(2*minG) = {ratio:.6f}")

# Compute actual C for A via sieve
max_C = 0.0
for x in range(1, h+1):
    d = abs(f[x] - delta_A * x)
    if d > max_C:
        max_C = d
print(f"C(A) approx = {max_C:.2f} (sieve at {h})")
print(f"Actual horizon 3*C/delta = {3*max_C/delta_A:.0f}")

# ============================================
# PART 2: SEARCH FOR EP-488 FAILURES
# ============================================
print("\n" + "=" * 70)
print("SEARCH: EP-488 failures with |A| <= 15, max <= 200")
print("Strategy: random + structured sampling")
print("=" * 70)
sys.stdout.flush()

import random
random.seed(42)

worst_ratio_found = 0.0
worst_set_found = None
total_checked = 0
failures = 0

# Strategy 1: scaled prime sets {m*p : p prime}
print("\n--- Scaled prime sets ---")
for m in range(2, 20):
    for max_p in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        primes = [p for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47] if p <= max_p]
        A = [m*p for p in primes]
        A = [a for a in A if a <= 200]
        if len(A) < 4 or not is_primitive(A):
            continue
        total_checked += 1
        M = max(A)
        h = max(3000, 20*M)
        f = sieve_F(h, A)
        mg = float('inf'); xg = 0.0
        for x in range(M, h+1):
            gx = f[x]/x
            if gx < mg: mg = gx
            if gx > xg: xg = gx
        if mg > 0:
            r = xg/(2*mg)
            if r > worst_ratio_found:
                worst_ratio_found = r
                worst_set_found = tuple(A)
            if 2*mg <= xg:
                failures += 1
                print(f"  FAILURE: {A}")

print(f"  Checked {total_checked}, worst ratio {worst_ratio_found:.6f} at {worst_set_found}")
sys.stdout.flush()

# Strategy 2: consecutive k-tuples
print("\n--- Consecutive k-tuples {a,...,a+k-1} ---")
for k in range(4, 16):
    for a in range(3, 200-k+1):
        A = list(range(a, a+k))
        if not is_primitive(A):
            continue
        if max(A) > 200:
            continue
        total_checked += 1
        M = max(A)
        h = max(2000, 15*M)
        f = sieve_F(h, A)
        mg = float('inf'); xg = 0.0
        for x in range(M, h+1):
            gx = f[x]/x
            if gx < mg: mg = gx
            if gx > xg: xg = gx
        if mg > 0:
            r = xg/(2*mg)
            if r > worst_ratio_found:
                worst_ratio_found = r
                worst_set_found = tuple(A)
                if r > 0.98:
                    print(f"  TIGHT: k={k}, a={a}, ratio={r:.6f}")
            if 2*mg <= xg:
                failures += 1
                print(f"  FAILURE: {A}")

print(f"  Checked {total_checked}, worst ratio {worst_ratio_found:.6f}")
sys.stdout.flush()

# Strategy 3: random primitive sets
print("\n--- Random primitive sets ---")
for _ in range(50000):
    k = random.randint(4, 15)
    elems = sorted(random.sample(range(2, 201), min(k+5, 30)))
    # Try to find a primitive subset of size k
    prim_sub = []
    for e in elems:
        ok = True
        for p in prim_sub:
            if e % p == 0 or p % e == 0:
                ok = False
                break
        if ok:
            prim_sub.append(e)
        if len(prim_sub) == k:
            break
    if len(prim_sub) < 4:
        continue
    A = prim_sub
    total_checked += 1
    M = max(A)
    h = max(2000, 10*M)
    f = sieve_F(h, A)
    mg = float('inf'); xg = 0.0
    for x in range(M, h+1):
        gx = f[x]/x
        if gx < mg: mg = gx
        if gx > xg: xg = gx
    if mg > 0:
        r = xg/(2*mg)
        if r > worst_ratio_found:
            worst_ratio_found = r
            worst_set_found = tuple(A)
        if 2*mg <= xg:
            failures += 1
            print(f"  FAILURE: {A}")

print(f"  Checked {total_checked} total, worst ratio {worst_ratio_found:.6f}")
sys.stdout.flush()

print(f"\n{'='*70}")
print(f"FINAL RESULTS")
print(f"{'='*70}")
print(f"Total primitive sets checked: {total_checked}")
print(f"EP-488 failures: {failures}")
print(f"Worst ratio maxG/(2*minG): {worst_ratio_found:.6f}")
print(f"Worst set: {worst_set_found}")

print("\nDONE.")
