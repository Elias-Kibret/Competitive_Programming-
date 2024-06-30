class Solution {
    public int strStr(String haystack, String needle) {
                // Edge case: when needle is an empty string
        if (needle.isEmpty()) {
            return 0;
        }

        int lenH = haystack.length();
        int lenN = needle.length();

        // If needle is longer than haystack, it cannot be found
        if (lenN > lenH) {
            return -1;
        }

        // Loop through the haystack with a sliding window of size lenN
        for (int i = 0; i <= lenH - lenN; i++) {
            // Check if the substring starting from index i matches needle
            int j = 0;
            while (j < lenN && haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }
            if (j == lenN) {
                return i; // Match found
            }
        }

        // If needle is not found in haystack
        return -1;

        
    }
}