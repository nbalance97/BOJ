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
        String[] n = input().split(" ");
        int a = Integer.parseInt(n[0]);
        int b = Integer.parseInt(n[1]);
        int c = Integer.parseInt(n[2]);

        int[] time = new int[101];
        for (int i = 0; i < 3; i++) {
            String[] data = input().split(" ");
            int src = Integer.parseInt(data[0]);
            int dest = Integer.parseInt(data[1]);
            for (int j = src; j < dest; j++) {
                time[j]++;
            }
        }

        int answer = 0;
        for (int i = 0; i < 101; i++) {
            if (time[i] == 1) {
                answer += a;
            }
            if (time[i] == 2) {
                answer += b * 2;
            }
            if (time[i] == 3) {
                answer += c * 3;
            }
        }

        System.out.println(answer);
    }
}
