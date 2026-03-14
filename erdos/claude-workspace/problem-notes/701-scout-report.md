# Problem 701 — Scout Report
## March 13, 2026

## THE PROBLEM (Chvátal's Conjecture)

Let F be a family of sets closed under taking subsets (i.e. if B ⊆ A ∈ F then B ∈ F).
There exists some element x such that whenever F' ⊆ F is an intersecting subfamily,
we have |F'| ≤ |{A ∈ F : x ∈ A}|.

Source: [Er81], combinatorics, intersecting family
Status: OPEN, 0 comments on erdosproblems.com
No formalized statement in the Formal Conjectures repo.

## WHAT THIS IS SAYING (plain English):

Take any "downward-closed" family of sets (if a set is in the family, all its subsets 
are too — this is called a "simplicial complex" or "ideal" in combinatorics).

The conjecture says: there's always some element x that is "most popular" in the sense 
that the number of sets containing x is at least as large as any intersecting subfamily.

An intersecting subfamily is one where every pair of sets shares at least one common element.

## WHY THIS IS FAMOUS

This is CHVÁTAL'S CONJECTURE from 1974. It's one of the most well-known open problems 
in extremal set theory. It generalizes the Erdős-Ko-Rado theorem to non-uniform settings.

## KNOWN RESULTS

1. TRUE for "near-cone" complexes (Snevily)
2. TRUE for shifted/compressed families
3. TRUE when the ground set is small (computational verification)
4. The EKR theorem (uniform case) is a special case
5. Woodroofe gave EKR-type results for near-cone complexes via algebraic shifting

## MY ASSESSMENT

### This is NOT a good target for us. Here's why:

1. It's CHVÁTAL'S CONJECTURE — one of the most famous open problems in extremal 
   combinatorics. Open for 50+ years. Multiple experts have worked on it.

2. It's NOT decidable or reducible to computation. The problem says "for ALL 
   downward-closed families." That's an infinite class.

3. The 0 comments aren't because nobody has looked at it. They're because everyone 
   KNOWS this is hard and has nothing new to add.

4. The techniques from the other intersecting family problems (21, 56, 534, 844) 
   may not transfer because those are more specific (uniform families, weakly 
   divisible sets, etc.) while 701 is maximally general.

5. The $500 Problem 21 (Ahlswede-Khachatrian) was about t-intersecting uniform 
   families — a much more structured setting than general simplicial complexes.

### RECOMMENDATION: ABANDON 701. Focus on 848 and 686.

The intersecting family pattern I hypothesized (solved neighbors → technique transfer) 
DOES NOT APPLY here because 701 is qualitatively different from its neighbors. 
It's the GENERAL case while the solved problems are SPECIAL cases.

This is the risk I flagged in active-hypotheses.md: "People looked and it's obviously hard."
Confirmed — it's Chvátal's conjecture. Walk away.
