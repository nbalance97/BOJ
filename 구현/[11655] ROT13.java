import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static String input() {
        try {
            return br.readLine().trim();
        } catch (Exception e) {}
        return null;
    }

    public static void main(String[] args) {
        String data = input();
        StringBuilder sb = new StringBuilder();

        for (char ch : data.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                int changed = ch + 13;
                if (changed > 'Z') {
                    changed = changed - ('Z'-'A'+1);
                }
                sb.append((char)changed);
                continue;
            }
            if (Character.isLowerCase(ch)) {
                int changed = ch + 13;
                if (changed > 'z') {
                    changed = changed - ('z'-'a'+1);
                }
                sb.append((char)changed);
                continue;
            }
            sb.append(ch);
        }

        System.out.println(sb.toString());
    }
}
