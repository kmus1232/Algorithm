import java.util.Scanner;

public class boj_1436 {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        int N = sc.nextInt();
        int target = 1;

        while (true) {
            if (String.valueOf(target).contains("666")) {
                N -= 1;
            }
            if (N == 0) {
                break;
            }
            target += 1;
        }

        System.out.println(target);
    }
}
