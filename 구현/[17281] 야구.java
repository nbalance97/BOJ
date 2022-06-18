import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static List<List<Integer>> permutations = new ArrayList<>();
    static boolean[] visited = new boolean[9];

    public static String input() {
        try {
            return br.readLine().trim();
        } catch (Exception e) {}
        return null;
    }

    public static void permutations(List<Integer> permutation) {
        if (permutation.size() == 8) {
            List<Integer> target = new ArrayList<>(permutation);
            target.add(3, 0);
            permutations.add(target);
        }

        for (int i = 0; i < 9; i++) {
            if (i == 0) {
                continue;
            }

            if (!visited[i]) {
                visited[i] = true;
                permutation.add(i);
                permutations(permutation);
                permutation.remove(permutation.size() - 1);
                visited[i] = false;
            }
        }
    }



    public static void main(String[] args) {
        int n = Integer.parseInt(input());
        int[][] board = new int[n][9];

        for (int i = 0; i < n; i++) {
            StringTokenizer tokenizer = new StringTokenizer(input());
            for (int j = 0; j < 9; j++) {
                board[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }

        List<Integer> list = new ArrayList<>();
        permutations(list);
        int answer = 0;
        for (List<Integer> permutation : permutations) {
            int score = 0;
            int index = 0;

            for (int inning = 0; inning < n; inning++) {
                int outCount = 0;
                boolean first = false, second = false, third = false;

                while (outCount != 3) {
                    int hitter = permutation.get(index);
                    if (board[inning][hitter] == 0) {
                        outCount += 1;
                    }
                    if (board[inning][hitter] == 1) {
                        if (third) {
                            score += 1;
                            third = false;
                        }
                        if (second) {
                            third = true;
                            second = false;
                        }
                        if (first) {
                            second = true;
                        }
                        first = true;
                    }
                    if (board[inning][hitter] == 2) {
                        if (third) {
                            score += 1;
                            third = false;
                        }
                        if (second) {
                            score += 1;
                        }
                        if (first) {
                            third = true;
                            first = false;
                        }
                        second = true;
                    }
                    if (board[inning][hitter] == 3) {
                        if (third) {
                            score += 1;
                        }
                        if (second) {
                            score += 1;
                            second = false;
                        }
                        if (first) {
                            score += 1;
                            first = false;
                        }
                        third = true;
                    }
                    if (board[inning][hitter] == 4) {
                        if (third) {
                            score += 1;
                            third = false;
                        }
                        if (second) {
                            score += 1;
                            second = false;
                        }
                        if (first) {
                            score += 1;
                            first = false;
                        }
                        score += 1;
                    }
                    index = (index + 1) % 9;
                }
            }
            answer = Math.max(answer, score);
        }

        System.out.println(answer);
    }
}
