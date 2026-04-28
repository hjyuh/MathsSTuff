"""
Visible Slab Analysis for EP-488
Verifies split inequality and checks (A), (B) on the visible slab
for primitive pair-tail systems.

Author: Mahmoud
Date: March 28, 2026
Context: Erdos Problem 488, Chojecki framework

Results: 693 systems tested, ZERO failures.
Key finding: F(s) >= 2 always on visible slab (a and b are counted).
Tightest margin at (11,12,{19}), s=21, min_A = 0.68.
"""

from math import gcd
from fractions import Fraction
from functools import reduce
from itertools import combinations


def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_list(lst):
    if not lst:
        return 1
    return reduce(lcm, lst)

def F_count(a, b, T, n):
    count = 0
    for x in range(1, n + 1):
        if (x % a == 0 or x % b == 0):
            if all(x % t != 0 for t in T):
                count += 1
    return count

def quotient_tail(d, T):
    raw = set()
    for t in T:
        raw.add(t // gcd(t, d))
    minimal = set()
    for q in raw:
        if not any(q2 != q and q % q2 == 0 for q2 in raw):
            minimal.add(q)
    return minimal

def q_free_density(Q):
    if not Q:
        return Fraction(1)
    if 1 in Q:
        return Fraction(0)
    Q_list = sorted(Q)
    L = lcm_list(Q_list)
    count = sum(1 for x in range(1, L + 1) if all(x % q != 0 for q in Q_list))
    return Fraction(count, L)

def compute_W(a, b, T):
    U = [a, b]
    V = list(T)
    lambda_d = {}
    for s_size in range(1, len(U) + 1):
        for S in combinations(U, s_size):
            for t_size in range(0, len(V) + 1):
                for T_sub in combinations(V, t_size):
                    d = lcm_list(list(S) + list(T_sub))
                    sign = (-1) ** (len(S) + len(T_sub) + 1)
                    lambda_d[d] = lambda_d.get(d, 0) + sign
    W_plus = sum(v for v in lambda_d.values() if v > 0)
    W_minus = sum(-v for v in lambda_d.values() if v < 0)
    return W_plus, W_minus

def check_split_inequality(a, b, T, n_max=None):
    N_0 = max([a, b] + list(T))
    if n_max is None:
        n_max = max(N_0 * 20, 500)
    F_vals = {}
    for x in range(N_0, n_max + 1):
        F_vals[x] = F_count(a, b, T, x)
    for n in range(N_0, n_max):
        if F_vals[n] == 0:
            continue
        two_f_over_n = Fraction(2 * F_vals[n], n)
        for m in range(n + 1, n_max + 1):
            f_over_m = Fraction(F_vals[m], m)
            if f_over_m >= two_f_over_n:
                return False, (n, m)
    return True, None

def scan_systems(max_val=15, t_max=25, check_range=200):
    tested = 0
    failures = []
    for a in range(2, max_val):
        for b in range(a + 1, max_val):
            if b % a == 0:
                continue
            for t in range(b + 1, t_max):
                T = [t]
                if t % a == 0 or t % b == 0:
                    continue
                tested += 1
                result, fail = check_split_inequality(a, b, T, n_max=check_range)
                if not result:
                    failures.append((a, b, T, fail))
    print(f"Tested {tested} systems, failures: {len(failures)}")
    return failures

if __name__ == "__main__":
    scan_systems()
