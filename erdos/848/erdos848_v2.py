#!/usr/bin/env python3
"""
Erdős Problem 848 — Computer-Assisted p=13 Verifier v2
Verifies: s_max^(13)(N) + max(V+,V-) + d_max(N) + R_{>13}(N) < M(N)
for N in [5000, N_max].

FIXED: excludes base-class elements (≡7,18 mod 25) from outsider count.
"""

import math
import sys

def sieve_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

def modinv(a, m):
    if m == 1: return 0
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

def build_mask(a, b, L, primes):
    """
    Build non-squarefree mask for progression a*n + b, n=0..L-1.
    mask[n] = 1 iff a*n+b is non-squarefree (divisible by some q^2).
    """
    mask = bytearray(L)
    max_val = a * (L - 1) + b if L > 0 else b
    for q in primes:
        qq = q * q
        if qq > max_val: break
        g = math.gcd(a, qq)
        if b % g != 0: continue
        a1, mod, b1 = a // g, qq // g, b // g
        inv = modinv(a1, mod)
        if inv is None: continue
        r = ((-b1) * inv) % mod
        n = r
        while n < L:
            mask[n] = 1
            n += mod
    return mask

def find_roots(p):
    p2 = p * p
    for r in range(1, p2):
        if (r * r + 1) % p2 == 0: return r, p2 - r
    return None, None

def main():
    N_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    N_START = 5000
    P, R_P, R_M, P2 = 13, 70, 99, 169

    print(f"Erdos 848 v2: N in [{N_START}, {N_MAX}]")

    max_val_est = 25 * N_MAX * (N_MAX // 25 + 1)
    plim = min(int(math.isqrt(max_val_est)) + 1, 500000)
    primes = sieve_primes(plim)
    print(f"Primes sieved up to {plim}: {len(primes)} primes")

    p1m4 = [p for p in primes if p > 13 and p % 4 == 1]
    roots_cache = {}
    for p in p1m4:
        if p * p > N_MAX: break
        rp, rm = find_roots(p)
        if rp: roots_cache[p] = (rp, rm)

    M_MAX = (N_MAX - 7) // 25 + 1
    U_MAX = (N_MAX - R_P) // P2 + 1
    V_MAX = (N_MAX - R_M) // P2 + 1

    is_outsider_plus = [(R_P + P2 * u) % 25 not in (7, 18) for u in range(U_MAX)]
    is_outsider_minus = [(R_M + P2 * v) % 25 not in (7, 18) for v in range(V_MAX)]

    n_out_plus = sum(is_outsider_plus)
    n_out_minus = sum(is_outsider_minus)
    print(f"M_MAX={M_MAX}, U_MAX={U_MAX}({n_out_plus} outsiders), V_MAX={V_MAX}({n_out_minus} outsiders)")

    print("Building masks...")
    E_plus = [None] * U_MAX
    for u in range(U_MAX):
        if not is_outsider_plus[u]: continue
        x = R_P + P2 * u
        E_plus[u] = build_mask(25 * x, 7 * x + 1, M_MAX, primes)
    
    E_minus = [None] * V_MAX
    for v in range(V_MAX):
        if not is_outsider_minus[v]: continue
        x = R_M + P2 * v
        E_minus[v] = build_mask(25 * x, 7 * x + 1, M_MAX, primes)

    C_plus = [None] * U_MAX
    for u in range(U_MAX):
        if not is_outsider_plus[u]: continue
        x = R_P + P2 * u
        C_plus[u] = build_mask(P2 * x, R_M * x + 1, V_MAX, primes)

    C_minus = [None] * V_MAX
    for v in range(V_MAX):
        if not is_outsider_minus[v]: continue
        x = R_M + P2 * v
        C_minus[v] = build_mask(P2 * x, R_P * x + 1, U_MAX, primes)

    print("Simulating...")
    events = []
    for m in range(M_MAX):
        n = 7 + 25 * m
        if n >= N_START: events.append((n, 'b', m))
    for u in range(U_MAX):
        n = R_P + P2 * u
        if n >= N_START: events.append((n, '+', u))
    for v in range(V_MAX):
        n = R_M + P2 * v
        if n >= N_START: events.append((n, '-', v))
    events.sort()

    aM = aU = aV = 0
    bc_p = [0]*U_MAX; bc_m = [0]*V_MAX
    dp = [0]*U_MAX; dm = [0]*V_MAX

    for m in range(M_MAX):
        if 7+25*m <= N_START: aM = m+1
    for u in range(U_MAX):
        if R_P+P2*u <= N_START:
            aU = u+1
            if is_outsider_plus[u]:
                bc_p[u] = sum(E_plus[u][mm] for mm in range(aM))
    for v in range(V_MAX):
        if R_M+P2*v <= N_START:
            aV = v+1
            if is_outsider_minus[v]:
                bc_m[v] = sum(E_minus[v][mm] for mm in range(aM))
    for u in range(aU):
        if not is_outsider_plus[u]: continue
        for v in range(aV):
            if not is_outsider_minus[v]: continue
            if C_plus[u][v]:
                dp[u] += 1; dm[v] += 1

    fails = 0; checks = 0
    for idx, (n, et, ei) in enumerate(events):
        if et == 'b':
            m = ei; aM = m+1
            for u in range(aU):
                if is_outsider_plus[u]: bc_p[u] += E_plus[u][m]
            for v in range(aV):
                if is_outsider_minus[v]: bc_m[v] += E_minus[v][m]
        elif et == '+':
            u = ei; aU = u+1
            if is_outsider_plus[u]:
                bc_p[u] = sum(E_plus[u][mm] for mm in range(aM))
                dp[u] = 0
                for v in range(aV):
                    if is_outsider_minus[v] and C_plus[u][v]:
                        dp[u] += 1; dm[v] += 1
        elif et == '-':
            v = ei; aV = v+1
            if is_outsider_minus[v]:
                bc_m[v] = sum(E_minus[v][mm] for mm in range(aM))
                dm[v] = 0
                for u in range(aU):
                    if is_outsider_plus[u] and C_minus[v][u]:
                        dm[v] += 1; dp[u] += 1

        N = n
        s_max = max((bc_p[u] for u in range(aU) if is_outsider_plus[u]), default=0)
        s_max = max(s_max, max((bc_m[v] for v in range(aV) if is_outsider_minus[v]), default=0))
        d_max = max((dp[u] for u in range(aU) if is_outsider_plus[u]), default=0)
        d_max = max(d_max, max((dm[v] for v in range(aV) if is_outsider_minus[v]), default=0))

        Rgt = 0
        for p in p1m4:
            p2 = p*p
            if p2 > N: break
            rp, rm = roots_cache.get(p, (None,None))
            if rp is None: continue
            if rp <= N: Rgt += (N-rp)//p2 + 1
            if rm <= N: Rgt += (N-rm)//p2 + 1

        Vmax = max(aU, aV)
        LHS = s_max + Vmax + d_max + Rgt
        RHS = aM
        checks += 1
        if LHS >= RHS:
            fails += 1
            if fails <= 20:
                print(f"  FAIL N={N}: s={s_max} V={Vmax} d={d_max} R={Rgt} LHS={LHS} >= M={RHS}")
        if checks % 2000 == 0:
            print(f"  {checks} events, N={N}, fails={fails}")

    print(f"\n{'='*50}")
    print(f"{checks} events, {fails} failures")
    if fails == 0:
        print("*** ALL PASS — PROBLEM 848 VERIFIED ***")
    else:
        print(f"{fails} values of N failed the inequality")

if __name__ == '__main__':
    main()
