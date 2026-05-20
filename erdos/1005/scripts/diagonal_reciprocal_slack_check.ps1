param(
    [int]$NMax = 1000,
    [int]$MaxSurplus = 1
)

$code = @'
using System;

public static class DiagonalReciprocalSlackCheck {
    static int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a < 0 ? -a : a;
    }

    static int Predicted(int n) {
        int[] d = {1, 2, 2, 4};
        return n / 4 + d[n & 3];
    }

    static int RowCount(int lo, int hi, int modulus) {
        if (hi < lo) {
            return 0;
        }
        if (modulus == 1) {
            return hi - lo + 1;
        }
        int total = 0;
        for (int p = lo; p <= hi; p++) {
            if (Gcd(p, modulus) == 1) {
                total++;
            }
        }
        return total;
    }

    static int Certificate(int n, int a, int h, int r) {
        int sigma = n - (h * a + r);
        int total = 1;
        for (int j = 1; j < r; j++) {
            int lo = (a * j) / r + 1;
            int hi = a + (r + sigma - j) / h;
            total += RowCount(lo, hi, j);
        }

        int c = h + 1 - r;
        for (int k = 1; k < c; k++) {
            int lo = ((a + 1) * k) / c + 1;
            int hi = a + (r + sigma + k) / h;
            total += RowCount(lo, hi, k);
        }
        return total;
    }

    public static void Run(int nMax, int maxSurplus) {
        long checkedTriples = 0;
        int recordCount = 0;
        int bad = 0;
        int minSurplus = Int32.MaxValue;
        string minRows = "";

        for (int n = 92; n <= nMax; n++) {
            int target = Predicted(n);
            for (int h = 4; h <= n; h++) {
                for (int a = 1; a <= n / h; a++) {
                    int maxR = Math.Min(Math.Min(h, a - 1), n - h * a);
                    for (int r = 1; r <= maxR; r++) {
                        int c = h + 1 - r;
                        if (Gcd(a, r) != 1 || Gcd(a + 1, c) != 1) {
                            continue;
                        }
                        int q = h * a + r;
                        int lower = Certificate(n, a, h, r);
                        int surplus = lower - target;
                        checkedTriples++;

                        if (surplus < minSurplus) {
                            minSurplus = surplus;
                            minRows = String.Format(
                                "surplus={0} n={1} q={2} sigma={3} h={4} a={5} r={6} lower={7} target={8} C={9}",
                                surplus, n, q, n - q, h, a, r, lower, target, c
                            );
                        }

                        if (surplus < 0) {
                            bad++;
                            if (bad <= 20) {
                                Console.WriteLine(String.Format(
                                    "BAD surplus={0} n={1} q={2} sigma={3} h={4} a={5} r={6} lower={7} target={8} C={9}",
                                    surplus, n, q, n - q, h, a, r, lower, target, c
                                ));
                            }
                        }

                        if (surplus <= maxSurplus) {
                            recordCount++;
                            Console.WriteLine(String.Format(
                                "RECORD surplus={0} n={1} q={2} sigma={3} h={4} a={5} r={6} lower={7} target={8} C={9}",
                                surplus, n, q, n - q, h, a, r, lower, target, c
                            ));
                        }
                    }
                }
            }
        }

        Console.WriteLine(String.Format("checked={0}", checkedTriples));
        Console.WriteLine(String.Format("bad={0}", bad));
        Console.WriteLine(String.Format("records={0}", recordCount));
        Console.WriteLine(String.Format("minSurplus={0}", minSurplus));
        Console.WriteLine(String.Format("minRows={0}", minRows));
    }
}
'@

Add-Type -TypeDefinition $code -Language CSharp
[DiagonalReciprocalSlackCheck]::Run($NMax, $MaxSurplus)

