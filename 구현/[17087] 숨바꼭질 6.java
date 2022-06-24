import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    private static final int DIVISOR = 1000000007;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static String input() {
        try {
            return br.readLine().trim();
        } catch (Exception e) {}
        return null;
    }

    public static void main(String[] args) {
        String[] temp = input().split(" ");
        int n = Integer.parseInt(temp[0]);
        int s = Integer.parseInt(temp[1]);
        int[] children = Arrays.stream(input().split(" "))
                .mapToInt(Integer :: parseInt)
                .map(i -> Math.abs(i - s))
                .toArray();

        int gcd = -1;

        for (int child : children) {
            if (gcd == -1) {
                gcd = child;
                continue;
            }
            gcd = GCD(gcd, child);
        }

        System.out.println(gcd);
    }

    private static int GCD(int a1, int a2) {
        BigInteger a = BigInteger.valueOf(a1);
        BigInteger b = BigInteger.valueOf(a2);

        return a.gcd(b).intValue();
    }
}
