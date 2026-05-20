param(
    [int]$QMax = 1000,
    [int]$MaxSurplus = 5
)

$code = @'
using System;

public static class DiagonalNonreciprocalBaseCheck {
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

    static int CountBaseStrip(int a, int h, int r) {
        int c = r - h - 1;
        int total = 0;
        for (int p = 1; p <= a; p++) {
            int lo = (c * p) / (a + 1) + 1;
            int hi = (r * p - 1) / a;
            for (int j = lo; j <= hi; j++) {
                if (Gcd(p, j) == 1) {
                    total++;
                }
            }
        }
        return total;
    }

    public static void Run(int qMax, int maxSurplus) {
        long checkedRows = 0;
        int bad = 0;
        int records = 0;
        int minSurplus = Int32.MaxValue;
        string minRow = "";

        for (int h = 1; h <= qMax; h++) {
            for (int a = 1; h * a <= qMax; a++) {
                int maxR = Math.Min(a - 1, qMax - h * a);
                for (int r = h + 2; r <= maxR; r++) {
                    int c = r - h - 1;
                    if (Gcd(a, r) != 1 || Gcd(a + 1, c) != 1) {
                        continue;
                    }
                    int q = h * a + r;
                    if (q < 92) {
                        continue;
                    }
                    int count = CountBaseStrip(a, h, r);
                    int target = Predicted(q);
                    int surplus = count - target;
                    checkedRows++;
                    if (surplus < minSurplus) {
                        minSurplus = surplus;
                        minRow = String.Format(
                            "q={0} h={1} a={2} r={3} count={4} target={5} surplus={6}",
                            q, h, a, r, count, target, surplus
                        );
                    }
                    if (surplus < 0) {
                        bad++;
                        if (bad <= 20) {
                            Console.WriteLine(String.Format(
                                "BAD q={0} h={1} a={2} r={3} count={4} target={5} surplus={6}",
                                q, h, a, r, count, target, surplus
                            ));
                        }
                    }
                    if (surplus <= maxSurplus) {
                        records++;
                        Console.WriteLine(String.Format(
                            "RECORD q={0} h={1} a={2} r={3} count={4} target={5} surplus={6}",
                            q, h, a, r, count, target, surplus
                        ));
                    }
                }
            }
        }

        Console.WriteLine(String.Format("checked={0}", checkedRows));
        Console.WriteLine(String.Format("bad={0}", bad));
        Console.WriteLine(String.Format("records={0}", records));
        Console.WriteLine(String.Format("minSurplus={0}", minSurplus));
        Console.WriteLine(String.Format("minRow={0}", minRow));
    }
}
'@

Add-Type -TypeDefinition $code -Language CSharp
[DiagonalNonreciprocalBaseCheck]::Run($QMax, $MaxSurplus)

