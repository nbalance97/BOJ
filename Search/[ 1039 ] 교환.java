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
        String[] temp = input().split(" ");

        String n = temp[0];
        int k = Integer.parseInt(temp[1]);

        int answer = bfs(n, k);
        System.out.println(answer);
    }

    private static int bfs(String n, int k) {
        Set<String> visited = new HashSet<>();
        Queue<Element> queue = new LinkedList<>();
        visited.add(n);
        queue.offer(new Element(n, 0));
        int answer = -1;
        int opCount = -1;

        while (!queue.isEmpty()) {
            Element data = queue.poll();

            if (opCount != data.opCount) {
                visited.clear();
                opCount = data.opCount;
            }

            if (data.opCount == k) {
                answer = Math.max(answer, Integer.parseInt(data.number));
                continue;
            }

            for (int i = 0; i < n.length(); i++) {
                for (int j = i+1; j < n.length(); j++) {
                    if (i == 0 && data.number.charAt(j) == '0') {
                        continue;
                    }
                    String swaped = swap(data.number, i, j);
                    if (visited.contains(swaped)) {
                        continue;
                    }
                    visited.add(swaped);
                    queue.offer(new Element(swaped, data.opCount + 1));
                }
            }
        }
        return answer;
    }

    private static String swap(String temp, int i, int j) {
        StringBuilder sb = new StringBuilder();
        sb.append(temp, 0, i);
        sb.append(temp.charAt(j));
        sb.append(temp, i+1, j);
        sb.append(temp.charAt(i));
        sb.append(temp, j+1, temp.length());

        return sb.toString();
    }

    static class Element {
        String number;
        int opCount;

        public Element(String number, int opCount) {
            this.number = number;
            this.opCount = opCount;
        }
    }
}
