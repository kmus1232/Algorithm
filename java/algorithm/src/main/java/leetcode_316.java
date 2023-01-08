import java.util.*;
import java.util.stream.Collectors;

public class leetcode_316 {

    public static String removeDuplicateLettersStack(String s) {
        int[] lastIndex = new int[26];
        for (int i = 0; i < s.length(); i++) {
            lastIndex[s.charAt(i) - 'a'] = i;
        }
        boolean[] seen = new boolean[26];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            int curr = s.charAt(i) - 'a';
            if (seen[curr])
                continue;
            while (!stack.empty() && stack.peek() > curr && lastIndex[stack.peek()] > i)
                seen[stack.pop()] = false;
            stack.push(curr);
            seen[curr] = true;
        }

        StringBuffer sb = new StringBuffer();
        while (!stack.empty()) sb.append((char) (stack.pop() + 'a'));
        return sb.reverse().toString();
    }

    public String removeDuplicateLettersUsingSet(String s) {
        if (s.isEmpty()) return s;

        SortedSet<Character> set = getSortedSet(s);
        for (Character c : set) {
            String suffix = s.substring(s.indexOf(c));
            if (getSortedSet(suffix).equals(set)) {
                return c + removeDuplicateLettersUsingSet(suffix.replace("" + c, ""));
            }
        }
        return "hello";
    }

    private static SortedSet<Character> getSortedSet(String s) {
        return new TreeSet<>(List.of(s.chars().mapToObj(c -> (char) c).toArray(Character[]::new)));
    }

    public String removeDuplicateLettersRecursive(String s) {
        if (s.isEmpty()) return s;

        int[] cnt = new int[26];
        int pos = 0;
        for (int i = 0; i < s.length(); i++) cnt[s.charAt(i) - 'a']++;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < s.charAt(pos)) pos = i;
            if (--cnt[s.charAt(i) - 'a'] == 0) break;
        }
        return s.charAt(pos) + removeDuplicateLettersRecursive(s.substring(pos).replace("" + s.charAt(pos), ""));
    }

}