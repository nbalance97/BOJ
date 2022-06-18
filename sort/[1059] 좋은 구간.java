import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static String input() {
        try {
            return br.readLine().trim();
        } catch (Exception e) {}
        return null;
    }

    public static void main(String[] args) {
        int L = Integer.parseInt(input());
        Integer[] sequence = Arrays.stream(input().split(" "))
                .mapToInt(Integer :: parseInt)
                .boxed()
                .toArray(Integer[]::new);

        int n = Integer.parseInt(input());
        int left = 0, right = 0;
        Arrays.sort(sequence);

        for (int i = 0; i < sequence.length; i++) {
            if (n == sequence[i]) {
                System.out.println(0);
                return;
            }
            if (n < sequence[i]) {
                if (i == 0) {
                    left = 1;
                    right = sequence[i]-1;
                    break;
                }
                left = sequence[i-1]+1;
                right = sequence[i]-1;
                break;
            }
        }

        int answer = 0;
        for (int i = left; i <= right; i++) {
            for (int j = i+1; j <= right; j++) {
                if (i <= n && n <= j) {
                    answer += 1;
                }
            }
        }

        System.out.println(answer);
    }
}
