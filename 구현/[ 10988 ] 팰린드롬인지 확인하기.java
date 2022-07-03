import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;


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
        StringBuilder sb = new StringBuilder(data);
        sb.reverse();

        if (data.equals(sb.toString())) {
            System.out.println(1);
            return;
        }
        System.out.println(0);
    }
}
