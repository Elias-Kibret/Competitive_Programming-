import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxSubStringLength = 0;
        HashSet<Character> lookup = new HashSet<>();

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            while (lookup.contains(currentChar)) {
                lookup.remove(s.charAt(left));
                left++;
            }

            lookup.add(currentChar);
            maxSubStringLength = Math.max(maxSubStringLength, right - left + 1);
        }

        return maxSubStringLength;
    }
}
