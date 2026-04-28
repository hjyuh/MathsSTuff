# EP-488 Road to 100% — Checklist (April 15, 2026)

Current: **87%**. Remaining: **13%** spread across the items below.

---

## ALREADY BANKED (87%)

| % | Item | Status |
|---|------|--------|
| 15% | Pair case (|R|=1) | ✅ Machine-verified (Aristotle) |
| 10% | Top Window reduction (only C ⊂ (q/2,q] can be extremal) | ✅ Proved |
| 10% | n < 2q case (all |R|) | ✅ Proved |
| 15% | m-side solved (q-excluded Hunter bound) | ✅ Verified (Codex B) |
| 10% | Forest case / Edge-Domination | ✅ Proved |
| 5% | Five atomic families closed | ✅ Computational (18M+ tuples) |
| 5% | Separator superadditivity | ✅ Machine-verified |
| 5% | BBDS structural infrastructure (blockCov_mono, slotMass_mono, minimal subfamily, collision, block decomposition) | ✅ Machine-verified (Aristotle) |
| 5% | Deep structure identified (ε_n decomposition, (★) equation, 4 edge types under n<3q) | ✅ Framework established |
| 7% | Triple case (13/18 Lean theorems + two informal proofs of the final sorry) | ✅ Proof exists, awaiting formalization |

---

## REMAINING TO 100% (13%)

### Tier 1 — Formalization of existing proofs (3%)

| % | Item | What's needed | Difficulty | Next action |
|---|------|--------------|------------|-------------|
| 2% | Formalize f_supermodular_topwindow in Lean | Two independent proofs exist (5.4-A, 5.2). Submit to Gauss. | Medium — proof is clean but has case splits | Send to Gauss next session |
| 1% | Triple case cascade (5 remaining Lean sorries) | Automatic once f_supermodular_topwindow is formalized | Easy — should cascade mechanically | Follows from above |

### Tier 2 — Unicyclic closure (3%)

| % | Item | What's needed | Difficulty | Next action |
|---|------|--------------|------------|-------------|
| 2% | Prove CML for c=1: M_T(n,m) ≥ 2/n for unicyclic components under n < 3q | Interval arithmetic over 60 residue classes mod lcm(2,3,4,5). Only 4 edge types. | Medium — finite computation, needs careful bookkeeping | Send to Muse (parallelism ideal for residue enumeration) |
| 1% | Formalize unicyclic CML in Lean | Depends on above proof | Medium | Send to Gauss once proof exists |

### Tier 3 — Multi-cycle closure (5%)

This is the hardest remaining piece. Three sub-routes, any ONE of which suffices:

| % | Item | What's needed | Difficulty | Next action |
|---|------|--------------|------------|-------------|
| 5% | **Option A: Tighten ε_n bound** — Prove ε_n ≤ ⌈c/2⌉ (or similar) for c ≥ 2 | Structural analysis of cycle corrections in inclusion-exclusion. Currently only ε_n ≤ c is known. | Hard — no proof or approach yet | Send to 5.4 + Muse for exploration |
| 5% | **Option B: Strengthen CML target** — Prove M_T(n,m) ≥ (2c+1)/n for c ≥ 2 | Stronger interval arithmetic; may need component-specific analysis | Hard — might not be true at this target | Computational verification first |
| 5% | **Option C: Cycle absorption** — Prove 2ε_n/n − ε_m/m ≤ M_T(n,m) directly | Show cycles penalize m at least proportionally to n. Uses full (★) with −ε_m/m term. | Hard — most elegant but least developed | Send to 5.4 for structural exploration |

*Only one of A/B/C needed. If any succeeds, this 5% is banked.*

### Tier 4 — Final integration (2%)

| % | Item | What's needed | Difficulty | Next action |
|---|------|--------------|------------|-------------|
| 1% | Connect all cases into single proof | Pairs + triples + forest + unicyclic + multi-cycle + n<2q → full EP-488 | Easy once components exist | Orchestrator drafts, Gauss/Aristotle verify |
| 1% | Full machine verification or write-up | Either complete Lean proof or publishable paper | Medium — mostly assembly | Final round |

---

## DEPENDENCY GRAPH

```
f_supermodular_topwindow (Lean)          CML c=1 proof
        │                                     │
        ▼                                     ▼
  Triple case closed (3%)            Unicyclic closed (3%)
                                              │
                              ┌───────────────┼───────────────┐
                              ▼               ▼               ▼
                         Option A         Option B         Option C
                        (ε_n bound)    (stronger CML)  (cycle absorption)
                              │               │               │
                              └───────┬───────┘───────────────┘
                                      ▼
                            Multi-cycle closed (5%)
                                      │
                                      ▼
                            Final integration (2%)
                                      │
                                      ▼
                                   100% ✓
```

---

## CRITICAL PATH (fastest route to 100%)

1. **Tomorrow:** Submit f_supermodular_topwindow to Gauss → **90%**
2. **This week:** Prove CML for c=1 via interval arithmetic → **93%**
3. **Next 1-2 weeks:** Crack any ONE of Options A/B/C for multi-cycle → **98%**
4. **Final assembly:** Integration + verification → **100%**

**Hardest step:** #3. This is where the last 65 years of "open" lives. Everything else is execution on existing proofs or concrete finite computations.

---

## RISK ASSESSMENT

| Risk | Impact | Mitigation |
|------|--------|------------|
| f_supermodular_topwindow fails to formalize | Blocks 3% | Two independent proofs; both are clean. Low risk. |
| CML for c=1 is false | Blocks 3% | Computationally verified. Low risk. |
| ALL of Options A/B/C fail | Blocks 5% | This would mean a fundamentally new idea is needed. Moderate risk. But: zero counterexamples in exhaustive search, hexagon margin is 7× what's needed, and the −ε_m/m term is unexploited. |
| Gauss/Aristotle hit rate limits | Delays formalization | Switch backends (Gauss already switched to Codex). Multiple verifiers available. |
