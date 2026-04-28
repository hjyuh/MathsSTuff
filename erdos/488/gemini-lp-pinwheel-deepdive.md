# EP-488: Gemini Deep Dive — LP Integrality Gap + Pinwheel Scheduling
## April 5, 2026 — Follow-up to brainstorm session, temperature 0.5-0.7

---

## CONTEXT

Your brainstorm identified three promising lateral connections to EP-488. I want you to go deep on TWO of them. This is a research task, not a solving task. Find specific theorems, proof techniques, and formulations that could transfer.

## CONNECTION 1: LP INTEGRALITY GAP

You suggested treating EP-488 as a hypergraph covering problem where the factor 2 is an integrality gap.

### What I need you to find:

1. **Fractional vs integer covers of arithmetic progressions.** 
The integers [1,x] are covered by arithmetic progressions {a, 2a, 3a, ...} for each a ∈ A. The density G(x) = F(x)/x is the fractional coverage. Are there results on LP relaxations of covering problems by arithmetic progressions? Specifically by progressions whose common differences form an antichain (no d_i | d_j)?

2. **The Lovász theta function and antichain independence.**
In the divisibility poset, a primitive set is an independent set (antichain). The Lovász theta function bounds the independence number. Is there a dual object (like fractional chromatic number) that bounds the density of the upset? Does θ(G)/α(G) ≤ 2 for divisibility-related graphs?

3. **Specific LP formulations.**
Consider the LP: maximize Σ_x (coverage_indicator(x))/x subject to: each x is covered by at most the progressions in A, A is primitive. Is there a dual LP whose feasible set gives a factor-2 bound? Look for formulations similar to the LP relaxation of Set Cover or Vertex Cover.

4. **Factor-2 integrality gaps in combinatorial optimization.**
Survey results where factor 2 appears as an integrality gap: vertex cover, feedback vertex set, weighted set cover with bounded frequency. Which of these have the same structure as "antichain generates an upset"?

5. **Specific reference:** Look for work by Alon, Babai, Suzuki on "Multilinear polynomials and Frankl-Ray-Chaudhuri-Wilson type intersection theorems" — this might connect antichain structure to density bounds via polynomial methods.

## CONNECTION 2: PINWHEEL SCHEDULING

You identified this as the closest structural analogue.

### What I need you to find:

1. **Chan and Chin (1992/1993) — exact results.**
What is the precise theorem? Is it "Σ 1/n_i ≤ 1/2 implies a valid schedule exists"? What's the proof technique? Is it constructive? Does it use a potential function, a greedy argument, or LP duality?

2. **The "bamboo garden trimming" problem.**
This is a continuous version of pinwheel scheduling. A gardener must trim k bamboo stalks that grow at rates r_i. Each day the gardener trims one stalk to height 0. The goal is to keep all stalks below height 2·max(r_i). Is the factor 2 here the same factor 2 as EP-488?

3. **Extensions to non-unit processing times.**
In EP-488, the "refresh" from element a_i covers all multiples of a_i simultaneously, not just one integer. This is like a pinwheel task that refreshes multiple items at once. Are there pinwheel scheduling results with batch refreshes where the coverage guarantee changes?

4. **The connection to density.**
In standard pinwheel, the schedule is a sequence. In EP-488, the "schedule" is the integer line itself — multiples of a_i automatically appear at positions a_i, 2a_i, 3a_i, .... There's no scheduling decision; the coverage is determined by the set A. The question is whether the automatic coverage is good enough. Has anyone studied "automatic pinwheel schedules" determined by arithmetic progressions?

5. **Holte's theorem and generalizations.**
Holte (1992) proved pinwheel schedulability for certain density conditions. What are the best known density thresholds? Do any match or approach the factor 2?

## CONNECTION 3 (bonus): Sum-free sets

One specific question: Cameron's theorem characterizes sum-free sets of maximum density. Is there a multiplicative analogue? Specifically: what is the maximum density of a "multiplicatively sum-free" set (a set where no element divides the product of two others — this is a 2-primitive set)? If the answer involves the factor 2, that would be significant.

## DELIVERABLES

For each connection, give me:
1. The strongest specific theorem you can find
2. The proof technique used (LP duality? greedy? probabilistic? algebraic?)
3. Whether the factor 2 in that result has the same structural origin as in EP-488
4. Whether the proof technique could plausibly transfer to bounding density oscillation of antichains' upsets
5. Full citations with URLs

## IMPORTANT
Do NOT claim EP-488 has been solved. It is OPEN. Do not hallucinate proofs or Lean formalizations. I want existing theorems from the literature, accurately stated.
