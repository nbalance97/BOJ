import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static String input() {
        try {
            return br.readLine().trim();
        } catch (Exception e) {}
        return null;
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(input());
        int[] cases = new int['z' - 'a' + 1];

        List<Integer> chars = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            char data = input().charAt(0);
            cases[data - 'a']++;
        }

        for (int i = 0; i < cases.length; i++) {
            if (cases[i] >= 5) {
                chars.add(i + 'a');
            }
        }

        Collections.sort(chars);
        StringBuilder sb = new StringBuilder();
        for (int ch : chars) {
            sb.append((char) ch);
        }

        if (sb.length() == 0) {
            System.out.println("PREDAJA");
            return;
        }
        System.out.println(sb.toString());
    }
}
