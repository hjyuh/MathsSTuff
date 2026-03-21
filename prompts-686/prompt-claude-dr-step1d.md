# PROMPT FOR CLAUDE DR — Step 1D: Paper Decomposition
# Paste this entire thing into a new Claude Deep Research chat.

---

You are operating as part of a multi-model research pipeline targeting Erdős Problem 686. You are communicating with another model, not a student. Be direct. Commit to claims. Flag errors without softening. No summaries — decompose.

## Your Role: Step 1D — Lemma Decomposition

## The Target Problem (686)

Can every integer N ≥ 2 be written as N = ∏_{1≤i≤k}(m+i) / ∏_{1≤i≤k}(n+i) for some k ≥ 2 and m ≥ n+k?

Status: Open. Computational verification shows all N ≤ 100 work EXCEPT {4, 25, 49, 64, 81} (all perfect powers). Tao has linked this problem to Problem 388 via the Beukers-Shorey-Tijdeman (1999) framework.

## What I Need You To Do

Find and deeply decompose TWO papers. Not summarize — decompose into individual lemmas as reusable parts.

### Paper 1: Beukers, Shorey, and Tijdeman (1999)
This paper concerns products of consecutive integers and their Diophantine properties. Find the paper (likely in Acta Arithmetica or a comparable journal) and for EVERY key lemma or proposition:

(a) State the result abstractly, stripped of the paper's specific context. What is the purely structural claim?
(b) What property of the objects does this lemma exploit? Be specific — "divisibility" is too vague. What specific structural property?
(c) Is the lemma STRONGER than what the authors actually needed? If so, state the more general version.
(d) What other mathematical objects have the same structural property exploited in (b)?
(e) Could this lemma apply to the equation f_k(x) = N · f_k(y), where f_k(x) = x(x+1)···(x+k-1)? This is Problem 686 rearranged. Be specific about what works and what breaks.

### Paper 2: Kulkarni and Sury (2003, Indagationes Mathematicae 14(3-4), pp. 457-462)
Their "Theorem C" classifies when f(x) = g(y) has infinitely many solutions via three exceptional families. Decompose:

(a) Each step of the exceptional family elimination (power compositions, Dickson polynomials, degree-4 special case).
(b) What structural property of f_k(x) = x(x+1)···(x+k-1) makes each elimination work? Specifically: the roots form an arithmetic progression — how is this used?
(c) Does Theorem C apply to equations of the form f(x) = c · g(y) where c is a fixed integer? If not, what modification is needed? If yes, what changes in the exceptional family analysis?
(d) The Bilu-Tichy theorem (2000) is a predecessor. What does Kulkarni-Sury add beyond Bilu-Tichy, and does that addition matter for the ratio equation in 686?

### Also Search For:
Any paper that directly addresses the representability of integers as ratios of products of consecutive integers, or ratios of binomial coefficients C(m+k,k)/C(n+k,k). This specific problem may have been studied under different terminology.

## Context From Prior Work on Problem 388

A collaborator applied Kulkarni-Sury Theorem C to prove: for fixed k₁ ≠ k₂ with both ≥ 4, the equation f_{k₁}(x) = f_{k₂}(y) has only finitely many integer solutions. The elimination of the three exceptional families works because f_k has roots in arithmetic progression, which prevents decomposition through Dickson polynomials or power compositions.

The open question from 388: does this finiteness extend uniformly across all pairs (k₁, k₂)?

Tao's comment connecting 388 to 686: "Some of the recent progress on #686 may be transferable to this problem."

## Output Format

For each lemma you decompose, use this structure:

**Lemma [number] from [Paper]:**
- Abstract statement (context-free):
- Structural property exploited:
- Stronger than needed? If so, general version:
- Other objects with same property:
- Applies to 686's ratio equation? Specifically:

At the end, give your assessment: which decomposed lemma is MOST LIKELY to transfer to 686, and why?
