param(
    [int]$XMax = 168,
    [int]$HMax = 7800
)

$code = @'
using System;

public static class TwoTriangleSlackCheck {
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

    static int IntervalTarget(int start, int end) {
        int lo = Math.Max(start, end - 3);
        int best = 0;
        for (int n = lo; n <= end; n++) {
            int v = Predicted(n);
            if (v > best) {
                best = v;
            }
        }
        return best;
    }

    public static void Run(int xMax, int hMax) {
        int[,] prefix = new int[xMax + 1, hMax + 1];
        for (int p = 1; p <= xMax; p++) {
            int s = 0;
            for (int j = 1; j <= hMax; j++) {
                if (Gcd(p, j) == 1) {
                    s++;
                }
                prefix[p, j] = s;
            }
        }

        int[,] tri = new int[xMax + 1, hMax + 1];
        for (int x = 1; x <= xMax; x++) {
            for (int y = 0; y <= hMax; y++) {
                int total = 0;
                for (int p = 1; p <= x; p++) {
                    int maxJ = y == 0 ? 0 : ((y + 1) * p - 1) / x;
                    if (maxJ > y) {
                        maxJ = y;
                    }
                    total += prefix[p, maxJ];
                }
                tri[x, y] = total;
            }
        }

        long checkedRows = 0;
        int bad = 0;
        int minSurplus = Int32.MaxValue;
        string minRow = "";

        for (int h = 4; h <= hMax; h++) {
            for (int x = 3; x <= xMax; x++) {
                int maxR = Math.Min(h, x - 2);
                for (int r = 1; r <= maxR; r++) {
                    if (h * (x - 1) + r < 92) {
                        continue;
                    }
                    int lower = 1 + tri[x, r - 1] + tri[x, h - r];
                    int start = h * x + r;
                    int end = start + h - 1;
                    int target = IntervalTarget(start, end);
                    int surplus = lower - target;
                    checkedRows++;
                    if (surplus < minSurplus) {
                        minSurplus = surplus;
                        minRow = String.Format(
                            "h={0} X={1} r={2} lower={3} target={4} surplus={5}",
                            h, x, r, lower, target, surplus
                        );
                    }
                    if (surplus < 0) {
                        bad++;
                        if (bad <= 20) {
                            Console.WriteLine(String.Format(
                                "BAD h={0} X={1} r={2} lower={3} target={4} surplus={5}",
                                h, x, r, lower, target, surplus
                            ));
                        }
                    }
                }
            }
        }

        Console.WriteLine(String.Format("checked={0}", checkedRows));
        Console.WriteLine(String.Format("bad={0}", bad));
        Console.WriteLine(String.Format("minSurplus={0}", minSurplus));
        Console.WriteLine(String.Format("minRow={0}", minRow));
    }
}
'@

Add-Type -TypeDefinition $code -Language CSharp
[TwoTriangleSlackCheck]::Run($XMax, $HMax)

