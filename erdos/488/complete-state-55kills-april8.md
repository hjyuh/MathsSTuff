# EP-488: Complete State — April 8, 2026 Evening
## 90%. Two days of work. 77 kills. 35+ proved results.

## CONVERGENCE: Two independent proofs of Separator Superadditivity

5.2 and 5.4 independently proved the same theorem:

If A = A₁ ∪ A₂, K = A₁ ∩ A₂, lcm(x,y) > n for x ∈ A₁\K, y ∈ A₂\K:
  B(A) ≥ B(A₁) + B(A₂) - B(K)

5.4 additionally:
- Verified with explicit biconnected example ({5,8,9,12}, 4-cycle)
- Identified the frontier as "separator-tight atoms" not just biconnected blocks
- Confirmed path-pruning failure still blocks naive internal deletion

## THE COMPLETE DECOMPOSITION CHAIN

| Level | Tool | Proved by | Reduces to |
|-------|------|-----------|-----------|
| 0 | Superadditivity (K=∅) | 5.2 (v7) | Connected components |
| 1 | Articulation (K={c}) | 5.4 (v9.1) | Biconnected blocks |
| 2 | Leaf-pruning | 5.2 (v9.1) | 2-core |
| 3 | Dominated-LCM pruning | 5.2 (v9.1) | Quotient-antichain 2-core |
| 4 | Separator (K={u,v}+) | 5.2+5.4 (v9.2) | Separator-tight atoms |

Additionally:
- Single-obstruction safety (Codex B): bad layers need ≥ 2 obstructions
- Literal-2 safety (5.4): components with literal 2 are safe
- Lifted {2,3}-core safety (3 models): dB with 2,3∈B always safe
- Split-core tripod safety (Codex B): {2u,3v,uv} always safe (also corollary of leaf-pruning)

## THE REMAINING 10%

After the full decomposition chain, a minimal counterexample is a
SEPARATOR-TIGHT ATOM: a primitive set whose n-LCM graph cannot be
decomposed further by any separator where B(side) ≥ B(separator).

Properties of such an atom:
1. Every vertex has degree ≥ 2 (leaf-pruning)
2. Every vertex has incomparable quotient set (dominated-LCM)
3. Every vertex has ≥ 2 independent obstructions (single-obstruction safety)
4. No literal 2 (literal-2 safety)
5. Connected, biconnected, separator-tight
6. Primitive
7. Budget ≤ 0

SEVEN simultaneous constraints. Zero computational violations.

The question: can such an object exist?

## KILL COUNT: 77
## PERCENTAGE: 90%
