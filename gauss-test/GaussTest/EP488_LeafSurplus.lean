import Mathlib.Tactic

/-- Given the four defining identities (ε = c - τ), (|E| = |Λ| + 2τ),
    (|Λ| - |C| = (x_3 - x_1 - τ)/2), (c = |E| - |C| + 1),
    conclude 2ε = 2 + x_3 - x_1 + τ.
    For Nat-safety, we state the doubled form to avoid division. -/
theorem leaf_surplus_identity
    (eps c tau E Lambda Csize x3 x1 : ℤ)
    (h_eps : eps = c - tau)
    (h_edge : E = Lambda + 2 * tau)
    (h_branch : 2 * (Lambda - Csize) = x3 - x1 - tau)
    (h_cyclo : c = E - Csize + 1) :
    2 * eps = 2 + x3 - x1 + tau := by
  omega
