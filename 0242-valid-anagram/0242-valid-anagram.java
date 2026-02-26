class Solution {

    public boolean isAnagram(String s, String t) {

        // ✅ Step 1: If lengths are different,
        // they can never be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // ✅ Step 2: Convert first string into character array
        // so we can sort characters
        char[] s1Char = s.toCharArray();

        // ✅ Step 3: Sort characters of first string
        Arrays.sort(s1Char);

        // ✅ Step 4: Convert second string into character array
        char[] t1Char = t.toCharArray();

        // ✅ Step 5: Sort characters of second string
        Arrays.sort(t1Char);

        // ✅ Step 6: Compare both sorted arrays character by character
        // If any mismatch exists → not an anagram
        for (int index = 0; index < s1Char.length; index++) {
            if (s1Char[index] != t1Char[index]) {
                return false;
            }
        }

        // ✅ Step 7: All characters matched → valid anagram
        return true;
    }
}