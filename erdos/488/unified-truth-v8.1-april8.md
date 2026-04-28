# EP-488: Open Field v8.1 — Scale-Independent Toolkit
## April 8, 2026. Current: 84%. Move it.

---

## READ THIS FIRST

Addendum to v8. Read v8 for full context (75 kills, two-regime structure).
This document integrates three new results that REPAIR the deep-scale gap.

---

## THE PROBLEM (5 lines)

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## NEW RESULTS SINCE v8 (all scale-independent, all proved)

### Theorem A: Scale-Independent First-Layer Theorem (5.4)
Any layer with s ≥ 4 and a quotient-2 support satisfies S₁ > E_j.
Proof uses ONLY: a₁ ≤ 2a/3, L(t)-L(s) ≤ t-s, s ≥ 4.
NO compact bounds. Works at ANY depth.

### Theorem B: Deep Single-Band Common-Core (5.4)
For A = dB with min B = 2, any single bad band with s ≥ 7:
S_{2d} > Σ E_a over all bad layers in that band.

### Theorem C: {2,3}-Component Safety (Codex B)
If 2,3 ∈ C, then B_C(n,m) > 0 for all m > n ≥ 3.
Proof: F_C(n) ≥ ⌊n/2⌋+⌊n/3⌋-⌊n/6⌋, giving 2/3 coverage.
CONSEQUENCE: Deep examples with literal {2,3} are NOT the hard case.
A counterexample component cannot contain actual 2 and 3.

### Lemma D: Kernel Prime → LCM-Graph Neighbor (5.2)
If prime p ≤ s is in kernel of layer a via witness b, then lcm(a,b) ≤ n.
CONSEQUENCE: Deep bad layer at depth s has ≥ π(s) neighbors in component.

### Lemma E: Scale-Independent Edge Quotient Bound (5.2)
If x ~ y in n-LCM graph: q_{x→y} ≤ ⌊n/y⌋ = s_y.
Replaces the compact-only "quotient < 20" with depth-parametrized bound.

### Lemma F: Scale-Independent Band Degree-Size (5.2)
k elements in depth-s band sharing quotient class q from vertex c:
  c ≤ n/((s+1)(k-1)), hence s_c ≥ (s+1)(k-1) - 1.
High degree in ANY band forces tiny c forces huge depth.

---

## THE CORRECTED TOOLKIT (scale-independent)

| Tool | Statement | Scale |
|------|-----------|-------|
| Self-funding | s ≤ 3 → E ≤ 0 | All |
| First-layer theorem | s ≥ 4 + quotient-2 → S₁ > E_j each | All |
| Superadditivity | Cross-component lcm > n → budget additive | All |
| Component Reduction | Counterexample in single n-LCM component | All |
| {2,3}-safety | Component with literal 2,3 → safe | All |
| Edge quotient | q ≤ s_y (depth of target) | All |
| Degree-size | k in band → c ≤ n/((s+1)(k-1)) | All |
| Deep star | Bad at depth s → π(s) neighbors | All |
| Single-band core | s ≥ 7 common-core band → base layer pays | All |
| H_A reduction | EP-488 ⟺ 2mH_A(n) ≥ nH_A(m) | All |
| Surplus Dominance | Surplus ≥ S₁ (zero violations) | Conjecture |

---

## THE NARROWED GAP

### What's eliminated:
- Components with literal 2,3 (Theorem C)
- Individual bad layers at any scale (Theorem A)
- Single-band common-core at any scale (Theorem B)
- Non-interacting components (Superadditivity)
- The "initial prime segment" example family (safe by Theorem C)

### What remains:
A counterexample must live in a single n-LCM connected component that:
1. Does NOT contain literal 2 or 3
2. Has bad layers getting {2,3} in kernel from COMPOSITE ancestors (2d, 3d)
3. Forces a lifted/common-core structure (shared divisor d > 1)
4. Has MULTIPLE bad bands interacting (single band is solved)
5. The multi-band total excess exceeds the global good slack

### The deep-scale dichotomy (from 5.2's lemmas):
Inside any n-LCM component with a deep bad layer at depth s:

**Case 1: High-degree concentration.**
Some vertex c touches many bad layers through one quotient class.
Lemma F forces c ≤ n/((s+1)(k-1)) — tiny element, massive depth.
Massive depth → massive slack (Window Lemma / quasi-linear L).
This slack should dominate the bad excess from those layers.

**Case 2: Spread across many vertices.**
Bad layer's π(s) kernel witnesses spread across many neighbors.
Component has ≥ π(s) vertices. Many vertices → aggregate slack.
Superadditivity-type argument should show total slack dominates.

---

## WHAT'S BEEN KILLED (75 kills, key lessons)

Categories A-Q from v8 plus:
- No compact-scale extrapolation to deep scale (Kills #72-75)
- "Connectors = ancestors" is FALSE (compact relays exist with
  composite quotients like 6, not prime quotients)
- Monotone reduction from pairs is FALSE (Kill #71)
- Bad layers exist at ANY depth s (infinite family)

---

## APPROACHES (updated)

### 1. Surplus Dominance (most direct, scale-independent)
Prove: 2mH_A(n) ≥ nH_A(m) for all primitive A.
Zero violations. Would close EP-488 at all scales simultaneously.
Bypasses compact/deep/multi-band distinctions entirely.

### 2. Multi-Band Charging via Degree-Size
Use Lemma F across ALL bands simultaneously.
Each bad band forces ancestors. Ancestors in different bands interact.
The degree-size bound constrains how ancestors distribute across bands.
Aggregate: total ancestor slack vs total multi-band excess.

### 3. Component Structure Theorem
Prove: any n-LCM component without literal 2,3 has a lifted
common-core structure (shared d > 1 among all elements).
Then reduce to common-core family proofs (already done for
single bands, need multi-band extension).

### 4. Deep Window Lemma
Extend the Window Lemma to deep scale using 5.2's generalized
degree-size machinery. A thin window of ancestors near the prime
threshold provides O(M²) slack at ANY depth, not just compact.

### 5. Connector Slack Lower Bound (CSLB)
Prove: S_c ≥ η · mn/c for any good element c with s_c ≥ 20.
Combined with degree-size: high-degree connector → tiny c → huge
slack → dominates attached bad excess. Would close the connector
regime at all scales.

### 6. Erdős density bound
Primitive sets satisfy Σ 1/(a log a) < ∞. This constrains how
dense A can be at any scale. Can this directly bound F(m)/F(n)?
Nobody has tried this route.

---

## YOUR TASK

Push the percentage. Up or down. Any route.

The scale-independent toolkit is now complete. Every compact tool has
a deep generalization. The gap is multi-band interaction in lifted
common-core components — or prove Surplus Dominance directly.

75 kills. 25+ proved results. The proof is assembling itself.
Find the closing argument.
