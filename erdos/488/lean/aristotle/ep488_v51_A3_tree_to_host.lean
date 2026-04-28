-- EP-488 v51 / A3: Tree-to-unicyclic-host stripping (5.4-β)
--
-- For any spanning tree T of G_n under n < 3q: triple fibers are
-- vertex-disjoint {12d, 15d, 20d} triangles (machine-verified in the v46
-- package). T omits at least one edge from each triangle. Delete one omitted
-- edge per triangle to get G_T. Then T ⊆ G_T, G_T is connected, and
-- c(G_T) = c(G_n) - τ_n = ε_n.
--
-- When ε_n = 1: every spanning tree of G_n lives inside a connected
-- unicyclic host.
--
-- This is the reduction lemma that lets the analytic CML target be
-- specialized from "arbitrary ε_n ≤ 1 components" to "spanning trees of
-- connected unicyclic top-window graphs."
--
-- ================================================================
-- NOTE ON FORMALIZATION STRATEGY
-- ================================================================
-- We state the lemma abstractly in terms of a simple graph G, a set of
-- pairwise vertex-disjoint triangles Triples, and a spanning tree T ⊆ G.
-- The EP-488-specific content (that triple fibers in B_n really are such
-- vertex-disjoint triangles) is a separate lemma from the v46 package.
--
-- Key facts we use:
-- (i)   Each triangle in Triples contributes exactly 3 edges to G.
-- (ii)  Pairwise vertex-disjoint triangles don't share edges either.
-- (iii) A spanning tree T has no cycles, so T omits ≥ 1 edge from each
--       triangle.
-- (iv)  For each triangle, pick a canonical edge not in T and delete it.
--       The resulting subgraph G' is still connected (since T ⊆ G') and
--       c(G') = c(G) - |Triples|.
--
-- We prove a skeleton of the lemma with the connectivity + cyclomatic
-- reduction as the core step.

import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Acyclic
import Mathlib.Combinatorics.SimpleGraph.Connectivity
import Mathlib.Tactic

namespace EP488.TreeToHost

open SimpleGraph Finset

variable {V : Type*} [DecidableEq V] [Fintype V]

/-- A triangle in a graph G is a 3-element subset of V such that all three
    pairs are edges of G. -/
structure GraphTriangle (G : SimpleGraph V) where
  verts : Finset V
  card_eq : verts.card = 3
  all_adj : ∀ u ∈ verts, ∀ v ∈ verts, u ≠ v → G.Adj u v

/-- Two triangles are vertex-disjoint if their vertex sets are disjoint. -/
def VertexDisjoint {G : SimpleGraph V} (t1 t2 : GraphTriangle G) : Prop :=
  Disjoint t1.verts t2.verts

/-- A family of pairwise vertex-disjoint triangles. -/
structure DisjointTriangleFamily (G : SimpleGraph V) where
  triangles : Finset (GraphTriangle G)
  pairwise_disjoint : ∀ t1 ∈ triangles, ∀ t2 ∈ triangles, t1 ≠ t2 → VertexDisjoint t1 t2

/-- For a spanning tree T of G and a triangle in G, T omits at least one
    edge of the triangle (because T is acyclic and a triangle is a 3-cycle). -/
theorem spanning_tree_omits_triangle_edge
    {G : SimpleGraph V} (T : Subgraph G) (hT_span : T.IsSpanning)
    (hT_acyclic : (T.coe).IsAcyclic)
    (t : GraphTriangle G) :
    ∃ u ∈ t.verts, ∃ v ∈ t.verts, u ≠ v ∧ ¬ T.Adj u v := by
  sorry

/-- MAIN SKELETON.
    Given G with a family F of pairwise vertex-disjoint triangles, and any
    spanning tree T ⊆ G, there exists a subgraph G' with T ⊆ G' ⊆ G, G'
    connected, and |edges(G')| = |edges(G)| - |F|.
    Since cyclomatic number = |edges| - |verts| + (# components), and G and
    G' have the same vertex set and both are connected (1 component), we get
    c(G') = c(G) - |F|. -/
theorem tree_to_unicyclic_host
    (G : SimpleGraph V) (hG_conn : G.Connected)
    (F : DisjointTriangleFamily G)
    (T : Subgraph G) (hT_span : T.IsSpanning)
    (hT_acyclic : (T.coe).IsAcyclic) :
    ∃ G' : SimpleGraph V,
      G' ≤ G ∧
      G'.Connected ∧
      (∀ u v, T.Adj u v → G'.Adj u v) ∧
      G'.edgeFinset.card = G.edgeFinset.card - F.triangles.card := by
  sorry

/-- COROLLARY.
    When ε_n = 1 (meaning in the EP-488 setting c(G) - τ = 1, i.e.,
    |edges(G)| - |verts| + 1 - |F| = 1), the resulting host G' has
    c(G') = 1, i.e., G' is connected unicyclic. -/
theorem unicyclic_host_when_epsilon_one
    (G : SimpleGraph V) (hG_conn : G.Connected)
    (F : DisjointTriangleFamily G)
    (T : Subgraph G) (hT_span : T.IsSpanning)
    (hT_acyclic : (T.coe).IsAcyclic)
    (h_eps_one : G.edgeFinset.card - Fintype.card V + 1 - F.triangles.card = 1) :
    ∃ G' : SimpleGraph V,
      G' ≤ G ∧
      G'.Connected ∧
      (∀ u v, T.Adj u v → G'.Adj u v) ∧
      G'.edgeFinset.card - Fintype.card V + 1 = 1 := by
  sorry

end EP488.TreeToHost
