param(
    [int]$HMax = 1300,
    [int]$AMax = 1100,
    [int]$MaxSurplus = -1
)

$code = @'
using System;

public static class DiagonalReciprocalBaseCheck {
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

    public static void Run(int hMax, int aMax, int maxSurplus) {
        int maxY = hMax + 2;
        int maxX = aMax + 2;

        int[,] coprimePrefix = new int[maxX + 2, maxY + 2];
        for (int p = 1; p <= maxX; p++) {
            int s = 0;
            for (int h = 1; h <= maxY; h++) {
                if (Gcd(p, h) == 1) {
                    s++;
                }
                coprimePrefix[p, h] = s;
            }
        }

        int[,] primitiveTriangle = new int[maxX + 2, maxY + 2];
        for (int x = 1; x <= maxX; x++) {
            for (int y = 0; y <= maxY; y++) {
                int total = 0;
                if (y > 0) {
                    for (int p = 1; p <= x; p++) {
                        int maxH = ((y + 1) * p - 1) / x;
                        if (maxH > y) {
                            maxH = y;
                        }
                        if (maxH > 0) {
                            total += coprimePrefix[p, maxH];
                        }
                    }
                }
                primitiveTriangle[x, y] = total;
            }
        }

        long checkedTriples = 0;
        int bad = 0;
        int records = 0;
        int minSurplus = Int32.MaxValue;
        string minRows = "";

        for (int h = 4; h < hMax; h++) {
            for (int a = 1; a < aMax; a++) {
                int maxR = Math.Min(h, a - 1);
                for (int r = 1; r <= maxR; r++) {
                    int c = h + 1 - r;
                    if (Gcd(a, r) != 1 || Gcd(a + 1, c) != 1) {
                        continue;
                    }

                    int q = h * a + r;
                    if (q < 92) {
                        continue;
                    }

                    int lower =
                        1
                        + primitiveTriangle[a, r - 1]
                        + primitiveTriangle[a + 1, h - r]
                        - coprimePrefix[a + 1, c - 1];

                    int target = Predicted(q);
                    int surplus = lower - target;
                    checkedTriples++;

                    if (surplus < minSurplus) {
                        minSurplus = surplus;
                        minRows = String.Format(
                            "h={0} a={1} r={2} q={3} lower={4} target={5} surplus={6}",
                            h, a, r, q, lower, target, surplus
                        );
                    }

                    if (surplus < 0) {
                        bad++;
                        if (bad <= 20) {
                            Console.WriteLine(String.Format(
                                "BAD h={0} a={1} r={2} q={3} lower={4} target={5} surplus={6}",
                                h, a, r, q, lower, target, surplus
                            ));
                        }
                    }
                    if (maxSurplus >= 0 && surplus <= maxSurplus) {
                        records++;
                        Console.WriteLine(String.Format(
                            "RECORD h={0} a={1} r={2} q={3} lower={4} target={5} surplus={6}",
                            h, a, r, q, lower, target, surplus
                        ));
                    }
                }
            }
        }

        Console.WriteLine(String.Format("checked={0}", checkedTriples));
        Console.WriteLine(String.Format("bad={0}", bad));
        Console.WriteLine(String.Format("records={0}", records));
        Console.WriteLine(String.Format("minSurplus={0}", minSurplus));
        Console.WriteLine(String.Format("minRows={0}", minRows));
    }
}
'@

Add-Type -TypeDefinition $code -Language CSharp
[DiagonalReciprocalBaseCheck]::Run($HMax, $AMax, $MaxSurplus)
