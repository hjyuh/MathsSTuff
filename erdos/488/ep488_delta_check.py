"""Check: Delta_3 >= Delta_2 + Delta_4 where Delta_j = S_j(lcm) - S_j(product)."""
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

def compute_Sj_both(A, j):
    """Compute S_j using lcm and using product."""
    s_lcm = 0.0
    s_prod = 0.0
    for combo in combinations(A, j):
        l = combo[0]
        p = combo[0]
        for c in combo[1:]:
            l = lcm2(l, c)
            p *= c
        s_lcm += 1.0 / l
        s_prod += 1.0 / p
    return s_lcm, s_prod

# Check for non-coprime primitive sets
print("Delta_j = S_j(lcm) - S_j(product) analysis")
print("Need: Delta_3 >= Delta_2 + Delta_4")
print("=" * 60)

violations = 0
count = 0
for tk in range(4, 8):
    me = min(25, 6 + 3*tk)
    vk = 0
    for a1 in range(2, min(10, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:12]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            # Skip coprime (all deltas = 0)
            if all(gcd(A[i],A[j])==1 for i in range(len(A)) for j in range(i+1,len(A))):
                continue
            count += 1

            s2l, s2p = compute_Sj_both(A, 2)
            s3l, s3p = compute_Sj_both(A, 3)
            D2 = s2l - s2p
            D3 = s3l - s3p
            D4 = 0.0
            if tk >= 4:
                s4l, s4p = compute_Sj_both(A, 4)
                D4 = s4l - s4p

            ok = D3 >= D2 + D4 - 1e-12
            if not ok:
                vk += 1
                violations += 1
                if violations <= 10:
                    S1 = sum(1.0/a for a in A)
                    # Also compute actual Bonf-4 vs coprime Bonf-4
                    bonf4_lcm = S1 - s2l + s3l - (s4l if tk>=4 else 0)
                    bonf4_prod = S1 - s2p + s3p - (s4p if tk>=4 else 0)
                    print(f"  k={tk} VIOLATION: {A}")
                    print(f"    D2={D2:.6f}, D3={D3:.6f}, D4={D4:.6f}")
                    print(f"    D3-(D2+D4)={D3-D2-D4:.6f}")
                    print(f"    Bonf4(lcm)={bonf4_lcm:.6f}, Bonf4(prod)={bonf4_prod:.6f}")
                    print(f"    S1/2={S1/2:.6f}, Bonf4(lcm) > S1/2: {bonf4_lcm > S1/2}")

    print(f"  k={tk}: {count} non-coprime sets, Delta_3 >= Delta_2+Delta_4 violations: {vk}")

# Even if D3 >= D2+D4 fails, does Bonf4(lcm) > S1/2 still hold?
print("\nDirect check: Bonf4(lcm) > S1/2 for all primitive sets")
print("=" * 60)
for tk in range(4, 8):
    me = min(25, 6 + 3*tk)
    fail = 0
    cnt = 0
    for a1 in range(2, min(10, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:12]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            cnt += 1
            S1 = sum(1.0/a for a in A)
            s2l, _ = compute_Sj_both(A, 2)
            s3l, _ = compute_Sj_both(A, 3)
            s4l = compute_Sj_both(A, 4)[0] if tk >= 4 else 0
            bonf4 = S1 - s2l + s3l - s4l
            if bonf4 <= S1/2 + 1e-12:
                fail += 1
    print(f"  k={tk}: {cnt} sets, Bonf4 <= S1/2: {fail}")

print("\nDONE.")
