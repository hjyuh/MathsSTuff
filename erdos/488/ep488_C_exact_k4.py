"""Exact C computation for k=4 consecutive sets and check C < 2^(k-1) = 8."""
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

def density_ie(A):
    total = 0.0
    for size in range(1, len(A)+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            total += ((-1)**(size+1)) / l
    return total

def compute_C_exact(A, max_L=5_000_000):
    """Exact C via full period enumeration."""
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > max_L:
        return None, L
    delta = density_ie(A)
    hit = bytearray(L + 1)
    for a in A:
        for m in range(a, L + 1, a):
            hit[m] = 1
    running = 0
    max_C = 0.0
    for r in range(1, L + 1):
        running += hit[r]
        d = abs(running - delta * r)
        if d > max_C:
            max_C = d
    return max_C, L

print("CONSECUTIVE k-TUPLES: EXACT C")
print("=" * 60)

# k=3: consecutive triples
print("\nk=3 triples {a, a+1, a+2}:")
for a in [3,5,7,10,13,20,30,50,75,100,120]:
    A = [a, a+1, a+2]
    if not is_primitive(A): continue
    C, L = compute_C_exact(A)
    if C is not None:
        print(f"  a={a:4d}: C={C:.4f}, L={L:>10d}, C/(2^(k-1))={C/4:.4f}")

# k=4: consecutive quadruples
print("\nk=4 quadruples {a, a+1, a+2, a+3}:")
for a in [3,4,5,7,8,9,10,11,13,15,17,19,20,23,25,28,30,35,40,50]:
    A = [a, a+1, a+2, a+3]
    if not is_primitive(A): continue
    C, L = compute_C_exact(A)
    if C is not None:
        print(f"  a={a:4d}: C={C:.4f}, L={L:>10d}, C/8={C/8:.4f}")
    else:
        print(f"  a={a:4d}: L={L:>10d} > 5M, skipped")

# k=5: consecutive quintuples (where feasible)
print("\nk=5 quintuples {a, ..., a+4}:")
for a in [3,4,5,7,8,9,10,11,13,15,17,19]:
    A = [a, a+1, a+2, a+3, a+4]
    if not is_primitive(A): continue
    C, L = compute_C_exact(A, max_L=10_000_000)
    if C is not None:
        print(f"  a={a:4d}: C={C:.4f}, L={L:>10d}, C/16={C/16:.4f}")
    else:
        print(f"  a={a:4d}: L={L:>10d} > 10M, skipped")

# Non-consecutive k=4 (worst from earlier search)
print("\nNon-consecutive k=4 (selected):")
for A in [[4,5,11,17], [8,9,11,13], [13,25,27,28], [13,27,28,29],
          [15,29,31,32], [17,18,19,37], [19,20,21,41], [28,29,30,31],
          [3,5,13,17], [4,5,6,14], [3,5,7,11]]:
    A = sorted(A)
    if not is_primitive(A): continue
    C, L = compute_C_exact(A)
    if C is not None:
        delta = density_ie(A)
        print(f"  {A}: C={C:.4f}, L={L}, delta={delta:.4f}, C/8={C/8:.4f}")
    else:
        print(f"  {A}: L={L} > 5M, skipped")

# Check: is C always < (a-1)*delta for some pattern?
print("\n\nPATTERN CHECK: C vs (a-1)*delta for consecutive triples")
for a in [3,5,7,10,13,20,30,50,75,100]:
    A = [a, a+1, a+2]
    if not is_primitive(A): continue
    C, L = compute_C_exact(A)
    if C is None: continue
    delta = density_ie(A)
    ratio = C / ((a-1)*delta) if delta > 0 else 0
    print(f"  a={a}: C={C:.4f}, (a-1)*delta={(a-1)*delta:.4f}, ratio={ratio:.4f}")

print("\nDONE.")
