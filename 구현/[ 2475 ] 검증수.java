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
        String[] n = input().split(" ");
        int answer = 0;
        for (String element : n) {
            int value = Integer.parseInt(element);
            answer += value * value;
        }

        System.out.println(answer % 10);
    }
}
