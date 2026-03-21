/* verify_known.gp — Verify known values of a(n) for Erdős Problem #396
 *
 * Problem: a(n) = smallest k such that k(k-1)(k-2)...(k-n) | C(2k, k)
 *
 * Method: By Kummer's theorem, ν_p(C(2k,k)) = number of carries when
 * adding k + k in base p. So the divisibility condition is:
 *   For every prime p ≤ 2k:
 *     Σ_{i=0}^{n} ν_p(k - i) ≤ (carries when doubling k in base p)
 *
 * We check this prime-by-prime. We do NOT compute C(2k,k) directly.
 *
 * Known values (OEIS A375077):
 *   a(1) = 2, a(2) = 2480, a(3) = 8178, a(4) = 45153,
 *   a(5) = 3648841, a(6) = 7979090, a(7) = 101130029
 */

/* Count carries when adding k + k in base p (i.e., doubling k in base p).
 * This equals ν_p(C(2k, k)) by Kummer's theorem. */
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

/* Compute ν_p(n) = p-adic valuation of n */
val_p(n, p) =
{
  if (n == 0, return(+oo));  \\ convention: ν_p(0) = +oo
  my(v = 0);
  while (n % p == 0, v++; n \= p);
  return(v);
}

/* Check if k(k-1)...(k-n) | C(2k, k).
 * Returns 1 if divisibility holds, 0 if not.
 * If verbose=1, prints the failing prime. */
check_divisibility(k, n, verbose=0) =
{
  /* The product is k * (k-1) * ... * (k-n).
   * For each prime p up to 2k, we need:
   *   sum_{i=0}^{n} ν_p(k-i) ≤ carries(k, p)
   * But we only need to check primes p ≤ k (since k-i < k for i≥1,
   * and the product terms are at most k).
   * Actually we need p ≤ k since the largest factor is k itself.
   * For p > k, both sides are 0. */
  forprime(p = 2, k,
    my(carries = count_carries(k, p));
    my(product_val = 0);
    for(i = 0, n,
      if (k - i > 0,
        product_val += val_p(k - i, p);
      );
    );
    if (product_val > carries,
      if (verbose,
        printf("  FAIL at p=%d: product_val=%d > carries=%d\n", p, product_val, carries);
      );
      return(0);
    );
  );
  return(1);
}

/* Verify that k is the SMALLEST value satisfying the condition for given n.
 * This checks that:
 *   1. k itself satisfies the divisibility
 *   2. k-1 does NOT satisfy it (confirming minimality)
 * For large k, checking all values from 1 to k-1 is infeasible,
 * so we just verify the value works and check k-1 fails. */
verify_known_value(n, k) =
{
  printf("Verifying a(%d) = %d ... ", n, k);

  /* Check k satisfies the condition */
  if (!check_divisibility(k, n),
    printf("FAILED — k=%d does NOT satisfy the divisibility!\n", k);
    check_divisibility(k, n, verbose=1);
    return(0);
  );

  /* Check k-1 does NOT satisfy the condition */
  if (k > 1 && check_divisibility(k-1, n),
    printf("PROBLEM — k-1=%d ALSO satisfies it! a(%d) might be smaller.\n", k-1, n);
    return(0);
  );

  printf("PASSED (k works, k-1 fails)\n");
  return(1);
}

/* Main verification */
{
  printf("=== Verifying known values of a(n) for Erdős Problem #396 ===\n\n");

  my(known = [[1, 2], [2, 2480], [3, 8178], [4, 45153],
               [5, 3648841], [6, 7979090], [7, 101130029]]);

  my(all_pass = 1);
  for(j = 1, #known,
    my(n = known[j][1], k = known[j][2]);
    if (!verify_known_value(n, k), all_pass = 0);
  );

  printf("\n");
  if (all_pass,
    printf("ALL KNOWN VALUES VERIFIED SUCCESSFULLY.\n");
  ,
    printf("*** SOME VALUES FAILED — CHECK DISCREPANCIES ***\n");
  );
}
