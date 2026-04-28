from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


def parse_ints(spec: str | None) -> list[int]:
    if not spec:
        return []
    return [int(x.strip()) for x in spec.replace("\n", ",").split(",") if x.strip()]


def is_square(n: int) -> int | None:
    if n < 0:
        return None
    r = math.isqrt(n)
    return r if r * r == n else None


def factor_pair(n: int, d: int) -> tuple[int, int] | None:
    disc = d * d + 4 * n
    s = is_square(disc)
    if s is None or (s - d) % 2:
        return None
    a = (s - d) // 2
    b = a + d
    if a <= 0 or a * b != n:
        return None
    return a, b


def verify(ns: list[int], deltas: list[int]) -> dict:
    matrix = []
    ok = True
    for n in ns:
        rels = []
        for d in deltas:
            pair = factor_pair(n, d)
            if pair is None:
                ok = False
                rels.append({"delta": d, "ok": False})
            else:
                a, b = pair
                rels.append({"delta": d, "ok": True, "a": a, "b": b})
        matrix.append({"n": n, "relations": rels})
    return {
        "ok": ok,
        "num_N": len(ns),
        "num_deltas": len(deltas),
        "N_values": ns,
        "deltas": deltas,
        "matrix": matrix,
    }


def load_seed(path: Path) -> tuple[list[int], list[int]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(map(int, data["N_values"])), list(map(int, data["deltas"]))


def scan_ordered_rows(rows: tuple[int, int, int, int], p_max: int) -> dict:
    d1, d2, d3, d4 = rows
    a_const = d1 * d1 - d2 * d2
    b_const = d1 * d1 - d3 * d3
    k_const = d4 * d4 - d1 * d1
    deltas_scaled_by_l: dict[int, set[int]] = {}
    records = []

    for p in range(1, p_max + 1):
        p2 = p * p
        q3 = p2 * p2 + (2 * a_const - 4 * b_const) * p2 + a_const * a_const
        q4 = p2 * p2 + (2 * a_const + 4 * k_const) * p2 + a_const * a_const
        s3 = is_square(q3)
        if s3 is None:
            continue
        s4 = is_square(q4)
        if s4 is None:
            continue

        # With L=2p, N' = L^2 * ((lambda - d1^2) / 4).
        n_scaled = ((p2 + a_const) * (p2 + a_const)) // 4 - p2 * d1 * d1
        if n_scaled <= 0:
            continue
        # The numerator above should be integral for valid parity; skip if not.
        if ((p2 + a_const) * (p2 + a_const)) % 4:
            continue
        l_scale = 2 * p
        scaled_rows = tuple(sorted(l_scale * d for d in rows))
        cert = verify([n_scaled], list(scaled_rows))
        if not cert["ok"]:
            continue
        deltas_scaled_by_l.setdefault(l_scale, set()).add(n_scaled)
        records.append(
            {
                "p": p,
                "L": l_scale,
                "ordered_rows": list(rows),
                "scaled_deltas": list(scaled_rows),
                "N": n_scaled,
                "sqrt_Q3": s3,
                "sqrt_Q4": s4,
            }
        )

    grouped = []
    for l_scale, ns in sorted(deltas_scaled_by_l.items()):
        scaled_deltas = tuple(sorted(l_scale * d for d in rows))
        grouped.append(
            {
                "L": l_scale,
                "scaled_deltas": list(scaled_deltas),
                "N_count": len(ns),
                "N_values": sorted(ns)[:20],
                "is_K44_candidate": len(ns) >= 4,
            }
        )
    return {
        "ordered_rows": list(rows),
        "A": a_const,
        "B": b_const,
        "K": k_const,
        "hit_count": len(records),
        "hits": records[:100],
        "groups": grouped,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Integer p-scan for EP885 K44 quartic model.")
    parser.add_argument("--seed", required=True)
    parser.add_argument("--rows", help="Optional comma-separated rows; defaults to seed deltas.")
    parser.add_argument("--p-max", type=int, required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    _, seed_rows = load_seed(Path(args.seed))
    rows = parse_ints(args.rows) or seed_rows
    if len(rows) != 4:
        raise SystemExit("this scanner expects exactly four rows")

    reports = [scan_ordered_rows(tuple(order), args.p_max) for order in itertools.permutations(rows, 4)]
    k44 = []
    for report in reports:
        for group in report["groups"]:
            if group["is_K44_candidate"]:
                k44.append({"ordered_rows": report["ordered_rows"], **group})

    result = {
        "seed": args.seed,
        "rows": rows,
        "p_max": args.p_max,
        "ordered_case_count": len(reports),
        "total_hit_count": sum(r["hit_count"] for r in reports),
        "k44_candidate_count": len(k44),
        "k44_candidates": k44,
        "reports": reports,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "p_max": args.p_max,
                "total_hit_count": result["total_hit_count"],
                "k44_candidate_count": len(k44),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
