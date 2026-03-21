# Literature Summary — Erdős Problem #396

## Problem Statement (from erdosproblems.com)

For every positive integer k, does there exist n such that
∏_{0 ≤ i ≤ k} (n - i) | C(2n, n)?

Equivalently: let a(k) = smallest n such that n(n-1)...(n-k) | C(2n,n). Is a(k) finite for all k?

**Status:** Open.
**Source:** Erdős-Graham (1980).
**OEIS:** A375077.
**Formalized:** Yes (Lean, formal-conjectures repository).

---

## Known Results Cited on the Problem Page

### Pomerance (2014) [Po14]
- For any k ≥ 0, **infinitely many** n satisfy (n-k) | C(2n,n), though this set has upper density < 1/3.
- The set of n where ∏_{1 ≤ i ≤ k} (n+i) | C(2n,n) has density 1.
- Note: Pomerance's result is about a *single* factor (n-k), not the full product.

### Erdős-Graham observation
- n+1 always divides C(2n,n) (Catalan numbers), but divisibility by n itself is rare.

---

## Forum Thread (erdosproblems.com/forum/thread/396)

### Terence Tao — Comment posted 03:59 on 29 Sep 2025

Tao explained the core difficulty involves two stages:

1. **Finding consecutive smooth numbers** in the required range
2. **Ensuring these don't fall into exceptional sets** where base-p expansions are unfavorable for Kummer's theorem

He identified this as a technical obstacle involving number-theoretic properties of the binomial coefficient. The challenge is that the divisibility condition must hold *simultaneously* at all primes, and the base-p digit constraints interact in complex ways.

### Other activity
- User "thomas" marked the problem as "finds it tractable"
- No other substantive comments
- No one listed as currently working on it
- No one listed as interested in collaborating

---

## Key Takeaways

1. **Pomerance's result** handles single factors (n-k) | C(2n,n) but NOT the full product. There's a gap between "each factor divides individually for some n" and "all factors divide simultaneously for one n."

2. **Tao's comment** points directly at the carry-counting / base-p digit obstacle — exactly the approach used in #728. This suggests the #728 machinery is the right tool.

3. **Minimal community attention** — only 1 forum comment, no one actively working on it. This is an opportunity.

4. **The problem is formalized in Lean** — we can potentially contribute a Lean proof if we find one.

---

*Compiled by Claude Code, March 15, 2026*
