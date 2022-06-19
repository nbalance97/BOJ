import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static String answer = null;
    static StringBuilder sb = new StringBuilder();
    static String[] appendix = new String[]{"1", "2", "3"};

    public static String input() {
        try {
            return br.readLine().trim();
        } catch (Exception e) {}
        return null;
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(input());
        solve(n, 0);
        System.out.println(answer);
    }

    private static void solve(int n, int i) {
        if (check(sb.toString())) {
            return;
        }

        if (n == i) {
            answer = sb.toString();
            return;
        }

        for (String addict : appendix) {
            sb.append(addict);
            solve(n, i+1);
            sb.delete(sb.length() - 1, sb.length());
            if (answer != null) {
                return;
            }
        }
    }

    public static boolean check(String data) {
        for (int i = 1; i <= data.length() / 2; i++) {
            String a1 = data.substring(data.length()-i);
            String a2 = data.substring(data.length()-2*i, data.length()-i);
            if (a1.equals(a2)) {
                return true;
            }
        }
        return false;
    }
}
