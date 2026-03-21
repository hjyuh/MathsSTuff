/* growth_analysis.gp — Analyze growth patterns in a(1)..a(7)
 *
 * We look for patterns:
 *   - Ratios a(n+1)/a(n)
 *   - log(a(n))/n, log(a(n))/n^2, log(a(n))/n*log(n)
 *   - Fit to C^n, C^(n^2), n!, etc.
 *   - Any regularity
 */

{
  my(a = [2, 2480, 8178, 45153, 3648841, 7979090, 101130029]);
  my(N = #a);

  printf("=== Growth Analysis for a(1)..a(7) ===\n\n");

  /* Raw values */
  printf("n  |  a(n)\n");
  printf("---+------------\n");
  for(n = 1, N,
    printf("%d  |  %d\n", n, a[n]);
  );
  printf("\n");

  /* Ratios */
  printf("=== Consecutive Ratios ===\n");
  printf("a(n+1)/a(n):\n");
  for(n = 1, N-1,
    printf("  a(%d)/a(%d) = %.4f\n", n+1, n, 1.0*a[n+1]/a[n]);
  );
  printf("\n");

  /* Log analysis */
  printf("=== Logarithmic Analysis ===\n");
  printf("n  |  log(a(n))  |  log/n    |  log/n^2  |  log/(n*ln(n))  |  log/n!  \n");
  printf("---+-------------+-----------+-----------+-----------------+----------\n");
  for(n = 1, N,
    my(la = log(1.0*a[n]));
    my(ln_n = if(n > 1, log(1.0*n), 1.0));
    my(nfact = if(n <= 1, 1, n!));
    printf("%d  |  %9.4f  |  %7.4f  |  %7.4f  |  %13.4f  |  %7.6f\n",
           n, la, la/n, la/n^2, la/(n * ln_n), la/log(1.0*nfact));
  );
  printf("\n");

  /* Check if a(n) ~ C^n */
  printf("=== Exponential Fit: a(n) ~ C^n ===\n");
  printf("C = a(n)^(1/n):\n");
  for(n = 1, N,
    printf("  n=%d: C = %.4f\n", n, exp(log(1.0*a[n])/n));
  );
  printf("\n");

  /* Check if a(n) ~ C^(n^2) */
  printf("=== Super-exponential Fit: a(n) ~ C^(n^2) ===\n");
  printf("C = a(n)^(1/n^2):\n");
  for(n = 1, N,
    printf("  n=%d: C = %.6f\n", n, exp(log(1.0*a[n])/n^2));
  );
  printf("\n");

  /* Check if a(n) ~ (n!)^alpha */
  printf("=== Factorial Fit: a(n) ~ (n!)^alpha ===\n");
  printf("alpha = log(a(n))/log(n!):\n");
  for(n = 2, N,
    my(la = log(1.0*a[n]));
    my(lf = log(1.0*n!));
    printf("  n=%d: alpha = %.4f\n", n, la/lf);
  );
  printf("\n");

  /* Check if a(n) ~ n^(Cn) */
  printf("=== Power-tower Fit: a(n) ~ n^(C*n) ===\n");
  printf("C = log(a(n))/(n*log(n)):\n");
  for(n = 2, N,
    my(la = log(1.0*a[n]));
    my(ln = log(1.0*n));
    printf("  n=%d: C = %.4f\n", n, la/(n*ln));
  );
  printf("\n");

  /* Second differences of log */
  printf("=== Second Differences of log(a(n)) ===\n");
  my(logs = vector(N, n, log(1.0*a[n])));
  printf("First differences (Δ log a):\n");
  for(n = 1, N-1,
    printf("  Δ_%d = %.4f\n", n, logs[n+1] - logs[n]);
  );
  printf("Second differences (Δ² log a):\n");
  for(n = 1, N-2,
    my(d2 = logs[n+2] - 2*logs[n+1] + logs[n]);
    printf("  Δ²_%d = %.4f\n", n, d2);
  );
  printf("\n");

  /* Summary */
  printf("=== Summary ===\n");
  printf("The sequence a(1)..a(7) = 2, 2480, 8178, 45153, 3648841, 7979090, 101130029\n");
  printf("Key observations:\n");
  printf("  - The ratios a(n+1)/a(n) are NOT constant (not purely exponential)\n");
  printf("  - The jumps a(4)->a(5) and a(6)->a(7) are much larger than others\n");
  printf("  - This suggests the growth rate may be super-exponential\n");
  printf("  - Check the digit analysis to see which prime is the bottleneck\n");
}
