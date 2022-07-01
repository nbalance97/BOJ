import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {

    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    public static String input() {
        try {
            return reader.readLine().trim();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        int answer = -1;
        String[] data = input().split(" ");
        int n = Integer.parseInt(data[0]);
        int m = Integer.parseInt(data[1]);
        Set<Integer> cases = new HashSet<>();
        Set<Integer> perfects = new HashSet<>();
        char[][] table = new char[n][];

        int p = 0;
        while (p * p < 1000000000) {
            perfects.add(p * p);
            p++;
        }

        for (int i = 0; i < n; i++) {
            table[i] = input().toCharArray();
        }

        for (int addictRow = -n; addictRow < n; addictRow++) {
            for (int addictCol = -m; addictCol < m; addictCol++) {

                if (addictRow == 0 && addictCol == 0) {
                    continue;
                }

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        StringBuilder sb = new StringBuilder();
                        int currentX = i;
                        int currentY = j;
                        while (0 <= currentX && currentX < n && 0 <= currentY && currentY < m) {
                            sb.append(table[currentX][currentY]);
                            cases.add(Integer.parseInt(sb.toString()));
                            currentX += addictRow;
                            currentY += addictCol;
                        }
                    }
                }
            }
        }

        for (Integer currentCase : cases) {
            if (perfects.contains(currentCase)) {
                answer = Math.max(answer, currentCase);
            }
        }

        System.out.println(answer);
    }
}
