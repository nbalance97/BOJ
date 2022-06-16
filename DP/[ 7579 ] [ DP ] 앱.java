import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static String input() {
        try {
            return br.readLine();
        } catch (Exception e) {}
        return null;
    }

    public static void main(String[] args) {
        List<Memory> memories = new ArrayList<>();
        StringTokenizer tokenizer = new StringTokenizer(input());
        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());
        int[] dp = new int[10001];

        StringTokenizer memoryTokenizer = new StringTokenizer(input());
        StringTokenizer costTokenizer = new StringTokenizer(input());
        while (memoryTokenizer.hasMoreTokens()) {
            Memory memory = new Memory();
            memory.bytes = Integer.parseInt(memoryTokenizer.nextToken());
            memory.cost = Integer.parseInt(costTokenizer.nextToken());
            memories.add(memory);
        }

        for (int i = 0; i < memories.size(); i++) {
            Memory memory = memories.get(i);
            for (int p = 10000; p - memory.cost > 0; p--) {
                if (dp[p - memory.cost] == 0) {
                    continue;
                }
                dp[p] = Math.max(dp[p], dp[p-memory.cost] + memory.bytes);
            }
            dp[memory.cost] = Math.max(dp[memory.cost], memory.bytes);
        }

        int answer = 0;
        for (int i = 1; i < 10001; i++) {
            if (dp[i] >= m) {
                answer = i;
                break;
            }
        }

        System.out.println(answer);
    }
}

class Memory {
    int bytes;
    int cost;

}
