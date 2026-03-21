/* digit_analysis.gp — Analyze digit patterns in known a(n) values
 *
 * For each known a(n), we compute:
 *   - Base-2, 3, 5 representations
 *   - Carry counts when doubling in base 2, 3, 5
 *   - p-adic valuations of the product k(k-1)...(k-n) for p=2,3,5
 *   - Slack = carries - product_valuation at each prime
 *
 * Goal: identify which prime is the bottleneck (tightest constraint)
 * and see if there's a digit pattern that makes these k values special.
 */

/* ========== Utility functions ========== */

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

val_p(n, p) =
{
  if (n == 0, return(99999));
  my(v = 0);
  while (n % p == 0, v++; n \= p);
  return(v);
}

product_valuation(k, n, p) =
{
  my(s = 0);
  for(i = 0, n, s += val_p(k - i, p));
  return(s);
}

/* Convert k to a string of its base-p digits (most significant first) */
base_p_string(k, p) =
{
  if (k == 0, return("0"));
  my(digits = [], m = k);
  while (m > 0,
    digits = concat([m % p], digits);
    m \= p;
  );
  my(s = "");
  for(i = 1, #digits,
    s = concat(s, Str(digits[i]));
    if (i < #digits && (i % 4 == (#digits % 4)), s = concat(s, " "));
  );
  return(s);
}

/* Count digits in base p */
digit_count(k, p) =
{
  if (k == 0, return(1));
  my(c = 0, m = k);
  while (m > 0, c++; m \= p);
  return(c);
}

/* Digit sum in base p */
digit_sum(k, p) =
{
  my(s = 0, m = k);
  while (m > 0, s += m % p; m \= p);
  return(s);
}

/* Count how many base-p digits are ≥ ceil(p/2) */
high_digits(k, p) =
{
  my(threshold = (p + 1) \ 2, count = 0, m = k);
  while (m > 0,
    if (m % p >= threshold, count++);
    m \= p;
  );
  return(count);
}

/* ========== Main analysis ========== */

{
  my(known = [[1, 2], [2, 2480], [3, 8178], [4, 45153],
               [5, 3648841], [6, 7979090], [7, 101130029]]);

  my(primes_to_check = [2, 3, 5, 7, 11, 13]);

  for(j = 1, #known,
    my(n = known[j][1], k = known[j][2]);

    printf("============================================================\n");
    printf("a(%d) = %d\n", n, k);
    printf("============================================================\n\n");

    /* Base representations */
    printf("Base-2:  %s\n", base_p_string(k, 2));
    printf("Base-3:  %s\n", base_p_string(k, 3));
    printf("Base-5:  %s\n", base_p_string(k, 5));
    printf("Base-7:  %s\n", base_p_string(k, 7));
    printf("\n");

    /* Digit statistics */
    printf("Digit counts:  base2=%d, base3=%d, base5=%d\n",
           digit_count(k, 2), digit_count(k, 3), digit_count(k, 5));
    printf("Digit sums:    base2=%d, base3=%d, base5=%d\n",
           digit_sum(k, 2), digit_sum(k, 3), digit_sum(k, 5));
    printf("High digits:   base2=%d/%d, base3=%d/%d, base5=%d/%d\n",
           high_digits(k, 2), digit_count(k, 2),
           high_digits(k, 3), digit_count(k, 3),
           high_digits(k, 5), digit_count(k, 5));
    printf("\n");

    /* Carries and valuations */
    printf("Prime | Carries | Product_val | Slack | Carry_density\n");
    printf("------+---------+-------------+-------+--------------\n");

    my(tightest_prime = 0, tightest_slack = 99999);

    for(pi = 1, #primes_to_check,
      my(p = primes_to_check[pi]);
      my(carries = count_carries(k, p));
      my(pv = product_valuation(k, n, p));
      my(slack = carries - pv);
      my(ndigits = digit_count(k, p));
      my(density = 1.0 * carries / ndigits);

      printf("  %3d | %7d | %11d | %5d | %.4f\n",
             p, carries, pv, slack, density);

      if (pv > 0 && slack < tightest_slack,
        tightest_slack = slack;
        tightest_prime = p;
      );
    );

    printf("\nTightest prime: p = %d (slack = %d)\n", tightest_prime, tightest_slack);

    /* Show the product terms and their valuations at tightest prime */
    if (tightest_prime > 0,
      my(p = tightest_prime);
      printf("Product terms at p=%d: ", p);
      for(i = 0, n,
        printf("v(%d)=%d ", k-i, val_p(k-i, p));
      );
      printf("\n");
    );

    printf("\n\n");
  );
}
