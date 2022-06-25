import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
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
        char[][] board = new char[5][];
        Set<Pos> pieces = new HashSet<>();
        for (int i = 0; i < 5; i++) {
            board[i] = input().toCharArray();
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == '*') {
                    pieces.add(new Pos(i, j));
                }
            }
        }

        int distance = bfs(pieces);
        System.out.println(distance);
    }

    private static String toStr(Set<Pos> positions) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                Pos pos = new Pos(i, j);
                if (positions.contains(pos)) {
                    sb.append('*');
                    continue;
                }
                sb.append('.');
            }
        }

        return sb.toString();
    }

    private static int bfs(Set<Pos> pieces) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        Set<String> visited = new HashSet<>();
        visited.add(toStr(pieces));
        Queue<Set<Pos>> queue = new LinkedList<>();
        Queue<Integer> movement = new LinkedList<>();
        queue.offer(pieces);
        movement.offer(0);

        while (!queue.isEmpty()) {
            Set<Pos> currentPieces = queue.poll();
            int mc = movement.poll();

            if (check(currentPieces)) {
                return mc;
            }

            for (Pos pos : currentPieces) {
                for (int i = 0; i < 4; i++) {
                    Set<Pos> newSet = new HashSet<>(currentPieces);
                    Pos nextPos = new Pos(pos.x + dx[i], pos.y + dy[i]);

                    if (nextPos.validate() && !newSet.contains(nextPos)) {
                        newSet.add(nextPos);
                        newSet.remove(pos);

                        if (!visited.contains(toStr(newSet))) {
                            queue.offer(newSet);
                            movement.offer(mc + 1);
                            visited.add(toStr(newSet));
                        }
                    }
                }
            }
        }
        return 0;
    }

    private static boolean check(Set<Pos> currentPieces) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        Set<Pos> visited = new HashSet<>();
        Pos standard = currentPieces.stream().findAny().get();
        Queue<Pos> queue = new LinkedList<>();
        queue.offer(standard);
        visited.add(standard);

        while (!queue.isEmpty()) {
            Pos position = queue.poll();
            for (int i = 0; i < 4; i++) {
                Pos nextPos = new Pos(position.x + dx[i], position.y + dy[i]);
                if (currentPieces.contains(nextPos) && !visited.contains(nextPos)) {
                    queue.offer(nextPos);
                    visited.add(nextPos);
                }
            }
        }

        return visited.size() == currentPieces.size();
    }

    static class Pos {
        int x;
        int y;

        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "Pos{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }

        public boolean validate() {
            if (this.x < 0 || this.x >= 5 || this.y < 0 || this.y >= 5) {
                return false;
            }
            return true;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pos pos = (Pos) o;
            return x == pos.x && y == pos.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}
