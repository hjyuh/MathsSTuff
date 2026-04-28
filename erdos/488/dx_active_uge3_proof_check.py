"""
EP-488 / D(x) triple case support script.

This script is intentionally *core-level*: it works with the compressed
coprime core (u,v,q0) and checks the "run-end" inequality in the form

  D~(M)/M <= 2*D~(N)/(N+1)

which is the hardest g->infty specialization of the operator

  D~(M)/M <= 2*D~(N)/(N+1-1/g),  g>=2.

Rationale:
  - In the remaining regime, gcd(a,b)=g>=2 and N >= lcm(u,v)=u*v.
  - Using N+1 instead of N+1-1/g makes the RHS smaller, so it's the
    conservative inequality to test.

The goal is to support a hybrid proof strategy:
  1) Prove a general density/discrepancy lemma:
       D~(Y) is within O(1) of rho*Y, where rho is the exact density.
  2) Use that lemma to close all large-N cases automatically.
  3) Brute-check the finite leftover small-N region.

This script implements step (3) and prints the first violating witness
(if any) in a minimal, copy-pastable form.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import ceil, gcd
from typing import Iterable, Optional, Tuple

import dx_triple_check as dx


def _delta(u: int, v: int) -> Fraction:
    # gcd(u,v)=1 in coprime cores, so lcm(u,v)=u*v.
    return Fraction(1, u) + Fraction(1, v) - Fraction(1, u * v)


def rho(u: int, v: int, q0: int) -> Fraction:
    """
    Exact density of D~ for the periodic set:
      { y : (u|y or v|y) and q0 ∤ y }.

    With (u',v') = (u/gcd(u,q0), v/gcd(v,q0)):
      rho = delta(u,v) - delta(u',v')/q0.
    """
    up, vp = dx.uv_prime(u, v, q0)
    return _delta(u, v) - _delta(up, vp) / q0


def rhs_bound(u: int, v: int, q0: int, N: int) -> Fraction:
    Dn = dx.D_tilde(u, v, q0, N)
    if Dn <= 0:
        return Fraction(0, 1)
    return 2 * Fraction(Dn, 1) / Fraction(N + 1, 1)


def lhs(u: int, v: int, q0: int, M: int) -> Fraction:
    return Fraction(dx.D_tilde(u, v, q0, M), M)


@dataclass(frozen=True)
class Witness:
    u: int
    v: int
    q0: int
    N: int
    M: int
    Dn: int
    Dm: int
    lhs: Fraction
    rhs: Fraction
    rho: Fraction


def find_violation_for_fixed_N(*, u: int, v: int, q0: int, N: int) -> Optional[Witness]:
    """
    Check all M >= max(N+1, q0) up to the point where the universal
    upper bound

      D~(M)/M <= rho + 4/M

    guarantees safety.
    """
    Dn = dx.D_tilde(u, v, q0, N)
    if Dn <= 0:
        return None
    rhs = 2 * Fraction(Dn, 1) / Fraction(N + 1, 1)

    r = rho(u, v, q0)
    if rhs <= r:
        # If rhs <= rho, then asymptotically D~(M)/M -> rho would force a
        # violation for large M. We have not seen this happen for N>=uv;
        # treat it as an explicit red-flag.
        raise RuntimeError(f"unexpected rhs<=rho: (u,v,q0,N)=({u},{v},{q0},{N}) rho={r} rhs={rhs}")

    start_M = max(N + 1, q0)

    # For M >= ceil(4/(rhs-rho)), we have rho + 4/M <= rhs, hence safe.
    M0 = ceil(Fraction(4, 1) / (rhs - r))
    stop_M_excl = max(start_M, M0) + 1

    for M in range(start_M, stop_M_excl):
        Dm = dx.D_tilde(u, v, q0, M)
        L = Fraction(Dm, M)
        if L > rhs:
            return Witness(
                u=u,
                v=v,
                q0=q0,
                N=N,
                M=M,
                Dn=Dn,
                Dm=Dm,
                lhs=L,
                rhs=rhs,
                rho=r,
            )
    return None


def iter_coprime_pairs(*, u_min: int, u_max: int, v_max: int) -> Iterable[Tuple[int, int]]:
    for u in range(u_min, u_max + 1):
        for v in range(u + 1, v_max + 1):
            if gcd(u, v) == 1:
                yield u, v


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--u", type=int, default=0, help="check a single u (with --v)")
    ap.add_argument("--v", type=int, default=0, help="check a single v (with --u)")
    ap.add_argument("--u-max", type=int, default=10, help="max u when sweeping")
    ap.add_argument("--v-max", type=int, default=15, help="max v when sweeping")
    ap.add_argument("--q0-max", type=int, default=200, help="max q0 (q0 ranges from v+1..min(q0_max, N))")
    ap.add_argument("--N-max", type=int, default=200, help="max N to brute check (N ranges from u*v..N_max)")
    args = ap.parse_args()

    pairs: Iterable[Tuple[int, int]]
    if args.u and args.v:
        pairs = [(args.u, args.v)]
    else:
        pairs = iter_coprime_pairs(u_min=3, u_max=args.u_max, v_max=args.v_max)

    checked = 0
    for (u, v) in pairs:
        if u < 3 or v <= u or gcd(u, v) != 1:
            continue
        uv = u * v
        for N in range(uv, max(args.N_max, uv) + 1):
            q0_hi = min(args.q0_max, N)
            for q0 in range(v + 1, q0_hi + 1):
                checked += 1
                w = find_violation_for_fixed_N(u=u, v=v, q0=q0, N=N)
                if w is not None:
                    print("VIOLATION FOUND")
                    print(f"(u,v,q0)=({w.u},{w.v},{w.q0})")
                    print(f"(N,M)=({w.N},{w.M})")
                    print(f"D~(N)={w.Dn}, D~(M)={w.Dm}")
                    print(f"rho={w.rho} ~= {float(w.rho):.12f}")
                    print(f"lhs=D~(M)/M={w.lhs} ~= {float(w.lhs):.12f}")
                    print(f"rhs=2D~(N)/(N+1)={w.rhs} ~= {float(w.rhs):.12f}")
                    raise SystemExit(1)

    print("no violations in brute box")
    print(f"checked parameter tuples (u,v,q0,N) = {checked}")


if __name__ == "__main__":
    main()

