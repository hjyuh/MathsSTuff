# EP-488: v8.2 — The Closing Question
## April 8, 2026. Current: 88%. One question remains.

---

## THE SITUATION

Three independent models (Codex B, 5.2, 5.4) proved the same theorem:

**Lifted {2,3}-Core Safety:** If A = dC with 2,3 ∈ C primitive,
then 2mF_A(n) - nF_A(m) > 0 for all m > n ≥ max(A).

Combined with superadditivity (component reduction) and all prior
results, EP-488 reduces to ONE structural question.

---

## THE CLOSING QUESTION (two parts)

Let C be an n-LCM connected component of a primitive set A.
Assume C contains a bad layer (some element with L_K(s) = 1, E > 0).
Assume C does NOT contain literal 2 or literal 3.

**Part 1:** Must gcd(C) > 1?

**Part 2:** If gcd(C) = d > 1 and we write C = dB, must 2,3 ∈ B?

If BOTH parts are YES → Lifted {2,3}-Core Safety applies → EP-488 proved.

---

## WHY PART 1 MIGHT BE TRUE

A bad layer a needs a 2-witness b ∈ A with b/gcd(b,a) = 2.
So b = 2g where g = gcd(b,a), and g | a.
Since b ≠ 2 (no literal 2 in C): g ≥ 2.
So gcd(a,b) = g ≥ 2. Elements a and b share a factor ≥ 2.

Similarly, a needs a 3-witness c ∈ A with c/gcd(c,a) = 3.
So c = 3h where h = gcd(c,a), and h | a.
Since c ≠ 3 (no literal 3 in C): h ≥ 2.
So gcd(a,c) = h ≥ 2. Elements a and c share a factor ≥ 2.

Now: b is in the same n-LCM component as a (by Lemma D: lcm(a,b) ≤ n).
And c is in the same component. If the component is connected, every
element is reachable from a through edges with lcm ≤ n.

For gcd(C) > 1: need a single prime p dividing ALL elements.

From a's perspective: g | a and g | b, h | a and h | c.
If g and h share a prime p: then p | a, p | b, p | c.
Does p propagate to ALL elements of C through the n-LCM graph?

KEY STRUCTURAL FACT: If element x is in C and x ~ y (edge), then
lcm(x,y) ≤ n, so gcd(x,y) = xy/lcm(x,y) ≥ xy/n.
Since both x,y ≤ n (they're in A with n ≥ max(A)):
gcd(x,y) ≥ xy/n ≥ x·y/n.

For compact elements (x,y > n/20): gcd ≥ (n/20)²/n = n/400.
So every edge in the compact band forces a large shared gcd.

---

## WHY PART 2 MIGHT BE TRUE

If gcd(C) = d > 1 and C = dB:
- The bad layer a = d·(a/d). Its 2-witness is b = 2g = d·(2g/d).
  For 2 ∈ B: need 2g/d to equal 2, i.e., g = d.
  That means gcd(b,a) = d, i.e., b = 2d.

But g = gcd(b,a) might not equal d. It could be a multiple of d
(since d | a and d | b, we have d | g). So g = d·g' for some g' ≥ 1.
Then b = 2dg' and a = d·(hg'/something)... this gets complicated.

Actually: since d | a and d | b: g = gcd(a,b) ≥ d. So g = d·g'
with g' | (a/d) and g' | (b/d). The quotient b/g = 2, so b = 2g = 2dg'.
In B: b/d = 2g'. For 2 ∈ B: need g' = 1, i.e., g = d, i.e., b = 2d.

IS b = 2d ALWAYS the 2-witness? Not necessarily. The 2-witness b
satisfies b/gcd(b,a) = 2. There might be multiple valid 2-witnesses.
The question is whether SOME 2-witness has g = d (i.e., is exactly 2d).

If 2d ∈ A and gcd(2d, a) = d and 2d/d = 2: then 2d IS a valid
2-witness for a. But 2d might not be in A.

---

## A POTENTIAL COUNTEREXAMPLE TO PART 2

Consider: d = 6, C = {12, 18, 35·6} = {12, 18, 210}.
C = 6·{2, 3, 35}. gcd(C) = 6. B = {2, 3, 35}. 2,3 ∈ B. ✓

But what about: d = 6, C = {42, 66, 210}?
C = 6·{7, 11, 35}. gcd(C) = 6. B = {7, 11, 35}. 2 ∉ B, 3 ∉ B. ✗

Is 210 a bad layer here? Check: B_{210} would include quotients from
42 and 66. 42/gcd(42,210) = 42/42 = 1 (not > 1, so no obstruction).
66/gcd(66,210) = 66/6 = 11. So K_{210} = {11}. Not ⊇ {2,3}.
So 210 is NOT a bad layer requiring {2,3}. No problem.

But CAN we construct a component with gcd = d where B doesn't
contain 2,3, yet some element IS bad with {2,3} in kernel?

For {2,3} ⊆ K_a: need witnesses creating quotients 2 and 3.
2-witness b with b/gcd(b,a) = 2. In C = dB: b = d·b', a = d·a'.
gcd(b,a) = d·gcd(b',a'). Quotient = b'/gcd(b',a') = 2.
So b' = 2·gcd(b',a') and b' ∈ B.

For 2 ∈ B: need b' = 2 (with gcd(2,a') = 1, quotient = 2). That
requires gcd(2,a') = 1, i.e., a' is odd.
If a' is odd and b' gives quotient 2: b' = 2·gcd(b',a').
gcd(b',a') could be > 1 (e.g., b' = 10, a' = 15, gcd = 5, quot = 2).
Then b' = 10 ∈ B but 2 ∉ B.

So YES: it's possible for B to NOT contain literal 2 while still
having a quotient-2 obstruction through a composite element of B.

THIS MEANS PART 2 CAN FAIL. gcd(C) > 1 does NOT guarantee 2,3 ∈ B.

---

## THE REFINED CLOSING QUESTION

Part 2 as stated is FALSE. A component can have gcd > 1 but the
reduced set B need not contain 2 or 3.

So Lifted {2,3}-Core Safety does NOT automatically apply even if
gcd(C) > 1. We need a DIFFERENT closing argument.

POSSIBLE REPAIRS:

### Repair A: Recursive Reduction
If C = dB and B has a bad layer, apply the same analysis to B.
B is a smaller primitive set. Eventually either:
- You reach a set containing literal 2,3 → Theorem applies
- Or gcd keeps being > 1 → C = d₁d₂d₃...·B' with shrinking B'
- Since elements are finite, this terminates

### Repair B: Direct Budget Bound for dB without 2,3 ∈ B
Maybe {2,3} ∈ B isn't needed. The key is that SOME coverage
exists in B. If B has enough density, the budget is positive.
The 2/3 coverage from {2,3} was convenient but not the only way.

### Repair C: Prove gcd(C) > 1 AND the recursive structure
Show that the reduction C → B → B' → ... eventually reaches {2,3}.

### Repair D: Surplus Dominance directly
Bypass the component structure entirely. Prove 2mH_A(n) ≥ nH_A(m)
for all primitive A. Scale-independent, no components needed.

---

## YOUR TASK

The Closing Question has a subtlety: Part 2 can fail.
Find the right closing argument. Options:

1. Prove Part 1 (gcd > 1) and then handle Part 2 failure via
   recursive reduction or direct density argument.
2. Prove a stronger version of Lifted Core Safety that doesn't
   need 2,3 ∈ B — just some density condition on B.
3. Prove Surplus Dominance directly (bypasses everything).
4. Find a counterexample showing Part 1 also fails (gcd(C) = 1
   possible with bad layers and no literal 2,3).

75 kills. 25+ proved results. 88%. The gap is precise.
Close it.
