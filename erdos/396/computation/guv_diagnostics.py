import argparse
import math
from collections import Counter, defaultdict


def divisors(n: int):
    ds = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return sorted(ds)


def analyze(X: int, d: int, q: int, eps_list):
    y = int(math.isqrt(2 * X))
    g_divs = divisors(abs(d))
    g_counts = Counter()
    g_H_mass = defaultdict(float)
    eps_counts = {eps: 0 for eps in eps_list}
    eps_H_mass = {eps: 0.0 for eps in eps_list}
    shell_counts = Counter()
    shell_H_mass = defaultdict(float)
    total_blocks = 0
    total_H_mass = 0.0

    for g in g_divs:
        U = (y - 1) // g
        for u in range(1, U + 1):
            for v in range(1, U + 1):
                if math.gcd(u, v) != 1:
                    continue
                Delta = math.gcd(q, g * u * v)
                H = (X * Delta) / (q * g * u * v)
                total_blocks += 1
                total_H_mass += H
                g_counts[g] += 1
                g_H_mass[g] += H

                for eps in eps_list:
                    if H >= X ** eps:
                        eps_counts[eps] += 1
                        eps_H_mass[eps] += H

                k = int(math.floor(math.log(max(H, 1e-300), 2.0)))
                shell_counts[k] += 1
                shell_H_mass[k] += H

    return {
        "X": X,
        "d": d,
        "q": q,
        "y": y,
        "total_blocks": total_blocks,
        "total_H_mass": total_H_mass,
        "g_counts": dict(g_counts),
        "g_H_mass": dict(g_H_mass),
        "eps_counts": eps_counts,
        "eps_H_mass": eps_H_mass,
        "shell_counts": dict(shell_counts),
        "shell_H_mass": dict(shell_H_mass),
    }


def render(result, eps_list):
    lines = []
    X = result["X"]
    d = result["d"]
    q = result["q"]
    lines.append(f"# (g,u,v) diagnostics")
    lines.append("")
    lines.append(f"X = {X}")
    lines.append(f"d = {d}")
    lines.append(f"q = {q}")
    lines.append(f"y = floor(sqrt(2X)) = {result['y']}")
    lines.append(f"total coprime blocks = {result['total_blocks']}")
    lines.append(f"total H-mass = {result['total_H_mass']:.6f}")
    lines.append("")
    lines.append("## By gcd type")
    for g in sorted(result["g_counts"]):
        lines.append(
            f"- g = {g}: blocks = {result['g_counts'][g]}, H-mass = {result['g_H_mass'][g]:.6f}"
        )
    lines.append("")
    lines.append("## Long-block thresholds")
    for eps in eps_list:
        lines.append(
            f"- eps = {eps}: blocks with H >= X^eps = {result['eps_counts'][eps]}, H-mass = {result['eps_H_mass'][eps]:.6f}"
        )
    lines.append("")
    lines.append("## Top H-shells by block count")
    top_shells = sorted(result["shell_counts"].items(), key=lambda kv: (-kv[1], -kv[0]))[:12]
    for k, c in top_shells:
        h_lo = 2 ** k
        h_hi = 2 ** (k + 1)
        lines.append(
            f"- 2^{k} <= H < 2^{k+1}  ({h_lo:.3g} to {h_hi:.3g}): blocks = {c}, H-mass = {result['shell_H_mass'][k]:.6f}"
        )
    lines.append("")
    lines.append("## Top H-shells by H-mass")
    top_mass = sorted(result["shell_H_mass"].items(), key=lambda kv: (-kv[1], -kv[0]))[:12]
    for k, mass in top_mass:
        h_lo = 2 ** k
        h_hi = 2 ** (k + 1)
        lines.append(
            f"- 2^{k} <= H < 2^{k+1}  ({h_lo:.3g} to {h_hi:.3g}): H-mass = {mass:.6f}, blocks = {result['shell_counts'][k]}"
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--X", type=int, required=True)
    parser.add_argument("--d", type=int, required=True)
    parser.add_argument("--q", type=int, default=1)
    parser.add_argument("--eps", nargs="*", type=float, default=[0.2, 0.3, 0.4])
    args = parser.parse_args()
    result = analyze(args.X, args.d, args.q, args.eps)
    print(render(result, args.eps))


if __name__ == "__main__":
    main()