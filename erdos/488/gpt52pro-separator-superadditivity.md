# EP-488: 5.2 Pro — Separator Superadditivity (PROVED)
## April 8, 2026

## NEW PROVED THEOREM: Separator Superadditivity

If A = A₁ ∪ A₂, S = A₁ ∩ A₂, and lcm(a,b) > n for all
a ∈ A₁\S, b ∈ A₂\S, then:

  B(A) ≥ B(A₁) + B(A₂) - B(S)

Proof:
- At n: overlap is exactly U_S(n) (cross-pairs n-disconnected)
  → F_A(n) = F_{A₁}(n) + F_{A₂}(n) - F_S(n)
- At m: overlap ≥ U_S(m) (at least the separator's multiples)
  → F_A(m) ≤ F_{A₁}(m) + F_{A₂}(m) - F_S(m)
- Combine: B(A) ≥ B(A₁) + B(A₂) - B(S). ∎

## HIERARCHY OF SPECIAL CASES

| Separator S | B(S) correction | Source |
|-------------|----------------|--------|
| S = ∅ | B(∅) = 0 | Original superadditivity |
| S = {c} | B({c}) = T(c) | Articulation superadditivity (5.4) |
| S = {u,v} | T(u)+T(v)-T(lcm(u,v)) | NEW: 2-separator inequality |
| General S | B(S) explicit from IE | NEW: full separator theorem |

## WHY THIS MATTERS: SPQR DECOMPOSITION

Biconnected blocks can be decomposed along 2-vertex separators
into "SPQR atoms":
- R-nodes: 3-connected primitive nuclei
- S-nodes: cycle-type nuclei  
- P-nodes: parallel-pair nuclei

The separator superadditivity gives the EXACT gluing formula:
  B(block) ≥ Σ B(atoms) - Σ B(separator pairs)

Since pair budgets B({u,v}) are explicit and already-understood,
the problem reduces to: prove each SPQR atom has budget ≥ its
share of separator corrections.

## THE SHARP NEXT TARGET

For each SPQR atom X with terminal pair {u,v}:
  Prove B(X) ≥ B({u,v})

This would make the SPQR gluing automatically positive.

## KILL COUNT: 77
## PERCENTAGE: 90%

Up from 89%. Separator superadditivity is a strict generalization
of both original superadditivity and articulation superadditivity.
It opens the door to SPQR decomposition of biconnected blocks,
reducing the problem to 3-connected nuclei + explicit pair corrections.
