/* search_a8.gp — Search for a(8) in Erdős Problem #396
 *
 * a(n) = smallest k such that k(k-1)...(k-n) | C(2k, k)
 *
 * Strategy: For each candidate k, check the p-adic valuation condition
 * at every prime p. Fail fast: check small primes first since they are
 * most likely to be the bottleneck (the product of 9 consecutive integers
 * has high 2-adic and 3-adic valuations).
 *
 * Optimization: for prime p, the condition is
 *   Σ_{i=0}^{8} ν_p(k-i) ≤ carries(k, p)
 *
 * For p > 8: at most one of k, k-1, ..., k-8 is divisible by p,
 * so the LHS is just ν_p(k-j) for one j. The RHS (carries) grows
 * with k. So large primes are rarely the bottleneck.
 *
 * For p ≤ 8 (i.e., p = 2, 3, 5, 7): the product of 9 consecutive
 * integers always has significant p-adic valuation. These are checked first.
 */

/* ========== Core functions ========== */

/* Count carries when doubling k in base p = ν_p(C(2k,k)) by Kummer */
count_carries(k, p) =
{
  my(carry = 0, count = 0, m = k);
  while (m > 0 || carry > 0,
    my(d = m % p);
    my(s = 2*d + carry);
    if (s >= p, count++; carry = s \ p, carry = 0);
    m = m \ p;
  );
  return(count);
}

/* Compute ν_p(n) */
val_p(n, p) =
{
  if (n == 0, return(99999));  \\ effectively +oo
  my(v = 0);
  while (n % p == 0, v++; n \= p);
  return(v);
}

/* Sum of ν_p(k-i) for i=0..n */
product_valuation(k, n, p) =
{
  my(s = 0);
  for(i = 0, n, s += val_p(k - i, p));
  return(s);
}

/* ========== Fast check ========== */

/* Check divisibility condition for a single prime p.
 * Returns 1 if OK, 0 if fails at this prime. */
check_prime(k, n, p) =
{
  my(pv = product_valuation(k, n, p));
  if (pv == 0, return(1));  \\ no constraint from this prime
  my(carries = count_carries(k, p));
  return(pv <= carries);
}

/* Full divisibility check with early termination on small primes.
 * n = 8 for a(8). Returns 1 if k(k-1)...(k-8) | C(2k,k). */
check_k(k, n) =
{
  /* Check small primes first — most likely to fail */
  if (!check_prime(k, n, 2), return(0));
  if (!check_prime(k, n, 3), return(0));
  if (!check_prime(k, n, 5), return(0));
  if (!check_prime(k, n, 7), return(0));

  /* Check remaining primes up to k.
   * For p > n, at most one term k-i is divisible by p.
   * For p > sqrt(k), ν_p(k-i) ≤ 1 for all i, so the condition
   * is: (1 if p | some k-i) ≤ carries(k,p).
   * carries(k,p) = 0 only if all base-p digits of k are < p/2.
   * For p > sqrt(k), k has at most 2 digits in base p.
   * First digit < p/2 means k < p*p/2, so k < p^2/2.
   * This is almost always satisfied for large p.
   */
  forprime(p = 11, k,
    if (!check_prime(k, n, p), return(0));
  );
  return(1);
}

/* ========== Search ========== */

{
  my(n = 8);
  my(start_k = 2);  \\ Set higher to resume search, e.g., start_k = 101130030

  /* CONFIGURATION: Change start_k here to resume from a checkpoint */
  \\ start_k = 101130030;  \\ Uncomment to start from after a(7)

  printf("=== Searching for a(%d) ===\n", n);
  printf("Starting from k = %d\n", start_k);
  printf("Checking condition: k(k-1)...(k-%d) | C(2k,k)\n\n", n);

  my(checked = 0);
  my(t0 = getwalltime());

  for(k = start_k, 10^12,
    checked++;

    if (checked % 1000000 == 0,
      my(elapsed = (getwalltime() - t0) / 1000.0);
      my(rate = checked / elapsed);
      printf("Progress: k = %d, checked %d values, %.1f sec, %.0f k/sec\n",
             k, checked, elapsed, rate);
    );

    if (check_k(k, n),
      my(elapsed = (getwalltime() - t0) / 1000.0);
      printf("\n*** FOUND: a(%d) = %d ***\n", n, k);
      printf("After checking %d values in %.1f seconds\n", checked, elapsed);

      /* Verify by showing the slack at each small prime */
      printf("\nVerification (slack at small primes):\n");
      forprime(p = 2, 30,
        my(pv = product_valuation(k, n, p));
        my(carries = count_carries(k, p));
        if (pv > 0,
          printf("  p=%d: product_val=%d, carries=%d, slack=%d\n",
                 p, pv, carries, carries - pv);
        );
      );
      break;
    );
  );
}
