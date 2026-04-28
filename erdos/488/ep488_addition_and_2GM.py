"""
TASK 1: Element-addition conjecture — does ratio(A∪{c}) <= ratio(A) always?
TASK 4: Is 2G(M) > S1 for all primitive sets?
TASK 5: If not, at what n does 2G(n) first exceed S1?
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

def analyze(A, mult=20):
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
    S1 = sum(1.0/e for e in A)
    F_M = 0
    hit2 = bytearray(M + 1)
    for e in A:
        for m in range(e, M + 1, e):
            hit2[m] = 1
    F_M = sum(hit2)
    return {
        'k': k, 'a': a, 'M': M, 'S1': S1,
        'min': mn, 'max': mx,
        'ratio': mx/(2*mn) if mn > 0 else 999,
        'F_M': F_M, 'GM': F_M/M,
    }

def can_add(c, A):
    """Can c be added to A while keeping primitive?"""
    if c in A: return False
    for a in A:
        if c % a == 0 or a % c == 0:
            return False
    return True

# ============================================
# TASK 1: ELEMENT-ADDITION CONJECTURE
# ============================================
print("TASK 1: Does adding an element decrease the ratio?")
print("=" * 70)

violations = []
total = 0
t0 = time.time()

for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 50) if x % a1 != 0][:14]
    for tk in range(2, 7):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            r_A = analyze(A, mult=15)['ratio']
            # Try adding each possible c
            for c in range(2, max(A)):  # c < max(A)
                if not can_add(c, A): continue
                A_new = sorted(A + [c])
                if not is_primitive(A_new): continue
                r_new = analyze(A_new, mult=15)['ratio']
                total += 1
                if r_new > r_A + 1e-9:
                    violations.append((tuple(A), c, r_A, r_new, r_new - r_A))

elapsed = time.time() - t0
print(f"  Checked {total} (A, c) additions in {elapsed:.1f}s")
print(f"  Violations (r(A+c) > r(A)): {len(violations)}")

if violations:
    violations.sort(key=lambda x: -x[4])
    print(f"  Worst violations:")
    for A, c, r_A, r_new, excess in violations[:10]:
        print(f"    A={list(A)}, c={c}: r(A)={r_A:.5f}, r(A+c)={r_new:.5f}, excess=+{excess:.5f}")
    print(f"  Violation rate: {100*len(violations)/total:.2f}%")
else:
    print("  CONJECTURE HOLDS: every addition decreases or maintains ratio.")
sys.stdout.flush()

# ============================================
# TASK 4: 2G(M) > S1 for all primitive sets?
# ============================================
print("\n" + "=" * 70)
print("TASK 4: Is 2G(M) > S1 for all primitive sets?")
print("=" * 70)

fail_count = 0
fail_examples = []
total4 = 0
worst_deficit = 0

for a1 in range(2, 15):
    pool = [x for x in range(a1+1, 50) if x % a1 != 0][:16]
    for tk in range(2, 8):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total4 += 1
            r = analyze(A, mult=5)
            twoGM = 2 * r['GM']
            S1 = r['S1']
            if twoGM <= S1 + 1e-12:
                fail_count += 1
                deficit = S1 - twoGM
                if deficit > worst_deficit:
                    worst_deficit = deficit
                if len(fail_examples) < 20:
                    fail_examples.append((tuple(A), r['GM'], S1, twoGM, deficit))

print(f"  Checked {total4} primitive sets")
print(f"  Sets where 2G(M) <= S1: {fail_count}")
print(f"  Fraction: {100*fail_count/total4:.2f}%")
print(f"  Worst deficit: {worst_deficit:.6f}")
if fail_examples:
    print(f"  Examples:")
    for A, GM, S1, twoGM, deficit in fail_examples[:10]:
        print(f"    {list(A)}: G(M)={GM:.5f}, 2G(M)={twoGM:.5f}, S1={S1:.5f}, deficit={deficit:.5f}")
sys.stdout.flush()

# ============================================
# TASK 5: For failures, at what n does 2G(n) first exceed S1?
# ============================================
print("\n" + "=" * 70)
print("TASK 5: For sets where 2G(M)<=S1, find first n with 2G(n)>S1")
print("=" * 70)

def find_first_n(A, max_mult=50):
    M = max(A)
    S1 = sum(1.0/e for e in A)
    h_abs = max_mult * M
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    for x in range(M, h_abs + 1):
        run += hit[x]
        if 2*run/x > S1:
            return x, x/M
    return None, None

print("  For each failure: first n where 2G(n) > S1, and n/M ratio")
n_over_M_stats = []
for A, GM, S1, twoGM, deficit in fail_examples[:20]:
    A_list = list(A)
    n, ratio = find_first_n(A_list)
    if n is not None:
        n_over_M_stats.append(ratio)
        print(f"    {A_list}: first n={n}, n/M={ratio:.3f}")
    else:
        print(f"    {A_list}: NO n found in horizon")

if n_over_M_stats:
    print(f"\n  Statistics of n/M:")
    print(f"    Max: {max(n_over_M_stats):.3f}")
    print(f"    Avg: {sum(n_over_M_stats)/len(n_over_M_stats):.3f}")
    print(f"    Min: {min(n_over_M_stats):.3f}")
sys.stdout.flush()

# EXTENDED: check if there's a universal constant c such that 2G(n)>S1 by n = cM
print("\n" + "=" * 70)
print("EXTENDED: Find max(first_n/M) across ALL sets")
print("=" * 70)

max_n_over_M = 0
max_set = None
total5 = 0

for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 40) if x % a1 != 0][:14]
    for tk in range(2, 7):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total5 += 1
            n, r = find_first_n(A, max_mult=100)
            if r is not None and r > max_n_over_M:
                max_n_over_M = r
                max_set = tuple(A)

print(f"  Checked {total5} sets")
print(f"  Max n/M where 2G(n) first exceeds S1: {max_n_over_M:.3f} at {max_set}")
sys.stdout.flush()

print("\nDONE.")
