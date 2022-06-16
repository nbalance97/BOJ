import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
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
        int n = Integer.parseInt(input());
        List<Shark> sharks = new ArrayList<>();
        int[] eaten = new int[n];

        Arrays.fill(eaten, -1);

        for (int i = 0; i < n; i++) {
            sharks.add(new Shark(input()));
        }

        for (int step = 0; step < 2; step++) {
            for (int i = 0; i < n; i++) {
                boolean[] visited = new boolean[n];
                dfs(visited, sharks, eaten, i);
            }
        }

        int answer = (int) Arrays.stream(eaten)
                .filter(v -> v == -1)
                .count();
        System.out.println(answer);
    }

    private static boolean dfs(boolean[] visited, List<Shark> sharks, int[] eaten, int current) {
        if (visited[current]) {
            return false;
        }

        visited[current] = true;

        for (int i = 0; i < sharks.size(); i++) {
            if (i == current) {
                continue;
            }

            Shark currentShark = sharks.get(current);
            Shark targetShark = sharks.get(i);

            if (currentShark.isSameAbility(targetShark) && current > i) {
                continue;
            }

            if (currentShark.checkEatable(targetShark)) {
                if (eaten[i] == -1 || dfs(visited, sharks, eaten, eaten[i])) {
                    eaten[i] = current;
                    return true;
                }
            }
        }
        return false;
    }
}

class Shark {
    int size;
    int speed;
    int intel;

    public Shark(String input) {
        StringTokenizer tokenizer = new StringTokenizer(input);
        this.size = Integer.parseInt(tokenizer.nextToken());
        this.speed = Integer.parseInt(tokenizer.nextToken());
        this.intel = Integer.parseInt(tokenizer.nextToken());
    }

    public boolean checkEatable(Shark shark) {
        if (shark.intel <= intel && shark.size <= size && shark.speed <= speed) {
            return true;
        }
        return false;
    }

    public boolean isSameAbility(Shark shark) {
        return shark.intel == intel && shark.size == size && shark.speed == speed;
    }
}
