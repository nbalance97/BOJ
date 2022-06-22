import java.io.BufferedReader;
import java.io.InputStreamReader;
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
        int n = Integer.parseInt(input());

        int a = 0;
        int b = 1;
        int c = 1;

        if (n == 0) {
            System.out.println(0);
            return;
        }

        if (n == 1) {
            System.out.println(1);
            return;
        }

        for (int i = 2; i <= n; i++) {
            c = (a + b) % DIVISOR;
            a = b % DIVISOR;
            b = c % DIVISOR;
        }
        System.out.println(c);
    }
}
