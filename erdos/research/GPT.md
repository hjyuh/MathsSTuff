# Next Erdős Target Selection for AI-Assisted Lean Formalization

## Executive summary

The provided document sets a concrete objective: identify the “best next” Erdős-problem target(s) for an AI-assisted Lean pipeline—focusing on problems where (i) the statement is already formalized in the entity["organization","Formal Conjectures","github repo"] repository, (ii) a known proof (or known partial proof) exists in the literature or forum comments, and (iii) the Lean proof is still missing (`sorry`) and plausibly short enough to be automated. fileciteturn0file0

Based on a cross-read of (a) the entity["organization","Erdős Problems database","erdosproblems.com"] status pages and forum metadata, and (b) the corresponding Lean stubs in entity["company","Google DeepMind","ai research lab"]’s entity["organization","Formal Conjectures","github repo"], the most pipeline-aligned “next targets” are not (primarily) the famous, high-profile open conjectures, but rather “bridge tasks” inside open problems: formalizing already-known special cases, explicit examples, and “sanity-check” lemmas that are currently tagged as `high_school`/`undergraduate` (or occasionally `research solved`) but remain `sorry`. This matches the document’s stated strengths (Finset arithmetic, concrete constructions, computation-assisted verification) and avoids the stated weaknesses (new Mathlib infrastructure, abstract algebra, measure theory). fileciteturn0file0 citeturn14view0turn13search0

A ranked set of seven candidates (spanning the document’s Tier A/B/C framing) is presented below, each with: status, Lean file location, what exactly to prove, expected Mathlib dependencies, forum activity signals, and a recommended proof-production route (human outline → LLM formalization → verification). citeturn23view0turn33view0turn31search0turn10view0turn8view0turn27view0turn32view2turn32view0turn35view0

## Extracted goals, questions, tasks, and data items from the document

The document contains the following explicit items (grouped by type). fileciteturn0file0

**Primary goal**
- Find Erdős problems to formalize (or solve) using an AI pipeline: Claude (orchestration) → GPT (proof strategy) → Codex (Lean code) → Aristotle (formalization) → Axle (verification). fileciteturn0file0

**Primary task**
- Search both the Erdős-problems website and the Formal Conjectures repository to find the best targets. fileciteturn0file0

**Selection criteria (explicit)**
- Tier A: “solved but not formalized” (known proof exists; statement present as a `.lean` file with `sorry`; proof not yet formalized). fileciteturn0file0  
- Tier B: “recently AI-solved” (late 2025/2026-ish character), where the proof exists but formalization may be incomplete/unsubmitted; good for replicating an automated pipeline. fileciteturn0file0  
- Tier C: “genuinely open” but potentially tractable, preferably combinatorics/elementary number theory with Mathlib coverage and low-hanging progress available. fileciteturn0file0

**Explicit exclusions**
- Avoid heavy algebraic infrastructure (polynomials/resultants/field extensions); avoid measure theory; avoid famous open conjectures; avoid problems actively being formalized; avoid problems already formalized by entity["people","Boris Alexeev","mathematician"], Neel Somani, or entity["people","Terence Tao","mathematician"]. fileciteturn0file0

**Required output format**
- Return 5–10 candidates; for each: problem number/link, plain-English statement, tier, whether a `.lean` statement exists and is still `sorry`, status on erdosproblems.com, why it is a good target, difficulty estimate (1–10), key Mathlib dependencies, and forum activity warnings. fileciteturn0file0

**Context/data points**
- The team recently proved 3/8 theorems on Erdős Problem 494 (counterexample results). fileciteturn0file0turn29view0  
- The pipeline is strongest at concrete Finset arithmetic, membership proofs, `norm_num`, `omega`, and explicit constructions; weakest at abstract algebra, polynomials, measure theory, and new Mathlib infrastructure. fileciteturn0file0

## Goal-to-findings map

The table below maps each extracted goal/question/task to what was found, with sources, confidence, and next steps.

| Document item (verbatim intent) | Findings | Sources | Confidence | Recommended next steps |
|---|---|---|---|---|
| Identify “next” Erdős targets for an AI→Lean pipeline | Best-fit targets are “proofable stubs” with existing `.lean` statements, low forum activity, and proofs reducible to finite/computational or short combinatorial lemmas; the “main open conjecture” often remains too hard, but sub-lemmas are ideal. | fileciteturn0file0 citeturn13search0turn14view0 | High | Focus on 1–2 “Tier A/B” formalization wins (below) to harden pipeline; then add 1 “Tier C falsifiable” search harness. |
| Search erdosproblems.com + Formal Conjectures | For each recommended candidate, both a status page on erdosproblems.com and a corresponding file in the Formal Conjectures ErdosProblems directory were located (or explicitly confirmed). | citeturn23view0turn32view0turn31search0turn10view0turn8view0turn35view0turn32view2turn33view0turn27view0 | High | Use a scripted “sweep” over `FormalConjectures/ErdosProblems` to detect `@[category …]` + `sorry` clusters, then cross-check forum activity counts. |
| Tier A filter: solved but not formalized | A clean Tier A exemplar is Problem 194 (disproved; formal statement exists; `sorry`; zero comments). The proof is known in the literature and not flagged as already Lean-formalized on the page. | citeturn23view0turn13search9turn16search17 | Medium | Attempt a formal counterexample via a definable strict total order (see candidate details). If it balloons into set-theory/choice issues, de-prioritize. |
| Tier B filter: recent AI-solved / AI-aided | Problem 42 has a community proof for small M (M=1,2,3) attributed to AI-assisted work in the comments; Formal Conjectures contains multiple `sorry` stubs for examples/lemmas. | citeturn32view0turn33view0 | High (for small cases), Low (for full problem) | Treat as Tier B for “formalize the M=3 case + the shipped example lemmas”; leave the asymptotic statement Tier C. |
| Tier C filter: genuinely open but tractable | Problem 64 is explicitly *falsifiable* (finite counterexample would disprove); Formal Conjectures has a direct formalization as a finite-graph statement with `sorry`. This is well-suited to “search + verify” workflows. | citeturn22search19turn31search0 | Medium | Build a counterexample-search harness (SAT/ILP or brute with pruning), then prove correctness in Lean for any found graph. |
| Avoid heavy topics and already-formalized-by-X | Selected candidates are largely finite/combinatorial; however, some open number-theory problems (470, 730, 1054, 931) have partial low-hanging lemmas worth formalizing even if the headline conjecture is hard. | citeturn32view2turn8view0turn10view0turn35view0 | Medium | For each open problem, target only the “small lemma” layer (explicit examples, definitional sanity checks) unless a short proof exists. |
| Provide 5–10 candidates with required metadata | Seven candidates are provided below with the specified metadata fields and an implementation plan for each. | citeturn23view0turn32view0turn31search0turn10view0turn8view0turn35view0turn32view2turn33view0turn27view0 | High | Use the comparison table to pick the top 1–2; start with “small, computationally verifiable” lemmas to reduce risk. |

## Candidate targets and analysis

### Comparison table of recommended candidates

Difficulty is estimated for *producing a Lean proof in Mathlib today* (1 = routine; 10 = research-grade formalization effort). Items marked “micro-target” mean the recommended deliverable is a lemma/variant in the file, not the full open problem.

| Problem | Target theorem(s) in Formal Conjectures | Tier | erdosproblems.com status and activity | `.lean` presence / proof state | Difficulty (1–10) | Why this is a strong fit |
|---|---|---|---|---|---|---|
| 194 | `erdos_194` | A | Disproved; 0 comments; formal statement exists. citeturn23view0 | `ErdosProblems/194.lean`, `research solved`, proof is `sorry`. citeturn13search9 | 6–8 | A clean “solved but not Lean” target with minimal forum contention; success would demonstrate rigorous counterexample formalization. |
| 42 | `example_maximal_sidon`, `example_difference_set`, `maximal_sidon_contains_zero`, and (optionally) “M=3” special case as a new lemma | B (micro) / C (full) | Open; 6 comments; notes a proof for M=3 in comments using AI tools. citeturn32view0 | `ErdosProblems/42.lean`, multiple `sorry` stubs for examples and core statement. citeturn33view0 | 3–5 for micro; 9–10 for full | Micro-targets are exactly “Finset/Set arithmetic + Sidon definitions”, ideal for the stated tool strengths. |
| 64 | `erdos_64` | C | Falsifiable open; finite counterexample would resolve; high prize; graph-theoretic. citeturn22search19 | `ErdosProblems/64.lean`, `research open`, `sorry`. citeturn31search0 | 5–9 | Perfect for “compute candidate object → Lean verification” workflow; does not require deep new theory if a small counterexample exists. |
| 730 | `erdos_730.variants.explicit_pairs` (micro-target) plus any additional `S`-membership lemmas | C (micro) / C (full) | Open; 2 comments; statement formalized; has explicit OEIS link. citeturn20search11 | `ErdosProblems/730.lean` has `research open` main theorem `sorry`; explicit-pairs lemma is `sorry`. citeturn8view0 | 2–4 for micro; 10 for full | Micro-target is straightforward computation-heavy Lean: prime factor sets of specific binomial coefficients. |
| 1054 | `f_undefined_at_2`, `f_undefined_at_3` (micro-targets) | A (micro) / C (full) | Open; 5 comments; explicitly notes f undefined at 2 and 5 (site-level claim). citeturn32view1 | `ErdosProblems/1054.lean` includes these as `high_school` theorems with `sorry`. citeturn10view0 | 2–4 | “Junk-value / undefined-case” lemmas are great pipeline tests: finite search + divisors + sums. |
| 470 | `smallest_weird_eq_70`, `odd_weird_gt_…` bounds (micro-target scope recommended: smallest-weird lemma only) | C (micro) | Open; 2 comments; gives concrete facts (smallest weird is 70; no odd weird < 1e21). citeturn32view2 | File has definitions and `sorry` for small results (e.g., 70). citeturn7search0 | 3–5 (for 70 lemma) | Computation + divisor-sum and subset-sum arguments fit the pipeline; avoid the enormous “1e21” bound. |
| 931 | `erdos_931` and/or `erdos_931.variants.exists_prime` (micro-target exploration likely) | C | Open; 0 comments; already lists a concrete counterexample to a strengthened variant. citeturn35view0 | `ErdosProblems/931.lean` includes one counterexample proof already (nonempty set) and other `sorry` statements. citeturn27view0 | 4–7 for micro; 10 for full | “Explicit counterexample + primeFactors + interval products” problems align with computation and number-theory tactics; low forum contention. |

### Visual aid: decision flow for picking the next target

```mermaid
flowchart TD
  A[Start: candidate Erdős problem] --> B{Statement in Formal Conjectures?}
  B -- No --> B1[Deprioritize (unless very high value) or add statement first]
  B -- Yes --> C{Proof stub exists? (sorry)}
  C -- No --> C1[Already formalized; skip per constraints]
  C -- Yes --> D{Known proof source?}
  D -- Published / forum proof --> E{Proof likely <200 lines in Lean?}
  D -- None --> F[Tier C: consider search/partial lemmas]
  E -- Yes --> G[Tier A/B: prioritize]
  E -- No --> H[Decompose into micro-target lemmas]
  G --> I[Run pipeline: strategy → formalize → verify → PR]
  H --> I
  F --> I
```

### Candidate-by-candidate detail

#### Erdős Problem 194

**Problem statement (plain English)**  
The site states the problem asks whether *every* ordering of the real numbers must contain a monotone arithmetic progression of length \(k\ge 3\); it is marked **DISPROVED**, and the site attributes the negative solution (even for \(k=3\)) to a published source. citeturn23view0

**Formal Conjectures status**  
`ErdosProblems/194.lean` contains a theorem `erdos_194` tagged `@[category research solved, AMS 5]` with proof `sorry`. citeturn13search9turn16search17

**Tier classification**  
Tier A (solved/disproved; statement present; proof absent). citeturn23view0turn13search9

**Forum activity / collision risk**  
0 comments on the problem page suggests low immediate contention. citeturn23view0

**Why it fits / why it’s risky**  
- Fit: a single, self-contained disproof is often a good “Tier A win” if the counterexample structure is formalizable with existing order-theory tooling. citeturn13search9  
- Risk: the formal statement quantifies over *all* strict total orders on ℝ, so the Lean proof must exhibit (or encode) one strict total order with no monotone 3-term AP; depending on the literature proof style, this may drag in “choice-y” encodings, noncomputable constructions, or heavy set-theory. citeturn13search9turn23view0

**Key Lean/Mathlib dependencies (expected)**  
`IsStrictTotalOrder`, lists, arithmetic progressions on ℝ, and a definable alternative order relation; likely `Set`, `List`, `Order`, possibly `Classical` (noncomputable). citeturn13search9

**Actionable recommendation**  
Treat this as a “high-upside Tier A” but do an early feasibility spike: implement the counterexample order on a *countable dense* subset first (e.g., rationals) and attempt to extend to ℝ if needed, or refactor the theorem statement to a simpler equivalent that matches the literature proof (if the current statement forces unnecessary generality). If the proof requires large foundational changes, shift effort to lower-risk micro-targets (Problems 42/730/1054). citeturn13search9turn33view0turn8view0turn10view0

#### Erdős Problem 42

**Problem statement (plain English)**  
The site asks: given a Sidon set \(A\subset\{1,\dots,N\}\), can one find another Sidon set \(B\subset\{1,\dots,N\}\) of fixed size \(M\) so that the difference sets intersect only at 0; it is marked **OPEN**. The page notes that the cases \(M=1,2,3\) have proofs in the comments, with \(M=3\) credited to a post using AI tools. citeturn32view0

**Formal Conjectures status**  
`ErdosProblems/42.lean` contains the main conjecture (`erdos_42`) as `research open` with `sorry`, plus a constructive variant and several “Related results and examples” that are also `sorry` (e.g., `{1,2,4}` maximal Sidon in `{1,…,4}`, its difference set calculation, and a lemma that any maximal Sidon set has 0 in its difference set). citeturn33view0

**Tier classification**  
- Tier B (micro-target): formalize the already-solved small-M cases and the shipped example lemmas. citeturn32view0turn33view0  
- Tier C (full problem): the asymptotic statement is still open and plausibly deep. citeturn32view0turn33view0

**Forum activity / collision risk**  
6 comments, and the page marks the problem as “looks tractable” by the profile “BorisAlexeev” (as a site interaction). This increases collision risk if you try the *full* conjecture, but micro-lemma formalizations should remain welcome. citeturn32view0

**Why this is a strong pipeline target**  
This file is almost a “unit test” for the strengths described in the document: Sidon sets are definitional; the three provided `undergraduate` lemmas are finite-set computations and difference-set equalities; proving them in Lean likely reduces to `Finset`/`Set` algebra and small computations. citeturn33view0turn32view0fileciteturn0file0

**Key Lean/Mathlib dependencies (expected)**  
- Set difference `A - A` with `open scoped Pointwise`  
- `Set.Icc`, `Set.ncard`, `IsSidon`, and the custom predicate `IsMaximalSidonSetIn` used in the file. citeturn33view0

**Actionable recommendation**  
Deliver a “Tier B micro-package” PR:
1) fill `example_maximal_sidon` and `example_difference_set` and `maximal_sidon_contains_zero`;  
2) add a new theorem formalizing the \(M=1\) and \(M=2\) cases (explicitly), then attempt \(M=3\) by translating the forum-comment proof into Lean.

This yields immediate verified progress without committing to the full asymptotic conjecture. citeturn33view0turn32view0

#### Erdős Problem 64

**Problem statement (plain English)**  
The site frames this as **FALSIFIABLE**: does every finite graph with minimum degree ≥ 3 contain a cycle of length \(2^k\) for some \(k\ge 2\)? A finite counterexample would disprove it. citeturn22search19

**Formal Conjectures status**  
`ErdosProblems/64.lean` states the problem as: for any finite simple graph with minDegree ≥ 3, there exists \(k\ge 2\) and a closed walk that is a cycle of length \(2^k\); the theorem is `answer(sorry)` with `sorry` proof. citeturn31search0

**Tier classification**  
Tier C. It is open, but uniquely suited to computational falsification and post-hoc Lean verification. citeturn22search19turn31search0

**Forum activity / collision risk**  
Not determined from the provided snippet beyond its falsifiable status and prize framing; treat as moderate risk, but computational counterexample search is still a valuable contribution even if no counterexample is found. citeturn22search19turn31search0

**Why this is a strong pipeline target**  
This is a canonical “search + verify” problem. If you find a graph \(G\) with minDegree ≥ 3 and *no* power-of-two cycle lengths, Lean can verify it mechanistically once you encode the graph and prove the absence of cycles of those lengths—often via brute force enumeration of walks/cycles in a finite graph. citeturn31search0

**Key Lean/Mathlib dependencies (expected)**  
`SimpleGraph`, `Fintype V`, decidable adjacency, `minDegree`, `Walk`, `IsCycle`, and length arithmetic. citeturn31search0

**Actionable recommendation**  
Treat this as an engineering+math project:
- Build an external searcher (SAT/ILP or brute with pruning) to hunt for candidate graphs.
- For any candidate, generate Lean code that defines the graph explicitly (adjacency matrix/list) and proves:
  1) minDegree ≥ 3;  
  2) for all \(k\ge 2\), there is **no** cycle of length \(2^k\).

Even if no counterexample is found quickly, you can still contribute helper lemmas or automation around cycle enumeration and degree bounds in `SimpleGraph`, which may benefit other graph-theory problems. citeturn31search0turn13search0

#### Erdős Problem 730

**Problem statement (plain English)**  
The Lean file defines a set \(S\) of pairs \((n,m)\) where the central binomial coefficients \(\binom{2n}{n}\) and \(\binom{2m}{m}\) share the same set of prime divisors; the main question is whether there are infinitely many such pairs. citeturn8view0

**Formal Conjectures status**  
- `erdos_730` is `research open` and `sorry`.  
- `erdos_730.variants.explicit_pairs` is `high_school` and `sorry` (prove specific pairs \((87,88)\) and \((607,608)\) are in \(S\)).  
- A separate variant `delta_ne_one` is already proven in the file (no `sorry`) using explicit witnesses. citeturn8view0

**erdősproblems.com status and activity**  
The page indicates the statement is formalized (“Yes”), references OEIS A129515, and shows 2 comments (low activity). citeturn20search11

**Tier classification**  
Tier C overall; “explicit-pairs lemma” is a Tier A-style micro-target (already-known example, missing formal proof). citeturn8view0turn20search11

**Why this is a strong pipeline target**  
The micro-target is exactly what your document describes as a “Codex/Aristotle sweet spot”: compute prime-factor sets for fixed naturals, then discharge with `norm_num`, `decide`, or specialized lemmas about `Nat.centralBinom` / prime factors. citeturn8view0fileciteturn0file0

**Key Lean/Mathlib dependencies (expected)**  
`Nat.centralBinom`, `Nat.primeFactors`, finite-set reasoning on pairs, and computation tactics (`norm_num`, `decide`, possibly `native_decide`). citeturn8view0

**Actionable recommendation**  
Ship a PR that proves `erdos_730.variants.explicit_pairs` and any supporting lemmas needed to make such “prime-factor equality by computation” proofs smooth and reusable (this also benefits the nearby theorem `delta_ne_one` style). citeturn8view0turn20search11

#### Erdős Problem 1054

**Problem statement (plain English)**  
Define \(f(n)\) as the least \(m\) such that \(n\) is the sum of the \(k\) smallest divisors of \(m\) for some \(k\ge 1\). The page asks asymptotic questions about whether \(f(n)=o(n)\), whether it holds for almost all \(n\), and whether \(\limsup f(n)/n=\infty\). It also explicitly states \(f\) is undefined for \(n=2\) and \(n=5\). citeturn32view1

**Formal Conjectures status**  
The file `ErdosProblems/1054.lean` formalizes three open asymptotic subquestions and also includes two `high_school` lemmas `f_undefined_at_2 : f 2 = 0` and `f_undefined_at_3 : f 5 = 0`, both currently `sorry`. citeturn10view0

**Tier classification**  
- Tier A (micro-target): the undefined-at-2 and undefined-at-5 facts are intended to be provable now. citeturn32view1turn10view0  
- Tier C (full): the asymptotic questions remain open/complex, and the page notes a disproof of the strong form in comments elsewhere. citeturn32view1turn10view0

**Forum activity / collision risk**  
5 comments; the “looks tractable” tag is associated with Tao’s profile. This suggests some attention, but the micro-target lemmas are unlikely to conflict. citeturn32view1

**Why this is a strong pipeline target**  
“Undefined/junk-value” lemmas are excellent automated formalization tests: they often reduce to showing no witness exists for the defining `if` branch, hence the function takes the `else 0` case; this is typically a finite, checkable number theory argument about divisors and small sums. citeturn10view0turn32view1

**Key Lean/Mathlib dependencies (expected)**  
`Nat.divisors`, indexing into a divisor list (`Nat.nth` with membership predicate), finite sums, simple contradiction arguments. citeturn10view0

**Actionable recommendation**  
Implement `f_undefined_at_2` and `f_undefined_at_3` as a self-contained micro-PR. If you need automation, write a small helper lemma: “no natural \(m,k\ge 1\) has sum of k smallest divisors equal to 2 / 5.” This should be possible with bounded case splits on \(m\) using divisor properties rather than any analytic machinery. citeturn10view0turn32view1

#### Erdős Problem 470

**Problem statement (plain English)**  
Defines “weird” numbers: \(\sigma(n)\ge 2n\) and \(n\) is not pseudoperfect (not a sum of a set of its divisors). Asks whether any odd weird numbers exist and whether there are infinitely many primitive weird numbers. The page states the smallest weird number is 70 and cites additional partial results/bounds. citeturn32view2

**Formal Conjectures status**  
The Formal Conjectures file for 470 includes the definition of weird numbers and several stubs/variants such as `smallest_weird_eq_70` and other auxiliary statements, still `sorry`. citeturn7search0

**Tier classification**  
Tier C overall; but `smallest_weird_eq_70` is a Tier A-style micro-target: a concrete fact expected to be formalizable with finite computation and subset-sum reasoning. citeturn32view2turn7search0

**Forum activity / collision risk**  
2 comments; low collision. citeturn32view2

**Why this is a strong pipeline target**  
The “70 is weird” claim decomposes into:
1) compute divisors and show \(\sigma(70)\ge 2\cdot 70\);  
2) prove there is no subset of proper divisors summing to 70 (a finite subset-sum proof).  
This is precisely the kind of bounded combinatorial computational argument that can be checked and then made Lean-acceptable (either by constructive enumeration in Lean or by lemma-based reasoning plus `decide`). citeturn32view2turn7search0

**Key Lean/Mathlib dependencies (expected)**  
Divisors, sigma function, finite set subset sums; potentially a bit of infrastructure around “pseudoperfect” encoding if not already provided in the file. citeturn7search0

**Actionable recommendation**  
Commit only to the micro-target “smallest weird number is 70” (and possibly a small library of subset-sum helpers). Do **not** attempt the huge computational bounds referenced on the page (e.g., no odd weird < \(10^{21}\))—those are not realistic pipeline wins unless they already exist as formally verified code artifacts elsewhere. citeturn32view2turn7search0

#### Erdős Problem 931

**Problem statement (plain English)**  
Asks whether there are only finitely many pairs of intervals \(\prod_{i\le k_1}(n_1+i)\) and \(\prod_{j\le k_2}(n_2+j)\) with the same prime factors. The page is marked **OPEN**, gives an example pair from Tijdeman, and notes that a strengthened form is false with an explicit counterexample (credited to AlphaProof). citeturn35view0

**Formal Conjectures status**  
`ErdosProblems/931.lean` contains:
- the main conjecture and an “additional condition” variant as `research open` with `sorry`;  
- a proven explicit counterexample lemma `additional_condition_nonempty` (already filled, no `sorry`);  
- an open lemma `exists_prime` with `sorry` that would prove the existence of a prime between \(n_1\) and \(n_2\) under the prime-factors-equality hypothesis. citeturn27view0

**Tier classification**  
Tier C. Use as a micro-target file: formalize one of the intermediate open variants (e.g., `exists_prime`) *if* it has a short proof in the literature or forum; otherwise restrict to adding more computational counterexamples / helper lemmas. citeturn35view0turn27view0

**Forum activity / collision risk**  
0 comments on the problem page: low collision, but also likely low existing guidance beyond the stated examples. citeturn35view0

**Why this is a strong pipeline target**  
It already demonstrates the style you want: explicit counterexample logic using `primeFactors`, interval products with `Finset.Icc`, and computational normalization (`norm_num`, `decide`). Extending this file with additional examples or auxiliary lemmas is a good “proof engineering” project that aligns with your strengths. citeturn27view0turn35view0

**Key Lean/Mathlib dependencies (expected)**  
`Finset.prod_Icc`, `Nat.primeFactors`, basic prime arithmetic, interval bounds, and normalization tactics. citeturn27view0

**Actionable recommendation**  
Do *not* attempt the full finiteness conjecture until a short, Lean-friendly proof route is identified. Instead:
- Formalize the Tijdeman example explicitly as a lemma (mirroring the AlphaProof counterexample already in the file).  
- If feasible, fill `exists_prime` for restricted parameter ranges (or add a bounded / finite version first), to create stepping stones and test automation. citeturn35view0turn27view0

## Reproducible workflow, code snippets, and practical guidance

### Repository-driven target discovery

The Formal Conjectures repository provides explicit guidance on the meanings of `research open`, `research solved`, and “research formally solved” tags and emphasizes that many files contain only statements with `sorry`. citeturn13search0

A reproducible way to find additional Tier A/B micro-targets is to scan the `ErdosProblems` directory for:
- `@[category research solved` followed by a theorem proof `:= by sorry`
- `@[category high_school` or `@[category undergraduate` with `:= by sorry` (excellent micro-targets)
- low line-count files (often easiest formalizations)

Example (local Python pseudocode you can run on a checkout of the repo):

```python
import re, pathlib

root = pathlib.Path("formal-conjectures/FormalConjectures/ErdosProblems")
hits = []
for p in root.glob("*.lean"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    if "sorry" not in txt:
        continue
    # crude signals
    solved = "category research solved" in txt and "by\n\n sorry" in txt or "by\n sorry" in txt
    easy  = "category high_school" in txt or "category undergraduate" in txt
    if solved or easy:
        hits.append((p.name, solved, easy, txt.count("sorry")))
hits.sort(key=lambda x: (not x[2], not x[1], x[3]))
print(hits[:30])
```

### Counterexample-search harness for “falsifiable” graph problems (Problem 64)

For Problem 64, the computational side can be done outside Lean, then exported.

Illustrative Python (NetworkX) search skeleton:

```python
import itertools
import networkx as nx

def has_cycle_of_length_power_of_two(G):
    n = G.number_of_nodes()
    # check cycle lengths up to n
    # (naive; replace with better cycle enumeration / SAT constraints)
    for k in range(2, 1 + (n.bit_length())):
        L = 2**k
        if L > n:
            break
        # networkx.simple_cycles works for directed graphs; for undirected,
        # use cycle_basis as heuristic, or implement your own.
    return False

def min_degree(G):
    return min(dict(G.degree()).values())

def search(n, max_edges=None):
    nodes = list(range(n))
    all_edges = [(i,j) for i in nodes for j in nodes if i<j]
    for r in range(n-1, len(all_edges)+1):
        if max_edges and r > max_edges:
            break
        for edges in itertools.combinations(all_edges, r):
            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)
            if min_degree(G) < 3:
                continue
            if not has_cycle_of_length_power_of_two(G):
                return G
    return None
```

Lean-side verification approach (high level):
1) define `V := Fin n` and `G : SimpleGraph V` via a decidable adjacency predicate;
2) prove `G.minDegree ≥ 3` by `decide`/`native_decide`;
3) prove `¬ ∃ (k≥2) (v) (c : G.Walk v v), c.IsCycle ∧ c.length = 2^k` again by bounded enumeration if `n` is small.

This division of labor matches the pipeline ethos described by entity["people","Thomas F. Bloom","mathematician"] and entity["people","Boris Alexeev","mathematician"]: use automation to generate candidates, but keep Lean as the final certificate. citeturn14view0turn31search0

### Practical cautions aligned with the document

The Alexeev write-up emphasizes that “misformalization” (wrong statements, missing hypotheses, swapped variables) is a recurring failure mode; this is especially relevant in older Erdős-problem formulations and in problems whose English statement may have implicit constraints. citeturn14view0

Accordingly:
- Prefer micro-targets that are *explicitly checkable* (Problem 730 explicit pairs; Problem 1054 undefined cases; Problem 470 “70 is weird”). citeturn8view0turn10view0turn32view2  
- For open problems, invest first in “API + examples” to ensure the formal statement matches the intended mathematics (Problem 42’s example lemmas are a good template). citeturn33view0turn32view0

## Appendices

### URLs of core sources consulted

(Placed in a code block to satisfy the “list URLs” request while remaining consistent with system constraints.)

```text
https://www.erdosproblems.com/
https://github.com/google-deepmind/formal-conjectures
https://www.erdosproblems.com/194
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/194.lean
https://www.erdosproblems.com/42
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/42.lean
https://www.erdosproblems.com/64
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/64.lean
https://www.erdosproblems.com/730
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/730.lean
https://www.erdosproblems.com/1054
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1054.lean
https://www.erdosproblems.com/470
https://www.erdosproblems.com/931
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/931.lean
https://xenaproject.wordpress.com/2025/12/05/formalization-of-erdos-problems/
```

### Raw notes and short source excerpts

All excerpts are kept short; for full context, follow the linked citations.

- Problem 194 status excerpt: “DISPROVED … The answer is no, even for \(k=3\) …” citeturn23view0  
- Problem 42 excerpt (small cases): “Sedov … proved this is true for M=3. The case M=1 is trivial; … M=2 … also proved …” citeturn32view0  
- Problem 64 formal statement excerpt (Lean): “Does every finite graph with minimum degree at least 3 contain a cycle of length \(2^k\) … ?” citeturn31search0  
- Problem 1054 excerpt (undefined cases): “The function \(f(n)\) is undefined for \(n=2\) and \(n=5\) …” citeturn32view1  
- Problem 470 excerpt: “The smallest weird number is 70.” citeturn32view2  
- Problem 931 excerpt (strengthened variant false): the page provides an explicit counterexample showing the strengthened ‘\(n_2 \le 2(n_1+k_1)\)’ form fails. citeturn35view0  
- Pipeline/field context excerpt: Alexeev’s post describes the rapid growth of formalized Erdős-problem statements and highlights misformalization as a recurring issue. citeturn14view0