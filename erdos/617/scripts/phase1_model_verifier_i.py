from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Literal


Kind = Literal["auto", "skeleton", "coloring"]


def _popcount(x: int) -> int:
    return x.bit_count()


def _norm_edge(u: int, v: int) -> tuple[int, int]:
    if u == v:
        raise ValueError(f"self-loop edge ({u}, {v})")
    return (u, v) if u < v else (v, u)


def _choose(n: int, k: int) -> int:
    return math.comb(n, k)


def _infer_n_from_edges(edges: Iterable[tuple[int, int]]) -> int:
    mx = -1
    for a, b in edges:
        mx = max(mx, a, b)
    if mx < 0:
        raise ValueError("cannot infer n from empty edge list")
    return mx + 1


def _edge_list(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def _build_adj_bitsets(n: int, edges: Iterable[tuple[int, int]]) -> list[int]:
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def _edges_in_subset(adj: list[int], subset: tuple[int, ...]) -> int:
    mask = 0
    for v in subset:
        mask |= 1 << v
    s = 0
    for v in subset:
        s += _popcount(adj[v] & mask)
    return s // 2


def _is_k_clique(adj: list[int], verts: tuple[int, ...]) -> bool:
    mask = 0
    for v in verts:
        mask |= 1 << v
    for v in verts:
        need = mask & ~(1 << v)
        if (adj[v] & mask) != need:
            return False
    return True


def _k5_cliques(adj: list[int], n: int, sample_limit: int) -> tuple[int, list[tuple[int, ...]]]:
    count = 0
    samples: list[tuple[int, ...]] = []
    for Q in itertools.combinations(range(n), 5):
        if _is_k_clique(adj, Q):
            count += 1
            if len(samples) < sample_limit:
                samples.append(Q)
    return count, samples


def _k5_star_violations(
    adj: list[int],
    n: int,
    sample_limit: int,
) -> tuple[int, int, list[dict[str, Any]]]:
    k5_cliques = 0
    violations = 0
    samples: list[dict[str, Any]] = []
    for Q in itertools.combinations(range(n), 5):
        if not _is_k_clique(adj, Q):
            continue
        k5_cliques += 1
        qmask = 0
        for u in Q:
            qmask |= 1 << u
        qset = set(Q)
        for v in range(n):
            if v in qset:
                continue
            deg = _popcount(adj[v] & qmask)
            if deg > 1:
                violations += 1
                if len(samples) < sample_limit:
                    samples.append({"clique": Q, "outside": v, "deg_into_clique": deg})
    return k5_cliques, violations, samples


@dataclass(frozen=True)
class SkeletonSpec:
    n: int
    min_edges: int | None
    max_edges: int | None
    subset_k: int
    subset_lower: int | None
    subset_upper: int | None
    omega_max: int | None
    check_k5_star: bool


def _verify_skeleton(edges: list[tuple[int, int]], spec: SkeletonSpec) -> dict[str, Any]:
    out: dict[str, Any] = {"kind": "skeleton", "n": spec.n}

    if spec.subset_k > spec.n:
        out["ok"] = False
        out["error"] = f"invalid parameters: subset_k={spec.subset_k} > n={spec.n}"
        return out

    seen = set()
    dupes = 0
    bad_edges: list[Any] = []
    for e in edges:
        if not (isinstance(e, tuple) and len(e) == 2):
            bad_edges.append(e)
            continue
        u, v = e
        if not (0 <= u < spec.n and 0 <= v < spec.n):
            bad_edges.append(e)
            continue
        if u == v:
            bad_edges.append(e)
            continue
        if e in seen:
            dupes += 1
        else:
            seen.add(e)

    out["edge_list_check"] = {
        "ok": not bad_edges and dupes == 0,
        "bad_edge_samples": bad_edges[:5],
        "duplicate_edges": dupes,
        "edges_reported": len(edges),
        "edges_unique": len(seen),
    }

    m = len(seen)
    if spec.min_edges is not None or spec.max_edges is not None:
        ok = True
        if spec.min_edges is not None and m < spec.min_edges:
            ok = False
        if spec.max_edges is not None and m > spec.max_edges:
            ok = False
        out["edge_count_check"] = {
            "ok": ok,
            "edge_count": m,
            "min_edges": spec.min_edges,
            "max_edges": spec.max_edges,
        }

    adj = _build_adj_bitsets(spec.n, seen)

    if spec.subset_lower is not None or spec.subset_upper is not None:
        vcount = 0
        samples: list[dict[str, Any]] = []
        min_seen = 10**9
        max_seen = -1
        for S in itertools.combinations(range(spec.n), spec.subset_k):
            c = _edges_in_subset(adj, S)
            min_seen = min(min_seen, c)
            max_seen = max(max_seen, c)
            if spec.subset_lower is not None and c < spec.subset_lower:
                vcount += 1
                if len(samples) < 5:
                    samples.append({"subset": S, "edge_count": c, "type": "lower"})
                continue
            if spec.subset_upper is not None and c > spec.subset_upper:
                vcount += 1
                if len(samples) < 5:
                    samples.append({"subset": S, "edge_count": c, "type": "upper"})
        out["subset_edgecount_check"] = {
            "ok": vcount == 0,
            "subset_k": spec.subset_k,
            "lower": spec.subset_lower,
            "upper": spec.subset_upper,
            "violations": vcount,
            "min_seen": min_seen if max_seen >= 0 else None,
            "max_seen": max_seen if max_seen >= 0 else None,
            "violation_samples": samples,
        }

    clique_samples: list[tuple[int, ...]] = []
    if spec.omega_max is not None and spec.omega_max < 5:
        k5_count, clique_samples = _k5_cliques(adj, spec.n, sample_limit=5)
        out["omega_check"] = {
            "ok": k5_count == 0,
            "omega_max": spec.omega_max,
            "k5_cliques_found": k5_count,
            "k5_samples": clique_samples,
        }

    if spec.check_k5_star:
        k5s, vcount, vsamples = _k5_star_violations(adj, spec.n, sample_limit=5)
        out["k5_star_check"] = {
            "ok": vcount == 0,
            "k5_cliques_found": k5s,
            "violations": vcount,
            "violation_samples": vsamples,
        }

    required = [
        out.get("edge_list_check", {}).get("ok", True),
        out.get("edge_count_check", {}).get("ok", True),
        out.get("subset_edgecount_check", {}).get("ok", True),
        out.get("omega_check", {}).get("ok", True),
        out.get("k5_star_check", {}).get("ok", True),
    ]
    out["ok"] = all(required)
    return out


def _parse_skeleton_json(data: Any, n: int | None) -> tuple[int, list[tuple[int, int]]]:
    edges_raw: Any

    if isinstance(data, list):
        edges_raw = data
    elif isinstance(data, dict):
        if "edges" in data:
            edges_raw = data["edges"]
        elif "model_edges" in data:
            edges_raw = data["model_edges"]
        else:
            raise ValueError("unrecognized skeleton JSON object (expected list or dict with 'edges')")
    else:
        raise ValueError("unrecognized skeleton JSON top-level (expected list or dict)")

    if not isinstance(edges_raw, list):
        raise ValueError("skeleton edges payload is not a list")

    edges: list[tuple[int, int]] = []
    for e in edges_raw:
        if not (isinstance(e, (list, tuple)) and len(e) == 2):
            raise ValueError(f"bad edge entry: {e!r}")
        u = int(e[0])
        v = int(e[1])
        edges.append(_norm_edge(u, v))

    if n is None:
        n = _infer_n_from_edges(edges)
    return n, edges


def _parse_coloring_json(data: Any, n: int | None, r: int | None) -> tuple[int, int, dict[tuple[int, int], int]]:
    rows: Any
    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict):
        if "coloring" in data:
            rows = data["coloring"]
        elif "edges" in data:
            rows = data["edges"]
        else:
            raise ValueError("unrecognized coloring JSON object (expected list or dict with 'coloring'/'edges')")
    else:
        raise ValueError("unrecognized coloring JSON top-level (expected list or dict)")

    if not isinstance(rows, list):
        raise ValueError("coloring payload is not a list")
    if not rows:
        raise ValueError("empty coloring list")

    edge_to_color: dict[tuple[int, int], int] = {}
    for row in rows:
        if isinstance(row, dict):
            if "edge" not in row or "color" not in row:
                raise ValueError(f"bad coloring row (expected keys edge/color): {row!r}")
            e = row["edge"]
            c = row["color"]
        elif isinstance(row, (list, tuple)) and len(row) == 3:
            e = [row[0], row[1]]
            c = row[2]
        else:
            raise ValueError(f"bad coloring row: {row!r}")

        if not (isinstance(e, (list, tuple)) and len(e) == 2):
            raise ValueError(f"bad edge in coloring row: {row!r}")
        u = int(e[0])
        v = int(e[1])
        edge = _norm_edge(u, v)
        col = int(c)
        if edge in edge_to_color:
            raise ValueError(f"duplicate edge in coloring: {edge}")
        edge_to_color[edge] = col

    if n is None:
        n = _infer_n_from_edges(edge_to_color.keys())
    if r is None:
        mx = max(edge_to_color.values())
        r = mx + 1

    return n, r, edge_to_color


def _verify_coloring(
    n: int,
    r: int,
    edge_to_color: dict[tuple[int, int], int],
    *,
    require_full_coverage: bool,
    subset_k: int,
    subset_upper: int | None,
    min_color_min_edges: int | None,
    min_color_max_edges: int | None,
    min_color_subset_lower: int | None,
    min_color_subset_upper: int | None,
    min_color_omega_max: int | None,
    check_k5_star: bool,
) -> dict[str, Any]:
    out: dict[str, Any] = {"kind": "coloring", "n": n, "r": r}

    if subset_k > n:
        out["ok"] = False
        out["error"] = f"invalid parameters: subset_k={subset_k} > n={n}"
        return out

    expected = n * (n - 1) // 2
    missing: list[tuple[int, int]] = []
    missing_count = 0
    for u, v in _edge_list(n):
        if (u, v) not in edge_to_color:
            missing_count += 1
            if len(missing) < 10:
                missing.append((u, v))
    extra_edges = []
    out_of_range_count = 0
    for e in edge_to_color.keys():
        u, v = e
        if not (0 <= u < n and 0 <= v < n):
            out_of_range_count += 1
            if len(extra_edges) < 10:
                extra_edges.append(e)
    complete_ok = (len(edge_to_color) == expected) and (not missing) and (not extra_edges)
    out["complete_edge_check"] = {
        "ok": complete_ok,
        "expected_edges": expected,
        "actual_edges": len(edge_to_color),
        "missing_edges": missing_count,
        "missing_edge_samples": missing,
        "out_of_range_edges": out_of_range_count,
        "out_of_range_edge_samples": extra_edges,
    }

    bad_colors = []
    counts = [0] * r
    for e, c in edge_to_color.items():
        if not (0 <= c < r):
            if len(bad_colors) < 10:
                bad_colors.append({"edge": e, "color": c})
            continue
        counts[c] += 1
    out["color_range_check"] = {"ok": not bad_colors, "bad_color_samples": bad_colors}
    out["global_color_counts"] = counts

    min_count = min(counts) if counts else None
    min_colors = [i for i, cc in enumerate(counts) if cc == min_count]
    out["min_color"] = {"min_edges": min_count, "colors": min_colors}

    # Build dense matrix for subset scans.
    mat = [[-1] * n for _ in range(n)]
    for (u, v), c in edge_to_color.items():
        if 0 <= u < n and 0 <= v < n:
            mat[u][v] = c
            mat[v][u] = c

    # Coverage / per-subset counts.
    bad_subset_samples: list[dict[str, Any]] = []
    bad_subsets = 0
    missing_total = 0
    upper_violations = 0
    upper_samples: list[dict[str, Any]] = []
    for S in itertools.combinations(range(n), subset_k):
        scounts = [0] * r
        for i, a in enumerate(S):
            row = mat[a]
            for b in S[i + 1 :]:
                c = row[b]
                if c < 0:
                    # Missing edge; let complete_edge_check surface it.
                    continue
                if 0 <= c < r:
                    scounts[c] += 1
        missing_here = [i for i, cc in enumerate(scounts) if cc == 0]
        if missing_here:
            bad_subsets += 1
            missing_total += len(missing_here)
            if len(bad_subset_samples) < 5:
                bad_subset_samples.append({"subset": S, "missing_colors": missing_here, "counts": scounts})
        if subset_upper is not None:
            too_high = [i for i, cc in enumerate(scounts) if cc > subset_upper]
            if too_high:
                upper_violations += 1
                if len(upper_samples) < 5:
                    upper_samples.append({"subset": S, "too_high_colors": too_high, "counts": scounts})
    out["coverage_check"] = {
        "ok": (bad_subsets == 0) if require_full_coverage else True,
        "subset_k": subset_k,
        "bad_subsets": bad_subsets,
        "missing_total": missing_total,
        "bad_subset_samples": bad_subset_samples,
    }
    if subset_upper is not None:
        out["subset_upper_check"] = {
            "ok": upper_violations == 0,
            "subset_k": subset_k,
            "upper": subset_upper,
            "violations": upper_violations,
            "violation_samples": upper_samples,
        }

    # Minimum-color skeleton checks (for each min color, if tied).
    min_checks: list[dict[str, Any]] = []
    for c in min_colors:
        edges_c = [e for e, col in edge_to_color.items() if col == c]
        spec = SkeletonSpec(
            n=n,
            min_edges=min_color_min_edges,
            max_edges=min_color_max_edges,
            subset_k=subset_k,
            subset_lower=min_color_subset_lower,
            subset_upper=min_color_subset_upper,
            omega_max=min_color_omega_max,
            check_k5_star=check_k5_star,
        )
        chk = _verify_skeleton(edges_c, spec)
        chk["color"] = c
        min_checks.append(chk)
    out["min_color_skeleton_checks"] = min_checks

    required_ok = [
        out["complete_edge_check"]["ok"],
        out["color_range_check"]["ok"],
        out.get("coverage_check", {}).get("ok", True),
        out.get("subset_upper_check", {}).get("ok", True),
    ]
    # If the caller asked for min-color derived constraints, enforce them.
    if min_color_min_edges is not None or min_color_max_edges is not None or min_color_omega_max is not None:
        required_ok.append(all(chk.get("ok", False) for chk in min_checks))
    out["ok"] = all(required_ok)
    return out


def _detect_kind(data: Any) -> Kind:
    if isinstance(data, list) and data:
        head = data[0]
        if isinstance(head, dict) and "edge" in head and "color" in head:
            return "coloring"
        if isinstance(head, (list, tuple)) and len(head) == 2:
            return "skeleton"
    if isinstance(data, dict):
        if "coloring" in data:
            return "coloring"
        if "edges" in data and isinstance(data["edges"], list) and data["edges"]:
            h = data["edges"][0]
            if isinstance(h, dict) and "edge" in h and "color" in h:
                return "coloring"
            if isinstance(h, (list, tuple)) and len(h) == 2:
                return "skeleton"
    return "skeleton"


def _maybe_deref_model_json(raw: Any, base_path: Path) -> tuple[Any, dict[str, Any] | None]:
    """If raw is a summary JSON pointing at a model file, load and return the model JSON."""
    if not isinstance(raw, dict):
        return raw, None
    for key in ("model_path", "model"):
        val = raw.get(key)
        if not isinstance(val, str) or not val:
            continue
        cand = Path(val)
        tried = []
        for p in (cand, base_path.parent / cand):
            tried.append(str(p))
            if p.exists() and p.is_file():
                model_raw = json.loads(p.read_text(encoding="utf-8"))
                return model_raw, {"deref_key": key, "deref_path": str(p), "tried": tried}
        return raw, {"deref_key": key, "deref_path": val, "tried": tried, "error": "path_not_found"}
    return raw, None


def main() -> int:
    parser = argparse.ArgumentParser(description="Phase 1 model verifier (Agent I).")
    parser.add_argument("inputs", nargs="+", type=Path, help="JSON model file(s) to verify.")
    parser.add_argument("--kind", choices=["auto", "skeleton", "coloring"], default="auto")
    parser.add_argument("--n", type=int, default=26)
    parser.add_argument("--r", type=int, default=5, help="Number of colors (for --kind coloring).")
    parser.add_argument("--out", type=Path, default=Path("erdos/617/results/phase1_i_verifier_checks.jsonl"))
    parser.add_argument("--overwrite", action="store_true", help="Overwrite --out instead of appending.")

    # Skeleton constraints (default to Phase 1 lemma).
    parser.add_argument("--min-edges", type=int, default=60)
    parser.add_argument("--max-edges", type=int, default=65)
    parser.add_argument("--subset-k", type=int, default=6)
    parser.add_argument("--subset-lower", type=int, default=1)
    parser.add_argument("--subset-upper", type=int, default=11)
    parser.add_argument("--omega-max", type=int, default=4)
    parser.add_argument("--check-k5-star", action="store_true", help="Verify K5-star projection (if K5s exist).")

    # Coloring coverage constraint.
    parser.add_argument(
        "--no-require-full-coverage",
        action="store_true",
        help="Do not fail overall if some (r+1)-set is missing a color.",
    )

    args = parser.parse_args()

    mode: Kind = args.kind  # type: ignore[assignment]
    out_path: Path = args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if args.overwrite:
        out_path.write_text("", encoding="utf-8")

    any_fail = False
    for p in args.inputs:
        raw0 = json.loads(p.read_text(encoding="utf-8"))
        raw, deref = _maybe_deref_model_json(raw0, p)
        k = _detect_kind(raw) if mode == "auto" else mode
        rec: dict[str, Any] = {
            "input": str(p),
            "requested_kind": mode,
            "detected_kind": k,
            "deref": deref,
            "settings": {
                "n": args.n,
                "r": args.r,
                "min_edges": args.min_edges,
                "max_edges": args.max_edges,
                "subset_k": args.subset_k,
                "subset_lower": args.subset_lower,
                "subset_upper": args.subset_upper,
                "omega_max": args.omega_max,
                "check_k5_star": bool(args.check_k5_star),
                "require_full_coverage": not args.no_require_full_coverage,
            },
        }
        try:
            if k == "skeleton":
                n, edges = _parse_skeleton_json(raw, n=args.n)
                spec = SkeletonSpec(
                    n=n,
                    min_edges=args.min_edges,
                    max_edges=args.max_edges,
                    subset_k=args.subset_k,
                    subset_lower=args.subset_lower,
                    subset_upper=args.subset_upper,
                    omega_max=args.omega_max,
                    check_k5_star=bool(args.check_k5_star),
                )
                rec["result"] = _verify_skeleton(edges, spec)
            elif k == "coloring":
                n, r, edge_to_color = _parse_coloring_json(raw, n=args.n, r=args.r)
                subset_k = args.subset_k
                if subset_k != r + 1:
                    # For the Erdos-Gyarfas "balanced" property, subset size is r+1.
                    subset_k = r + 1
                total_edges = subset_k * (subset_k - 1) // 2
                derived_upper = total_edges - (r - 1) if r >= 2 else None
                rec["result"] = _verify_coloring(
                    n=n,
                    r=r,
                    edge_to_color=edge_to_color,
                    require_full_coverage=not args.no_require_full_coverage,
                    subset_k=subset_k,
                    subset_upper=derived_upper,
                    min_color_min_edges=args.min_edges,
                    min_color_max_edges=args.max_edges,
                    min_color_subset_lower=args.subset_lower,
                    min_color_subset_upper=args.subset_upper,
                    min_color_omega_max=args.omega_max,
                    check_k5_star=bool(args.check_k5_star),
                )
            else:
                raise ValueError(f"unknown kind: {k}")
        except Exception as e:  # pragma: no cover
            rec["result"] = {"kind": k, "ok": False, "error": f"{type(e).__name__}: {e}"}

        any_fail = any_fail or (not rec.get("result", {}).get("ok", False))
        with out_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, sort_keys=True) + "\n")
            f.flush()
        print(json.dumps(rec, indent=2, sort_keys=True))

    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
