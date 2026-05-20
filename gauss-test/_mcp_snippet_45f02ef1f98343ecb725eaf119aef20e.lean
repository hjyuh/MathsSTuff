import Mathlib

open Nat

-- Check: descFactorial 1 1 = 1
#eval descFactorial 1 1  -- should be 1
#eval centralBinom 1      -- should be 2

-- Check: descFactorial 2 2 = 2
#eval descFactorial 2 2  -- should be 2
#eval centralBinom 2      -- should be 6

-- Check k=2: descFactorial 2480 3
#eval descFactorial 2480 3  -- should be 2480*2479*2478
#eval centralBinom 2480 % descFactorial 2480 3  -- should be 0
