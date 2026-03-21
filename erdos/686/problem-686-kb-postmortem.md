# Problem 686 — KB Observation Post-Mortem
## March 15, 2026

## What Codex Killed

### Claim A (the "iff"): KILLED
- KB gives sufficient condition only, not necessary
- Counterexample: k=2, N=4. z²-4 is reducible but x(x+1)-4y(y+1) is irreducible
- The entire reducibility table built from perfect-power detection is wrong
- BST Theorem 2.1 gives the actual irreducibility classification for this family

### Claim B (even/odd pattern): KILLED  
- "Prime squares are reducible at every even k" is false at k=2
- The Pell equation IS the whole irreducible conic, not a reducible component
- Algebraic irreducibility ≠ arithmetic reductions (natso26's k=4→k=2 trick)

### Claim C (explains stuck squares): KILLED
- The mechanism "perfect powers → reducible → stuck" is not true for this family
- The real structural split is by k (conic at k=2, genus 1 at k=3, genus>1 at k≥5)
- Not about N being a perfect power at all

### Claim D (k=3 question): WOUNDED → SURVIVES as subproblem
- Valid as one concrete question, not as THE key question
- Demote to: "determine admissible integral points on k=3 genus-1 curves for square N"

## What Survived

1. KB does apply correctly to this polynomial family (sufficient direction)
2. The genus structure is real: k=3 is genus 1, k≥5 is genus >1 (from BST)
3. The k=3 subproblem for prime squares is genuinely open
4. Our computation to N ≤ 10,000 is still novel data

## Novelty: Dead

- BST (1999) already studies F_m(X) - λF_n(Y) for this exact family
- Tao cited BST on March 3, 2026 on the forum
- MalekZ suggested KB on March 15, 2026 on the forum
- We are restating known theory, not discovering new structure

## Lessons

1. The pre-emptive arguments worked — every flagged weakness was real
2. But the UNFLAGGED weakness (counterexample killing the whole table) was worse
3. "Novel framework" claims are dangerous when the framework has a 1999 paper
4. Always read the actual paper (BST) before building on what you think it says
5. The adversarial process saved us from posting this publicly

## What To Do Now

The KB direction as an "observation" is dead. What remains:

1. **Read BST (1999) properly.** It's the actual framework. Everything we tried 
   to build, they already built. Read their Theorems 2.1 and 2.2.

2. **The k=3 subproblem is real.** For each stuck square N ∈ {4, 25, 49, 64, 81}, 
   the k=3 curve is genus 1. Compute these specific elliptic curves explicitly, 
   find their Cremona labels, check if they have integer points. This is concrete 
   math, not framework speculation.

3. **The computation to N ≤ 10,000 is still novel.** Post that data, properly 
   contextualized, without any theoretical claims attached.

4. **The 677-678 transfer direction is untouched by this review.** It wasn't 
   part of the KB observation. Still worth exploring separately.
