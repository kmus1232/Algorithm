import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class leetcode_739 {
    public int[] dailyTemperatures(int[] temperatures) {
        int hottest = Integer.MIN_VALUE;
        int[] ans = new int[temperatures.length];
        for (int i = temperatures.length - 1; i >= 0; i--) {
            if (hottest <= temperatures[i]) {
                hottest = temperatures[i];
            } else {
                int j = i + 1;
                while (temperatures[i] >= temperatures[j]) {
                    j += ans[j];
                }
                ans[i] = j - i;
            }
        }
        return ans;
    }

    public static int[] dailyTemperaturesStack(int[] temperatures) {
        Deque<Integer> deque = new ArrayDeque<>();
        int[] ans = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!deque.isEmpty() && temperatures[deque.getLast()] < temperatures[i]) {
                int j = deque.pollLast();
                ans[j] = i - j;
            }
            deque.addLast(i);
        }
        return ans;
    }
}

