This project was edited by [Aristotle](https://aristotle.harmonic.fun).

To cite Aristotle:
- Tag @Aristotle-Harmonic on GitHub PRs/issues
- Add as co-author to commits:
```
Co-authored-by: Aristotle (Harmonic) <aristotle-harmonic@harmonic.fun>
```

# Aristotle Submission: Adjacent Pair Global Max Theorem
## April 12, 2026

### What this formalizes
The Adjacent Pair Global Max Theorem (proved informally by Codex BA):

For Q = {q-1, q} with q ≥ 3, the global maximum of O_Q(n,m) = 2·A_Q(n)/n - A_Q(m)/m
over all integers m > n ≥ q occurs at (n,m) = (2q-3, (q-1)²), with value
1 - (4q-5)/((2q-3)(q-1)²).

### Proof structure (from route2-adjacent-pair-global-max.md)
The proof decomposes into two independent optimizations:
- Lemma 1: max A(n)/n over n ≥ q is at n = 2q-3 (unique)
- Lemma 2: min A(m)/m over m ≥ 1 is at m = (q-1)² (unique, via periodicity mod L=q(q-1))
- Finish: O(n,m) = 2·A(n)/n - A(m)/m ≤ 2·max - min = O(2q-3, (q-1)²)

### Source
Informal proof: `../../route2-adjacent-pair-global-max.md`
Depends on: definitions from `../ep488_pairs_aristotle/ep488_pairs.lean` (already verified)

### Aristotle prompt
"Fill all the sorries in the given file. Use auxiliary lemmas that would help
prove the main goal in this file. Write mathlib quality code where possible."

### Status
Submitted: April 12, 2026
Status: PENDING
