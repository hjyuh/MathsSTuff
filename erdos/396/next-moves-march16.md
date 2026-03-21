# Next moves after DR literature survey — March 16, 2026

## Priority 1: Find Cumberbatch (2025)
The talk "Smooth Integers with Restricted Digits" at IRIF Numération Seminar (April 2025) is the closest active research to our exact problem. We need:
- The preprint or slides (search arXiv for Cumberbatch + smooth + digits)
- What density results does it prove?
- Does it handle the √x-smooth threshold?
- Can we contact the author?

## Priority 2: Can Fouvry-Mauduit bridge Blocker A?
Fouvry-Mauduit proved BV for the digit-sum function with exponent > 1/2. 
Our Blocker A asks: does a fixed arithmetic progression equidistribute among digit-defined bad sets at many primes?
This is exactly what Fouvry-Mauduit technology addresses — BV for digit conditions.
Send to GPT: "Can the Fouvry-Mauduit BV theorem for digit sums be applied to show that a fixed AP mod M_n equidistributes among carry-defined bad residue classes for primes W < p ≤ √(2X)?"

## Priority 3: Shubin-Müllner for simultaneous carries
Their in-progress work extends Drmota-Mauduit-Rivat to any number of bases simultaneously.
If their result gives equidistribution of simultaneous digit-sum conditions across k bases (= k primes for us), that could handle the joint carry condition at all small primes.
Search for any preprint by Shubin and/or Müllner on simultaneous digit conditions.

## Priority 4: The Holte Markov chain angle
Holte (1997) showed carries in base-b addition form a Markov chain.
Diaconis-Fulman (2009) deepened this.
Could the Markov chain structure of carries give us the independence across primes that the CRT argument needs?
This is a different lens than sieve theory — it's probabilistic/algebraic.

## The web of connected solved problems (Mahmoud's framework)

OUR PROBLEM: Joint digit-smoothness count in a fixed AP
     |
     | remove smoothness requirement
     v
SOLVED: Digit-sum equidistribution in APs (Gel'fond, Mauduit-Rivat)
     
OUR PROBLEM
     |
     | remove digit requirement  
     v
SOLVED: Smooth numbers in APs (Soundararajan-Harper, Pascadi 2025)

OUR PROBLEM
     |
     | remove the AP constraint
     v  
PARTIALLY SOLVED: Smooth integers with restricted digits (Cumberbatch 2025)

OUR PROBLEM
     |
     | weaken to single prime instead of all primes
     v
SOLVED: Carry equidistribution at one prime (Mauduit-Rivat)

The solution should combine techniques from at least two of these solved neighbors.
