#!/usr/bin/env python3
"""Finite certificates for v79 smooth-frontier motif representatives."""

from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction

from ep488_v58_full_component_census import finite_certificate


def certify_representatives(input_json: str, max_cutoff: int) -> dict[str, object]:
    data = json.load(open(input_json, encoding="utf-8"))
    rows = []
    status_counts: dict[str, int] = {}
    for index, motif in enumerate(data["motifs"], start=1):
        rep = motif["representative"]
        cert = finite_certificate(
            tuple(int(x) for x in rep["C"]),
            int(rep["q"]),
            int(rep["n"]),
            int(rep["D_n"]),
            max_cutoff,
        )
        status = str(cert["status"])
        status_counts[status] = status_counts.get(status, 0) + 1
        rows.append(
            {
                "index": index,
                "size": motif["size"],
                "q": rep["q"],
                "n": rep["n"],
                "epsilon_values": motif["epsilon_values"],
                "normalized_C": motif["normalized_C"],
                "status": status,
                "B": cert.get("B"),
                "delta": cert.get("delta"),
                "eta": cert.get("eta"),
                "E": cert.get("E"),
                "terms": cert.get("terms"),
                "cutoff": cert.get("cutoff"),
                "best": cert.get("best"),
                "best_over_B": cert.get("best_over_B"),
                "failures": cert.get("failures"),
            }
        )

    certified = [row for row in rows if row["status"] == "certified" and row["best_over_B"]]
    certified.sort(key=lambda row: Fraction(str(row["best_over_B"])), reverse=True)
    return {
        "source": input_json,
        "max_cutoff": max_cutoff,
        "motif_count": len(data["motifs"]),
        "status_counts": status_counts,
        "top_certified_by_best_over_B": certified[:20],
        "representatives": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", default="ep488_v79_a2_smooth_motif_frontier_q10000.json")
    parser.add_argument("--max-cutoff", type=int, default=10_000_000)
    parser.add_argument("--json-out", default="ep488_v79_a2_smooth_motif_representative_certs_q10000.json")
    args = parser.parse_args()

    start = time.time()
    result = certify_representatives(args.input_json, args.max_cutoff)
    result["elapsed_seconds"] = time.time() - start
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"motifs={result['motif_count']} status={result['status_counts']} "
        f"elapsed_seconds={result['elapsed_seconds']:.2f}"
    )
    for row in result["top_certified_by_best_over_B"][:10]:
        print(
            f"best_over_B={row['best_over_B']} q={row['q']} n={row['n']} "
            f"size={row['size']} eps={row['epsilon_values']} cutoff={row['cutoff']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
