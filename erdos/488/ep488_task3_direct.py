"""
Task 3: Direct proof for k >= 3.
Test refined lower bounds on min G.

The simple argument 2G(n) > S1 fails because max G can approach S1.
The refined argument: show max G - 2 min G < 0 via structural bounds.

Specifically: max G is NOT S1 for spread sets. For such sets, the tight
upper bound on max G is something like S1 - 2*S2 + ... (true delta).
"""
from math import gcd
from itertools import combinations
import sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def check(A, mult=20):
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
    S1 = sum(1.0/e for e in A)
    return mn, mx, S1

# The ratio formula: max G / (2 min G) < 1 iff 2 min G > max G.
# Test various upper bounds for max G.

# BOUND 1: max G <= S1 (first-order Bonferroni)
# BOUND 2: max G <= 1 - 1/M (since 1 is not counted)
# BOUND 3: max G <= min(S1, 1 - 1/M)

# LOWER bounds for min G:
# LB1: min G >= 1/a - 1/n (from multiples of a alone)
# LB2: min G >= F(M)/M = G(M)  -- wait, this isn't a lower bound on min over [M, infty)
# LB3: min G >= k/(2a-1) for consecutive (proved)
# LB4: min G >= k/max(A) ... no, k/M is a lower bound at x = M but min can be less

# The key question: what's the TIGHTEST lower bound on min G that works universally?

print("TIGHTER BOUND: test min G >= (F(M)+something)/some-x")
print("=" * 70)

# First: understand the relationship between min G and various candidates
test_sets = [
    [2, 3, 5, 7],
    [3, 5, 7, 11],
    [4, 6, 10, 14],
    [5, 6, 7, 8],
    [10, 11, 12, 13],
    [4, 6, 9, 10, 14, 15],
    [5, 8, 9, 11],
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73],
    [4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94, 106, 118, 122, 134, 142, 146],
]

print(f"{'set':<30} {'k':>3} {'M':>4} {'minG':>10} {'maxG':>10} {'S1':>8} {'1-1/M':>8} {'ratio':>8}")
print("-" * 85)
for A in test_sets:
    A = sorted(A)
    if not is_primitive(A): continue
    mn, mx, S1 = check(A, mult=15)
    M = max(A)
    r = mx/(2*mn) if mn > 0 else 999
    s_str = str(A) if len(str(A)) < 29 else str(A[:4])[:-1] + ",...," + str(A[-1]) + "]"
    print(f"{s_str:<30} {len(A):>3} {M:>4} {mn:>10.5f} {mx:>10.5f} "
          f"{S1:>8.5f} {1-1/M:>8.5f} {r:>8.5f}")
sys.stdout.flush()

# KEY OBSERVATION from data: for large k sets, max G is close to 1 - 1/M.
# For the 21-prime set: M=73, max G = 0.987 = 1 - 0.013 ≈ 1 - 1/77.
# Very close to 1 - 1/M.

# So the CANDIDATE universal bound is: max G <= 1 - 1/M.
# Combined with 2*min G > 1 - 1/M (sufficient for EP-488), we get ratio < 1.

# Test: is max G <= 1 - 1/M always?
print("\n" + "=" * 70)
print("TEST: max G <= 1 - 1/M for all primitive sets?")
print("=" * 70)

total = 0
fails = 0
worst_excess = 0
worst_set = None

for a1 in range(2, 15):
    pool = [x for x in range(a1+1, 40) if x % a1 != 0][:16]
    for tk in range(2, 10):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total += 1
            mn, mx, S1 = check(A, mult=10)
            M = max(A)
            bound = 1 - 1/M
            if mx > bound + 1e-12:
                fails += 1
                excess = mx - bound
                if excess > worst_excess:
                    worst_excess = excess
                    worst_set = (tuple(A), mx, bound)

print(f"  Checked {total}")
print(f"  Failures of max G <= 1 - 1/M: {fails}")
if worst_set:
    A, mx, bnd = worst_set
    print(f"  Worst: {list(A)}, maxG={mx:.6f}, 1-1/M={bnd:.6f}, excess={worst_excess:.6f}")
sys.stdout.flush()

# Now the critical condition: is 2*min G > 1 - 1/M?
print("\n" + "=" * 70)
print("TEST: 2*min G > 1 - 1/M for all primitive sets?")
print("=" * 70)

fails2 = 0
worst_deficit = 0
worst_set2 = None
total2 = 0

for a1 in range(2, 15):
    pool = [x for x in range(a1+1, 40) if x % a1 != 0][:16]
    for tk in range(2, 10):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total2 += 1
            mn, mx, S1 = check(A, mult=10)
            M = max(A)
            bound = 1 - 1/M
            if 2*mn <= bound + 1e-12:
                fails2 += 1
                deficit = bound - 2*mn
                if deficit > worst_deficit:
                    worst_deficit = deficit
                    worst_set2 = (tuple(A), 2*mn, bound, mn, mx)

print(f"  Checked {total2}")
print(f"  Failures of 2*min G > 1 - 1/M: {fails2}")
if worst_set2:
    A, tm, bnd, mn, mx = worst_set2
    r = mx/(2*mn) if mn > 0 else 999
    print(f"  Worst: {list(A)}")
    print(f"    2*minG = {tm:.6f}, 1-1/M = {bnd:.6f}")
    print(f"    deficit = {worst_deficit:.6f}")
    print(f"    ratio = {r:.6f}")
else:
    print("  SUCCESS: 2*min G > 1 - 1/M always!")

# Check: does EP-488 follow from 2*min G > 1 - 1/M?
# Yes: if max G <= 1 - 1/M (need to verify), then 2*min G > 1 - 1/M >= max G gives ratio < 1.
# But max G <= 1 - 1/M is NOT proved. max G <= 1 - 1/m at point m.

# Actually: G(m) = F(m)/m <= (m-1)/m = 1 - 1/m. So for any m >= M, G(m) <= 1 - 1/m <= 1 - 1/M' where M' = max such m... no, G(m) <= 1 - 1/m, and for larger m this is larger.

# So max G <= sup_{m >= M} (1 - 1/m) = 1 (as m -> infty). The bound 1 - 1/M doesn't hold for m >> M.

# Let me re-check the failures where max G > 1 - 1/M. For m large, G(m) can approach δ_A < 1, so G(m) < 1. But is G(m) <= 1 - 1/M?

# Actually the data showed a failure for max G > 1 - 1/M. Let me investigate.

print("\n" + "=" * 70)
print("RETHINK: G(m) <= 1 - 1/m (tight), but m can vary")
print("=" * 70)

# For the 21-prime set: max G = 0.987 at some m. 1 - 1/m at that m is what?
A = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]
M = 73
h = 3000
hit = bytearray(h+1)
for e in A:
    for mm in range(e, h+1, e):
        hit[mm] = 1
run = 0
for x in range(1, M):
    run += hit[x]
max_g = 0; max_g_x = M
for x in range(M, h+1):
    run += hit[x]
    g = run/x
    if g > max_g:
        max_g = g; max_g_x = x
print(f"  21 primes: max G = {max_g:.6f} at x = {max_g_x}")
print(f"  1 - 1/max_g_x = {1 - 1/max_g_x:.6f}")
print(f"  max G <= 1 - 1/x at this x? {max_g <= 1 - 1/max_g_x + 1e-12}")
# And: max G <= 1 - 1/M (the RHS with fixed M)?
print(f"  1 - 1/M = {1 - 1/M:.6f}, max G <= 1-1/M? {max_g <= 1 - 1/M + 1e-12}")

print("\nDONE.")
