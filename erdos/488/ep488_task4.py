"""Task 4 fix: fixed (a, M) with a not dividing M."""
from math import gcd
from itertools import combinations

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
    for x in range(M, h_abs + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g
        if g > mx: mx = g
    return mx/(2*mn) if mn > 0 else 999

# Try several (a, M) pairs with a not dividing M
for (a, M_t) in [(5, 21), (5, 23), (3, 20), (4, 21), (5, 22), (7, 25), (10, 33)]:
    print(f"\n=== min={a}, max={M_t} ===")
    for k in [3, 4, 5, 6]:
        # Middle elements: in (a, M_t), not dividing M_t, not divisible by a, not divisible by M_t
        middle = []
        for x in range(a+1, M_t):
            if x % a == 0: continue  # a divides x
            if M_t % x == 0: continue  # x divides M_t
            if x % M_t == 0: continue  # M_t divides x (can't happen x < M_t)
            middle.append(x)
        if len(middle) < k-2:
            continue

        candidates = []
        for sub in combinations(middle, k-2):
            A = sorted([a] + list(sub) + [M_t])
            if not is_primitive(A): continue
            r = analyze(A)
            candidates.append((r, tuple(A)))
        candidates.sort(reverse=True)

        if candidates:
            print(f"  k={k}: {len(candidates)} sets")
            # Consecutive (if valid): {a, a+1, ..., M_t} with M_t = a+k-1 requires M_t = a+k-1
            # But M_t is fixed here, so "consecutive" means contiguous subset containing a and M_t
            # For k=4, M_t=a+3: {a, a+1, a+2, a+3}
            is_consecutive = (M_t == a + k - 1)
            print(f"    top 5:")
            for rv, A in candidates[:5]:
                print(f"      {rv:.6f}  {list(A)}")
            if len(candidates) > 5:
                print(f"    bottom 3:")
                for rv, A in candidates[-3:]:
                    print(f"      {rv:.6f}  {list(A)}")

# Try a=3, M=11 (consecutive is possible with k=9 max, but with constraint)
print("\n\n=== min=3, max=11 (so k can range from 2 to ~9) ===")
a, M_t = 3, 11
middle = [x for x in range(a+1, M_t) if x%a!=0 and M_t%x!=0 and x%M_t!=0]
print(f"Valid middle elements: {middle}")
for k in [3, 4, 5, 6, 7]:
    candidates = []
    for sub in combinations(middle, k-2):
        A = sorted([a] + list(sub) + [M_t])
        if not is_primitive(A): continue
        r = analyze(A)
        candidates.append((r, tuple(A)))
    candidates.sort(reverse=True)
    if candidates:
        print(f"  k={k}: {len(candidates)} sets, worst ratio={candidates[0][0]:.6f} at {list(candidates[0][1])}")
        for rv, A in candidates[:3]:
            print(f"    {rv:.6f}  {list(A)}")

print("\nDONE.")
