import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static String input() {
        try {
            return br.readLine().trim();
        } catch (Exception e) {}
        return null;
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(input());
        int[] sequence = Arrays.stream(input().split(" "))
                .mapToInt(Integer :: parseInt)
                .toArray();
        List<Integer> students = new ArrayList<>();
        for (int i = 0; i < sequence.length; i++) {
            students.add(students.size() - sequence[i], i+1);
        }

        for (int student : students){
            System.out.print(student + " ");
        }
    }
}
