import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
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
        String target = input();
        String[] temp = input().split(" ");
        int row = Integer.parseInt(temp[0]);
        int col = Integer.parseInt(temp[1]);
        char[][] table = new char[row][];

        for (int i = 0; i < row; i++) {
            table[i] = input().toCharArray();
        }

        int[] dx = {-1, 1, 0, 0, 1, -1, 1, -1};
        int[] dy = {0, 0, 1, -1, 1, 1, -1, -1};
        int length = target.length();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                for (int way = 0; way < dx.length; way++) {
                    String data = extract(table, dx[way], dy[way], i, j, length);
                    if (data.equals(target)) {
                        System.out.println(1);
                        return;
                    }
                }
            }
        }

        System.out.println(0);
    }

    private static String extract(char[][] table, int dx, int dy, int i, int j, int length) {
        int cx = i;
        int cy = j;
        StringBuilder sb = new StringBuilder();
        sb.append(table[cx][cy]);
        cx += dx;
        cy += dy;
        while (cx >= 0 && cx < table.length && cy >= 0 && cy < table[0].length) {
            if (sb.length() == length) {
                break;
            }
            sb.append(table[cx][cy]);
            cx += dx;
            cy += dy;
        }

        return sb.toString();
    }

}
