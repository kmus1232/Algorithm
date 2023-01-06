import java.util.*;
import java.util.stream.Collectors;

class leetcode_316 {


    public static String removeDuplicateLettersStack(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        Set<Character> seen = new HashSet<>();
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            cnt[c - 'a']--;
            if(seen.contains(c)) {
                continue;
            }
            while (!stack.empty() && stack.peek() > c && cnt[stack.peek() - 'a'] > 0) {
                seen.remove(stack.pop());
            }
            seen.add(c);
            stack.push(c);
        }
        return stack.stream().map(Object::toString).collect(Collectors.joining(""));
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