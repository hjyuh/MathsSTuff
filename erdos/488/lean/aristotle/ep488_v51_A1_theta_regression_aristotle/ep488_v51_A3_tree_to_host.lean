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

import Mathlib

set_option maxHeartbeats 800000

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
  contrapose! hT_acyclic with hT_not_acyclic
  simp_all +decide [SimpleGraph.isAcyclic_iff_forall_adj_isBridge]
  obtain ⟨u, v, w, h⟩ := Finset.card_eq_three.mp t.card_eq
  use u, by aesop, v, by aesop, by aesop
  simp_all +decide [SimpleGraph.isBridge_iff, SimpleGraph.Subgraph.Adj]
  have h_path : SimpleGraph.Reachable
      (T.coe \ SimpleGraph.fromEdgeSet {s(⟨u, by aesop⟩, ⟨v, by aesop⟩)})
      ⟨u, by aesop⟩ ⟨w, by aesop⟩ ∧
    SimpleGraph.Reachable
      (T.coe \ SimpleGraph.fromEdgeSet {s(⟨u, by aesop⟩, ⟨v, by aesop⟩)})
      ⟨w, by aesop⟩ ⟨v, by aesop⟩ := by
    constructor <;> refine' SimpleGraph.Adj.reachable _ <;> aesop
  exact h_path.1.trans h_path.2

/-- If two triangles are vertex-disjoint, their edges are distinct. -/
lemma vertex_disjoint_imp_edge_disjoint {G : SimpleGraph V}
    (t1 t2 : GraphTriangle G) (h_disj : VertexDisjoint t1 t2)
    (u1 v1 : V) (hu1 : u1 ∈ t1.verts) (hv1 : v1 ∈ t1.verts)
    (u2 v2 : V) (hu2 : u2 ∈ t2.verts) (hv2 : v2 ∈ t2.verts)
    (hne1 : u1 ≠ v1) (hne2 : u2 ≠ v2) :
    s(u1, v1) ≠ s(u2, v2) := by
  simp_all +decide [Finset.disjoint_left, VertexDisjoint]
  grind

/-
Deleting edges from a connected graph preserves connectivity when each
    deleted edge has a bypass: an alternative 2-path through some vertex w
    whose bypass edges are not deleted.
-/
lemma connected_deleteEdges_of_bypass
    {G : SimpleGraph V} (hG_conn : G.Connected)
    (S : Set (Sym2 V))
    (hS_bypass : ∀ u v, s(u, v) ∈ S → ∃ w, G.Adj u w ∧ G.Adj w v ∧
      s(u, w) ∉ S ∧ s(w, v) ∉ S) :
    (G.deleteEdges S).Connected := by
  -- Let's choose any two vertices u and v in V.
  have h_connected : ∀ u v : V, G.Reachable u v → (G.deleteEdges S).Reachable u v := by
    intro u v huv
    induction' huv with u v huv ih;
    induction' u with u v huv ih;
    · exact SimpleGraph.Reachable.refl _;
    · by_cases h : s(v, huv) ∈ S;
      · obtain ⟨ w, hw₁, hw₂, hw₃, hw₄ ⟩ := hS_bypass v huv h;
        exact SimpleGraph.Reachable.trans ( SimpleGraph.Adj.reachable ( by aesop ) ) ( SimpleGraph.Adj.reachable ( by aesop ) |> SimpleGraph.Reachable.trans <| by assumption );
      · exact SimpleGraph.Reachable.trans ( SimpleGraph.Adj.reachable ( by aesop ) ) ‹_›;
  rw [ SimpleGraph.connected_iff_exists_forall_reachable ] at *;
  exact ⟨ hG_conn.choose, fun w => h_connected _ _ ( hG_conn.choose_spec w ) ⟩

/-
MAIN SKELETON.
-/
theorem tree_to_unicyclic_host
    (G : SimpleGraph V) [DecidableRel G.Adj] (hG_conn : G.Connected)
    (F : DisjointTriangleFamily G)
    (T : Subgraph G) (hT_span : T.IsSpanning)
    (hT_acyclic : (T.coe).IsAcyclic) :
    ∃ G' : SimpleGraph V,
      G' ≤ G ∧
      G'.Connected ∧
      (∀ u v, T.Adj u v → G'.Adj u v) ∧
      G'.edgeFinset.card = G.edgeFinset.card - F.triangles.card := by
  choose! u hu v hv huv using fun i : F.triangles => spanning_tree_omits_triangle_edge T hT_span hT_acyclic i.1;
  -- Let $S$ be the set of edges $\{u_i, v_i\}$ for each triangle $i \in F.triangles$.
  set S : Finset (Sym2 V) := Finset.image (fun i : F.triangles => s(u i, v i)) Finset.univ;
  refine' ⟨ G.deleteEdges S, _, _, _, _ ⟩;
  · norm_num +zetaDelta at *;
    exact?;
  · apply connected_deleteEdges_of_bypass hG_conn;
    simp +zetaDelta at *;
    rintro u v t ht ( ⟨ rfl, rfl ⟩ | ⟨ rfl, rfl ⟩ );
    · -- Let $w$ be the third vertex of the triangle $t$.
      obtain ⟨w, hw⟩ : ∃ w : V, w ∈ t.verts ∧ w ≠ u ⟨t, ht⟩ ∧ w ≠ v ⟨t, ht⟩ := by
        have := Finset.card_eq_three.mp t.card_eq;
        obtain ⟨ x, y, z, hxy, hxz, hyz, h ⟩ := this; simp_all +decide ;
        grind;
      refine' ⟨ w, _, _, _, _ ⟩;
      · exact t.all_adj _ ( hu _ ht ) _ hw.1 ( by tauto );
      · exact t.all_adj _ hw.1 _ ( hv _ ht ) ( by tauto );
      · intro x hx;
        constructor <;> intro h <;> have := F.pairwise_disjoint x hx t ht <;> simp_all +decide [ VertexDisjoint ];
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          · grobner;
          · grind;
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          exact fun h'' => this ( hv x hx ) ( by aesop );
      · intro x hx;
        constructor <;> intro h <;> have := F.pairwise_disjoint x hx t ht <;> simp_all +decide [ VertexDisjoint ];
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          exact fun h'' => this ( hv x hx ) ( by aesop );
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          grind +suggestions;
    · -- Let $w$ be the third vertex of the triangle $t$.
      obtain ⟨w, hw⟩ : ∃ w : V, w ∈ t.verts ∧ w ≠ u ⟨t, ht⟩ ∧ w ≠ v ⟨t, ht⟩ := by
        have := Finset.card_eq_three.mp t.card_eq;
        obtain ⟨ x, y, z, hxy, hxz, hyz, h ⟩ := this; simp_all +decide ;
        grind;
      refine' ⟨ w, _, _, _, _ ⟩;
      · exact t.all_adj _ ( hv _ ht ) _ hw.1 ( by tauto );
      · exact t.all_adj _ hw.1 _ ( hu _ ht ) ( by tauto );
      · intro x hx;
        constructor <;> intro h <;> have := F.pairwise_disjoint x hx t ht <;> simp_all +decide [ VertexDisjoint ];
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          grind +suggestions;
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          exact fun h'' => this ( hv x hx ) ( by aesop );
      · intro x hx;
        constructor <;> intro h <;> have := F.pairwise_disjoint x hx t ht <;> simp_all +decide [ VertexDisjoint ];
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          exact fun h'' => this ( hv x hx ) ( by aesop );
        · by_cases h' : x = t <;> simp_all +decide [ Finset.disjoint_left ];
          · grobner;
          · grind;
  · intro u v huv';
    simp +zetaDelta at *;
    refine' ⟨ T.adj_sub huv', fun a ha => ⟨ _, _ ⟩ ⟩ <;> intro h₁ h₂ <;> have := huv a ha <;> simp_all +decide [ SimpleGraph.Subgraph.adj_comm ];
  · -- By definition of $S$, we know that $|S| = |F.triangles|$.
    have hS_card : S.card = F.triangles.card := by
      rw [ Finset.card_image_of_injective ];
      · simp +decide;
      · intro i j hij; have := F.pairwise_disjoint; simp_all +decide [ Finset.disjoint_left ] ;
        specialize this i.1 i.2 j.1 j.2 ; contrapose! this ; simp_all +decide [ VertexDisjoint ];
        exact Finset.not_disjoint_iff.mpr ⟨ u i, hu _ i.2, by aesop ⟩;
    have hS_subset : S ⊆ G.edgeFinset := by
      simp +zetaDelta at *;
      intro e he
      obtain ⟨i, hi, rfl⟩ := Finset.mem_image.mp he;
      have := i.1.all_adj ( u i ) ( hu i.1 i.2 ) ( v i ) ( hv i.1 i.2 ) ( huv i.1 i.2 |>.1 ) ; aesop;
    rw [ ← hS_card, SimpleGraph.edgeFinset_deleteEdges ];
    grind

/-- COROLLARY. -/
theorem unicyclic_host_when_epsilon_one
    (G : SimpleGraph V) [DecidableRel G.Adj] (hG_conn : G.Connected)
    (F : DisjointTriangleFamily G)
    (T : Subgraph G) (hT_span : T.IsSpanning)
    (hT_acyclic : (T.coe).IsAcyclic)
    (h_eps_one : G.edgeFinset.card - Fintype.card V + 1 - F.triangles.card = 1) :
    ∃ G' : SimpleGraph V,
      G' ≤ G ∧
      G'.Connected ∧
      (∀ u v, T.Adj u v → G'.Adj u v) ∧
      G'.edgeFinset.card - Fintype.card V + 1 = 1 := by
  obtain ⟨G', hle, hconn, hadj, hcard⟩ := tree_to_unicyclic_host G hG_conn F T hT_span hT_acyclic
  exact ⟨G', hle, hconn, hadj, by omega⟩

end EP488.TreeToHost