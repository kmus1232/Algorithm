import java.util.*;

public class Memo {
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < 10; i++) {
            q.offer(i);
        }
        System.out.println(q.toString());

        while (!q.isEmpty()) {
            System.out.println(q.peek());
            System.out.println(q.poll());
        }
    }
}
