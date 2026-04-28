#!/usr/bin/env python3
"""
EP-488 v31 Path 1: primitive triple case miner for the D(x) two-point inequality.

For a primitive triple Q={a,b,q} with q=max(Q), define

  D(x) := #{ t <= x : q does NOT divide t, and (a|t or b|t) }.

The D(x) inequality is:

  D(m)/m <= 2*D(n)/n  for all integers m > n >= q.

For |Q|=3, inclusion-exclusion gives:

  2*D(n)/n - D(m)/m = B_a(n,m) + B_b(n,m) - B_{a,b}(n,m),

where each B-term is a paired floor-difference:

  B_d(n,m) := 2*(floor(n/d) - floor(n/lcm(d,q)))/n
             - (floor(m/d) - floor(m/lcm(d,q)))/m.

This script is evidence/diagnostic tooling, not a proof.

Notes:
  - Uses the run-end extremizer restriction by default (Lemma A):
      n at end of D-uncovered run, m at end of D-covered run.
    This is safe for finding violations and for locating worst ratios.
  - Supports regime filters:
      --regime proved: only n with lcm(a,b) > n (the easy/proved triple regime)
      --regime open:   only n with lcm(a,b) <= n (the remaining triple regime)
  - Supports exclusion filters on the coprime-core compression:
      --exclusion inert:  q0 > floor(m/g)  (q0 exclusion is inactive up to M)
      --exclusion active: q0 <= floor(m/g) (q0 exclusion can matter at m)
  - Windows console encoding can be cp1252; avoid unicode in output.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, List, Optional, Tuple


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def is_primitive_triple(a: int, b: int, q: int) -> bool:
    if not (2 <= a < b < q):
        return False
    # Primitive antichain: no divisibility.
    if b % a == 0:
        return False
    if q % a == 0 or q % b == 0:
        return False
    return True


def coprime_core(a: int, b: int, q: int) -> Tuple[int, int, int, int, int]:
    """
    Return the coprime core decomposition for a triple {a,b,q}:
      g = gcd(a,b), a = g*u, b = g*v with gcd(u,v)=1,
      h = gcd(g,q), q = h*q0 (so gcd(g/h, q0)=1).

    The compression identity is:
      D_{a,b,q}(x) = Dtilde_{u,v,q0}(floor(x/g)).
    """
    g = gcd(a, b)
    u = a // g
    v = b // g
    if u > v:
        u, v = v, u
    h = gcd(g, q)
    q0 = q // h
    return g, u, v, h, q0


def delta_single(r: int, q0: int, x: int) -> int:
    return x // r - x // lcm(r, q0)


def delta_pair(u: int, v: int, q0: int, x: int) -> int:
    uv = lcm(u, v)
    return x // uv - x // lcm(uv, q0)


def D_tilde(u: int, v: int, q0: int, x: int) -> int:
    return delta_single(u, q0, x) + delta_single(v, q0, x) - delta_pair(u, v, q0, x)


def C_uv(u: int, v: int, x: int) -> int:
    """Count y<=x with (u|y or v|y)."""
    return x // u + x // v - x // lcm(u, v)


def uv_prime(u: int, v: int, q0: int) -> Tuple[int, int]:
    du = gcd(u, q0)
    dv = gcd(v, q0)
    return u // du, v // dv


def D_tilde_decomp(u: int, v: int, q0: int, x: int) -> int:
    """
    Active-exclusion decomposition:
      D~(x) = C_{u,v}(x) - C_{u',v'}(floor(x/q0)),
    where u' = u/gcd(u,q0), v' = v/gcd(v,q0).
    This holds for all x (when x<q0, the correction term is 0).
    """
    up, vp = uv_prime(u, v, q0)
    return C_uv(u, v, x) - C_uv(up, vp, x // q0)


def frac_ge(num1: int, den1: int, num2: int, den2: int) -> bool:
    """Return (num1/den1) >= (num2/den2) for positive denominators."""
    return num1 * den2 >= num2 * den1


def build_D_and_E(a: int, b: int, q: int, Bmax: int) -> Tuple[List[int], List[bool]]:
    """
    Return (D, E) where:
      - D[x] = D(x) for x=0..Bmax+1
      - E[x] = 1 iff x is counted (divisible by a or b, and not by q)
    We compute through Bmax+1 to support run-end eligibility tests.
    """
    D = [0] * (Bmax + 2)
    E = [False] * (Bmax + 2)
    s = 0
    for x in range(1, Bmax + 2):
        hit = (x % q != 0) and (x % a == 0 or x % b == 0)
        E[x] = hit
        if hit:
            s += 1
        D[x] = s
    return D, E


@dataclass(frozen=True)
class WorstCase:
    a: int
    b: int
    q: int
    n: int
    m: int
    Dn: int
    Dm: int
    # ratio = (D(m)/m) / (2*D(n)/n) = ratio_num/ratio_den
    ratio_num: int
    ratio_den: int
    # margin = 2*D(n)/n - D(m)/m = margin_num/margin_den
    margin_num: int
    margin_den: int

    def ratio(self) -> Fraction:
        return Fraction(self.ratio_num, self.ratio_den)

    def margin(self) -> Fraction:
        return Fraction(self.margin_num, self.margin_den)


def analyze_triple(
    a: int,
    b: int,
    q: int,
    *,
    Bmult: int,
    use_run_ends: bool,
    regime: str,
    exclusion: str,
) -> Optional[WorstCase]:
    """
    Analyze the triple on the window:
      q <= n < m <= Bmult*q.

    Returns the (n,m) attaining the worst ratio (closest to violation)
    under the suffix-argmax strategy.
    """
    if not is_primitive_triple(a, b, q):
        return None
    Bmax = Bmult * q
    if Bmax <= q:
        raise ValueError("Need Bmult*q > q so that m>n is possible.")

    D, E = build_D_and_E(a, b, q, Bmax)
    lab = lcm(a, b)
    g, u, v, h, q0 = coprime_core(a, b, q)

    if regime not in ("all", "open", "proved"):
        raise ValueError("regime must be one of: all, open, proved")
    if exclusion not in ("all", "active", "inert"):
        raise ValueError("exclusion must be one of: all, active, inert")

    n_lo = q
    n_hi = Bmax - 1
    if regime == "open":
        n_lo = max(n_lo, lab)  # lcm(a,b) <= n
    elif regime == "proved":
        n_hi = min(n_hi, lab - 1)  # lcm(a,b) > n
    if n_lo > n_hi:
        return None

    eligible_n = [True] * (Bmax + 2)
    eligible_m = [True] * (Bmax + 2)
    if use_run_ends:
        # n: end of uncovered run (E[n]=0, E[n+1]=1)
        # m: end of covered run   (E[m]=1, E[m+1]=0)
        for x in range(1, Bmax + 1):
            eligible_n[x] = (not E[x]) and E[x + 1]
            eligible_m[x] = E[x] and (not E[x + 1])

    if exclusion != "all":
        # Active/inert is defined on the compressed M=floor(m/g) (for run-end m, M=m/g).
        for x in range(1, Bmax + 1):
            if not eligible_m[x]:
                continue
            active = (x // g) >= q0
            if exclusion == "active" and not active:
                eligible_m[x] = False
            if exclusion == "inert" and active:
                eligible_m[x] = False

    # Suffix argmax of D(m)/m over eligible m.
    best_m_from = [0] * (Bmax + 3)
    has_best = False
    best_m = Bmax
    for m in range(Bmax, 0, -1):
        if eligible_m[m]:
            best_m = m
            has_best = True
            break
    if not has_best:
        return None

    for i in range(Bmax, 0, -1):
        if eligible_m[i]:
            # Tie-break to smaller m (scan descending, so update on equality).
            if frac_ge(D[i], i, D[best_m], best_m):
                best_m = i
        best_m_from[i] = best_m

    worst: WorstCase | None = None

    for n in range(n_lo, n_hi + 1):
        if use_run_ends and not eligible_n[n]:
            continue
        Dn = D[n]
        if Dn == 0:
            continue
        m = best_m_from[n + 1]
        if m <= n:
            continue
        Dm = D[m]

        # ratio = Dm/m / (2*Dn/n) = (Dm*n) / (2*Dn*m)
        ratio_num = Dm * n
        ratio_den = 2 * Dn * m
        # margin = 2*Dn/n - Dm/m = (2*Dn*m - Dm*n)/(n*m)
        margin_num = 2 * Dn * m - Dm * n
        margin_den = n * m

        # Violation check.
        if margin_num < 0:
            # Still return it as the "worst" case for reporting.
            g1 = gcd(abs(ratio_num), abs(ratio_den))
            g2 = gcd(abs(margin_num), abs(margin_den))
            return WorstCase(
                a=a,
                b=b,
                q=q,
                n=n,
                m=m,
                Dn=Dn,
                Dm=Dm,
                ratio_num=ratio_num // g1,
                ratio_den=ratio_den // g1,
                margin_num=margin_num // g2,
                margin_den=margin_den // g2,
            )

        if worst is None or ratio_num * worst.ratio_den > worst.ratio_num * ratio_den:
            g1 = gcd(ratio_num, ratio_den)
            g2 = gcd(margin_num, margin_den)
            worst = WorstCase(
                a=a,
                b=b,
                q=q,
                n=n,
                m=m,
                Dn=Dn,
                Dm=Dm,
                ratio_num=ratio_num // g1,
                ratio_den=ratio_den // g1,
                margin_num=margin_num // g2,
                margin_den=margin_den // g2,
            )
    return worst


def B_term(d: int, q: int, n: int, m: int) -> Fraction:
    Dd = lcm(d, q)
    En = n // d - n // Dd
    Em = m // d - m // Dd
    return Fraction(2 * En, n) - Fraction(Em, m)


def B_ab_term(a: int, b: int, q: int, n: int, m: int) -> Fraction:
    dab = lcm(a, b)
    Dab = lcm(dab, q)
    En = n // dab - n // Dab
    Em = m // dab - m // Dab
    return Fraction(2 * En, n) - Fraction(Em, m)


def print_one(w: WorstCase, *, Bmult: int) -> None:
    print("=" * 80)
    print("Primitive triple D(x) inequality: worst-case window witness")
    print("=" * 80)
    print(f"Q = [{w.a}, {w.b}, {w.q}] (q=max(Q)={w.q})")
    print(f"window: q <= n < m <= {w.q}*{Bmult}")
    g, u, v, h, q0 = coprime_core(w.a, w.b, w.q)
    lab = lcm(w.a, w.b)
    regime_at_n = "PROVED (lcm>n)" if lab > w.n else "OPEN (lcm<=n)"
    N = w.n // g
    M = w.m // g
    ex = "ACTIVE (q0<=M)" if q0 <= M else "INERT (q0>M)"
    print(f"lcm(a,b) = {lab} ; regime at n: {regime_at_n}")
    print(f"core: gcd(a,b)=g={g}, (u,v)=({u},{v}) with gcd(u,v)=1, q0=q/gcd(g,q)={q0} (h={h})")
    Dn_t = D_tilde(u, v, q0, N)
    Dm_t = D_tilde(u, v, q0, M)
    print(f"compressed: floor(n/g)=N={N}, floor(m/g)=M={M} [{ex}] ; D~(N)={Dn_t}, D~(M)={Dm_t}")
    # Run-end form uses denominator n/g = N+1-1/g (since n=gN+g-1), m/g = M (since m is a hit).
    denomN = Fraction(g * (N + 1) - 1, g)  # = N + 1 - 1/g
    if M > 0 and Dn_t > 0:
        core_ratio = Fraction(Dm_t, M) / (2 * Fraction(Dn_t, 1) / denomN)
        core_margin = 2 * Fraction(Dn_t, 1) / denomN - Fraction(Dm_t, M)
        # Note: core_margin = g * (2D(n)/n - D(m)/m).
        print(f"core-run-end ratio (D~(M)/M) / (2D~(N)/(N+1-1/g)) = {core_ratio} = {float(core_ratio):.12f}")
        print(f"core-run-end margin 2D~(N)/(N+1-1/g) - D~(M)/M = {core_margin} = {float(core_margin):.12f}")

    # Verify active-exclusion decomposition when q0 is in range.
    Dn_dec = D_tilde_decomp(u, v, q0, N)
    Dm_dec = D_tilde_decomp(u, v, q0, M)
    if Dn_dec != Dn_t or Dm_dec != Dm_t:
        print("WARNING: D~ decomposition mismatch (this indicates a bug).")
    if q0 <= M:
        up, vp = uv_prime(u, v, q0)
        print(f"decomp: (u',v')=({up},{vp}), floor(N/q0)={N//q0}, floor(M/q0)={M//q0}")
        print(f"  D~(N)=C_uv(N)-C_u'v'(floor(N/q0)) = {C_uv(u,v,N)} - {C_uv(up,vp,N//q0)} = {Dn_dec}")
        print(f"  D~(M)=C_uv(M)-C_u'v'(floor(M/q0)) = {C_uv(u,v,M)} - {C_uv(up,vp,M//q0)} = {Dm_dec}")
    print()
    print(f"worst (n,m) = ({w.n}, {w.m})")
    print(f"D(n)={w.Dn}, D(m)={w.Dm}")
    print(f"ratio = (D(m)/m) / (2*D(n)/n) = {w.ratio_num}/{w.ratio_den} = {float(w.ratio()):.12f}")
    print(
        f"margin = 2*D(n)/n - D(m)/m = {w.margin_num}/{w.margin_den} = {float(w.margin()):.12f}"
    )
    print()

    Ba = B_term(w.a, w.q, w.n, w.m)
    Bb = B_term(w.b, w.q, w.n, w.m)
    Bab = B_ab_term(w.a, w.b, w.q, w.n, w.m)
    total = Ba + Bb - Bab
    print("B-terms at the witness (exact):")
    print(f"  B_a     = {Ba} = {float(Ba):.12f}")
    print(f"  B_b     = {Bb} = {float(Bb):.12f}")
    print(f"  B_a,b   = {Bab} = {float(Bab):.12f}")
    print(f"  total   = B_a + B_b - B_a,b = {total} = {float(total):.12f}")


def scan_triples(
    *,
    qmax: int,
    Bmult: int,
    top_k: int,
    use_run_ends: bool,
    regime: str,
    top_cores: int,
    exclusion: str,
    min_u: int,
    top_window_only: bool,
) -> None:
    if qmax < 4:
        raise SystemExit("Need qmax >= 4 to have any triples.")
    if Bmult < 2:
        raise SystemExit("Need Bmult >= 2.")

    checked = 0
    analyzed = 0
    violations = 0
    best: WorstCase | None = None
    best_margin: WorstCase | None = None
    top: List[WorstCase] = []
    core_best: dict[tuple[int, int, int], WorstCase] = {}

    for q in range(4, qmax + 1):
        for a in range(2, q - 1):
            for b in range(a + 1, q):
                if not is_primitive_triple(a, b, q):
                    continue
                if top_window_only and (2 * a <= q or 2 * b <= q):
                    continue
                g, u, v, h, q0 = coprime_core(a, b, q)
                if u < min_u:
                    continue
                checked += 1
                w = analyze_triple(
                    a,
                    b,
                    q,
                    Bmult=Bmult,
                    use_run_ends=use_run_ends,
                    regime=regime,
                    exclusion=exclusion,
                )
                if w is None:
                    continue
                analyzed += 1
                if w.margin_num < 0:
                    violations += 1
                    print(
                        f"VIOLATION: Q=[{w.a},{w.b},{w.q}] n={w.n} m={w.m} "
                        f"Dn={w.Dn} Dm={w.Dm} ratio={w.ratio_num}/{w.ratio_den}"
                    )
                    continue

                if best is None or w.ratio_num * best.ratio_den > best.ratio_num * w.ratio_den:
                    best = w
                if best_margin is None or w.margin_num * best_margin.margin_den < best_margin.margin_num * w.margin_den:
                    best_margin = w

                # Maintain a small top-k list by ratio (descending).
                if top_k > 0:
                    top.append(w)
                    top.sort(key=lambda x: Fraction(x.ratio_num, x.ratio_den), reverse=True)
                    if len(top) > top_k:
                        top = top[:top_k]

                if top_cores > 0:
                    key = (u, v, q0)
                    prev = core_best.get(key)
                    if prev is None or w.margin_num * prev.margin_den < prev.margin_num * w.margin_den:
                        core_best[key] = w

        if q % 10 == 0:
            print(f"...scanned up to q={q}, triples checked={checked}, violations={violations}")

    print()
    print("=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"qmax={qmax}, window: q <= n < m <= {Bmult}q")
    print(f"use_run_ends={'ON' if use_run_ends else 'OFF'}")
    print(f"regime={regime}")
    print(f"exclusion={exclusion}")
    print(f"min_u={min_u}")
    print(f"top_window_only={'ON' if top_window_only else 'OFF'}")
    print(f"primitive triples checked: {checked}")
    if analyzed != checked:
        print(f"triples with nonempty n-range under regime: {analyzed}")
    print(f"violations found: {violations}")

    if best is not None:
        print()
        print("Worst ratio (closest to violation):")
        lab = lcm(best.a, best.b)
        regime_at_n = "PROVED(lcm>n)" if lab > best.n else "OPEN(lcm<=n)"
        g, u, v, h, q0 = coprime_core(best.a, best.b, best.q)
        print(
            f"  Q=[{best.a},{best.b},{best.q}]  (n,m)=({best.n},{best.m})  "
            f"Dn={best.Dn} Dm={best.Dm}  "
            f"ratio={best.ratio_num}/{best.ratio_den}={float(best.ratio()):.12f}  "
            f"margin={best.margin_num}/{best.margin_den}={float(best.margin()):.12f}  "
            f"lcm(a,b)={lab} [{regime_at_n}]  core(g,u,v,q0)=({g},{u},{v},{q0})"
        )

    if best_margin is not None:
        print()
        print("Smallest margin (within scanned windows):")
        lab = lcm(best_margin.a, best_margin.b)
        regime_at_n = "PROVED(lcm>n)" if lab > best_margin.n else "OPEN(lcm<=n)"
        g, u, v, h, q0 = coprime_core(best_margin.a, best_margin.b, best_margin.q)
        print(
            f"  Q=[{best_margin.a},{best_margin.b},{best_margin.q}]  (n,m)=({best_margin.n},{best_margin.m})  "
            f"Dn={best_margin.Dn} Dm={best_margin.Dm}  "
            f"margin={best_margin.margin_num}/{best_margin.margin_den}={float(best_margin.margin()):.12f}  "
            f"ratio={best_margin.ratio_num}/{best_margin.ratio_den}={float(best_margin.ratio()):.12f}  "
            f"lcm(a,b)={lab} [{regime_at_n}]  core(g,u,v,q0)=({g},{u},{v},{q0})"
        )

    if top:
        print()
        print(f"Top {len(top)} by ratio:")
        for w in top:
            lab = lcm(w.a, w.b)
            regime_at_n = "PROVED" if lab > w.n else "OPEN"
            g, u, v, h, q0 = coprime_core(w.a, w.b, w.q)
            print(
                f"  Q=[{w.a},{w.b},{w.q}]  (n,m)=({w.n},{w.m})  "
                f"ratio={w.ratio_num}/{w.ratio_den}={float(w.ratio()):.6f}  "
                f"margin={float(w.margin()):.6f}  "
                f"lcm(a,b)={lab} [{regime_at_n}]  core(g,u,v,q0)=({g},{u},{v},{q0})"
            )

    if top_cores > 0 and core_best:
        print()
        print(f"Top {min(top_cores, len(core_best))} coprime cores by smallest margin:")
        items = list(core_best.items())
        items.sort(key=lambda kv: Fraction(kv[1].margin_num, kv[1].margin_den))
        for (u, v, q0), w in items[:top_cores]:
            g, _, _, h, _ = coprime_core(w.a, w.b, w.q)
            N = w.n // g
            uv = u * v  # coprime core => lcm(u,v)=uv
            print(
                f"  core(u,v,q0)=({u},{v},{q0})  uv={uv}  witness Q=[{w.a},{w.b},{w.q}] "
                f"(g={g},h={h}) (n,m)=({w.n},{w.m}) floor(n/g)={N}  "
                f"margin={w.margin_num}/{w.margin_den}={float(w.margin()):.6f}"
            )


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    p_one = sub.add_parser("one", help="analyze one primitive triple")
    p_one.add_argument("--a", type=int, required=True)
    p_one.add_argument("--b", type=int, required=True)
    p_one.add_argument("--q", type=int, required=True)
    p_one.add_argument("--Bmult", type=int, default=10, help="window size: m <= Bmult*q")
    p_one.add_argument("--no-run-ends", action="store_true", help="disable run-end restriction")
    p_one.add_argument(
        "--exclusion",
        choices=["all", "active", "inert"],
        default="all",
        help="restrict m by q0 vs floor(m/g) (active: q0<=M, inert: q0>M)",
    )
    p_one.add_argument(
        "--regime",
        choices=["all", "open", "proved"],
        default="all",
        help="restrict n by lcm(a,b) vs n (open: lcm<=n, proved: lcm>n)",
    )

    p_scan = sub.add_parser("scan", help="scan all primitive triples with q<=qmax")
    p_scan.add_argument("--qmax", type=int, default=50)
    p_scan.add_argument("--Bmult", type=int, default=10, help="window size: m <= Bmult*q")
    p_scan.add_argument("--top", type=int, default=10, help="print top-k tight cases by ratio")
    p_scan.add_argument("--top-cores", type=int, default=0, help="print top-k coprime cores by smallest margin")
    p_scan.add_argument("--min-u", type=int, default=2, help="restrict to coprime cores with u >= this value")
    p_scan.add_argument("--top-window-only", action="store_true", help="restrict to triples with a,b in (q/2,q]")
    p_scan.add_argument("--no-run-ends", action="store_true", help="disable run-end restriction")
    p_scan.add_argument(
        "--exclusion",
        choices=["all", "active", "inert"],
        default="all",
        help="restrict m by q0 vs floor(m/g) (active: q0<=M, inert: q0>M)",
    )
    p_scan.add_argument(
        "--regime",
        choices=["all", "open", "proved"],
        default="all",
        help="restrict n by lcm(a,b) vs n (open: lcm<=n, proved: lcm>n)",
    )

    args = p.parse_args()

    if args.cmd == "one":
        w = analyze_triple(
            args.a,
            args.b,
            args.q,
            Bmult=args.Bmult,
            use_run_ends=not args.no_run_ends,
            regime=args.regime,
            exclusion=args.exclusion,
        )
        if w is None:
            raise SystemExit("Not a primitive triple (need 2<=a<b<q and no divisibility).")
        print_one(w, Bmult=args.Bmult)
        if w.margin_num < 0:
            raise SystemExit("\nWARNING: inequality violated in the search window.")
        return

    if args.cmd == "scan":
        scan_triples(
            qmax=args.qmax,
            Bmult=args.Bmult,
            top_k=args.top,
            use_run_ends=not args.no_run_ends,
            regime=args.regime,
            top_cores=args.top_cores,
            exclusion=args.exclusion,
            min_u=args.min_u,
            top_window_only=args.top_window_only,
        )


if __name__ == "__main__":
    main()
